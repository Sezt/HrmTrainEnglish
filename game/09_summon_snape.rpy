label summon_snape:
    if snape_busy:
        ">Professor Snape is unavailable."
        if daytime:
            jump day_main_menu
        else: 
            jump night_main_menu
    
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    #$ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    #$ walk_xpos=470 #Animation of walking chibi. (From)
    #$ walk_xpos2=360 #Coordinates of it's movement. (To)
    #show screen snape_walk_01 
    #with d3
    #pause 1.5
    $ menu_x = 0.2 #Menu is moved to the left side. (Default menu_x = 0.5)
    $ tt_xpos=350 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_02 #Snape stands still.
    show screen bld1
    show screen snape_main
    with Dissolve(.3)

  
    sna "Yes, what is it?"
    label snape_ready:
        pass
    menu:
        "-Chit chat-" if sfmax and not chitchated_with_snape and not daytime: # sfmax - friendship with Snape maxed out.
            $ chitchated_with_snape = True #Prevents you from chitchating more then once a day. Turns back to False every night and every day.
            $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
            #$ snape_busy = True
            jump snape_chitchat
        "-Chit chat-" if daytime and not chitchated_with_snape: # sfmax - friendship with Snape maxed out.
            $ chitchated_with_snape = True #Prevents you from chitchating more then once a day. Turns back to False every night and every day.
            $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
            #$ snape_busy = True
            jump snape_chitchat
        "\"Let's hang.\"" if not daytime and not sfmax: # Turns TRUE when friendship with Snape been maxed out.
            if one_of_ten == 10:
                call not_today #Snape says: "I am busy tonight."
#            elif snape_friendship >= 39 and whoring <= 5: # Whoring level <= 2. Makes sure you don't proceed after Date #6 until reached Whoring lvl 3.
#                call not_today #Snape says: "I am busy tonight."
            elif snape_friendship >= 88 and whoring <= 14: # Whoring level <= 5. Makes sure you don't proceed after Date #12 until reached Whoring lvl 6.
                call not_today #Snape says: "I am busy tonight."
            else:
                pass
                $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
                jump snape_dates
        "\"Nevermind.\"":
            stop music fadeout 1.0
            $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
            if daytime:
                sna "Alright, back to work then..."
                play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
            else: 
                sna "Goodnight then."
                play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
            $ snape_busy = True
            hide screen snape_02 #Snape stands still.
            hide screen bld1
            hide screen snape_main
            with d3
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            if daytime:
                jump day_main_menu
            else: 
                jump night_main_menu
    

label snape_dates:  ### HANGING WITH SNAPE ###
    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    show screen fireplace_fire
    hide screen genie
    hide screen chair
    hide screen desk
    show screen desk
    
    hide screen snape_02 #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3

    
    with fade
    $ fire_in_fireplace = True
   
#    if snape_against_hermione: #Turns True after event_08 (Hermione shows up for the first time).
                               #Activates special event when hanging out with Snape next time.
#        show screen with_snape #Makes sure the scene is not animated...
#        jump special_date_with_snape
    
