

    

    
###################REQUEST_30 (Level 08) (75 pt.) (FUCK A CLASSMATE). (Available during daytime only).
label new_request_30: #LV.8 (Whoring = 21 - 23)

    $herView.hideQQ()
    m "{size=-4}(Tell her to fuck one of her classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request
            
    
    $ pos = POS_140
    
    if request_30_points == 0: # <================================================================================ FIRST TIME
        m "Miss Granger..."
        m "Today I need you to have sex with a classmate of your choice."
        if hermi.whoring <=20 or request_24_points <= 1: # Counts how many times you sent Hermione to give blowjob to a boy.
            jump too_much
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $herView.hideshowQQ( "body_47.png", pos )
        her ".............."
        $herView.hideshowQQ( "body_66.png", pos )
        her "I had the feeling that we would get to this sooner or later..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "But..."
        her "..................."
        m "If you do this, \"Gryffindor\" will be getting seventy five points tonight."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Well, then I will do it, sir."
        m "Great. See you after your classes then."
        $herView.hideshowQQ( "body_120.png", pos )
        her "............."

        
    else: # <================================================================================ NOT FIRST TIME
        m "Miss Granger..."
        m "I need you to go have sex with another classmate of yours."
        $herView.hideshowQQ( "body_117.png", pos )
        her "Again, sir?"
        m "Yes. And you will get 75 points again as well."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Well, alright..."
        
    
    
    
    
    $ request_30 = True

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
    $event.Finalize()    
    jump day_main_menu
    
    

 
label new_request_30_complete: # <=================================================================================================== EVENING
    
    $ pos = POS_370

    # LEVEL 08+                
    if one_out_of_three == 1: ### EVENT (A)
        if fucked_ron_and_har:
            jump returns_next_morning
        else:
            $ fucked_ron_and_har = True #In public events. Have sex with a classmate. Event # 1. "Returns next morning". Turns True after that.

        
        m "....."
        m ".........."
        m "She was supposed to be here, by now..."
        m "Hm..."
        $ request_30_points += 1 
        $ request_30 = False 
        $ hermione_sleeping = True
        $ request_30_a = True #Turns True when hermione fails to show up after her "Fuck a classmate" favour. Runs an event next morning.
        $event.Finalize()    
        return
        # NEXT MORNING
        
        
    elif one_out_of_three == 2: ### EVENT (B)
        $ walk_xpos=520 #Animation of walking chibi. (From)
        $ walk_xpos2=400 #Coordinates of it's movement. (To)
        $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        show screen hermione_walk_01 
        with d4
        pause 1.7 
        $ hermione_chibi_xpos = 400 #Near the desk.
        show screen hermione_02 #Hermione stands still.
        pause.5
        show screen bld1
        with Dissolve(.3)
        m "Miss Granger, did you complete your task?"
        show screen blktone
        with d3
        $herView.hideshowQQ( "body_120.png", pos )
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "Yes I did, sir."
        $herView.hideshowQQ( "body_186.png", pos )
        her "And in the school library of all places..."
        her "At first I was kind of worried that we would make too much noise..."
        her "But the boy literally lasted only one minute, sir."
        m "Don't hold it against him, girl."
        m "You are quite attractive, he probably got too excited..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Nevertheless..."
        her "A dozen or so of rather gingerly thrusts and he is cumming already?"
        her "As a girl I cannot help but feel disappointed..."
        m "I see..."
        m "What did you do afterwards?"
        m "Pulled up your panties and went about your business as if nothing happened?"
        $herView.hideshowQQ( "body_87.png", pos )
        her "My panties?"
        $herView.hideshowQQ( "body_69.png", pos )
        her "I rarely bother to wear them anymore, sir."
        m "Oh really?"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Yes... I find not wearing any underwear very empowering."
        m "Good for you, miss Granger."
        
        
    elif one_out_of_three == 3: ### EVENT (C)
        label returns_next_morning:
            pass
        $ walk_xpos=520 #Animation of walking chibi. (From)
        $ walk_xpos2=400 #Coordinates of it's movement. (To)
        $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        show screen hermione_walk_01 
        with d4
        pause 1.7 
        $ hermione_chibi_xpos = 400 #Near the desk.
        show screen hermione_02 #Hermione stands still.
        pause.5
        show screen bld1
        with Dissolve(.3)
            
        m "Miss Granger, did you complete your task?"
        $herView.hideshowQQ( "body_120.png", pos )
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        her "I did, sir."
        $herView.hideshowQQ( "body_124.png", pos )
        her "I took one of the \"Ravenclaw\" boys to the girl's restroom..."
        her "...and let him have his way with me in one of the stalls."
        m "Well done, girl."
        $herView.hideshowQQ( "body_69.png", pos )
        her "....................."
        m "I said you did great. What's the matter?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Ehm... well..."
        her "I am getting paid well for performing such tasks..."
        her "So I have no right to complain, but..."
        m "Hm...?"
        $herView.hideshowQQ( "body_183.png", pos )
        her "My reputation is starting to suffer and it troubles me, sir..."
        m "Your reputation?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Well, yes... ehm..."
        m ".............."

