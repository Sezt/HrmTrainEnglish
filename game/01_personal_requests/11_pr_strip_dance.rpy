    
##################################################################################################################################
### LEVEL 04 #####################################################################################################################
###################REQUEST_11 (Level 04) (DANCE FOR ME AND SNAPE) (Day/Night) ################################################################
label new_request_11: #LV.4 (Whoring = 9 - 11)
    $herView.hideQQ()
   
    m "{size=-4}(Ask her to dance for me?){/size}"

    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request

    $ current_payout = 35 #Because will have option to pay extra.

    $ herView.data().saveState()
    #$ herView.data().addItemKey( 'sweat', CharacterExItemSweat( herView.mMiscFolder, "sweat.png", G_Z_POSE - 1 ) )
    $ herView.data().addItem( 'item_misc_sweat_97to99' )

    if IsFirstRun(): 
#    if request_11_points == 0: #<==============================EVENT 01
        
        m "Miss Granger, I need you to dance for me a little."
        $herView.hideQQ()
        $ pos = POS_140
        $herView.showQQ( "body_11.png", pos )
        her "You want me to..."
        $herView.hideshowQQ( "body_10.png", pos )
        her "...dance for you, sir?"
        if hermi.whoring <= 8:
            jump too_much
#        $ new_request_11_01 = True # HEARTS
        m "Yes... You think you could manage that?"
        her "Ehm... I suppose so..."
        $herView.hideshowQQ( "body_11.png", pos )
        her "Is this your official wish, sir?"
        with hpunch
        g4 "What did you just say!?"
        stop music fadeout 1.0
        $herView.hideshowQQ( "body_12.png", pos )
        her "I mean, favour. Is this an official favour sir?"
        show screen whitetone8
        hide screen blktone
        with Dissolve(1)
        $herView.hideQ( Dissolve( 1 ) )
        g4 "(\"Is this your official wish, master....?\")"
        m "(Man, this sure brings back memories...)"
        m "(Agrabah and genie the joker...)"
        m "(A pre-akabur era of my life...)"
        m "(Simpler times...)"
        g4 "(The bastard ruined my life!)"
        her "Em... Professor?"
        hide screen whitetone8
        with Dissolve(1)
        $herView.showQQ( None, pos )
        call music_block
        her "Sir..?"
        m "Hermione, right..."
        m "Got lost in my thoughts for a moment there..."
        her "So am I getting paid for this?"
        m "Of course, girl!"
        $herView.hideshowQQ( "body_29.png", pos )
        her "So... Just a little dancing then..."
        m "Whenever you're ready..."
        her "................."
        $herView.hideQQ()
        ">Hermione starts dancing..."
        stop music fadeout 1.0
        hide screen blktone
        $ hermione_chibi_xpos = 400 #Near the desk.
        #$ hermione_chibi_ypos = 240 #Default: 250
        show screen clothed_dance #Hermione stands still.
        with fade
        m "Хм..."
        $her_head_state = 12
        her_head_main "{size=-5}(...........................................){/size}"
        $her_head_state = 4
        her_head_main "{size=-5}(This is silly...){/size}"
        ">Hermione looks embarrassed but she keeps on \"dancing\"..."
        m "..................."
        her_head_main "{size=-5}(...........................................){/size}"
        m "Alright, you can start undressing now."
        show screen hermione_02 #Hermione stands still.
        with hpunch
        $her_head_state = 7
        her_head_main "??!"
        $her_head_state = 8
        her_head_main "I thought all I had to do was dance?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "Really? That's adorable."
        m "Now start taking off those clothes."
        $her_head_state = 12
        her_head_main "You want me to... strip for you...?"
        m "Yes. And I expect you to do it today, girl."
        $her_head_state = 19
        her_head_main "Professor Dumbledore!"
        m "don't you raise your voice at me, girl!"
        $her_head_state = 7
        her_head_main ".....!!?"
        m "Nobody is forcing you to do this."
        m "I am doing you a favour!"
        m "If you don't need the points, please feel free to leave."
        $her_head_state = 8
        her_head_main "....................."
        $her_head_state = 12
        her_head_main "......................................."
        ">Hermione is starting to dance again..."
        show screen clothed_dance #Hermione stands still.
        with fade
        $her_head_state = 15
        her_head_main "{size=-5}(...........................................){/size}"
        m "What are you waiting for then?"
        m "Start with the vest."
        $her_head_state = 12
        her_head_main "............................................................."
        ">Hermione gives you a confused look and then takes off her vest..."
        show screen ctc
        pause
        show screen no_vest_dance
        with d3
        pause
        $her_head_state = 19
        her_head_main "{size=-5}(Am I really going to do this?){/size}"
        menu:
            m "......................."
            "\"Now get rid of your skirt!\"":
                her_head_main "................................."
                show screen blktone
                with d3
                ">Hermione starts to unzip her skirt..."
                ">She seems very hesitant and takes her time..."
                ">Finally the zipper is undone and she has no choice but to take the skirt off..."
                hide screen blktone
                with d3
                her_head_main "{size=-5}(Here it comes then...){/size}"
                $her_head_state = 24
                her_head_main "{size=-5}(For the honour of the \"Gryffindor\"....){/size}"
                ">Hermione takes of her  skirt..."
                show screen ctc
                pause
                show screen no_skirt_dance
                with d3
                pause
                m "..............."
                $her_head_state = 19
                her_head_main "{size=-5}(.........................................){/size}"
                ">Hermione keeps on dancing..."
                m "Alright, your shirt is next!"
                $her_head_state = 20
                her_head_main "My shirt....?"
                show screen blktone
                with d3
                ">Hermione looks extremely embarrassed..."
                ">She clumsily fumbles with the buttons of her shirt..."
                hide screen blktone
                with d3
                m "What's the problem, girl?"
                $her_head_state = 19
                her_head_main "I'm sorry, sir..."
                her_head_main "It's stuck..."
                her_head_main "It won't budge..."
                $her_head_state = 28
                her_head_main "Why won't it budge?! *sob*"
                her_head_main "No, I can't do this, sir! *sob*"
                m "What?"
                her_head_main "I thought I could, but..."
                her_head_main "Stripping for you, sir?"
                her_head_main "People look up to me in this school!"
                her_head_main "I have a reputation...*sob*"
                $her_head_state = 29
                her_head_main "And if I do this..."
            "\"Now take off your shirt!\"":
                $her_head_state = 19
                her_head_main "................................."
                show screen blktone
                with d3
                ">Hermione starts to unbutton her shirt..."
                ">She seems very hesitant and takes her time..."
                ">Finally the last button is undone and she has no choice but to take the shirt off..."
                hide screen blktone
                with d3
                her_head_main "{size=-5}(Okay, take off...){/size}"
                her_head_main "{size=-5}(For honor of \"Gryffindor\"!){/size}"
                show screen blktone
                with d3
                ">Hermione takes off her shirt..."
                hide screen blktone
                with d3
                show screen ctc
                pause
                show screen no_shirt_dance
                with d3
                pause
                $her_head_state = 40
                her_head_main "{size=-5}(I actually did it...){/size}"
                her_head_main "{size=-5}(Professor Dumbledore can see my breasts while I'm dancing for him...){/size}"
                her_head_main "{size=-5}(This is so demeaning...){/size}"
                her_head_main "{size=-5}(But I am doing this for my house...){/size}"
                m "Not bad...."
                her_head_main "{size=-5}(.........................................){/size}"
                show screen blktone
                with d3
                ">Hermione is topless now..."
                ">She keeps on dancing but seems very restricted in her movements now. Even more so than before..."
                ">It seems like she's desperately trying to prevent her breasts from bouncing or swaying..."
                hide screen blktone
                with d3
                m "Alright, your skirt is next!"
                her_head_main "...................."
                show screen blktone
                with d3
                ">Hermione looks extremely embarrassed..."
                show screen blktone8
                with d3
                ">She fumbles with the zipper of her skirt..."
                m "What's the problem, girl?"
                her_head_main "I'm sorry, sir..."
                her_head_main "It's stuck..."
                her_head_main "It won't budge..."
                her_head_main "Why won't it budge?! *sob*"
                $her_head_state = 41
                her_head_main "No, I can't do this, sir! *sob*"
                m "What?"
                her_head_main "I thought I could, but..."
                her_head_main "Stripping for points, sir?"
                her_head_main "People look up to me in this school!"
                her_head_main "I have reputation...*sob*"
                $her_head_state = 42
                her_head_main "And If I do this..."
                
        menu:
            "\"Who cares about your reputation?\"":
                m "Who cares about your reputation? Continue to undress!"
                $ end.SetEndingValue(const_ENDING_STRONG_GIRL,1)
            "There is no one there":
                m "Well, there is no one there and your reputation is not endangered."        


        show screen blkfade 
        with d3
        hide screen blktone8    
        ">Hermione quickly puts her uniform back on..."
        stop music fadeout 1.0
        show screen hermione_02 #Hermione stands still.
        hide screen blkfade
        with d3
        $her_head_state = 31
        her_head_main "Sir, I think I'd better go now... *Sob!*"
        menu:
            "\"Alright. I had fun. Here are your points.\"":
                $herView.setZOrder( 8 )
                $ pos = gMakePos( 390, 340 )
                $herView.showQ( "body_13.png", pos )
                her2 "Really? I didn't ruin it completely then?"
                $herView.hideQ()
                pause.2 #Otherwise a bug occurs. 
                $herView.setZOrder( 5 )
                $ pos = gMakePos( 390, 0 )
            "\"Sure. You will receive no points though.\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $herView.setZOrder( 8 )
                $ pos = gMakePos( 390, 340 )
                $herView.showQ( "body_02.png", pos )
                her2 "Sir... I may not be very good at this..."
                her2 "But I did my best... I think I deserve some--"
                $herView.hideQ()
                m "Juts make sure you try harder next time, miss Granger."
                $herView.showQ( "body_31.png", pos )
                her2 "Next time?!"
                $herView.hideQ()
                $herView.showQ( "body_47.png", pos )
                her2 "I assure you, sir, there will be no next time..."
                $herView.hideQ()
                m "We'll see..."
                $herView.showQ( "body_66.png", pos )
                her2 "Tsk!"
                $herView.hideQ()
                pause.2 #Otherwise a bug occurs. 
                $herView.setZOrder( 5 )
                $ pos = gMakePos( 390, 0 )
                $ hermi.liking -= 35
                call music_block
                jump restore_state_could_not_flirt

    # SECOND PART #

    if IsRunNumber(2): #<====================================================================================================================EVENT 02 
