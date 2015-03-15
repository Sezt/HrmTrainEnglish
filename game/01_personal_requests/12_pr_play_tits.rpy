
###################REQUEST_12 (Level 04) (Play with her tits.) (Day/Night) ############################################################################
label new_request_12: #LV.4 (Whoring = 9 - 11)
    $herView.hideQQ()
    if IsFirstRun():
#    if request_12_points == 0:
        m "{size=-4}(I feel like playing with those titties.){/size}"
    else:
        m "{size=-4}(I feel like playing with those titties again.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request
    
    if whoring <=8:
        jump too_much

    $ pos = POS_140
    $ herView.data().saveState()
        
    if IsFirstRun() and whoring <= 14: # LEVEL 05 (one level higher then level at which it unlocks - 04) # FIRST TIME.
#    if request_12_points == 0 and whoring <= 14: # LEVEL 05 (one level higher then level at which it unlocks - 04) # FIRST TIME.
        m "Miss Granger."
        $herView.hideshowQQ( "body_01.png", pos )
        her "Yes, sir?"
        m "How about selling me another favour today?"
        $herView.hideshowQQ( "body_02.png", pos )
        her "Uhm... Alright..."
        her "What will it be, sir?"
        m "Well, how about you come closer and bare your tits for me...?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "!!!"
        m "I want to give them a good squeeze."
        $herView.hideshowQQ( "body_66.png", pos )
        her "Professor Dumbledore! Don't you think this is too much?"
        m "You think?"
        her "I am not one of those harlots from \"Slytherin\", you know..."
        m "I know... You from \"Griffondor\" or whatever......" #<- GRYFFINDOR MISSPELLED ON PERPOUSE   I KNOW
        $herView.hideshowQQ( "body_29.png", pos )
        her "And if I don't feel like it I don't have to sell you a single favour, sir!"
        m "Of course..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "..................."
        m "I'll give you 35 house points for this."
        $herView.hideshowQQ( "body_66.png", pos )
        her "......................."
        her "All you are going to do is watch, sir?"
        m "Well, I feel more like touching, actually..."
        her "...................................."


    else: # Intro. Not first time.
        if whoring >= 9 and whoring <= 14: # LEVEL 04 AND LEVEL 05 # NOT A WHORE YET.
            m "Miss granger..."
            $herView.hideshowQQ( "body_01.png", pos )
            her "Sir?"
            m "I feel like playing with your tits a little..."
            $herView.hideshowQQ( "body_79.png", pos )
            her "Sir... I'd prefer it if you wouldn't make me such offers..."
            m "Why? Too hard to resist?"
            her "Nothing like that, sir."
            m "I'll give you 35 house points for this..."
            $herView.hideshowQQ( "body_69.png", pos )
            her ".................."
            her "Well, alright... You can touch them a little..."
        elif whoring >= 15: # LEVEL 06 and higher # NASTY WHORE.
            m "Miss granger..."
            
            $herView.hideshowQQ( "body_01.png", pos )
            her "Sir?"
            m "I feel like playing with your tits a little..."
            $herView.hideshowQQ( "body_78.png", pos )
            her "Of course sir..."
    

    label new_request_12_mainonly:
    $herView.hideQQ()
    hide screen blktone
    with d3
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


    hide screen hermione_walk_01
    hide screen genie
    show screen ctc
    #show screen chair_02 #Genie's chair.
    hide screen genie
    show screen genie_and_tits_01
    with d1
    hide screen blkfade
    with d5
    stop music fadeout 1.0
    pause
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    show screen blktone 
    with d3
    $herView.hideQQ()
    #$ only_upper = True #No lower body displayed. 
    $herView.data().addPose( CharacterExItemPoseShowTits( herView.mPoseFolder, 'pose_dress_up.png', G_Z_POSE ) )
    $herView.showQQ( "body_82.png", pos )
    pause
    her "...................................."
    
    
    
    $ posHead = gMakePos( 390, 340 )
    
    menu:
        m "..."
        "-Grab them-":
            label no_smacking_tits:
                pass
            $herView.hideQQ()
            $herView.data().delPose()
            show screen blkfade
            with d5
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen groping_naked_tits
            with d1
            hide screen blkfade
            hide screen blktone
            with d5
            pause
            show screen bld1
            with d3
            

            
            if whoring >= 9 and whoring <= 14: # LEVEL 04 AND LEVEL 05 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).

                $herViewHead.showQ( "body_118.png", posHead )
                her ".............................."
                $herViewHead.hideQ()
                m "You have great tits, girl..."
                $herViewHead.showQ( "body_118.png", posHead )
                her "...................................."
                $herViewHead.hideQ()
                m "You like it when I squeeze them like this?"
                $herViewHead.showQ( "body_120.png", posHead )
                her2 "Excuse me, sir, but you are confusing me with one of those lowly harlots again..."
                her2 "I am only letting you fondle me because I am getting paid for it..."
                her "Not because I enjoy it..."
                $herViewHead.hideQ()
                m "I see..."
                m "So, you're more like a prostitute then..."
                $herViewHead.showQ( "body_119.png", posHead )
                her "Professor Dumbledore!"
                her "Prostitutes are getting paid to have sex with men..."
                $herViewHead.showQ( "body_120.png", posHead )
                her "I'd never do something like that!"
                $herViewHead.hideQ()
                show screen blktone
                with d3
                ">You squeeze one of the girl's tits tightly and give the other a couple of firm tugs."
                hide screen blktone
                with d3
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ah..."
                $herViewHead.hideQ()
                m "Enjoying yourself, miss granger?"
                if whoring >= 9 and whoring <= 11: # LEVEL 04 #  <=================================================================================== FIRST EVENT.
                    $herViewHead.showQ( "body_120.png", posHead )
                    her "Sir, I am only doing this--"
                    $herViewHead.hideQ()
                    show screen blktone
                    with d3
                    ">You squeeze both of her tits with force..."
                    hide screen blktone
                    with d3
                    $herViewHead.showQ( "body_132.png", posHead )
                    her "ah..."
                    $herViewHead.hideQ()
                    m "Tell me you like this, girl!"
                    $herViewHead.showQ( "body_131.png", posHead )
                    her "Sir, I am only letting you do this to me because--"
                    $herViewHead.hideQ()
                    m "I know, know..."
                    m "You are starting to sound like a broken record."
                    $herViewHead.showQ( "body_79.png", posHead )
                    her "...."
                    $herViewHead.hideQ()
                    show screen blktone
                    with d3
                    show screen blkfade
                    with d7

                    show screen genie
                    hide screen groping_naked_tits
                    hide screen ctc

            
                    ">You let go of the girl's breasts..."
                else:  # LEVEL 05 # <=================================================================================== SECOND EVENT.
                    $herViewHead.showQ( "body_87.png", posHead )
                    her "Ah..."
                    $herViewHead.hideQ()
                    show screen blktone
                    with d3
                    ">You squeeze her tits a few more times, then give them a firm tug..."
                    hide screen blktone
                    with d3
                    $herViewHead.showQ( "body_31.png", posHead )
                    her "Ah... Sir..."
                    $herViewHead.hideQ()
                    m "What? You do enjoy this, don't you?"
                    $herViewHead.showQ( "body_31.png", posHead )
                    her "No... I..."
                    $herViewHead.hideQ()
                    m "Don't you lie to your headmaster, girl!"
                    show screen blktone
                    with d3
                    ">You squeeze her tits again..."
                    hide screen blktone 
                    with d3
                    $herViewHead.showQ( "body_87.png", posHead )
                    her "Ah..."
                    her "I am not lying, sir..."
                    $herViewHead.showQ( "body_31.png", posHead )
                    her "Why would I enjoy this?"
                    $herViewHead.hideQ()
                    m "I don't know girl. You tell me."
                    show screen blktone
                    with d3
                    ">You keep massaging her breasts..."
                    hide screen blktone
                    with d3
                    $herViewHead.showQ( "body_31.png", posHead )
                    her "Ah... I..."
                    $herViewHead.hideQ()
                    m "Yes, what is it?"
                    $herViewHead.showQ( "body_117.png", posHead )
                    her "It's... It's nothing, sir..."
                    $herViewHead.hideQ()
                    m "Oh, I think it's something."
                    m "I think you like me squeezing your tits like this."  
                    $herViewHead.showQ( "body_118.png", posHead )
                    her "Sir, please..."
                    if daytime:
                        her "The classes are about to start..."
                    else: 
                        her "It's getting late..."
                    $herViewHead.showQ( "body_117.png", posHead )
                    her "Can I go now, sir? Please?"
                    $herViewHead.hideQ()
                    show screen blkfade 
                    with d3
                    m "Sure, go ahead..."
                    $herViewHead.showQ( "body_118.png", posHead )
                    her "..............."
                    $herViewHead.showQ( "body_117.png", posHead )
                    her "Sir, your are still... Holding me..."
                    $herViewHead.hideQ()
                    m "Oh, right... my bad...."
                    ">You let go of Hermione's breasts..."
                    
                    show screen genie
                    hide screen groping_naked_tits
                    hide screen ctc

            elif whoring >= 15: # LEVEL 06 and higher # <=================================================================================== THIRD EVENT. 
               
                $herViewHead.showQ( "body_121.png", posHead )
                her "Ah..."
                $herViewHead.hideQ()
                m "A bit sensitive today, aren't you?"
                $herViewHead.showQ( "body_128.png", posHead )
                her "I suppose..."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ah..."
                $herViewHead.hideQ()
                m "You like it when I squeeze them like this?"
                $herViewHead.showQ( "body_128.png", posHead )
                her "I do, sir... Ah..."
                $herViewHead.hideQ()
                m "Heh..."
                m "What if I pinch your nipples?"
                show screen blktone
                with d5
                $herViewHead.showQ( "body_117.png", posHead )
                her "!!!"
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ah! Sir..."
                $herViewHead.hideQ()
                m "And what if I do this?"
                show screen blktone8
                with d3
                ">You grab the girl by her hard nipples and start pulling..."
                hide screen blktone8
                with d3
                $herViewHead.showQ( "body_132.png", posHead )
                her "Ah... Ah... Ah... Sir..."
                $herViewHead.hideQ()
                m "What if I pull even harder?"
                $herViewHead.showQ( "body_130.png", posHead )
                her "Ah... Sir, please..."
                $herViewHead.hideQ()
                show screen blktone8
                with d3
                ">Hermione clutches the edge of your desk to keep herself form taking a step towards you..."
                hide screen blktone8
                with d3
                m "Good girl..."
                $herViewHead.showQ( "body_123.png", posHead )
                her "*Panting heavily*"
                $herViewHead.hideQ()
                m "Do you enjoy this?"
                $herViewHead.showQ( "body_139.png", posHead )
                her "You are hurting me, sir..."
                $herViewHead.hideQ()
                m "But do you enjoy it?"
                $herViewHead.showQ( "body_140.png", posHead )
                her "Ah... Yes, sir... I don't know why, but I do..."
                $herViewHead.hideQ()
                m "Good girl..."
                show screen blktone8
                with d3
                ">You let go of her nipples..."
                hide screen blktone8
                with d3
                $herViewHead.showQ( "body_138.png", posHead )
                her "Ah..."
                $herViewHead.hideQ()
                show screen blkfade
                with d5
                m "This will be all for today, miss Granger..."
                $herViewHead.showQ( "body_139.png", posHead )
                her "Ооо...?"
                $herViewHead.hideQ()
                m "What is it? You look disappointed."
                m "I will pay you of course..."
                $herViewHead.showQ( "body_141.png", posHead )
                her "That's not it, sir..."
                her "It's..."
                $herViewHead.showQ( "body_139.png", posHead )
                if daytime:
                    her2 "It's just that I still have some time left before I have to leave for the classes and..."
                else:
                    her "It's not really that late yet, is it?"
                her "uhm..."
                her "..................."
                $herViewHead.hideQ()
                m "You want me to hurt you some more, don't you?"
                $herViewHead.showQ( "body_139.png", posHead )
                her "I don't \"want to\"... "
                $herViewHead.showQ( "body_138.png", posHead )
                her "But if you insist sir..."
                $herViewHead.hideQ()
                m "Well, I do insist... apparently."
                $herViewHead.showQ( "body_138.png", posHead )
                her "Ah..."
                $herViewHead.hideQ()
                hide screen blkfade
                with d5
                
                show screen ctc
                pause
                hide screen ctc
                
                #BLACK FADE
                show screen blkfade
                with d7
                ">You spend some more time with Hermione's breasts..."
                
                show screen genie
                hide screen groping_naked_tits
                hide screen ctc

        "-Slap them-":
            $herView.hideQ()
            with d5
            ">You give Hermione's tits a loud slap!"
            $ renpy.play('sounds/slap.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            if whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).
                $herView.hideQQ()
                $herView.showQ( "182.png", pos )
                her "!!!"
                $herView.hideQQ()
                $herView.showQ( "183.png", pos )
                her "Ouch! It hurts! *SOB!*"
                m "Did you like it though?"
                $herView.hideQQ()
                $herView.showQ( "body_81.png", pos )
                her "Did I... \"like it\, sir..?"
                her "What girl in her right mind would like to be treated this way?"
                $herView.hideQQ()
                $herView.showQQ( "184.png", pos )
                stop music fadeout 1.0
                her "You are a mean and demented old man!"
                $herView.hideQQ()
                show screen blkfade
                with d3
                # RUNS OFF
                $ mad += 20
                m "............"
                m "Well, no points for \"Gryffindor\" then..."
                
                show screen genie
                hide screen groping_naked_tits
                hide screen ctc
                hide screen genie_and_tits_01
                call music_block

                # restore state before leaving
                $herView.data().loadState()
                jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                
                    
            elif whoring >= 12 and whoring <= 14: # LEVEL 05 # <=================================================================================== SECOND EVENT.
                $herView.hideQQ()
                $herView.showQ( "182.png", pos )
                her "!!!"
                $herView.hideQQ()
                $herView.showQ( "183.png", pos )
                her "Ouch!"
                her "Sir, what did you do this for?"
                m "Dunno... Seemed like a good idea..."
                m "Did you like it?"
                $herView.hideQQ()
                $herView.showQ( "body_83.png", pos )
                her "...Of course, not, sir."
                m "Let's try this again, then."
                $herView.hideQQ()
                $herView.showQ( "body_82.png", pos )
                her "What?"
                $herView.hideQQ()
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.08
                hide screen white
                $herView.hideQQ()
                $herView.showQ( "182.png", pos )
                her "!!!"
                her "Ouch! Stop hurting me!"
                m "Admit that you enjoy it and I will."
                $herView.hideQQ()
                $herView.showQ( "body_85.png", pos )
                her "But I don't..."
                her "And if you plan to keep on doing this to me, sir..."
                $herView.hideQQ()
                $herView.showQ( "body_81.png", pos )
                her "...then I think I should leave."
                m "Fine, fine..."
                $herView.hideQQ()
                jump no_smacking_tits #Jumps to usual tits molesting scene.

            elif whoring >= 15: # LEVEL 06 and higher # <=================================================================================== THIRD EVENT. 
                $herView.hideQQ()
                $herView.showQ( "182.png", pos )
                her "Ах!!!"
                $herView.hideQQ()
                $herView.showQ( "185.png", pos )
                her "Sir, why did you do that?"
                m "Dunno... Seemed like a good idea..."
                m "Did you like it?"
                $herView.hideQQ()
                $herView.showQ( "body_82.png", pos )
                her ".........."
                her "I am not a pervert..."
                $herView.hideQQ()
                show screen blktone8
                with d3
                ">You give Hermione's tits another loud smack!"
                hide screen blktone8
                with d3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.08
                hide screen white
                $herView.hideQQ()
                $herView.showQ( "186.png", pos )
                her "A-ah!!!"
                m "Tell me you like it!"
                her "Sir... I..."
                $herView.hideQQ()
                show screen blktone8
                with d5
                ">You unleash a whole series of slaps!"
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                ">Hermione's tits bounce allover the place, completely out of control"
                hide screen blktone8
                with d5
                $herView.hideQQ()
                $herView.showQ( "187.png", pos )
                her "A-ah!!! Ah!!! A-a-aha!!!"
                m "You enjoy this. Admit it."
                $herView.hideQQ()
                $herView.showQ( "188.png", pos )
                her "..........."
                $herView.hideQ()
                hide screen ctc
                with d3
                ">You smack her tits again."
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $herView.hideQQ()
                $herView.showQQ( "187.png", pos )
                her "A-ah! Yes! I do, I do! A-ah..."
                $herView.hideQQ()
                $herView.showQQ( "184.png", pos )
                her "...does this mean I'm a pervert, sir?"
                m "What?"
                m "Stop being silly, girl."
                m "It is completely natural for a girl to enjoy her tits getting smacked around a little."
                her "......"
                her "Are you sure about that, sir?"
                m "Yes. Believe me, I know."
                $herView.hideQQ()
                ">You give her tits one more slap!"
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $herView.hideQQ()
                $herView.showQQ( "187.png", pos )
                her "A-ah... Yes... Thank you, sir."
                $herView.hideQQ()
                m "Well... Enough with the slapping for now..."
                jump no_smacking_tits #Jumps to usual tits molesting scene.

    
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
    
    stop music fadeout 1.0
    m "Yes, miss Granger. 35 points to \"Gryffindor\"."  
    $ gryffindor +=35
    $herView.showQ( "body_13.png", pos )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, sir..."

    if whoring <= 11: # If still of level of unlocking - 04
        $ whoring +=1

#    $ request_12_points += 1
    $SetHearts(GetStage(whoring,9,3,3))


#    if whoring >= 9 and whoring <= 11:
#        $ level = "04"
#        $ new_request_12_01 = True # HEARTS.
#    if whoring >= 12 and whoring <= 14:
#        $ level = "05"
#        $ new_request_12_02 = True # HEARTS.
#    if whoring >= 15:
#        $ level = "06"
#        $ new_request_12_03 = True # HEARTS.


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

    $ herView.data().loadState()
    call music_block
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
   
    




