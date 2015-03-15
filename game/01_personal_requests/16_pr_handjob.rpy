#############################################################################################################################
### LEVEL 05 ################################################################################################################   
###################REQUEST_16 (Level 05) (HANDJOB) (Day/Night) #####################################################
label new_request_16: #LV.5 (Whoring = 12 - 14)
    $herView.hideQQ()
    if IsFirstRun():
#    if request_16_points == 0:
        m "{size=-4}(Should I ask her for a handjob?){/size}"
    else:
        m "{size=-4}(Should I ask the girl to give me another handjob?){/size}"
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
    $herView.data().saveState()

    $ current_payout = 45 #Used when haggling about price of th favor.  
#    if request_16_points == 0: # FIRST EVENT <============================================================== EVENT 01
    if IsFirstRun(): # FIRST EVENT <============================================================== EVENT 01
        m "Miss Granger."
        $herView.hideshowQQ( "body_01.png", pos )
        her "Yes, professor?"
        m "Do you know what a \"handjob\" is?"
        if whoring <=11:
            jump too_much
        $herView.hideshowQQ( "body_79.png", pos )
        her "Why?"
        m "I feel like getting one..."
        $herView.hideshowQQ( "body_47.png", pos )
        her "Professor!"
        m "Just another favour. No big deal, right?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "......"
        $herView.hideshowQQ( "body_34.png", pos )
        her "{size=-7}I want 100 house points for this...{/size}"
        m "Huh? What was that?"
        $herView.hideshowQQ( "body_32.png", pos )
        her "I want 100 house points for this!!!"
        m "100 house points, huh?"
        m "And you will stroke my cock and everything?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "{size=-7}Yes...{/size}"
        m "Sorry, I couldn't hear you..."
        $herView.hideshowQQ( "body_32.png", pos )
        her "Yes, I said yes! I will stroke your cock, sir!"
        label back_to_handjob_choices:
        menu:
            m "..."
            "\"You will get 15 house points.\"":
                $ mad +=7
                $herView.hideshowQQ( "body_69.png", pos )
                her "For 15 house points I suppose I could let you molest me a little, but that is all you'll be getting, sir."
                her "I will not stoop as low as to sell handjobs for 15 house points."
                her "That is just insulting, sir."
                jump back_to_handjob_choices
            "\"You will get 45 house points.\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "....."
                $herView.hideshowQQ( "body_87.png", pos )
                her "45 house points...?"
                her "This could put \"Gryffindor\" back in the lead..."
                m "Is that a \"yes\"?"
                $herView.hideshowQQ( "body_79.png", pos )
                her "Yes, it is a yes, sir."
                m "Great!"
            "\"you will get 100 house points.\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $ current_payout = 100 #Used when haggling about price of th favor.
                $ mad = 0
                $herView.hideshowQQ( "body_72.png", pos )
                her "100 house points?!"
                her "This will definitely put \"Gryffindor\" in the lead!"
                m "Is that a \"yes\" then?"
                $herView.hideshowQQ( "body_75.png", pos )
                her "Of course!"
                $herView.hideshowQQ( "body_80.png", pos )
                her "If it will bring \"Gryffindor\" 100 house points, I don't mind touching your... thing a little."
        # GENIE STANDS WITH HIS COCK OUT
       
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        $herView.hideQ()
        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02

        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3
        $ posHead = gMakePos( 390, 235 )        
        $herViewHead.showQ( "body_31.png", posHead )
        her "..........."
        $herViewHead.hideQ()
        m "Whenever you're ready, girl."
        $herViewHead.showQ( "body_34.png", posHead )
        her "Right..."
        $herViewHead.hideQ()
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3
        label event_01_round_02:
        ">Hermione puts her slender hands on your cock..."
        m "Good. Now stroke it."
        $herViewHead.showQ( "body_34.png", posHead )
        her "Right..."
        $herViewHead.hideQ()
        #Stroking the cock.
        $ genie_chibi_xpos = 60 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "handjob_ani"
        hide screen hermione_walk_01 
        hide screen blkfade
        with d3
        show screen ctc
        pause
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen ctc
        show screen bld1
        with d3
        g9 "Nice..."
