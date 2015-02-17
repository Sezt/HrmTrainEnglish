###################REQUEST_22 (Level 06) (55 pt.) (Blowjob). 
label new_request_22: #LV.6 (Whoring = 15 - 17)
    $herView.hideQQ()
    if request_22_points == 0:
        m "{size=-4}(Ask a girl to give me a Blowjob?){/size}"
    else:
        m "{size=-4}(Ask a girl to give me another Blowjob?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes! Lets do this!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
            
 
    $ pos = POS_140
    $ herView.data().saveState()

    if request_22_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Miss Granger?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Yes, professor?"
        m "I plan to grant \"Gryffindor\" 55 house points today..."
        m "If you suck me off..."
        if whoring <=14: # LEVEL 05
            jump too_much
        $herView.hideshowQQ( "body_87.png", pos )
        her "Oh..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "Alright."
        m "Really? Just like that?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "Yes. I know I'm supposed feel outraged..."
        $herView.hideshowQQ( "body_117.png", pos )
        her "But somehow I do not..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "I suppose I am just glad that I can help out my house..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "And if to do that I must put your penis in my mouth so be it..."
        m "Well, alright then."
        $herView.hideshowQQ( "body_118.png", pos )
        her "Although, now when I say it out loud like this..."
        m "Too late! You already said \"yes\"!"
        $herView.hideshowQQ( "body_24.png", pos )
        her "I know..."

        label blowjob_jumping:
        # BLOWJOB
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        $herView.hideQ()
        hide screen genie
        $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
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
#        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
#        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
#        show screen h_head2                                                             # HERMIONE
#        $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE


        

        
        her "*Slurp!* *Gulp!* *Slurp!*"
        m "Yes..."
        m "Try to take it deeper now..."
        her "*Gulp!* *Gobble!* *Gobble!*"
        m "Yes, like that. Good."
        her "*Slurp!* *Gltch!* *Gulp!*"
        m "Yes, that's a good girl."

        $ posHead = gMakePos( 390, 235 )
        menu:
            m "Hm..."
            "\"Whatever happened to your \"MRM\" thing?\"":
                her "*Slurp?*"
                
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                
                $herViewHead.showQ( "body_118.png", posHead )
                her "Oh, well..."
                her "We are still active, but..."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Gobble!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_122.png", posHead )
                her2 "But we are not getting as popular and as much support as I thought we would..."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                $herViewHead.hideQ()
                her "*Slurp!* *Gulp!* *Gulp!*"
                m "Oh... This is good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Hm..."
                m "So you don't mind selling me sexual favours, letting me play with your tits and such..."
                her "*Gobble!* *Gltch!* *Slurp!*"
                m "And then condemn such behavior in front of the other students."
                her "*Slurp!* *Slurp!* *Gulp!*"
                m "You perverted, little hypocrite."
                her "*Gulp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_117.png", posHead )
                her "That's not what we stand for, sir."
                $herViewHead.hideQ()
                m "What do you mean?"
                $herViewHead.showQ( "body_16.png", posHead )
                her2 "The \"MRM\" is about gender equality."
                her2 "We are not as much against selling sexual favours to the teachers..."
                her2 "As we are against the gender inequality that the selling of sexual favour creates..."
                $herViewHead.hideQ()
                m "Hm..."
                m "This conversation is starting to bore me..."
                m "Suck on my cock some more before we continue."
                $herViewHead.showQ( "body_121.png", posHead )
                her "Of course, sir."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                $herViewHead.hideQ()
                her "*Gobble!* *Slurp!* *Slurp!*"
                m "Yes, much better..."
                m "But you still disapprove of selling the favours, right?"
                her "*Slurp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_120.png", posHead )
                her2 "Yes, it is frowned upon..."
                $herViewHead.hideQ()
                m "And yet, you are the biggest offender by far."
                $herViewHead.showQ( "body_120.png", posHead )
                her "But what choice do I have?"
                her2 "I've been put in a very difficult position..."
                $herViewHead.hideQ()
                m "The cock, girl."
                $herViewHead.showQ( "body_120.png", posHead )
                her "Right, sorry..."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                $herViewHead.hideQ()
                her "*Slurp!* *Gulp!* *Gltch!*"
                her "*Slurp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_117.png", posHead )
                her2 "This one time we had a meeting right after I sold you another favour, sir."
                her2 "I had to give a speech with my uniform all messy and stained."
                her2 "It felt awful that I had to do that..."
                $herViewHead.hideQ()
                m "You did enjoy it a little bit though..."
                $herViewHead.showQ( "body_118.png", posHead )
                her "Well..."
                $herViewHead.hideQ()
                m "Just admit it."
                $herViewHead.showQ( "body_117.png", posHead )
                her "..............."
                $herViewHead.hideQ()
                m "Yes, I knew it. You took pleasure in it, you little perv."
                $herViewHead.showQ( "body_118.png", posHead )
                her2 "I suppose it was embarrassing and exciting at the same time..."
                her2 "And it made me feel even worse about myself."
                $herViewHead.hideQ()
                m "You poor thing."
                m "Cock back in the mouth."
                $herViewHead.showQ( "body_117.png", posHead )
                her "Yes, sir."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                

            "\"Your parents must be proud of you...\"":
                her "*Slurp--"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                $herViewHead.showQ( "body_75.png", posHead )
                her "Yes, I believe they are..."
                $herViewHead.showQ( "body_74.png", posHead )
                her2 "With me being an excellent student despite being muggle-born and all..."
                $herViewHead.showQ( "body_117.png", posHead )
                her2 "Although at first they were against sending me to some \"Bogus boarding school\"."
                $herViewHead.showQ( "body_74.png", posHead )
                her2 "Took some effort to convince them that \"Hogwarts\" is a respectable institution."
                $herViewHead.hideQ()
                m "Yes, a respectable institution indeed."
                m "Cock back in your mouth girl."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Gulp!* *Gobble!*"
                $herViewHead.hideQ()
                m "Yes, just keep at it for a while..."
                her "*Slurp!* *Gltch!* *Gulp!*"
                $herViewHead.hideQ()
                m "Good, good..."
                m "So, what would your folks say if they were to see you now, girl?"
                her "*Slurp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_87.png", posHead )
                her "They would not understand of course..."
                her "But I do not care."
                $herViewHead.showQ( "body_120.png", posHead )
                her2 "I am not afraid to \"get my hands dirty\" and do what needs to be done."
                $herViewHead.hideQ()
                m "A bit rebellious, aren't you?"
                $herViewHead.showQ( "body_122.png", posHead )
                her "Hm... I suppose I am."
                $herViewHead.hideQ()
                m "Back to sucking then. Teach your folks a lesson."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Slurp!* *Slurp!*"
                

            "\"Tell me about the \"Gryffindor\" house.\"":
                her "*Slurp--"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                $herViewHead.showQ( "body_13.png", posHead )
                her "What can I say that you don't already know, sir?"
                $herViewHead.hideQ()
                m "Yes... Ehm... I know everything of course."
                m "But I want to see how much you know."
                m "To test your knowledge on the subject."
                show screen blktone
                with d3
                ">As soon as you mention \"test\" Hermone's eyes light up with excitement."
                hide screen blktone
                with d3
                $herViewHead.showQ( "body_80.png", posHead )
                her "OK. But I need a moment gather my thoughts..."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Slurp!* *Gulp!*"
                m "Oh, yes... Take as much time as you need, girl."
                her "*Slurp!* *Gulp!* *Slurp!*"
                her "*Gulp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                hide screen ctc
                $herViewHead.showQ( "body_87.png", posHead )
                her2 "The \"Gryffindor\" house was founded by Godric Gryffindor, thus the name."
                her2 "The heraldic animal of \"Gryffindor\" is the lion..."
                $herViewHead.showQ( "body_127.png", posHead )
                her "And it's colors are red and gold."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING 
                her "*Gulp!* *Slurp!* *Slurp!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_127.png", posHead )
                her2 "Professor Minerva McGonagall is the headmaster of our house."
                her2 "The \"Gryffindor\" house emphasizes the traits of courage..."
                her2 "As well as \"daring, nerve and chivalry\"..."
                her2 "And thus its members are generally regarded as brave but reckless..."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Slurp!* *Slurp!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_127.png", posHead )
                her2 "\"Gryffindor\" corresponds roughly to the element of fire..."
                her2 "And for that reason the colours of red and gold were chosen."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Gulp!* *Slurp!*"
                m "Hm..."
                m "Well, I thought I could turn this around somehow to make fun of you..."
                $herViewHead.hideQ()
                her "*Slurp??*"
                m "Well, with your house representing courage and righteousness and such..."
                m "And you being a nasty slut..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_86.png", posHead )
                her "Professor!"
                $herViewHead.hideQ()
                $herViewHead.hideQ()
                m "But to be honest..."
                m "\"Daring, nerve, fire, recklessness\"..."
                m "That sort of describes your personality quite well..."
                $herViewHead.showQ( "body_45.png", posHead )
                her "Sir..."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Gobble!!* *Gltch!!* *Gobble!!!*"
                m "Good girl..."
        
        m "Good..."
        her "*Gobble!* *Slurp!* *Slurp!*"
        m "Good... Back and forth, back and forth... Good girl."
        her "*Slurp!* *Slurp!* *Slurp!*"
        her "*Slurp--"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        $herViewHead.showQ( "body_87.png", posHead )
        her "Sir... I am a... whore."
        $herViewHead.hideQ()
        m "What?"
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING
        her "*Slurp-Slurp-Slurp!*"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        $herViewHead.showQ( "body_117.png", posHead )
        her2 "I truly am a slut and deeply enjoy sucking your cock."
        $herViewHead.hideQ()
        m "Oh, yes, yes... Say more things like that."
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING
        her "*Slurp!* *Gulp!* *Slurp!*"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        $herViewHead.showQ( "body_121.png", posHead )
        her "Please, sir. Cum for me."
        $herViewHead.hideQ()
        with hpunch
        g4 "Argh! You little...!!!"
        g4 "{size=-4}(Here it comes. Should I give her a warning?){/size}"
        menu:
            m "..."
            "-Warn her-":
                $herViewHead.showQ( "body_121.png", posHead )
                her "Yes, I love to suck and --"
                $herViewHead.hideQ()
                g4 "Heads up, girl! Here it comes!"
                $herViewHead.showQ( "body_18.png", posHead )
                her "!!!"
                $herViewHead.hideQ()
                show screen ctc
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "cum_in_mouth_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                ">Hermione quickly puts your cock back in her mouth and continues to suck on it with great passion."
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}ARGH!{/size}"
                #Cumming.
                her "*Gulp!-Gulp!-Gulp!*"
                with hpunch
                g4 "And some more!"
                her "*Gulp!* *Gulp!* *Gulp!*"
                hide screen blkfade
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                m "Well, I think that's it."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_126.png", posHead )
                her ".............."
                $herViewHead.hideQ()
                m "Are you alright there, girl?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "Yes, sir..."
                her "You came so much..."
                $herViewHead.hideQ()
                m "You managed to swallow it all though."
                $herViewHead.showQ( "body_123.png", posHead )
                her "Yes... I thought I would choke..."
                her2 "But I made a promise to myself that I won't let go of your penis no matter what!"
                $herViewHead.hideQ()
                m "Good girl."
                $herViewHead.showQ( "body_123.png", posHead )
                her "Thank you, sir."
                her "But, still... You came so much..."
                $herViewHead.showQ( "body_121.png", posHead )
                her "I almost feel as if I just got fed..."
                her "My stomach is so full..."
                $herViewHead.hideQ()
                g9 "Yes, I fed you with my cum!"
                if daytime:
                    $herViewHead.showQ( "body_121.png", posHead )
                    her2 "I think I may skip the meal and go straight to class today."
                else:
                    $herViewHead.showQ( "body_121.png", posHead )
                    her2 "Yes. I think I may skip supper tonight..."
                $herViewHead.showQ( "body_122.png", posHead )
                her "Can I get paid now?"
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
            "-Don't bother-":
                $herViewHead.showQ( "body_121.png", posHead )
                her "Yes, I love to suck and --"
                $herViewHead.hideQ()
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}Whore!{/size}"
                $herViewHead.showQ( "body_48.png", posHead )
                her "!!?"
                $herViewHead.hideQ()
                
                $ g_c_u_pic = "cum_on_face_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                show screen ctc
                hide screen bld1
                with d3
                pause
                hide screen ctc
                show screen bld1
                with d3
                
                #Cumming.
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, 'sperm_04.png', G_Z_FACE + 1 ) )

                $herViewHead.showQ( "body_48.png", posHead )
                her "Professor..."
                $herViewHead.hideQ()
                g4 "Don't you move now, girl."
                g4 "Yes, just be still and take it."
                g4 "Argh! You little slut! You make me cum hard, girl!"
                $herViewHead.showQ( "body_21.png", posHead )
                her ".............."
                $herViewHead.hideQ()
                m "Whew..."
                $ g_c_u_pic = "cum_on_face_blink_ani"
                $herViewHead.showQ( "body_33.png", posHead )
                her ".............."
                $herViewHead.hideQ()
                m "Alright, I'm done..."
                $herViewHead.showQ( "body_31.png", posHead )
                her "................."
                if daytime:
                    her "My classes are about to start..."
                else:
                    pass
                $herViewHead.hideQ()
                m "Just wipe it off and you'll be alright."
                $herViewHead.showQ( "body_31.png", posHead )
                her "............"
                $herViewHead.hideQ()
                m "Unless, you don't want to."
                $herViewHead.showQ( "body_34.png", posHead )
                her "Huh?"
                $herViewHead.hideQ()
                m "And would rather go outside looking like this."
                m "Let everyone see what a nasty little slut you are."
                $herViewHead.showQ( "body_34.png", posHead )
                her "Of course not, sir!"
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
                stop music fadeout 1.0
                if daytime:
                    m "You better go before you are late for your classes..."
                else:
                    m "It's getting late..."
                    $herViewHead.showQ( "body_34.png", posHead )
                    her "Yes..."
                $herViewHead.showQ( "body_44.png", posHead )
                her "Can I get paid before I leave, sir?"
                $herViewHead.hideQ()
                $herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 2 ) )

        
        
    elif request_22_points == 1: #  <============================================================== EVENT 02
        m "Miss Granger?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Sir?"
        m "How about another blowjob?"
        $herView.hideshowQQ( "body_86.png", pos )
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        her "Professor, how dare you propose such a thing to one of your pupils!"
        m "Wha...?"
        $herView.hideshowQQ( "body_86.png", pos )
        her "This is unbecoming of a man of your standing."
        $herView.hideshowQQ( "body_47.png", pos )
        her "You should be ashamed of yourself sir!"
        menu:
            m "???"
            "\"Fine. No points to you then! Leave!\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $herView.hideQQ()
                $herView.showQQ( "body_24.png", pos )
                her "Sir, calm down, please."
                m "You are dismissed, miss Granger."
                $herView.hideQQ()
                $herView.showQQ( "body_24.png", pos )
                her "Sir, please, I didn't mean any of the things I said."
                m "What?"
            "\"Ehm... I am sorry?\"":
                stop music fadeout 1.0
                $herView.hideQQ()
                $herView.showQQ( "body_06.png", pos )
                her "*Giggle*"
                m "Huh?"
                $herView.hideQQ()
                $herView.showQQ( "body_24.png", pos )
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "I got you... sir."
                m "What?"
        $herView.hideshowQQ( "body_45.png", pos )
        her "Well, so much has happened lately..."
        her2 "I had so many new experiences that kind of changed the way I look at things..."
        her2 "So I was just trying to imagine how the \"old me\" would've reacted to this."
        m "So..."
        g4 "You were messing with me then?"
        $herView.hideshowQQ( "body_34.png", pos )
        her "uhm... I'm sorry sir, I didn't mean to..."
        g4 "You nasty little girl! You must be punished!"
        g9 "I'll punish you with my cock!"
        $herView.hideshowQQ( "body_34.png", pos )
        her "..............................."

        jump blowjob_jumping
  
    elif request_22_points >= 2: # <============================================================== EVENT 03
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "Suck my dick, girl."
        $herView.hideshowQQ( "body_45.png", pos )
        her "Of course..."
        # Sucking.
        
        $herView.hideQ()
        hide screen genie
        $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
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
        
        her "*Slurp!* *Slurp!* *Gulp!*"
        m "Yes, good girl..."
        her "*Slurp!* *Gobble!* *Slurp!*"
        
        $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
        "> *Knock-knock-knock!*"
        her "{size=+7}!!!{/size}"
        m "Hm?"
        if daytime:
            m "Who could that be?"
        else:
            m "Who could that be at this hour?"
        $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ hermione_chibi_ypos = 10
        $ h_c_u_pic = "hand_ani" # Not sucking
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        
        $ posHead = gMakePos( 390, 235 )

        $herViewHead.showQ( "body_48.png", posHead )
        her "(Professor, what should I do?)"
        $herViewHead.hideQ()
        m "Just keep sucking my cock, girl. This doesn't concern you."
        sna "Albus? Are you there? I need to talk to you."
        $herViewHead.showQ( "body_117.png", posHead )
        her "(It's professor Snape!)"
        her "(Sir, please, send him away, I beg you!)"
        $herViewHead.hideQ()
        menu:
            m "..."
            "\"Please, come on in, Severus.\"":
                $ mad = 30
                $herViewHead.showQ( "body_76.png", posHead )
                stop music fadeout 1.0
                her "(Sir, no!)"
                $herViewHead.hideQ()
                show screen blktone
                with d3
                with hpunch
                ">Hermione gives your balls a firm twist full of frustration."
                hide screen blktone
                with d3
                g4 "Ouch!"
                hide screen bld1
                with d3
                # SNAPE COMES IN
                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                $ walk_xpos=610 #Animation of walking chibi. (From)
                $ walk_xpos2=360 #Coordinates of it's movement. (To)
                $ snapes_speed = 04.0 #The speed of moving the walking animation across the screen.
                show screen snape_walk_01 
                pause 4
                show screen snape_02 #Snape stands still.
                show screen bld1
                with d3
                $ s_head_xpos = 330 # x = 330,
                $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
                $ s_sprite = "03_hp/10_snape_main/snape_01.png"
                show screen s_head2

                play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                sna "Good, you are here."
                hide screen s_head2
                
                $ g_c_u_pic = "blowjob_ani" # sucking
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_06.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Listen, there is something I want to discuss..."
                $ s_sprite = "03_hp/10_snape_main/snape_05.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Hm...?"
                sna "Genie? Are you alright?"
                hide screen s_head2
                her "{size=-4}(Ginny!!? Is she here as well?!){/size}"
                her "{size=-4}(No, please! I will die of shame!){/size}"
                m "Yes, Severus, I am fine..."
                her "{size=-4}(What? *Slurp...?* *Slurp...?* *Gulp...?*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_05.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "What are you... looking at?"
                hide screen s_head2
                m "Ehm... Just admiring...{w} the cupboard."
                m "Please continue..."
                $ s_sprite = "03_hp/10_snape_main/snape_05.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "..............."
                hide screen s_head2
                her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                m "Did you want to discuss something?"
                $ s_sprite = "03_hp/10_snape_main/snape_06.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Yes. That Hermione girl."
                hide screen s_head2
                her "{size=-4}(*Slurp...!* *Gobble...!* *Gulp...!*){/size}"
                m "Oh... What about her?"
                $ s_sprite = "03_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna2 "You promised that you would take care of the little witch."
                hide screen s_head2
                her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "But she is still being a major pain in my arse!"
                sna "Her tactics have changed..."
                $ s_sprite = "03_hp/10_snape_main/snape_03.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna2 "But the amount of grief she manages to bring me is the same..."
                hide screen s_head2
                m "I see... ah..."
                $ s_sprite = "03_hp/10_snape_main/snape_10.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "I swear, that girl is driving me crazy!"
                hide screen s_head2
                g4 "Yeah, she is driving me crazy as well... ah..."
                her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Will you take care of this then?"
                hide screen s_head2
                m "Yes. She'll get what she deserves."
                $ s_sprite = "03_hp/10_snape_main/snape_06.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Good. That is all I wanted to hear."
                if daytime:
                    hide screen s_head2
                    m "Well, have a good day, Severus."
                    $ s_sprite = "03_hp/10_snape_main/snape_06.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "Yes, thank you."
                else:
                    hide screen s_head2
                    m "Good night, Severus."
                    $ s_sprite = "03_hp/10_snape_main/snape_06.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "Right..."
                # SNAPE LEAVES
                hide screen s_head2
                hide screen ctc
                
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen snape_walk_01_f 
                pause 3
                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                hide screen snape_walk_01_f 
                with d4
                pause.5
                show screen ctc
                stop music fadeout 1.0
                pause
                hide screen ctc
                show screen blkfade
                with d5
    
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                ">Hermione doesn't say a thing. Her face is crimson due to a mix of embarrassment, guilt and excitement."
                ">Seeing her being so confused and vulnerable and yet continuing to perform her task diligently pushes you over the edge."
                g4 "(Here it comes!)"

                
            "\"I am busy right now, Severus.\"":
                $herViewHead.showQ( "body_117.png", posHead )
                her "(Thank you, sir.)"
                $herViewHead.hideQ()
                sna "Busy? With what?"
                sna "All you do is sit on you arse all day."
                sna "I really need to talk to you about something."
                m "I said I am busy, Severus."
                m "Understood? I am \"busy\"!"
                sna "Oh... You mean \"Busy\" busy? Gotcha!"
                sna "Well, I'll talk to you later then."
                #">Hermione keeps sucking on your cock with a rather fierce determination."
                
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING                
                #">Hermione is working hard to please you..."
                her "*Slurp!* *Slurp!* *Gulp!*"
                show screen blktone
                with d3
                ">Hermione keeps sucking on your cock with a rather fierce determination."
                ">Her technique is lacking but she makes up for it with the effort she puts it."
                hide screen blktone
                with d3
                m "Yes... I love your eager, little mouth girl..."
                her "*Gobble!* *Gobble!* *Gobble!*"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_121.png", posHead )
                her "Sir?"
                $herViewHead.hideQ()
                m "Hm?"
                $herViewHead.showQ( "body_121.png", posHead )
                her "Are you going to cum on my face today?"
                her "Or do you plan to cum in my mouth?"
                $herViewHead.hideQ()
                menu:
                    "\"I Plan to splatter you face with cum!\"":
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "I see..."
                        $herViewHead.hideQ()
                        m "Why do you ask?"
                        $herViewHead.showQ( "body_123.png", posHead )
                        her2 "Oh... I just read in a book that semen contains a lot of antioxidants..."
                        her "It's good for the skin..."
                        $herViewHead.hideQ()
                        m "Great. One facial coming up."
                        m "Back to work now."
                    "\"I Plan to fill your mouth with cum!\"":
                        $herViewHead.showQ( "body_123.png", posHead )
                        her "I see..."
                        $herViewHead.hideQ()
                        m "Why do you ask?"
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "Well, I am trying to watch my calorie-intake..."
                        her2 "I just wonder how much calories your load contains, sir."
                        her2 "Maybe I should skip my next meal..."
                        $herViewHead.hideQ()
                        m "Girl."
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "Yes?"
                        $herViewHead.hideQ()
                        m "Dick back in the mouth."
                    "\"I don't plan so far ahead.\"":
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "I see..."
                        $herViewHead.hideQ()
                        m "Don't you like surprises?"
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "Not really..."
                        her "I rather enjoy planning ahead actually..."
                        $herViewHead.hideQ()
                        m "Well some things in life are just unpredictable."
                        m "There is only one way to find out for sure."
                        
                    "\"What would you like?\"":
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "If it is all the same to you, sir..."
                        if generating_points == 1:
                            $herViewHead.showQ( "body_123.png", posHead )
                            her2 "I would like you to cum on my face, sir."
                            her2 "I read that it's good for the skin."
                        else:
                            $herViewHead.showQ( "body_123.png", posHead )
                            her2 "I would like you to cum in my mouth."
                            her2 "You usually cum so much so I think I will be able to just skip my next meal..."
                            her2 "And do some homework instead."
                        $herViewHead.hideQ()
                        m "Well, we'll see about that."
                        m "Back to sucking now."
                    
                    
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING   
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Hm..."
                m "You are getting better at this girl."
                her "*Slurp!* *Slurp!* *Gulp!*"
                m "Ok, say something nasty now..."
                her "*Slurp--?"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_118.png", posHead )
                her "uhm..."
                $herViewHead.showQ( "body_117.png", posHead )
                her "I eat cockroaches?"
                $herViewHead.hideQ()
                m "What the fuck?"
                $herViewHead.showQ( "body_117.png", posHead )
                her "T-they are pretty nasty, sir..."
                $herViewHead.hideQ()
                m "No, girl, I mean something dirty!"
                m "And don't you dare to say \"mud\"!"
                m "I mean dirty in a sexual way!"
                $herViewHead.showQ( "body_118.png", posHead )
                her "Oh... Ehm..."
                $herViewHead.hideQ()
                m "Ah, never mind, the moment is gone..."
                $herViewHead.showQ( "body_117.png", posHead )
                her "Ehm... I'm sorry, sir."
                $herViewHead.hideQ()
                m "Yeah, whatever. Make it up to me by sucking my cock harder."
                $herViewHead.showQ( "body_120.png", posHead )
                her "Of course, sir."
                $herViewHead.hideQ()
                
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING 
                
                her "*Slurp!* *Gulp!* *Slurp!*"
                m "Yes, like this... Good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "You know what? I think we are almost there."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Yes, definitely."
                her "*Slurp!* *Gobble!* *Gobble!*"
                m "Alright, girl, this is the final stretch."
                g4 "Show me what you've got."
                her "!!! *Gobble-goble-slurp-goble!* !!!"
                g4 "Yes, like that!"
                her "{size=+5}!!! *Gobble-gobble-slurp-gobble!* !!!{/size}"
                g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
                g4 "Ghr!!!"
                
        menu:
            g4 "!!!"
            "-Cum in her mouth-":
                hide screen blkfade
                with d3
                g4 "Here it comes, girl! get ready to swallow fast!"
                her "!!!"
                
                $herViewHead.hideQ()
                show screen ctc
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "cum_in_mouth_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}ARGH!{/size}"
                g4 "Eat my cum, slut!"
                #Cumming.
                her "*Gulp!-Gulp!-Gulp!*"
                with hpunch
                g4 "Yes! Down your fucking throat!"
                her "*Gulp-gulp-gulp-gulp-gulp!*"
                hide screen blkfade
                hide screen bld1
                with d3
                show screen ctc
                stop music fadeout 1.0
                pause
                hide screen ctc
                show screen bld1
                with d3
                m "Well, I think that's it."
                m "You can let go now..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_125.png", posHead )
                her "..........................."
                her "................"
                her "........"
                $herViewHead.showQ( "body_126.png", posHead )
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                her "*GULP!*"
                $herViewHead.showQ( "body_115.png", posHead )
                her "Gua-ha..."
                $herViewHead.hideQ()
                m "Ты в порядке?"
                $herViewHead.showQ( "body_123.png", posHead )
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                m "You alright?"
                $herViewHead.hideQ()
                m "Going to skip your next meal?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "I think so..."
                her "You always cum so much, sir..."
                $herViewHead.hideQ()
                m "Heh... And who's fault is tat??"
                $herViewHead.showQ( "body_123.png", posHead )
                her "............." #Smile.
                her "Can I get paid now?"
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3

                
            "-Cum on her face-":
                show screen bld1
                hide screen blkfade
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                g4 "Ready for your facial, girl?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "Yes sir!"
                $herViewHead.hideQ()
                g4 "Here it comes then!"
                
                $herViewHead.hideQ()
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}Whore!{/size}"
                $herViewHead.showQ( "body_48.png", posHead )
                her "!!?"
                $herViewHead.hideQ()
                
                $ g_c_u_pic = "cum_on_face_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                show screen ctc
                hide screen bld1
                with d3
                pause
                hide screen ctc
                show screen bld1
                with d3
                
                #Cumming.
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, 'sperm_04.png', G_Z_FACE + 1 ) )
                $herViewHead.showQ( "body_48.png", posHead )
                her "Professor..."
                $herViewHead.hideQ()
                g4 "All over your fucking face!"
                $herViewHead.showQ( "body_123.png", posHead )
                her "Ааааh!"
                $ g_c_u_pic = "cum_on_face_blink_ani"
                $herViewHead.hideQ()
                m "Well, I'm done."
                $herViewHead.showQ( "body_123.png", posHead )
                her "...................................."
                $herViewHead.hideQ()
                m "I said it's over, girl."
                $herViewHead.showQ( "body_123.png", posHead )
                her "Yes, I heard you sir..."
                $herViewHead.hideQ()
                m "So... Aren't you going to clean up?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "In a moment..."
                her2 "I'm giving my skin time to soak in the anti-oxidants..." 
                $herViewHead.hideQ()
                m "Hm... I find this quite hot..."
                m "Take your time, girl..."
                show screen blkfade
                with d3
                stop music fadeout 1.0 
                ">A while later."
                $herViewHead.data().delItem( 'sperm' )
                $herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                $herViewHead.showQ( "body_122.png", posHead )
                her "I take it you enjoyed yourself sir?"
                $herViewHead.hideQ()
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                m "Yes I did, girl."
                $herViewHead.showQ( "body_123.png", posHead )
                her "Good, so Can I get paid now?"
                $herViewHead.hideQ()
                
                    
                
            
        
    
    $herViewHead.data().delItem( 'sperm' )
    $ gryffindor += current_payout #35
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
    with d3
    
    
    m "Yes, miss Granger. 55 points to \"Gryffindor\"."
    $ gryffindor +=55
    $herView.showQ( "body_13.png", pos )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, sir..."

    if whoring <= 17:
        $ whoring +=1

    
    
    if request_22_points == 0:
        $ new_request_22_01 = True #  HEARTS
    if request_22_points == 1:
        $ new_request_22_02 = True #  HEARTS
    if request_22_points >= 2:
        $ new_request_22_03 = True #  HEARTS

    $ request_22_points += 1

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
    
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            

