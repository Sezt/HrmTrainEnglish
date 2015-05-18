
###################REQUEST_05 (Level 02) (BUTT MOLESTER).
label new_request_05:
    $herView.hideQQ()
    m "{size=-4}(I'll just molest her butt a little.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request

    
    if hermi.whoring <=2:
        jump too_much
        
#    if whoring >= 3 and whoring <= 5:
#        $ level = "02"
#        $ new_request_05_01 = True # HEARTS.
#    elif whoring >= 6 and whoring <= 8:
#        $ level = "03"
#        $ new_request_05_02 = True # HEARTS.
#    elif whoring >= 9:
#        $ level = "04"
#        $ new_request_05_03 = True # HEARTS.

    $SetHearts(GetStage(hermi.whoring, 3, 3, 3))

        
        
    if hermi.whoring >= 3 and hermi.whoring <= 5: # LEVEL 02 # Hermione is hesitant. <=================================================================================== FIRST EVENT.
        
        hide bld1
        with d3
        m "Come closer, child. Let me molest your butt a little."
        if IsFirstRun() and hermi.whoring <= 5: #First time
#        if request_05_points == 0 and whoring <= 5: #First time
            stop music fadeout 5.0
            $her_head_state = 7
            her_head_main "Professor Dumbledore!?"
            m "Relax, girl. It will be the easiest 15 points you've ever made, I promise."
            $her_head_state = 8
            her_head_main "But...."
            m "All I am going to do is squeeze your little butt a couple of times..."
            $her_head_state = 4
            her_head_main "This is inappropriate, professor................"
            m "Nobody needs to know how exactly you got the points..."
            $her_head_state = 12
            her_head_main "(These 15 points could really make a difference...)"
            $her_head_state = 19
            her_head_main "(Darn it.....!)"
        else:
            $her_head_state = 4
            her_head_main "Again.....?"
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
        her_head_main ".................."
        her_head_main "Do you want me to turn around then, sir?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Hm..."
            "\"Yes. Turn around, miss Granger.\"":
                her_head_main "As you say, sir..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
                her_head_main "............."
                her_head_main "..........................."
                $her_head_state = 25
                her_head_main "Sir, I would like to be done with this sooner rather then later..."
                m "Don't rush me girl... Let me savour the moment..."
                $her_head_state = 4
                her_head_main "............................."
                menu:
                    m "Hm..."
                    "-Give her butt a squeeze-":
                        pass
                    "-Give her butt a slap-":
                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                        show screen white
                        with hpunch
                        pause.08
                        hide screen white
                        show screen bld1
                        $her_head_state = 22
                        her_head_main "!!!!!!!!!!!!!"
                        her_head_main "Professor!!?"
                        menu:
                            "\"Fine, fine... I just couldn't resist....\"":
                                $her_head_state = 25
                                her_head_main "......................."
                                pass
                            "-Give her butt another slap-":
                                $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                show screen white
                                with hpunch
                                pause.08
                                hide screen white
                                show screen bld1
                                $her_head_state = 21
                                her_head_main "!!!!!!!!!!!!!"
                                $her_head_state = 15
                                her_head_main "Professor, what are you doing!?"
                                her_head_main "You said all you were going to do is touch!"
                                menu:
                                    "\"Fine, fine... I just couldn't resist....\"":
                                        $her_head_state = 25
                                        her_head_main "......................."
                                        pass
                                    "-Give her butt another slap-":
                                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                        show screen white
                                        with hpunch
                                        pause.08
                                        hide screen white
                                        show screen bld1
                                        $her_head_state = 15
                                        her_head_main "Ouch! It hurts!"
                                        $her_head_state = 20
                                        her_head_main "This is so demeaning!"
                                        her_head_main "You said all you were going to do is touch..."
                                        $her_head_state = 20
                                        her_head_main "Why are you doing this, professor?"
                                        g4 "Just stand still, miss Granger!"
                                        $her_head_state = 19
                                        her_head_main "I don't think so, sir!"
                                        $her_head_state = 24
                                        her_head_main "No amount of points are worth this humiliation!"
                                        $her_head_state = 23
                                        her_head_main "You are abusing your power, sir!"
                                        g4 "What?"
                                        $her_head_state = 19
                                        her_head_main "I'm leaving!"
                                        menu:
                                            g4 "Tsk..."
                                            "\"I... I apologize...\"":
                                                $her_head_state = 25
                                                her_head_main "Just don't do this anymore, sir..."
                                                pass
                                            "\"You are not getting any points for this!\"":
                                                $ hermi.liking -= 30
                                                $her_head_state = 20
                                                her_head_main "Ha! See if I care, sir!"
                                                ### Takes place aftre you refuse to pay her the очков.
                                                $ walk_xpos=300 #Animation of walking chibi. (From)
                                                $ walk_xpos2=610 #Coordinates of it's movement. (To)
                                                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie
                                                show screen hermione_walk_01_f 
                                                with fade
                                                pause 2
                                                hide screen hermione_walk_01_f 
                                                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                                                with Dissolve(.3)
                                                pause.5
                                                g4 "Tsk! (You little brat!)"
