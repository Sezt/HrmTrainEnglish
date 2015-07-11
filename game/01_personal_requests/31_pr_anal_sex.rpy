
###############################################################################################################################
### LEVEL 09 ##################################################################################################################
###################REQUEST_31 (Level 08) (75 pt.) (Anal sex).  #####################################################
label new_request_31: #LV.8 (Whoring = 21 - 23)
    $herView.hideQQ()
    m "{size=-4}(Should I ask her to have anal sex with me?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            $wtevent.NotFinished()
            jump new_personal_request
 
    label new_request_31_start:
    $ pos = POS_140
    $ posHead = gMakePos( 390, 340 )
    $ herView.data().saveState()
 
    if IsFirstRun(): # FIRST EVENT <============================================================== EVENT 01
#    if request_31_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Miss Granger..."
        $herView.hideshowQQ( "body_17.png", pos )
        her "Sir..?"
        m "How familiar you are with the term \"Anal Sex\"?"
        if hermi.whoring <=20:
            jump too_much
        $herView.hideshowQQ( "body_79.png", pos )
        her "90 house points..."
        m "What?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "............................."
        m "Well alright then. 90 house points it is."
        $herView.hideQ()
        
        
        label lucky_guess:
            
        show screen blkfade
        with d3
        
        stop music fadeout 1.0
        
        $herViewHead.showQ( "body_29.png", posHead )
        her "..........."
        $herViewHead.hideQ()
        m "Let's see..."
        $herViewHead.showQ( "body_34.png", posHead )
        her "................."
        $herViewHead.hideQ()
        m "hm..."
        $herViewHead.showQ( "body_18.png", posHead )
        her "!!!"
        $herViewHead.hideQ()
        g4 "Oh, come on!"
        $herViewHead.showQ( "body_20.png", posHead )
        her "Ouch!"
        $herViewHead.hideQ()
        m "Just try to loosen up a little, would you?"
        $herViewHead.showQ( "body_21.png", posHead )
        her "I'm trying!"
        $herViewHead.hideQ()
        m "Ok, what if I do this..?"
        $herViewHead.showQ( "body_20.png", posHead )
        her "Ouch! What are you doing, sir?"
        $herViewHead.hideQ()
        m "Yeah, this won't work either..."
        m "Hm..."
        m "Alright, I think I know what we should do."
        menu:
            m "..."
            "\"I think I'll spit on it and just force it in!\"":
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                $herViewHead.showQ( "body_18.png", posHead )
                her "Force it in, sir?!"
                $herViewHead.hideQ()
                $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
                g3 "*SPIT!*"
                $herViewHead.showQ( "body_32.png", posHead )
                her "Eeeeeew!"
                $herViewHead.showQ( "body_31.png", posHead )
                her2 "No, sir, wait! Maybe if I just relax--"
                $herViewHead.hideQ()
                m "No need, here I come!"
                with hpunch
                $herViewHead.showQ( "body_22.png", posHead )
                her "ARGH!"
                $herViewHead.showQ( "body_20.png", posHead )
                her "Ouch! Ouch! Ouch!"
                $herViewHead.hideQ()
                g4 "Almost in!"
                $herViewHead.showQ( "body_32.png", posHead )
                her "No, you're hurting me! You are hurting me!"
                $herViewHead.hideQ()
                g4 "Almost! Almost!"
                $herViewHead.showQ( "body_32.png", posHead )
                her "Ah! It hurts!"
                $herViewHead.hideQ()
                g4 "Shut it, girl! I'm doing you a favour!"
                g4 "Your anus is so tight it's completely un-fuckable!"
                $herViewHead.showQ( "body_20.png", posHead )
                her "Then stop, please!"
                $herViewHead.hideQ()
                m "No! We need to loosen up your asshole a little!"
                $herViewHead.showQ( "body_20.png", posHead )
                her "But I don't want you to!"
                $herViewHead.hideQ()
                m "Really? How do you expect people to fuck you up your ass then?"
                $herViewHead.showQ( "body_132.png", posHead )
                her "What people?"
                $herViewHead.hideQ()
                g4 "You know... people."
                g4 "Argh, dammit... My dick is hurting too now."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Stop then! Stop, sir!"
                her "I've changed my mind! I don't need 90 points!"
                $herViewHead.hideQ()
                g4 "I think I'm almost..."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                $herViewHead.showQ( "body_130.png", posHead )
                her2 "{size=+5}Аааааh!!!{/size}"
                $herViewHead.hideQ()
                g4 "yes!!!"
                $herViewHead.showQ( "body_130.png", posHead )
                her "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH!"
                $herViewHead.hideQ()
                g4 "Let us pump this little asshole full of semen then, shall we?"
                $herViewHead.showQ( "body_137.png", posHead )
                her "Yes... Please, I just want this to end..."
                $herViewHead.hideQ()




                $herView.hideQ()
                hide screen genie
                $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
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
                        
                        
                        
                
                
                
                
                #SCHUSH!
                
               
                g4 "Agh... You want this to end sooner?"
                g4 "Help me out then!"
                $herViewHead.showQ( "body_139.png", posHead )
                her "*sob!* How?"
                $herViewHead.hideQ()
                g4 "You know..."
                $herViewHead.showQ( "body_139.png", posHead )
                her "Оh..."
                $herViewHead.showQ( "body_140.png", posHead )
                her "I am a whore??"
                $herViewHead.hideQ()
                g9 "Yes you are!"
                $herViewHead.showQ( "body_141.png", posHead )
                her "*Sob!* I am a whore..."
                her "I love to suck cock..."
                $herViewHead.showQ( "body_142.png", posHead )
                her2 "And now my tiny asshole is getting ripped to pieces... *Sob!*"
                $herViewHead.hideQ()
                g4 "Yes! Yes!"
                g4 "Agrh! Yes!"
                $herViewHead.showQ( "body_144.png", posHead )
                her "No! Is it getting bigger?! I'm scared!"
                $herViewHead.hideQ()
                g4 "ARGH!"

                
            "\"Suck me off first. Lubricate my cock!\"":
                $herViewHead.showQ( "body_31.png", posHead )
                her "Oh... Alright..."
                $herViewHead.hideQ()
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                #SUCKING
                
                hide screen blkfade
                
                
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
                        
                
                
                
                
                
                
                
                her "*Slurp!* *Slurp!* *Slurp!*"
                $herViewHead.hideQ()
                m "Yes... good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                $herViewHead.hideQ()
                m "Alright, I think that's enough. Back on the desk now."
                show screen blkfade
                with d3

                
                #ON THE DESK
                $herViewHead.showQ( "body_31.png", posHead )
                her "............."
                $herViewHead.hideQ()
                g4 "Yes! Almost!"
                $herViewHead.showQ( "body_32.png", posHead )
                her "Ouch!"
                $herViewHead.hideQ()
                m "Relax. Almost in."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                $herViewHead.showQ( "body_130.png", posHead )
                her2 "{size=+5}AAAAAAAAhhhh!!!{/size}"
                $herViewHead.hideQ()
                g4 "yes!!!"
                $herViewHead.showQ( "body_130.png", posHead )
                her "My... my..."
                $herViewHead.showQ( "body_132.png", posHead )
                her "It hurts!"
                $herViewHead.hideQ()
                g4 "Let's pump this little asshole full of semen then, shall we?"
                $herViewHead.showQ( "body_141.png", posHead )
                her "....................."
                $herViewHead.hideQ()
                
                # SEX
                
                $herView.hideQ()
                hide screen genie
                $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
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


                $herViewHead.showQ( "body_139.png", posHead )
                her "....................."
                $herViewHead.hideQ()
                m "You alright there, slut?"
                $herViewHead.showQ( "body_140.png", posHead )
                her2 "Ah... You are... stretching me out from the inside... sir."
                $herViewHead.showQ( "body_141.png", posHead )
                her "And it still hurts..."
                $herViewHead.hideQ()
                m "Hm..."
                m "Maybe not enough lubrication...?"
                m "Come on down, girl. Suck my dick some more."
                $herViewHead.showQ( "body_140.png", posHead )
                her "What? But..."
                $herViewHead.showQ( "body_139.png", posHead )
                her "But it's dirty... It's been inside already."
                $herViewHead.hideQ()
                m "Yes, it's been inside, but that doesn't mean it's dirty now."
                m "Come one, girl. Suck my cock some more."
                $herViewHead.showQ( "body_139.png", posHead )
                her "..........."
                $herViewHead.hideQ()
                show screen blkfade
                with d3
                
                
                #SUCKING
                
                hide screen blkfade
                
                
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
                
                
                
                
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Yes... good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Can you taste your ass on my dick?"
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Alright, Maybe that's enough."
                show screen blkfade
                with d3
               

                
                #ON DESK AGAIN.
                
                
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
                
                $herViewHead.showQ( "body_139.png", posHead )
                her "Аh..."
                $herViewHead.hideQ()
                m "Better now?"
                $herViewHead.showQ( "body_140.png", posHead )
                her "It still hurts..."
                her "But I think I will be fine..."
                $herViewHead.hideQ()
                m "I'll take it slow for now..."
                $herViewHead.showQ( "body_141.png", posHead )
                her "Ah... thank you, sir."
                $herViewHead.hideQ()
                m "Oh... yes... this feels great..."
                $herViewHead.showQ( "body_139.png", posHead )
                her "..........."
                $herViewHead.hideQ()
                m "Oh... So tight..."
                $herViewHead.showQ( "body_143.png", posHead )
                her "................"
                $herViewHead.hideQ()
                m "Why are you being so quiet girl?"
                $herViewHead.showQ( "body_140.png", posHead )
                her "Because this is painful..."
                her2 "And I just want you to cum sooner, sir..."
                $herViewHead.hideQ()
                m "So you stifle your cries of pain?"
                $herViewHead.showQ( "body_142.png", posHead )
                her "yes sir. *Sob!*"
                $herViewHead.hideQ()
                m "Don't do that."
                m "Sob, scream and cry as much as you wish!"
                $herViewHead.showQ( "body_140.png", posHead )
                her "B-but--"
                $herViewHead.hideQ()
                m "That will make me cum sooner."
                $herViewHead.showQ( "body_142.png", posHead )
                her "Really? *Sob!*"
                $herViewHead.showQ( "body_139.png", posHead )
                her2 "*Sob!* It hurts! *Sob!* It hurts so much! *Sob!*"
                $herViewHead.hideQ()
                m "Yes, yes..."
                $herViewHead.showQ( "body_145.png", posHead )
                her "*SOB!*"
                $herViewHead.hideQ()
                m "You poor little kid..."
                m "A Big, evil man is raping your asshole!"
                $herViewHead.showQ( "body_146.png", posHead )
                her "*SOB!* Yeees! *SOB!*"
                $herViewHead.hideQ()
                g4 "Argh!"
                $herViewHead.showQ( "body_147.png", posHead )
                her "No, I'm scared! *SOB!*"
                $herViewHead.hideQ()
        
        menu:
            "-Fill Hermione up with cum-":
                g4 "Argh!"
                $herViewHead.showQ( "body_130.png", posHead )
                her "No! AH!"
                $herViewHead.hideQ()
                
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
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '05' )
                $herViewHead.showQ( "body_144.png", posHead )
                her "AH! IT'S FILLING ME UP!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                
                
                g4 "Yes, you whore! Yes!"
                $herViewHead.showQ( "body_145.png", posHead )
                her "It hurts, it hurts!"
                $herViewHead.hideQ()
                g4 "Shut up!"
                with hpunch
                $herViewHead.showQ( "body_149.png", posHead )
                her2 "No, I am already full! Stop cumming, you bastard!"
                $herViewHead.hideQ()
                g4 "Shut the fuck up, slut! I am not done yet!"
                $herViewHead.showQ( "body_146.png", posHead )
                her "No! Please! My stomach! I will explode!"
                $herViewHead.hideQ()
                g4 "ARGH!"
                $herViewHead.showQ( "body_144.png", posHead )
                her "No, I think I will throw up..."
                $herViewHead.hideQ()
                with hpunch
                $herViewHead.showQ( "body_150.png", posHead )
                play sound "sounds/burp.mp3"
                her "{size=+7}*ХЛЮП!*!!!!!{/size}"
                $herViewHead.showQ( "body_151.png", posHead )
                her "......................."
                her "............."
                $herViewHead.showQ( "body_126.png", posHead )
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                her "{size=+7}*BURP!*!!!!!{/size}"
                $herViewHead.showQ( "body_145.png", posHead )
                her "*SOB!* I HATE YOU..."
                $herViewHead.showQ( "body_148.png", posHead )
                her2 "{size=+5}I HATE YOU AND YOUR NASTY OLD COCK?{/size}"
                her "{size=+5}I HATE YOU! YOU HEAR ME?!{/size}"
                $herViewHead.hideQ()
                g4 "Agh...Shut it, whore!"
                $herViewHead.showQ( "body_145.png", posHead )
                her "*sob!* *Sob!*..."
                $herViewHead.hideQ()
                
                
                
                
                
                
                
                # AFTER CUM INSIDE
                
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "03_hp/08_animation_02/23_cum_19.png"
                $herViewHead.showQ( "body_142.png", posHead )
                her "*Sob!*..."
                $herViewHead.hideQ()
                m "Whew!... I think that was the last of it."
                m "You alright?"
                $herViewHead.showQ( "body_142.png", posHead )
                her "Yes... *Sob!*"
                $herViewHead.hideQ()
                m "Are You crying?"
                $herViewHead.showQ( "body_142.png", posHead )
                her "My butt hurts, but I am alright, sir..."
                $herViewHead.hideQ()
                m "Well, you took my dick stoically, I must say..."
                $herViewHead.showQ( "body_142.png", posHead )
                her "Thank you sir..."
                $herViewHead.hideQ()

                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                $herViewHead.showQ( "body_152.png", posHead )
                her "I apologize for saying that I hate you, sir..."
                her "And your cock is not nasty..."
                $herViewHead.showQ( "body_153.png", posHead )
                her "I don't know what's gotten into me..."
                $herViewHead.hideQ()
                g9 "My dick!"
                $herViewHead.showQ( "body_153.png", posHead )
                her2 "I suppose it's as when you call me a \"whore\". I know you actually don't mean it..."
                $herViewHead.hideQ()
                m "Yeah, sure..."
                m "Does it still hurt?"
                $herViewHead.showQ( "body_154.png", posHead )
                her "A little..."
                $herViewHead.showQ( "body_155.png", posHead )
                her "I also feel full and warm inside..."
                $herViewHead.hideQ()
                m "You plan to keep it in? My cum I mean."
                $herViewHead.showQ( "body_156.png", posHead )
                her "Yes..."
                if daytime:
                    her2 "I hope it won't start leaking during my classes..."
                else:
                    her2 "I hope it won't start leaking before I get to my room..."
                $herViewHead.hideQ()
                m "Well, good luck on your journey."
                $herViewHead.showQ( "body_155.png", posHead )
                her "Can I get paid now please?"
                $herViewHead.hideQ()
                
                    
                
                
                
                
            "-Pull out and cum on Hermione-":
                
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
                #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '05' )
                $herViewHead.showQ( "body_133.png", posHead )
                her2 "Ааh...{image=textheart.png}{image=textheart.png}{image=textheart.png}"

                $herViewHead.hideQ()
                g4 "Yes!!! Allover your ass!"
                $herViewHead.showQ( "body_134.png", posHead )
                her "Ah... It's so hot!"
                $herViewHead.hideQ()

                
                $herViewHead.hideQ()
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3


                
                
                show screen blkfade
                with d7
                
                m "Well, I'm done... You can get off my desk now."
                $herViewHead.showQ( "body_138.png", posHead )
                her "Yes, sir..."
                $herViewHead.hideQ()
                m "You feeling alright?"
                $herViewHead.showQ( "body_139.png", posHead )
                her "Yes, sir. It still hurts a little, but..."
                $herViewHead.hideQ()
                m "But what?"
                $herViewHead.showQ( "body_138.png", posHead )
                her "But in a good way... sir."
                $herViewHead.hideQ()
                m "In a good way, huh?"
                g9 "Heh... You cute, little mynx."
                $herViewHead.showQ( "body_138.png", posHead )
                her "Can I get paid now, sir?"
                $herViewHead.hideQ()

        
    elif IsRunNumber(2): # FIRST EVENT <============================================================== EVENT 02
