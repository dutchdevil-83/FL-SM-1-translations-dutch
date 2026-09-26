init -1 python:
    class SMGalleryUnlockCondition(object):
        def __init__(self, images):
            self.images = images
    
        def check(self, all_prior):
            for i in self.images:
                if not renpy.seen_image(i):
                    return False
            return True

    class SMGallery(Gallery, object):
        def unlock(self, *images):
            self.unlockable.conditions.append(SMGalleryUnlockCondition(images))
    
        @staticmethod
        def start_replay(codename):
            global in_a_replay, in_a_scene
            in_a_replay = True
            in_a_scene = True
            player.add_movie_replay_history(codename)
            movie = next((v for v in sm_website_videos if v[CODENAME] == codename), None)
            character_names = movie.get("NAMES", {})
            original_names_backup = {}
            if character_names:
                for character, movie_name in character_names.items():
                    if movie_name:
                        original_names_backup[character] = character.name
                        character.name = movie_name
            setattr(renpy.store, "original_names_backup", original_names_backup)
            renpy.jump(f"{codename}_movie_replay")
    
        @staticmethod
        def end_replay():
            global in_a_replay, in_a_scene
            if in_a_replay:
                in_a_replay = False
                in_a_scene = False
                if getattr(renpy.store, "original_names_backup"):
                    for character, original_name in renpy.store.original_names_backup.items():
                        character.name = original_name
                renpy.jump("sm_website")