#                                                $ request_05_points += 1
                                                if daytime:
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu
                                            "\"I'm subtracting points from you then!\"":
                                                $ hermi.liking -= 20
                                                $her_head_state = 22
                                                her_head_main "You can't be serious!?"
                                                $ gryffindor -=10
                                                g4 "The \"Gryffindor\" house, minus 10 points!"
                                                g4 "There! It's done!"
                                                $her_head_state = 24
                                                her_head_main "Gr..........."
                                                her_head_main "........................"
                                                $her_head_state = 27
                                                her_head_main "This is not fair..."
                                                m "What? Hey, wait, don't you start crying on me..."
                                                $her_head_state = 29
                                                her_head_main "I hate you, professor! I hate you!"
                                                
                                                $ walk_xpos=300 #Animation of walking chibi. (From)
                                                $ walk_xpos2=610 #Coordinates of it's movement. (To)
                                                $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie
                                                show screen hermione_run
                                                with fade
                                                pause.9
                                                hide screen hermione_run
                                                with Dissolve(.3)
                                                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                                                m ".............."
                                                menu:
                                                    "\"Dammit. Now I feel like crap...\"":
                                                        $ hermi.liking += 5
                                                        m "Dammit... Now I feel like crap..."
                                                        m "But who could resist slapping that little behind of her's?"
                                                        #m "Но кто бы смог устоять и не шлепнуть ее великолепную попку?"
                                                    "\"She made me do this, that brat!\"":
                                                    #"\"Эта девица, все из-за нее!\"":
                                                        $ hermi.liking -= 9
                                                        m "She made me do this, that brat!"
                                                        m "Acting all wounded now..."
                                                        m "I bet she actually enjoyed the slapping and just won't admit it..."
                                                        #m "Она подтолкнула меня к этому!"
                                                        #m "А теперь строит из себя оскробленную..."
                                                        #m "Я уверен что ей понравились эти шлепки, она просто не хочет в этом признаться..."