#        if request_16_points == 0:
        if IsFirstRun():
            $herViewHead.showQ( "body_48.png", posHead )
            her "!!!"
            her "Are you about to finish, sir?!"
            $herViewHead.hideQ()
            m "About to finish?"
            m "Don't be ridiculous girl, we are just getting started."
            $herViewHead.showQ( "body_34.png", posHead )
            her "Oh..."
            her "......"
            $herViewHead.showQ( "body_44.png", posHead )
            her2 "You will give me a warning though, won't you, sir?"
            $herViewHead.hideQ()
        else:
            $herViewHead.showQ( "body_34.png", posHead )
            her "Sir...?"
            $herViewHead.hideQ()
            m "What is it?"
            $herViewHead.showQ( "body_34.png", posHead )
            her "Will you warn me before... uhm... you now..."
            $herViewHead.hideQ()
        $ d_flag_01 = False #If TRUE Genie promised to warn her.
        menu:
            m "..."
            "\"Of course I'll let you know when it's time.\"":
                $ d_flag_01 = True #If TRUE Genie promised to warn her.
                $herViewHead.showQ( "body_33.png", posHead )
                her "Thank you, sir."
                $herViewHead.hideQ()
            "\"I myself don't always know when...\"":
                $herViewHead.showQ( "body_31.png", posHead )
                her "Really? But I thought..."
                $herViewHead.showQ( "body_33.png", posHead )
                her "Well, never mind then..."
                $herViewHead.hideQ()
        $herViewHead.showQ( "body_31.png", posHead )
        her "........"
        $herViewHead.hideQ()
        m "............."
        $herViewHead.showQ( "body_33.png", posHead )
        her "............."
        $herViewHead.showQ( "body_33.png", posHead )
        her "Err... Sir?"
        $herViewHead.hideQ()
        m "Yes, what is it?"
        $herViewHead.showQ( "body_31.png", posHead )
        her "How long do you think this will take?"
        $herViewHead.hideQ()
        m "Why?"
        if daytime:
            $herViewHead.showQ( "body_44.png", posHead )
            her2 "Well, it's just that my classes are about to start..."
        else: 
            $herViewHead.showQ( "body_44.png", posHead )
            her2 "Well, it's just that I have this paper that I need to finish..."
            her2 "It's due tomorrow, and it's getting pretty late..."
        $herViewHead.hideQ()
        m "Do you need the points or not?"
        $herViewHead.showQ( "body_74.png", posHead )
        her "I do, sir! I'm sorry..."
        her "I will just keep on stroking it then..."
        $herViewHead.hideQ()
        m "Well, there is something you could do to speed up the process..."
        $herViewHead.showQ( "body_45.png", posHead )
        her "Really? What is it sir?"
        $herViewHead.hideQ()
        menu:
            m "..."
            "\"Tell me how much of a whore you are!\"":
                $herViewHead.showQ( "body_47.png", posHead )
                her "What?"
                her "But I'm not..."
                $herViewHead.hideQ()
                m "No need to be honest, girl."
                m "Just make things up."
                $herViewHead.showQ( "body_44.png", posHead )
                her "Really?"
                $herViewHead.hideQ()
                m "Sure. Just have fun with it."
                $herViewHead.showQ( "body_87.png", posHead )
                her "Well, in that case..."
                her "I am a... whore."
                $herViewHead.hideQ()
                m "Heh... good. Go on."
                $herViewHead.showQ( "body_87.png", posHead )
                her "I am a big whore..."
                $herViewHead.hideQ()
                m "Yes, you are."
                $herViewHead.showQ( "body_79.png", posHead )
                her "I am the biggest whore in England!"
                her2 "I try to act innocent, but in truth all I think about is cock!"
                $herViewHead.hideQ()
                m "Yes, you little slut!"
                $herViewHead.showQ( "body_69.png", posHead )
                her "Yes! I am a slut!"
                her "I crave cock all the time."
                $herViewHead.hideQ()
                m "Very nice!"
                m "But, like I said, you don't have to be honest."
                $herViewHead.showQ( "body_48.png", posHead )
                her "What?"
                $herViewHead.showQ( "body_44.png", posHead )
                her "Sir, those things I say are not true!"
                $herViewHead.hideQ()
                g9 "Heh... I know. I'm just messing with you."
                $herViewHead.showQ( "body_66.png", posHead )
                her "Sir!"
                $herViewHead.hideQ()
                m "You are doing a great job, though. Keep at it!"
                $herViewHead.showQ( "body_87.png", posHead )
                her "....."
                her "I love cock..."
                $herViewHead.showQ( "body_88.png", posHead )
                her "And I love... spunk..."
                her "And semen... and sperm..."
                her "I love to drink sperm..."
                $herViewHead.showQ( "body_65.png", posHead )
                her "I want you to feed me your sperm, sir!"
                $herViewHead.hideQ()
                g4 "!!!"
                $herViewHead.showQ( "body_64.png", posHead )
                her2 "Or better yet, pump me full of it, sir!"
                hide screen ctc
                $herViewHead.hideQ()
                with hpunch
                g4 "{size=-4}(Here it comes! Should I warn her?){/size}"
            
            "\"Stick your tongue out and look at me!\"":
                $herViewHead.showQ( "body_45.png", posHead )
                her "What?"
                $herViewHead.hideQ()
                m "Just do it, slut."
                $herViewHead.showQ( "body_38.png", posHead )
                her "Like this?"
                $herViewHead.hideQ()
                m "Yes, good. Keep looking into my eyes and stroke my cock."
                $herViewHead.showQ( "body_115.png", posHead )
                her "....................."
                $herViewHead.hideQ()
                m "Yes... Good..."
                $herViewHead.showQ( "body_115.png", posHead )
                her "..........."
                her "..........."
                $herViewHead.showQ( "body_31.png", posHead )
                her2 "I can't keep my mouth open for so long, sir. I will start to drool..."
                $herViewHead.hideQ()
                m "But I want you to drool..."
                $herViewHead.showQ( "body_31.png", posHead )
                her "What? But I will look silly!"
                $herViewHead.hideQ()
                m "That's the point, girl!"
                $herViewHead.showQ( "body_29.png", posHead )
                her "......."
                $herViewHead.hideQ()
                m "Don't you want to be done with this as soon as possible?"
                $herViewHead.showQ( "body_33.png", posHead )
                her "............"
                $herViewHead.showQ( "body_115.png", posHead )
                her "A-ha....."
                $herViewHead.hideQ()
                m "Good, girl."
                $herViewHead.showQ( "body_115.png", posHead )
                her ".............."
                $herViewHead.hideQ()
                m "Yes, keep on stroking my cock."
                $herViewHead.showQ( "body_115.png", posHead )
                her ".................."
                $herViewHead.hideQ()
                g4 "Oh... I just want to slide my cock into that wet hole of a mouth of yours!"
                $herViewHead.showQ( "body_40.png", posHead )
                her "................."
                $herViewHead.hideQ()
                m "No, keep on looking at me!"
                $herViewHead.showQ( "body_115.png", posHead )
                her "....................."
                $herViewHead.hideQ()
                m "Yes, you little slut!"
                $herViewHead.showQ( "body_116.png", posHead )
                her "......................"
                $herViewHead.hideQ()
                m "I want to cum in that mouth, yes..."
                $herViewHead.showQ( "body_116.png", posHead )
                her "................"
                $herViewHead.hideQ()
                with hpunch
                g4 "{size=-4}(Here it comes! Should I warn her?){/size}"

            "\"Give my cock a kiss!\"":
                $herViewHead.showQ( "body_47.png", posHead )
                her "Excuse me?"
                $herViewHead.hideQ()
                m "You know, just a little kiss, right on the tip."
                $herViewHead.showQ( "body_47.png", posHead )
                her "............."
                $herViewHead.showQ( "body_48.png", posHead )
                her "...with my lips?"
                $herViewHead.hideQ()
                m "Sure... That will speed things up, I'm telling you."
                $herViewHead.showQ( "body_87.png", posHead )
                her "*sigh!*.............."
                her "Well, I might as well, I suppose..."
                $herViewHead.hideQ()
                ">Hermione gives the tip of your engorged cock a tender kiss."                
                
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3

                $herViewHead.showQ( "body_87.png", posHead )
                her "Like this?"
                $herViewHead.hideQ()
                m "Wasn't that bad, was it?"
                $herViewHead.showQ( "body_44.png", posHead )
                her "No, I suppose not..."
                $herViewHead.hideQ()
                m "Can you do it again, then?"
                $herViewHead.showQ( "body_33.png", posHead )
                her "I could..."
                $herViewHead.hideQ()
                m "Do it!"
                $herViewHead.showQ( "body_31.png", posHead )
                her "Well, alright..."
                $herViewHead.hideQ()
                ">Hermione gives your cock another kiss..."
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                ">This time she lingers a moment longer..."
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3

                $herViewHead.hideQ()
                m "Good... Now do it again and just stay there for a while."
                $herViewHead.showQ( "body_31.png", posHead )
                her "You mean with my lips touching your... cock, sir?"
                $herViewHead.showQ( "body_29.png", posHead )
                her "No, I will look stupid..."
                $herViewHead.hideQ()
                m "Don't be silly, girl. Nobody is watching."
                $herViewHead.showQ( "body_87.png", posHead )
                her "You are, sir."
                $herViewHead.hideQ()
                m "But that's the whole point!"
                $herViewHead.showQ( "body_79.png", posHead )
                her "......"
                $herViewHead.hideQ()
                m "It will make me cum in no time!"
                $herViewHead.showQ( "body_69.png", posHead )
                her "..............."
                $herViewHead.hideQ()
                m "And then you can just get out and and take care of your business today."
                $herViewHead.showQ( "body_66.png", posHead )
                her "............."
                $herViewHead.showQ( "body_87.png", posHead )
                her "Well, alright then...."
                $herViewHead.hideQ()
                ">Hermione reaches down with her lips again..."
                ">She touches the tip of your cock with her lips and keeps them there..."
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                $herViewHead.hideQ()
                show screen blktone
                with d3
                m "Very good..."
                m "Now touch it with your tongue."
                her "??!"
                $herViewHead.hideQ()
                m "That's the last thing I will be asking of you today."
                her "............"
                ">You feel the tip of Hermione's tongue warily rubbing against the head of your cock..."
                $herViewHead.hideQ()
                m "Yes, like this..."
                ">Hermione wiggles her tongue a little...."
                $herViewHead.hideQ()
                m "Yes... Good..."
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3
                $herViewHead.showQ( "body_87.png", posHead )
                her2 "So, did it work? Are you ready to... finish, professor?"
                $herViewHead.hideQ()
                g4 "{size=-4}(Surprisingly, yes! I'm about to cum! Should I warn her?){/size}"
                hide screen blktone
        menu:
            m "..."
            "-Give her a warning-":
                g4 "Here it comes, girl! You better be ready!"
                $herViewHead.showQ( "body_48.png", posHead )
                her "What? So soon?!"
                $herViewHead.hideQ()
                g4 "{size=+5}Yeah, you did a great job!!!{/size}"
                g4 "{size=+5}You little whore!!!{/size}"
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade 
                with d5
                $herViewHead.showQ( "body_117.png", posHead )
                her "No, professor, wait, I--"
                $herViewHead.hideQ()
                g4 "{size=+5}Too late for that, slut!{/size}"
                $herViewHead.showQ( "body_118.png", posHead )
                her2 "*whimper*"
                $herViewHead.hideQ()
                ">Hermione suddenly slides your already dripping cock under her shirt..."
                g4 "?!!"
                ">The sensation of her warm skin against your cock overwhelms you and you begin to ejaculate like a mad-man."
                $herViewHead.hideQ()
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}ARGH! YES!!!{/size}"
              
                
                
                
                
                
                $herViewHead.showQ( "body_48.png", posHead )
                her "!!!!!!!!!!!"
                $herViewHead.hideQ()
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "undershirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                stop music fadeout 1.0
                pause 
                        
                #$herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm_dried' )
                $ posHead = gMakePos( 390, 300 )
                $herViewHead.showQ( "body_119.png", posHead )
                her2 "......................."
                $herViewHead.hideQ()
                m "..........................."
                $herViewHead.showQ( "body_119.png", posHead )
                her2 "......................."
                $herViewHead.hideQ()
                m "....................?"
                $herViewHead.showQ( "body_118.png", posHead )
                her2 "......................."
                $herViewHead.hideQ()
                m "...What the fuck just happened?"
                show screen bld1
                with d3
                $herViewHead.showQ( "body_34.png", posHead )
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "I don't know... I suppose I just panicked..."
                $herViewHead.hideQ()
                if daytime:
                    $herViewHead.showQ( "body_34.png", posHead )
                    her2 "My classes are about to start and I didn't want you to ruin my uniform, sir..."
                    $herViewHead.hideQ()
                    m "So you'll go to classes like this now?"
                    m "With your clothes all sperm-soaked from the inside?"
                    $herViewHead.showQ( "body_118.png", posHead )
                    her2 "What choice do I have?"
                    her2 "I can't just skip a class..."
                    $herViewHead.hideQ()
                else:
                    $herViewHead.showQ( "body_34.png", posHead )
                    her2 "At this hour The \"Gryffindor\" common room will be full of people..."
                    her2 "I didn't want to have to return there all covered in your... spunk, sir."
                    $herViewHead.showQ( "body_117.png", posHead )
                    her2 "Oh, it's getting pretty late..."
                    $herViewHead.hideQ()
                    m "So you will go like this, instead?"
                    m "With your clothes all sperm-soaked from the inside?"
                    $herViewHead.showQ( "body_118.png", posHead )
                    her "What choice do I have?"
                    $herViewHead.hideQ()
                    
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                ">Hermione releases your still pulsating cock."
                
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                show screen genie
                hide screen g_c_u
                $ posHead = gMakePos( 390, 235 )
                $herViewHead.showQ( "body_118.png", posHead )
                her "Ew... Your sperm, sir..."
                $herViewHead.showQ( "body_117.png", posHead )
                her "It's everywhere under my uniform..."
                $herViewHead.hideQ()
                m "Just put it in your mouth next time."
                $herViewHead.showQ( "body_79.png", posHead )
                her "I... don't think so, sir."
                her2 "I really need to go. Can I just get paid now?"
                $herViewHead.hideQ()
                
                
                
                
                
                
