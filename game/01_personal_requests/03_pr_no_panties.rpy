################### REQUEST_03 (Level 02) (Available during daytime only). "Give me your Трусики" ###############################
label new_request_03: #(Whoring = 3 - 5)
    if whoring <= 2:
        jump too_much
    $herView.hideQQ()
    
    $ pos = POS_370
    
    m "{size=-4}(I could ask her to take off her panties and give them to me before she leaves for classes today.){/size}"
    $ menu_x = 0.5 #Default position of the menu. Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request
    $herView.showQQ( None, pos )
    #show screen hermione_main
    her "I am listening, sir."
    m "I will need your panties..."   
    $herView.hideQQ()
    $ menu_x = 0.5 #Menu is moved to the left side.
    $ pos = POS_120
    show screen blktone 
    show screen ctc
    $herView.showQ( "body_01.png", pos )
    with Dissolve(.3)
    pause
    
    
    if request_03_points == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
        stop music fadeout 10.0
        $ new_request_03_01 = True # HEARTS.
        $ request_03 += 1
        $herView.hideshowQQ( "body_11.png", pos )
        her "W-what?"
        her "My... panties...?"
        her "Professor Dumbledore, this is..."
        m "This is the favour I will be buying from you today, miss Granger..."
        m "If you are not interested you are more than welcome to leave."
        her "No, I am interested. I am.... it's just..."
        her "You need my...."
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $herView.hideshowQQ( "body_47.png", pos )
        her "...panties, sir?"
        m "Yes I do..."
        $herView.hideshowQQ( "body_66.png", pos )
        her "May I ask what you are planning to do with them...?"
        m "Ehm...I'm conducting research..."
        her "But this is kind of inappropriate, don't you think?"
        m "But don't you hate it that some of the girls from \"Slytherin\"..."
        m "Are selling favours for house points, miss Granger?"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Yes I do!"
        $herView.hideshowQQ( "body_12.png", pos )
        her "(Those \"Slythering\" tramps have no dignity.)"
        $herView.hideQQ()
        m "Well, there you go then!"
        $herView.hideshowQQ( "body_66.png", pos )
        her "Huh?"
        m "Beat them at their own game!"
        her "What?"
        m "Yes! Don't just put the \"Gryffindor\" house back on top..."
        m "But do it by beating them at their own game!"
        $herView.hideshowQQ( "body_11.png", pos )
        her "Professor..."
        m "A headmaster cannot play favourites, but you know how I feel about \"Gryffindor\"..."
        m "I wish I could give you the points but that would ruin the system..."
        show screen blktone8
        $herView.hideQQ()
        ">Suddenly Hermione extends her arm to you..."
        ">You see that she is clutching a little piece of fabric in her fist..."
        ">Her panties? You can't help but wonder when she managed to take them off..."
        m "??!"
        ">You acquired Hermione's panties..."
        hide screen blktone8
        with d3
        $herView.hideshowQQ( "body_67.png", pos )
        
        her "Just take them sir..."
        m "What? When did you?"
        her "Your speech was so moving..."
        her "You are so right, sir! I shall beat them at their own game!"
        her "My classes are about to start, so I should probably go now..."
        $herView.hideQQ()

        $ pos = POS_370
        $herView.showQQ( "body_23.png", pos )
        her "..........."
        $herView.hideshowQQ( "body_29.png", pos )
        her "...I hope nobody will notice that I have no underwear on today..."
        $herView.hideshowQQ( "body_31.png", pos )
        her "Oh, and I will be back tonight to pick them up, sir."
        m "Of course. Your panties will be right here on my desk, waiting for you..."
        $herView.hideshowQQ( "body_34.png", pos )
        her "............."
        jump request_03_ends

    else: #<========================================================================================== FIRST EVENT!
        if request_03_points == 0 and whoring < 12:
            her "emm..."
            her " This is a surprise, sir, but..."
        if request_03 >= 1:
            her "Again, sir?"
            m "Yes again..."
        her "Here..."
        if whoring >= 12: #LEVEL 05
            $herView.hideQQ()
            ">Hermione pulls her panties out of her pocket..."
            m "What?"
            $herView.hideshowQQ( "body_45.png", pos )
            her "Yes, I had a feeling that you might ask for these today, sir."
            m "A feeling?"
            $herView.hideshowQQ( "body_68.png", pos )
            her "Well, to be completely honest I just do not bother to wear them much anymore..."
        else:
            $herView.hideQQ()
            ">Hermione takes off her panties and hands them over to you..."
        $herView.hideQQ()
        ">Hermione's panties acquired."
        $herView.showQQ( "body_15.png", pos )
        her "Well, the classes are about to start, so I'd better go now..."

        
    label request_03_ends:
    $ request_03 = True #True when Hermione has no Трусики on.
    if whoring <= 5:
        $ whoring +=1
        
    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
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

    $ hermione_takes_classes = True


    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###

    jump day_main_menu
    
    
        