#                                                $ request_05_points += 1
                                                if daytime:
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu     
        
                pause
                show screen groping_02
                with d7
                $her_head_state = 7
                her_head_main "!!!!!!?"
                m "What is it, miss Granger?"
                $her_head_state = 15
                her_head_main "It's nothing professor..."
                her_head_main "It's just... "
                her_head_main "I can't believe this is really happening..."
                her_head_main "This is so... inappropriate..."
                #m "Relax, girl. It's not like you are enjoying this..."
                m "Relax, girl. It's not like you are enjoying this..."
                $her_head_state = 19
                her_head_main "What? Of course not! This is depraved..."
                her_head_main "I am making this sacrifice for the the honour of my house..."
                m "Yes, concentrate on that..."
                $her_head_state = 20
                her_head_main "...................."
                show screen bld1
                with d3
                pause
                $her_head_state = 17
                her_head_main "But, professor..."
                $her_head_state = 5
                her_head_main "Why are {size=+7}you{/size} doing this?"
                menu: 
                    m "Hm..."
                    "\"I have my reasons...\"":
                        $her_head_state = 12
                        her_head_main "Oх..."
                        $her_head_state = 25
                        her_head_main "Хм..."
                    "\"In the name of science of course!\"":
                        $her_head_state = 3
                        her_head_main "really?!"
                        her_head_main "Is this a research of some kind?"
                        m "Yeah, sure, I'm researching ehm... er..."
                        m "Well, you wouldn't understand, this is some pretty advanced wizardry stuff..."
                        her_head_main "I see..."
                        $her_head_state = 2
                        her_head_main "Well, if it is for a research then I am glad to be of help..."
                    "-Just squeeze her butt cheeks tighter-":
                        ">You give Hermione's butt cheeks a couple of extra firm squeezes."
                        $her_head_state = 5
                        her_head_main "...................."
                        $her_head_state = 12
                        her_head_main "(Shall I just be quiet then.....?)"
                show screen blktone8
                with d3
                ">You continue to play with Hermione's buttocks..."
                ">You spend your hands down..."
                $her_head_state = 15
                her_head_main "................"
                label connection_of_rapes:
                menu:
                    "-Slide your hands under her panties-":
                        ">You slowly slide one of your hands under the fabric of the girl's panties..."
                        $her_head_state = 7
                        her_head_main "Professor... What are you...?"
                        m "That's alright, just think about those 15 points your house is about to receive..."
                        $her_head_state = 12
                        her_head_main "............."
                        menu:
                            "-Prod her pussy with one of your fingers-":
                                show screen blkfade
                                with d3
                                ">You slide one of your fingers down and place it against the girl's little slit..."
                                $her_head_state = 7
                                her_head_main "Professor? No! What are you...?"
                                ">Hermione tries to pull away from you..."
                                menu:
                                    "-Force your finger into her pussy!-":
                                        ">You force one of your fingers into her little pussy..."
                                        ">It's very tight and warm..."
                                        ">Also it is relatively dry... Doesn't look like Hermione's taking any pleasure in this..."
                                        jump screams_of_rapings
                                    "-Let the girl go...-":
                                        pass
                            "-Prod her butt-hole instead-":
                                show screen blkfade
                                with d3
                                ">You place your one of your thumbs against the girl's little butt-hole..."
                                her_head_main "Professor? No! What are you doing!?"
                                ">Hermione tries to pull away from you..."
                                menu:
                                    "-Force your thumb into her butt-hole-":
                                        ">You force one of your thumbs into her little butt-hole..."
                                        with hpunch
                                        $her_head_state = 30
                                        her_head_main "!!?"
                                        ">It's very tight and warm inside..."
                                        jump screams_of_rapings
                                    "-Let the girl go...-":
                                        pass
                            "-Stop pushing your luck. Dismiss the girl-":
                                pass
                    "-No. That's enough for today. Dismiss her-":
                        pass
            "\"No. Just stand still, miss Granger.\"":
                $her_head_state = 4
                her_head_main "As you say, sir..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_01
                with d1
                hide screen blkfade
                with d5
                pause
                $her_head_state = 1
                her_head_main "Sir, please hurry up, before someone discovers us like this..."
                m "What is the problem, miss Granger?"
                m "You know you are doing this for your house."
                $her_head_state = 4
                her_head_main "I do know."
                her_head_main "But not everyone would see it that way..."
                her_head_main "So let us be done with this as quick as possible..."
                $her_head_state = 5
                her_head_main "Please..."
                m "Well, if you insist..."
                show screen groping_01
                with d7
                $her_head_state = 7
                her_head_main "!!!"
                m "What is it?"
                $her_head_state = 5
                her_head_main "It's nothing, sir. Your hands are cold, that's all..."
                show screen bld1 
                with d3
                show screen blktone8
                with d3
                ">You run your hands up and down Hermione's legs..."
                $her_head_state = 4
                her_head_main "........................."
                ">You give her buttocks a good squeeze..."
                $her_head_state = 19
                her_head_main "................."
                m "Don't look away, girl. I want you to look into my eyes."
                her_head_main "I would rather not, sir..."
                menu:
                    m "..."
                    "\"Fine. Just keep standing still then.\"":
                        $her_head_state = 15
                        her_head_main "Thank you sir..."
                        ">You massage her buttocks lightly..."
                        her_head_main "...................."
                        ">And keep enjoying the sensation of her ass under your hands..."
                        $her_head_state = 19
                        her_head_main "....................."
                        ">Then you give Hermione's butt one last squeeze."
                        her_head_main "....................."
                    "\"Open your eyes, or lose the points!\"":
                        $ hermi.liking -= 7
                        her_head_main "Tsk! {size=-5}(You perverted old--{/size}"
                        m "Did you say something, Miss Granger?"
                        $her_head_state = 8
                        her_head_main "It's nothing, sir."
                        ">You massage her buttocks lightly..."
                        ">Hermione maintains the eye contact as she's been told..."
                        her_head_main "...................."
                        $her_head_state = 4
                        her_head_main "..............................."
                        m "What did I tell you about looking away?"
                        $her_head_state = 19
                        her_head_main "Yes, I remember..."
                        $her_head_state = 8
                        her_head_main "................................."
                        $her_head_state = 25
                        her_head_main "..................................."
                        her_head_main ".................................................."
                        ">You keep on enjoying the sensation of her soft ass-cheeks under your fingertips..."
                        $her_head_state = 8
                        her_head_main "....................."
                        jump connection_of_rapes
    
        
    elif hermi.whoring >= 6 and hermi.whoring <= 14: # LEVEL 04 # Hermione is hesitant. <=================================================================================== SECOND EVENT.
