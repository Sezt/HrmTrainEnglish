
    
###################REQUEST_23 (Level 06) (55 pt.) (Give handjob to a classmate). (Available during daytime only).#####################################################################################
label new_request_23: #LV.6 (Whoring = 15 - 17)
    
    $ current_payout = 55 #Used when haggling about price of the favour.
    
    $herView.hideQQ()
    m "{size=-4}(Tell her to give a handjob to one of her classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request
            
    
    $ pos = POS_140
    
    if request_23_points == 0: # <================================================================================ FIRST TIME
        if whoring <=14 or request_20_points <= 1: # Counts how many times you sent Hermione to kiss a girl.
            m "Miss Granger, I want you to do something different today..."
            $herView.hideshowQQ( "body_07.png", pos )
            her "...?"
            m "I want you to give a handjob to one of your classmates."
            jump too_much
        m "Miss Granger, I want today, you did something different..."
        $herView.hideshowQQ( "body_15.png", pos )
        her "..........."
        m "I want you to go out there and have sex with one of your classmates."
        stop music
        $herView.hideshowQQ( "body_48.png", pos )
        with hpunch                                                                                                                                                                                                               #HERMIONE
        her "{size=+5}What?!!{/size}"
        $herView.hideshowQQ( "body_47.png", pos )
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "Now you have done it, sir! You crossed the line!"
        her "I know I did sell you a couple of rather questionable favours in the past..."
        $herView.hideshowQQ( "body_86.png", pos )
        with vpunch
        her "{size=+5}But THIS?!{/size}"
        her "I cannot believe that you would ask one of your pupils to... to..."
        $herView.hideshowQQ( "body_76.png", pos )
        her "We are done here, sir!"
        m "Alright, alright, calm down, would you?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "I most certainly would not, sir! This is beyond inappropriate!"
        m "Alright, fine, maybe I really did cross some sort of line this time..."
        $herView.hideshowQQ( "body_47.png", pos )
        her "You think sir?! You think!!?"
        m "Yes, I apologize..."
        $herView.hideshowQQ( "body_79.png", pos )
        her "........."
        m "How about we try something less... engaging instead?"
        $herView.hideshowQQ( "body_120.png", pos )
        her "............"
        m "I'll be willing to grant \"Gryffindor\" fifty five points."
        m "All I ask in return is..."
        $herView.hideshowQQ( "body_187.png", pos )
        her "..........?"
        m "...that you go out there and give some lucky boy a handjob..."
        $herView.hideshowQQ( "body_47.png", pos )
        her "!!!......"
        m "Oh, come on... Just a harmless handjob"
        $herView.hideshowQQ( "body_66.png", pos )
        her "..."
        m "Fifty five house points..."
        $herView.hideshowQQ( "body_69.png", pos )
        her ".............."
        $herView.hideshowQQ( "body_79.png", pos )
        her "I am glad that you came to your senses, sir."
        m "Oh, but of course. Thank you for keeping me in check."
        m "Are you up for it then?"
        $herView.hideshowQQ( "body_69.png", pos )
        her "I am willing to give it a try..."
        m "Splendid... See you tonight then."

    else: # <================================================================================ NOT FIRST TIME
        if whoring >= 15 and whoring <= 17: # LEVEL 06 FIRST EVENT.
            m "Today's favour shall be..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "........."
            m "A Handjob to the boy of your choosing!"
            $herView.hideshowQQ( "body_118.png", pos )
            her "...again?"
            m "Sure, why not?"
            m "And another fifty five house points for the \"Gryffindor\" house of course."
            $herView.hideshowQQ( "body_29.png", pos )
            her ".........."
            m "So... Are you up for that, girl?"
            $herView.hideshowQQ( "body_69.png", pos )
            her "I will see what I can do..."
            m "Splendid!"
        
        elif whoring >= 18 and whoring <= 20: # LEVEL 07
            m "Ready to go have sex with one of your classmates yet?"
            $herView.hideshowQQ( "body_72.png", pos )
            stop music fadeout 1.0
            her "What?"
            $herView.hideshowQQ( "body_30.png", pos )
            her "Of course not! I would never--"
            m "How about a handjob then?"
            $herView.hideshowQQ( "body_69.png", pos )
            her "..............."
            m "Oh come on. You did it before."
            $herView.hideshowQQ( "body_79.png", pos )
            her "hm.........."
            her "Fifty five house points?"
            m "Naturally."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Well, alright... I'll see what I can do..."

        elif whoring >= 21: # LEVEL 08+
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Miss Granger..."
            m "What do you think about giving one of your classmates another handjob?"
            $herView.hideshowQQ( "body_71.png", pos )
            her "I don't mind, sir."
            m "Really?"
            $herView.hideshowQQ( "body_68.png", pos )
            her "Yes... I mean, it's just a handjob..."
            m "Great. Go have fun then!"
            m "And report back to me after your classes, as usual."
            $herView.hideshowQQ( "body_74.png", pos )
            her "Of course, sir."
    
    
    

    
    $ request_23 = True

    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    call music_block
    
    $ hermione_takes_classes = True
    jump day_main_menu
    