#                g4 "You whore! You little nasty wore!"
#                g4 "There! Allover your fucking belly and tits!"
#                her "Ah! It's so hot!"
#                hide screen h_head2 

#                g4 "Ох, yes, this is so good!"
#                her "Ah..."
#                hide screen h_head2 

#                m "..............."
#                her "............"
#                hide screen h_head2 

#                m "I think I'm done..."
#                her "Ох..."
#                ">Hermione releases your still pulsating cock."
#                her "Ew... Your sperm, сэр..."
#                her "It's everywhere under my uniform..."
#                hide screen h_head2 
#                m "What possessed you to put my cock there, м?"
                

            "-Just start cumming-":
                hide screen ctc
                with hpunch
                g4 "ARGH!"
                show screen blkfade
                with d3
                $herViewHead.showQ( "body_48.png", posHead )
                her "WHAT?!"
                $herViewHead.hideQ()
                g4 "Take this!"

                $herViewHead.hideQ()
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}ARGH! YES!!!{/size}"
                
                
                
                  
                $herViewHead.showQ( "body_48.png", posHead )
                her "!!!!!!!!!!!"
                $herViewHead.hideQ()
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "on_shirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                hide screen bld1
                with d3
                pause
                show screen bld1
                with d3
                        
                #$herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm_dried' )
                $ posHead = gMakePos( 390, 300 )
                $herViewHead.showQ( "body_119.png", posHead )
                her2 "......................."
                $herViewHead.hideQ()
                m "Yes... I Feel so much better now..."
                pause
                $ g_c_u_pic = "03_hp/08_animation_02/15_cum_21.png"
                
                #$herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_03_blowjob.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '03' )
               
                $ pos.xpos = 130
                $herView.showQ( "body_19.png", pos )
                with d5
                pause
                her ".........."
                m "Well, I think that's about it..."
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                hide screen g_c_u
                show screen genie
                $herView.hideQ()
                with fade                                                                                                                                                                                                                      #HERMIONE
                $ pos = POS_140
                $herView.showQQ( "body_32.png", pos )
                her "Professor! What have you done?!"
                m "What?"
                if d_flag_01: #If TRUE Genie promised to warn her.
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $ mad += 11
                    $herView.hideQQ()
                    $herView.showQQ( "body_47.png", pos )
                    her "You promised to give me a warning, sir!"
                    m "Oh, that's right... My bad."
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "My uniform is ruined..."
                    her "...I would like to get paid now."
                    $herView.hideQQ()
                else:
                    if daytime:
                        $herView.hideshowQQ( "body_69.png", pos )
                        her "My uniform is ruined now!"
                        $herView.hideshowQQ( "body_87.png", pos )
                        her "My classes are about to start and I can't go looking like this!"
                        m "Of course you can, just wipe it off or something..."
                        m "Nobody will even notice."
                        $herView.hideshowQQ( "body_79.png", pos )
                        her "...I would like to get paid now."
                        $herView.hideQQ()
                        #$herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
                        $herViewHead.data().addItem( 'item_sperm_dried' )
                    else:
                        $herView.hideshowQQ( "body_69.png", pos )
                        her "My uniform is ruined!"
                        her "Am I supposed to go back to the \"Gryffindor\" common room looking like this?!"
                        m "Why not? You look hot, girl!"
                        $herView.hideshowQQ( "body_79.png", pos )
                        her "PROFESSOR!!!"
                        m "Alright, alright. Just wipe it off or something."
                        m "Nobody will even notice."
                        $herView.hideshowQQ( "body_79.png", pos )
                        her "...I would like to get paid now."
                        $herView.hideQQ()
                        #$herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
                        $herViewHead.data().addItem( 'item_sperm_dried' )
        #her "Can I get my points?"

    elif IsRunNumber(2): # SECOND EVENT <============================================================== EVENT 02