#    if request_11_points == 1: #<====================================================================================================================EVENT 02 
#        $ new_request_11_02 = True # HEARTS
        m "Miss Granger, I need you to dance for me."
        $herView.hideQQ()
        $ pos = POS_140
        $herView.showQQ( "body_66.png", pos )
        her "That again, sir...?"
        m "You will get paid accordingly of course..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "............................"
        $herView.hideshowQQ( "body_69.png", pos )
        her "And you expect me to... ehm..."
        m "Take your clothes off. Naturally."
        $herView.hideshowQQ( "body_69.png", pos )
        stop music fadeout 1.0
        her "......................"
        $herView.hideshowQQ( "body_66.png", pos )
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "Well, why not?"
        $herView.hideshowQQ( "body_86.png", pos )
        her "Yes, I don't see why not!"
        m "Hm...? {size=-4}(Look at her, so eager all of a sudden...){/size}"
        $herView.hideshowQQ( "body_30.png", pos )
        her "After all, as a pupil I am meant to obey your every order, isn't that right, sir?!"
        m "...................."
        $herView.hideshowQQ( "body_30.png", pos )
        her "If the Headmaster tells me to strip for him, Then I shall strip!!!"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Do I find this extremely inappropriate, disgraceful and humiliating?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Of course not. What nonsense!"
        m ".............."
        $herView.hideshowQQ( "body_47.png", pos )
        her "Ha! Might as well do this the proper way!"
        $herView.hideQQ()
        hide screen blktone 
        with d3
        m "??!"
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
        pause 5
        g4 "!!!!!!"
        ">To your surprise Hermione just hops onto your desk and starts dancing franticly..."
        hide screen blkfade
        $ hermione_chibi_xpos = 210 #Near the desk: 400.
        $ hermione_chibi_ypos = 180 #Default: 250
        show screen clothed_dance #Hermione stands still.
        show screen ctc
        with fade
        pause
        show screen bld1
        show screen blktone
        with d3
        $herView.setZOrder( 8 )
        $ pos = gMakePos( 390, 340 )
        $herView.showQ( "body_30.png", pos )
        her2 "If I must degrade myself in order to protect the honour of my house..."
        $herView.hideQ()
        ">Hermione is starting to take off her vest..."
        $herView.showQ( "body_86.png", pos )
        her "So be it then!"
        $herView.hideQ()
        $herView.showQ( "body_87.png", pos )
        her "Just..."
        $herView.hideQ()
        $herView.showQ( "body_88.png", pos )
        her "*groan*"
        $herView.hideQ()
        show screen blktone8
        hide screen blktone
        with d3
        ">Her vest seems to be stuck somehow, but the girl keeps pulling on at the fabric with anger..."
        $herView.showQ( None, pos )
        her "Why won't it....?!"
        $herView.addFaceName( "body_81.png" )
        her "There!"
        $herView.hideQ()
        ">Hermione finally manages to untangle herself and sends the vest flying to the other side of the room..."
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        show screen no_vest_dance
        with d3
        pause
        show screen bld1
        with d3
        $herView.showQ( "body_30.png", pos )
        hide screen ctc
        her "The skirt is next, right?"
        $herView.hideQ()
       
        menu:
            m "..."
            "\"Yes, that's right. Take it off!\"":
                $herView.showQ( None, pos )
                her "Of course!"
                $herView.addFaceName( "body_87.png" )
                her "Here it goes!"
                $herView.hideQ()
                pause.1
                show screen blktone8
                with d3
                ">Hermione sends her skirt flying across the room, just like she did with her vest a moment earlier..."
            "\"You need to calm down, girl. \"":
                $herView.showQ( None, pos )
                her2 "Well, {size=+7}EXCUSE ME{/size}, professor!"
                her2 "You told me to strip for you, but you never told me your preferences in regards to the pace!"
                $herView.hideQ()
                m "Well, I'm telling you now, girl!"
                $herView.showQ( None, pos )
                her2 "Too late!"
                $herView.hideQ()
                pause.1
                show screen blktone8
                with d3
                ">And sure enough Hermione sends the skirt flying across the room, just like she did with her vest a moment earlier..."
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        show screen no_skirt_dance
        with d3
        pause
        show screen bld1
        with d3
        hide screen ctc
        m "{size=-4}(Wow, she is getting really worked up over this...){/size}"
        m "{size=-4}(Maybe it was still too early to--{/size}"
        $herView.showQ( "body_66.png", pos )
        her "My shirt?!!"
        $herView.addFaceName( "body_86.png" )
        her "{size=+9}I don't need it!{/size}"
        $herView.hideQ()
        pause.1
        show screen blktone8
        with d5
        ">Hermione's shirt suddenly hits the floor."
        g4 "{size=-4}(When did she??!){/size}"
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        show screen no_shirt_no_skirt_dance
        with d3
        pause
        show screen bld1
        with d3
        $herView.showQ( None, pos )
        hide screen ctc
        her "Do you enjoy this, sir?"
        $herView.addFaceName( "body_30.png" )
        her2 "Shall I shake my breasts for you like one of those harlots?"
        $herView.hideQ()
        m "Well---"
        $herView.showQ( "body_30.png", pos )
        her2 "Of course! Why wouldn't I degrade myself for your pleasure?!"
        $herView.addFaceName( "body_86.png" )
        her2 "This is completely {size=+7}acceptable!{/size}"
        $herView.hideQ()
        pause.1
        show screen blktone
        with d3
        ">Hermione is starting to shake her naked breasts rather clumsily..."
        ">As you watch the girl's tits sway right and left before your face you find yourself fighting the urge to..."
        menu:
            m "..."
            "-Grab them!-":
                g9 "{size=-4}(Yes, just get my hands on these ample titties, that's what I want to do!){/size}"
                g9 "{size=-4}(Maybe pull on them a little, yes...){/size}"
            "-Slap them!-":
                m "{size=-4}(I want to slap the crap out of her fun bags.){/size}"
                g9 "{size=-4}(Yes, just slap them around a little...){/size}"
            "-Bite on them!":
                m "{size=-4}(Is it weird that I feel like sinking my teeth into her tits?){/size}"
                m "{size=-4}(No, it's not weird!){/size}"
                m "{size=-4}(Just a couple of gentle love-bites!){/size}"
                g9 "{size=-4}(Yes... Maybe more than just a couple...){/size}"
            "-Motorboat them!-":
                m "{size=-4}(I just want to put my face right in between them!){/size}"
                g9 "{size=-4}(Yes, To motorboat these titties would be the best!){/size}"
        ">While you are lost in thought, Hermione keeps on dancing..."
        
        call req11_undress
        $ pos = gMakePos( 390, 235 )
        $herView.showQ( "body_89.png", pos )
        her2 "(Dancing naked in front of the headmaster...)"
        her2 "(If my parents knew about this they would lose their minds...)"
        $herView.addFaceName( "body_90.png" )
        her2 "(Especially my father...)"
        $herView.hideQ()
        ">Hermione is starting to shake her tits again...)"
        $herView.showQ( "body_90.png", pos )
        her "(Hermione Granger - the stripper...)"
        $herView.addFaceName( "body_91.png" )
        her2 "(Forgive me father...)"
        $herView.hideQ()
        pause.1
        show screen blktone8
        hide screen blktone
        with d3
        ">Hermione puts her hands on her tits and starts squeezing them..."
        ">You can only assume that she means to look seductive, but she just looks awkward and ashamed."
        $herView.showQ( "body_91.png", pos )
        her2 "(I used to be a top student... Used to have standards...)"
        $herView.hideQ()
        ">Hermione clutches her tits even harder and then gives them a couple of twists..."
        ">It almost looks as if she is mad at her own breasts and trying to punish them..."
        ">You find the thought strangely arousing..."
        $herView.showQ( "body_92.png", pos )
        $ h_c_u_pic = "03_hp/08_animation_02/05_panties_01.png"
        show screen h_c_u
        her "Well, I hope you enjoyed yourself, sir!"
        $herView.hideQ()
        m "What?"
        $herView.showQ( "body_93.png", pos )
        her "I would like to get paid now..."
        $herView.hideQ()
        m "Aren't you forgetting something, miss Granger?"
        $herView.showQ( "body_92.png", pos )
        her2 "Sir...?"
        $herView.hideQ()
        m "Your panties...?"
        $herView.showQ( "body_94.png", pos )
        her "My panties?"
        her "But, they always leave them on!"
        $herView.hideQ()
        m "Who exactly are \"they\"?"
        m "Strippers in kid's cartoons?"
        m "Stripping is stripping, girl!"
        m "Now take off your panties!"
        $herView.showQ( "body_95.png", pos )
        her "................"
        $herView.hideQ()
        ">Hermione looks horror-struck. All of her anger is gone..."
        $herView.showQ( "body_90.png", pos )
        her "................."
        $herView.hideQ()
        ">Without saying another word..."
        ">She starts to pull down her panties..."
        g9 "......................................."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
        $ walk_xpos=470 #Animation of walking chibi. (From)
        $ walk_xpos2=360 #Coordinates of it's movement. (To)
        hide screen blktone8
        hide screen bld1
        show screen snape_walk_01 
        with d3
        pause 1.5
        stop music 
        $ renpy.play('sounds/scratch.wav')
        show screen snape_02 #Snape stands still.
        
        $ posHead = gMakePos( pos.xpos, pos.ypos )
        

        $ tt_xpos=330 #Defines position of the Snape's full length sprite. (Default 300). 140 - center.
        $ tt_ypos=340#(Default 0). Right bottom corner: 340
        $ s_sprite = "03_hp/10_snape_main/snape_01.png"
        show screen s_head
        $ h_c_u_pic = "03_hp/08_animation_02/05_panties_01.png"
        show screen h_c_u
               
        sna2 "Listen, Genie. I've been thinki--"
        $ s_sprite = "03_hp/10_snape_main/snape_11.png"
        with hpunch
        sna2 "................................................................................................................................................................................"
        
        # add black-white hermione as a pose, higher then face
        #$herViewHead.data().addPose( CharacterExItem( herViewHead.mPoseFolder, 'hermione_bw_strip.png', G_Z_FACE + 1 ) )
        $herViewHead.data().addItem( 'item_pose_bw_strip' )
        $herViewHead.showQ( "body_96.png", posHead )
        with hpunch
        her "(Professor Snape???????!)"
        $ s_sprite = "03_hp/10_snape_main/snape_12.png"
        show screen s_head
        sna2 "Miss Granger?"
        hide screen s_head
        $herViewHead.showQ( "body_96.png", posHead )
        her "(No, no... This is not happening. Please...)"
        $herViewHead.hideQ()
        $herViewHead.data().delPose()
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "...................................."
        show screen bld1
        with d3
        menu:
            m "..."
            "\"Severus, I am busy right now.\"":
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna "Yes... I can see that..."
                $herViewHead.showQ( "body_97.png", posHead )
                her "{size=-7}(I want to die!){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_12.png"
                show screen s_head
                sna2 "I shall postpone our conversation for later then, Geni-- *khem!* Albus."
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                sna "Miss Granger..."
                $herViewHead.showQ( "body_97.png", posHead )
                her ".........................................."
                $herViewHead.hideQ()
            "\"Severus! Please, come join us.\"":
                $ hermi.liking -= 37
                $ snape_invated_to_watch = True #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
                $ s_sprite = "03_hp/10_snape_main/snape_14.png"
                show screen s_head
                sna "Seriously?"
                $herViewHead.showQ( "body_97.png", posHead )
                her "(Professor, no, please.............................)"
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna "A very tempting offer indeed..."
                $herViewHead.showQ( "body_95.png", posHead )
                her "!!!!!!......."
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna2 "Well, maybe some other time..."
                $herViewHead.showQ( "body_99.png", posHead )
                her "{size=-5}(There will be no other time!){/size}"
                her "{size=-5}(I will stop selling favours from now on, I swear!){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_12.png"
                show screen s_head
                sna2 "I shall postpone our conversation then, Geni-- *khem!* Albus."
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                sna2 "Miss Granger..."
                $herViewHead.showQ( "body_97.png", posHead )
                her "................................."
                $herViewHead.hideQ()
        show screen blkfade 
        with d3
        hide screen snape_walk_01 
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        pause 1.5

        
        ">Snape leaves..."
        ">Hermione hastily hops off your desk."
        ">She starts putting her clothes back on rather frantically..."
        $herViewHead.showQ( "body_98.png", posHead )
        her "My shirt! Where is my shirt?!"
        $herViewHead.hideQ()
        m "It's over there, by the fireplace..."
        pause 1

        call req11_dress
        #$herViewHead.data().addPose( CharacterExItemPoseShowTits( herViewHead.mPoseFolder, 'pose_dress_up.png', G_Z_POSE ) )
        $herViewHead.data().addItem( 'item_pose_show_tits' )
        $herViewHead.showQ( "body_85.png", posHead )
        her2 "................................"
        $herViewHead.hideQ()
        pause 2
        $herViewHead.data().delPose()
        $herViewHead.showQ( "body_33.png", posHead )
        
        
        her "........................"
        stop music fadeout 2.0
        her "Can I just get my points now, please?"
        $herViewHead.hideQ()
        hide screen snape_02 #Snape stands still.
        pause.1
        $herView.setZOrder( 5 )
        
        $ pos = gMakePos( pos.xpos, 0 )
        $ hermione_chibi_xpos = 400 #Near the desk.
        show screen hermione_02 #Hermione stands still.
        $ hermione_chibi_ypos = 250 #Default: 250. Another number is 180
            
            
    # THIRD PART #
            
    if IsRunNumberOrMore(3): #<====================================================================================================================EVENT 03