#        $ new_request_05_02 = True # HEARTS.
        hide screen bld1
        with d3
        m "Come closer, girl. Let me molest your butt a little."
        $her_head_state = 17
        her_head_main "If I must..."
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
        $her_head_state = 18
        her_head_main "Do you want me to turn around then, sir?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Hm..."
            "\"Yes. Turn around, miss Granger.\"":
                her_head_main "As you say, sir..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
                $her_head_state = 35
                her_head_main "............."
                menu:
                    m "Hm..."
                    "-Give her butt a squeeze-":
                        pass
                    "-Give her butt a slap-":
                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                        show screen white
                        with hpunch
                        pause.08
                        hide screen white
                        show screen bld1
                        $her_head_state = 22
                        her_head_main "!!!!!!!!!!!!!"
                        $her_head_state = 18
                        her_head_main "Professor....?"
                        menu:
                            "\"Fine, fine... I just couldn't resist....\"":
                                her_head_main "It's Ok..."
                                pass
                            "-Give her butt another slap-":
                                $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                show screen white
                                with hpunch
                                pause.08
                                hide screen white
                                show screen bld1
                                $her_head_state = 21
                                her_head_main "!!!!!!!!!!!!!"
                                $her_head_state = 18
                                her_head_main "Professor, what are you doing!?"
                                her_head_main "You said all you are going to do is touch!"
                                menu:
                                    "\"Fine, fine... I just couldn't resist....\"":
                                        her_head_main "It's not a big deal..."
                                        pass
                                    "-Give her butt another slap-":
                                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                        show screen white
                                        with hpunch
                                        pause.08
                                        hide screen white
                                        show screen bld1
                                        $her_head_state = 34
                                        her_head_main "Professor, not so loud, please..."
                                        her_head_main "What if somebody hears us?"
                                        m "Alright, alright... proceeding with groping then..."
                                        $her_head_state = 18
                                        her_head_main "................"

                pause
                show screen groping_02
                with d7
                her_head_main "..................."
                m "You are being awfully quiet today, miss granger."
                her_head_main "Am I...?"
                $her_head_state = 35
                her_head_main "Well, you know me, sir..."
                her_head_main "I'm just happy to be able to do my part for the \"Gryffindor\" house...."
                her_head_main "Please don't mind it and continue..."
                $her_head_state = 18
                her_head_main "(...to grope me...)"
                show screen blktone8
                with d3
                ">You keep on playing with Hermione's ass..."
                ">And continue sliding your hands up and down her inner tighs..."
                #">Ваша рука продолжает скользить по внутренней части ее бедра..."
                her_head_main "................"
                label connection_of_rapes_02:
                menu:
                    "-Slide your hands under her panties-":
                        ">You slowly slide one of your hands under the fabric of the girl's panties..."
                        $her_head_state = 17
                        her_head_main "Professor... What are you...?"
                        m "It's alright, just think about those 15 points your house is about to receive..."
                        her_head_main "As you say..."
                        menu:
                            "-Prod her pussy with one of your fingers-":
                                show screen blkfade
                                with d3
                                ">You slide one of your fingers down and place it against the girl's little slit..."
                                $her_head_state = 18
                                her_head_main "Professor?" 
                                menu:
                                    "-Force your finger into her pussy!-":
                                        ">You force one of your fingers into her little pussy..."
                                        ">It's very tight and warm..."
                                        ">it is quite wet as well...  Seems like Hermione's taking pleasure in this..."
                                        jump screams_of_pleasure
                                    "-Let the girl go...-":
                                        pass
                            "-Prod her butt-hole instead-":
                                show screen blkfade
                                with d3
                                ">You place your one of your thumbs against the girl's little butt-hole..."
                                her_head_main "Professor? What are planning on doing?"
                                menu:
                                    "-Force your thumb into her butt-hole-":
                                        ">You force one of your thumbs into her little butt-hole..."
                                        with hpunch
                                        $her_head_state = 36
                                        her_head_main "ah... your finger is up my..."
                                        ">It's very tight and warm inside..."
                                        jump screams_of_pleasure
                                    "-Let the girl go...-":
                                        pass
                            "-Stop pushing your luck. Dismiss the girl-":
                                pass
                    "-No. That's enough for today. Dismiss her-":
                        pass
            "\"No. Just stand still, miss Granger.\"":
                $her_head_state = 4
                her_head_main "As you say, sir..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_01
                with d1
                hide screen blkfade
                with d5
                pause
                $her_head_state = 1
                her_head_main "Sir, please hurry up, before someone discovers us like this..."
                m "What's the problem, miss Granger?"
                m "You know you are doing this for your house."
                $her_head_state = 4
                her_head_main "I do know."
                her_head_main "But not everyone would see it that way..."
                her_head_main "So let us be done with this as quick as possible..."
                $her_head_state = 5
                her_head_main "Please..."
                m "Well, if you insist..."
                show screen groping_01
                with d7
                $her_head_state = 7
                her_head_main "!!!"
                m "What is it?"
                $her_head_state = 5
                her_head_main "nothing, sir. Your hands are cold, that's all..."
                show screen bld1 
                with d3
                show screen blktone8
                with d3
                ">You run your hands up and down Hermione's legs..."
                $her_head_state = 4
                her_head_main "........................."
                ">And give her Ass a good squeeze..."
                $her_head_state = 19
                her_head_main "................."
                m "Don't look away, girl. I want you to look into my eyes."
                her_head_main "I would rather not, sir..."
                menu:
                    m "..."
                    "\"Fine. Just keep on standing still then.\"":
                        $her_head_state = 15
                        her_head_main "Thank you sir..."
                        ">You massage her ass-cheeks lightly..."
                        her_head_main "...................."
                        ">And keep enjoying the sensation of her butt under your hands..."
                        $her_head_state = 19
                        her_head_main "....................."
                        ">Then You give Hermione's butt one last squeeze."
                        her_head_main "....................."
                    "\"Open your eyes, or you'll lose the points!\"":
                        $ hermi.liking -= 20
                        her_head_main "Tsk! {size=-5}(You perverted old--{/size}"
                        m "Did you say something, Miss Granger?"
                        $her_head_state = 8
                        her_head_main "It's nothing, sir."
                        ">You massage her ass-cheeks lightly..."
                        ">Hermione maintains eye contact as she's been told..."
                        her_head_main "...................."
                        $her_head_state = 4
                        her_head_main "..............................."
                        m "What did I tell you about looking away?"
                        $her_head_state = 19
                        her_head_main "Yes, I remember..."
                        $her_head_state = 8
                        her_head_main "................................."
                        $her_head_state = 25
                        her_head_main "..................................."
                        her_head_main ".................................................."
                        ">You keep enjoying the sensation of her soft buttocks under your fingertips..."
                        $her_head_state = 8
                        her_head_main "....................."
                        jump connection_of_rapes_02  
        
    elif hermi.whoring >= 15: # LEVEL 05 # Hermione is more then willing. <=================================================================================== SECOND EVENT.
