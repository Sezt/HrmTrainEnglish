###################REQUEST_02 (Level 01)
label new_request_02: #SHOW ME YOUR Трусики
    $herView.hideQQ()
    $ pos = POS_370
    m "{size=-4}(I will ask her to show me her panties. Plain and simple.){/size}"
    $ menu_x = 0.5 #Default menu position restored.
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request
    $herView.showQQ( "body_01.png", pos )
    her "So, what will it be sir?"
    m "Nothing drastic, really..."
    m "I just want you to show me your panties."               

    if IsFirstRun() and whoring <= 5: #First time this event taking place. and LEVEL 02.  
#    if request_02 == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.  
#        $ new_request_02_01 =  True #Hearts.
        $SetHearts(1)

        $herView.hideshowQQ( "body_14.png", pos )
        her "My... panties...?"
        $herView.hideshowQQ( "body_47.png", pos )
        her  "Professor Dumbledore!"
        m "I know, I know, this a little weird..."
        $herView.hideshowQQ( "body_48.png", pos )
        her  " {size=+7}A little !?{/size}"
        her "This is completely inappropriate!"
        m "Listen, we need to go through this phase before we get to the good stuff, alright?"
        $herView.hideshowQQ( "body_31.png", pos )
        her  "The \"good stuff\"? Professor I don't understand..."
        m "What don't you understand, miss Granger?"
        m "Do you need these points or not?"
        $herView.hideshowQQ( "body_31.png", pos )
        her  "I do..."
        m "Lift up your skirt then..."
        $herView.hideshowQQ( "body_47.png", pos )
        her "............."
    else:
        if IsNextRun(): #First time this event taking place. and LEVEL 02.  
#        if request_02 >= 1: #Not the first time
            $herView.hideshowQQ( "body_29.png", pos )
            her "Oh... again?"
            m "Just do it..."
        $herView.hideshowQQ( "body_29.png", pos )
        her ".................."
        
        
    $ current_payout = 5 #Used when haggling about price of th favor.

    hide screen bld1
    $herView.hideQ( d5 )
    $ menu_x = 0.5 #Default menu position restored.
    if whoring <= 2:    #angry with pants
        show screen hermione_lift_skirt_angry
        with d3
    elif whoring <= 5:
        show screen hermione_lift_skirt_normal #Hermione lifts her skirt WITH pants
        with d3
    elif whoring >=6 and whoring<13:  # no panties
        show screen hermione_lift_skirt_no_panties
        with d3
    else: 
        pass
        
        
    #play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 

    if whoring >= 0 and whoring <= 2: #LEVEL 01
        $her_head_state = 8
        her_head_main "........................"
    elif whoring >= 3 and whoring <= 5: #LEVEL 02
        $her_head_state = 14
        her_head_main "....................."
    elif whoring >= 6 and whoring<13: #LEVEL 03 and up.
        $her_head_state = 18
        her_head_main ".........................."
        g4 "!!?"

        
        

    # save previous state and add pose
    # add pose with lifted skirt
    if whoring<13:
        $herView.data().saveState()
        $herView.data().addPose( CharacterExItemSkirtLifted( herView.mPoseFolder, 'pose_skirt_up.png', G_Z_POSE ) )
        $ pos = POS_120
    
    if whoring >= 0 and whoring <= 2: #LEVEL 01   <============================= Fist event.
#        $ new_request_02_01 =  True #Hearts.
#        SetHearts(1)

        show screen bld1
        with d3
        show screen blktone
        with d3
        $herView.showQ( "body_49.png", pos )
        show screen ctc
        with d3
        pause
        
        her "....................."
        menu:
            "-Stare at her face-":
                ">You study Hermione's face..."
                pause
                ">You wonder what's going through her mind right now."
                $herView.hideshowQQ( "body_51.png", pos )
                her "......................."
                pause
            "-Stare at her panties-":
                ">That's a plain girlish underwear..."
                pause
                $herView.hideshowQQ( "body_51.png", pos )
                her "......................."
               

    elif whoring >= 3 and whoring <= 5: #LEVEL 02  <====================================================================== SECOND EVENT!
#        $ new_request_02_02 =  True #Hearts.
        $SetHearts(2)

        show screen bld1
        with d3
        show screen blktone
        with d3
        $herView.showQ( "body_52.png", pos )
        show screen ctc
        with d3
        pause
        her "Here, professor..."
        menu:
            "\"You don't look too embarrassed...\"":
                $herView.hideshowQQ( "body_53.png", pos )
                her "That's not true..."
                $herView.hideshowQQ( "body_54.png", pos )
                her "But this is a small price to pay if the \"Gryffindors\" keep the cup this year."
                her "I know everyone will be so happy..."
                pause
            "\"I like your panties...\"":
                $herView.hideshowQQ( "body_53.png", pos )
                her "Thank you, professor..."
            "-Keep looking into her eyes-":
                $herView.hideshowQQ( "body_55.png", pos )
                her ".............................."
                her "...........................?"
                $herView.hideshowQQ( "body_56.png", pos )
                her "................................"
                $herView.hideshowQQ( "body_57.png", pos )
                her "Professor, please... You are embarrassing me."
                

    elif whoring >= 6 and whoring<13: #LEVEL 04 and up. <====================================================================== FINAL EVENT! (No Трусики).
