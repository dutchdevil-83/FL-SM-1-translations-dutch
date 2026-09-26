import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('voice_profiles', ROOT / 'tools/voice_profiles.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class VoiceProfilesTests(unittest.TestCase):
    def setUp(self):
        self.registry = MODULE.load_json(ROOT / 'voice/characters.json')
        self.sources = MODULE.load_json(ROOT / 'voice/character_sources.json')

    def test_registry_is_valid_and_all_tokens_have_profiles(self):
        MODULE.validate_registry(self.registry, self.sources)
        self.assertEqual(len(self.registry['characters']), 59)

    def test_narrator_profile_uses_direct_source_evidence(self):
        narrator = self.registry['characters']['narrator']
        self.assertTrue(narrator['enabled'])
        self.assertEqual(narrator['profile']['identity_status'], 'direct_source_supported')
        self.assertEqual(narrator['profile']['evidence_ids'], [])
        self.assertTrue(narrator['profile']['direct_source_evidence'])
        MODULE.validate_registry(self.registry, self.sources)

    def test_manifest_audit_allows_profiles_from_other_game_versions(self):
        registry = copy.deepcopy(self.registry)
        registry['characters']['narrator']['line_count'] = 99
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / 'dialogue.jsonl'
            manifest.write_text(
                json.dumps({
                    'id': 'narrator_test',
                    'speaker': 'narrator',
                    'source_file': 'original-source/game/code/data/characters/names.rpy',
                    'source_line': 1,
                    'review_reasons': [],
                }) + '\n',
                encoding='utf-8',
            )
            audit, evidence = MODULE.audit_manifest(registry, manifest)
        self.assertIn('ag', audit['inactive_profile_tokens'])
        self.assertEqual(audit['speaker_line_counts']['narrator'], 1)
        self.assertEqual(audit['profile_line_count_drift']['narrator']['canonical_source'], 1)
        self.assertTrue(evidence['narrator'])

    def test_nari_age_is_fact_but_other_casting_ages_are_not(self):
        chars = self.registry['characters']
        self.assertEqual(chars['ns']['profile']['canonical_age_years'], 21)
        self.assertIsNone(chars['dvh']['profile']['canonical_age_years'])
        self.assertEqual(chars['dvh']['language_code'], 'en-US')
        self.assertEqual(chars['dvh']['profile']['accent_basis'], 'explicit_dialogue')

    def test_aliases_resolve_to_one_protagonist(self):
        for speaker in ('mct', 'mo'):
            self.assertEqual(MODULE.resolve_identity(self.registry['characters'], speaker), 'mc')
            with self.assertRaises(ValueError):
                MODULE.design_request(self.registry, speaker, 'gemini-3.8-flash-tts')

    def test_unresolved_bindings_do_not_create_requests(self):
        for speaker in ('mhmes', 'sbf', 'ed', 'ef', 'ic', 'zh'):
            self.assertFalse(self.registry['characters'][speaker]['enabled'])
            with self.assertRaises(ValueError):
                MODULE.design_request(self.registry, speaker, 'gemini-3.8-flash-tts')

    def test_request_contains_only_documented_creation_fields(self):
        request = MODULE.design_request(self.registry, 'ns', 'gemini-3.8-flash-tts')
        self.assertEqual(set(request), {'store', 'voice'})
        self.assertEqual(set(request['voice']), {'model', 'type', 'display_name', 'gender', 'language_code', 'prompted',
                         'accent', 'context', 'description', 'persona', 'pitch', 'region_code'})
        self.assertEqual(set(request['voice']['prompted']), {'input'})
        self.assertNotIn('canonical_age_years', json.dumps(request))
        self.assertNotIn('sample_audio', request['voice'])
        self.assertNotIn('id', request['voice'])

    def test_cycle_is_rejected(self):
        self.registry['characters']['mc']['voice_ref'] = 'mct'
        with self.assertRaises(ValueError):
            MODULE.validate_registry(self.registry, self.sources)

    def test_disabled_reference_is_rejected(self):
        self.registry['characters']['mc']['enabled'] = False
        with self.assertRaises(ValueError):
            MODULE.validate_registry(self.registry, self.sources)

    def test_dutch_voice_locale_is_rejected(self):
        self.registry['characters']['dvh']['language_code'] = 'nl-NL'
        with self.assertRaises(ValueError):
            MODULE.validate_registry(self.registry, self.sources)

    def test_unknown_model_is_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.design_request(self.registry, 'ns', 'invented-tts-model')

    def test_distinct_characters_cannot_silently_share_one_voice(self):
        self.registry['characters']['ns']['voice_id'] = 'voice_test'
        self.registry['characters']['sy']['voice_id'] = 'voice_test'
        with self.assertRaises(ValueError):
            MODULE.validate_registry(self.registry, self.sources)

    def test_request_export_preserves_an_approved_identity(self):
        self.registry['characters']['ns']['voice_id'] = 'voice_test_existing'
        self.registry['characters']['ns']['casting_status'] = 'approved'
        before = copy.deepcopy(self.registry)
        request = MODULE.design_request(self.registry, 'ns', 'gemini-3.8-flash-tts')
        self.assertEqual(before, self.registry)
        self.assertNotIn('id', request['voice'])
        self.assertNotIn('casting_status', request['voice'])

    def test_accent_region_metadata_is_separate_from_spoken_language(self):
        for speaker, accent, region in (('dvh', 'Dutch', 'NL'), ('ns', 'South Korean', 'KR')):
            voice = MODULE.design_request(self.registry, speaker, 'gemini-3.8-flash-tts')['voice']
            self.assertEqual(voice['accent'], accent)
            self.assertEqual(voice['region_code'], region)
            self.assertEqual(voice['language_code'], 'en-US')
            self.assertEqual(voice['context'], 'Conversational')
            self.assertIn(voice['pitch'], {'low', 'medium', 'high'})

    def test_readonly_and_replication_fields_never_leak_into_prompted_request(self):
        self.registry['characters']['ns']['sample_audio'] = 'not-an-input'
        self.registry['characters']['ns']['expire_time'] = 'not-an-input'
        self.registry['characters']['ns']['replicated'] = {'source_audio': 'not-an-input'}
        voice = MODULE.design_request(self.registry, 'ns', 'gemini-3.8-flash-tts')['voice']
        for field in ('id', 'key', 'sample_audio', 'expire_time', 'usage', 'replicated'):
            self.assertNotIn(field, voice)

    def test_export_removes_stale_request_for_a_blocked_identity(self):
        characters = self.registry['characters']
        evidence = {speaker: [] for speaker in characters}
        audit = {'speaker_tokens': len(characters), 'dialogue_rows': 0,
                 'untokenized_rows': 0, 'unresolved_dialogue': []}
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory)
            (destination / 'requests').mkdir()
            (destination / 'requests/ed.json').write_text('{}')
            MODULE.export_profiles(self.registry, self.sources, audit, evidence,
                                   destination, 'gemini-3.8-flash-tts')
            self.assertFalse((destination / 'requests/ed.json').exists())
            self.assertEqual(len(list((destination / 'profiles').glob('*.json'))), 59)
            self.assertEqual(len(list((destination / 'requests').glob('*.json'))), 51)

    def test_unmapped_accent_is_not_silently_replaced_by_american(self):
        self.registry['characters']['ns']['profile']['accent'] = 'another accent'
        with self.assertRaises(ValueError):
            MODULE.design_request(self.registry, 'ns', 'gemini-3.8-flash-tts')

    def test_creation_count_excludes_aliases_and_review_queue(self):
        available = [key for key, value in self.registry['characters'].items() if value['enabled'] and not value['voice_ref']]
        self.assertEqual(len(available), 51)
        prompts = {self.registry['characters'][key]['design_prompt'] for key in available}
        self.assertEqual(len(prompts), len(available))


if __name__ == '__main__':
    unittest.main()
