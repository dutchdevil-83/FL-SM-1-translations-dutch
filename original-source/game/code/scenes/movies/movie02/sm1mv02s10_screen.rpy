screen sm1mv02s10_credit_roll():
    style_prefix "sm1mv02s10_credit_roll"

    add "images/MV/mv02/s10/sm1mv02s010-107 credits-roll_back.webp"
    vbox:
        xalign 0.5
        spacing 500
        at credits_roll_effect
        null height 550
        vbox:
            text "Captain Ramses Hornstar" style "sm1mv02s10_credit_role"
            text f"{mcname} Young" style "sm1mv02s10_credit_name"
        vbox:
            text "Commander Luffie Orion" style "sm1mv02s10_credit_role"
            if persistent.is_special:
                text "Stacy Young" style "sm1mv02s10_credit_name"
            else:
                text "Stacy Brown" style "sm1mv02s10_credit_name"
        vbox:
            text "Doctor Jalerra" style "sm1mv02s10_credit_role"
            text "Nari Nutlicker" style "sm1mv02s10_credit_name"
        vbox:
            text "Commander Vel Spectre" style "sm1mv02s10_credit_role"
            if player.get_choice("sm1mv02s02_recruit_mes"):
                text "Swizzel (Min Eun-Soo)" style "sm1mv02s10_credit_name"
            else:
                text "Kandy Serpent (Lyssa Harris)" style "sm1mv02s10_credit_name"
        vbox:
            text "Lieutenant Kira Solo" style "sm1mv02s10_credit_role"
            text "Taisia Linqvist" style "sm1mv02s10_credit_name"
        vbox:
            text "Director of Photography" style "sm1mv02s10_credit_role"
            text "Kanya Vu" style "sm1mv02s10_credit_name"
        vbox:
            text "Writing" style "sm1mv02s10_credit_role"
            text f"{mcname} Young" style "sm1mv02s10_credit_name"
        vbox:
            text "Second Grip" style "sm1mv02s10_credit_role"
            text "Taisia Linqvist" style "sm1mv02s10_credit_name"
        vbox:
            text "Sets" style "sm1mv02s10_credit_role"
            text f"{mcname} Young" style "sm1mv02s10_credit_name"
        null height 1080
    add "images/MV/mv02/s10/sm1mv02s010-107 credits-roll_front.webp"
transform credits_roll_effect:
    subpixel True
    yalign 0.0
    linear 71.0 yalign 1.0
style sm1mv02s10_credit_roll_vbox xalign 0.5 spacing 20
style sm1mv02s10_credit_role:
    font "fonts/mr-amazin-regular-type.otf"
    size 50
    color "#000000"
    xalign 0.5
style sm1mv02s10_credit_name:
    font "fonts/mr-amazin-regular-type.otf"
    size 45
    color "#000000"
    xalign 0.5