#    elif request_16_points == 1: # SECOND EVENT <============================================================== EVENT 02
        m "Miss Granger?"
        $herView.hideQQ()
        $ pos = POS_140
        $herView.showQQ( "body_01.png", pos )
        her "Yes, sir?"
        m "Do you know what a \"handjob\" is?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "You have asked me that already, sir."
        m "Ah, that's right."
        m "Well, I want you to play with my cock again."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Sir, you are being vulgar again..."
        m "Fine, fine."
        m "Miss Granger, I would like to buy another favour from you today."
        $herView.hideshowQQ( "body_69.png", pos )
        her "Of course, sir."
        g9 "The favour being you playing with my cock!"
        $herView.hideshowQQ( "body_66.png", pos )
        her ".............."
        m "Oh, come on. For the honour of the \"Gryffindors\"?"
        $herView.hideshowQQ( "body_47.png", pos )
        her "............."
        g9 "Play with my cock for the honour of the \"Gryffindors\", girl!"
        $herView.hideshowQQ( "body_86.png", pos )
        her "Stop saying that, sir..."
        #Genie with his cock out
        m "Come on girl, it's not like I'm asking you to do this for free."
        $herView.hideshowQQ( "body_69.png", pos )
        her "......."
        stop music fadeout 4.0
        

        $herView.hideQ()
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3                                                                                                                                                                      #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02
        hide screen blktone

        jump event_01_round_02


    elif IsRunNumberOrMore(3): # THIRD EVENT <========================================================================================================= EVENT 03