#    elif request_31_points == 1: # FIRST EVENT <============================================================== EVENT 02
        m "Girl?"
        $herView.hideshowQQ( "body_15.png", pos )
        her "Professor?"
        m "I will be buying another favour from you today..."
        $herView.hideshowQQ( "body_08.png", pos )
        her "............."
        m "Care to guess what the favour will be?"
        m "You have three attempts to find out."
        $herView.hideshowQQ( "body_09.png", pos )
        her "..........."
        $herView.hideshowQQ( "body_66.png", pos )
        her "Anal sex?"
        g4 "Wha..........?!"
        g4 "How did you...?"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Just a lucky guess, sir..."
        m "Sometimes you scare me, girl..."
        $herView.hideQQ()
        jump lucky_guess
        
        
        
        
        
    elif IsRunNumberOrMore(3): # FIRST EVENT <============================================================== EVENT 03
#    elif request_31_points >= 2: # FIRST EVENT <============================================================== EVENT 03
        m "How about another assfuck, girl?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "How about another 90 house points, sir?"
        g9 "Come here, you little mynx!"
        $herView.hideQQ()
        # SEX
        show screen blkfade
        with d3
        
        stop music fadeout 1.0
        
        $herViewHead.showQ( "body_29.png", posHead )
        her "........"
        $herViewHead.hideQ()
        m "hm..."
        $herViewHead.showQ( "body_31.png", posHead )
        her "..........."
        $herViewHead.hideQ()
        
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        $herViewHead.showQ( "body_130.png", posHead )
        her2 "Ооооооооh....{image=textheart.png}"
        $herViewHead.hideQ()
        g4 "Oh, ye-es!"
        $herViewHead.showQ( "body_121.png", posHead )
        her "Ah..."
        $herViewHead.hideQ()
        m "It seems like your butthole became a bit more welcoming, girl."
        $herViewHead.showQ( "body_128.png", posHead )
        her "Ah... It still hurts a little."
        $herViewHead.showQ( "body_129.png", posHead )
        her "And please, just call me \"whore\", sir."
        $herViewHead.hideQ()
        g4 "Agh! You slut! You always get me with your words!"



        
        
        
        
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
        
        # INSERTION
        $herViewHead.showQ( "body_127.png", posHead )
        her "Аh... Аh..."
        her "Аh..."
        $herViewHead.showQ( "body_128.png", posHead )
        her "Sir?"
        $herViewHead.hideQ()
        m "Yes, whore?"
        $herViewHead.showQ( "body_117.png", posHead )
        her "Em..."
        $herViewHead.hideQ()
        hide screen ctc
        $herViewHead.showQ( "body_118.png", posHead )
        her "Would you marry me, sir?"
        $herViewHead.hideQ()
        with hpunch
        g4 "{size=+9} WHAT?!{/size}"
        g4 "Don't tell me you're pregnant, girl!"
        $herViewHead.showQ( "body_122.png", posHead )
        her2 "I Couldn't get pregnant the way we are doing it, sir..."
        $herViewHead.hideQ()
        m "What is this talk of marriage then?"
        $herViewHead.showQ( "body_117.png", posHead )
        her "You misunderstood me sir."
        $herViewHead.showQ( "body_118.png", posHead )
        her "I meant to say, would you marry a girl {size=+5}like{/size} me?"
        $herViewHead.showQ( "body_34.png", posHead )
        her2 "I would never propose to a man with his cock in my ass, sir..."
        $herViewHead.hideQ()
        m "Good. Because I don't think any man would be able to say \"no\" to then."
        $herViewHead.showQ( "body_127.png", posHead )
        her "Аh{image=textheart.png}..."
        $herViewHead.showQ( "body_118.png", posHead )
        her2 "What I meant... ah{image=textheart.png} {w} ...to say was ah{image=textheart.png}... {w}...do you think someone would ever ah{image=textheart.png}... {w} ...want to marry a girl like me?"
        $herViewHead.hideQ()
        m "hm?"
        $herViewHead.showQ( "body_118.png", posHead )
        her2 "I mean, with all that was happening lately... ah{image=textheart.png}..."
        her "I can't help but feel unclean... damaged even."
        her "And in a no way innocent..."
        $herViewHead.showQ( "body_117.png", posHead )
        her "Who would want a wife like that?"
        $herViewHead.hideQ()
        menu:
            m "..."
            "\"I would marry you in a heartbeat!\"":
                $herViewHead.showQ( "body_31.png", posHead )
                her "What?"
                $herViewHead.hideQ()
                m "Well, hypothetically speaking of course..."
                $herViewHead.showQ( "body_54.png", posHead )
                her "...of course...{image=textheart.png}"
                $herViewHead.showQ( "body_53.png", posHead )
                her ".............."
                $herViewHead.showQ( "body_55.png", posHead )
                her "But why do you say that, sir?"
                $herViewHead.hideQ()
                m "Huh?"
                m "What do you mean \"why\", whore?"
                m "You are young and attractive..."
                m "Tight asshole, full tits and wet little pussy..."
                $herViewHead.showQ( "body_127.png", posHead )
                her "Аh...{image=textheart.png}"
                $herViewHead.hideQ()
                m "You will make some lucky guy a very happy man one day, whore."
                m "Ehm, I mean, miss Granger."
                $herViewHead.showQ( "body_134.png", posHead )
                her2 "No, \"whore\" is good. Call me that, sir."
                $herViewHead.hideQ()
                m "There, you see? You are a great catch, I'm telling you, whore."
                $herViewHead.showQ( "body_134.png", posHead )
                her "Ah...{image=textheart.png} Thank you, sir."
                $herViewHead.hideQ()
                m "Huh?"
                m "Are you crying?"
                label among_other_things:
                $herViewHead.showQ( "body_133.png", posHead )
                her "Among other things, sir...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                m "Among other things?"
                $herViewHead.showQ( "body_135.png", posHead )
                her "I'm cumming sir...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                g4 "Agh! My cock!" 
                g4 "Relax your muscles a little, would you?"
                $herViewHead.showQ( "body_131.png", posHead )
                her "BUT I'M CUMMING!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                g4 "Fine! Have it your way whore!"
                with hpunch
                $herViewHead.showQ( "body_130.png", posHead )
                her "{size=+7}Ah-ah-aha!!! I'm cumming!!!{/size}"
                $herViewHead.hideQ()
                g4 "{size=+7}Argh!{/size}"
                
            "\"Marriage is out of the picture for you.\"":
                $herViewHead.showQ( "body_143.png", posHead )
                her "That's what I thought..."
                $herViewHead.hideQ()
                m "Oh... I just love that little asshole of yours!"
                $herViewHead.showQ( "body_142.png", posHead )
                her "....................."
                her2 "Yes... After all the things I had to do for my house..."
                $herViewHead.showQ( "body_145.png", posHead )
                her "...no one will ever want me..."
                $herViewHead.hideQ()
                m "Oh, they will want you alright!"
                $herViewHead.showQ( "body_144.png", posHead )
                her "What? But you said..."
                $herViewHead.hideQ()
                m "Marriage, girl. Marriage is impossible for you."
                m "But as a man-pleaser you are a great catch!"
                $herViewHead.showQ( "body_144.png", posHead )
                her "Really?"
                $herViewHead.hideQ()
                m "Are you kidding me?!"
                m "Young, hot and slutty. You could have any man you want!"
                m "Or a wizard or whatever you are into..."
                $herViewHead.showQ( "body_157.png", posHead )
                her "I think you may be right, sir."
                $herViewHead.hideQ()
                m "I know I am right, whore."
                m "Now wiggle that little ass of yours a little."
                $herViewHead.showQ( "body_138.png", posHead )
                her "Like this?"
                $herViewHead.hideQ()
                m  "Yes, that's a good whore."
                $herViewHead.showQ( "body_133.png", posHead )
                her "I am a whore, aren't I?"
                $herViewHead.hideQ()
                m "You just sold me your asshole for 90 house points. How would you call that?"
                $herViewHead.showQ( "body_138.png", posHead )
                her "Yes, yes...{image=textheart.png} I am a whore...{image=textheart.png}"
                $herViewHead.hideQ()
                m "Are you crying?"
                jump among_other_things
                
        menu:
            g4 "!!!"
            "-Fill Hermione up with cum-":
                $herViewHead.showQ( "body_130.png", posHead )
                her "!!!"
                $herViewHead.hideQ()
                m "Yes! Argh!"
                $herViewHead.showQ( "body_134.png", posHead )
                her "Ah!{image=textheart.png} It's filling me up!{image=textheart.png} I can feel it!{image=textheart.png}"
                $herViewHead.hideQ()
                m "Shut up, whore!"
                $herViewHead.showQ( "body_137.png", posHead )
                her "Ah! I AM A WHORE!!!!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                m "Agh!"
                $herViewHead.showQ( "body_144.png", posHead )
                her "Ah...{image=textheart.png} your cum, sir...{image=textheart.png}"
                $herViewHead.hideQ()
                m "Yes, yes..."
                $herViewHead.showQ( "body_145.png", posHead )
                her "Аааh...{image=textheart.png}"
                $herViewHead.hideQ()
                m "......"
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3


                
                
                show screen blkfade
                with d7
            "-Cum allover Hermione-":
                
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
                #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '05' )
                $herViewHead.showQ( "body_133.png", posHead )
                her "Ah-aha! You're cumming! {image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                g4 "{size=+7}Yes I do, whore!{/size}"
                $herViewHead.showQ( "body_147.png", posHead )
                her "Ah, me too! Me too!"
                $herViewHead.hideQ()
                g4 "{size=+7}FUCKING SLUT!{/size}"
                $herViewHead.showQ( "body_142.png", posHead )
                her "Ah...{image=textheart.png} your cum...{image=textheart.png}"
                her "I'm so full...{image=textheart.png}{image=textheart.png}{image=textheart.png}"


                $herViewHead.hideQ()
                g4 "Yes!!! All over your ass!"
                $herViewHead.showQ( "body_134.png", posHead )
                her "Ah... It's so hot!"
                $herViewHead.hideQ()

                
                $herViewHead.hideQ()
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3


                
                
                show screen blkfade
                with d7

                
                
                
                
                
                
                
                
                
                
                
               
              
        #Ending
        m "Well, this was intense..."
        $herViewHead.showQ( "body_158.png", posHead )
        her "Ah-ha...{image=textheart.png} ah...{image=textheart.png}"
        $herViewHead.hideQ()
        m "Are You alright, girl?"
        $herViewHead.showQ( "body_158.png", posHead )
        her "I think so... I'm not sure..."
        $herViewHead.showQ( "body_158.png", posHead )
        her "I think I may still be cumming, sir."
        $herViewHead.showQ( "body_158.png", posHead )
        her "Or maybe not..."
        her "Everything is in a daze... and my legs feel so weak..."
        her "Can I just get paid now, sir?"
        $herViewHead.hideQ()

        
    
    stop music fadeout 1.0
    
    if herViewHead.data().getItem( 'item_sperm' ) != None:
        $herViewHead.data().addItem( 'item_sperm_dried' )
        #$herViewHead.data().addItemKey( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
    $herViewHead.data().delItem( 'item_sperm' )
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
 
    if wtevent.Name=="new_request_08": 
        jump new_request_08_finish
    m "Yes, miss Granger. 90 points to \"Gryffindor\"." 
    $ gryffindor +=90
    $herView.showQ( "body_141.png", pos )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, sir..."

    if hermi.whoring <= 23: # Level 08 <
        $ hermi.whoring +=1

#    if request_31_points == 0:
#        $ new_request_31_01 = True # HEARTS.
#    if request_31_points == 1:
#        $ new_request_31_02 = True # HEARTS.
#    if request_31_points >= 2:
#        $ new_request_31_03 = True # HEARTS.


#    $ request_31_points += 1


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
    
    $wtevent.Finalize()    
    $SetHearts(GetStage(wtevent._finishCount,1,3,1))
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
   

    



