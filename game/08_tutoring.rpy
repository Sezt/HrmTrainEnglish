label tutoring:

    $ tut_happened = True # Turns TRUE after you click the tutoring button and see th message that tutoring is not a part of this game. Make sure the tutoring button will not be visible after that.
    
    $herView.hideQQ()
    $ pos = POS_370
    $herView.showQQ( "body_14.png", pos )
    
    her "Of course, sir."
    her "I'll go get my books then."
    
    $herView.hideQ()

    #add pose with the book!
    $herView.data().saveState()
    #$herView.data().addPose( CharacterExItemPoseBook( herView.mPoseFolder, "pose_with_book.png", G_Z_POSE ) )
    $herView.data().addItem( 'item_pose_book' )

    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    



    $ pos = POS_140
    $herView.showQQ( "body_199.png", pos )
    
    
    hide screen blkfade
    with d3
    
    show screen ctc
    pause
    hide screen ctc
    
    $herView.hideQQ()
                                                                                                                                                                                                                        #HERMIONE
    if knowledge == 0:
        $ tut_happened = True
        $herView.showQQ( "body_199.png", pos )
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        her "Thank you again for what you do for me, sir."
        her "You must be very busy with school affairs, but still you take the time to tutor me..."
        her "I want to say that I appreciate your concern."
        m "No problem at all, Miss Granger. Monitoring student performance is one of the main duties of the Headmaster."
        g9 "{size=-4}(In addition, I am going to climb back in your panties when we finish.){/size}"
        $herView.hideQQ()

        # hide books pose
        $herView.data().delPose()

        $herView.showQQ( "body_08.png", pos )
        her "You say something, sir?"                                                                                                                                                                                  #HERMIONE
        m "Ahem ... I said that you will have no problem passing any exam, when we're done."
        $herView.hideQQ()
        $herView.showQQ( "body_06.png", pos )
        her "I never for a moment doubted it."
        her "Because of you - Albus Dumbledore - one of the greatest wizards of our time."
        g9 "Of course! I am great!"
        $herView.hideQQ()
        $herView.showQQ( "body_17.png", pos )
        her "..."
        $herView.hideQQ()
        $herView.showQQ( "body_06.png", pos )
        her "Let's start, Professor?"                                                                                                                                                                                   #HERMIONE
        m "Of course, child. Have you got any questions?"
        $herView.showQQ( "body_06.png", pos )
        her "I don't think so. Although ..."
        $herView.hideQQ()
        $herView.showQQ( "body_14.png", pos )
        her "There is something I am unsure of and it haunts me."
        g9 "And what is that? Do not be shy, you can ask the greatest magician in the world!"
        $herView.hideQQ()
        $herView.showQQ( "body_12.png", pos )
        her "..."
        $herView.hideQQ()
        $herView.showQQ( "body_04.png", pos )
        her "Ok..."
        $herView.hideQQ()
        $herView.showQQ( "body_11.png", pos )
        her "I'm not quite sure how the spell \"patiskor Walde\" would work against the Peruvian manticore..."
        her "Indeed, this case would ideally fit \"Gailey sekundum\", but in the publication \"Ekstsilius prohorosa \" 1831 states otherwise ..."
        $herView.hideQQ()
        $herView.showQQ( "body_06.png", pos )
        her "Could you tell what my mistake is?"                                                                                                                                                                                  #HERMIONE
        m "Of course, child..."
        m "..."
        m "..."
        m "..!"
        m "{size=-4}(What kind of nonsense is she talking about?){/size}"
        m "{size=-4}(OK, pull yourself together, Ginny...){/size}"
        m "Ahem ... It's worth noting that we are not talking about simple muntikorah, namely perduanskih..."
        $herView.hideQQ()
        $herView.showQQ( "body_04.png", pos )
        her "\"Peruvian manticores\", sir..."
        $herView.hideQQ()
        m "Correct! Clever girl. I was just testing you. Give me the main features of these feather ... Beings."
        $herView.hideQQ()
        $herView.showQQ( "body_01.png", pos )
        her "Of course, sir."
        $herView.showQQ( "body_14.png", pos )
        her "Peruvian Manticore - Manticore living in the country of Peru, wingspan..."
        her "*Pssssssssssssssss*"
        her "*psssssssssssssss*"
        m "..."
        her "-BZZZZZZZZZZZZZZZZZ..."
        her "PSPPSPSPSPSPSP"
        m "..."
        g9 "{size=-4}(And it's even funny.){/size}"
        her "Nya-Nya-Nya-Nya-Nya-Nya-Nya..."
        her "Nya-Nya-Nya-{b}member{/b}-Nya-Nya."
        m "..."
        stop music 
        $ renpy.play('sounds/scratch.wav')
        m "..!"
        m "What did you say, Miss Granger ?!"
        $herView.hideQQ()
        $herView.showQQ( "body_13.png", pos )
        her "Um ... the first time a detailed study of their member association Malburzhskoy magician - Istafar Arius..."
        $herView.hideQQ()
        $herView.showQQ( "body_11.png", pos )
        her "I said something wrong ..?"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        m "... no, no, that's right..."
        $herView.hideQQ()
        $herView.showQQ( "body_01.png", pos )
        her "Then if we can go back to my question, sir?"        
        m "Ah, yes ... Question..."
        m "Hmm..."
        m "Miss Granger, what do you know about Finches?"
        $herView.hideQQ()
        $herView.showQQ( "body_14.png", pos )
        her "Excuse me, sir?"
        m "Close your eyes and imagine a Finch, Miss Granger."
        $herView.hideQQ()
        $herView.showQQ( "body_11.png", pos )
        her "But..."
        m "Just imagine."
        $herView.hideQQ()
        $herView.showQQ( "body_17.png", pos )
        her "..."
        $herView.hideQQ()
        $herView.showQ( "body_16.png", pos )
        her "Ok."
        $herView.hideQQ()
        $herView.showQQ( "body_207.png", pos )
        m "Now imagine your... Mantihole."
        $herView.hideQQ()
        $herView.showQQ( "body_16.png", pos )
        her "Manticore..."
        m "I know. It was another test. Focus on the Finch and that creature."
        $herView.hideQQ()
        $herView.showQQ( "body_207.png", pos )
        m "In the entire universe there is only these two creatures..."
        m "Nothing else..."
        $herView.hideQQ()
        $herView.showQQ( "body_208.png", pos )
        her "..."
        m "They fill your entire mind..."
        her "..."
        $herView.hideQQ()
        m "And now..."
        $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
        menu:
            "The Manticore eats the finch!":
                $herView.hideQQ()
                $herView.showQQ( "body_18.png", pos )
                her "..?!"
                $herView.hideQQ()
                $herView.showQQ( "body_14.png", pos )
                her "professor Dumbledore?!"
                m "This is the answer to your question, Miss Granger."
                $herView.hideQQ()
                $herView.showQQ( "body_12.png", pos )
                her "But..."
                m "If you have no more questions, then you are free to go, Miss Granger."
                $herView.hideQQ()
                $herView.showQQ( "body_04.png", pos )
                her "But..."
                m "Good night, Miss Granger."
                $herView.hideQQ()
                $herView.showQQ( "body_12.png", pos )
                her "..."
                her "..Goodbye, Professor."
                her "..."
                $herView.hideQQ()
                $herView.showQQ( "body_13.png", pos )
                her "{size=-4}(What a hell..?){/size}"
                $herView.hideQQ()
                #Гермиона уходит
                call hermione_leave_tutoring
             
            "The Finch eats the Manticore!":
                $ zyablik_switch = 1
                g4 "He plunges his razor-sharp beak into the carcass of the poor creature!"
                $herView.hideQQ()
                $herView.showQQ( "body_18.png", pos )
                her "..?!"
                g4 "Breaks its carcass into small pieces and starts to devour her insides!"
                g4 "The manticore eyes are looking at the small bird with a look of despair, fear and silent prayers."
                g4 "But the little monster just continues to devour her insides, making disgusting sucking sounds ..."
                m "{size=-4}(Damn, it seems I got a gorgeous hard-on.){/size}"
                $herView.hideQQ()
                $herView.showQQ( "body_04.png", pos )
                her "Professor Dumbledore!"
                her "What a..."
                m "This is the answer to your question, young lady."
                m "Now leave me."
                m "I need to, uh ... clean the pipe."
                $herView.hideQQ()
                $herView.showQQ( "body_12.png", pos )
                her "But..."
                m "Good night, Miss Granger."
                $herView.hideQQ()
                her "..."
                #Гермиона уходит
                call hermione_leave_tutoring

                g9 "And I've got to start \"cleaning the pipes\"."
                show screen blkfade # Затемнение экрана
                g4 "Take that, bloody dismembered creature!"
                g4 "{size=+7}AGRH!!!{/size}"
                hide screen blkfade # Экран посветлел xD
                m "..."
                m "That was weird."
                
            "Grab her breasts!":
                ">You gently squeeze her boobs with your hands."
                $herView.hideQQ()
                $herView.showQQ( "body_127.png", pos )
                her "Professor, what is that?"
                m "Hmm? What you talking about?"
                $herView.hideQQ()
                $herView.showQQ( "body_33.png", pos )
                her "I feel that my chest ... Something's going on..."
                m "Oh, it's ... It's part of meditation. Cosmic energy flows into your heart to give an answer to your question."
                ">You start gently massaging her breasts."
                $herView.hideQQ()
                $herView.showQQ( "body_32.png", pos )
                her "*Ah! * Cosmic energy? That's something ... * Ah! * From Indian magic?"
                m "Certainly. And you are very well-read, Miss. Now focus on the cosmic energy..."
                $herView.hideQQ()
                $herView.showQQ( "body_74.png", pos )
                her "Well, Professor."
                her "..."
                ">Snap-Snap..."
                g4 "{size=-4}(Damn, it seems I got a gorgeous hard-on!){/size}"
                m "{size=-4}(I don't think it is necessary to take it further at the beginning of training ...){/size}"
                m "The lesson is over, you can open your eyes, Miss Granger."
                $herView.hideQQ()
                $herView.showQQ( "body_124.png", pos )
                her "..."
                m "Well, now? Did this answer your question?"
                $herView.hideQQ()
                $herView.showQQ( "body_79.png", pos )
                her "Actually..."
                her "I had a feeling that someone touched my breasts..."
                her "And more than anything."
                m "You liked it?"
                $herView.hideQQ()
                $herView.showQQ( "body_76.png", pos )
                her "Professor ?!..."
                m "Share your feelings during meditation, it is an important part of training."
                $herView.hideQQ()
                $herView.showQ( "body_29.png", pos )
                her "..."
                her "It was an unusual feeling ...."
                her "But I never received an answer."
                m "It will come with time, Miss Granger."
                m "And now I ask you to leave me. I need to, uh..."
                m "Clean the pipe."
                $herView.hideQQ()
                $herView.showQ( "body_45.png", pos )
                her "...Of course, sir."
                her "Bye now."
                m "Good night, Miss Granger."
                $herView.hideQQ()
                #Гермиона уходит
                call hermione_leave_tutoring

                g9 "Well, it's time to start \"cleaning the pipes\"."
                show screen blkfade # Экран темнеет
                g4 "Take that, big boobed little witch!"
                g4 "{size=+7}AGRH!!!{/size}"
                hide screen blkfade # Экран светлеет
                m "... that was refreshing."
                pass
        
        m "..."
        m "It is unlikely that I will be able to train her, I do not really know about this world..."
        m "I think I should talk about it with Snape."
        $ teacher_jinn_quest = 1

        $herView.data().loadState()
        jump day_start    
        #$ knowledge +=1
    

    # "You spend the evening tutoring Hermione. Hermione become a bit smarter."
    
    elif knowledge >= 5 and tutoring_events == 0 and hermi.whoring >= 1:
        $ tutoring_events += 1
        "Event 01"
        
    elif knowledge >= 10 and tutoring_events == 1 and hermi.whoring >= 2: #LEVEL 02
        $ tutoring_events += 1
        "Event 02"
        
    elif knowledge >= 15 and tutoring_events == 2 and hermi.whoring >= 3: #LEVEL 03
        $ tutoring_events += 1
        "Event 03"
        
    elif knowledge >= 20 and tutoring_events == 3 and hermi.whoring >= 4: #LEVEL 04
        $ tutoring_events += 1
        "Event 04"
        
    elif knowledge >= 25 and tutoring_events == 4 and hermi.whoring >= 5: #LEVEL 05
        $ tutoring_events += 1
        "Event 05"
        
    elif knowledge >= 30 and tutoring_events == 5 and hermi.whoring >= 7: #LEVEL 06
        $ tutoring_events += 1
        "Event 06"
        
    elif knowledge >= 35 and tutoring_events == 6 and hermi.whoring >= 8: #LEVEL 07
        $ tutoring_events += 1
        "Event 07"
         
    if knowledge >= 40 and tutoring_events == 7 and hermi.whoring >= 9: #LEVEL 08
        $ tutoring_events += 1
        "Event 08"
        
    elif knowledge >= 45 and tutoring_events == 8 and hermi.whoring >= 11: #LEVEL 09
        $ tutoring_events += 1
        "Event 09"
        
    elif knowledge >= 50 and tutoring_events == 9 and hermi.whoring >= 13: #EVENT 10
        $ tutoring_events += 1
        "Event 10"
        
    elif knowledge >= 55 and tutoring_events == 10 and hermi.whoring >= 14: #EVENT 10
        $ tutoring_events += 1
        "Event 11"
        
    elif knowledge >= 60 and tutoring_events == 11 and hermi.whoring >= 16: #EVENT 11
        $ tutoring_events += 1
        "Event 12"
         
    elif knowledge >= 65 and tutoring_events == 12 and hermi.whoring >= 18: #EVENT 12
        $ tutoring_events += 1
        "Event 13"
        
    elif knowledge >= 70 and tutoring_events == 13 and hermi.whoring >= 20: #EVENT 13
        $ tutoring_events += 1
        "Event 14"
        
    elif knowledge >= 75 and tutoring_events == 14 and hermi.whoring >= 21: #EVENT 14
        $ tutoring_events += 1
        "Event 15"
        
 
    
   
    # $ knowledge +=1
    "> You dismiss Hermione."
    jump day_start


label hermione_leave_tutoring:
    hide screen hermione_02 #Hermione stands still.
    with d3
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    return
