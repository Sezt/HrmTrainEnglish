    
###################REQUEST_04 (Level 02) (Touch tits's through fabric.)###############################
label new_request_04:
    $herView.hideQQ()
    m "{size=-4}(I will molest her tits a little. Won't even ask her to bare them for me. Pretty harmless stuff.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $wtevent.NotFinished()
            jump new_personal_request
    
    
    
    $ current_payout = 15 #Used when haggling about price of th favor.
    if hermi.whoring <=2: # LEVEL 01 # Hermione refuses.
        jump too_much
        
    elif hermi.whoring >= 3 and hermi.whoring <= 5: # LEVEL 02 # Hermione is hesitant. 
#        $ new_request_04_01 = True # Hearts.

        hide bld1
        with d3
        m "Come on, girl..."
        $her_head_state = 2
        her_head_main "Uh... Okay..."
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
                ">Hermione slightly backs away..."
                ">You reach out swiftly and grab both of her tits through her uniform..." #WARNING_Z What the fuck?
                #"- Just reach out and grab her tits. -"
                #">You reach out with both of your hands and grab the girl's tits!"
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
        m "Go to your happy place or something..."
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
                her_head_main "Hey.............."
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

            "- Massage the Breasts -":
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

    if hermi.whoring >= 6: # LEVEL 03 and higher # Hermione doesn't mind. <============================================================================EVENT LEVEL: 03
#        $ new_request_04_02 = True # Hearts.

#        if whoring > 8: # LEVEL 03.
#            $ new_request_04_03 = True # Hearts.

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
        if this.new_request_12.IsFinished(): # Если уже играл с ее голыми сиськами
            ">Hermione is starting to pull her uniform up..."
            m "No, no need. I want to do it while you're fully dressed..."
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
                hide screen blktone8

        if hermi.whoring>=12: #If you have already played with her bare breasts
            her "Umm... Professor, maybe you'll do it for real?"
            m "Really?"
            her "Yes, I want you to... that is, it will earn me more points. You want me to lift my uniform?"
            menu:
                "Strip, Miss!":
                    m "Alright. Strip, Miss!"
                    show screen blkfade
                    with Dissolve(1)
                    pause.5

                    $ posHead = gMakePos( 390, 340 )

                    $herViewHead.showQ( "body_120.png", posHead )
                    her "Hmmph! Sir, no need to be so vulgar."
                    $herViewHead.hideQ()
                    m "You want to censor me, miss Granger, or would you rather earn points?"
                    $herViewHead.showQ( "body_66.png", posHead )
                    her "......................."
                    $herViewHead.hideQ()
                    m "So?"


                    hide screen genie
                    show screen ctc
                    #show screen chair_02 #Genie's chair.
                    hide screen genie
                    show screen genie_and_tits_01
                    with d1
                    hide screen blkfade
                    with d5
                    "> Hermione lifts her blouse and shirt."
                    $current_payout+=20
                    jump new_request_12_mainonly

                "That's all for today.":
                    show screen blkfade
                    with Dissolve(1)
                    pause.5
                    $ hermione_chibi_xpos = 400 #Near the desk.
                    hide screen bld1