#        label test:
        menu:
            "Disassembled itself":
                m "Well, you adult girl, or do you need a nanny who will take care of your reputation?"
                $ end.SetEndingValue(const_ENDING_STRONG_GIRL,3)
            "Just be careful":
                m "Just be careful."
#        m ".............."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Yes, you are right, sir."
        her "Sorry, forget about what I just said, sir."
        m "hm..."
#        jump your_whore




    



    $ gryffindor += 75 #75
    m "\"Gryffindor\" gets 75 points!"
    her "Thank you, sir."
    
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


    
    $ request_30_points += 1 
    $ request_30 = False 
    $ hermione_sleeping = True
    
    call music_block
    
    $event.Finalize()    
    return

    
    
    
   
   
   
   ####
   
label new_request_30_complete_a: #Hermione does not show up. This is label where she shows up next morning.
    $ request_30_a = False #Turns True when hermione fails to show up after her "Fuck a classmate" favour. Runs an event next morning.
    
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
            
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    m "Miss Granger, you missed your debriefing yesterday."
    $herView.hideQQ()

    $ pos = POS_370

    $herView.showQQ( "body_16.png", pos )
    her "Yes, sir, I apologize... *yawn*..."
    m "Care to explain yourself?"
    $herView.hideshowQQ( "body_190.png", pos )
    her "Of course, sir."
    $herView.hideshowQQ( "body_188.png", pos )
    her "It is sort of embarrassing, though..."
    $herView.hideshowQQ( "body_190.png", pos )
    her "I spent the last night with two of my friends..."
    m "A slumber party with some girlfriends, huh?"
    $herView.hideshowQQ( "body_122.png", pos )
    her "Girlfriends?"
    $herView.hideshowQQ( "body_189.png", pos )
    her "No, sir. Harry and Ron are boys..."
    m "Hm..."
    $herView.hideshowQQ( "body_188.png", pos )
    her "Yes, we were best friends for such a long time..."
    $herView.hideshowQQ( "body_128.png", pos )
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    her "But last night the boys made me their little plaything..."
    $herView.hideshowQQ( "body_123.png", pos )
    her "And I did not mind it one bit..."
    her "They did everything they wanted to do to me..."
    her "And everything I wanted to be done to me has been done..."
    $herView.hideshowQQ( "body_121.png", pos )
    her "................."
    $herView.hideshowQQ( "body_122.png", pos )
    her "Will I get paid for this, sir?"
    
    $ gryffindor += 75 #75
    m "\"Gryffindor\" gets 75 points!"
    her "Thank you, sir."
    
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


    
    $ request_30_points += 1 
    $ request_30 = False 
    $ hermione_takes_classes = True
    
    call music_block 
    
    $event.Finalize()    
    return

  