#    if request_11_points >= 2: #<====================================================================================================================EVENT 03
#        $ new_request_11_03 = True # HEARTS
        if snape_invated_to_watch: #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
            m "(Hm... Should I invite that Professor Snape guy to watch as well?)"
            menu:
                "\"Yes! Hermione needs an audience!\"":
                    if not invited_snape_once_already:
                        $ invited_snape_once_already = True #Makes sure this event takes place only once.
                        hide screen blktone
                        with d3
                        m "Miss, Granger, I will be buying another favour from you today."
                        $herView.hideQQ()
                        $ pos = POS_140
                        $herView.showQQ( "body_16.png", pos )
                        her "Of course, sir."
                        m "But before that, do you think you could go and fetch professor Snape for me?"
                        $herView.hideshowQQ( "body_17.png", pos )
                        her "...professor Snape?"
                        her "May I ask, why, sir?"
                        m "Oh, I just think you could use a bigger audience for your striptease performance."
                        $herView.hideshowQQ( "body_48.png", pos )
                        her "My striptease performance...?!!"
                        $herView.hideshowQQ( "body_47.png", pos )
                        her "With all due respect, sir..."
                        $herView.hideshowQQ( "body_07.png", pos )
                        her "{size=-5}(Which I have oh so little left for you...){/size}"
                        $herView.hideshowQQ( "body_30.png", pos )
                        her "I refuse to degrade myself for professor Snape's amusement!"
                        m "No, no, you got it all wrong, girl."
                        $herView.hideshowQQ( "body_15.png", pos )
                        her "Hm..?"
                        m "I want to prove that professor Snape is dirty, and I need your help."
                        $herView.hideshowQQ( "body_48.png", pos )
                        her "!!!"
                        m "Yes, I want to catch him in the act!"
                        $herView.hideshowQQ( "body_11.png", pos )
                        her "Professor, I didn't realize..."
                        $herView.hideshowQQ( "body_06.png", pos )
                        her "I see now..."
                        her "I am sorry for doubting you sir..."
                        m "No biggy. Now go find professor Snape and bring him here."
                        $herView.hideshowQQ( "body_111.png", pos )
                        her "Right away sir!"
                        label fetching_snape:
                        $herView.hideQQ()
                        hide screen bld1
                        with d3
                        hide screen hermione_02 #Hermione stands still.
                        $ walk_xpos=400 #Animation of walking chibi. (From)
                        $ walk_xpos2=610 #Coordinates of it's movement. (To)
                        $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                        show screen hermione_walk_01_f 
                        pause 2
                        hide screen hermione_walk_01_f 
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        with Dissolve(.3)
                        pause.2
                        show screen blkfade
                        with d5
                        stop music fadeout 1.0
                        ">...................{w}...................{w}...................{w}..................."
                        hide screen blkfade
                        with d5
                        $ walk_xpos=610 #Animation of walking chibi. (From)
                        $ walk_xpos2=360 #Coordinates of it's movement. (To)
                        $ snapes_speed = 04.0 #The speed of moving the walking animation across the screen.
                        show screen snape_walk_01 
                        
                        pause 4
                        show screen snape_02 #Snape stands still.

                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        $ hermione_chibi_xpos = 610
                        $ hermione_chibi_ypos = 250
                        show screen hermione_02 #Hermione stands still.
                        with Dissolve(.5)
                        pause.3
                        
                        $ walk_xpos=610 #Animation of walking chibi. (From)
                        $ walk_xpos2=500 #Coordinates of it's movement. (To) 400 - near desk.
                        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                        show screen hermione_walk_01 
                        pause 3
                        $ hermione_chibi_xpos = 500 #Near the desk - 400
                        show screen hermione_02 #Hermione stands still.
                        pause.5
                        show screen ctc
                        pause
                        show screen bld1
                        with Dissolve(.3)
                        $ tt_xpos=180 #Defines position of the Snape's full length sprite. Default - 300
                        $ tt_ypos=0
                        $ s_sprite = "03_hp/10_snape_main/snape_01.png"
                        show screen snape_main
                        show screen ctc
                        with Dissolve(.3)
                        
                    else:
                        hide screen blktone
                        with d3
                        m "Miss, Granger, I will be buying another favour from you today."
                        $herView.hideQQ()
                        $ pos = POS_140
                        $herView.showQQ( "body_16.png", pos )
                        her "Of course, sir."
                        m "But before that, do you think you could go and fetch professor Snape for me?"
                        $herView.hideshowQQ( "body_17.png", pos )
                        her "...professor Snape?"
                        her "may I ask, why, sir?"
                        m "Oh, I just want you to dance for us."
                        $herView.hideshowQQ( "body_14.png", pos )
                        her "!!!"
                        m "I want to prove that professor Snape is dirty, and I need your help."
                        $herView.hideshowQQ( "body_29.png", pos )
                        her "But didn't we already establish that last time I did this?"
                        m "Well, ehm... sure..."
                        m "But I will need more proof if I am to take this issue to the ministry of magic!"
                        $herView.hideshowQQ( "body_47.png", pos )
                        her "....."
                        m "So, what do you say girl?"
                        m "One more dance for the greater good?"
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Well, alright..."
                        m "Good. Go find professor Snape then."
                        jump fetching_snape
                    
                    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                    sna "Genie... err, I mean Albus, you wanted to see me?"
                    m "Yes. Are you in the mood for a little striptease?"
                    hide screen snape_main
                    with d3
                    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
                    show screen snape_main
                    with d3
                    sna "Oh...?"
                    sna "Miss Granger here will be performing I assume?"
                    $ pos.xpos = 380
                    $herView.showQQ( "body_34.png", pos )
                    her ".............."
                    m "Yes, our little mynx is more than happy to take off her clothes for our entertainment."
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "............"
                    m "Aren't you girl?"
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Yes, sir."
                    m "Let's get started then!"
                    $herView.hideQ()
                    hide screen snape_main
                    with d3
                    pause
                    
                    show screen blkfade
                    with Dissolve(1)
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 1
                    $ posHead = gMakePos( 390, 340 )
                    $herViewHead.showQ( "body_16.png", posHead )
                    her2 "............."

                    
                    
                    $ s_head_xpos = 330 # x = 330,
                    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.
                    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
                    show screen s_head2
                    sna "......................"
                    hide screen s_head2
                    m ".........................."
                    hide screen blkfade
                    hide screen bld1
                    $ hermione_chibi_xpos = 210 #Near the desk: 400.
                    $ hermione_chibi_ypos = 180 #Default: 250
                    show screen clothed_dance #Hermione stands still.
                    show screen ctc
                    show screen s_c_u
                    $ s_c_u_pic = "03_hp/09_snape_ani/snape_0130.png"
                    $ snape_chibi_xpos = 290 #Default 360.
                    $ snape_chibi_ypos = 210
                    with fade
                    pause
                    show screen bld1
                    with d3
                    m "So... Severus... How's life?"
                    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
                    show screen s_head2
                    sna "Well, you know... same old, same old..."
                    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
                    sna " The Students are causing me grief..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    sna2 "In fact, miss Granger here managed to cause me more stress than any other student..."
                    $herViewHead.showQ( "body_68.png", posHead )
                    her "..............................."
                    $herViewHead.hideQ()
                    m "Oh, I am sure she is very sorry about that..."
                    $herViewHead.showQ( "body_74.png", posHead )
                    her "{size=-4}(Not even a little bit!){/size}"
                    $herViewHead.hideQ()
                    m "And will make up for it today, won't you girl?"
                    $herViewHead.showQ( "body_53.png", posHead )
                    her "Uhm... Yes, professor."
                    $herViewHead.hideQ()
                    hide screen ctc
                    pause.2
                    show screen blktone
                    with d3
                    ">Hermione takes her vest off and starts to sway her hips seductively."
                    hide screen blktone
                    with d3

                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_vest_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    $herViewHead.showQ( "body_87.png", posHead )
                    her "..................."
                    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
                    show screen s_head2
                    sna "Hm... You are being suspiciously quiet girl."
                    $herViewHead.showQ( "body_48.png", posHead )
                    her "{size=-4}(Oh no! Is he onto us?){/size}"
                    $herViewHead.showQ( "body_57.png", posHead )
                    her2 "I am just doing what the headmaster told me, professor..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Aren't you going to lecture me on the \"corruption that is taking over Hogwarts\" like you do every other day?"
                    hide screen s_head2
                    m "Severus..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "No, Albus I want to hear little miss perfect's answer."
                    $herViewHead.showQ( "body_57.png", posHead )
                    her2 "I just want you to have a good time, sir..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Oh! It's \"sir\" now, isn't I?"
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
                    sna2 "What happened to \"snape'o'doodle\" and \"Professor Snivellus\"??!"
                    hide screen s_head2
                    g9 "{size=-5}( \"snape'o'doodle\, heh... that's funny.){/size}"
                    $herViewHead.showQ( "body_57.png", posHead )
                    her "............."
                    $ s_sprite = "03_hp/10_snape_main/snape_08.png"
                    show screen s_head2
                    sna2 "Yes, I know what are you calling me behind my back, you wretched girl!"
                    $herViewHead.showQ( "body_86.png", posHead )
                    her2 "Well, maybe that's because you deserve it... sir."
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "What?!"
                    sna "How dare you....?"
                    $ s_sprite = "03_hp/10_snape_main/snape_15.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Who do you think you are? You filthy mu--"
                    $herViewHead.showQ( "body_62.png", posHead )
                    her2 "Professor, one of your staff is verbally abusing me!"
                    her2 "Are you going to allow this?"
                    $ s_sprite = "03_hp/10_snape_main/snape_08.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Verbally abusing...?! You have some nerve, girl!"
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna2 "Albus, will you allow her to talk back to a teacher like that?"
                    $herViewHead.showQ( "body_62.png", posHead )
                    her "Professor Dumbledore!"
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Albus!"
                    hide screen s_head2
                    menu:
                        m "..."
                        "\"Miss Granger, show some respect!\"":
                            $ hermi.liking -= 9
                            $herViewHead.showQ( "body_61.png", posHead )
                            her "What?"
                            her "But professor!"
                            $herViewHead.hideQ()
                            m "Young lady, you {size=+4}will{/size} calm down now."
                            $herViewHead.showQ( "body_66.png", posHead )
                            her "Tsk!"
                            $herViewHead.hideQ()
                            m "And take off your skirt already, would you?"
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "......."
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "..........."
                            hide screen s_head2  
                        "\"Severus, you started this.\"":
                            $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                            show screen s_head2  
                            sna "What? Me?!"
                            $herViewHead.showQ( "body_52.png", posHead )
                            her "Thank you, professor."
                            $ s_sprite = "03_hp/10_snape_main/snape_08.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Albus, you are spoiling the girl! She must be taught a lesson!"
                            hide screen s_head2 
                            m "...............Severus."
                            g4 "Did you hit your head?!"
                            $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "I beg your pardon?"
                            hide screen s_head2 
                            g4 "The girl is already stripping for you!"
                            g4 "What punishment are you talking about?"
                            $ s_sprite = "03_hp/10_snape_main/snape_16.png" #SNAPE
                            show screen s_head2  
                            sna "Tsk... How about a flogging?" 
                            hide screen s_head2
                            g4 "Severus!"
                            $ s_sprite = "03_hp/10_snape_main/snape_17.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Alright, alright, I see your point..."
                            hide screen s_head2
                            m "Miss Granger, are you going to strip or did you climb on my desk to get a better view?"
                            $herViewHead.showQ( "body_87.png", posHead )
                            her "Ehm..."
                            $herViewHead.hideQ()
                            m "Take of your skirt, girl!"
                            $herViewHead.showQ( "body_55.png", posHead )
                            her "Yes, sir..."
                            $herViewHead.hideQ()
                        "\"Both of you, calm the fuck down.\"":
                            m "You, tall-dark-and-handsome, calm down a bit, would you?"
                            $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "I beg your pardon?"
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "Yes! You tell him profess--"
                            $herViewHead.hideQ()
                            m "You as well, you perverted little mynx!"
                            m "Calm down and take your skirt off already."
                            $herViewHead.showQ( "body_79.png", posHead )
                            her "I am not perverted..."
                            $herViewHead.hideQ()
                            m "The skirt, girl!"
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "......"
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2  
                            sna "............."
                            hide screen s_head2     
                    
                    show screen blktone
                    with d3
                    ">Hermione swiftly takes off her \"Hogwarts\" skirt..."
                    hide screen blktone
                    with d3
                   
                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_skirt_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    show screen s_head2
                    sna "Hm..."
                    $herViewHead.showQ( "body_87.png", posHead )
                    her "........................"
                    $herViewHead.hideQ()
                    m "Yes, much better!"
                    show screen blktone
                    with d3
                    ">Hermione keeps on dancing, while she's Wearing nothing but her shirt now..."
                    menu:
                        m "..."
                        "\"Severus, what about that Potter boy?\"":
                            $herViewHead.showQ( "body_55.png", posHead )
                            her "(.....?)"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2
                            sna "What about him?"
                            hide screen s_head2
                            m "Is he still causing you grief?"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Oh..."
                            sna "Not really, no..."
                            $ s_sprite = "03_hp/10_snape_main/snape_06.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "To be honest I never really had a problem with the boy himself..."
                            sna2 "Although I did plan to make his life here miserable because of his father..."
                            $ s_sprite = "03_hp/10_snape_main/snape_02.png" #SNAPE
                            show screen s_head2    
                            sna2 "But lately I have way more interesting projects to occupy myself with..."
                            $herViewHead.showQ( "body_55.png", posHead )
                            her "..................."  
                            $herViewHead.hideQ()
                        "\"Severus, what about the Weasleys?\"":
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "What about them?"
                            hide screen s_head2   
                            m "Are they still causing you trouble?"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes... Even more than before."
                            hide screen s_head2
                            m "Hm...?"
                            m "You seem surprisingly indifferent about that..."
                            $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "That's because I know that they will get what they deserve eventually..."
                            hide screen s_head2
                            m "Revenge? Cool! What do you have in mind?"
                            $herViewHead.showQ( "body_55.png", posHead )
                            her "!!!"
                            $ s_sprite = "03_hp/10_snape_main/snape_06.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Hm... Can't discuss this with \"the enemy\" present."
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "Tsk!"
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "All I can say is that it involves their beloved little sister Ginny..."
                            hide screen s_head2  
                            m "Ginny? Hm... What a curious name for a girl..."
                            m "............."
                            m "So, you plan to fuck her then?"
                            $ s_sprite = "03_hp/10_snape_main/snape_08.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "!!?"
                            $ s_sprite = "03_hp/10_snape_main/snape_17.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Albus, please, not in front of the girl!"
                            hide screen s_head2  
                            m "Alright, alright..."
                            $herViewHead.showQ( "body_87.png", posHead )
                            her "{size=-5}(Ginny...){/size}"
                            $herViewHead.hideQ()
                        "\"How would you grade Hermione's butt?\"":
                            $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "miss Hermione's buttocks?" 
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "!!!............"
                            $herViewHead.hideQ()
                            m "Sure! As you would grade a paper."
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Hm..."
                            hide screen s_head2  
                            pause.1
                            ">Professor Snape gives Hermione's buttocks an appraising look..."
                            $herViewHead.showQ( "body_44.png", posHead )
                            her ".........?"
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "I would say..."
                            $herViewHead.showQ( "body_59.png", posHead )
                            her "............?!"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes... \"{size=+5}F-{/size}\"."
                            $herViewHead.showQ( "body_48.png", posHead )
                            her "(What?!)"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Unsatisfactory..."
                            sna2 "Look at that pitiful thing. Tiny and skinny... That's a boy's butt."
                            $herViewHead.showQ( "body_51.png", posHead )
                            her "!!!!!!!!!!"
                            $herViewHead.hideQ()
                            
                    show screen blktone
                    with d3
                    ">One after another, Hermione undoes the buttons of her shirt and then takes it off..."
                    hide screen blktone
                    with d3
                   
                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_shirt_no_skirt_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    m "Alright! We Finally get to the good stuff!"
                    $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                    show screen s_head2       
                    sna "Hm..."
                    
                    call req11_undress
                    
                    $ posHead = gMakePos( 390, 235 )
                    $herViewHead.showQ( "body_90.png", posHead )
                    her "........"
                    $herViewHead.hideQ()
                    menu:
                        m "..."
                        "-Start jerking off-":
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            
                            hide screen bld1
                            show screen ctc
                            with d3
                            pause
                            show screen blkfade
                            with d6
                            $herViewHead.showQ( "body_94.png", posHead )
                            her "Professor Dumbledore?!"
                            $herViewHead.hideQ()
                            m "It's alright, girl. Don't mind me..."
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Oh, we're doing it like this then?"
                            sna "Well, don't mind if I do..."
                            $ posHead.ypos = 340
                            $herViewHead.showQ( "body_94.png", posHead )
                            
                            her "!!!"
                            $herViewHead.hideQ()
                            
                            
                            hide screen genie
                            hide screen no_shirt_no_skirt_dance
                            $ genie_chibi_xpos = -185
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "jerking_off_02_ani"
                            $ snape_chibi_xpos = -185
                            $ snape_chibi_ypos = 10
                            $ s_c_u_pic = "jerking_off_03_ani" #Snape.
                            show screen chair_02
                            show screen g_c_u
                            show screen desk_02
                            show screen no_shirt_no_skirt_dance
                            hide screen blkfade
                            with fade
                            pause
                            show screen bld1
                            with d3
                            $herViewHead.showQ( "body_95.png", posHead )
  
                            her2 "No, guys... err I mean, sirs... Ehm, professors!"
                            $herViewHead.hideQ()
                            m "Don't you mind us girl, just keep on doing your thing."
                            $herViewHead.showQ( None, posHead )
                            her "But..."
                            $herViewHead.showQ( "body_99.png", posHead )
                            her2 "No! I refuse to dance with those things pointed at me!"
                            her2 "You need to put them away or the dance is over!"
                            $herViewHead.hideQ()
                            m "You aren't in any position to give us orders, girl."
                            $herViewHead.showQ( "body_110.png", posHead )
                            her2 "that was not an order, sir. It was an ultimatum."
                            $herViewHead.hideQ()
                            menu:
                                m "..."
                                "\"Alright Severus, let's be civil...\"":
                                    $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                                    show screen s_head2                                                          #SNAPE
                                    sna2 "I see Miss Granger manages to remain exceptionally stubborn in any situation..."
                                    hide screen s_head2  
                                    show screen blkfade
                                    with d3
                                    hide screen no_shirt_no_skirt_dance
                                    show screen genie
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk_02
                                    show screen no_shirt_no_skirt_dance
                                    show screen s_c_u
                                    $ s_c_u_pic = "03_hp/09_snape_ani/snape_0130.png"
                                    $ snape_chibi_xpos = 290 #Default 360.
                                    $ snape_chibi_ypos = 210
                                    pause.3
                                    hide screen blkfade 
                                    with d3
                                    jump civil_with_snape
                                    
                                "\"(Pst! Remember why we are doing this!)\"":
                                    if hermi.whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        $herViewHead.showQ( "body_104.png", posHead )
                                        her "Oh, right..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "What was that?"
                                        $herViewHead.showQ( "body_108.png", posHead )
                                        her "Please don't mind what I just said..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Hm...?"
                                        $herViewHead.showQ( "body_108.png", posHead )
                                        her2 "I do not mind you touching yourself in front of me..."
                                        her2 "Yes, I do not mind it at all..."
                                        her "I will just keep on dancing then..."
                                        $herViewHead.hideQ()
                                        hide screen ctc
                                        pause.1
                                        show screen blktone
                                        with d3
                                        show screen blktone8
                                        with d3
                                        ">You keep on jerking off while you're watching Hermione dance..."
                                        ">Hermione squeezes her breasts and shakes her hips slightly..."
                                        hide screen blktone8
                                        with d3
                                        m "Yes, girl. Very good."
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "*Khem!* Acceptable performance, miss Granger."
                                        $herViewHead.showQ( "body_97.png", posHead )
                                        her "...................."
                                        $herViewHead.hideQ()
                                        m "Heh..."
                                        $herViewHead.hideQ()
                                        m "How would you grade her tits then?"
                                        $herViewHead.showQ( "body_94.png", posHead )
                                        her "......"
                                        $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Hm......"
                                        $herViewHead.showQ( "body_103.png", posHead )
                                        her "........"
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "\"B+\"!"
                                        $herViewHead.showQ( "body_94.png", posHead )
                                        her "!!!"
                                        $herViewHead.hideQ()
                                        m "Really?"
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Yes. I do give credit where credit is due."
                                        $herViewHead.showQ( "body_90.png", posHead )
                                        her "(Professor...)"
                                        $herViewHead.showQ( "body_102.png", posHead )
                                        her "(Time for my finishing act then!)"
                                        $herViewHead.hideQ()
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Hermione bends over and slides her panties down."
                                        ">Her movements lack grace..."
                                        ">But a pretty pussy is always a welcome sight nonetheless..."
                                        ">You show your appreciation by stroking your cook even faster..."
                                        
                                       
                                        hide screen blktone8 
                                        hide screen blktone
                                        with d3
                                        hide screen bld1
                                        with d3
                                        show screen ctc
                                        pause
                                        $ h_c_u_pic = "no_panties_dance_ani"
                                        hide screen no_shirt_no_skirt_dance
                                        show screen h_c_u
                                        with d3
                                        pause
                                        show screen bld1
                                        with d3
                                        show screen blktone
                                        with d3
                                        
                                        $ s_sprite = "03_hp/10_snape_main/snape_18.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Yes... Yes!!!"
                                        sna2 "Now shake those B+ titties for me, you harlot!"
                                        $herViewHead.showQ( "body_99.png", posHead )
                                        her "......."
                                        $herViewHead.hideQ()
                                        hide screen ctc
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Hermione suddenly breaks into a series of rather complex pirouettes."
                                        $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Yes, such grace..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "That lithe young body!"
                                        $herViewHead.showQ( "body_106.png", posHead )
                                        her "........."
                                        $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Oh, yes!"
                                        $herViewHead.showQ( "body_106.png", posHead )
                                        her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}"
                                        $herViewHead.hideQ()
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Hermione seems very focused on her dancing routine..."
                                        hide screen blktone8
                                        with d3
                                        $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Yes, and now another pirouette!"
                                        sna "Magnificent!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "I would applaud you but one of my hands is very busy at the moment."
                                        hide screen s_head2  
                                        m "{size=-4}(Was that an attempt at a joke?){/size}"
                                        m "{size=-4}(Man, horny Snape is weird...){/size}"
                                        show screen blktone8
                                        with d3
                                        ">Hermione performs another set of movements and pirouettes..."
                                        ">Gives a little curtsy bow to the imaginary public..."
                                        show screen blkfade
                                        with d3
                                        $ hermione_chibi_xpos = -210 #400 = Near the desk.
                                        $ hermione_chibi_ypos = 10
                                        $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                        ">And then slumps down on her butt exhausted."
                                        
                                        hide screen blktone
                                        with d3
                                        hide screen blktone8
                                        with d3
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1 
                                        with d3
                                        show screen ctc
                                        pause
                                        $herViewHead.showQ( "body_102.png", posHead )
                                        her "Whew... This was--"
                                        $herViewHead.hideQ()
                                        with hpunch
                                        g4 "ARGH! YOU FUCKING WHORE!"
                                        $herView.hideQQ()
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ genie_chibi_xpos = -210
                                        $ genie_chibi_ypos = 10
                                        $ genie_cum_chibi_xpos =  -210
                                        $ genie_cum_chibi_ypos  = 10
                                        $ g_c_c_u_pic = "genie_cum_03"
                                        $ h_c_u_pic = "03_hp/08_animation_02/08_sits_02.png"
                                        show screen g_c_c_u
                                        pause
                                        
                                        #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, 'sperm_01.png', G_Z_FACE + 1 ) )
                                        $herViewHead.data().addItem( 'item_sperm', '01' )
                                        $herViewHead.showQ( "body_104.png", posHead )
                                        her "??!!!"
                                        $herViewHead.hideQ()
                                        $herViewHead.showQ( "body_97.png", posHead )
                                        
                                        $ s_sprite = "03_hp/10_snape_main/snape_18.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Good job, you harlot!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Here is your reward!"
                                        hide screen s_head2     
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ snape_chibi_xpos = -210
                                        $ snape_chibi_ypos = 10
                                        $ snape_cum_chibi_xpos =  -210
                                        $ snape_cum_chibi_ypos  = 10
                                        $ s_c_c_u_pic = "snape_cum_01"
                                        show screen s_c_c_u
                                        pause
                                        $herViewHead.showQ( "body_104.png", posHead )
                                        #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, 'sperm_02.png', G_Z_FACE + 1 ) )
                                        $herViewHead.data().addItem( 'item_sperm', '02' )
                                        her "!!!!!!!!!!!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Oh... Yes..."
                                        hide screen s_head2 
                                        g4 "Little slut!"
                                        $herViewHead.showQ( "body_106.png", posHead )
                                        her "..............................."
                                
                                        $ s_c_c_u_pic = "03_hp/08_animation_02/11_cum_18.png"
                                        $ g_c_c_u_pic = "03_hp/08_animation_02/09_cum_18.png"
                                        $ s_sprite = "03_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Ha-ha-ha! This is magnificent!"
                                        hide screen s_head2
                                        g9 "I know, right!?"
                                        show screen bld1
                                        with d3
                                        $ g_c_u_pic = "03_hp/08_animation_02/06_jerking_01.png" # Genie stands still with his dick in hand.
                                        $ s_c_u_pic = "03_hp/08_animation_02/10_jerking_01.png" # Snape stands still with his dick in hand.
                                        $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Yes... We should do this more often."
                                        $herViewHead.showQ( "body_106.png", posHead )
                                        her "................."
                                        $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Your performance was acceptable, miss Granger..."
                                        $herViewHead.showQ( "body_91.png", posHead )
                                        her "Thank you................"
                                        $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "But if I were to grade it..."
                                        $herViewHead.showQ( "body_91.png", posHead )
                                        her "..........."
                                        $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Hm...."
                                        $herViewHead.showQ( "body_91.png", posHead )
                                        her "............"
                                        $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "\"{size=+5}F+{/size}\"!"
                                        $herViewHead.showQ( "body_112.png", posHead )
                                        stop music
                                        her "{size=+5}WHAT?!!!{/size}"
                                        $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Yes... Quite a few things could use some improvement actually."
                                        $herViewHead.showQ( "body_110.png", posHead )
                                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                        her "I cannot believe this!"
                                        $herViewHead.hideQ()
                                        pause
                                        show screen blkfade 
                                        with d3
                                        hide screen h_c_u 
                                        hide screen s_c_c_u
                                        hide screen g_c_c_u
                                        show screen genie
                                        $ snape_chibi_xpos = -60
                                        $ snape_chibi_ypos = 10
                                        $ s_c_u_pic = "jerking_off_03_ani" #Snape.
                                        hide screen chair_02
                                        hide screen g_c_u
                                        hide screen desk_02
                                        $ hermione_chibi_xpos = 300 #Near the desk: 400. (210 - standing on desk.)
                                        $ hermione_chibi_ypos = 260#Default: 250. (180- standing on desk.)
                                        show screen h_c_u 
                                        $ h_c_u_pic = im.Flip("03_hp/08_animation_02/07_dance_03.png", horizontal=True)
                                        ">Hermione furiously jumps off your desk."
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1
                                        with d3
                                        pause
                                        
                                        
                                        
                                        $ pos = POS_140
                                        show screen bld1
                                        with d5
                                        
                                        
                                        $herView.data().addTransform( gTrEx( 'flip', horizontal = True ) )
                                        $herView.showQQ( "body_101.png", pos )
                                        pause
                                        hide screen ctc
                                        her "I demand a higher grade than that!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                                        show screen s_head2      
                                        sna2 "You do not demand a grade miss Granger, you earn it."
                                        hide screen s_head2     
                                        $herView.hideQQ()
                                        $ herView.showQQ( "body_107.png", pos )
                                        her "I did earn it!"
                                        $herView.hideQQ()
                                        $ herView.showQQ( "body_103.png", pos )
                                        her "And could you at least have the decency to stop touching yourself, sir!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2     
                                        sna2 "Tch..."
                                        hide screen s_head2   
                                        $herView.hideQQ()
                                        m "(Are they for real?)"
                                        show screen ctc
                                        pause
                                        show screen blkfade
                                        with d7
                                        hide screen ctc
                                        hide screen s_c_u
                                        hide screen h_c_u
                                        $ hermione_chibi_xpos = 400 #Near the desk.
                                        $ hermione_chibi_ypos = 250 #Default: 250
                                        show screen hermione_02 #Hermione stands still.
                                        ">You watch Snape with his dick still hanging out and the cum-covered Hermione argue loudly about her imaginary grade."
                                        ">After a while Professor Snape agrees to change Hermione's grade from \"F+\" to \"D-\"."
                                        ">Then he beats a hasty retreat before Hermione has a chance to start another argument..."
                                        hide screen blkfade
                                        with d5
                                        $herView.data().delTransform()
                                        $herView.data().delItem( 'item_sperm' )
                                        #$herView.data().addItemKey( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                        $herView.data().addItem( 'item_sperm_dried' )
                                        $herView.hideQQ()
                                        $ pos = POS_140
                                        call req11_dress
                                        $herView.showQQ( "body_29.png", pos )
                                        her "Well..."
                                        her "Was our mission a success, sir?"
                                        menu:
                                            m "..."
                                            "\"Huh? What mission?\"":
                                                $ hermi.liking -= 7
                                                $herView.hideshowQQ( "body_32.png", pos )
                                                her "I only agreed to this so that you could catch professor Snape in the act, sir!"
                                                $herView.hideshowQQ( "body_33.png", pos )
                                                her "So that we would have definite proof that he is \"dirty\"!"
                                                m "Oh, that mission..."
                                                m "Yes. Mission accomplished!"
                                            "\"Yes! Thanks to you!\"":
                                                pass
                                        m "Good job. Miss Granger."
                                        $herView.hideshowQQ( "body_33.png", pos )
                                        her "I am happy to have been of help, sir!"
                                        $herView.hideshowQQ( "body_34.png", pos )
                                        her "...Can I get paid now, please?"
                                        

                                    else:
                                        $herViewHead.showQ( "body_94.png", posHead )
                                        her "Оh..."
                                        $herViewHead.showQ( "body_97.png", posHead )
                                        her "No, I can't! This is just not worth it!"
                                        hide screen ctc
                                        $herViewHead.hideQ()
                                        pause.1
                                        show screen blkfade
                                        with d5
                                        ">Hermione jumps off the desk and starts to put her clothes back on."
                                        $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Well, this was awfully anticlimactic..."
                                        hide screen s_head2  
                                        g4 "You don't say..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "May as well leave now I suppose. I will talk to you later, Albus."
                                        hide screen s_head2  
                                        m "Yes, later, Severus."
                                        $ s_sprite = "03_hp/10_snape_main/snape_04.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Miss Granger..."
                                        $herViewHead.showQ( "body_99.png", posHead )
                                        her "Professor..."
                                        $herViewHead.hideQ()
                                        her "I would like to get paid now."
                                        show screen ctc
                                        pause.4
                                        hide screen s_c_u
                                        hide screen ctc
                                        ">Professor Snape leaves..."
                                        $herViewHead.showQ( "body_91.png", posHead )
                                        stop music fadeout 1.0
                                        her "...................."
                                        $herViewHead.hideQ()
                                        pause.5
                                        ">.................{w}.................{w}.................{w}................."
                                        call req11_dress
                                        $herViewHead.showQ( "body_33.png", posHead )
                                        
                                        
                                        her "...Can I get paid now... sir...?"
                                        $herViewHead.hideQ()

                        "-Just keep on watching-":
                            label civil_with_snape:
                            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                            # JUST WATCHING.
                            $herViewHead.showQ( "body_102.png", posHead )
                            her "I will just keep on dancing then..."
                            $herViewHead.hideQ()
                            hide screen ctc
                            pause.1
                            show screen blktone8
                            with d3
                            ">Hermione squeezes her breasts and shakes her hips slightly..."
                            hide screen blktone8
                            with d3
                            m "Yes, girl. Very good."
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "*Khem!* Acceptable performance, miss Granger."
                            $herViewHead.showQ( "body_102.png", posHead )
                            her "...."
                            $herViewHead.hideQ()
                            m "Heh..."
                            m "How would you grade her tits then?"
                            $herViewHead.showQ( "body_90.png", posHead )
                            her "......"
                            $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Hm......"
                            $herViewHead.showQ( "body_90.png", posHead )
                            her "........"
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "\"B+\"!"
                            $herViewHead.showQ( "body_94.png", posHead )
                            her "!!!"
                            $herViewHead.hideQ()
                            m "Really?"
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes. I do give credit where it's due."
                            $herViewHead.showQ( "body_95.png", posHead )
                            her "(Professor...)"
                            $herViewHead.showQ( "body_102.png", posHead )
                            her "(Time for my finishing act then!)"
                            $herViewHead.hideQ()
                            pause.1
                            show screen blktone8
                            with d3
                            ">Hermione bends over and slides her panties down."
                            ">Her movements lack grace..."
                            ">But a pretty pussy is always a welcome sight nonetheless..."
                            hide screen blktone
                            with d3
                            $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes... Yes..."
                            sna2 "Now shake those B+ titties for me, you harlot!"
                            $herViewHead.showQ( "body_99.png", posHead )
                            her "......."
                            $herViewHead.hideQ()
                            show screen blktone8
                            with d3
                            ">Hermione suddenly breaks into a series of rather complex pirouettes."
                            $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes, such grace..."
                            $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "That lithe, young body!"
                            $herViewHead.showQ( "body_102.png", posHead )
                            her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}"
                            $herViewHead.hideQ()
                            ">Hermione seems very focused on her dancing routine..."
                            $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                            show screen s_head2
                            sna "Yes, and now another pirouette!"
                            sna "Magnificent!"
                            hide screen s_head2
                            show screen blkfade
                            with d3
                            ">Hermione performs another set of movements and pirouettes..."
                            ">Gives a little curtsy bow to the imaginary public..."
                            ">And then slumps down on her butt exhausted."
                            $ hermione_chibi_xpos = -210 #400 = Near the desk.
                            $ hermione_chibi_ypos = 10
                            $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                            show screen h_c_u
                            hide screen blkfade
                            with d3
                            hide screen blktone8
                            with d3
                            $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Good job, you harlot!"
                            $herViewHead.showQ( "body_105.png", posHead )
                            her "............."
                            if daytime:
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2                                                          #SNAPE
                                sna2 "Well, my class is about to start so I will be leaving now."
                                sna2 "Don't you have potion class with me today, MIss Granger?"
                                $herViewHead.showQ( "body_91.png", posHead )
                                her2 "Yes, sir..."
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2                                                          #SNAPE
                                sna2 "Well, don't be late, girl..."
                                hide screen s_head2      
                            else:
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2    
                                sna2 "Well, it is getting rather late. I think I will be leaving now."
                                sna2 "Good night, Albus."
                                hide screen s_head2    
                                m "Severus."
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2    
                                sna2 "Harlot."
                                $herViewHead.showQ( "body_91.png", posHead )
                                her2 "Professor..."
                                $herViewHead.hideQ()


                            show screen ctc
                            pause
                            show screen blkfade
                            hide screen s_c_u
                            hide screen ctc
                            with d5
                            ">Professor Snape leaves..."
                            $herViewHead.showQ( "body_91.png", posHead )
                            stop music fadeout 1.0
                            her "...................."
                            $herViewHead.hideQ()
                            pause.5
                            ">.................{w}.................{w}.................{w}................."
                            call req11_dress
                            $herViewHead.showQ( "body_33.png", posHead )
                            her "May I... may get paid now... sir...?"
                            $herViewHead.hideQ()


                "\"Nah... That's not a good idea...\"":
                    label no_snape_watching:  
                    hide screen blktone
                    with d3
                    m "Miss Granger, how about another strip?"     
                    $ pos = POS_140
                    $herView.showQQ( "body_66.png", pos )
                    her ".............."
                    her "I would really rather not, professor..."
                    m "Why? You are getting quite good at it."
                    $herView.hideshowQQ( "body_79.png", pos )
                    her "........................."
                    $herView.hideshowQQ( "body_87.png", pos )
                    her "Thirty five house points?"
                    m "Sure! The usual rate."
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "..................."
                    $herView.hideQQ()
                    hide screen bld1
                    with d3
                    pause
                    #Walks to the door
                    
                    $ walk_xpos=400 #Animation of walking chibi. (From) 400 = desk.
                    $ walk_xpos2=650 #Coordinates of it's movement. (To) 610 = door.
                    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                    show screen hermione_walk_01_f 
                    pause 2
                    hide screen hermione_walk_01_f 
                    $ hermione_chibi_xpos = 650 # Position of the chibi (Near the door).
                    $ h_c_u_pic = im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
                    show screen h_c_u
                    pause.5
                   
                    $ tt_xpos=670
                    $ tt_ypos=200
                    show screen thought 
                    with Dissolve(.3)
                    pause.5
                    hide screen thought
                    pause.5
                   
                    $ h_c_u_pic = im.Flip("03_hp/animation/h_walk_03.png", horizontal=True)
                    $ renpy.play('sounds/09_lock.wav') #Sound of a door opening.
                    pause.4
                    $ h_c_u_pic = im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
                    show screen ctc
                    pause
                    m "??!"
                    hide screen h_c_u
                    hide screen ctc
                    $ walk_xpos=650 #Animation of walking chibi. (From)
                    $ walk_xpos2=400 #Coordinates of it's movement. (To)
                    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                    show screen hermione_walk_01 
                    pause 3
                    $ hermione_chibi_xpos = 400 #Near the desk.
                    show screen hermione_02 #Hermione stands still.
                    show screen bld1
                    with Dissolve(.3)
                    $herView.showQQ( "body_69.png", pos )
                    her "Just in case..."
                    stop music fadeout 1.0
                    $herView.hideQ( d5 )

                    show screen blkfade
                    with Dissolve(1)
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 5
                    $ posHead = gMakePos( 390, 340 )

                    $herViewHead.showQ( "body_16.png", posHead )
                    her2 "Just for the record..."
                    her2 "I still consider this a highly inappropriate favour to be buying from one of your students, sir."
                    $herViewHead.hideQ()
                    m "Right. And an equally inappropriate favour to be selling to your headmaster. Woulnd't you agree?"
                    $herViewHead.showQ( "body_69.png", posHead )
                    her ".........."
                    $herViewHead.hideQ()
                    hide screen blkfade
                    hide screen bld1
                    $ hermione_chibi_xpos = 210 #Near the desk: 400.
                    $ hermione_chibi_ypos = 180 #Default: 250
                    show screen clothed_dance #Hermione stands still.
                    show screen ctc
                    with fade
                    pause
                    show screen no_vest_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    $herViewHead.showQ( "body_87.png", posHead )
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her ".............."
                    $herViewHead.addFaceName( "body_85.png" )
                    her2 "What if my parents were to find out about this, sir?"
                    her2 "Mother would never understand..."
                    $herViewHead.addFaceName( "body_44.png" )
                    her "As for my father..."
                    $herViewHead.hideQ()
                    menu:
                        m "..."
                        "{size=-3}\"Your father would be proud of you!\"{/size}":
                            $herViewHead.showQ( "body_44.png", posHead )
                            her "I doubt it..."
                            her "Yes, I am doing this for the right reasons, but..."
                            $herViewHead.showQ( "body_61.png", posHead )
                            her "He would never see it that way..."
                            her "He must never know about this..."
                            $herViewHead.hideQ()
                        "{size=-3}\"Your father would spank you hard!\"{/size}":
                            $herViewHead.showQ( "body_48.png", posHead )
                            her "He would not!"
                            $herViewHead.addFaceName( "body_44.png" )
                            her "And I am too old for that anyways..."
                            $herViewHead.hideQ()
                            g9 "I would say that you are in the perfect age for that..."
                            $herViewHead.showQ( "body_57.png", posHead )
                            her "Huh?"
                            her "I do not know what you mean, sir."
                            $herViewHead.hideQ()
                        "{size=-3}\"Your father would disown you!\"{/size}":
                            $herViewHead.showQ( "body_34.png", posHead )
                            her "You are probably right, sir..."
                            $herViewHead.addFaceName( "body_22.png" )
                            her "(Oh father, I am so sorry...)"
                            $herViewHead.addFaceName( "body_21.png" )
                            her "he must never find out..."
                            $herViewHead.hideQ()
                        "{size=-3}\"Your father love to would watch you strip!\"{/size}":
                            $herViewHead.showQ( "body_33.png", posHead )
                            her "He would not! He would be ashamed of me!"
                            $herViewHead.hideQ()
                            m "Are you sure about that?"
                            $herViewHead.showQ( "body_32.png", posHead )
                            her "absolutely! My father is a man of integrity!"
                            $herViewHead.hideQ()
                            m "But he {size=+4}is{/size} a {size=+4}man{/size}, right?"
                            $herViewHead.showQ( "body_50.png", posHead )
                            her "....................."
                            $herViewHead.addFaceName( "body_29.png" )
                            her "My father must never know about this..."
                            $herViewHead.hideQ()
                    show screen blktone
                    with d3
                    ">Hermione is starting to sway her hips rather seductively while she slides her skirt down..."
                    hide screen blktone
                    with d3
                    hide screen bld1
                    with d3
                    show screen ctc
                    pause
                    show screen no_skirt_dance
                    with d3
                    pause
                    hide screen ctc
                    show screen bld1
                    with d3
                    
                    $herViewHead.showQ( "body_31.png", posHead )
                    her "Professor?"
                    $herViewHead.hideQ()
                    m "Huh?"
                    $herViewHead.showQ( "body_44.png", posHead )
                    her "Can I ask you a question?"
                    $herViewHead.hideQ()
                    m "Go ahead..."
                    $herViewHead.showQ( "body_33.png", posHead )
                    her "..............."
                    $herViewHead.addFaceName( "body_57.png" )
                    her "Have you ever been in love...?"
                    $herViewHead.hideQ()
                    menu:
                        m "..."
                        "\"Don't be ridiculous! Love is a lie!\"":
                            $herViewHead.showQ( "body_29.png", posHead )
                            her "I am sorry you think that way, sir!"
                            $herViewHead.addFaceName( "body_50.png" )
                            her "But you couldn't be more wrong!"
                            $herViewHead.addFaceName( "body_54.png" )
                            her2 "I believe that true love is what makes the earth turn!"
                            $herViewHead.hideQ()
                            m "Actually the conservation of angular momentum is responsible for that."
                            $herViewHead.showQ( "body_44.png", posHead )
                            her "Huh?"
                            $herViewHead.hideQ()
                            m "Never mind. Just take off your shirt already?"
                            $herViewHead.showQ( "body_50.png", posHead )
                            her "............"      
                            $herViewHead.hideQ()
                        "\"Be quiet and keep on dancing!\"":
                            $herViewHead.showQ( "body_50.png", posHead )
                            her "But you said I could ask you a question..."
                            $herViewHead.hideQ()
                            m "And you did, didn't you?"
                            $herViewHead.showQ( "body_31.png", posHead )
                            her "!!!............"
                            $herViewHead.addFaceName( "body_50.png" )
                            her2 "...................................."
                            $herViewHead.hideQ()
                            m "Now, hush and take your shirt off."
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "........"
                            $herViewHead.hideQ()
                        "\"Yes... a very long time ago...\"":
                            $herViewHead.hideQ()
                            m "Yes... a very long time ago..."
                            $herViewHead.showQ( "body_31.png", posHead )
                            her2 "!!!!!??.............................."
                            $herViewHead.hideQ()
                            m "Her name was Eden..."
                            $herViewHead.showQ( "body_45.png", posHead )
                            her "Was she beautiful?"
                            $herViewHead.hideQ()
                            m "She was so much more than that..."
                            m "She was smart, green and perfect..."
                            $herViewHead.showQ( "body_87.png", posHead )
                            her "She was... \"green\"...?"
                            $herViewHead.addFaceName( "body_47.png" )
                            her2 "Are you making fun of me, sir?"
                            $herViewHead.hideQ()
                            m "Oh, you humans know nothing of true love..."
                            $herViewHead.showQ( "body_55.png", posHead )
                            her ".....................................?"
                            $herViewHead.hideQ()
                            m "Err... I mean, take off that shirt, girl!"
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "................."
                            $herViewHead.hideQ()
                        "\"I feel like I'm in love right now!\"":
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "You don't have to be vulgar, sir."
                            $herViewHead.hideQ()
                            m "Oh, but I mean it!"
                            $herViewHead.showQ( "body_66.png", posHead )
                            her "Sir, please!"
                            $herViewHead.addFaceName( "body_55.png" )
                            her "I am one of your students!"
                            $herViewHead.addFaceName( "body_57.png" )
                            her "And you are older than my father!"
                            $herViewHead.hideQ()
                            m "{size=-4}(You have no idea, girl.){/size}"
                            $herViewHead.showQ( "body_55.png", posHead )
                            her2 "Although some scientists insist that what we consider \"love\" is actually nothing but a chemical reaction..."
                            $herViewHead.addFaceName( "body_16.png" )
                            her2 "And when a man is experiencing sexual arousal, the same type of hormones--"
                            $herViewHead.hideQ()
                            m "Miss granger!"
                            $herViewHead.showQ( "body_15.png", posHead )
                            her "Yes, sir?"
                            $herViewHead.hideQ()
                            m "Did you forget where you are?"
                            $herViewHead.showQ( "body_24.png", posHead )
                            her "Oh, my apologies, sir... I get distracted sometimes."
                            $herViewHead.hideQ()
                            m "Take off your shirt already, would you?!"
                            $herViewHead.showQ( "body_29.png", posHead )
                            her "Right..."
                            $herViewHead.hideQ()
                    show screen blktone
                    with d3
                    ">Hermione undoes the last button of her shirt and takes it off somewhat gracefully..."
                    hide screen blktone
                    with d3
                    hide screen bld1
                    with d3
                    show screen ctc
                    pause
                    show screen no_shirt_no_skirt_dance
                    with d3
                    pause
                    hide screen ctc
                    show screen bld1
                    with d3
                    g9 "Yes! The tits!"
                    
                    
                    
                    $ posHead = gMakePos( 390, 235 )
                    $herViewHead.data().hideItemKey('dress')
                    $herViewHead.showQ( "body_90.png", posHead )
                    her "Must you be so vulgar, sir?"
                    $herViewHead.hideQ()
                    menu: 
                        "-Take your cock out, start jerking off-":
                            hide screen bld1
                            show screen ctc
                            with d3
                            pause
                            show screen blkfade
                            with d6
                            $herViewHead.showQ( "body_94.png", posHead )
                            her "Professor Dumbledore?!"
                            $herViewHead.hideQ()
                            m "It's alright, girl. Don't mind me..."
                            
                            
                            hide screen genie
                            hide screen no_shirt_no_skirt_dance
                            $ genie_chibi_xpos = -185
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "jerking_off_02_ani"
                            show screen chair_02
                            show screen g_c_u
                            show screen desk_02
                            show screen no_shirt_no_skirt_dance
                            hide screen blkfade
                            with fade
                            pause
                            show screen bld1
                            with d3
                            $herViewHead.showQ( "body_95.png", posHead )
                            her "B-but..."
                            her "Your..."
                            $herViewHead.hideQ()
                            m "Yes... Ah, yes, this is good..."
                            $herViewHead.showQ( "body_98.png", posHead )
                            her "Professor!!!"
                            her "I must insist that you put away your..."
                            $herViewHead.addFaceName( "body_99.png" )
                            her "...thing."
                            $herViewHead.hideQ()
                            menu:
                                m "..."
                                "\"I said, keep on dancing, girl!\"":
                                    if hermi.whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        $herViewHead.showQ( "body_99.png", posHead )
                                        her "But..."
                                        her "............................."
                                        $herViewHead.addFaceName( "body_101.png" )
                                        her2 "Well, alright, but only if you will promise me not to....finish, sir."
                                        $herViewHead.hideQ()
                                        menu:
                                            m "..."
                                            "-Promise her to hold it-":
                                                    $ d_flag_07 = True #Promised to hold it.
                                                    $herViewHead.showQ( "body_102.png", posHead )
                                                    her "Well, alright then..."
                                                    $herViewHead.hideQ()
                                            "-Give her no such promise-":
                                                $ d_flag_07 = False #Did not promise to hold it.
                                                m "\"Not to finish\"? That would be like torture!"
                                                m "Please keep your sadistic urges to yourself, miss granger."
                                                $herViewHead.showQ( "body_103.png", posHead )
                                                her2 "I don't have any... sadistic urges, sir!"
                                                her "I just don't want to..."
                                                $herViewHead.hideQ()
                                                g9 "Yes... Those are some nice tits you have..."
                                                $herViewHead.showQ( "body_97.png", posHead )
                                                her "............"
                                                $herViewHead.hideQ()
                                                g9 "A-ah... Yes..."
                                                $herViewHead.showQ( "body_97.png", posHead )
                                                her ".........."
                                                $herViewHead.addFaceName( "body_99.png" )
                                                her "Fine! Have it your way, sir!"
                                                $herViewHead.addFaceName( "body_103.png" )
                                                her "{size=-5}(As usual...){/size}"
                                                $herViewHead.hideQ()
                                        show screen blktone
                                        with d3
                                        ">You keep on wanking while you watch Hermione's dance..."
                                        $herViewHead.showQ( "body_90.png", posHead )
                                        her "Time for the finishing act I suppose..."
                                        $herViewHead.hideQ()
                                        m "Yes, girl! Take them off!"
                                        $herViewHead.showQ( "body_91.png", posHead )
                                        her "........"
                                        $herViewHead.hideQ()
                                        show screen blktone8
                                        with d3
                                        ">Hermione bends over slightly and slides her panties down..."
                                        ">You can see that she is doing her best to be graceful..."
                                        ">But she looks rather ridiculous in her attempts to act like a professional stripper..."
                                        hide screen blktone8 
                                        hide screen blktone
                                        with d3
                                        hide screen bld1
                                        with d3
                                        pause
                                        $ h_c_u_pic = "no_panties_dance_ani"
                                        hide screen no_shirt_no_skirt_dance
                                        show screen h_c_u
                                        with d3
                                        pause
                                        show screen bld1
                                        with d3
                                        show screen blktone
                                        with d3
                                        ">Nonetheless you decide to show her some appreciation..."
                                        ">By stroking your cock even faster!"
                                        $herViewHead.showQ( "body_91.png", posHead )
                                        her ".........."
                                        $herViewHead.hideQ()
                                        show screen blktone8
                                        with d3
                                        ">Suddenly Hermione breaks into a whole series of rather complex pirouettes..."
                                        m "{size=-4}(This looks quite impressive actually...){/size}"
                                        ">Hermione gives her breasts a squeeze followed by another series of rather complex (and naughty) movements..."
                                        m "{size=-4}(Did she practice this?){/size}"
                                        g9 "Oh, what do I care?"
                                        ">You stroke your diamond-hard cock furiously."
                                        $herViewHead.showQ( "body_102.png", posHead )
                                        her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}"
                                        $herViewHead.hideQ()
                                        ">Hermione performs another set of movements that could be considered classy..."
                                        ">if not for her naked tits bouncing all over the place..."
                                        g9 "Yes, yes, you little whore!"
                                        ">A few more movements, a couple of gestures and a little curtsy bow to the imaginary public..."
                                        show screen blkfade
                                        with d3
                                        $ hermione_chibi_xpos = -210 #400 = Near the desk.
                                        $ hermione_chibi_ypos = 10
                                        $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                        ">And then Hermione slumps on her butt, completely exhausted."
                                        hide screen blktone
                                        with d3
                                        hide screen blktone8
                                        with d3
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1 
                                        with d3
                                        pause
                                        $herViewHead.showQ( "body_102.png", posHead )
                                        her "Whew... This was--"
                                        $herViewHead.hideQ()
                                        with hpunch
                                        g4 "ARGH! YOU FUCKING CUNT!"
                                        $herView.hideQQ()
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ genie_chibi_xpos = -210
                                        $ genie_chibi_ypos = 10
                                        $ genie_cum_chibi_xpos =  -210
                                        $ genie_cum_chibi_ypos  = 10
                                        $ g_c_c_u_pic = "genie_cum_03"
                                        $ h_c_u_pic = "03_hp/08_animation_02/08_sits_02.png"
                                        show screen g_c_c_u
                                        pause
                                        
                                        #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, 'sperm_01.png', G_Z_FACE + 1 ) )
                                        $herViewHead.data().addItem( 'item_sperm', '01' )
                                        $herViewHead.showQ( "body_104.png", posHead )
                                        her "??!!!"
                                        $herViewHead.hideQ()
                                        show screen bld1
                                        with d3
                                        $herViewHead.showQ( "body_97.png", posHead )
                                        her "Professor!!!"
                                        $ g_c_c_u_pic = "03_hp/08_animation_02/09_cum_18.png"
                                        $herViewHead.hideQ()
                                        if d_flag_07: #Promised to hold it.
                                            $herViewHead.showQ( "body_97.png", posHead )
                                            her "No, professor! You promised!"
                                            $herViewHead.hideQ()
                                            g4 "Oh, man... This was pretty intense..."
                                            $herViewHead.showQ( "body_98.png", posHead )
                                            her "You went back on your word, sir!"
                                            $herViewHead.hideQ()
                                            m "Ah? What are you talking about?"
                                            $herViewHead.showQ( "body_113.png", posHead )
                                            her "How could you do this to me, sir?"
                                            $herViewHead.hideQ()
                                            m "Oh, calm down, girl."
                                            m "You earned your points today."
                                            m "Now, just get dressed and leave before somebody discovers you like this."
                                            $herViewHead.showQ( "body_114.png", posHead )
                                            her "*sob!*........................"
                                            $herViewHead.hideQ()
                                            $ hermi.liking -= 50
                                            show screen blkfade 
                                            with d3
                                            
                                            $herViewHead.data().delItem( 'item_sperm' )
                                            #$herViewHead.data().addItemKey( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                            $herViewHead.data().addItem( 'item_sperm_dried' )
                                            stop music fadeout 5.0
                                            ">.................{w}.................{w}.................{w}................."
                                            call req11_dress
                                            $herViewHead.showQ( "body_12.png", posHead )
                                            her "...Can I just get paid now, Sir... please?"
                                            $herViewHead.hideQ()
                                            jump done_with_dancing
                                        else:
                                            $herViewHead.showQ( "body_97.png", posHead )
                                            her "it's so hot..."
                                            $herViewHead.hideQ()
                                            $ g_c_u_pic = "03_hp/08_animation_02/06_jerking_01.png" # Genie stands still with his dick in hand.
                                            m "Aha... Yeah... This feels great..."
                                            $herViewHead.showQ( "body_105.png", posHead )
                                            her "You came all over me..."
                                            her "I am your pupil and..."
                                            $herViewHead.showQ( "body_106.png", posHead )
                                            her "You just cum at me..."
                                            $herViewHead.hideQ()
                                            g9 "I know! Pretty cool, huh?!"
                                            $herViewHead.showQ( "body_107.png", posHead )
                                            her "Nothing of that sort!"
                                            #her "You should not have done this, sir!"
                                            her2 "You should have restrained yourself like a proper headmaster would!"
                                            $herViewHead.hideQ()
                                            m "Really? What did you expect me to do?"
                                            m "Aim at the wall or just put it back in my pants and start cumming?"
                                            $herViewHead.showQ( "body_105.png", posHead )
                                            her "........"
                                            $herViewHead.showQ( "body_101.png", posHead )
                                            her "Still, you should not have..."
                                            $herViewHead.showQ( "body_102.png", posHead )
                                            her "I agreed to perform a striptease for you..."
                                            her2 "But I didn't agree to be defiled like this."
                                            $herViewHead.hideQ()
                                            m "I think I know where this is going..."
                                            $herViewHead.showQ( "body_100.png", posHead )
                                            her "I demand to be paid extra!"
                                            $herViewHead.hideQ()
                                            m "Of course you do..."
                                            menu:
                                                m "..."
                                                "\"You get 1 extra point.\"":
                                                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                                    $herViewHead.showQ( "body_101.png", posHead )
                                                    her "One extra point?"
                                                    $herViewHead.addFaceName( "body_98.png" )
                                                    her2 "One meagre extra point for letting you do this to me?"
                                                    $herViewHead.addFaceName( "body_101.png" )
                                                    her "Now, that is just insulting, sir!"
                                                    $herViewHead.hideQ()
                                                    m "One extra point, miss Granger. Take it or leave it."
                                                    $herViewHead.showQ( "body_103.png", posHead )
                                                    her "............."
                                                    $herViewHead.addFaceName( "body_101.png" )
                                                    her "I'll take it."
                                                    $herViewHead.hideQ()
                                                    $ hermi.liking -= 30
                                                    $ current_payout = 36
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    
                                                    #$herView.data().addItemKey( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                                    $herView.data().addItem( 'item_sperm_dried' )
                                                    jump done_with_dancing
                                                "\"You get 10 extra points.\"":
                                                    $ current_payout = 45
                                                    $herViewHead.showQ( "body_101.png", posHead )
                                                    her "Ten extra points sir?"
                                                    her "But that is not even nearly enough!"
                                                    $herViewHead.hideQ()
                                                    m "Ten extra points. Take'em or leave'em miss Granger."
                                                    $herViewHead.showQ( "body_103.png", posHead )
                                                    her "..............."
                                                    $herViewHead.showQ( "body_101.png", posHead )
                                                    her "Well, alright... Better than nothing I suppose..."
                                                    $herViewHead.hideQ()
                                                    $ hermi.liking -= 11
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    
                                                    #$herView.data().addItemKey( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                                    $herView.data().addItem( 'item_sperm_dried' )
                                                    jump done_with_dancing
                                                "\"You get 25 extra points.\"":
                                                    $ current_payout = 60
                                                    $herViewHead.showQ( "body_102.png", posHead )
                                                    her2 "Yes, I believe this would be an appropriate amount."
                                                    $herViewHead.hideQ()
                                                    m "are we good then?"
                                                    $herViewHead.showQ( "body_102.png", posHead )
                                                    her "Yes, sir. Thank you sir."
                                                    $herViewHead.hideQ()
                                                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    
                                                    #$herView.data().addItemKey( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                                    $herView.data().addItem( 'item_sperm_dried' )
                                                    jump done_with_dancing
                                                "\"You get 50 extra points.\"":
                                                    $ current_payout = 85
                                                    $herViewHead.showQ( "body_95.png", posHead )
                                                    her "Seriously?!"
                                                    $herViewHead.addFaceName( "body_94.png" )
                                                    her "Oh, I don't know what to say..."
                                                    $herViewHead.hideQ()
                                                    m "I enjoyed your performance miss Granger."
                                                    $herViewHead.showQ( "body_109.png", posHead )
                                                    her "Thank you sir..."
                                                    $herViewHead.hideQ()
                                                    m "I also enjoyed plastering your agile little body with cum..."
                                                    $herViewHead.showQ( "body_108.png", posHead )
                                                    her "Sir......"
                                                    $herViewHead.hideQ()
                                                    m "So, just allow me to show my appreciation."
                                                    m "Fifty extra points. Well deserved, miss Granger."
                                                    $herViewHead.showQ( "body_108.png", posHead )
                                                    her "Thank very much, sir."
                                                    $herViewHead.hideQ()
                                                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    
                                                    #$herView.data().addItemKey( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                                    $herView.data().addItem( 'item_sperm_dried' )
                                                    jump done_with_dancing
                                                "\"You're not getting shit!\"":
                                                    stop music fadeout 1.0
                                                    $herViewHead.showQ( "body_104.png", posHead )
                                                    her "What? Not even my usual pay?"
                                                    $herViewHead.hideQ()
                                                    menu:
                                                        m "..."
                                                        "\"Oh, no, you are still getting that.\"":
                                                            $ hermi.liking -= 30
                                                            $herViewHead.showQ( "body_101.png", posHead )
                                                            her "How generous of you, sir." 
                                                            $herViewHead.hideQ()
                                                            hide screen bld1
                                                            with d3
                                                            pause
                                                            show screen blkfade
                                                            with d7
                                                            pause.5
                                                            
                                                            #$herView.data().addItemKey( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                                            $herView.data().addItem( 'item_sperm_dried' )
                                                            jump done_with_dancing
                                                        "\"No, not even that!\"":
                                                            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                                            $herViewHead.showQ( "body_104.png", posHead )
                                                            her "!!!?"
                                                            her "I danced for you, sir..."
                                                            $herViewHead.addFaceName( "body_105.png" )
                                                            her "I degraded myself for your amusement..."
                                                            $herViewHead.addFaceName( "body_107.png" )
                                                            her "I let you cum on me..."
                                                            $herViewHead.addFaceName( "body_110.png" )
                                                            with hpunch
                                                            her "And I get NOTHING?!"
                                                            $herViewHead.hideQ()
                                                            m "You are dismissed, miss Granger!"
                                                            $herViewHead.showQ( "body_101.png", posHead )
                                                            her "Oh, this is a new low even for you, sir!"
                                                            $herViewHead.hideQ()
                                                            m "I said you are dismissed."
                                                            $herViewHead.showQ( "body_110.png", posHead )
                                                            her "*GROAN!*"
                                                            $ hermi.liking -= 90
                                                            $herViewHead.hideQ()
                                                            hide screen bld1
                                                            with d3
                                                            pause
                                                            show screen blkfade
                                                            with d7
                                                            pause.5
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
                                                            call music_block
                                                            jump restore_state_could_not_flirt #Leaves without getting any очков.
                                                        

                                    else: # You jerk off your cock and Hermione is NOT OK with it.
                                        $herViewHead.showQ( "body_103.png", posHead )
                                        stop music fadeout 1.0
                                        her "No, sir!"
                                        $herViewHead.hideQ()
                                        m "Huh?"
                                        show screen blkfade
                                        with d7
                                        ">Hermione jumps off your desk and starts to put her clothes back on while glaring at you..."
                                        m "Oh, come on! Don't leave me like that!"
                                        $ posHead = gMakePos( 390, 340 )
                                        $herViewHead.showQ( "body_101.png", posHead )
                                        her "The dance is over sir!"
                                        $herViewHead.hideQ()
                                        pause 1
                                        call req11_dress
                                        $herViewHead.showQ( "body_79.png", posHead )
                                        her "I would like to get paid now!"
                                        $herViewHead.hideQ()
                                        m "Stubborn girl..."
                                        ">You reluctantly put your cock away..."
                                        $herViewHead.showQ( "body_79.png", posHead )
                                        her "I would like to get paid now."
                                        $herViewHead.hideQ()
                                        jump done_with_dancing
                                "\"Fine. There is no need for drama!\"": 
                                    $herViewHead.showQ( "body_103.png", posHead )
                                    her2 "......................"
                                    $herViewHead.hideQ()
                                    pause.1
                                    hide screen no_shirt_no_skirt_dance
                                    show screen genie
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk_02
                                    show screen no_shirt_no_skirt_dance
                                    hide screen blkfade
                                    with fade
                                    pause
                                    show screen bld1
                                    with d3
                                    pass

                        "-Show some manners, just watch-":
                            pass
                    # JUST WATCHING.
                    show screen blktone
                    with d3
                    ">You watch Hermione Dance..."
                    $herViewHead.showQ( "body_97.png", posHead )
                    her "(Time for the finishing act I suppose...)"
                    $herViewHead.hideQ()
                    m "Yes, girl! Take them off!"
                    $herViewHead.showQ( "body_90.png", posHead )
                    her "........"
                    $herViewHead.hideQ()
                    show screen blktone8
                    with d3
                    ">Hermione bends over slightly and slides her panties down..."
                    ">You can see that she is doing her best to be graceful..."
                    ">But she looks rather ridiculous in her attempts to act like a professional stripper..."
                    $herViewHead.showQ( "body_109.png", posHead )
                    her ".........."
                    $herViewHead.hideQ()
                    ">Suddenly Hermione breaks into a whole series of rather complex pirouettes..."
                    $herViewHead.hideQ()
                    m "{size=-4}(This looks quite impressive actually...){/size}"
                    ">Hermione gives her breasts a squeeze followed by another series of rather complex (and naughty) movements..."
                    m "{size=-4}(Did she practice this?){/size}"
                    g9 "Oh, why would I care?"
                    $herViewHead.showQ( "body_102.png", posHead )
                    her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}"
                    $herViewHead.hideQ()
                    ">Hermione performs another set of movements that could be considered classy if not for her naked tits bouncing all over the place..."
                    g9 "Yes, yes, you little harlot!"
                    
                    show screen blkfade
                    with d3
                    $ hermione_chibi_xpos = -210 #400 = Near the desk.
                    $ hermione_chibi_ypos = 10
                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                    ">A few more movements, a couple of gestures and a little curtsy bow to the imaginary audience and Hermione slumps on her butt completely exhausted."
                    show screen h_c_u
                    hide screen blktone
                    with d3
                    hide screen blktone8
                    with d3
                    hide screen blkfade
                    with d3
                    hide screen bld1 
                    with d3
                    pause
                    $herViewHead.showQ( "body_108.png", posHead )
                    show screen bld1
                    with d3
                    her "Whew... This was rather exciting..."
                    $herViewHead.hideQ()
                    menu:
                        m "..."
                        "{size=-3}\"Good job, girl! You sure know how to dance!\"{/size}":
                            m "Good job girl!"
                            $herViewHead.showQ( "body_109.png", posHead )
                            her "Really?"
                            $herViewHead.hideQ()
                            m "Yes! You have a lot of talent for this!"
                            $herViewHead.showQ( "body_108.png", posHead )
                            her "Thank you sir."
                            $herViewHead.hideQ()
                        "{size=-3}\"Hm... This was quite awful...\"{/size}":
                            $herViewHead.showQ( "body_105.png", posHead )
                            her "Oh... I'm sorry..."
                            $herViewHead.hideQ()
                            m "That's OK... You just need to practice more..."
                            $herViewHead.showQ( "body_107.png", posHead )
                            her "Em... I will keep that in mind, sir..."
                            $herViewHead.hideQ()
                        "{size=-3}\".................................................\"{/size}":
                            $herViewHead.showQ( "body_108.png", posHead )
                            her "......................."
                            $herViewHead.hideQ()

                    
                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                    hide screen bld1
                    show screen ctc
                    with d3
                    pause
                    show screen blkfade
                    with d7
                    pause.5

                            
        else: #Stripping only for Genie.
            jump no_snape_watching 

        
        

    label done_with_dancing:
    call req11_dress
    $herView.data().delItem( 'item_sperm' )
    
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
    $herViewHead.hideQ()
    $herView.hideQ()
    hide screen blkfade
    with d3
    
    
    m "Yes, miss Granger. [current_payout] to the \"Gryffindor\" house." 
    $ pos = POS_140
    $herView.showQ( "body_13.png", pos )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    
    her "Thank you, sir..."

    if hermi.whoring <= 11:
        $ hermi.whoring +=1

#    $ request_11_points += 1
    



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

    $event.Finalize()    
    $SetHearts(GetStage(event._finishCount,1,3,1))

    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu       


label restore_state_could_not_flirt:
    $herView.data().loadState()
    jump could_not_flirt

label req11_undress:
    $herView.data().hideItemKey( 'dress' )
    $herView.data().hideItemKey( 'skirt' )
    $herView.data().hideItemKey( 'panties' )
    return
    
label req11_dress:
    $herView.data().showItemKey( 'dress' )
    $herView.data().showItemKey( 'skirt' )
    $herView.data().showItemKey( 'panties' )
    return
