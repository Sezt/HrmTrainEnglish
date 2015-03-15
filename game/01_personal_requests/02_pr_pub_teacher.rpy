
#################################################################################################################################
### LEVEL 02 ####################################################################################################################    
###################REQUEST_02_c (LEVEL02) ### FLIRT WITH TEACHERS ###
label new_request_02_c:
    
    $herView.hideQQ()
    m "{size=-4}(Tell her to be flirtatious with her teachers today?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request

    m "Miss granger, I want you to be especially flirtatious with your teachers today."
    if whoring <=2 or request_02_b_points <= 1: # request_02_b_points - counts how many times Hermione was sent to flirt with boys. 
        jump too_much
   
    $ pos = POS_140

    if request_02_c_points == 0 and whoring <= 8: ### up to LEVEL 03
    ### LEVEL 03 ### <===============================================================FIRST EVENT!
        $herView.showQQ( "body_01.png", pos )
        her "I will do my best, sir!"
        $herView.hideshowQQ( "body_02.png", pos )
        her "I am glad you finally decided to act, sir!"
        m "Huh?"
        $herView.hideshowQQ( "body_07.png", pos )
        her "You are finally ready to investigate the teachers who made a habit out of buying favours from the students, aren't you?" 
        $herView.hideshowQQ( "body_16.png", pos )
        her "I am honoured to pose as bait in this noble endeavor."
        m "Ehm... Yeah, that's exactly what I'm doing."
        $herView.hideshowQQ( "body_07.png", pos )
        her "Splendid! You can count on me, sir!"
    else:
        $herView.hideshowQQ( "body_07.png", pos )
        her "I shall provide you with a detailed report later tonight, sir."
        m "I will be waiting..."
    

    her "Well, I'd better go now. Classes are about to start..."
#    $ request_02_c = True

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


    $ hermione_takes_classes = True
    jump day_main_menu

    
    
