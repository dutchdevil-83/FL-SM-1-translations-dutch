label sm1cs_mh005i:
    scene sm1cs-mh005i-01 mc-knock_c1
    pause(0.3)
    play sound sfx_knock_wood1
    scene sm1cs-mh005i-02 mc-knock_c1
    pause(0.1)
    scene sm1cs-mh005i-01 mc-knock_c1
    pause(0.1)
    scene sm1cs-mh005i-02 mc-knock_c1
    pause(0.1)
    scene sm1cs-mh005i-01 mc-knock_c1
    pause(0.1)
    scene sm1cs-mh005i-02 mc-knock_c1
    pause(0.1)
    scene sm1cs-mh005i-01 mc-knock_c1
    pause(0.1)
    scene sm1cs-mh005i-02 mc-knock_c1
    pause(2)
    scene sm1cs-mh005i-03 mc-waiting_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mct "Huh, I guess Lyssa isn't home..."
    mct "I'll just send her a text..."
    play sound sfx_message_out1 volume 1.5
    scene sm1cs-mh005i-04 mc-texting_c1 with dissolve
    mct "Hey, Lyssa, are you free tonight?"
    mct "..."
    play sound sfx_message_in1
    scene sm1cs-mh005i-06 mc-texting-smile_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mct "Awesome! She's free!"
    scene sm1cs-mh005i-05 mc-texting-thinking_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "What would a cool guy send next..."
    mct "Just the address, yeah... Be all mysterious like."
    scene sm1cs-mh005i-06 mc-texting-smile_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mct "Cool, I should get moving - have to make sure I beat Lyssa to the arcade!"
    scene black with fade
    $ StoryController.end_scene(MH_STORY, 0, 15, 0)
    return