#                    $herView.hideQ()
                    hide screen blktone 
                    hide screen hermione_02
                    hide screen ctc
                    hide screen bld1
                    hide screen chair_02 #Genie's chair.
                    hide screen groping_03
                    show screen genie
                    show screen hermione_01 #Hermione stands still.
                    hide screen blkfade
                    with Dissolve(1)


                    $herView.showQQ( "body_55.png", pos )
                    m "That's all for tonight, girl."
                    m "However, unless you are ready to lie down and spread your legs..."
                    if hermi.whoring<18: # If she is not ready for sex
                        $herView.showQQ( "body_05.png", pos )
                        her "Argh! Sir... how dare you!... I!..."
                        m "Hush, dear, hush. I was just kidding."
                    else:
                        $herView.showQQ( "body_103.png", pos )
                        her "I... I agree, Professor."
                        g9 "I did not doubt that you would."
                        $herView.showQQ( "body_120.png", pos )
                        her "Not just that Professor, its points to the house, proud \"Gryffindor\"!"
                        m "Yes, the same old song."
                        $herView.showQQ( "body_51.png", pos )
                        her "Argh! Sir... how dare you!... I!..."
                        m "Alright, miss Granger, I was joking about spreading your legs. No need for your advances."

                    if not end.IsEnding(const_ENDING_STRONG_GIRL):
                        $herView.showQQ( "body_120.png", pos )
                        her "GRR!... Pay me and I'll go!"
                        $hermi.liking -=30
                        jump new_request_04_finish
                    else:
                        $music.Start("Supergirl")                                   
                        $herView.showQQ( "body_50.png", pos )
                        her "These jokes of yours, Professor..."
                        $herView.showQQ( "body_61.png", pos )
                        her "................................"
                        $herView.showQQ( "body_69.png", pos )
                        her "................................"
                        m "What?"
                        $herView.showQQ( "body_29.png", pos )
                        her "I was thinking that maybe..."
                        m "Really?"
                        $herView.showQQ( "body_56.png", pos )
                        her "Maybe I could..."
                        m "Could what?"
                    if hermi.whoring<18: # Если не готова к сексу
                        $herView.showQQ( "body_123.png", pos )
                        her "Well, as you said, advance... If this is it...it should be paid, of course!"
                        g9 "Of course, it should. Of course!" 
                    else:
                        $herView.showQQ( "body_123.png", pos )
                        her "Well, as you said, advance...for free...."
                        $herView.showQQ( "body_64.png", pos )
                        her "Don't think about it, just{size=+4} do {/size} it..."
                        g9 "Well, finally I have taken over your mind, girl!"

                    g9 "Well then, come here, take off your panties..."
                    $herView.showQQ( "body_80.png", pos )
                    her "Easy, Professor, easy, don't get excited!.. I was also {size=+4}JOKING{/size}!"
                    g4 "...................."
                    g4 "Oh, you shallow bitch!"
                    $herView.showQQ( "body_100.png", pos )
                    her "Yes, sir! And now I want to get my points."
                    menu:
                        "Out!":
                            m "Get out of here! No points for you!"
                            $herView.showQQ( "body_05.png", pos )
                            her2 "As you will not keep your word, sir, I will not come to you."
                            $hermi.liking -=50
                            jump new_request_04_nopoints
                        "Well, here you are!":
                            m "Well, miss Granger, you get your points."
                            m "But next time a joke like that will deduct points, not add."
                            m "You can't make a fool of me."
                            $herView.showQQ( "body_58.png", pos )
                            her "Quite, sir."
                            her2 "But if so, Professor, I will have to be silent, like a mouse. Afraid that I might say the wrong thing."
                            m "It's for the best, miss Granger."
                            $herView.showQQ( "body_129.png", pos )
                            her2 "How am I going to report to you, Professor?.. But of course, I will do as you say."
                            "> Hermione is going to leave."
                            m "Well, miss Granger, this time I forgive you. But I warn you - watch your tongue!"
                            $herView.showQQ( "body_84.png", pos )
                            her "Of course, Professor!"



    label new_request_04_finish:

    if hermi.whoring <= 5:
        $ hermi.whoring +=1
        
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
    show screen genie
    show screen hermione_01 #Hermione stands still.


    stop music fadeout 1.0
    if hermi.whoring<12: # Если еще не играл с ее голыми сиськами
        ">You let go of Hermione's breasts..."
        m "This will do for now."
        $her_head_state = 4
        her_head_main "................"
    else:
        $music()
    
    hide screen blkfade 
    with d3
    
    $ gryffindor +=current_payout
    m "The \"Gryffindor\" house gets [current_payout] points!"
    
#    $ request_04_points += 1
   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    $ pos = POS_370
    if current_payout==35:
        $herView.showQQ( "body_05.png", pos )
        her "Wait, sir!"
        her "Why 35 points? 15 and 35 provide is a total of 50!"
        m "No, miss Granger. 35 for this service. Total amount is 35!"
        $herView.showQQ( "body_76.png", pos )
        her "Sir, with all due respect! Touching through the uniform is worth 15 points and topless 35!"
        her "Don't try to cheat me!"
        m "Miss Granger, I agreed with you and allowed you to go topless..."
        m "...and giving 35 points instead of the promised 15. And now you want more!"
        m "No wonder they say, good deeds do not go unpunished..."
        her "Good deeds, sir?! We agreed that..."
        m "Agreed? Did we agree that you would sell me two services at a time?"
        $herView.showQQ( "body_66.png", pos )
        her "No, but..."
        m "If you had discussed this with me..."
        her "I wanted to, but..."
        m "That \"but\"? You liked it so much that you forget about everything?" 
        $herView.showQQ( "body_88.png", pos )
        her "No! No way!"
        m "Whatever, miss Granger, the decision is final. 35 points and not a point more!" 
        $herView.showQQ( "body_86.png", pos )
        her "It's not fair, sir!"
        $hermi.liking -=15
    else:
        $herView.showQQ( "body_29.png", pos )
        her ".................."
        her "Thank you sir..."
        if daytime:
            her "Now if you don't mind I'd better go. The classes are about to start."
        else:
            her "I'd better go now. It's getting pretty late..."
    
    label new_request_04_nopoints:
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

    $SetHearts(GetStage(hermi.whoring, 3, 4, 3))

    $wtevent.Finalize()    

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