#        $ new_request_02_03 =  True #Hearts.
        $SetHearts(3)

        show screen bld1
        with d3
        show screen blktone
        with d3
        
        # we should remove panties from hermi in this event
        $herView.data().delPanties()
        
        $herView.showQ( "body_58.png", pos )
        show screen ctc
        with d3
        pause
        g4 "Where are your panties, miss Granger?"
        $herView.hideshowQQ( "body_59.png", pos )
        her "Oh, lately I just don't feel like wearing them..."
        menu:
            "\"You little slut!\"":
                her "Hm..."
                $herView.hideshowQQ( "body_58.png", pos )
                her "I suppose I am..."
                her "Do I get extra points for that?"
                menu:
                    "\"Absolutely!\"":
                        m "Absolutely!"
                        $ gryffindor +=10
                        m "Ten points to \"Gryffindor\"!" 
                        $herView.hideshowQQ( "body_60.png", pos )
                        her "Thank you, sir!"
                    "\"Absolutely not!\"":
                        $ mad +=15
                        $herView.hideshowQQ( "body_61.png", pos )
                        her ".............................."
                        $herView.hideshowQQ( "body_62.png", pos )
                        her "Then I don't appreciate you being mean to me, professor."   
            "\"Good! Five points!\"":
                pass           
    elif whoring >= 13: #Хотя бы один раз дрочила
        $herView.hideshowQQ( "body_12.png", pos )
        her "Sir, you really called me here because of these accidents 5 points?"
        her "I feel sorry for wasting time on such a service. This is for year students, sir!"
        m "Really?"
        her "\"Show panties for 5 points\". It is ridiculous!"
        $herView.hideshowQQ( "body_10.png", pos )
        her "Maybe we'll go do something .... um ... interesting?"
        her "In a sense, giving more points?"
        menu: 
            "\"And what you want to do?\"":
                m "And what do you want, Miss Granger?"
                $herView.hideshowQQ( "body_68.png", pos )
                her "I do not know, sir. There are different options!"
                jump new_personal_request
            "\"Since when did you become to choose their assignments, Miss Granger?":
                $ SetHearts(4)
                m "Since when did you become to choose their assignments, Miss Granger?"
                m "This seems to be here, I decide which service is paid."
                m "So, today paid showing your panties!"
                $herView.hideshowQQ( "body_202.png", pos )
                her "Excuse me, sir! Of Course."
                m "And?"
                her "Here it is, professor."
                $herView.hideshowQQ( "body_111.png", pos )
                "> Hermione pulled out his pants and shows them to you."
                g4 "What a...?!"
                her "My panties, sir. I show them to you, as you requested."
                m "Are you kidding?"
                $herView.hideshowQQ( "body_53.png", pos )
                her "Sir?"
                m "I expect to see the underwear that on you!"
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ah! So it is not, sir. Today I go without panties."
                m "Well, then show me!"
                $herView.hideshowQQ( "body_31.png", pos )
                her "With all due respect, sir, it's an almost striptease. So, it is worth a lot more than five points!"
                $herView.hideshowQQ( "body_128.png", pos )
                her "So, count..."
                her "Guys want to see pussy girls more than anything else..."
                her "Let pussy - 2/3 of the total striptease..."
                $herView.hideshowQQ( "body_101.png", pos )
                her "2/3 of 35 points is 23 ... and three in the period, sir."
                her "Only out of respect for you is rounded down."
                $herView.hideshowQQ( "body_53.png", pos )
                her "Gets 20 points! Here, it will be fair."
                menu: 
                    "\"No!\"":
                        m "You're free, Miss Granger!"
                        $herView.hideshowQQ( "body_58.png", pos )
                        her "As you say, sir. In that case, I would like to receive your payment."
                    "\"Well, another 20 points. Show me!":
                        $current_payout+=20
                        m "Okay, I'll pay you 20 points. Show me!"
                        $herView.hideshowQQ( "body_186.png", pos )
                        her "25 points, sir."
                        g4 "?!"
                        her "20 for pussy and 5 for the panties, which I have already shown, sir. Total 25."
                        m "Miss Granger, you are trading on the market, you have lost all sense of shame!"
                        $herView.hideshowQQ( "body_64.png", pos )
                        her "Not lost, sir. You see, as I blush."
                        m "Really ... Ahem!"
                        m "Well, what are you waiting for? For 25 points I want to see something special."
#                        show screen bld1
#                        with d3
#                        show screen blktone
#                        with d3
                        
                        # we should remove panties from hermi in this event
                        show screen hermione_lift_skirt_no_panties
                        with d3
#                        $her_head_state = 18
#                        her_head_main ".........................."
#                        g4 "!!?"
                        hide screen bld1

                        $herView.data().delPanties()
                        $herView.data().saveState()
                        $herView.data().addPose( CharacterExItemSkirtLifted( herView.mPoseFolder, 'pose_skirt_up.png', G_Z_POSE ) )
                        $ pos = POS_120