label new_request_03_complete: # WHORING LEVEL 02 <=================
    
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 2.5
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    show screen hermione_02
    with Dissolve(.3)

    $ pos = POS_120
    
    "Good evening, sir..."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    menu:
        "\"Here are your panties.\"":
            if have_cum_soaced_panties:
                jump panties_soaked_in_cum
            else:
                her "Thank you, sir."
                her "And my payment?"
                m "Of course."
        "\"How was your day, miss Granger?\"":
            if  whoring <= 5: #LEVEL 02. EVENT LEVEL: 01
                $ new_request_03_01 = True # HEARTS.
                $herView.hideQQ()
                $ pos = POS_120
                $herView.showQQ( "body_15.png", pos )
                her "Oh..."
                her "Quite ordinary actually..."
                $herView.hideshowQQ( "body_13.png", pos )
                her "Although I could not help but worry that somebody would notice somehow..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "....."
                $herView.hideshowQQ( "body_31.png", pos )
                her "Can I have my panties back now?"
                m "Of course..."
                $herView.hideQQ()
                ">You give Hermione her panties back..."
                if have_cum_soaced_panties:
                    jump panties_soaked_in_cum
                else:
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "And my payment?"
                    m "Yes, yes..."
            elif whoring >= 6 and whoring <= 8: #LEVEL 03. EVENT LEVEL 02.
                $ new_request_03_02 = True # HEARTS.
                $herView.hideQQ()
                $ pos = POS_120
                $herView.showQQ( "body_15.png", pos )
                her "Oh..."
                her "It was quite ordinary really..."
                her "I spent some time with my classmates..."
                her "And we had a short \"MRM\" meeting after that..."
                $herView.hideshowQQ( "body_16.png", pos )
                her "I gave a short speech on \"Why it is wrong to sell sexual favours in exchange for house points\"..."
                $herView.hideshowQQ( "body_12.png", pos )
                her "I felt bad that I had to give the speech without any underwear on..."
                menu:
                    "\"You little hypocrite!\"":
                        $ mad +=5
                        $herView.hideshowQQ( "body_14.png", pos )
                        her "Professor?"
                        m "You sold your panties to me this morning..."
                        m "And a couple of hours later you already publicly condemned that exact behavior..."
                        m "What would you call this?"
                        $herView.hideshowQQ( "body_69.png", pos )
                        her "I know you are right, professor..."
                        her "(But we need the points...)"
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Can I have my payment now please?"
                        m "What about your panties?"
                        $herView.hideshowQQ( "body_34.png", pos )
                        her "Oh, them too of course..."  
                        if have_cum_soaced_panties:
                            jump panties_soaked_in_cum
                        else:
                            pass
                    "\"It's for the grater good...\"":
                        her "Exactly!"
                        her "We need those points badly..."
                        her "It is not my fault that the system is so corrupted..."
                        $herView.hideshowQQ( "body_16.png", pos )
                        her "I shall remain a symbol of righteousness to my peers, no matter what!"
                        $herView.hideshowQQ( "body_31.png", pos )
                        her "Can I have my panties back now, please?"
                        if have_cum_soaced_panties:
                            jump panties_soaked_in_cum
                        else:
                            her "And my payment."
            elif whoring >= 9: #LEVEL 04. EVENT LEVEL 03.
                $ new_request_03_03 = True # HEARTS.
                $herView.hideQQ()
                $ pos = POS_120
                $herView.showQQ( "body_16.png", pos )
                her "Another ordinary day at hogwarts..."
                her "Nothing worth mentioning happened today..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Although I have to admit..."
                her "It was oddly empowering to have no underwear on..."
                her "Hm..."
                $herView.hideshowQQ( "body_45.png", pos )
                her "Can I have my panties back now please?"
                m "Of course..."
                $herView.hideQQ()
                ">You give Hermione her panties back..."
                if have_cum_soaced_panties:
                    jump panties_soaked_in_cum
                else:
                    $herView.hideshowQQ( "body_45.png", pos )
                    her "And my payment?"
                    m "Yes, yes..."
    label back_from_panties:
    $ gryffindor +=15
    m "Fifteen points to \"Gryffindor\" miss Granger. Well deserved." 
    her "Thank you, sir..."
    m "You can go now."
    her "Good night, sir."
    m "Yes, good night..."

    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
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



    $ request_03_points += 1 #Leveling up the event.
    $ request_03 = False #When False - you gave her her Трусики back.
    $ hermione_sleeping = True

    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC

    return 
    
    
    