#       $ new_request_05_02 = True # HEARTS.
        hide screen bld1
        with d3
        m "Come over here, girl. I have a special surprise planned for you today."
        $her_head_state = 18
        her_head_main "Oh you have. Alright then."
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
        $her_head_state = 17
        her_head_main "Do you want me to turn around then, sir?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Hm..."
            "\"Yes. Turn around for me.\"":
                her_head_main "As you wish, sir..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
                $her_head_state = 35
                her_head_main "You may notice that I have a surprise for you as well..."
                m "Ohh I love surprises, Miss Granger, even more so when said with such a teasing tone."
                menu:
                    m "Well, lets see..."
                    "-Give her butt a squeeze-":
                        ">Moving your hands up her thighs ending on her bare bottom<"
                        m "Ohh how wonderful, miss Granger. Nothing between my fingers and your soft skin."
                        $her_head_state = 34
                        her_head_main "I am happy that you like it, sir"
                        pass
                    "-Give her butt a slap-":
                        ">You lift her skirt to make room for a good slap<"
                        m "Ohh Miss Granger, I love it. You seem to have left your panties at home"
                        $her_head_state = 34
                        her_head_main "Well yes, they are somewhat in the way these days"
                        m "I couldn't agree more. Your fine behind shouldn't be hindered in any way"
                        m "It should make this more enjoyable as well"
                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                        show screen white
                        with hpunch
                        pause.08
                        hide screen white
                        show screen bld1
                        $her_head_state = 15
                        her_head_main "Uhh..."
                        $her_head_state = 39
                        her_head_main "What are you up to, sir?"
                        menu:
                            "\"Just checking the firmness...very nice, miss\"":
                                her_head_main "Oh alright..."
                                pass
                            "-Give her butt another slap-":
                                $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                show screen white
                                with hpunch
                                pause.08
                                hide screen white
                                show screen bld1
                                $her_head_state = 15
                                her_head_main "Mmmmhh..."
                                $her_head_state = 01
                                her_head_main "It does hurt a bit more without panties"
                                her_head_main "But in a slightly good way."
                                m "Enough slapping for now"
                                jump fingering_behind_01
                                
            "\"No. Facing me is fine, miss Granger.\"":
                $her_head_state = 01
                her_head_main "As you wish, sir..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_01
                with d1
                hide screen blkfade
                with d5
                pause
                show screen groping_01
                with d7
                m "Ohh how lovely, miss Granger. No panties to hinder our progress!"
                $her_head_state = 35
                her_head_main "Yes sir, it does make a lot of things easier..."
                m "Excellent!"
                ">You massage her ass and slowly grasp her butt more firmly<"
                her_head_main "Hmmm...yes...."
                her_head_main "..................."
                her_head_main "Ohh I almost forgot...you mentioned something about a surprise..."
                ">You squeeze her cheeks and move a finger around her tiny hole<"
                m "Ahh yes. I have been thinking about doubling your fee for this service."
                $her_head_state = 03
                her_head_main "Mmmmh....."
                $her_head_state = 35
                her_head_main "Well...there must be ahhh reason for your generosity..."
                m "Just to open up some further options when exploring these sensations..."
                her_head_main "That does sound fair enough...ahhgreed..."
                m "Alright. Please turn around so I can get a better look at your lovely naked bottom, miss."
                her_head_main "Ohh yes, sure..."
                pause
                show screen groping_02
                with d7
                jump fingering_start_01
                
                        
                pause
                show screen groping_02
                with d7
                her_head_main "..................."
                m "Is something on your mind, miss granger."
                her_head_main "Oh, just thinking about the surprise you mentioned..."
                $her_head_state = 35
                m "Ahh yes, of course, I almost forgot all about it..."
                m "Your lovely naked bum distracted me a bit."
                ">You grab both buttcheeks a bit firmer and continue the massage<"
                $her_head_state = 38
                her_head_main "uhh Professor, that is pretty distracting as well"
                her_head_main "Not that you need to stop..."
                $her_head_state = 01
                m "I was thinking that we could move on to a more advanced curriculum."
                ">You run a finger down between her cheeks and circle her tiny hole<"
                $her_head_state = 03
                her_head_main "Ohh that is new"
                $her_head_state = 15
                her_head_main "Mmmm...If the price is right I am willing to explore some new knowledge, sir."
                m "Let's double the normal fee and see where that takes us"
                $her_head_state = 15
                her_head_main "That sounds fair...mmmh"
                label fingering_start_01:
                ">You continue to play with Hermione's ass..."
                her_head_main "................"
                menu:
                    "-Massage her ass and play with her butt-hole-":
                        ">You slowly slide one of your hands under the fabric of the girl's panties..."
                        $her_head_state = 17
                        her_head_main "Professor... What are you...?"
                        m "It's alright, just think about those 15 points your house is about to receive..."
                        her_head_main "As you say..."
                        menu:
                            "-Prod her pussy with one of your fingers-":
                                show screen blkfade
                                with d3
                                ">You slide one of your fingers down and place it against the girl's little slit..."
                                $her_head_state = 18
                                her_head_main "Professor?" 
                                menu:
                                    "-Force your finger into her pussy!-":
                                        ">You force one of your fingers into her little pussy..."
                                        ">It's very tight and warm..."
                                        ">it is quite wet as well...  Seems like Hermione's taking pleasure in this..."
                                        jump screams_of_pleasure
                                    "-Let the girl go...-":
                                        pass
                            "-Prod her butt-hole instead-":
                                show screen blkfade
                                with d3
                                ">You place your one of your thumbs against the girl's little butt-hole..."
                                her_head_main "Professor? What are planning on doing?"
                                menu:
                                    "-Force your thumb into her butt-hole-":
                                        ">You force one of your thumbs into her little butt-hole..."
                                        with hpunch
                                        $her_head_state = 36
                                        her_head_main "ah... your finger is up my..."
                                        ">It's very tight and warm inside..."
                                        jump screams_of_pleasure
                                    "-Let the girl go...-":
                                        pass
                            "-Stop pushing your luck. Dismiss the girl-":
                                pass
                    "-No. That's enough for today. Dismiss her-":
                        pass
            
  
  
  
    
        
