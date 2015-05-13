
#####################################################################################################################################################################
### LEVEL 03 ###########################################################################################################################################################
###################REQUEST_08 (Level 03) (Show me tits). #####################################################################################################################
label new_request_08: #LV.3 (Whoring = 6 - 8)
    $herView.hideQQ()
    if IsFirstRun():
#    if request_08_points == 0:
        m "{size=-4}(I want to see those boobs?){/size}"
    else:
        m "{size=-4}(I want to see those boobs again?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's try it.)\"":
            show screen blktone
            with d3
            pass
        "\"(Not now.)\"":
            $event.NotFinished()
            jump new_personal_request
    
    if hermi.whoring <=5:
        jump too_much
        
    
        
    $ current_payout = 25 #Used when haggling about price of th favor.
        
    $ pos = POS_140
    
    # we'll undress her, so save the state
    $herView.data().saveState()

    if IsFirstRun() and hermi.whoring <= 11: # LEVEL 04 # FIRST TIME.
        m "Miss Granger?"
        $herView.hideQQ()
        $ pos = POS_370
        
        $herView.showQQ( "body_03.png", pos )
        her "Yes, sir..."
        m "How much will it cost me to see your tits?"
        $herView.hideshowQQ( "body_14.png", pos )
        stop music fadeout 1.0
        her "How much will it cost you to...?"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $herView.hideshowQQ( "body_30.png", pos )
        her "Professor Dumbledore!"
        m "Hm... I thought your house could use some extra points..."
        m "But I guess I was wrong..."
        $herView.hideshowQQ( "body_31.png", pos )
        her ".........?"
        m "Please don't mind me..."
        m "All I want to do is help you..."
        $herView.hideshowQQ( "body_29.png", pos )
        her "............."
        $herView.hideshowQQ( "body_33.png", pos )
        her "200 house points, sir."
        m "So if I give you 200 house points, miss Granger..."
        m "You will shamelessly bare your melons before me?"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Professor Dumbldore! No need to be so vulgar!"
        her "I think I'd better go..."
        menu:
            "\"Wait. 200 points are yours. Show me!\"":
                $ current_payout = 200 #Used when haggling about price of the favor.
                $herView.hideshowQQ( "body_14.png", pos )
                her "Really?"
                m "Well?"
                $herView.hideshowQQ( "body_29.png", pos )
                her "......................................"
                her "You have to promise me not to touch them, sir."
                m "Sure, sure..."
                $herView.hideshowQQ( "body_32.png", pos )
                her "I am only doing this for the honour of my house, sir!"

            "\"I will give you 5 points to see your tits.\"":
                $herView.hideshowQQ( "body_72.png", pos )
                her "Five?!"
                $herView.hideshowQQ( "body_76.png", pos )
                her "Professor, I am not going to expose myself for a meagre five points!"
                m "Well, your tits sure aren't worth 200, girl!"
                $herView.hideshowQQ( "body_73.png", pos )
                her "(They aren't?)"
                $herView.hideshowQQ( "body_69.png", pos )
                her "Maybe a hundred points?"
                menu:
                    "\"Fine. 100 it is! Bare them already!":
                        $ current_payout = 100 #Used when haggling about price of th favor.
                        her "................."
                        her "So be it... For a hundred points..."
                    "\"25 house points that's my final offer!\"":
                        her "..............."
                        her "Well, so be it..."
            "\"Fine, leave. I don't care...\"":
                $hermi.liking -= 12
                her "argh!"
                call music_block
                
                jump loadState_and_could_not_flirt
                
                
        hide screen blktone
        with d3
        hide screen bld1
        with d3
        $herView.hideQ( d5 )
        $ menu_x = 0.5 #Default menu position restored.
        show screen ctc
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        pause
        show screen hermione_04
        with fade
        pause
        show screen bld1
        with d3
        m "Hm..."
        $her_head_state = 12
        her_head_main "{size=-5}(My breasts are completely exposed...){/size}"
        m "Come closer girl, let me take a better look..."
        $her_head_state = 4
        her_head_main "............"
        
        hide screen bld1
        with d3

        show screen blkfade #Completely black screen.
        with Dissolve(1)
        pause.5
        ">Hermione slowly walks towards your desk."
        ">With every step she takes her ample tits bounce a little..."
       
        hide screen hermione_04 #Stands with tits out.
        hide screen genie
        show screen ctc
        show screen genie_and_tits_01
        with d1
        hide screen blkfade
        with d5
        pause
        show screen bld1
        with d3
        $her_head_state = 1
        her_head_main "............"
        m "Very good..."
        $her_head_state = 4
        her_head_main "....."


        show screen blktone 
        with d3
        $herView.hideQQ()
        
        $ pos = POS_140
        #$ only_upper = True #No lower body displayed. 
        
        # add tits pose!
        call addTitsPose
    
        $herView.showQQ( "body_81.png", pos )
        pause
        her "...................................."
        
        
    else:
        if hermi.whoring >= 6 and hermi.whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).
            m "Miss Granger?"
            $her_head_state = 2
            her_head_main "Yes, professor?"
            m "I need to see your tits."
            $her_head_state = 4
            her_head_main "............"
            her_head_main "Do you promise not to touch, sir?"
            m "Of course."
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            $herView.hideQ( d5 )
            $ menu_x = 0.5 #Default menu position restored.
            show screen ctc
            pause
            show screen hermione_04
            with fade
            pause
            show screen bld1
            with d3
            m "Hm..."
            m "Come closer girl, let me take a better look..."
            hide screen bld1
            with d3
            show screen blkfade #Completely black screen.
            with Dissolve(1)
            pause.5
            ">Hermione slowly walks towards your desk."
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen ctc
            show screen genie_and_tits_01
            with d1
            hide screen blkfade
            with d5
            pause
            show screen bld1
            with d3
            m "Very good..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            show screen blktone 
            with d3
            $herView.hideQQ()
            
            # add tits pose!
            call addTitsPose

            $herView.showQQ( "body_81.png", pos )
            #$ only_upper = True #No lower body displayed. 

            pause
            her "...................................."
            
            
            
            
        elif hermi.whoring >= 9: # LEVEL 04 and higher# <=================================================================================== SECOND EVENT and THIRD EVENT. (HERMIONE IS INDIFFERENT) 
            m "I need to see your tits, miss Granger."
            $her_head_state = 15
            her_head_main "Are you only going to watch, sir?"
            m "Of course..."
            if hermi.whoring >= 15:
                $herView.hideshowQQ( "body_09.png", pos )
                her "Sir, we both know that you never just watch, you touch and do more..."
                m "Maybe {size=+4}YOU{/size} are interested, miss Granger, in me doing something else?"
                $herView.hideshowQQ( "body_17.png", pos )
                her "Sir, let us not play games. I need this for my house, you need sex."
                her "It does not give me pleasure, but if you need it, I am ready to earn more."
                m "You have a new part-time job, miss Granger?"
                $herView.hideshowQQ( "body_47.png", pos )
                her "What?.. SIR! I'm talking about how to earn points!"
                m "Oh, excuse me, but I thought..."
                $herView.hideshowQQ( "body_51.png", pos )
                her "You thought wrong! I will never stoop to that!"
                m "Well, miss, if we are talking about how to earn more points..."
                $herView.hideshowQQ( "body_47.png", pos )
                her "Only about that, sir!"
                m "Then let us take care of your ass."
                if hermi.whoring<21:
                    $herView.hideshowQQ( "body_95.png", pos )
                    her "Ass, sir? In the sense that you touch..." 
                    m "I mean, I will touch it with my dick..."
                    $herView.hideshowQQ( "body_48.png", pos )
                    her "But, sir! What are you... I didn't mean..." 
                    m "Didn't mean? And what do you think I should give you more points for? For a Christmas song?"
                    $herView.hideshowQQ( "body_32.png", pos )
                    her "But I'm not ready for that!!!"
                    m "Why are you messing with me head, miss, telling me you want to earn more points?"
                    $herView.hideshowQQ( "body_120.png", pos )
                    her "I want to, sir, but not at this price!"
                    m "What, you are now telling me what to buy?"
                    m "You know, miss, I'm partial to Gryffindor..." 
                    m "But because of your whims I seriously consider, whether I was mistaken in you?"
                    m "Could I call some girls from Slytherin? Surely, they are more loyal to their house."
                    m "Yes! Great idea. Miss Granger, please fetch professor Snape." 
                    m "Surely he could recommend me a {size=+4}DECENT{/size} candidate."
                    $herView.hideshowQQ( "body_117.png", pos )
                    her "Professor, please..."
                    m "What, miss Granger? Are you not able to?"
                    $herView.hideshowQQ( "body_67.png", pos )
                    her "Professor, I was wrong... I was wrong... please forgive me."
                    m "And what will happen tomorrow?"
                    m "You will again belittle points?"
                    her "No, sir, I understood."
                    $herView.hideshowQQ( "body_55.png", pos )
                    her "If you want to see my Boobs, then I must show you Tits and not bargain for points."
                    m "..............................."
                    her "............................."
                    menu:
                        "Forgive":
                            m "It seems you don't understand, miss Granger, that I find all possible jobs for you."
                            m "You should be grateful."
                            $herView.hideshowQQ( "body_29.png", pos )
                            her "I am grateful, sir, truely."
                            m "And as thanks today you show your Boobs for free. Right?"
                            $herView.hideshowQQ( "body_103.png", pos )
                            her "Uh... Y-Yes, sir."
                            $current_payout=0
                        "Punish":
                            $herView.hideshowQQ( "body_61.png", pos )
                            m "You understand, miss, that you are guilty and should be punished?"
                            her "P-probably..."
                            m "What, you are not sure?"
                            $herView.hideshowQQ( "body_103.png", pos )
                            her "No, I'm sure... probably."
                            m "I'm not going to bother you with a complex trial, just suck me. You love it..."
                            $herView.hideshowQQ( "body_47.png", pos )
                            her "Nothing like..."
                            m "What? Or should I choose a worse punishment?"
                            $herView.hideshowQQ( "body_34.png", pos )
                            her "Umm... Well, sir. Yes, I do love it."
                            m "You love what..?"
                            $herView.hideshowQQ( "body_47.png", pos )
                            her "I love... to suck, sir."
                            m "Wonderful. But this punishment has not turned into pleasure, this time I'm not going to pay you."
                            her "Yes, sir."
                            m "On the contrary, you will pay me for the pleasure. I will deduct the points from Gryffindor."
                            $herView.hideshowQQ( "body_130.png", pos )
                            her "But, sir!"
                            m "You think this is unfair, young lady?"
                            $herView.hideshowQQ( "body_47.png", pos )
                            her "....................................."
                            m "I can't hear you!"
                            $herView.hideshowQQ( "body_120.png", pos )
                            her "Well, if you say so..."
                            m "Excellent! Then treat yourself."
                            her "You mean, should I...?"
                            g9 "Go ahead, miss. Enjoy sucking my dick."
                            $current_payout=-55
                            jump blowjob_jumping
                else:
                    her "Thank you, sir."
                    menu:
                        "Change my mind":
                            m "However, I changed my mind, miss Granger." 
                            m "Today we will restrict ourselves to the view of your Boobs!"
                            $herView.hideshowQQ( "body_50.png", pos )

                            her "................"
                            m "Lets start."
                        "\"Then let's get started!\"":
                            m "Well..."
                            $current_payout=95
                            jump new_request_31_start
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            $herView.hideQ( d5 )
            $ menu_x = 0.5 #Default menu position restored.
            show screen ctc
            pause
            show screen hermione_04
            with fade
            pause
            show screen bld1
            with d3
            m "Hm..."
            m "Come closer girl, let me take a better look..."
            hide screen bld1
            with d3
            show screen blkfade #Completely black screen.
            with Dissolve(1)
            pause.5
            ">Hermione slowly walks towards your desk."
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen ctc
            show screen genie_and_tits_01
            with d1
            hide screen blkfade
            with d5
            pause
            show screen bld1
            with d3
            m "Very good..."
            show screen blktone 
            with d3
            $herView.hideQQ()
            
            

            # add tits pose!
            call addTitsPose
            
            $herView.showQQ( "body_84.png", pos )
            #$ only_upper = True #No lower body displayed. 
            pause
            her "...................................."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    


    menu:
        "\"Break your promise. Grab the tits!\"":
            if hermi.whoring >= 6 and hermi.whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT. HERMIONE OUTRAGED.
                $herView.hideQQ()
                show screen blkfade
                with d3
                ">You reach out and dig your fingers into the girl's ample flesh..."
                $her_head_state = 7
                her_head_main "Professor, what are you doing?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                
                m "Relax, girl. Just stand still!"
                m "Oh... Those are some nice titties you've got..."
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $her_head_state = 13
                her_head_main "No, sir, please! You mustn't do this..."
                m "This won't take long, just stand still."
                $her_head_state = 24
                her_head_main "You must unhand me now!!!"
                with hpunch
                $her_head_state = 23
                her_head_main "You have to let me go now!!!"
                show screen blkfade
                with d5
                ">Hermione pulls away from you and covers up hastily."
                $her_head_state = 19
                her_head_main "I think I'd better go..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                m "Go ahead, girl. You are not getting paid if you do..."
                her_head_main "But I showed you my..."
                $her_head_state = 24
                her_head_main "And you touched me..."
                $her_head_state = 23
                her_head_main "And I am getting nothing?"
                m "You are dismissed, miss granger..."
                $her_head_state = 19
                her_head_main "Gr.................."
                her_head_main "{size=-5}(Burn in hell, you wretched old---{/size}"
                $ hermi.liking -= 22
                call music_block
                jump loadState_and_could_not_flirt
            elif hermi.whoring >= 9 and hermi.whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT. A BIT ANGRY.
                $herView.hideQQ()
                $ only_upper = False #No lower body displayed. 
                show screen blkfade
                with d3
                ">You reach out and dig your fingers into the girl's ample flesh..."
                $her_head_state = 7
                her_head_main "Professor, what are you doing?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                m "Relax, girl. Just stand still!"
                $her_head_state = 4
                her_head_main "I didn't agree to this, sir..."
                her_head_main "I don't think you should..."
                m "Don't you like it...?"
                $her_head_state = 12
                her_head_main "What?"
                m "Don't you like it how I squeeze and pull on your breasts?"
                her_head_main "..............."
                m "Admit it, you like it a little bit..."
                her_head_main "{size=-5}(So strange to see my breasts in someone else's hands...){/size}"
                $her_head_state = 13
                her_head_main "Sir, I am letting you do this to me to help my house out, nothing more!"
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $her_head_state = 4
                her_head_main "Please, unhand me now!"
                show screen blkfade
                with d5
                ">Hermione pulls away from you suddenly and covers up."
                her_head_main "You promised not to touch, professor..."
                m "It was hard to resist..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                $her_head_state = 1
                her_head_main "............."
                $her_head_state = 9
                her_head_main "Can I get paid now please?"
                m "Sure..."
                $ hermi.liking -= 9
            elif hermi.whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT. ENJOYS A LITTLE.
                $herView.hideQQ()
                show screen blkfade
                with d3
                ">You reach out and dig your fingers into the girl's ample flesh..."
                $her_head_state = 7
                her_head_main "Professor, what are you doing?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                m "Relax, girl. Just stand still!"
                $her_head_state = 12
                her_head_main "But..."
                $her_head_state = 13
                her_head_main "ah...{image=textheart.png}"
                $her_head_state = 12
                her_head_main "I didn't agree to this..."
                m "But you like it, don't you?"
                $her_head_state = 13
                her_head_main "I do not, sir!{image=textheart.png}"
                show screen blktone
                with d3
                ">You give her tits a couple of firm squeezes..."
                hide screen blktone
                with d3
                $her_head_state = 15
                her_head_main "Sir, you promised not to touch..."
                m "I know, I know... But it's hard to resist..."
                $her_head_state = 20
                her_head_main "................."
                $her_head_state = 6
                her_head_main "....................ah...{image=textheart.png}"
                her_head_main "Sir, you need to stop now..."
                m "Just a bit longer..."
                show screen blktone8
                with d3
                ">You keep on massaging the girl's breasts..."
                hide screen blktone8
                with d3
                $her_head_state = 37
                her_head_main "Sir... please, stop this..."
                m "Why? Because you like it too much?"
                $her_head_state = 18
                her_head_main "No it's not that..."
                $her_head_state = 17
                her_head_main "I mean..."
                show screen blktone8
                with d3
                ">You pull the tits in opposite directions and then squish them together..."
                hide screen blktone8
                with d3
                $her_head_state = 38
                her_head_main "Ah...{image=textheart.png} Sir, I really need to go..."
                if daytime:
                    $her_head_state = 17
                    her_head_main "That's right... the classes are about to start..."
                else:
                    her_head_main "It is getting late..."
                m "Well, alright..."
                show screen blkfade
                with d5
                ">You let go of the girl's breasts..."
                ">Hermione covers up..."
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $her_head_state = 25
                her_head_main "Please don't think I forgot that you broke your promise, sir."
                m "Right..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                $her_head_state = 35
                her_head_main "Can I have my payment now?"
                $ hermi.liking -=7
   
        "\"Keep promise. Admire visually.\"":
            ">You take a long look at Hermione's naked tits..."
            if hermi.whoring >= 6 and hermi.whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.
                pause
                menu:
                    "-Nod your head in approval-":
                        ">You Look at the girl's tits for a while and then nod in approval..."
                        her "......................"
                    "-Shake your head in disapproval-":
                        $ hermi.liking -= 3
                        ">You Look at the girl's tits for a while and then shake your head in dissapointment..."
                        her ".....................?"
            elif hermi.whoring >= 9 and hermi.whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
                pause
                menu:
                    "\"A Nice set of tits you got there.\"":
                        $herView.hideshowQQ( "body_83.png", pos )
                        pause
                        her "Thank--"
                        $herView.hideshowQQ( "body_82.png", pos )
                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        her "..........."
                        $herView.hideshowQQ( "body_81.png", pos )
                        her "You are being inappropriate, professor."
                        
                    "\"Hm... I've seen better.\"":
                        $ hermi.liking -= 7
                        $herView.hideshowQQ( "body_83.png", pos );
                        her "Tsk..."
                        her "Are we done then?"

            elif hermi.whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
                pause
                menu:
                    "\"You have great tits, girl.\"":
                        $herView.hideshowQQ( "body_82.png", pos )
                        her "You really think so professor?"
                        $herView.hideshowQQ( "body_84.png", pos )
                        her "I am glad you like them, sir..."
                    "\"Your tits are alright I suppose...\"":
                        $herView.hideshowQQ( "body_82.png", pos )
                        her "Huh?"
                        her "Does this mean you don't like them, sir?"
                        $herView.hideshowQQ( "body_85.png", pos )
                        her "I'm sorry..."
            ">You stare at her breasts for a while longer..."
            pause
            m "Alright, you can cover up, girl..."
            her "............."
            $herView.hideQQ()
            
            show screen blkfade
            with d3
            ">Hermione covers up..."
            hide screen chair_02 #Genie's chair.
            hide screen genie_and_tits_01
            hide screen bld1
            hide screen blktone
            show screen genie
            show screen bld1
            $ hermione_chibi_xpos = 400 #Near the desk.
            show screen hermione_02 #Hermione stands still.
            with d5

        "\"Start jerking off.\"":
            if hermi.whoring >= 6 and hermi.whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.
                $ hermi.liking -= 2
                $herView.hideQQ()
                ">You take your cock out and start stroking it..."
                show screen blkfade
                hide screen bld1
                with d3
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $her_head_state = 30
                her_head_main "Professor?!!"
                m "Just stand still, girl..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                ">You stare at Hermione's breasts with hunger..."
                $her_head_state = 13
                her_head_main "Professor, what are you...?"
                ">You keep stroking your hard cock..."
                $her_head_state = 12
                her_head_main "Professor, no..."
                her_head_main "You must... Put it away..."
                m "Stop whining girl. I'm not touching you, am I?"
                $her_head_state = 19
                her_head_main "But..."
                $her_head_state = 20
                her_head_main "But I didn't agree to this!"
                $her_head_state = 19
                her_head_main "I..."
                her_head_main "I think I'd better leave now!"
                menu:
                    "\"Leave now, and you'll get no points!\"":
                        $her_head_state = 21
                        her_head_main "After {size=+5}this{/size}? Are you kidding me, sir?"
                        her_head_main "I showed you my..."
                        $her_head_state = 25
                        her_head_main ".........."
                        $her_head_state = 24
                        her_head_main "I am not going to sell you a single favour anymore, professor!"
                        show screen blkfade
                        with d3
                        ">Hermione pulls away from you and covers up..."
                        g4 "Don't you dare to leave me in this state, girl!"
                        $her_head_state = 10
                        her_head_main "I am not setting a foot into your office ever again, sir!"
                        g4 "Come on, now. Just say something dirty! I'm almost there!"
                        $her_head_state = 27
                        her_head_main "You are a horrible person, sir..."
                        $ hermi.liking -= 30
                        call music_block
                        jump loadState_and_could_not_flirt
                    "\"Alright, alright. That's enough for now.\"":
                        $ hermi.liking -=9
                        pass
                    "-Start jerking your cock faster-":
                        $ hermi.liking -= 35
                        ">You start jerking your cock furiously!"
                        $her_head_state = 23
                        her_head_main "No, professor, stop!"
                        ">You jerk it even faster!"
                        $her_head_state = 25
                        her_head_main "Professor, think I will be leaving now..."
                        g4 "No, wait, I'm almost there!"
                        show screen blkfade
                        with d3
                        $her_head_state = 10
                        her_head_main "Ew! Professor!"
                        her_head_main "I'm leaving!"
                        call music_block
                        jump loadState_and_could_not_flirt
            elif hermi.whoring >= 9 and hermi.whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
                $herView.hideQQ()
                ">You take your cock out and start stroking it..."
                show screen blkfade
                hide screen bld1
                with d3
                $her_head_state = 30
                her_head_main "Professor?"
                ">You stare at Hermione's breasts with hunger..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                $her_head_state = 13
                her_head_main "Professor, I didn't agree to this..."
                m "What are you complaining about, girl?"
                m "I'm not even touching you..."
                her_head_main "Yes, but you are... touching yourself, sir."
                ">You pick up the pace..."
                m "just stand still, girl."
                m "It will be over soon."
                her_head_main ".................."
                $her_head_state = 12
                her_head_main "(It's so big...)"
                m "Yes... Yes, like this..."
                m "Yes, with your tits all naked..."
                her_head_main ".............."
                $her_head_state = 17
                her_head_main "well, so be it..."
                her_head_main "You can keep touching yourself, sir..."
                $her_head_state = 1
                her_head_main "But you must promise me not to..."
                $her_head_state = 5
                her_head_main "Not to... em..."
                $her_head_state = 4
                her_head_main "Not to discharge..."
                $her_head_state = 8
                her_head_main "Not in front of me, sir..."
                m "Fine, whatever..."
                m "Oh, you little slut. You nasty little slut!"
                $her_head_state = 19
                her_head_main "......................."
                ">You start to stroke your cock even harder..."
                g4 "Yes, I know you want this! Yes!"
                her_head_main "................"
                show screen blkfade 
                with d3
                ">You are about to cum..."
                menu:
                    "-Hold it as promised-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        $her_head_state = 15
                        her_head_main "..............."
                        ">Hermione covers up..."
                    "-Just start cumming-":
                        #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        g4 "Argh! You whore!"
                        $her_head_state = 21
                        her_head_main "Proff-- ??"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        $her_head_state = 23
                        her_head_main "Professor, no, you promised!"
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        $her_head_state = 10
                        her_head_main "Professor, how could you...?"
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3

                        #add sperm on tits
                        call addSperm

                        $herView.showQQ( "body_85.png", pos )
                        pause
                        her "My uniform..."
                        her "It's ruined...."
                        m "Don't worry, I will give you your house points, girl."
                        m "You did good."
                        her "................"
                        her "I need to clean myslef up..."
                        $herView.hideQQ()
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        with d3

                        hide screen blkfade
                        with d5
                        
                        call delSperm

                        
                        
                        #here we'll remove pose and add aftersperm effect
                        call addAfterSperm

                        $herView.showQQ( "body_47.png", pos )
                        pause
                        #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        her "How could you do this to mr, sir?!"
                        her "You gave me your word!"
                        $herView.hideQQ()
                        $ hermi.liking -= 45
            elif hermi.whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
                $herView.hideQQ()
                ">You take your cock out and start stroking it..."
                show screen blkfade
                hide screen bld1
                with d3
                $her_head_state = 6
                her_head_main "Professor?"
                ">You stare at Hermione's breasts with hunger..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                $her_head_state = 13
                her_head_main "Professor, actually I never agreed to this..."
                m "What are you complaining about, girl?"
                m "I'm not even touching you..."
                her_head_main "Yes, but you are... touching yourself, sir."
                #">You pick up the pace..."
                m "Just stand still, bitch."
                m "It will be over soon."
                her_head_main ".................."
                m "Yes... Yes, like this..."
                m "Yes, with your tits all naked..."
                $her_head_state = 12
                her_head_main ".............."
                $her_head_state = 17
                her_head_main "well, so be it..."
                $her_head_state = 1
                her_head_main "But you must promise me not to..."
                $her_head_state = 5
                her_head_main "Not to... ehm..."
                $her_head_state = 4
                her_head_main "Not to discharge..."
                her_head_main "Not in front of me, sir..."
                m "Fine, whatever..."
                m "Oh, you little slut. You nasty little slut!"
                $her_head_state = 12
                her_head_main "......................."
                ">You start to stroke your cock even harder..."
                g4 "Yes, I know you want this! Yes!"
                her_head_main "................"
                show screen blkfade 
                with d3
                 # SAME AS PREVIOUS EVENT^^^
                g4 "Argh! (I'm about to cum!)"
                menu:
                    "-Hold it as promised-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        her_head_main "..............."
                        her_head_main "Ehm... I read that that is bad for you, sir..."
                        m "Huh?"
                        $her_head_state = 13
                        her_head_main "It is bad for your health to just hold it in like this..."
                        $her_head_state = 12
                        her_head_main "Em..."
                        $her_head_state = 14
                        her_head_main "If you want to you can--"
                        g4 "Argh! You whore!"
                        $her_head_state = 7
                        her_head_main "???"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        $her_head_state = 9
                        her_head_main "Professor, I didn't mean that you can release your... semen on me, sir..."
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        $her_head_state = 18
                        her_head_main "Well, what's done is done I suppose..."
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3

                        call addSperm

                        $herView.showQQ( "body_85.png", pos )
                        pause
                        her "My uniform is ruined though..."
                        m "Don't worry, I will give you your house points, girl."
                        m "You did good."
                        $herView.hideshowQQ( "body_84.png", pos )
                        her "Thank you sir."
                        $herView.hideshowQQ( "body_83.png", pos )
                        her "Now I need to clean myself up..."
                        pause
                        $herView.hideQQ()
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        hide screen blkfade
                        with d5

                        call delSperm
                        
                        #here we remove pose and add aftersperm effect
                        call addAfterSperm

                        $herView.showQ( "body_45.png", pos )
                        pause
                        her "Well, this should do for now..."
                        $herView.hideQQ()
                    "-Just start cumming-":
                        g4 "Argh! You whore!"
                        $her_head_state = 7
                        her_head_main "???"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        $her_head_state = 13
                        her_head_main "ah...{image=textheart.png} It's so hot...{image=textheart.png}"
                        $her_head_state = 9
                        her_head_main "Professor, you promised..."
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        $her_head_state = 15
                        her_head_main "Well, what's done is done I suppose..."
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3

                        call addSperm

                        $herView.showQQ( "body_85.png", pos )
                        pause
                        her "My uniform is ruined though..."
                        m "Don't worry, I will give you your house points, girl."
                        m "You did good."
                        $herView.hideshowQQ( "body_84.png", pos )
                        her "Thank you sir."
                        $herView.hideshowQQ( "body_83.png", pos )
                        her "Now I need to clean myself up..."
                        pause
                        $herView.hideQQ()
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        hide screen blkfade
                        with d5

                        call delSperm

                        
                        # remove pose and add aftersperm
                        call addAfterSperm

                        $herView.showQ( "body_45.png", pos )
                        pause
                        her "Well, this should do for now..."
                        $herView.hideQQ()
                        

    
    hide screen jerking_off_01                   
    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    show screen hermione_02
    show screen genie
    with fade
    
    hide screen blkfade
    with d3

    label new_request_08_finish:
    $ gryffindor +=current_payout
    m "The \"Gryffindor\" house gets [current_payout] points!"
    stop music fadeout 10.0

   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    # remove pose here, because sometimes we need to keep added items even here ( like sperm )
    $herView.data().delPose()

    $ pos = POS_370
    $herView.showQQ( "body_29.png", pos )
    her ".................."
    her "Thank you sir..."
    if daytime:
        her "Now if you don't mind I'd better go. my classes are about to start."
    else:
        her "I'd better go now then. It's getting pretty late..."
    
