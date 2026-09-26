image sm1cs_tl-pee01-a01-1 = Movie(play="images/FS_T/TL/tlpee01/sm1cs-tlpee01-a01-1-4x-60fps.webm", start_image="sm1cs-tlpee01-a01-1 tl-peeing-toilet-anim-000", image = "sm1cs-tlpee01-a01-1 tl-peeing-toilet-anim-189", loop = False)
image sm1cs_tl-pee01-a01-2 = Movie(play="images/FS_T/TL/tlpee01/sm1cs-tlpee01-a01-2-4x-60fps.webm", start_image="sm1cs-tlpee01-a01-2 tl-peeing-toilet-anim-000", image = "sm1cs-tlpee01-a01-2 tl-peeing-toilet-anim-189", loop = False)
label sm1cs_tl_pee01:
    scene sm1cs-tlpee01-a01-1 tl-peeing-toilet-anim-000
    pause 0.75
    play sound sfx_piss_tlpee01
    play voice3 girl24_sex_closedmoan1 noloop
    scene sm1cs_tl-pee01-a01-1
    pause 13.2
    scene sm1cs-tlpee01-a01-2 tl-peeing-toilet-anim-000
    pause 0.75
    play sound sfx_piss_tlpee01
    play voice3 girl24_sex_closedmoan3 noloop
    scene sm1cs_tl-pee01-a01-2
    pause 13.2
    pause
    stop sound fadeout 1.0
    $ gt.add(0,15,0)
    return