label ending_of_screams_of_pleasure:
    if hermi.whoring <= 5:
        $ hermi.whoring +=1
    show screen blkfade 
    with d5
    
    stop music fadeout 1.0
    ">You let go of her ass..."
    m "This will do for now."
    
    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    show screen hermione_02
    show screen genie
    with d1
    
    hide screen blkfade
    with d3

    $ gryffindor +=15
    m "The \"Gryffindors\" get 15 points!"
    
#    $ request_05_points += 1
   
   
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
        her "I'd better go now then. It's getting pretty late..."
    

    hide screen bld1
    $herView.hideQ( Dissolve(.3) )
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ hermione_chibi_xpos = 610 #Near the desk.
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    
    if hermi.whoring >= 3 and hermi.whoring <= 5: #First level. Not happy.
        $her_head_state = 12
        her_head_main "..........................."
        
        
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5

    call music_block # Lunches apropriete BGM day/night.

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu



### ALL THE SCREAMS ABOUT RAPE ###
label screams_of_rapings:
    $her_head_state = 10
    her_head_main "NO! What have you done!!?"
    ">Hermione gives you an unexpectedly strong shove..."
    with hpunch
    her_head_main "Why would you do this to me, sir...?"
    $her_head_state = 27
    her_head_main "I never agreed to... to..."
    her_head_main "You... you..."
    with hpunch
    $her_head_state = 29
    her_head_main "{size=+7}YOU RAPED ME!{/size}"
    g4 "What? Don't be ridiculous, girl! I did no such thing!"
    her_head_main "Yes you did! Yes you did!"
    g4 "I most certainly did not!"
    her_head_main "No, you did, professor!"
    $her_head_state = 31
    her_head_main "Now, you will give me 20--"
    her_head_main "No, 100 house points or I am reporting you to the Ministry of magic!"
    menu:
        m "(Ah, crap...)"
        "\"Alright, alright... 100 points it is...\"":
            $ gryffindor +=100
            m "One hundred points to \"Gryffindor\" !"
            m "There, it is done..."
            m "Now would you calm yourself down, miss Granger?"
            $her_head_state = 29
            her_head_main "No, I will not!"
            her_head_main "I've just been raped!"
            g4 "Oh, snap out of it girl, I didn't rape you! All I did was--"
            with hpunch
            her_head_main "{size=+7}You raped me!!!{/size}"
            g4 "By the great desert sands, would you keep it down about the rapes!?"
            g4  "Someone may hear you!"
            her_head_main "Good! I want them to hear!"
            m "Why would you want that? I already paid you!"
            $her_head_state = 32
            her_head_main "Oh... right..."
            $her_head_state = 33
            her_head_main "But I hate you! I hate you professor!"
            $ hermi.liking -=30

        "\"You're bluffing, girl!\"":
            $her_head_state = 29
            her_head_main "No, I'm not! I'm gonna do it!"
            g4 "By all means, go ahead..."
            g4 "There was no rape!"
            her_head_main "I hate you, professor!"
            $ hermi.liking -=50


    hide screen bld1
    hide screen ctc
    $herView.hideQ()
    show screen genie
    hide screen groping_01
    hide screen groping_02
    hide screen blkfade
    hide screen blktone8
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ hermione_chibi_xpos = 610 #Near the desk.
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)

    if hermi.whoring >= 3 and hermi.whoring <= 5: #First level. Not happy.
        $her_head_state = 12
        her_head_main "..........................."
        

        
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5

    $event.Finalize()    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
    


########### SCREAM OF PLEASURES ###        
label screams_of_pleasure:
    $her_head_state = 34
    her_head_main "Ah...."
    her_head_main "It's inside of me..."
    $her_head_state = 18
    her_head_main "No, professor, you must stop now..."
    m "Why? You don't like it?"
    her_head_main "It doesn't matter whether I like this or not, sir."
    her_head_main "You know why I'm doing this..."
    her_head_main "And it is wrong for me to let you do this to me for a meagre 15 points..."
    ">Hermione pulls away from you..."
    m "Heh... I see..."
    m "Well, in that case..."
    jump ending_of_screams_of_pleasure

    