#    if whoring >= 6 and whoring <= 8:
#        $ level = "03"
#        $ new_request_08_01 = True # HEARTS.
#    if whoring >= 9 and whoring <= 11:
#        $ level = "04"
#        $ new_request_08_02 = True # HEARTS.
#    if whoring >= 12:
#        $ level = "05"
#        $ new_request_08_03 = True # HEARTS.

    $SetHearts(GetStage(hermi.whoring, 6, 4, 3))


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
        
    if hermi.whoring >= 6 and hermi.whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.    
        $her_head_state = 12
        her_head_main "(How humiliating... What have I become...?)"
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)
    elif hermi.whoring >= 9 and hermi.whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
        her_head_main "........................"
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  
    elif hermi.whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
        $her_head_state = 6
        her_head_main "{size=-5}(That was so humiliating...){/size}"
        $her_head_state = 24
        her_head_main "{size=-5}No, Hermione, you silly girl!){/size}"
        her_head_main "{size=-5}(We are doing this to protect the honour of our house!){/size}"
        $her_head_state = 19
        her_head_main "................................."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  
    else:
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  


        
    if hermi.whoring <= 8:
        $ hermi.whoring +=1
        

#    $ request_08_points += 1
        

    # load from pose with tits and that sperm!
    $herView.data().loadState()
    
    $event.Finalize()    
    jump finish_daytime_event



label addTitsPose:
    # add tits pose!
    #$herView.data().addPose( CharacterExItemPoseShowTits( herView.mPoseFolder, 'pose_dress_up.png', G_Z_POSE ) )
    $herView.data().addItem( 'item_pose_show_tits' )
    return
    
label addSperm:
    # add sperm item!
    #$herView.data().addItemKey( 'sperm', CharacterExItem( herView.mMiscFolder, 'sperm_00.png', G_Z_FACE + 1 ) )
    $herView.data().addItem( 'item_sperm', '00' )
    return

label delSperm:
    # add sperm item!
    $herView.data().delItem( 'item_sperm' )
    return
    
label addAfterSperm:
    # del pose and add aftersperm
    $herView.data().delPose()
    #$herView.data().addItemKey( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
    $herView.data().addItem( 'item_sperm_dried' )
    return
    
label loadState_and_could_not_flirt:
    $herView.data().loadState()
    jump could_not_flirt
#    jump finish_daytime_event