#    if snape_against_hermione_02: #Activates after second visit from Hermione (event_09).
#        show screen with_snape #Makes sure the scene is not animated...
#        jump special_date_with_snape_02


    if this.IsStep("SNAPE"):
        show screen with_snape #Makes sure the scene is not animated...
        $ this.RunStep("SNAPE")
    
    
    if wine >= 1 and not wine_not: # Using Dumbledor's wine for the first time.
        $ wine_not = True # Turns True after you use Dumbledore's wine in the "Snape dating" for the first time. Makes sure the cut-scene is shown only once.
        call wine_first
    elif wine >= 1 and wine_not: # Using Dumbledor's wine not for the first time.
        call wine_not_first
    else:
        pass
    
    
    
    
    
    if snape_friendship >= 5 and snape_events == 0:
        call date_with_snape_01
        
    elif snape_friendship >= 12 and snape_events == 1: #LEVEL 02
        call date_with_snape_02
        
    elif snape_friendship >= 19 and snape_events == 2: #LEVEL 03
        call date_with_snape_03
        
    elif snape_friendship >= 27 and snape_events == 3: #LEVEL 04
        call date_with_snape_04
        
    elif snape_friendship >= 34 and snape_events == 4: #LEVEL 05
        call date_with_snape_05
        
    elif snape_friendship >= 41 and snape_events == 5: #LEVEL 06. Can't proceed after this until whoring >= Lv 3.
        call date_with_snape_06
        
    elif snape_friendship >= 48 and snape_events == 6: #LEVEL 07
        call date_with_snape_07
         
    elif snape_friendship >= 55 and snape_events == 7: #LEVEL 08
        call date_with_snape_08
        
    elif snape_friendship >= 62 and snape_events == 8: #LEVEL 09
        call date_with_snape_09
        
    elif snape_friendship >= 69 and snape_events == 9: #EVENT 10
        call date_with_snape_10
        
    elif snape_friendship >= 76 and snape_events == 10: #EVENT 10
        call date_with_snape_11
        
    elif snape_friendship >= 83 and snape_events == 11: #EVENT 11
        call date_with_snape_12
         
    elif snape_friendship >= 88 and snape_events == 12: #EVENT 12. If whoring level > 5.
        call date_with_snape_13
        
    elif snape_friendship >= 93 and snape_events == 13: #EVENT 13
        call date_with_snape_14
        
    elif snape_friendship >= 98 and snape_events == 14: #EVENT 14
        call date_with_snape_15
        
    else:
            
        show screen bld1
        with d3
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">You spend the evening hanging out with Professor Snape.\n>Your relationship with him has improved."
        hide screen bld1
        with d3
        
        
        

 
    $ snape_friendship +=1
    jump day_start
    
   
