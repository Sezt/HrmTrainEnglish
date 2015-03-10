
    
    

###################REQUEST_29 (Level 07) (65 pt.) (Sex). #################################################################
label new_request_29: #LV.7 (Whoring = 18 - 20)

    $herView.hideQQ()
    m "{size=-4}(Should I ask her to have sex with me?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request
            
    
    $ pos = POS_140
    $ posHead = gMakePos( 390, 340 )
    $herView.data().saveState()

    if IsFirstRun(): # FIRST EVENT <============================================================== EVENT 01
#    if request_29_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Miss Granger?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Sir?"
        m "The favour I will be buying from you today..."
        $herView.hideshowQQ( "body_06.png", pos )
        her ".......?"
        m "How should I put this delicately...?"
        $herView.hideshowQQ( "body_129.png", pos )
        her "Is it sex, sir?"
        m "Well, yes. How did you...?"
        if whoring <=17:
            jump too_much
        $herView.hideshowQQ( "body_128.png", pos )
        her "Not a terribly difficult deduction all things considered..."
        m "You don't mind then?"
        $herView.hideshowQQ( "body_120.png", pos )
        her "Of course, I mind, sir!"
        her "I am not a prostitute!"
        m "But you'll do it anyway??"
        $herView.hideshowQQ( "body_127.png", pos )
        her2 "\"Gryffindor\" is falling behind again..."
        her2 "What choice do I have...?"
        m "Great!"
        $herView.hideQ()
       
        label your_ass:
            
        show screen blkfade 
        with d7
            
        stop music fadeout 1.0
        $herViewHead.showQ( "body_120.png", posHead )
        her "............."
        $herViewHead.showQ( "body_119.png", posHead )
        her "!!!!!!!!!!!!!!!"
        $herViewHead.hideQ()
        m "Relax, girl. I'm Just gonna take off your panties."
        $herViewHead.showQ( "body_49.png", posHead )
        her ".............."
        $herViewHead.hideQ()
        m "Are you ready?"
        $herViewHead.showQ( "body_50.png", posHead )
        her "No..."
        $herViewHead.hideQ()
        m "Good girl."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        $herViewHead.showQ( "body_130.png", posHead )
        her2 "Ooooohhhhhhhhhhhh....{image=textheart.png}"
        $herViewHead.hideQ()




        $herView.hideQ()
        hide screen genie
        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3    
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            
            
            
            
        
        
        #FUCKING
        
        g4 "Your pussy... It's so tight."
        $herViewHead.showQ( "body_33.png", posHead )
        her "................"
        $herViewHead.hideQ()
        m "You alright?"
        $herViewHead.showQ( "body_21.png", posHead )
        her "A-ha... It's too big..."
        her "You will rip me apart, sir!"
        $herViewHead.hideQ()
        m "Nonsense! My cock is of a regular size."
        m "It's not my fault that you are so tiny."
        $herViewHead.showQ( "body_33.png", posHead )
        her "......................"
        $herViewHead.hideQ()
        hide screen ctc
        menu:
            "\"You should be ashamed of yourself!\"":
                $herViewHead.showQ( "body_33.png", posHead )
                her "I am not ashamed, sir!"
                her "I am doing this for the sake my house!"
                her "To help my--"
                $herViewHead.showQ( "body_131.png", posHead )
                her "ah-ha-a..."
                her "My classmates depend on me... ah-a..."
                $herViewHead.hideQ()
                m "Are you sure that's the only reason?"
                $herViewHead.showQ( "body_33.png", posHead )
                her "I don't know--"
                $herViewHead.showQ( "body_131.png", posHead )
                her2 "ah-a..."
                $herViewHead.showQ( "body_118.png", posHead )
                her2 "I don't know what you mean, sir."
                $herViewHead.hideQ()
                m "It seems to me that you are enjoying this a little bit too much."
                $herViewHead.showQ( "body_118.png", posHead )
                her "I'm not, sir!"
                $herViewHead.hideQ()
                m "Really?"
                $herViewHead.showQ( "body_33.png", posHead )
                her "......................"
                $herViewHead.hideQ()
                m "Then why is your pussy so wet?"
                $herViewHead.showQ( "body_131.png", posHead )
                her "....................а-а.{image=textheart.png}"
                $herViewHead.hideQ()
                m "Admit it, you enjoy getting fucked by your professor!"
                $herViewHead.showQ( "body_33.png", posHead )
                her "I do not!"
                $herViewHead.hideQ()
                m "Stubborn girl..."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Аааh...{image=textheart.png}" 
                $herViewHead.hideQ()
            "\"So... What's new in your life?\"":
                $herViewHead.showQ( "body_31.png", posHead )
                her "...Sir?"
                $herViewHead.hideQ()
                m "Just trying to have a polite conversation."
                $herViewHead.showQ( "body_31.png", posHead )
                her "Ah-ah... But... ah..."
                $herViewHead.hideQ()
                m "Any news from your folks?"
                $herViewHead.showQ( "body_34.png", posHead )
                her "My parents?"
                $herViewHead.showQ( "body_131.png", posHead )
                her2 "Professor, please, I cannot talk..."
                $herViewHead.hideQ()
                m "Why not? Enjoying this too much?"
                $herViewHead.showQ( "body_131.png", posHead )
                her "I am not... ah...{image=textheart.png}"
                $herViewHead.hideQ()
                m "I think you are."
                $herViewHead.showQ( "body_131.png", posHead )
                her "I am only doing this for the points, sir..."
                $herViewHead.hideQ()
                m "Oh, I see..."
                m "So you are like a prostitute then."
                $herViewHead.showQ( "body_117.png", posHead )
                her "What?"
                $herViewHead.hideQ()
                m "Well I pay you to have sex with me. How would you call that?"
                $herViewHead.showQ( "body_118.png", posHead )
                her "..........."
                $herViewHead.showQ( "body_131.png", posHead )
                her "I am not a prostitute..."
                $herViewHead.showQ( "body_21.png", posHead )
                her "Why are you being so mean to me, sir?"
                $herViewHead.hideQ()
                m "I think you like it when I'm mean."
                $herViewHead.showQ( "body_67.png", posHead )
                her "I do not!"
                $herViewHead.hideQ()
                m "Really? Then why is your pussy so wet?"
                $herViewHead.showQ( "body_118.png", posHead )
                her "Not because of that!"
                $herViewHead.hideQ()
                m "If you say so..."
                $herViewHead.showQ( "body_131.png", posHead )
                her "A-ah...{image=textheart.png}"
                $herViewHead.showQ( "body_132.png", posHead )
                her "I am... ah...{image=textheart.png} not a prostitute..."          
                $herViewHead.hideQ()
            "\"......................................................\"":
                $herViewHead.showQ( "body_131.png", posHead )
                her "A-ha... ah..."
                $herViewHead.hideQ()
                m "*Panting!*"
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ah... ha-aha..."
                $herViewHead.hideQ()
                m "Оh..."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ah-ah..."
                $herViewHead.hideQ()
                m "......................"
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ah... ah..."
                $herViewHead.showQ( "body_31.png", posHead )
                her "Ah... Sir?"
                $herViewHead.hideQ()
                m "What is it?"
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ah... Do you.... like it?"
                $herViewHead.hideQ()
                m "Do I like drilling your super-tight pussy?"
                m "Very much so, girl. Why?"
                $herViewHead.showQ( "body_33.png", posHead )
                her "....................."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ah... You just got so quiet..."
                $herViewHead.hideQ()
                m "Just enjoying the moment, girl."
                m "What about you? You alright?"
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ah... yes..."
                $herViewHead.showQ( "body_31.png", posHead )
                her "It hurts a little though, ah..."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Your penis is too big... ah..."
                $herViewHead.hideQ()
                m "Hm..."
                m "You need me to slow down or something?"
                $herViewHead.showQ( "body_31.png", posHead )
                her "No, sir... You don't have to..."
                $herViewHead.showQ( "body_33.png", posHead )
                her "Please, don't mind me... Enjoy your moment."
                her "I will... ah... Get used to it eventually... ah..."
                $herViewHead.hideQ()
                m "As you say, girl."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ah-a...{image=textheart.png}"
                $herViewHead.hideQ()

        m "Yes, this is great!"
        $herViewHead.showQ( "body_131.png", posHead )
        her "Ah-ah...{image=textheart.png}"
        $herViewHead.hideQ()
        if daytime:
            m "Going to classes after this?"
        else:
            m "Going to bed after this?"
        $herViewHead.showQ( "body_131.png", posHead )
        her "Yes, ah...{image=textheart.png}"
        her "If I'll be able to walk..."
        $herViewHead.hideQ()
        g4 "Ght! {image=textheart.png} Yes, you always say the right things, girl!"
        $herViewHead.showQ( "body_132.png", posHead )
        her "Ah...{image=textheart.png} ah...{image=textheart.png}{image=textheart.png}"
        with hpunch
        $herViewHead.showQ( "body_130.png", posHead )
        her "{size=+7}!!!!!!!!!!!!!!!{/size}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        m "Huh? You alright?"
        show screen blktone8
        with d3
        ">Hermione's legs are shaking..."
        m "Girl?"
        $herViewHead.showQ( "body_130.png", posHead )
        her "{image=textheart.png}{image=textheart.png}{image=textheart.png}I think I'm cumming, sir!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        g9 "Tch... You nasty slut!"
        $herViewHead.showQ( "body_133.png", posHead )
        her "AAH! I can't hold it!"
        $herViewHead.hideQ()
        g4 "You need to be punished for being such a slut!"
        ">You tighten your grip on Hermione's buttocks and start to fuck her fiercely!"
        $ g_c_u_pic = "sex2_ani"
        with hpunch
        $herViewHead.showQ( "body_130.png", posHead )
        her "NO! STOP! PLEASE!"
        $herViewHead.hideQ()
        g4 "Who told you you could cum, slut? This is your punishment!"
        $herViewHead.showQ( "body_131.png", posHead )
        her "Professor, no, ah-a!{image=textheart.png}"
        $herViewHead.showQ( "body_134.png", posHead )
        her "Ah-a...{image=textheart.png}I will go insane!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        g4 "{size=+7}Grragh!{/size}"
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc
        show screen bld1
        with d3
        $herViewHead.showQ( "body_134.png", posHead )
        her "No...{image=textheart.png} ah...{image=textheart.png}"
        her "I think I will...{image=textheart.png} pass out...{image=textheart.png}"
        $herViewHead.hideQ()
        g4 "OOOOH YES! WHORE!"
        menu:
            "-Cum all over Hermione-":
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                

                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_out_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc


                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.showQ( "body_133.png", posHead )
                her2 "Ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_blink_ani"

                m "Well, that was rather intense..."
                $herViewHead.showQ( "body_135.png", posHead )
                her "*heavy panting*"
                $herViewHead.hideQ()
                m "You alright?"
                $herViewHead.showQ( "body_133.png", posHead )
                her "Ah... yes..."
                her "My legs are still shaking..."
                $herViewHead.hideQ()
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                $herViewHead.showQ( "body_133.png", posHead )
                if daytime:
                    her "But I think I will be able to make it to my classes..."
                else:
                    her2 "But I think I will be able to make it to the common room..."
                $herViewHead.hideQ()
                m "Good."
                m "Did you enjoy getting fucked by your professor?"
                $herViewHead.showQ( "body_136.png", posHead )
                her2 "Sir, I am only doing this for my house."
                $herViewHead.hideQ()
                m "Seriously? Still?"
                $herViewHead.showQ( "body_131.png", posHead )
                her "Could I just get paid now... please?"
                $herViewHead.hideQ()
    
            "-Cum inside Hermione-":
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                
                
                
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}Аааh!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_in_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.showQ( "body_133.png", posHead )
                her2 "Ааааh...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "03_hp/08_animation_02/23_cum_19.png"
                $herViewHead.showQ( "body_133.png", posHead )
                her "You came inside of me..."
                $herViewHead.hideQ()
                g9 "I sure did."
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                $herViewHead.showQ( "body_133.png", posHead )
                her "But..."
                $herViewHead.hideQ()
                m "What?"
                $herViewHead.showQ( "body_132.png", posHead )
                her "What if I get pregnant?"
                $herViewHead.hideQ()
                m "Nah, you will be alright..."
                $herViewHead.showQ( "body_132.png", posHead )
                her "How do you know, sir?"
                $herViewHead.hideQ()
                m "We witchers are infertile."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Witchers?"
                $herViewHead.hideQ()
                m "Sure... You are a witch, that make me a witcher, right?"
                m "And everyone knows that witchers are infertile..."
                $herViewHead.showQ( "body_117.png", posHead )
                her "Sir, you make no sense..."
                her "Can I please just get paid now...?"
                $herViewHead.hideQ()

    elif IsRunNumber(2): # SECOND EVENT <============================================================== EVENT 02
