    
###################REQUEST_04 (Level 02) (Touch tits's through fabric.)###############################
label new_request_04:
    $herView.hideQQ()
    m "{size=-4}(I will molest her tits a little. Won't even ask her to bare them for me. Pretty harmless stuff.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    
    
    
    if whoring <=2: # LEVEL 01 # Hermione refuses.
        jump too_much
        
    elif whoring >= 3 and whoring <= 5: # LEVEL 02 # Hermione is hesitant. 
        $ new_request_04_01 = True # Hearts.
        hide bld1
        with d3
        m "Подойди, девочка..."
        $her_head_state = 2
        her_head_main "Эм... Ладно..."
        hide screen bld1
        with d3
        
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        pause.5

        her_head_main "Sir.....?"
        menu: 
            m "..."
            "\"I'm gonna molest your tits now.\"":
                $her_head_state = 3
                her_head_main "What? What do you mean, professor--?"
                ">Hermione slightly departs ago..."
                ">You reach out swiftly and grab both of her tits through her uniform..." #WARNING_Z What the fuck?
                "- Just reach out and grab her tits. -"
                ">You reach out with both of your hands and grab the girl's tits!"
        stop music fadeout 1.0
        with hpunch
        $her_head_state = 7
        her_head_main "!!!?"
        $her_head_state = 8
        her_head_main "Professor Dumbledore?!"
        ">Hermione tries to pull away from you, but you hold her firmly by her breasts..."
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        $her_head_state = 9
        her_head_main "Professor, what are you--?"
        ">She tries to pull away again."
        ">You squeeze her tits like a vice."
        $her_head_state = 10
        her_head_main "Professor, you're hurting me!"
        g4 "Then stand still, girl!"
        $her_head_state = 11
        her_head_main "B-but...."
        m "All I want to do is squeeze your tits a little, then you will get your points!"
        $her_head_state = 12
        her_head_main "B-but..... this..."
        m "Just stand still..."
        m "go to your happy place or something..."
        $her_head_state = 11
        her_head_main "M-my happy place...?"
        ">You feel the girl's shapely breasts in your palms..."
        hide screen hermione_walk_01
        hide screen genie
        show screen ctc
        show screen bld1
        show screen chair_02 #Genie's chair.
        show screen groping_03
        with d1
        hide screen blkfade
        with d5
        pause
        $her_head_state = 13
        her_head_main "............................"
        menu:
            "-Squeeze her tits with all of your strength-":
                show screen blktone
                with d5
                ">You put strength into your hold..."
                $her_head_state = 12
                her_head_main "my............"
                ">You squeeze her tits even harder..."
                $her_head_state = 13
                her_head_main "Professor, you're hurting them..."
                m "Be quiet girl..."
                $her_head_state = 12
                her_head_main "Ау.............."
                ">You squeeze her ample tits with all your strength."
                $her_head_state = 10
                her_head_main "Ah! It hurts!"
                her_head_main "They're gonna burst! Please stop it!"
                m "They are not going to burst, you silly girl..."
                ">You losen your grip a little..."
                $her_head_state = 13
                her_head_main "It hurts..."
                m "You will be fine..."
                $her_head_state = 4
                her_head_main "........."

            "- Massaging the Breasts -":
                show screen blktone
                with d5
                ">You start massaging Hermione's beasts through her uniform..."
                $her_head_state = 13
                her_head_main "Professor...?"
                m "The points, girl... You need the points. Concentrate on that."
                $her_head_state = 4
                her_head_main "Yes..."
                $her_head_state = 15
                her_head_main "Yes, for the honour of the \"gryffindor\" house..."
                "*Squeeze-squeeze!*"
                ">You keep massaging her tits..."
                ">You give one of her breasts a few pinches trying to locate the nipple..."
                $her_head_state = 13
                her_head_main "Professor... you're pinching me...?"
                ">Your attempts prove to be fruitless though. The fabric of the uniform is quite thick..."
                $her_head_state = 15
                her_head_main "\"gryffindor\" ............"

            "-Let her go and give her the points-":
                show screen blktone
                with d5
                m "Well if you gonna make a drama out of this, you might as well leave..."
                show screen blkfade
                with d5
                ">You unhand the girl's breasts..."
                $her_head_state = 14
                her_head_main "Really?"
                m "Yes, yes... I will even give you your points..."
                her_head_main "Err... thank you, professor..."
                m "But you didn't earn them today..."
                $her_head_state = 12
                her_head_main "Aw........."

    if whoring >= 6: # LEVEL 03 and higher # Hermione doesn't mind. <============================================================================EVENT LEVEL: 03
        $ new_request_04_02 = True # Hearts.
        if whoring > 8: # LEVEL 03.
            $ new_request_04_03 = True # Hearts.
        stop music fadeout 2.0
        m "Come closer girl... I want to give your tits a massage..."
        $her_head_state = 14
        her_head_main "As you say, professor..."
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        pause.5
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        ">Hermione is starting to pull her uniform up..."
        m "No, leave it on. I want to massage them while you are fully dressed..."
        her_head_main "Oh, I see..."
        ">Hermione stands in front of you expectantly..."
        ">You reach out for her ample breasts..."
        ">And start massaging them firmly..."

        hide screen hermione_walk_01
        hide screen genie
        show screen ctc
        show screen bld1
        show screen chair_02 #Genie's chair.
        show screen groping_03
        with d1
        hide screen blkfade
        with d5
        pause

        "*squeeze-squeeze-squeeze*"
        $her_head_state = 16
        her_head_main "................"
        menu:
            "\"Do you enjoy this, girl?\"":
                $her_head_state = 14
                her_head_main "What...?"
                her_head_main "Oh, I don't mind it..."
                "*squeeze-squeeze-squeeze*"
                ">You keep massaging her soft tits..."
                $her_head_state = 16
                her_head_main "I mean, this is not a big deal, as long as I am getting paid..."
                ">You keep on massaging her tits through her uniform..."
                $her_head_state = 1
                her_head_main "A small price to pay for the honour of my house, really......{image=textheart.png}"
            "-Pull on them abruptly with force-":
                show screen blktone8
                with d3
                ">You give Hermione's tits a sudden but firm pull..."
                with vpunch
                $her_head_state = 9
                her_head_main "Ouch..."
                ">You pull on her tits again. This time much stronger."
                with vpunch
                her_head_main "Ouch! Professor, what are you trying to do...?"
                ">You jerk the girl down by her tits with all your strength..."
                with vpunch
                with vpunch
                ">Hermione almost loses balance..."
                $her_head_state = 17
                her_head_main "*Panting* What are you doing, sir...?"
                $her_head_state = 18
                her_head_main "You don't need to be so rough with me....{image=textheart.png}"
        



    if whoring <= 5:
        $ whoring +=1
        
    show screen blkfade 
    with d3
    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    hide screen bld1
    hide screen chair_02 #Genie's chair.
    hide screen groping_03
    hide screen blktone8
    show screen genie
    show screen hermione_01 #Hermione stands still.


    stop music fadeout 1.0
    ">You let go of Hermione's breasts..."
    m "This will do for now."
    $her_head_state = 4
    her_head_main "................"
    
    hide screen blkfade 
    with d3
    
    $ gryffindor +=15
    m "The \"Gryffindor\" house gets 15 points!"
    
    $ request_04_points += 1
   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    $ pos = POS_370
    $herView.showQQ( "body_29.png", pos )
    her ".................."
    her "Thank you sir..."
    if daytime:
        her "Now if you don't mind I'd better go. The classes are about to start."
    else:
        her "I'd better go now. It's getting pretty late..."
    
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5

    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###


    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
