################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label new_request_01: #LV.1 (Whoring = 0 - 2)
    $herView.hideQQ()
    m "{size=-4}(All I'll do is have an innocent conversation with her...){/size}"
    menu:
        "\"(Yes, let's do that.)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    m "Alright then..."
    m "Just tell me some news about you."
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_08.png", pos )
    
    if request_01 == 0: #First time this event taking place.
        her "Ehm... Alright..."
        her "I just stand here and talk then...? Like this?"
    else:
        her "Here in the middle, right? I remember..."
    $herView.hideQQ()
    $ menu_x = 0.5 #Menu is moved to the left side.
    
    show screen blktone 
    with d3
    show screen ctc
    $herView.showQ( "body_01.png", pos )
    with Dissolve(.3)
    pause
    
    $pos = POS_140
    m "Well?"
    if request_01 == 0 and whoring <=5: #First time this event taking place.
        $  new_request_01_01 = True #Hearts on menu buttons.
        $herView.hideshowQQ( "body_11.png", pos )
        her "Em... very well..."
        ">Hermione is feeling confused..."
        $herView.hideshowQQ( "body_12.png", pos )
        her "..................."
    if whoring >= 0 and  whoring <= 5: #LEVEL 01 and LEVEL 02
        if whoring >= 3 and whoring <= 5:
            $ level = "02"
            $ new_request_01_02 = True #Hearts on menu buttons.
        $herView.hideshowQQ( "body_12.png", pos )
        her "My life has been quite uneventful lately to be honest..."
        her "Apart from that day when I failed that test..."
        her "Still can't believe it happened..."
        menu: 
            "-Jerk off while she is talking-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                $herView.hideQ()
                hide screen blktone
                with d3
                ">You reach under the desk and crab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                $herView.hideQQ()
                $ pos = POS_370
                $herView.showQQ( "body_14.png", pos )
                her "Professor, what are you doing?"
                m "What, oh it's nothing. Just scratching my leg."
                m "You were saying?"
                $herView.hideshowQQ( "body_14.png", pos )
                her "Yes... Well, that test I failed..."
            "-Participate in the conversation-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Yes, what a tragedy that was..."
                her "Exactly! I'm glad you understand, professor."
                pass
        her "Come to think of it, I don't feel like talking about it anymore..."
        m "Alright, what else has happened lately?"
        her "Em... Well, I'm doing pretty well at herbology lately..."
        her "I mean, I always score the top marks, but I have been studying really hard anyway..."
        her "And now I sort of feel like sometimes I know more than professor Sprout herself..."
        if d_flag_01:
            m "{size=-4}(Yes... ah...){/size}"
        else:
            m "(Professor Sprout... He-he, what a ridiculous name...)"
        
        $herView.hideshowQQ( "body_07.png", pos )
        her "Did you say something professor?"
        m "It's nothing, keep going..."
        $herView.hideshowQQ( "body_14.png", pos )
        her "Well, some students are making fun of professor Quirell behind his back..."
        her "But I disapprove of such behavior of course."
        if d_flag_01:
            m "{size=-4}(Come on! Say something naughty!){/size}"
        else:
            m ".................."
        her "Oh, and my \"Men's Rights Movement\" group is gaining popularity..."
        her "I'm very happy about that..."
        $herView.hideshowQQ( "body_16.png", pos )
        her "I think, given time, we will be able to make a real difference..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Yes, it is so invigorating to know that you are doing the right thing!"
        her "Would't you agree professor?"
        if d_flag_01:
            m "{size=-4}(Dammit. Now she killed the mood completely...){/size}"
            show screen genie
            with d3
            $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
            pass
        else:
            m "Zzzz........"
            
        $herView.hideshowQQ( "body_05.png", pos )
        her "Professor?"
        m "Yes, yes, I'm totally listening..."
        m "This is all very self righteous, er..."
        m "I mean, very invigorating and stuff..."
        $herView.hideshowQQ( "body_07.png", pos )
        her ".........................."
  
    elif whoring >= 6: #LEVEL 03
        $  new_request_01_03 = True #Hearts on menu buttons.
        $herView.hideshowQQ( "body_12.png", pos )
        her "My life has been quite uneventful lately to be honest..."
        her "Hm..."
        her "There is a fierce competition going on between the \"Slytherin\" and the \"Gryffindor\" house."
        her "To be honest, professor, there should be none..."
        her "\"Gryffindor\" would have been in the lead if not for those \"Slytherin\" harlots..."
        her "The things I hear those girls do simply to get a few extra points..."
        $herView.hideshowQQ( "body_04.png", pos )
        her "How despicable!"
        m "What does this make you then, miss Granger?"
        $herView.hideshowQQ( "body_03.png", pos )
        her "Exactly!"
        m "Huh?"
        $herView.hideshowQQ( "body_04.png", pos )
        her "I have to work even harder to compensate for the damage those nasty girls are doing..."
        $herView.hideshowQQ( "body_03.png", pos )
        her "Thank you for helping me out, professor."
        menu: 
            "-Start jerking off-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                $herView.hideQ()
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                $herView.hideQQ()
                $ pos = POS_370
                $herView.showQQ( "body_14.png", pos )
                her "Professor, what are you doing?"
                her "You are not.....?"
                $herView.hideshowQQ( "body_29.png", pos )
                her "Are you...?"
                m "What, it's nothing. Keep going."
                $herView.hideshowQQ( "body_07.png", pos )
                her "Hm..."
                m "{size=-4}(Is she onto me? Nah...){/size}"
            "-Participate in the conversation-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Don't mention it."
                pass
        $herView.hideshowQQ( "body_16.png", pos )
        her "Well, like I was saying..."
        her "I heard that this one girl sold one of the professors some naughty pictures of herself for ten house points..."
        if d_flag_01:
            m "{size=-4}(What a slut... ah... Yes...){/size}"
        else:
            m "Ten points, huh?"
        her "Yes..."
        if d_flag_01:
            $herView.hideshowQQ( "body_29.png", pos )
            her "And these two other girls..."
            her "There is a rumor that they are actually sleeping with professor snape..."
            m "{size=-4}(Yes... Those little, nasty, \"slytherin\" sluts!){/size}"
            $herView.hideshowQQ( "body_45.png", pos )
            her "Also there was this one girl, who gave a teacher a handjob, right during class..."
            m "{size=-4}(Yes... This is good stuff, go on!){/size}"
            $herView.hideshowQQ( "body_29.png", pos )
            her "And this other girl, she sucked off a teacher!"
            m "{size=-4}(Yes! Yes!){/size}"
            $herView.hideshowQQ( "body_46.png", pos )
            her "And another girl let a teacher cum in her mouth..."
            her "And she swallowed it all and loved it!"
            m "{size=-4}(Wait... Is she making this up?){/size}"
            $herView.hideshowQQ( "body_64.png", pos )
            her "I'm a very dirty girl..."
            g4 "what?!"
            $herView.hideshowQQ( "body_65.png", pos )
            her "I just want to suck a cock..."
            her "I want men to cum on my face like in those videos I saw!"
            g4 "{size=-4}(You little slut! That did it!) *Argh!*{/size}"
            $herView.hideQQ()
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            g4 "Argh! YES!"
            $herView.hideQQ()
            hide screen bld1
            with d3
            show screen genie_jerking_sperm
            with d3
            #pause 3
            pause
            
            $ mad = +7
            
            show screen bld1
            with d3
            $herView.showQQ( "body_47.png", pos )
            her "I knew it! You were touching yourself, professor!"
            show screen genie_jerking_sperm_02
            with d3
            g4 "What? No, I was just... ah, shit, this feels good..."
            show screen genie
            #show screen genie_jerking_off
            with d3
            $herView.hideshowQQ( "body_32.png", pos )
            her "This is disgusting! How could you!?"
            her "Sir, you are the headmaster! You are supposed to set a good example!"
            m "Hey, little missy, are you going to judge me or do you want your points?"
            $herView.hideshowQQ( "body_34.png", pos )
            her "My points please, I believe I earned those."
            m "Yes you did."
            $herView.hideshowQQ( "body_47.png", pos )
            her "Ew... I feel so dirty now..."
            hide screen genie_jerking_sperm_02
            with d3
        else:
            her "We need to put an end to this behavior, professor!"
            m "Yeah, sure..."
            her "So you agree with me then?"
            her "I think we need to implement a new penalty system to punish girls who are known to sell favours..."
            m "(All I heard was \"punish girls\"...)"
            her "This will also help the boys in our school to feel less discriminated against!"
            m "The boys?"
            m "Oh, right... Nobody wants to buy sexual favours from them... Poor bastards."
            $herView.hideQQ()
            $herView.showQ( "body_03.png", pos, d3 )
            her "I'm so glad that you understand my concerns, Sir."
            m "Yes, yes, sure..."


    stop music fadeout 2.0
    
    $ gryffindor +=5
    
    $herView.hideQQ()
    $herView.showQ( None, pos, d3 )
    m "Five points to \"Gryffindor\" miss Granger. Well done." 
    
    #$herView.showQ( "body_07.png", pos, d3 )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Will this be all then?"
    if whoring >= 0 and whoring <= 2: #LEVEL 01
        her "*sigh of relief*"
    m "Yes, you can go now."
    if request_01 == 0:
        $herView.hideshowQQ( "body_01.png", pos )
        her "Another 5 points... The Guys will be so happy."
        her "Thank you, professor."

    label request_01_done:
    if whoring <= 2:
            $ whoring +=1
 
    $ request_01 += 1
    
    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
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
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
