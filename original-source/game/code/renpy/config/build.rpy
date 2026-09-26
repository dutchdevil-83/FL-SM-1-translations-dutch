init 1 python:
    build.classify("**~"                    , None)
    build.classify("**.bak"                 , None)
    build.classify("**.bat"                 , None)
    build.classify("**.rar"                 , None)
    build.classify("**.psd"                 , None)
    build.classify("**/.**"                 , None)
    build.classify("**/#**"                 , None)
    build.classify("**/thumbs.db"           , None)
    build.classify("**/desktop.ini"         , None)


    build.classify("game/**.rpy"            , None)


    build.classify("game/cache/*.rpyb"      , None)


    build.classify("game/**/debug/**"       , None)
    build.classify("game/**/unused/**"      , None)


    build.classify("game/**.py"             , None)
    build.classify("game/**.pyc"            , None)
    build.classify("game/tl/**.txt"         , None)


    build.classify("game/saves/persistent"  , None)
    build.classify("game/saves/*.save"      , None)


    build.classify("game/**.md"             , None)
    build.classify("game/tl/media/**"       , None)


    build.classify("game/audio/**/orig/**"  , None)
    build.classify("game/audio/**/wav/**"   , None)
    build.classify("game/audio/**/test/**"  , None)
    build.classify("game/audio/**/unused/**", None)




    build.classify("game/images/bonus/**"  , None)


    if is_steam_edition or is_DLC_included is False:
        build.classify("game/**/hints.rpy"  , None)
        build.classify("game/**/hints.rpyc" , None)


    build.archive("code"                    , "all")
    if only_build_code is False:
        build.archive("images"                  , "all")
        build.archive("audio"                   , "all")
        build.archive("video"                   , "all")
        build.archive("fonts"                   , "all")


    build.classify("game/**.rpyc"           , "code")

    if only_build_code is False:
    
        build.classify("game/**.webp"           , "images")
        build.classify("game/**.png"            , "images")
        build.classify("game/**.jpg"            , "images")
    
    
        build.classify("game/**.ogg"            , "audio")
        build.classify("game/**.mp3"            , "audio")
        build.classify("game/**.wav"            , "audio")
    
    
        build.classify("game/**.mp4"            , "video")
        build.classify("game/**.avi"            , "video")
        build.classify("game/**.webm"           , "video")
    
    
        build.classify("game/**.ttf"            , "fonts")
        build.classify("game/**.otf"            , "fonts")
    else:
    
        build.classify("game/**.webp"           , None)
        build.classify("game/**.png"            , None)
        build.classify("game/**.jpg"            , None)
        build.classify("game/**.ogg"            , None)
        build.classify("game/**.mp3"            , None)
        build.classify("game/**.wav"            , None)
        build.classify("game/**.mp4"            , None)
        build.classify("game/**.avi"            , None)
        build.classify("game/**.webm"           , None)
        build.classify("game/**.ttf"            , None)
        build.classify("game/**.otf"            , None)