### Трусики SOAKED IN CUM ###
label panties_soaked_in_cum:
    $ have_cum_soaced_panties = False #TRUE when you have the Трусики in your possession (before you return them to Hermione).
    $ she_knows_about_cum = False
    $ pos = POS_120
    
    if whoring >= 3 and whoring <= 5: # LEVEL 02
        $herView.hideshowQQ( "body_71.png", pos )
        her "Hm....?"
        $herView.hideshowQQ( "body_05.png", pos )
        her "Sir? What is this?"
        her "What have you done to them?"
        $herView.hideshowQQ( "body_07.png", pos )
        her "They are covered in something slimy..."
        menu:
            "\"An experiment went wrong\"":
                $herView.hideshowQQ( "body_02.png", pos )
                her "An experiment went wrong, sir?"
                m "Yes... Or maybe I should rather say..."
                g9 "\"An experiment went very right\"? He-he..."
                $herView.hideshowQQ( "body_07.png", pos )
                her ".....................?"
                her "What kind of experiment was it?"
                m "What? Oh..."
                m "Some top secret research I'm conducting."
                m "I can't discuss it with a student."
                $herView.hideshowQQ( "body_05.png", pos )
                her "................................"
            "\"You gave them to me like this!\"":
                her "I most certainly did not, sir!"
                her ".........................."
        $herView.hideshowQQ( "body_71.png", pos )
        her "Well, these will require some serious cleaning before I can put them on again..."
        m "Or you could put them on now."
        $herView.hideshowQQ( "body_14.png", pos )
        her "What?"
        $herView.hideshowQQ( "body_13.png", pos )
        her "I really would rather not, sir..."
        menu:
            "\"Put them on or lose the points!\"":
                $ mad +=7
                $herView.hideshowQQ( "body_72.png", pos )
                her "What?"
                her "Professor, you are joking, right?"
                m "I am not..."
                $herView.hideshowQQ( "body_31.png", pos )
                her "B-but..."
                $herView.hideshowQQ( "body_33.png", pos )
                her "........................................"
                $herView.hideshowQQ( "body_47.png", pos )
                her "(Must you always have your way, sir?)"
                m "What was that, miss Granger?"
                $herView.hideshowQQ( "body_30.png", pos )
                her "It's nothing, sir."
                her "Putting my panties back on!"
                $herView.hideQQ()
                show screen blktone8
                with d3
                ">Hermione hesitantly puts on her panties..."
                ">A tiny stream of cum trickles down one of her legs..."
                ">Hermione looks very uncomfortable..."
                hide screen blktone8
                with d3
                $herView.hideshowQQ( "body_34.png", pos )
                her "......................"
            "\"Well, suit yourself...\"":
                pass
    if whoring >= 6 and whoring <= 8: # LEVEL 03 (SECOND EVENT)
        $herView.hideshowQQ( "body_71.png", pos )
        her "My panties..."
        $herView.hideshowQQ( "body_73.png", pos )
        her "What happened to them sir?"
        menu: 
            "\"An experiment went wrong.\"":
                her "Hm..."
                her "I see..."
            "\"You gave them to me like this!\"":
                her "Did I? Oh, well..."
        $herView.hideQQ()
        ">Hermione gives her cum-soaked underwear a quizzical look..."
        $herView.hideshowQQ( "body_71.png", pos )
        her "Seems like these will require some serious cleaning before I can put them on again..."
        m "Why not put them on now?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Hm....?"
        $herView.hideshowQQ( "body_71.png", pos )
        her "Well, I suppose I could wear them one more time before putting them into laundry..."
        $herView.hideQQ()
        show screen blktone8
        with d3
        ">Hermione puts the panties on..."
        hide screen blktone8
        with d3
        $herView.hideshowQQ( "body_34.png", pos )
        her "Will this be all, sir?"
        $herView.hideshowQQ( "body_44.png", pos )
        her "Это все, сэр?"
    if whoring >= 9: #LEVEL 04+ (THIRD EVENT)
        $herView.hideshowQQ( "body_71.png", pos )
        her "My panties..."
        if request_03 >= 1:
            her "They are covered in something slimy again..."
        else:
            her "They are covered in something slimy..."
        her "And they smell funny..."
        $herView.hideshowQQ( "body_29.png", pos )
        her "Hm... That smell..."
        her "It's familiar somehow..."
        $herView.hideshowQQ( "body_45.png", pos )
        her "What exactly did you do to them, sir?"
        menu:
            "\"An experiment went wrong\"":
                her "An experiment, huh?"
                her "Of what nature?"
                $herView.hideshowQQ( "body_46.png", pos )
                her "No, don't answer that... I think I know..."
            "\"You gave them to me like this!\"":
                her "I don't think so, sir."
                her "But it's alright if you don't want to tell me, sir..."
                her "I think I know exactly what happened to them..."
            "\"I came all over them!\"":
                $ she_knows_about_cum = True
                $herView.hideshowQQ( "body_64.png", pos )
                her "I knew it..."
                her "They reek of semen!"
        $herView.hideshowQQ( "body_68.png", pos )
        her "Hm..."
        her "Seems like these will require some serious cleaning before I can put them on..."
        $herView.hideshowQQ( "body_64.png", pos )
        her "Unless you want me to put them on now, sir...?"
        menu: 
            "\"Yes! Put them on now, girl!\"":
                her "Well, if I must..."
            "\"I don't care. Do what you want.\"":
                her "Why not put them on one more time?"
        
        $herView.hideshowQQ( "body_74.png", pos )
        her "I am only doing this to give my house a fair chance at winning the cup this year..."
        m "Right..."
        
        $herView.hideQQ()
        
        show screen blktone8
        with d3
        ">Hermione swiftly slides her drenched panties on..."
        hide screen blktone8
        with d3
        
        # NEW Branch :)
        $pos = POS_120
        if she_knows_about_cum == True and whoring >= 12:
            $herView.showQQ( "body_58.png", pos )
            her "...sir?"
            m "yes?"
            $herView.hideQQ()
            
            $herView.showQQ( "body_58.png", pos )
            her "One friend told me that guys like all kinds of perversions."
            $herView.hideshowQQ( "body_129.png", pos )
            her "That's right, sir?"
            m "Hmm, well, if you ask..."
            m "What specifically are you talking about?"
            $herView.hideshowQQ( "body_84.png", pos )
            her "Well, for example..."
            $herView.hideQQ()
            
            $herView.data().saveState()
            $herView.data().addPose( CharacterExItemSkirtLifted( herView.mPoseFolder, 'pose_skirt_up.png', G_Z_POSE ) )
            $herView.data().addItem( 'panties_cum', CharacterExItem( herView.mMiscFolder, 'panties_soaked.png', G_Z_PANTIES + 1, 'panties' ) )
            
            $herView.showQQ( "185.png", pos )
            her "...if the girl will be in panties soaked in cum?"
            pause
            menu:
                "\"Of course, guys are in awe of this!\"":
                    $herView.hideshowQQ( "body_128.png", pos )
                    her "I thought so, Professor."
                    $herView.hideQQ()
                    $herView.data().loadState()
                    $herView.showQQ( "body_52.png", pos )
                    her "Then I will go?"
                    m "Hmm, Yes, miss Granger..."
                    $herView.hideshowQQ( "body_64.png", pos )
                    her "You have not forgotten anything, sir?"
                    m "Оh..."
                    $herView.hideshowQQ( "body_45.png", pos )

                "\"I think it's dirty!\"":
                    $mad += 15
                    $herView.hideQQ()
                    $herView.data().loadState()
                    $herView.showQQ( "body_51.png", pos )
                    her "tsk!"
                    $herView.hideshowQQ( "body_191.png", pos )
                    her "My points, sir!"
                    
                    

    jump back_from_panties