### SPECIAL DATE ###
label special_date_with_snape: #TAKES PLACE AFTER FIRST VISIT FROM HERMIONE.
#    $ snape_against_hermione = False #Turns True after event_08. Activates special event (THIS EVENT) when hanging out with Snape next time.
    $sna_head_state = 2
    sna_head_main "..........................."
    m "...............................?"
    $sna_head_state = 3
    sna_head_main "I hate her so much..."
    menu:
        "\"Yeah! That bitch!\"":
            $sna_head_state = 1
            sna_head_main "Good to know that we are on the same page..."
            $sna_head_state = 2
            sna_head_main "That girl..."
        "\"You hate who?\"":
            $sna_head_state = 1
            sna_head_main "Why would you ask that?"
            sna_head_main "That Hermione girl of course!"
        "\"Is she that bad?\"":
            sna_head_main "She is the worst!"

    $sna_head_state = 2
    sna_head_main "A top student..."
    $sna_head_state = 3
    sna_head_main "Leads all sorts of extracurricular activities and clubs..."
    sna_head_main "the president of the school's Student Representative Body..."
    sna_head_main "Likely to become the head girl soon..."
    $sna_head_state = 2
    sna_head_main "................"
    $sna_head_state = 3
    sna_head_main "............"
    with hpunch
    $sna_head_state = 5
    sna_head_main "{size=+7}I hate that fucking witch!!!{/size}"
    g4 "{size=-4}(What the...?){/size}"
    $sna_head_state = 2
    sna_head_main ".............."
    sna_head_main "She used to be just an annoyance, but these days..."
    $sna_head_state = 1
    sna_head_main "She became a fully fledged menace..."
    sna_head_main "That witch is officially my least favorite student in the entire school now..."
    m "What about that Potter boy?"
    $sna_head_state = 6
    sna_head_main "The Potter boy? Ha! Who's that!?"
    $sna_head_state = 1
    sna_head_main "No I'm serious..."
    sna_head_main "I will go as far as to say that Potter jr. and his wretched father combined..." #I will go as far as to say that Potter jr. and his wretched father combined..."
    sna_head_main "Didn't cause me nearly as much grief as this little witch does lately..."
    m "Now, now, we both know that's not true..."
    $sna_head_state = 2
    sna_head_main "Yeah... You're probably right..."
    $sna_head_state = 7
    sna_head_main "That bastard James Potter really did a number on me-"
    $sna_head_state = 6
    sna_head_main "Wait, how do you know this?"
    m "Well... I've read the books..."
    sna_head_main "What? What books?"
    m "Nah, never-mind. I'm a genie, remember? I know things..."
    $sna_head_state = 9
    sna_head_main "Hm... And yet you need me to teach you stuff..."
    m "Well, I told you, my magic is acting up in your world..."
    sna_head_main "Sure, sure..."
    m "......"
    m "She came by the other day..."
    $sna_head_state = 10
    sna_head_main "Who did?"
    m "The Hermione girl..."
    $sna_head_state = 1
    sna_head_main "What?!"
    $sna_head_state = 2
    sna_head_main "I thought we agreed on the \"no human contact\" rule."
    $sna_head_state = 7
    sna_head_main "(Even though lately I've been wondering whether or not she is human at all...)"
    m "I know... She kinda forced her way in..."
    $sna_head_state = 1
    sna_head_main "I imagine she did..."
    sna_head_main "What did she want?"
    
    if jerk_off_session:
        m "I'm not sure..."
        $sna_head_state = 11
        sna_head_main "??"
        m "I've been jerking off during the entire time she was talking..."
        $sna_head_state = 2
        sna_head_main "You've been..."
        sna_head_main "... doing what?"
        m "Hey, don't judge me!"
        m "You don't know what it's like to be cooped up in this tower like a prisoner!"
        sna_head_main "You... y-you...."
        $sna_head_state = 12
        sna_head_main "......"
        $sna_head_state = 15
        sna_head_main "Ha.... ha-ha... HA-HA-HA!!!"
        m "Wha..? What did I say?"
        $sna_head_state = 14
        sna_head_main "Ha-ha-ha! You are amazing!"
        $sna_head_state = 9
        sna_head_main "Are all genies so... wonderfully nihilistic?"
        m "Yeah... We immortals tend to not give a fuck."
        sna_head_main "Understandable..."
        $sna_head_state = 10
        sna_head_main "Unfortunately, us mere mortal cannot afford such luxury..."
        
    else:
        m "Not sure... She's been talking a lot..."
        m "Something about some \"greefeendo\" points... and..."
        m "Er... I wasn't paying attention to be honest..."
        $sna_head_state = 1
        sna_head_main "Nah... Probably another load of self righteous crap..."
        $sna_head_state = 7
        sna_head_main "She is famous for that..."
    

    sna_head_main "I have a class early tomorrow, so let us call it a night." #собираться ночью."
    m "What about you teaching me magic and stuff?"
    $sna_head_state = 10
    sna_head_main "Yeah, absolutely..."
    sna_head_main "Next time..."
    m "Alright..."
    
    

    
#    $ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)
    jump day_start
    