#    elif request_29_points == 1: # SECOND EVENT <============================================================== EVENT 02
        m "Miss Granger, are you keeping your pussy wet and ready for me?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Professor!"
        m "Just say \"I do\" and come over here, girl."
        $herView.hideshowQQ( "body_31.png", pos )
        her "..........."
        $herView.hideshowQQ( "body_118.png", pos )
        her "I do...."
        $herView.hideQ()
        jump your_ass

    elif IsRunNumberOrMore(3): # THIRD EVENT <============================================================== EVENT 03
#    elif request_29_points >= 2: # THIRD EVENT <============================================================== EVENT 03
        m "Miss Granger..."
        m "Last night I had a dream..."
        g9 "You were lying on my desk and I was fucking your tight pussy like a madman..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "In that dream, sir..."
        $herView.hideshowQQ( "body_47.png", pos )
        her "Did I happen to receive 65 house points afterwards?"
        g9 "Why yes, you did, miss Granger."
        $herView.hideshowQQ( "body_66.png", pos )
        her "..............................."
        her "Let me just take my panties off..."
        stop music fadeout 1.0
        $herView.hideQQ()
        show screen blkfade
        with d3
        # SEX
        

        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        $herViewHead.showQ( "body_130.png", posHead )
        her2 "Ooooohhhhhhhhhhhh....{image=textheart.png}"
        $herViewHead.hideQ()
        
        $herView.hideQ()
        hide screen genie
        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        show screen bld1
        with d3    


        $herViewHead.showQ( "body_131.png", posHead )
        her "Ah...{image=textheart.png}"
        $herViewHead.hideQ()
        m "Your pussy feels a bit looser today..."
        $herViewHead.showQ( "body_131.png", posHead )
        her "Does it...{image=textheart.png} ah...?{image=textheart.png}"
        $herViewHead.showQ( "body_132.png", posHead )
        her "That's all because of you sir...{image=textheart.png}"
        $herViewHead.showQ( "body_134.png", posHead )
        her2 "You are ruining my little pussy with your monstrous penis...{image=textheart.png}"
        $herViewHead.hideQ()
        g4 "Agh, you whore!"
        $herViewHead.showQ( "body_134.png", posHead )
        her "Ah...{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()

        
        