label new_request_23_complete: # <=================================================================================================== EVENING
    
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ pos = POS_370
    $ herView.data().saveState()

    if whoring >= 15 and whoring <= 17: # LEVEL 06                    
        if one_out_of_three == 1: ### EVENT (A)
            m "Miss Granger, how was it?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_09.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "Quite awful... of course..."
            m "Just tell me what happened, girl..."
            $herView.hideshowQQ( "body_66.png", pos )
            her "I made a complete fool out of myself, that's what happened, sir."
            her "....."
            m "..."
            $herView.hideshowQQ( "body_29.png", pos )
            her ".........."
            $herView.hideshowQQ( "body_69.png", pos )
            her "I don't want to talk about it..."
            her "You told me to go and touch a boy's penis and I did just that, professor."
            $herView.hideQQ()

            $herView.showQQ( "body_31.png", pos )
            her "Please, just let me have my points now, sir..."
            m "I did not tell you to \"go and touch a boy's penis\", girl."
            m "I told you to give one of your classmates a proper handjob."
            $herView.hideshowQQ( "body_79.png", pos )
            her "Well, yes... that was what I meant of course..."
            m "Did you make him cum, then?"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Sir?"
            m "Did his \"wee-wee\" shoot white stuff at you, girl?"
            $herView.hideshowQQ( "body_29.png", pos )
            her "Well..."
            $herView.hideshowQQ( "body_33.png", pos )
            her "No, it did not..."
            menu: 
                "\"Well, this doesn't count then.\"":
                    stop music fadeout 4.0
                    $herView.hideshowQQ( "body_119.png", pos )
                    her "What?"
                    her "But, sir, I..."
                    m "If you didn't make him cum then that wasn't a proper handjob. Period."
                    $herView.hideshowQQ( "body_117.png", pos )
                    her "But... But what was it then...?"
                    m "How should I know? A cock massage?"
                    $herView.hideQQ()

                    $ pos = POS_140
                    $herView.showQQ( "body_118.png", pos )
                    her "Aww..."
                    her "But I really tried my best..."
                    m "No handjob - no payment, miss granger."
                    $herView.hideshowQQ( "body_117.png", pos )
                    her "....."
                    m "You are free to go, girl."
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "........."
                    $ mad +=9
                    $ request_23_points += 1 
                    $ request_23 = False 
                    $ hermione_sleeping = True
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                "\"You shall only get half the payment then.\"":
                    $ current_payout = 27 #Used when haggling about price of th favour.
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "Oh...?"
                    m "Is that a Problem, miss Granger?"
                    $herView.hideshowQQ( "body_118.png", pos )
                    her "No sir... It's only fair I suppose..."
                    m "Of course it is!"
                "\"Well, you did try. Here are the points.\"":
                    $herView.hideshowQQ( "body_117.png", pos )
                    her "Really?"
                    $herView.hideshowQQ( "body_87.png", pos )
                    her "Thank you, sir!"
                    $herView.hideshowQQ( "body_45.png", pos )
                    her "I promise, I will try harder next time!"
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "Ehm... Should you request a similar favour in the future, I mean..."

        elif one_out_of_three == 2: ### EVENT (B)
            m "Miss Granger, how did it go?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_31.png", pos )
            her "It went well, sir..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "I asked one if the \"Gryffindor\" boys to let me do \"it\" to him..."
            $herView.hideshowQQ( "body_183.png", pos )
            her "To my surprise he agreed eagerly."
            m "Shocker..."
            $herView.hideshowQQ( "body_127.png", pos )
            her "So we hid behind one of those huge tapestries in the east wing..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "And I... wanked him until he came..."
            her "........."
            $herView.hideshowQQ( "body_117.png", pos )
            her "And I asked him to keep the whole thing a secret, but..."
            m "What's the matter, girl?"
            m "Doubting the honesty of your fellow \"Gryffindors\"?"
            $herView.hideshowQQ( "body_120.png", pos )
            her "Of course not, sir."
            $herView.hideshowQQ( "body_118.png", pos )
            her "..........................."
            $herView.hideshowQQ( "body_117.png", pos )
            her "Still... Performing this sort of task could really damage my reputation..."
            m "Is this your way of asking for a raise, girl?"
            m "Fifty Five points is as high as I can go with this one."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Oh... Of course..."
            m "Unless, you've changed your mind about having sex with one of your classmates?"
            $herView.hideshowQQ( "body_48.png", pos )
            her "What?"
            $herView.hideshowQQ( "body_118.png", pos )
            her "Sir, I am not a prostitute!"
            m "Well, in that case..."
            
        elif one_out_of_three == 3: ### EVENT (C) Event level: 01.
            # HERMIONE HAVE A CUM-STAIN ON HER SHOULDER.
            m "Miss Granger, how did it go?"
            #$herView.data().addItemKey( 'sperm', CharacterExItem( herView.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
            $herView.data().addItem( 'item_sperm', '05' )
            #$herView.data().addItemKey( 'sperm_after', CharacterExItem( herView.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 2 ) )
            $herView.data().addItem( 'item_sperm_dried' )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_32.png", pos )
            her "Awful, sir. Simply awful..."
            m "You've got something... in your hair there..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Huh?"
            $herView.hideshowQQ( "body_189.png", pos )
            her "Oh, no! I thought I got it all off..."
            show screen ctc
            pause
            show screen blkfade 
            with d3
            pause.5
            $herView.data().delItem( 'sperm' )
            $herView.addFaceName( "body_120.png" )
            hide screen blkfade
            with d3
            pause
            hide screen ctc
            m "Hm... So I suppose you have completed your task?"
            $herView.hideshowQQ( "body_69.png", pos )
            her "I did, sir..."
            m "What's the problem, then?"
            $herView.hideshowQQ( "body_29.png", pos )
            her ".........."
            $herView.hideshowQQ( "body_30.png", pos )
            her "All boys are jerks! That is the problem, sir!"
            $herView.hideshowQQ( "body_87.png", pos )
            her "I gave this one boy a good wanking..."
            her "And do you know how he thanked me?"
            $herView.hideshowQQ( "body_86.png", pos )
            her "He got his spunk allover me..."
            $herView.hideshowQQ( "body_30.png", pos )
            her "And he did that on purpose, I know he did!"
            $herView.hideshowQQ( "body_29.png", pos )
            her "Nasty, good for nothing \"ravenclaws\"..."
            m "Well, I'd say a job well done."
            

    elif whoring >= 18 and whoring <= 20: # LEVEL 07                    
        if one_out_of_three == 1: ### EVENT (A)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_31.png", pos )
            her "Ehm..."
            her "Not yet, sir..."
            m "Not yet?"
            $herView.hideshowQQ( "body_29.png", pos )
            her "Yes... Let me explain, sir..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "uhm... Well..."
            her "I was wanking this one boy off in one of the empty classrooms..."
            her "And that nasty ghost Peeves walked in..."
            $herView.hideshowQQ( "body_29.png", pos )
            her "Or rather flew in on us..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "And as soon as he realized what I was doing to the boy..."
            her "He started to yell obscenities at us..."
            her "So we had to leave in a hurry..."
            m "I see..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "That is not all, sir..."
            m "Go on..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "Well, I sort of made a promise to the boy..."
            her "I promised to meet him after my classes and..."
            $herView.hideshowQQ( "body_79.png", pos )
            her "...and finish what I have started..."
            m "I see..."
            m "Did you?"
            $herView.hideshowQQ( "body_117.png", pos )
            her "No, sir. Not yet..."
            her "I am going to meet him as soon as we are done here, sir."
            m "Hm..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "So if you could just give those points in advance..."
            her "I would go meet with the boy right away and..."
            $herView.hideshowQQ( "body_189.png", pos )
            her "And give him a proper handjob..."
            menu:
                "\"No. You failed this favour, girl.\"":
                    stop music fadeout 3.0
                    $herView.hideshowQQ( "body_183.png", pos )
                    her "B-but..."
                    $herView.hideshowQQ( "body_119.png", pos )
                    her "But I gave him my word..."
                    her "I swore on Godric Gryffindor's name..."
                    $herView.hideshowQQ( "body_118.png", pos )
                    her "And now I will have to give him the wank off no matter what..."
                    m "Well, I didn't force you to give him that promise, did I?"
                    $herView.hideshowQQ( "body_117.png", pos )
                    her "......"
                    $herView.hideshowQQ( "body_32.png", pos )
                    her "This is just not fair!"
                    $ mad +=20
                    $ request_23 = False 
                    call music_block
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                
                "\"Alright, I think I can trust you.\"":
                    $herView.hideshowQQ( "body_45.png", pos )
                    her "Thank you, sir."
                    her "I knew you would understand."
                    m "Just make sure you finish your job properly this time."
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Of course, sir. I will give him the wank of his life, I promise!"
            
        elif one_out_of_three == 2: ### EVENT (B)
            m "MIss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_16.png", pos )
            her "I did, sir..."
            $herView.hideshowQQ( "body_29.png", pos )
            her "Although I am still not sure how I feel about all of this..."
            m "You personal feelings are of no concern to me, miss Granger."
            m "Just tell me how it went."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Well, there is not much to tell. sir..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Today I gave another handjob to one of my classmates..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "Me, Hermione Granger..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Giving free hanjobs in the school's restroom..."
            m "Wait. What do you mean with \"free\"?"
            $herView.hideshowQQ( "body_117.png", pos )
            her "Oh, of course... I get paid with house points for this..."
            her "But nobody knows about that..."
            her "And to everyone else this just looks like some harlot who does this for fun..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "They must think I am a slut..."
            $herView.hideshowQQ( "body_88.png", pos )
            her ".............."
            $herView.hideshowQQ( "body_190.png", pos )
            her "Do you think I'm a slut, sir?"
            menu:
                "\"What? Of course not, girl!\"":
                    $herView.hideshowQQ( "body_188.png", pos )
                    her ".............."
                    $herView.hideshowQQ( "body_124.png", pos )
                    her "You are right, sir..."
                    her "I am making this sacrifice for the glory of the \"Gryffindor\" house."
                    $herView.hideshowQQ( "body_121.png", pos )
                    her "I am not taking pleasure in this sort of activity..."
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "Because if I would..."
                    her "That would mean I really am a slut..."
                    $herView.hideshowQQ( "body_118.png", pos )
                    her "And I am not..."
                    her "......"
                    her "I am not a slut..."
                "\"A slut? No... Not yet.\"":
                    $herView.hideshowQQ( "body_117.png", pos )
                    her "\"Not yet\"??!"
                    $herView.hideshowQQ( "body_118.png", pos )
                    her ".........."
                    $herView.hideshowQQ( "body_72.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Well, of course!"
                    $herView.hideshowQQ( "body_15.png", pos )
                    her "You are right, as usual, sir!"
                    m "Huh?"
                    $herView.hideshowQQ( "body_14.png", pos )
                    her "I have done a few... naughty things..."
                    her "But that does not mean anything!"
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "..........."
                "\"Yes, that's exactly what you are.\"":
                    $herView.hideshowQQ( "body_20.png", pos )
                    her "I was afraid that you would say that, sir..."
                    her "But you are wrong, sir."
                    $herView.hideshowQQ( "body_21.png", pos )
                    her "You of all people should understand that I take no pleasure in this..."
                    $herView.hideshowQQ( "body_23.png", pos )
                    her "I just do what needs to be done..."
                    $ mad += 10
                    
            $herView.hideshowQQ( "body_13.png", pos )
            her "Sir, can I just get paid now, please?"
            m "Get paid? But you didn't tell me how it went yet?"
            her "I did not?"
            $herView.hideshowQQ( "body_183.png", pos )
            her "Sir, I gave a handjob to one of my classmates today..."
            her "I wanked his cock until he came..."
            $herView.hideshowQQ( "body_66.png", pos )
            her "Is that not what you told me to do?"
            m "That's exactly what I told you to do, girl."
            $herView.hideshowQQ( "body_184.png", pos )
            her "Then I would like to get paid now, please."
            m "........"
            m "Fine..."
            
            
            
        elif one_out_of_three == 3: ### EVENT (C)
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_16.png", pos )
            her "Yes, sir. I did."
            m "Great. Tell me more."
            $herView.hideshowQQ( "body_14.png", pos )
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Well, today was a rather busy day..."
            her "And I had to catch up on some studying..."
            her "So I really had no time to plan this out properly, like I normally would..."
            her "I pretty much just approached the first boy I saw..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "And asked him if he wants me to wank him off."
            her "a Few minutes later I was already stroking his hard cock in the restroom stall..."
            m "How very efficient of you..."
            $herView.hideshowQQ( "body_79.png", pos )
            her "Thank you, sir."
            $herView.hideshowQQ( "body_69.png", pos )
            her "So, as I was saying..."
            her "I wanked his cock until he came..."
            $herView.hideshowQQ( "body_66.png", pos )
            her "But after that he said: \"Good job, slut\" and just left me there..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Such a mean thing to do..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "It made me feel so cheap... and used."
            her "But it get's worse..."
            her "......."
            $herView.hideshowQQ( "body_118.png", pos )
            her "I think on some level it also made me feel good somehow..."
            her "All these favours I have been selling to you lately, sir..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "...it's starting to affect me."
            her "Sir, what is happening to me?"
            menu:
                "\"This is nothing. Stop overthinking it!\"":
                    $herView.hideshowQQ( "body_190.png", pos )
                    her "......."
                    $herView.hideshowQQ( "body_188.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "You are probably right, sir. As usual..."
                    her "This does not have to mean anything..."
                "\"That is a natural response...\"":
                    $herView.hideshowQQ( "body_190.png", pos )
                    her "It is?"
                    m "Of course."
                    m "You are a girl and he is a boy..."
                    m "You got excited and it made you feel good..."
                    $herView.hideshowQQ( "body_188.png", pos )
                    her "Hm..."
                    m "Now if you were to give a handjob and feel completely indifferent about it..."
                    m "...that would be... unnatural."
                    $herView.hideshowQQ( "body_190.png", pos )
                    her "I think you are right, sir."
                    $herView.hideshowQQ( "body_188.png", pos )
                    her "As usual." # :)
         
                "\"Yes! All goes according to plan!\"":
                    $herView.hideshowQQ( "body_119.png", pos )
                    her "What?"
                    m "What?"
                    $herView.hideshowQQ( "body_187.png", pos )
                    her "Professor, did you just say \"All goes according to plan\"?"
                    m "Did I?"
                    m "Oh, yes, of course."
                    m "ensuring that \"Gryffindor\" gets the house cup this year."
                    m "That's the plan And thanks to your hard work, girl..."
                    m "All goes according to keik-... I mean, the plan..."
                    $herView.hideshowQQ( "body_120.png", pos )
                    her "Hm..."
                    $ mad += 11

            
    elif whoring >= 21: # LEVEL 08+                    
        if one_out_of_three == 1: ### EVENT (A)
            if sucked_off_ron: #In public events. Give a handjob to classmate. Event level 03. Event # 1. "Jerked of and suked of Ron Weasley". Turns True after that.
                jump blowjob_ron
            else:
                $ sucked_off_ron = True #Makes sure this event is not repeated twice.
                
                stop music fadeout 1.0
                # HERMIONE HAS CUM ON HAIR.
                #$ aftersperm = True #Shows stains on Hermione's uniform.
                #$herView.data().addItemKey( 'sperm', CharacterExItem( herView.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herView.data().addItem( 'item_sperm', '05' )
                #$herView.data().addItemKey( 'sperm_after', CharacterExItem( herView.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 2 ) )
                $herView.data().addItem( 'item_sperm_dried' )

                show screen blktone
                with d3
                $herView.hideshowQQ( "body_11.png", pos )
                her "Professor Dumbledore, sir..."
                m "Miss Granger..."
                $herView.hideshowQQ( "body_10.png", pos )
                her "I did a bad thing today, sir..."
                m "Did you now? Do tell..."
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                her "Yes, I did a bad thing... a very bad thing..."
                $herView.hideshowQQ( "body_09.png", pos )
                her "A very bad and foolish thing..."
                her "..."
                m "...................."
                her "......................"
                $herView.hideshowQQ( "body_22.png", pos )
                her "I wanked off one of my best friend's brothers..."
                m "Interesting..."
                $herView.hideshowQQ( "body_21.png", pos )
                her "Seemed like such a great idea at first..."
                her "And Ron was so up for it..."
                $herView.hideshowQQ( "body_139.png", pos )
                her "But if Ginny were to find out... she..."
                $herView.hideshowQQ( "body_22.png", pos )
                her "She would most certainly kill me, sir..."
                m "A handjob, huh? Are you sure that was all you did?"
                $herView.hideshowQQ( "body_21.png", pos )
                her "Sir?"
                m "There is something in your hair..."
                $herView.hideshowQQ( "body_19.png", pos )
                her "What? But I swallowed it all... err..."
                $herView.hideshowQQ( "body_140.png", pos )
                her "I mean..."
                $herView.hideshowQQ( "body_139.png", pos )
                her "*Sigh*"
                her "...I sucked him off, sir."
                her "I did not plan to... but..."
                $herView.hideshowQQ( "body_140.png", pos )
                her "Ron is always so nice to me..."
                $herView.hideshowQQ( "body_143.png", pos )
                her "And I wanted to thank him...*Sob!*"
                $herView.hideshowQQ( "body_22.png", pos )
                her "And now Ginny will kill me! *Sob!*"
                her "She will kill me, sir!"
                $herView.hideshowQQ( "body_143.png", pos )
                her "And if she does not I will probably die of shame anyway."
                her "No, no, no... How will I ever face her...?"
                m "Calm down, girl."
                m "I assure you, this is not something a boy would be eager to brag about to his sister."
                $herView.hideshowQQ( "body_140.png", pos )
                her "It is not?"
                m "Don't be silly, girl."
                $herView.hideshowQQ( "body_23.png", pos )
                her "Hm..."
                $herView.hideshowQQ( "body_19.png", pos )
                her "You are probably right, sir..."
                her "And I made Ron give me his word that he will keep the whole incident a secret..."
                $herView.hideshowQQ( "body_10.png", pos )
                her "So, I think I should just trust him to keep his word..."
                $herView.hideshowQQ( "body_13.png", pos )
                her ".........."
                her "..."
                $herView.hideshowQQ( "body_06.png", pos )
                her "Will I get paid for this, sir?"
                m "Of course."

        elif one_out_of_three == 2: ### EVENT (B) (WANK DURING CLASS). Event level: 03.
            label blowjob_ron: #Sent here if sucked off Ron already.
                pass
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_06.png", pos )
            her "Yes I did, sir."
            $herView.hideshowQQ( "body_11.png", pos )
            her "But, ehm..."
            m "...?"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Well, I did not just wank off one of my classmates..."
            her "I.............."
            $herView.hideshowQQ( "body_88.png", pos )
            her "..............."
            m "Spit it out, girl. The suspense is killing me."
            $herView.hideshowQQ( "body_87.png", pos )
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "I sort of did it during class..."
            m "Impressive..."
            $herView.hideshowQQ( "body_124.png", pos )
            her "Yes, I was trying to act as nonchalant as I could..."
            her "Even took notes with my other hand..."
            $herView.hideshowQQ( "body_127.png", pos )
            her "And I think I gave him the wank of his life too..."
            her "Because he did not just cum."
            her "His cock simply exploded with spunk."
            m "You enjoyed it, didn't you?"
            $herView.hideshowQQ( "body_128.png", pos )
            her "To be completely honest with you, sir... I did."
            $herView.hideshowQQ( "body_111.png", pos )
            her "It was exciting to do something like that under everyone's noses..."
            her "It's empowering!"
            m "Ehm... sure, OK."
         
        elif one_out_of_three == 3: ### EVENT (C) Event level: 03. (Wanked off 5 boys).
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_129.png", pos )
            her "Yes, I did sir..."
            her "More than once actually..."
            m "More than once?"
            $herView.hideshowQQ( "body_128.png", pos )
            her "Five times, sir..."
            her "I got carried away a little I suppose..."
            m "What do you mean \"five times\", girl?"
            $herView.hideshowQQ( "body_129.png", pos )
            her "I mean I wanked off five boys today, sir."
            m "Very impressive, Miss Granger."
            $herView.hideshowQQ( "body_128.png", pos )
            her "Thank you, sir."
            m "You don't expect me to multiply your payment by seven or anything, do you?"
            $herView.hideshowQQ( "body_188.png", pos )
            her "Of course not, sir."
            m "Than why do it?"
            $herView.hideshowQQ( "body_190.png", pos )
            her "Well, it sort of just happened..."
            her "I was wanking off this one boy..."
            her "And another boy walked in on us..."
            her "He called his friends..."
            $herView.hideshowQQ( "body_128.png", pos )
            her "One thing lead to another..."
            m "And you ended up jerking off five cocks..."
            $herView.hideshowQQ( "body_121.png", pos )
            her "...yes."
            m "Well done, miss Garnger."
            $herView.hideshowQQ( "body_128.png", pos )
            
            

    
    
    
    $ gryffindor += current_payout #55
    m "The \"Gryffindor\" house gets [current_payout] points!"
    her "Thank you, sir."
    
    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    
 
 

    $herView.data().loadState()
    
    $ request_23_points += 1 
    $ request_23 = False 
    $ hermione_sleeping = True

    call music_block

    return

    
