label sm1ms015_18_first:
    if player.get_choice("io_MS015_first"):
        call sm1ms015 from _call_sm1ms015
    else:
        call sm1ms018 from _call_sm1ms018
    return
label sm1ms015_18_second:
    if player.get_choice("io_MS015_first"):
        call sm1ms018 from _call_sm1ms018_1
    else:
        call sm1ms015 from _call_sm1ms015_1
    return