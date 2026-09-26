init python:
    def sm1ms026_2_vn_block_condition():
        if not player.is_storyline_item_finished(MS, "sm1ms027"):
            return (False, _("Progress Main Story first"))
    
        if player.get_choice("first_movie") == "pirates_movie":
            ns_progress = player.has_played_scene("sm1cs_ns014")
            mes_progress = player.has_played_scene("sm1cs_mes007")
            mh_progress = player.has_played_scene("sm1cs_mh010")
            if not ns_progress and not (mes_progress or mh_progress):
                return (False, _("Progress Nari and Min or Lyssa's story first"))
            if not ns_progress and mes_progress and not mh_progress:
                return (False, _("Progress Nari's story first"))
            if not ns_progress and mh_progress and not mes_progress:
                return (False, _("Progress Nari's story first"))
            if ns_progress and not (mes_progress or mh_progress):
                return (False, _("Progress Min or Lyssa's story first"))
    
        if player.get_choice("first_movie") == "scifi_movie":
            if not player.is_storyline_item_finished(TL_STORY, "sm1cs_tl007"):
                return (False, _("Progress Tiasia's story first"))
    
        return (True, None)