#######################################################################################################################    
label special_date_with_snape_02: #TAKES PLACE AFTER SECOND VISIT FROM HERMIONE. (Where she says that she sent letter to the ministry.)
    show screen bld1
    with d5
    #$ snape_against_hermione = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.
    m "......................."
    m "Hermione Granger came by again..."
    $sna_head_state = 1
    sna_head_main "Don't mention the witch's name when I'm off duty...."
    $sna_head_state = 2
    sna_head_main "..............."
    $sna_head_state = 3
    sna_head_main "Dammit! I am a grown man, Albus!"
    m "My name is not--"
    sna_head_main "An esteemed wizard..."
    m "Well, alright, let it out..."
    $sna_head_state = 2
    sna_head_main "How come one tiny....cunt, is able to cause me so much grief?!"
    $sna_head_state = 4
    sna_head_main "I thought with you as my ally I will have a chance to--"
    m "To unclench?" 
    $sna_head_state = 2
    sna_head_main "Yeah, that could be the word..."
    $sna_head_state = 16
    sna_head_main "But all I did was give her more leverage to harass me with..."
    sna_head_main "She's even turning the teachers against me now..."
    $sna_head_state = 3
    sna_head_main "................."
    $sna_head_state = 7
    sna_head_main "She must go..."
    m "What do you mean?"
    with hpunch
    $sna_head_state = 5
    sna_head_main "{size=+6}I will have to kill her!{/size}"
    g4 "Like literally kill her?"
    $sna_head_state = 6
    sna_head_main "Do I have any other choice?"
    m "You're joking, right?"
    sna_head_main "Am i?!"
    $sna_head_state = 11
    sna_head_main "Can you do this for me?"
    m "Em..."
    m "As much I would \"enjoy\" murdering a teenage girl..."
    m "Genies can't kill..."
    $sna_head_state = 7
    sna_head_main "Rats!"
    m "And we frown upon murderers..."
    if jerk_off_session:
        $sna_head_state = 17
        sna_head_main "Really? I thought you didn't give a fuck..."
        m "to a certain degree..."
        $sna_head_state = 7
        sna_head_main "............."
    $sna_head_state = 2
    sna_head_main "Well... don't mind me then..."
    sna_head_main "I'm all talk..."
    sna_head_main "I would never actually harm a student..."
    $sna_head_state = 3
    sna_head_main "(...permanently that is.)"
    m "Listen, if she bugs you so much, why not just find a less radical way to deal with her?"
    $sna_head_state = 7
    sna_head_main "Nah... Flogging has been outlawed years ago..."
    m "That's not what I mean..."
    $sna_head_state = 1
    sna_head_main "Huh?"
    m "She is a top student, right?"
    $sna_head_state = 2
    sna_head_main "Yes, damn her. The girl is a hard-worker, I give her that."
    m "She also has a reputation for being self righteous."
    $sna_head_state = 6
    sna_head_main "Oh, yes!"
    m "And she thinks that she is better than everyone else..."
    $sna_head_state = 17
    sna_head_main "Where are you going with this?"
    m "Well it seems like all of her power comes from her reputation..."
    $sna_head_state = 11
    sna_head_main "......................?"
    m "What if we take that away from her?"
    $sna_head_state = 10
    sna_head_main "That would shut her up I suppose..."
    $sna_head_state = 2
    sna_head_main "But how? She's practically a saint."
    $sna_head_state = 7
    sna_head_main "Even students who hate her secretly admire her."
    $sna_head_state = 2
    sna_head_main "She didn't fail a single test in her entire time here..."
    sna_head_main "She is always ahead of the schedule..."
    $sna_head_state = 3
    sna_head_main "Damn, how I hate it when she corrects me during my classes..."
    $sna_head_state = 6
    sna_head_main "And thanks to her the \"Gryffindor\" house is way ahead of everybody else now..."
    $sna_head_state = 7
    sna_head_main "Even \"Slytherin\" is no match for them this year..."
    $sna_head_state = 16
    sna_head_main "........................"
    $sna_head_state = 6
    sna_head_main "Dammit... I need more wine..."
    m "The wine could wait. Hear me out first!"
    $sna_head_state = 1
    sna_head_main "Huh...?"
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label fuck_off:
    m "Hm... Let us..."
    menu:
        m "..."
        "{size=-3}\"Make sure she is not a top student any longer!\"{/size}" if not d_flag_01:
            $ d_flag_01 = True
            sna_head_main "What? You mean grade her unfairly?"
            $sna_head_state = 2
            sna_head_main "Nah... Dumbledore would never allow--"
            $sna_head_state = 9
            sna_head_main "Wait a second!"
            m "Exactly!"
            $sna_head_state = 18
            sna_head_main "You're right! I grade her tests unfairly! I could even make other teachers do the same!"
            sna_head_main "I could say that the order comes from you..."
            $sna_head_state = 19
            sna_head_main "And when the real Dumbledore shows up I will pretend that I had no idea that he was away..."
            m "Works for me."
            $sna_head_state = 10
            sna_head_main "Er..."
            sna_head_main "This is still you, genie, right?"
            m "Yeah, yeah, still here..."
            $sna_head_state = 18
            sna_head_main "OK, good"
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off
        "{size=-3}\"Make sure \"Gryffindor\" loses the cup this year!\"{/size}" if not d_flag_02:
            $ d_flag_02 = True
            $sna_head_state = 1
            sna_head_main "You mean to just start subtracting points from them for no good reason?"
            $sna_head_state = 18
            sna_head_main "Oh, I like that!"
            $sna_head_state = 20
            sna_head_main "There are a couple of \"Slytherin\" girls who are long overdue for receiving some extra house points as well."
            $sna_head_state = 19
            sna_head_main "Oh, this will work out magnificently!"
            $sna_head_state = 18
            sna_head_main "You are a Genius!"
            m "Yes, I am a genius genie. What are the odds of that..."
            translators "По-английски 'джинн' (genie), звучит сходно с 'гений' (genius)."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

        "{size=-3}\"Ruin her reputation!\"{/size}" if not d_flag_03:
            $ d_flag_03 = True
            $sna_head_state = 1
            sna_head_main "Tarnish her reputation?"
            sna_head_main "But the girl is incorruptible..."
            m "Nonsense!"
            m "All we need to do is convince her that she needs to make some sacrifices \"for the greater good\""
            $sna_head_state = 9
            sna_head_main "Oh, but of course..."
            $sna_head_state = 21
            sna_head_main "She would gladly \"Get her hands dirty\" to save the honour of her precious \"Gryffindor\" house!"
            $sna_head_state = 9
            sna_head_main "And when she does, we will have the leverage we need..."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

    sna_head_main "This could actually work!"
    m "I think so too."
    $sna_head_state = 19
    sna_head_main "Oh, I feel so alive tonight!"
    $sna_head_state = 15
    sna_head_main "Pour me another goblet!"
    $sna_head_state = 19
    sna_head_main "The \"Defence Against the Dark Arts\" class will start late tomorrow!"
    m "....."
    m "Don't you think this is a bit too brutal though?"
    m "I mean, she's just a girl..."
    $sna_head_state = 8
    sna_head_main "Just a girl?"
    sna_head_main "Oh no, no, no..."
    $sna_head_state = 4
    sna_head_main "She is the embodiment of pure evil!"
    $sna_head_state = 2
    sna_head_main "If we don't do this now..."
    $sna_head_state = 3
    sna_head_main "One of those days I may just snap and \"Avada Kedavra\" her!"
    m "You'll do what?"
    $sna_head_state = 4
    sna_head_main "Murder her for real!"
    m "Alright, alright... got it..."
    m "Let's choose the lesser of the two evils then."
    $sna_head_state = 7
    sna_head_main "Yes..."
    $sna_head_state = 6
    sna_head_main "Now, pour me some more wine."

    ">You spend rest of the evening in Snape's company drinking your worries away."
    
