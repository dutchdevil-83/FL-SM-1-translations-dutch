image sm1cs_ns-pee01-a01-1 = Movie(play="images/FS_IT/NS/nspee01/sm1cs-nspee01-a01-1-4x-60fps.webm", start_image="sm1cs-nspee01-a01-1 ns-peeing-toilet-anim-000", image = "sm1cs-nspee01-a01-1 ns-peeing-toilet-anim-180", loop = False)
image sm1cs_ns-pee01-a01-2 = Movie(play="images/FS_IT/NS/nspee01/sm1cs-nspee01-a01-2-4x-60fps.webm", start_image="sm1cs-nspee01-a01-2 ns-peeing-toilet-anim-000", image = "sm1cs-nspee01-a01-2 ns-peeing-toilet-anim-180", loop = False)
image sm1cs_ns-pee01-a02-1 = Movie(play="images/FS_IT/NS/nspee01/sm1cs-nspee01-a02-1-4x-60fps.webm", start_image="sm1cs-nspee01-a02-1 ns-peeing-toilet-anim-000", image = "sm1cs-nspee01-a02-1 ns-peeing-toilet-anim-180", loop = False)
label sm1cs_ns_pee01:
    scene sm1cs-nspee01-a01-1 ns-peeing-toilet-anim-000
    pause 0.75
    play sound sfx_piss_nspee01
    play voice3 nari_sex_closedmoan1 noloop
    scene sm1cs_ns-pee01-a01-1
    pause 13.2
    scene sm1cs-nspee01-a01-2 ns-peeing-toilet-anim-000
    pause 0.75
    play sound sfx_piss_nspee01
    play voice3 nari_sex_closedmoan2 noloop
    scene sm1cs_ns-pee01-a01-2
    pause 13.2
    scene sm1cs-nspee01-a02-1 ns-peeing-toilet-anim-000
    pause 0.75
    play voice3 nari_sex_closedmoan3 noloop
    play sound sfx_piss_nspee01
    scene sm1cs_ns-pee01-a02-1
    pause 13.2
    pause
    stop sound fadeout 1.0
    $ gt.add(0,15,0)
    return