label new_request_02_c_complete:  ### FLIRTING WITH TEACHERS COMPLETE ###
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
    $herView.showQ( "body_01.png", pos )
    show screen hermione_02
    with Dissolve(.3)
    her "Good evening, sir."
    m "Miss Granger..."
    m "Did you complete your task?"
    her "I did as you asked sir..."
    menu:
        "\"Great. Here are your points.\"":
            pass
        "\"Give me the details.\"":
            $herView.hideQQ()
            m "Tell me how many teachers did you flirt with, miss Granger?"
            m "Give me the details."
            show screen blktone
            with d3
    
            if  whoring >= 3 and whoring <= 5: ### LEVEL 02 <===================================================================== EVENT LEVEL 01
                if one_out_of_three == 1: ### EVENT (A)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Well, I tried flirting with Professor Flitwick..."
                    $herView.hideshowQQ( "body_09.png", pos )
                    her "But it didn't really work..."
                    $herView.hideshowQQ( "body_12.png", pos )
                    her ".............................."
                    m "How exciting..."
                    m "Is this all you have for me today, miss Granger?"
                    $herView.hideshowQQ( "body_11.png", pos )
                    her "Y-yes..."
                    her "But sir, I know for a fact that professor Flitwick is \"dirty\"!"
                    her "Everyone knows that because of his height..."
                    $herView.hideshowQQ( "body_13.png", pos )
                    her "He sometimes... ehm..."
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "He likes to look up girl's skirts, sir!"
                    m "Don't we all?"
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "What?"
                    m "I said, don't we all hate it and must be outraged by the a man like Professor Flick-flick."
                    $herView.hideshowQQ( "body_07.png", pos )
                    her "Er... It's \"Professor Flitwick\", sir."
                    m "Right. Putting him on my \"Naughty boys list\" as we speak."
                    $herView.hideshowQQ( "body_17.png", pos )
                    her "......................"
                    m "Well, I hate to admit it but you did a lousy job of today's favour, miss Granger."
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "................................"
                    
                    $ pos = POS_140
                    
                    menu:
                        "\"No points for you!\"":

                            $herView.hideshowQQ( "body_28.png", pos )
                            her "But professor, I did my best!"
                            $herView.hideshowQQ( "body_67.png", pos )
                            her "You are going back on your promise sir!"
                            m "......................."
                            $herView.hideshowQQ( "body_32.png", pos )
                            stop music fadeout 1.0
                            her "How unbecoming of a school headmaster!"
                            m "You are dismissed, miss Granger."
                            $herView.hideshowQQ( "body_76.png", pos )
                            her "Tsk!"
                            $ mad += 18
                            call music_block
                            jump could_not_flirt_02
                        "\"Here are your point's though.\"":
                            $herView.hideQQ()
                            $ pos = POS_140
                            $herView.showQQ( "body_28.png", pos )
                            her "Really?"
                            $herView.hideshowQQ( "body_75.png", pos )
                            her "Thank you so much professor!"
                           
                elif one_out_of_three == 2: ### EVENT (B)
                    $herView.hideQQ()
                    $ pos = POS_140
                    $herView.showQQ( "body_13.png", pos )
                    her ".................."
                    her "............................"
                    m "Miss Granger?"
                    $herView.hideshowQQ( "body_11.png", pos )
                    her "Yes, professor... I'm sorry... I just..."
                    $herView.hideshowQQ( "body_13.png", pos )
                    her "............"
                    m "Did you do what I asked you to do?"
                    $herView.hideshowQQ( "body_14.png", pos )
                    her "I tried, sir. I really did..."
                    m "Who did you try to flirt with?"
                    $herView.hideshowQQ( "body_13.png", pos )
                    her "........."
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "Professor Snape, sir."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    m "Severus? Interesting..."
                    m "How did it go?"
                    $herView.hideshowQQ( "body_07.png", pos )
                    her "It was awful sir..."
                    her "I am sorry, but I really hate professor Snape, sir!"
                    m "I'm sure the feeling is mutual..."
                    m "Tell me what happened."
                    $herView.hideshowQQ( "body_09.png", pos )
                    her "Nothing happened, sir. He just laughed at me..."
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "I may not have much feminine charm, but I tried to be nice..."
                    $herView.hideshowQQ( "body_30.png", pos )
                    her "And he just started laughing in my face!"
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "...it is really scary to see professor Snape laugh..."
                    her "........"
                    her "I am awful at flirting, I am sorry sir..."
                    $herView.hideshowQQ( "body_47.png", pos )
                    her "But I know that professor Snape is \"dirty\"!"
                    her "If you were to send someone else to him the outcome would be different, I know it!"
                    m "Someone else?"
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "Yes! Someone with more experience at this..."
                    her "Someone..."
                    her "Someone, uhm..."
                    m "Sluttier?"
                    $herView.hideshowQQ( "body_66.png", pos )
                    her "Yes, I suppose..."
                    m "Don't you give up, miss Granger. We will make a slut err--"
                    m "I mean a woman out of you yet!"
                    $herView.hideshowQQ( "body_79.png", pos )
                    her "..................."
                    menu:
                        "\"...But you get no points this time\"":
                            $herView.hideshowQQ( "body_12.png", pos )
                            her "But I did my best..."
                            $herView.hideshowQQ( "body_34.png", pos )
                            her "And I feel so humiliated now..."
                            $herView.hideshowQQ( "body_33.png", pos )
                            her "But I understand and won't argue with your decision..."
                            call music_block
                            jump could_not_flirt_02
                        "\"Here are your points, girl.\"":
                            pass
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "I tried to flirt with mr.Filch, sir..."
                    m "I see. {size=-5}(No idea who that is.){/size}"
                    $herView.hideQQ()
                    $ pos = POS_140
                    $herView.showQQ( "body_11.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Yes, I know that technically mr.Filch is not a teacher..."
                    m "Huh?"
                    $herView.hideshowQQ( "body_01.png", pos )
                    her "But he is part of the school's staff..."
                    her "And we did hit it off quite well too!"
                    her "He was surprisingly sweet."
                    her "But I don't think he is \"dirty\", sir."
                    #translators "Filtch - мистер Филч. Filth - грязь."
                    m "Gotcha... Mr.Fil{size=+7}TH{/size} is off the list then."
                    $herView.hideshowQQ( "body_07.png", pos )
                    her "It's \"Mr.Filch\", sir..."
                    m "What did I say?"
                    
                    
            elif whoring >= 6 and whoring <= 8: ### LEVEL 03 <=======================================================================================EVENT LEVEL 02
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    $herView.hideQQ()
                    $ pos = POS_140
                    $herView.showQQ( "body_10.png", pos )
                    her "Well, professor Slughorn invited me over to one of his..."
                    her "Rather disturbing tea-parties..."
                    $herView.hideshowQQ( "body_16.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "There were plenty of girls..."
                    her "But all of them were much younger then me..."
                    $herView.hideshowQQ( "body_17.png", pos )
                    her "Almost every guest was a freshman..."
                    $herView.hideshowQQ( "body_16.png", pos )
                    her "We had tea and some cake..."
                    her "Everything was pretty harmless..."
                    m "Did you flirt with the man or not?"
                    her "I did..."
                    $herView.hideshowQQ( "body_17.png", pos )
                    her "Or at least I tried..."
                    her "Professor Slughorn seems to be more interested in much younger girls..."
                    m "You almost sound jealous, miss Granger."
                    $herView.hideshowQQ( "body_18.png", pos )
                    her "What?!"
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "That is preposterous!"
                    m "Here are your points..."
                    her "...................."
          
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideQQ()
                    $ pos = POS_140
                    $herView.showQQ( "body_80.png", pos )
                    her "I had an amazing day, sir!"
                    m "Do tell, miss Granger..."
                    $herView.hideshowQQ( "body_68.png", pos )
                    her "I had a class with professor Lockhart today..."
                    her "Sir Lockhart is so charming and smart and..."
                    $herView.hideshowQQ( "body_78.png", pos )
                    her "And perfect..."
                    m "Please spare me your schoolgirl crush, miss Granger."
                    $herView.hideshowQQ( "body_80.png", pos )
                    her "Sir Lockhart was even kind enough to give me his autograph..."
                    m "How kind of him indeed."
                    $herView.hideshowQQ( "body_68.png", pos )
                    her "Yes, I can't wait to show it to the girls!"
                    m "Hm... Can I see it?"
                    $herView.hideshowQQ( "body_45.png", pos )
                    her "Sir?"
                    m "The Autograph, girl. Can I see it?"
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "Well... Em... It's in a rather private area, sir."
                    m "What? Well, then professor Goldenheart surely is \"dirty\"!"
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "It's professor Lockhart, sir..."
                    her "And... Ehm..."
                    her "Well, it's not {size=+5}that{/size} private..."
                    m "Show it to me then!"
                    $herView.hideshowQQ( "body_66.png", pos )
                    her "No, sir! That would be inappropriate!"
                    menu: 
                        "{size=-3}\"Lockhart will be out of this school in no time!\"{/size}":
                            $herView.hideshowQQ( "body_72.png", pos )
                            her "Because of me?"
                            $herView.hideshowQQ( "body_67.png", pos )
                            her "Sir, please!"
                            m "Show me!"
                            $herView.hideshowQQ( "body_32.png", pos )
                            her "No, it's embarrassing!"
                            menu:
                                "\"Fine. Here are your points.\"":
                                    $herView.hideshowQQ( "body_74.png", pos )
                                    her "Thank you for understanding, Professor."
                                "\"Show me or I won't pay you!\"":
                                    $herView.hideshowQQ( "body_72.png", pos )
                                    her "What?!"
                                    $herView.hideshowQQ( "body_73.png", pos )
                                    her "..............."
                                    $herView.hideshowQQ( "body_29.png", pos )
                                    her ".................."
                                    $herView.hideshowQQ( "body_47.png", pos )
                                    her "Well, alright, but only to clear my idol's name..."
                                    $herView.hideQQ()
                                    show screen blktone8
                                    with d5
                                    $her_head_state = 12
                                    her_head_main "Вот...."
                                    m "Хм..."
                                    hide screen blktone8 
                                    with d5
                                    $herView.data().saveState()
                                    # add pose with lifted skirt and authograph
                                    #$herView.data().addPose( CharacterExItemSkirtLifted( herView.mPoseFolder, 'pose_skirt_up.png', G_Z_POSE ) )
                                    $herView.data().addItem( 'item_pose_lifted_skirt' )
                                    #$herView.data().addItemKey( 'autograph', CharacterExItem( herView.mMiscFolder, 'autograph.png', G_Z_LEGS + 1 ) )
                                    $herView.data().addItem( 'item_autograph' )
                                    
                                    $herView.showQ( "body_51.png", pos )
                                    hide screen ctc
                                    show screen ctc
                                    with d3
                                    pause
                                    $herView.hideshowQQ( "body_50.png", pos )
                                    her "As you can see Professor Lockhart is nothing but an embodiment of everything pure and courageous!"
                                    pause
                                    m "Do I? From this?"
                                    her "You should not worry about professor Lockhart, sir."
                                    her "He is not \"dirty\"."
                                    m "Ah, what do I care..."
                                    $herView.hideshowQQ( "body_51.png", pos )
                                    her "............?"
                                    $herView.hideQQ()
                                    
                                    # load before pose
                                    $herView.data().loadState()
                                    
                                    $herView.showQ( "body_47.png", pos, fade )
                                    pause
                                    hide screen ctc
                                    $ mad += 18
                        "\"Fine... Here are your points.\"":
                            $herView.hideshowQQ( "body_74.png", pos )
                            her "Thank you for understanding, Professor."
                            
                elif one_out_of_three == 3: ### EVENT (C)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideQQ()
                    $ pos = POS_370
                    $herView.showQQ( "body_15.png", pos )
                    her "Well, I spent quite some time by flirting with mr.Filch today."
                    $herView.hideshowQQ( "body_16.png", pos )
                    her "What a well read and exceptionally well mannered gentleman mr.Filch is."
                    m "........"
                    $herView.hideshowQQ( "body_13.png", pos )
                    her "But I don't think anyone knows him like that..."
                    her "I don't think anyone knows mr.Filch like I do."
                    $herView.hideshowQQ( "body_06.png", pos )
                    her "I feel like he really opened up to me, sir."
                    m "Right..."
                    m "This, mr.Fli{size=+7}nt{/size}--"
                    $herView.hideQQ()
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $herView.showQQ( "body_04.png", pos )
                    her "It's mr.Filch, sir."
                    m "Yeah, whatever... Is he a teacher here then?"
                    her "Mr.Filch? A teacher? No, sir..."
                    $herView.hideshowQQ( "body_06.png", pos )
                    her "He is the caretaker..."
                    m "A caretaker...?"
                    m "You mean he is a janitor?"
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Well..."
                    m "Miss Granger, I did not send you out there to charm school janitors!"
                    $herView.hideshowQQ( "body_14.png", pos )
                    her "But mr.Filch is part of the school staff, sir!"
                    menu:
                        "\"Just take your points and go!\"":
                            $herView.hideshowQQ( "body_03.png", pos )
                            her "........................."
                        "\"Favour failed! No points for you!\"":
                            $ mad +=15
                            $herView.hideshowQQ( "body_07.png", pos )
                            her "But professor?"
                            m "You are dismissed, miss Granger."
                            $herView.hideshowQQ( "body_05.png", pos )
                            her "........................................."
                            jump could_not_flirt_02


            elif whoring >= 9: # LEVEL 04 and higher.
                if one_out_of_three == 1: ### EVENT (A) LEVEL04 <============================================================================
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_33.png", pos )
                    her "............................."
                    her "....................................."
                    m "Miss Granger?"
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Professor, I....."
                    m "What is it? What happened?"
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "Well..."
                    her "It's mr.Filch, sir..."
                    m "The janitor?"
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "I flirted with him a little..."
                    her "And it went great at first..."
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "......................."
                    m "................?"
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "And then..."
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "Not sure if I should..."
                    m "Miss Granger, if you are not going to speak up, you may as well leave."
                    $herView.hideshowQQ( "body_32.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "He showed me his \"thing\", sir!"
                    m "His what?"
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "His... manhood, sir."
                    g9 "Way to go, Janitor-guy!"
                    $herView.hideshowQQ( "body_72.png", pos )
                    her "What?!"
                    m "*Khem* I mean, this is unspeakable!"
                    $herView.hideshowQQ( "body_21.png", pos )
                    her "Yes... Vile crooked thing all covered in veins..."
                    m "Spare me the grisly details, girl."
                    $herView.hideshowQQ( "body_20.png", pos )
                    her "Why would he do such a thing?"
                    her "One second we were just talking and then..."
                    m "Well, your noble  sacrifice shall not go unnoticed, miss Granger!"
                    m "Fifteen points to \"Gryf--"
                    $herView.hideshowQQ( "body_19.png", pos )
                    her "Professor Dumbledore, please wait."
                    m "Huh?"
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "Well, aren't you going to do something about this?"
                    m "Well..."
                    $herView.hideshowQQ( "body_47.png", pos )
                    her "What if I am not the first victim..?"
                    her "Some unfortunate freshman could be traumatized for life!"
                    m "And who wouldn't be really?"
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "Does this mean you will take action, sir?"
                    m "uhm... Yeah, sure..."
                    m "There! Putting it on my \"to-do-list\"..."
                    m "\"Take care of the creepy janitor-guy and his crooked cock.\"..."
                    m "Yes, first thing tomorrow."
                    $herView.hideshowQQ( "body_16.png", pos )
                    her "Thank you sir."
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "Can I have my points now?"
    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_76.png", pos )
                    her "Professor Snape!"
                    m "Uh... yeah, I am, in fact, Dumbledore, such as..."
                    $herView.hideQQ()
                    
                    g4 "{size=-5}(Wait, did {size=+7}he{/size} just put me under another disguise?){/size}"
                    g4 "{size=-5}(So do I look like that Professor Snape guy now?){/size}"
                    g4 "{size=-5}(By the great desert sands! Akabur, you need to learn restrain yourself!){/size}"
                    a5 "{size=-5}(Would you hear the girl out first! Geez...){/size}"
                    $herView.hideshowQQ( "body_02.png", pos )
                    her "Professor? Who are you talking to?"
                    m "Em... I'm communicating with a spirit from another dimension..."
                    $herView.hideshowQQ( "body_17.png", pos )
                    her ".....??!"
                    $herView.hideQQ()
                    a6 "{size=-5}(Stick to the script, you bastard!){/size}"
                    g4 "Yes, a particularly annoying spirit... Annoying and dumb!"
                    a6 "{size=-5}(You......!){/size}"
                    $herView.hideshowQQ( "body_02.png", pos )
                    her "Professor Dumbledore, please, you need to listen to me!"
                    m "Yes, yes, girl, I'm listening."
                    $herView.hideshowQQ( "body_04.png", pos )
                    her "I just confirmed that professor Snape is corrupted and \"dirty\", sir!"
                    m "Tell me what happened."
                    $herView.hideshowQQ( "body_02.png", pos )
                    her "Well, during the classes today..."
                    her "I have been doing my best to attract professor Snape's attention..."
                    her "I have been giving him \"dreamy looks\"..."
                    her "And I've been eyeing his crotch..."
                    m "You..."
                    m "Eyed his crotch?"
                    $herView.hideshowQQ( "body_04.png", pos )
                    her "Yes... It's when you stare at a man's crotch and imagine that you are looking at something you want badly..."
                    m "Where do you get this stuff?"
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Women's magazines..."
                    $herView.hideshowQQ( "body_07.png", pos )
                    her "Well, anyway, it worked, sir."
                    $herView.hideshowQQ( "body_47.png", pos )
                    her "As soon as the class was over, professor Snape grabbed my buttocks, sir!"
                    m "The fiend!"
                    m "Did you enjoy it, though?"
                    $herView.hideshowQQ( "body_30.png", pos )
                    her "Sir, I am only doing this--"
                    m "Go \"Gryffindors\"! honour and all that. Yes, I remember."
                    m "Here are your points."
                    $herView.hideshowQQ( "body_66.png", pos )
  
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_09.png", pos )
                    her "Professor Lockhart!"
                    m "Got it! Adding him to the \"Naughty list\"!"
                    $herView.hideshowQQ( "body_11.png", pos )
                    her "No, sir, it's not that..."
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "Or..."
                    her "I'm not sure..."
                    $herView.hideshowQQ( "body_11.png", pos )
                    her "I used to adore him..."
                    $herView.hideshowQQ( "body_13.png", pos )
                    her "But he..."
                    her "He just..."
                    $herView.hideshowQQ( "body_20.png", pos )
                    her "How is this possible?"
                    her "I can't believe it..."
                    $herView.hideQQ()
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    m "{size=-4}(Agh! The suspense is killing me!){/size}" 
                    m "{size=-4}(Did he force her to blow him?){/size}"
                    m "{size=-4}(Did he rape her?){/size}"
                    g4 "What was it, girl? Speak up!"
                    $herView.hideshowQQ( "body_14.png", pos )
                    her "Huh?"
                    m "What did Professor Lockhart do to you?"
                    $herView.hideshowQQ( "body_13.png", pos )
                    her "Ehm... Nothing, sir..."
                    m "Nothing?!"
                    $herView.hideshowQQ( "body_11.png", pos )
                    her "Yes, I sort of cornered mr.Lockhart today..."
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "And I also may have sort of made a pass at him..."
                    m "Seriously?"
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Yes... Not sure what had gotten into me, sir..."
                    m "Way to go, miss Granger!"
                    $herView.hideshowQQ( "body_32.png", pos )
                    her "Hear me out first sir, please!"
                    m "My apologies. Please continue."
                    $herView.hideshowQQ( "body_14.png", pos )
                    her "Well, I always knew that mr.Lockhart was a true gentleman and..."
                    her "And... and I just wanted to clear his name from any suspicions once and for all..."
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "..............."
                    her "Well mr.Lockhart did not reject me..."
                    m "You are killing me girl!"
                    m "He didn't reject you, he didn't rape you..."
                    m "What the hell happened then?"
                    $herView.hideshowQQ( "body_33.png", pos )
                    her "............."
                    $herView.hideshowQQ( "body_34.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "I made him cry, sir..."
                    m "..............wait.......what?"
                    $herView.hideshowQQ( "body_28.png", pos )
                    her "He gave me a bewildered look and then started to sob..."
                    her "He looked like he was genuinely afraid of me, sir."
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "I think..."
                    her "I think mr.Lockhart might be afraid of women..."
                    m "Afraid of women?"
                    m "What is that supposed to mean?"
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "That he is into boys, sir?"
                    m "Oh..."
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "............"
                    m "..........."
                    m "Well, I bet it was a traumatizing experience for you, miss Granger."
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "It was, sir..."
                    m "Well, I hope these points will make you feel better."
                    
                            
    
    $ gryffindor +=15
    m "The \"Gryffindors\" gets 15 points!"
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

    call music_block

    $ p_level_03_active = True #When turns TRUE public favors of level 03 become available. 

    
    if whoring <= 5:  # (if whoring >= 3 and whoring <= 5) - LEVEL 02
        $ whoring +=1

    $ request_02_c_points += 1 #Leveling up the event.
#    $ request_02_c = False 
    $ hermione_sleeping = True

    return    
    
label could_not_flirt_02: #Sent here when chose "Задание провалено! Ты не получишь очки!"
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
    
    $ request_02_b_points += 1
#    $ request_02_b = False 
    $ hermione_sleeping = True
    
    return   