#                        her "test"
                        
                        show screen bld1
                        with d3
                        show screen blktone
                        with d3
                        
                        # we should remove panties from hermi in this event
                        
                        $herView.showQ( "body_58.png", pos )
                        show screen ctc
                        with d3
                        pause






                        her "This is a rather special, sir? I just today Throw."
                        m "fascinating details."
                        menu:
                            "\"You are not too troubled, Miss ...\"":
                                $herView.hideshowQQ( "body_53.png", pos )
                                m "You are not too embarrassed, Miss Granger."
                                her "Well, if my director wants to see me better, should I mind??..."
                                $herView.hideshowQQ( "body_54.png", pos )
                                her "Especially because Gryffindor receive another [current_payout] points."
                            "- Continue to look her eyes -":
                                $herView.hideshowQQ( "body_55.png", pos )
                                her ".............................."
                                her "...........................?"
                                $herView.hideshowQQ( "body_56.png", pos )
                                her "................................"
                                if not end.IsEnding(const_ENDING_STRONG_GIRL) and whoring<14:
                                    her "Sir, I have to go. I now Potions lesson, and Professor Snape is very strict to be late..."               
                                    her "... if they Gryffindor."               
                                    m "Well, Miss Granger."
                                else:
                                    $MusicStart("music/Reamonn-Supergirl.mp3",0.1)
                                    $herView.hideshowQQ( "body_64.png", pos )
                                    "> Hermione cheeky looks into your eyes and you feel you are getting excited."
                                    "> Bitch, as if by chance, licks his lips."
                                    her "Sir, soon learned. Maybe I'm in a hurry and go milking you do?"
                                    menu:
                                        "\"No! Enough for today.\"":
                                            $herView.hideshowQQ( "body_55.png", pos )
                                            m "Well, Miss Granger."
                                        "\"What will you do ?!...\"":
                                            $herView.hideshowQQ( "body_53.png", pos )
                                            g4 "What will you do ?!"
                                            her "Milking you. Do not tell me you do not know how the girls call it."
                                            m "I know how they call. But how do you know it, Miss Granger ?!"
                                            m "You're not interested in such things?"
                                            $herView.hideshowQQ( "body_84.png", pos )
                                            her "Well, sir, since you already asked me about this service, I had to prepare for and conduct a little research."
                                            m "Scientific, of course?"
                                            her "Of course, sir. And now I know a lot of suitable expressions play a hand, playing the fool, shake purse..."
                                            m "Miss Granger, spare me your linguistic exercises."
                                            $herView.hideshowQQ( "body_75.png", pos )
                                            her "Of course, sir... "
                                            $herView.hideshowQQ( "body_46.png", pos )
                                            her "So today we will play with cudgel or something?"
                                            menu:
                                                "\"No!...\"":
                                                    $herView.hideshowQQ( "body_53.png", pos )
                                                    m "Miss Granger, go away!"
                                                    her "I can not with cudgel, sir, because \"cudgel\" is a figurative name of your..."
                                                    m "No matter, miss Granger, just enough for today."
                                                    her ".............................."
                                                "Well, miss Granger...":
                                                    $herView.hideshowQQ( "body_56.png", pos )
                                                    m "Well, miss Granger, proceed. I hope your hands are as skilful as your language."
                                                    $herView.hideshowQQ( "body_53.png", pos )
                                                    her "Yes, sir. Plus 45 points?"
                                                    m "Yes girl, Yes. Plus 45."
                                                    $current_payout+=45
                                                    $MusicStop()
                                                    $ hermione_chibi_xpos = 400 #Near the desk.
                                                    $ pos = POS_120
                                                    hide screen ctc
                                                    $herView.hideQQ()
                                                      
                                                    # load state before doing mess
                                                    $herView.data().loadState()

                                                    jump new_request_16_jerkonly

    stop music fadeout 4.0
    
    label request_02_done:
    $ gryffindor +=current_payout
    m "[current_payout] to \"Gryffindor\" miss Granger. Well done."
    pause
    
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ pos = POS_120
    hide screen ctc
    $herView.hideQQ()
      
    # load state before doing mess
    $herView.data().loadState()

    show screen hermione_02 #Hermione stands still.
    $herView.showQ( "body_31.png", pos )
    with fade
    
    stop music fadeout 4.0

    her "will this be all then?"
    m "Yes, you can go now."

    if IsFirstRun():
#    if request_02 == 0: #First time.
        $herView.hideQQ()
        $ pos.xpos = 300
        $herView.showQQ( "body_13.png", pos )
        her "Another 5 points..."
        her "Can't wait to tell the guys!"
        $herView.hideshowQQ( "body_12.png", pos )
        her "Only that I can't actually tell them about any of this..."
    
    if daytime:
        her "Well, my classes are about to start..."
    else:
        her "It's getting pretty late, Sir... I should go..."

    label new_request_16_jerkonly_to_02:
        $herView.data().loadState()

    
    $herView.hideQQ()
    hide screen bld1
    hide screen blktone 
    hide screen ctc
    with d3
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    

    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###



    if whoring <= 2:
        $ whoring +=1
#    $ request_02 += 1
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