#        if not ask_me_once: #Turns true after Hermione asks you about your true identity, during sex.
#            $ ask_me_once = True #Turns true after Hermione asks you about your true identity, during sex.
#            her "Professor, can I ask you something?"
#            m "What is it, girl?"
#            her "Ah... Oh, not so deep please..."
#            her "Ah... I... Ah..."
#            her "?!!"
#            her "Professor? Why did you stop?"
#            m "What did you want to ask me, girl?"
#            her "But I think I was about to cum..."
#            m "So soon? Good think I did stop then."
#            her "Sir, please..."
#            her "I want to ask you this question while..."
#            her "While you are fucking me..."
#            her "Ah..."
#            her "Sir, I just want to know..."
#            her "Are you really Professor Dumbledore?"
#            g4 "WHAT!?"
#            menu:
#                m "!!!"
#                "\"Yes! Albus Dumbledore! That's me!\"":
#                    her "Oh..."
#                    her "You just been acting so unlike yourself lately..."
#                    g4 "You whore! Your little pussy is the best!"
#                    her "I suppose that was just my imagination then..."
#                    her "Ah-ah-a..."
#                "\"You got me... The truth is...\"":
        m "Yes! Do you like it when I fuck you like this?"
        $herViewHead.showQ( "body_128.png", posHead )
        her "Yes, sir..."
        $herViewHead.hideQ()
        menu:
            g4 "..."
            "\"Be sweet but passionate.\"":
                m "Yes, you're liking this?"
                $herViewHead.showQ( "body_127.png", posHead )
                her "I do, sir... ah...{image=textheart.png}"
                $herViewHead.hideQ()
                m "Good girl!"
                m "Just relax and take my cock!"
                $herViewHead.showQ( "body_127.png", posHead )
                her "Yes... ah...{image=textheart.png}"
                $herViewHead.hideQ()
                m "All the way in... all the way..."
                $herViewHead.showQ( "body_131.png", posHead )
                her "ah...{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                m "Yes, my little princess..."
                $herViewHead.showQ( "body_119.png", posHead )
                her "What?"
                $herViewHead.showQ( "body_118.png", posHead )
                her "No, please don't call me that... ah...{image=textheart.png}"
                her2 "My daddy used to call me his little princess when I was little..."
                $herViewHead.hideQ()
                m "Well, right now I am your daddy!"
                $herViewHead.showQ( "body_121.png", posHead )
                her "Ah...{image=textheart.png} ah-ah...{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                m "And you are my little princess-slut!"
                $herViewHead.showQ( "body_123.png", posHead )
                her "Ah...{image=textheart.png} ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            "\"Be mean to her!\"":
                $herViewHead.hideQ()
                m "Yes, you slut!"
                m "I bet you love every second of this!"
                show screen blktone
                hide screen ctc
                with d3
                ">You pick up the pace."
                hide screen blktone
                with d3
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ah...{image=textheart.png} Professor..."
                $herViewHead.hideQ()
                m "You nasty slut!"
                $herViewHead.showQ( "body_132.png", posHead )
                her "Ah...{image=textheart.png} ah-a...{image=textheart.png}"
                $herViewHead.hideQ()
                m "You are a disgrace, girl!"
                $herViewHead.showQ( "body_132.png", posHead )
                her "А-оh...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                m "Your parents sent you here to study, not to screw your teachers, you disgusting cunt!"
                $herViewHead.showQ( "body_132.png", posHead )
                her "Аh-а...{image=textheart.png} But I am only doing this--"
                $herViewHead.hideQ()
                m "Nobody cares why you are doing this, cocksucker!"
                m "Look at what you've become!"
                m "Butt-naked, on your professor's old cock, like a cheap whore!"
                $herViewHead.showQ( "body_134.png", posHead )
                her "Ah...{image=textheart.png} No...{image=textheart.png} stop saying...{image=textheart.png} ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                show screen blktone
                with d3
                ">You pick up the pace some more."
                $ g_c_u_pic = "sex2_ani"
                ">The room fills up with rhythmical sound of a flesh hitting flesh..."
                hide screen blktone
                with d3
                m "You let me molest you... You suck my cock..."
                m "What are you after that I ask you!?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "................"
                $herViewHead.showQ( "body_132.png", posHead )
                her "Аh...{image=textheart.png} Ах....{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.showQ( "body_118.png", posHead )
                her "......................."
                her "{size=-5}I am a whore...{/size}"
                her "{size=-5}I am a whore... ah...{/size}"
                $herViewHead.hideQ()
        
        m "Yes! That's exactly what you are!"
        $herViewHead.showQ( "body_118.png", posHead )
        her "Ah... ah... ah..."
        her "Sir, you think you could... ah..."
        $herViewHead.hideQ()
        m "What?"
        $herViewHead.showQ( "body_138.png", posHead )
        her "Could you spank me a little... ah...?"
        $herViewHead.hideQ()
        g4 "Gladly!"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch

        $herViewHead.showQ( "body_139.png", posHead )
        her "АА-А-Аh!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        m "You liked that one, huh?"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $herViewHead.showQ( "body_138.png", posHead )
        her "Ah..!{image=textheart.png} Yes!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        m "And some more!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $herViewHead.showQ( "body_138.png", posHead )
        her "Ahh! Yes!"
        $herViewHead.hideQ()
        show screen blktone
        with d3
        ">You notice that every time you slap the girl's butt, her pussy clutches your cock tightly for a second..."
        ">You love the sensation..."
        ">You unleash another series of slaps on Hermione's ass-cheeks."
        ">Every single one met with a gasp of excitement from the girl."
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $herViewHead.showQ( "body_138.png", posHead )
        her "Aah!!!{image=textheart.png}{image=textheart.png}{image=textheart.png} IT HURTS!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.showQ( "body_134.png", posHead )
        her2 "It hurts...{image=textheart.png}{image=textheart.png}{image=textheart.png} It hurts...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        m "Hm?"
        m "Why your legs are shaking, girl?"
        m "Are you cumming?"
        $herViewHead.showQ( "body_133.png", posHead )
        her "Yes...{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        m "Well, I think I will follow your example then."
        $herViewHead.showQ( "body_133.png", posHead )
        her ".............."
        $herViewHead.hideQ()
        show screen blktone 
        with d3
        ">You start fucking Hermione with renewed determination!"
        hide screen blktone 
        with d3
        $herViewHead.showQ( "body_139.png", posHead )
        her "Ah! No! I can't...{image=textheart.png} I...{image=textheart.png} ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        m "Shut it whore!"
        g4 "Argh!"
        menu:
            "-Cum inside of Hermione-":
                with hpunch
                g4 "{size=+7}Argh, TAKE THIS!!!{/size}"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_in_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.showQ( "body_133.png", posHead )
                her "!!!"
                her "AH! IT'S FILLING ME UP!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                g4 "I'm Not done yet, bitch!"
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                $herViewHead.showQ( "body_139.png", posHead )
                her "AH! MY BELLY!"
                $herViewHead.hideQ()
                g4 "{size=+5}SLUT!{/size}"






                $herViewHead.hideQ()
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "03_hp/08_animation_02/23_cum_19.png"

                show screen blktone
                with d7
               

                
                
                
                
    
 
                
                m "Well, this was pretty great..."
                $herViewHead.showQ( "body_133.png", posHead )
                her "Аааh...{image=textheart.png}"
                $herViewHead.hideQ()
                m "You alright there, slut? Ehm, I mean, girl."
                $herViewHead.showQ( "body_133.png", posHead )
                her "Yes... I..."
                $herViewHead.showQ( "body_135.png", posHead )
                her "I feel so full..."
                $herViewHead.showQ( "body_130.png", posHead )
                her "!!!"
                her "You came inside of me, sir!"
                $herViewHead.hideQ()
                m "I sure did."
                $herViewHead.showQ( "body_131.png", posHead )
                her "You shouldn't have..."
                $herViewHead.hideQ()
                m "Didn't you enjoy it?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "....maybe."
                $herViewHead.showQ( "body_121.png", posHead )
                her "I think I came several times..."
                show screen blkfade
                with d3
                $herViewHead.showQ( "body_122.png", posHead )
                her2 "Maybe you are right, sir, and I should'nt worry so much."
                her "Can I get my payment now?"
                $herViewHead.hideQ()

            "-Cum all over Hermione-":
                
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                

                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_out_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.showQ( "body_133.png", posHead )
                her2 "Ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                g4 "{size=+5}You whore! Take this!{/size}"
                $herViewHead.showQ( "body_138.png", posHead )
                her "{size=+5}!!!{/size}"
                $herViewHead.hideQ()
                $herViewHead.hideQ()
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_blink_ani"
                
                


                
                m "Well, that was pretty great..."
                $herViewHead.showQ( "body_138.png", posHead )
                her "Ah...{image=textheart.png}"
                $herViewHead.hideQ()
                m "You alright there, slut?"
                $herViewHead.showQ( "body_133.png", posHead )
                her "Yes... I..."
                $herViewHead.hideQ()
                m "Didn't you enjoy this?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "....I think so..."
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
                $herViewHead.showQ( "body_121.png", posHead )
                her "I think I came several times, sir..."
                $herViewHead.showQ( "body_122.png", posHead )
                her "Can I get my payment now?"
                $herViewHead.hideQ()
        
        
    if herViewHead.data().getItem( 'sperm' ) != None:
        $herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
    $herViewHead.data().delItem( 'sperm' )
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    hide screen blktone
    with d3
    
    stop music fadeout 4.0
    m "Yes, miss Granger. 65 points to the \"Gryffindor\" house." 
    $ gryffindor +=65
    $herView.showQ( "body_13.png", pos )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, sir..."

    if whoring <= 20: # Level 07 <
        $ whoring +=1




#    if request_29_points == 0:
#        $ new_request_29_01 = True # HEARTS
#    if request_29_points == 1:
#        $ new_request_29_02 = True # HEARTS
#    if request_29_points >= 2:
#        $ new_request_29_03 = True # HEARTS
    


#    $ request_29_points += 1
    $SetHearts(GetStage(event._finishCount,1,1,1))


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

    $herView.data().loadState()

    #call music_block 
    
    if daytime:
        jump night_start
    else:
        jump day_start
                   