#    elif request_16_points >= 2: # THIRD EVENT <========================================================================================================= EVENT 03
#        $ new_request_16_03 = True #  Hearts
        
        m "Miss Granger?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Sir?"
        m "You don't mind giving me another handjob, do you?"
        $herView.hideshowQQ( "body_68.png", pos )
        her "As long as I am getting paid..."
        m "Well, come here then. Time to earn those points."
        
        label new_request_16_jerkonly:
        $herView.hideQ()
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3

        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02
        hide screen blktone
        
        
        
        ">Hermione puts her slender hands on your cock..."
        $ posHead = gMakePos( 390, 290 )
        $herViewHead.showQ( "body_68.png", posHead )
        stop music fadeout 3.0
        her "Do you like it when I do it like this, sir?"
        $herViewHead.hideQ()
        g9 "Actually, yes! Very nice!"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $herViewHead.hideQ()
        #Stroking the cock.
        $ genie_chibi_xpos = 60 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "handjob_ani"
        hide screen hermione_walk_01 
        hide screen blkfade
        with d7
        show screen ctc
        pause
        hide screen ctc
        show screen bld1
        with d3

        m "Yes, yes, like that..."
        m "Hm... You are getting pretty good at this."
        $herViewHead.showQ( "body_74.png", posHead )
        her "Thank you, sir."
        her2 "I figured the better I do this, the sooner it'll be over."
        $herViewHead.hideQ()
        m "Hm..."
        menu:
            m "..."
            "\"What do you think of my cock?\"":
                $herViewHead.showQ( "body_31.png", posHead )
                her "Huh?"
                her2 "Oh, that's right..."
                $herViewHead.showQ( "body_34.png", posHead )
                her2 "I need to compliment your penis! I completely forgot about that!"
                $herViewHead.hideQ()
                m "Well, you don't have to--"
                $herViewHead.showQ( "body_120.png", posHead )
                her "Sir, let me be honest with you..."
                $herViewHead.hideQ()
                m "Yes?"
                $herViewHead.showQ( "body_111.png", posHead )
                her "You have the biggest penis I have ever seen!"
                $herViewHead.hideQ()
                m "Well I suppo--"
                $herViewHead.showQ( "body_30.png", posHead )
                her "Not done yet!"
                $herViewHead.hideQ()
                m "Apologies."
                $herViewHead.showQ( "body_118.png", posHead )
                her "Your penis is so big it almost scares me!"
                $herViewHead.hideQ()
                g9 "You little mynx. You know exactly what to say..."
                $herViewHead.showQ( "body_121.png", posHead )
                her "And yet I lust for it..."
                her2 "Any woman would be happy to have your huge penis inside of her!"
                $herViewHead.hideQ()
                m "...you're good!"
                $herViewHead.showQ( "body_30.png", posHead )
                her "There is more!"
                $herViewHead.hideQ()
                m "By all means..."
                $herViewHead.showQ( "body_30.png", posHead )
                her2 "I think your magnificent cock is a blessing to this world!"
                $herViewHead.hideQ()
                m "Well, I wouldn't go that far--"
                $herViewHead.showQ( "body_30.png", posHead )
                her2 "Listen to me, sir!"
                her2 "I think a statue dedicated to your magnificent penis shall be erected in every city!"
                her2 "So that people of the world could worship your phallus freely!"
                $herViewHead.hideQ()
                m "OK, I think I've heard enough."
                $herViewHead.showQ( "body_112.png", posHead )
                her "Too much?"
                $herViewHead.hideQ()
                m "Yeah, just a bit."
                $herViewHead.showQ( "body_34.png", posHead )
                her "Sorry..."
                $herViewHead.hideQ()
                m "No biggie. Just keep on stroking it."
                $herViewHead.showQ( "body_121.png", posHead )
                her2 "................."
                $herViewHead.hideQ()
                show screen blktone
                with d3
                ">Hermione keeps on stroking your cock."
                ">She is doing a great job of it too."    
                hide screen blktone
                with d3
                m "Yes, yes... Like that."
                
            "\"Call yourself a whore, girl!\"":
                $herViewHead.showQ( "body_31.png", posHead )
                her "Excuse me?"
                $herViewHead.showQ( "body_17.png", posHead )
                her2 "Oh, that's right! I'm supposed to degrade myself, right?"
                $herViewHead.hideQ()
                m "Well, you don't have to, but..."
                $herViewHead.showQ( "body_120.png", posHead )
                her2 "That's alright, I don't mind."
                $herViewHead.showQ( "body_45.png", posHead )
                her "Alright then! I am a whore!"
                $herViewHead.hideQ()
                m "Good. Glad we established that."
                m "Now I want you to say..."
                menu:
                    m "..."
                    "\"I am a worthless slut!\"":
                        $herViewHead.showQ( "body_122.png", posHead )
                        her "Of course."
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "I am a worthless slut."
                        her "A dirty little slut, that's what I am."
                        $herViewHead.hideQ()
                        m "Yes! Good!"
                    "\"I live to suck cock!\"":
                        $herViewHead.showQ( "body_122.png", posHead )
                        her "Em..."
                        $herViewHead.showQ( "body_45.png", posHead )
                        her2 "I live to suck penis, er... I mean cock..."
                        $herViewHead.hideQ()
                        m "Really? Well why don't you suck on this one then?"
                        $herViewHead.showQ( "body_111.png", posHead )
                        her2 "Sir, I am just repeating after you..."
                        $herViewHead.hideQ()
                        m "Really? Could've fooled me...."
                        $herViewHead.showQ( "body_122.png", posHead )
                        her2 "...................."
                        $herViewHead.hideQ()
                        m ".................."
                    "\"I love to swallow cum!\"":
                        $herViewHead.showQ( "body_122.png", posHead )
                        her "I love to... ehm... swallow cum."
                        $herViewHead.hideQ()
                        m "You hesitated there for a moment."
                        $herViewHead.showQ( "body_122.png", posHead )
                        her "Yes, I know...."
                        her "Let me try again..."
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "I love to swallow cum!"
                        her "It is truly the best to swallow cum!"
                        her "I love it!"
                        $herViewHead.showQ( "body_123.png", posHead )
                        her2 "..................................."
                        $herViewHead.showQ( "body_122.png", posHead )
                        her "How was that, sir?"
                        $herViewHead.hideQ()
                        m "Perfect." 
            "\"This is really good. Did you practice?\"":
                $herViewHead.showQ( "body_74.png", posHead )
                her "Hm?"
                her "Sort of... Well not really..."
                $herViewHead.showQ( "body_122.png", posHead )
                her "I had a talk with the girls, and..."
                $herViewHead.hideQ()
                m "About handjobs?"
                $herViewHead.showQ( "body_80.png", posHead )
                her "Among other things..."
                $herViewHead.hideQ()
                m "So those girls of yours, they know a lot about such things?"
                $herViewHead.showQ( "body_48.png", posHead )
                her "Actually, yes. I was surprised myself."
                $herViewHead.showQ( "body_68.png", posHead )
                her2 "All sorts of weird sexual things seem to be happening lately in our school..."
                her "Can't say I approve of that..."
                $herViewHead.showQ( "body_74.png", posHead )
                her "But they did teach me quite a few... tricks."
                $herViewHead.hideQ()
                m "Really? Like what?"
                $herViewHead.showQ( "body_124.png", posHead )
                her "Well, let's see..."
                her "If I put one of my hands here..."
                her "And another one here..."
                $herViewHead.hideQ()
                m "Oh, I see... Yes, this feels quite good."
                $herViewHead.showQ( "body_122.png", posHead )
                her "Does it?"
                $herViewHead.showQ( "body_68.png", posHead )
                her "So Ginny was right about this one..."
                $herViewHead.hideQ()
                g4 "What did you just say?"
                $herViewHead.showQ( "body_74.png", posHead )
                her "Ginny Weasley, she taught me this one."
                $herViewHead.hideQ()
                m "Oh, right..."
                $herViewHead.showQ( "body_124.png", posHead )
                her2 "She said any boy would fall in love with me if I did this to him..."
                her2 "There is also this thing when I form a ring with my fingers..."
                her2 "And then I put one finger here..."
                $herViewHead.hideQ()
                m "Hm... I don't feel anything..."
                $herViewHead.showQ( "body_118.png", posHead )
                her "Really?"
                her "Hm..."
                $herViewHead.showQ( "body_124.png", posHead )
                her "Oh! That's right!"
                her "The finger goes here! Silly me!"
                $herViewHead.hideQ()
                with hpunch
                with kissiris
                g4 "Oh!!! By the great desert sands, yes!"
                $herViewHead.showQ( "body_80.png", posHead )
                her "Really? That good?"
                $herViewHead.showQ( "body_124.png", posHead )
                her2 "What if I keep doing this but stick my finger here and press a little..."
                $herViewHead.hideQ()
                g4 "Girl, you are killing me!"
                $herViewHead.showQ( "body_80.png", posHead )
                her "Really? Really?!"
                her "This is actually quite fun!"
                $herViewHead.showQ( "body_122.png", posHead )
                her "Err... I mean..."
                her "I am only doing this to help my house of course..."
                $herViewHead.hideQ()
                m "Yes, yes... The \"Gryffindor\" honour and all that."
                m "You just keep massaging that spot..."
                m "Oh, yes..."
                $herViewHead.showQ( "body_124.png", posHead )
                her "..............."
                $herViewHead.hideQ()
        m "Yes... Keep stroking it."
        $herViewHead.showQ( "body_122.png", posHead )
        her ".............."
        $herViewHead.hideQ()
        m "Now I want you to say..."
        menu:
            m "..."
            "{size=-4}\"I fantasize about being raped by my father.\"{/size}":
                $ mad += 11
                $herViewHead.showQ( "body_77.png", posHead )
                her "I do not!"
                $herViewHead.hideQ()
                m "I know. Just say it."
                $herViewHead.showQ( "body_76.png", posHead )
                her "My father? That's disgusting, sir!"
                $herViewHead.hideQ()
                m "Humour me."
                $herViewHead.showQ( "body_79.png", posHead )
                her "..........."
                $herViewHead.showQ( "body_87.png", posHead )
                her "Well..."
                her "Sometimes I fantasize about being raped..."
                her "......."
                $herViewHead.hideQ()
                m "I see. And in those fantasies of yours..."
                m "Who is doing the raping?"
                $herViewHead.showQ( "body_117.png", posHead )
                her "My father...?"
                $herViewHead.hideQ()
                m "Do you enjoy it?"
                $herViewHead.showQ( "body_118.png", posHead )
                her "No. I cry and beg for him to stop!"
                $herViewHead.hideQ()
                m "Heh... Nice."
                $herViewHead.showQ( "body_118.png", posHead )
                her "......."
                $herViewHead.hideQ()
                m "Well, this wasn't that hard, was--"
                $herViewHead.showQ( "body_67.png", posHead )
                her "I scream for my Mommy but she is still at work..."
                $herViewHead.hideQ()
                m "Huh?"
                $herViewHead.showQ( "body_33.png", posHead )
                her "My daddy takes me to my room..."
                her "He throws me on my bed!"
                $herViewHead.showQ( "body_32.png", posHead )
                her "I cry \"No, daddy, please, I'm still a virgin!\""
                $herViewHead.showQ( "body_123.png", posHead )
                $ g_c_u_pic= "03_hp/08_animation_02/12_handjob_01.png"
                her "But He doesn't listen! He ripps my panties off!"
                $herViewHead.showQ( "body_22.png", posHead )
                her "I beg him to stop! I scream and I scream!"
                $herViewHead.hideQ()
                m "Uhm, girl?"
                $herViewHead.showQ( "body_21.png", posHead )
                her "Yes?"
                $herViewHead.hideQ()
                m "You are not stroking my cock anymore..."
                $herViewHead.showQ( "body_24.png", posHead )
                her "Oh, I am sorry, sir."
                her "I got lost in thought..."
                $ g_c_u_pic = "handjob_ani"
                $herViewHead.showQ( "body_31.png", posHead )
                her "But everything I just said is not true of course!"
                her "I never have fantasies like that!"
                $herViewHead.hideQ()
                m "Right."
            "{size=-4}\"Sometimes I get lonely and let my dog mount me.\"{/size}":
                $herViewHead.showQ( "body_18.png", posHead )
                her "What?!"
                $herViewHead.showQ( "body_17.png", posHead )
                her "That's disgusting."
                $herViewHead.showQ( "body_16.png", posHead )
                her "Dogs carry {size=+5}STD{/size}s, sir."
                $herViewHead.hideQ()
                m "Actually, human and canine {size=+5}STD{/size}s are species specific..."
                m "Means that they can only be spread to the same species."
                $herViewHead.showQ( "body_08.png", posHead )
                her "............"
                $herViewHead.hideQ()
                m "Also I hear that many women do enjoy getting \"knotted\" quite a bit."
                $herViewHead.showQ( "body_07.png", posHead )
                her "What does getting \"knotted\" mean?"
                $herViewHead.hideQ()
                m "Ehm... Well..."
                m "Ah, it doesn't matter."
                m "Just say the thing!"
                $herViewHead.showQ( "body_03.png", posHead )
                her "Fine!"
                $herViewHead.showQ( "body_08.png", posHead )
                her "Sometimes I get lonely and let my dog mount me."
                $herViewHead.hideQ()
                m "That sounded so fake..."
                $herViewHead.showQ( "body_07.png", posHead )
                m "Because we have not even dogs!"
                $herViewHead.hideQ()
                m "Fine, whatever, let's just move on then..."
            "{size=-4}\"-Manual user input-\"{/size}":
                window hide
                # The phrase in the brackets is the text that the game will display to prompt 
                # the player to enter the name they've chosen.
                $ jasname = renpy.input("(Use keyboard to enter the phrase.)")

                $ jasname = jasname.strip()
                # The .strip() instruction removes any extra spaces the player may have typed by accident.

                #  If the player can't be bothered to choose a name, then we
                #  choose a suitable one for them:
                if jasname == "":
                    $ jasname="I'm a whore."
                    $herViewHead.showQ( "body_29.png", posHead )
                    her2 "Hm...?"
                    her2 "Should I just say \"I'm a whore\" as usual?"
                    $herViewHead.hideQ()
                if one_out_of_three == 1:
                    $herViewHead.showQ( "body_29.png", posHead )
                    her "I don't want to say that..."
                    $herViewHead.hideQ()
                    m "Oh, just do it, girl."
                    $herViewHead.showQ( "body_29.png", posHead )
                    her "..........."
                    $herViewHead.showQ( "body_30.png", posHead )
                    her2 "[jasname]"
                    $herViewHead.hideQ()
                    g9 "He-he..."
                    $herViewHead.hideQ()
                elif one_out_of_three == 2:
                    $herViewHead.showQ( "body_29.png", posHead )
                    her "Huh?"
                    her2 "What does That have to do with anything?"
                    $herViewHead.hideQ()
                    m "Just say it."
                    $herViewHead.showQ( "body_29.png", posHead )
                    her "......"
                    $herViewHead.hideQ()
                    m "Come on, humour me."
                    $herViewHead.showQ( "body_30.png", posHead )
                    her2 "[jasname]"
                    $herViewHead.hideQ()
                    g9 "He-he..."
                    $herViewHead.hideQ()
                elif one_out_of_three == 3:
                    $herViewHead.showQ( "body_29.png", posHead )
                    her "..........."
                    her2 "Do I really have to?"
                    $herViewHead.hideQ()
                    m "Just say it."
                    $herViewHead.showQ( "body_30.png", posHead )
                    her2 "[jasname]"
                    $herViewHead.hideQ()
                    g9 "He-he..."
        
        #CUMMING
        m "Hm..."
        m "I love that thing you do with the palm of your hand!"
        $herViewHead.showQ( "body_30.png", posHead )
        her2 "You noticed...?"
        her2 "Shall I do it some more then?"
        $herViewHead.hideQ()
        show screen blkfade
        with d3
        ">Hermione presses her palm against the tip of your pulsating cock and starts rubbing it very gently..."
        m "Oh yes!!!"
        stop music fadeout 1.0
        g4 "{size=-5}(I think this is it! Should I give her a waring?){/size}"
        menu:
            m "..."
            "\"(Yes, I must warn her).\"":
                g4 "I think I'm about to--"
                if whoring >= 18: # LEVEL 07
                    jump kiss_suck
                else:
                    pass
                ">Hermione swiftly pulls her shirt up..."
                ">She then pushes your already dribbling cock against her belly and covers it up again..."
                ">The sensation of her skin under your engorged cock almost makes you lightheaded..."
                ">Hermione placed your cock a bit higher than you would expect..."
                ">You can feel her incredibly soft tits rubbing against the tip of your cock..."
               
                
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}ARGH! YES!!!{/size}"
              
                
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                
                
                
                $herViewHead.showQ( "body_48.png", posHead )
                her "!!!!!!!!!!!"
                $herViewHead.hideQ()
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "undershirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                pause 
                        
                #$herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm_dried' )
                $ posHead = gMakePos( 390, 300 )

                
                
                g4 "Argh! You whore!"
                $herViewHead.showQ( "body_124.png", posHead )
                her2 "Yes, sir! Just let it out!"
                $herViewHead.hideQ()
                g4 "Argh! Fucking slut!"
                #Cuming.
                $herViewHead.showQ( "body_64.png", posHead )
                her2 "Ah!! It's so hot!"
                $herViewHead.showQ( "body_121.png", posHead )
                her2 "And it's getting everywhere! So much of it!"
                her2 "...professor."
                $herViewHead.hideQ()
                g4 "Argh!!!"
                m "............"
                m "I think I am done..."
                $herViewHead.showQ( "body_122.png", posHead )
                her2 "Ah, alright..."
                $herViewHead.showQ( "body_124.png", posHead )
                her2 ".............."
                $herViewHead.showQ( "body_121.png", posHead )
                her2 "You came so much this time, sir..."
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d5
                ">Hermione releases your still pulsating cock."
                
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                show screen genie
                hide screen g_c_u
                $ posHead = gMakePos( 390, 235 )
                hide screen blkfade
                with d5
                
               
                
                
                
                
                if daytime:
                    $herViewHead.showQ( "body_45.png", posHead )
                    her2 "Well, I think I'd better go now... my Classes are about to start."
                else:
                    $herViewHead.showQ( "body_45.png", posHead )
                    her2 "Well, I think I'd better go now...  It's getting late."
                $herViewHead.hideQ()
                m "Will you be alright in those clothes?"
                $herViewHead.showQ( "body_87.png", posHead )
                her "What?"
                $herViewHead.showQ( "body_68.png", posHead )
                her "Oh. Yes, I will be fine..."
                $herViewHead.showQ( "body_74.png", posHead )
                her2 "It may soak through a little here and there, but I doubt that anyone will notice."
                $herViewHead.hideQ()
                m "Hm... You could just put it in your mouth next time, and avoid the trouble..."
                $herViewHead.showQ( "body_122.png", posHead )
                her "And swallow your hot spunk like that, sir?"
                $herViewHead.hideQ()
                m "Would keep your clothes clean."
                $herViewHead.showQ( "body_120.png", posHead )
                her "With all due respect sir..."
                $herViewHead.showQ( "body_122.png", posHead )
                her2 "Not for the meagre 45 points..."
                her2 "Speaking of which. Can I get may payment now please?"
                $herViewHead.hideQ()
                

            "\"(Nah... no need).\"":
                g4 "Here! Take this, whore!"
                if whoring >= 18: # LEVEL 07
                    jump kiss_suck
                else:
                    pass
                with hpunch
                g4 "ARGH!"
                show screen blkfade
                with d3
                $herViewHead.showQ( "body_48.png", posHead )
                her "WHAT?!"
                $herViewHead.hideQ()
                g4 "Take this!"

                $herViewHead.hideQ()
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}ARGH! YES!!!{/size}"
                
                
                
                  
                $herViewHead.showQ( "body_48.png", posHead )
                her "!!!!!!!!!!!"
                $herViewHead.hideQ()
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "on_shirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                hide screen bld1
                with d3
                pause
                show screen bld1
                with d3
                        
                #$herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm_dried' )
                $ posHead = gMakePos( 390, 300 )
                $herViewHead.showQ( "body_119.png", posHead )
                her2 "......................."
                $herViewHead.hideQ()
                m "Yes... I Feel so much better now..."
                pause
                $ g_c_u_pic = "03_hp/08_animation_02/15_cum_21.png"
                
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_03_blowjob.png", G_Z_FACE + 1 ) )
                $ pos.xpos = 130
                $herView.showQ( "body_19.png", pos, d5 )
                pause
                her ".........."
                m "Well, I think that's about it..."
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                hide screen g_c_u
                show screen genie
                $herView.hideQ( fade )                                                                                                                                                                                                         #HERMIONE
                $ pos = POS_140
                $herView.showQQ( "body_32.png", pos )
                her "Professor! What have you done?"
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                m "What?"
                $herView.hideshowQQ( "body_32.png", pos )
                her "You came all over me sir..."
                $herView.hideshowQQ( "body_118.png", pos )
                her "What a mess..."
                $herView.hideshowQQ( "body_120.png", pos )
                her2 "Professor, you should have warned me."
                m "It's your fault, girl!"
                $herView.hideshowQQ( "body_117.png", pos )
                her2 "My fault?"
                m "Yes! You got me going too well..."
                m "I forgot about everything else..."      
                $herView.hideshowQQ( "body_122.png", pos )
                her2 "Oh..."
                her2 "Well, what's done is done..."
                $herView.hideshowQQ( "body_123.png", pos )
                her "I will just wipe it off and hope that nobody will notice..."
                $herView.hideshowQQ( "body_122.png", pos )
                her2 "Can I get my payment now?"
                $herView.hideQ()
                with fade  
    
    label done_with_handjob:

#    $ gryffindor += current_payout #35 Дважды суммировалось
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
    

    m "Yes, miss Granger. [current_payout] to \"Gryffindor\"." 
    $ gryffindor +=current_payout
    $ pos = POS_140
    $herView.showQ( "body_13.png", pos )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, sir..."

    if event.Name=="new_request_02": 
        jump new_request_16_jerkonly_to_02

    $herViewHead.data().delItem( 'item_sperm' )

    if whoring <= 14:
        $ whoring +=1

    
    
#    if whoring >= 12 and whoring <= 14:
#        $ level = "05"
#        $ new_request_16_01 = True #  Hearts
#    if whoring >= 15 and whoring <= 17:
#        $ level = "06"
#        $ new_request_16_02 = True #  Hearts
    
    if IsRunNumberOrMore(3): 
        $SetHearts(3)
    else:
        $SetHearts(GetStage(whoring,12,3,2))


#    $ request_16_points += 1

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
   

        
        
### KISS SUCK! ###

label kiss_suck: #Jumps here after event #03 and if WHORING >= LEVEL 07
    ">Hermione swiftly puts the tip of your cock on her lips, as if to give it a kiss..."
    ">The simple gesture makes your dick practically explode with pleasure and waves of cum."
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause .1
    hide screen white
    with hpunch
    g4 "{size=+5}ARGH! YES!!!{/size}"
    $ genie_chibi_xpos = 60 #-185 behind the desk.
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "kiss_cum_ani"
    
    hide screen blkfade
    with d3
    show screen ctc
    hide screen bld1
    with d3
    pause
    
    
    
    show screen bld1
    with d3
                        
   
    her2 "*Gulp!-Gulp!-Gulp!*"
    $herViewHead.hideQ()
    g4 "Argh! You little whore!"
    g4 "Yes, you slut! Dink my cum! Drink all of it!"
    her2 "*Gulp!-Gulp!-Gulp!*"
    g4 "Argh... Yes!"
    ">You notice that Hermione is barely able to keep up with the amount of hot cum your cock is pumping into her mouth."
    her2 "*Gulp!-Gulp!-Gulp!*"
    g4 "Ah..."
    g4 "This feels great..."
    her2 "*Gulp!* *Gulp!* *Gulp!*"
    m "I think that's it, girl..."
    m "You can let go now..."
    pause
    show screen blkfade
    with d5
    show screen hermione_01 
    hide screen chair_02
    hide screen desk_02
    hide screen g_c_u
    show screen genie
    $herView.hideQ()
                                                                                                                                                                                                                         #HERMIONE
    $ pos = POS_140
    $herView.showQQ( "body_125.png", pos )
    show screen ctc
    pause
    her2 "........................................."
    $herView.hideshowQQ( "body_126.png", pos )
    her2 "GULP!!!"
    $herView.hideshowQQ( "body_39.png", pos )
    her2 "Gu-ah-a..."
    hide screen blkfade
    with d3
    $herView.hideshowQQ( "body_123.png", pos )
    her2 "I swallowed it all, sir!"
    m "Good girl..."
    $herView.hideshowQQ( "body_123.png", pos )
    her "At one point I thought I was going to choke..."
    her2 "There was so much of it..."
    $herViewHead.hideQ()
    m "Well, the deed is done and your form perfectly clean."
    $herView.hideshowQQ( "body_124.png", pos )
    her2 "I can just go to classes now as if nothing ever happened."
    if daytime:
        $herView.hideshowQQ( "body_122.png", pos )
        her "I'd rather just go to class, as if nothing had happened."
    else:
        $herView.hideshowQQ( "body_124.png", pos )
        her "I can just go and spend some time with the guys in the common room now and nobody will know..."
    $herViewHead.hideQ()
    m "Yes... With your belly full of semen..."
    $herView.hideQQ()
    $herView.showQQ( "body_117.png", pos )
    her2 "Professor!"
    her2 "...Can I just get paid now, please, Sir?"
    $herViewHead.hideQ()
    jump done_with_handjob #^^^ (<-That's to a smiley. That's a arrow up).
    
     
     