#    $ snape_against_hermione_02 = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.   
#    $ hermione_is_waiting_02 = True #Triggers another visit from Hermione. (Event_11)
   

    #$ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)
    hide screen bld1
    with d3
    $ days_without_an_event = 0 #Making sure next even will not start right away.
    jump day_start
   
   
######################################################################################   

    
####Snape bonus###
#label snape_bonus:
#    if snape_events == 1:
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=3
#            "Slytherin got +3 points as a Snape-Bonus."
    
#    if snape_events == 2:#WEEK No.2
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=7
#            "Slytherin got +7 points as a Snape-Bonus."
    
#    if snape_events == 3:#WEEK No.3
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=10
#            "Slytherin got +10 points as a Snape-Bonus."
            
#    if snape_events == 4:#WEEK No.4
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=12
#            "Slytherin got +12 points as a Snape-Bonus."
            
#    if snape_events == 5:#WEEK No.5
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=16
#            "Slytherin got +16 points as a Snape-Bonus."
            
#    if snape_events == 6:#WEEK No.6
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=22
#            "Slytherin got +22 points as a Snape-Bonus."
            
#    if snape_events == 7:#WEEK No.7
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=26
#            "Slytherin got +26 points as a Snape-Bonus."
            
#    if snape_events == 8:#WEEK No.8
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=32
#            "Slytherin got +32 points as a Snape-Bonus."
            
#    if snape_events == 9:#WEEK No.9
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=36
#            "Slytherin got +36 points as a Snape-Bonus."
            
#    if snape_events == 10:#WEEK No.10
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=43
#            "Slytherin got +43 points as a Snape-Bonus."
            
#    if snape_events == 11:#WEEK No.11
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=46
#            "Slytherin got +46 points as a Snape-Bonus."
            
#    if snape_events == 12:#WEEK No.12
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=50
#            "Slytherin got +50 points as a Snape-Bonus."
            
#    if snape_events == 13:#WEEK No.13
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=56
#            "Slytherin got +56 points as a Snape-Bonus."
            
#    if snape_events == 14:#WEEK No.14
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=61
#            "Slytherin got +61 points as a Snape-Bonus."
            
#    if snape_events == 15:#WEEK No.15
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=66
#            "Slytherin got +66 points as a Snape-Bonus."

#return




####################################
label wine_first:
    m "Look what I've got!"
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Hm..?"
    sna "Let me see..."
    hide screen s_head2    
    pause.1
    $ the_gift = "03_hp/18_store/27.png" # WINE.
    show screen gift
    with d3
    ">You hand over the bottle you found in the cupboard to professor Snape..." 
    hide screen gift
    with d3
    $ wine -= 1
    
    $ s_sprite = "03_hp/10_snape_main/24.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "This one has got to be from Albus' personal stash!"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Some pricey and incredibly rare stuff."
    hide screen s_head2 
    m "Shall we then?"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "We most certainly shall!"
    hide screen s_head2 
    show screen bld1
    with d3
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Your relationship with Professor Snape has improved."
    $ snape_friendship +=1
    hide screen bld1
    with d3
    return


label wine_not_first:
    m "Look what I've got!"
    hide screen s_head2    
    pause.1
    $ the_gift = "03_hp/18_store/27.png" # WINE.
    show screen gift
    with d3
    ">You hand over the bottle you fond in the cupboard to professor Snape..." 
    hide screen gift
    with d3
    $ wine -= 1
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Another one?"
    if one_of_ten == 1:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Splendid!"
    elif one_of_ten == 2:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Alright!"
    elif one_of_ten == 3:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Awesome!"
    elif one_of_ten == 4:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Well done, my friend!"
    elif one_of_ten == 5:
        $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Did you find Albus' secret stash or was it his personal wine cellar?"
    elif one_of_ten == 6:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "lately I am having hard time drinking anything but this!"
    elif one_of_ten == 7:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Great! I feel less stressed out already!"
    elif one_of_ten == 8:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "This just keeps getting better and better!"
    elif one_of_ten == 9:
        $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Seriously, how big is that stash?"
    elif one_of_ten == 2:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "It's sure good to be us! let's uncork that bastard!"
    
    hide screen s_head2 
    show screen bld1
    with d3
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Your relationships with Professor Snape have improved."
    $ snape_friendship +=1
    hide screen bld1
    with d3
    return
    
    
  ########
label not_today:
    if one_out_of_three == 1:
        sna "Sorry, I can't tonight..."
    elif one_out_of_three == 2:
        sna "Sorry, I have other business to attend to tonight..."
    elif one_out_of_three == 3:
        sna "Sorry, I have other plans. Maybe some other time?"
    
    jump snape_ready