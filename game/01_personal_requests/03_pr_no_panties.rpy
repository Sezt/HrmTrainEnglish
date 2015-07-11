################### REQUEST_03 (Level 02) (Available during daytime only). "Give me your panties" ###############################
label new_request_03: #(Whoring = 3 - 5)
    if hermi.whoring <= 2:
        jump too_much
    $herView.hideQQ()
    
    $ pos = POS_370
    
    m "{size=-4}(I could ask her to take off her panties and give them to me before she leaves for classes today.){/size}"
    $ menu_x = 0.5 #Default position of the menu. Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $wtevent.NotFinished()
            jump new_personal_request
    $herView.showQQ( None, pos )
    #show screen hermione_main
    her "I am listening, sir."
    m "I will need your panties..."   
    $herView.hideQQ()
    $ menu_x = 0.5 #Menu is moved to the left side.
    $ pos = POS_120
    show screen blktone 
    show screen ctc
    $herView.showQ( "body_01.png", pos )
    with Dissolve(.3)
    pause
    
    
#    if request_03_points == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
    if IsFirstRun() and hermi.whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
        stop music fadeout 10.0
#        $ new_request_03_01 = True # HEARTS.

#        $ request_03 += 1
        $herView.hideshowQQ( "body_11.png", pos )
        her "W-what?"
        her "My... panties...?"
        her "Professor Dumbledore, this is..."
        m "This is the favour I will be buying from you today, Miss Granger..."
        m "It is a small thing.  Something I'm sure you won't even miss not having."
        m "But if you are not interested you are more than welcome to leave."
        her "No, I am interested. I am.... it's just..."
        her "You want my...."
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $herView.hideshowQQ( "body_47.png", pos )
        her "...panties, sir?"
        m "Yes I do..."
        $herView.hideshowQQ( "body_66.png", pos )
        her "May I ask what you are planning to do with them...?"
        m "Let's just say I am conducting an experiment."
        her "But this is kind of inappropriate, don't you think?"
        m "I'm not sure that it is.  You give your clothing to the house elves to launder or mend regularly, I'm sure."
        m "As I said, you are in no way obligated to do any favour I ask.  I will not hold it against you."
        m "But if it is as you say and some of the girls from Slytherin are selling favours for house points..."
        m "...that would put Gryffindor at a disadvantage, wouldn't it, Miss Granger?"
        m "And you claim that many of them are doing things far worse so they may be getting even more points..."
        $herView.hideshowQQ( "body_47.png", pos )
        her "Then...then I shall!"
        $herView.hideshowQQ( "body_12.png", pos )
        her "(Those Slytherin tramps have no dignity.)"
        $herView.hideQQ()
        m "Well, then you {i}have{/i} shown them, haven't you!"
        $herView.hideshowQQ( "body_66.png", pos )
        her "Huh?"
        m "Gave them a taste of their own medicine, so to speak!"
        $herView.hideshowQQ( "body_14.png", pos )
        her "What?"
        m "Yes! You see it now, do you not?  Don't just put Gryffindor house back on top..."
        m "...but do it by beating them at their own game!"
        $herView.hideshowQQ( "body_11.png", pos )
        her "Professor...if there is another way..."
        m "A headmaster cannot play favourites, as you know, but Gryffindor House has always been a shining beacon..."
        m "I wish I could merely give you the points but that would hardly be fair to Hufflpuff and Ravenclaw..."
        show screen blktone8
        $herView.hideQQ()
        ">Hermione thinks for a moment, then bends down in front of your desk..."
        ">She stands and suddenly Hermione extends her arm to you..."
        ">You see that she is clutching a small ball of fabric in her fist..."
        ">Her panties? You can't help but wonder how she managed to take them off so quickly..."
        m "Ah!"
        ">You got Hermiones panties..."
        hide screen blktone8
        with d3
        $herView.hideshowQQ( "body_67.png", pos )
        
        her "Just take them sir..."
        m "And you do so of your own volition?"
        her "Your speech was so moving..."
        her "You are so right, sir! I shall beat them at their own game!"
        her "Any small discomfort I may have...well, Gryffindor is worth it!"
        her "My classes are about to start, so I should probably go now..."
        ">You acquired Hermione's panties..."
        $herView.hideQQ()

        $ pos = POS_370
        $herView.showQQ( "body_23.png", pos )
        her "..........."
        $herView.hideshowQQ( "body_29.png", pos )
        her "...I hope nobody will notice that I have no underwear on today..."
        $herView.hideshowQQ( "body_31.png", pos )
        her "Oh, Professor, I will be back tonight to get them."
        m "Of course. Your panties will be right here on my desk, waiting for you..."
        $herView.hideshowQQ( "body_34.png", pos )
        her "(I wish he would not leave them out on his desk like that.  Someone might see!)"
        jump request_03_ends

    else: #<========================================================================================== FIRST EVENT!
#        if request_03_points == 0 and whoring < 12:
        if IsFirstRun() and hermi.whoring < 12:
            her "emm..."
            her " This is a surprise, sir, but..."
        if not IsFirstRun():
            her "Again, sir?"
            m "Yes again..."
        her "Here..."
        if hermi.whoring >= 12: #LEVEL 05
            $herView.hideQQ()
            ">Hermione pulls her panties out of her pocket..."
            m "What?"
            $herView.hideshowQQ( "body_45.png", pos )
            her "Yes, I had a feeling that you might ask for these today, sir."
            m "A feeling?"
            $herView.hideshowQQ( "body_68.png", pos )
            her "To be completely honest I find it more comfortable not to wear them much anymore..."
            if hermi.whoring >= 15: #LEVEL 05
                $herView.hideshowQQ( "body_78.png", pos )
                her "There can be different circumstances and panties will only hinder."
                m "Hinder?.."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ah, it doesn't matter, sir."
        else:
            $herView.hideQQ()
            ">Hermione takes off her panties and hands them over to you..."
        $herView.hideQQ()
        ">Hermione's panties acquired."
        $herView.showQQ( "body_15.png", pos )
        her "Well, my classes are about to start, so I'd better go now..."

        
    label request_03_ends:
    $ request_03 = True #True when Hermione has no Трусики on.
    if hermi.whoring <= 5:
        $ hermi.whoring +=1
        
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


    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###
    $wtevent.Finalize()
    jump day_main_menu
    
    
        
label new_request_03_complete: # WHORING LEVEL 02 <=================
    
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 2.5
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    show screen hermione_02
    with Dissolve(.3)

    $ pos = POS_120
    
    "Good evening, sir..."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    menu:
        "\"Here are your panties.\"":
            if have_cum_soaced_panties:
                jump panties_soaked_in_cum
            else:
                her "Thank you, sir."
                her "And my payment?"
                m "Of course."
        "\"How was your day, Miss Granger?\"":
            if  hermi.whoring <= 5: #LEVEL 02. EVENT LEVEL: 01
#                $ new_request_03_01 = True # HEARTS.

                $herView.hideQQ()
                $ pos = POS_120
                $herView.showQQ( "body_15.png", pos )
                her "Oh..."
                her "Quite ordinary actually..."
                $herView.hideshowQQ( "body_13.png", pos )
                her "Although I could not help but worry that somebody would notice somehow..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "....."
                $herView.hideshowQQ( "body_31.png", pos )
                her "Can I have my panties back now?"
                m "Of course..."
                $herView.hideQQ()
                ">You give Hermione her panties back..."
                if have_cum_soaced_panties:
                    jump panties_soaked_in_cum
                else:
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "And my payment?"
                    m "Yes, yes..."
            elif hermi.whoring >= 6 and hermi.whoring <= 8: #LEVEL 03. EVENT LEVEL 02.
#                $ new_request_03_02 = True # HEARTS.

                $herView.hideQQ()
                $ pos = POS_120
                $herView.showQQ( "body_15.png", pos )
                her "Oh..."
                her "It was quite ordinary really..."
                her "I spent some time with my classmates and went to classes, of course..."
                her "And we had a short MRM meeting after that..."
                #translators "Напоминание.\nОЗМП - Общество по Защите Мужских Прав."
                $herView.hideshowQQ( "body_16.png", pos )
                her "I gave a short speech on why it is wrong to sell sexual favours in exchange for House points..."
                $herView.hideshowQQ( "body_12.png", pos )
                her "I felt odd that I had to give the speech without any underwear on..."
                menu:
                    "\"You little hypocrite!\"":
                        $ hermi.liking -=5
                        $herView.hideshowQQ( "body_14.png", pos )
                        her "Professor?!  How dare you call me that!"
                        m "You sold your panties to me this morning..."
                        m "And a few hours later you publicly condemned that exact behavior..."
                        m "What would you call that?"
                        $herView.hideshowQQ( "body_69.png", pos )
                        her "It seems you are right, Professor..."
                        her "(But we need the points...)"
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Can I have my payment now please?"
                        m "What about your panties?"
                        $herView.hideshowQQ( "body_34.png", pos )
                        her "Oh, them too of course..."  
                        if have_cum_soaced_panties:
                            jump panties_soaked_in_cum
                        else:
                            pass
                    "\"It's for the greater good...\"":
                        her "Exactly!"
                        her "Gryffindor deserves those points, if only to offset those gotten immorally..."
                        her "It is not my fault that the system is so corrupted..."
                        $herView.hideshowQQ( "body_16.png", pos )
                        her "I shall remain a symbol of righteousness to my peers, no matter what!"
                        her "(no matter what I have to do sometimes...)"
                        $herView.hideshowQQ( "body_31.png", pos )
                        her "Can...can I just have my panties back now, please?"
                        if have_cum_soaced_panties:
                            jump panties_soaked_in_cum
                        else:
                            her "And my payment."
            elif hermi.whoring >= 9: #LEVEL 04. EVENT LEVEL 03.
#                $ new_request_03_03 = True # HEARTS.

                $herView.hideQQ()
                $ pos = POS_120
                $herView.showQQ( "body_16.png", pos )
                her "Another ordinary day at Hogwarts..."
                her "Nothing remarkable..."
                if hermi.whoring>=15:
                    m m "No more linen does not deliver you inconvenience, miss Granger?"
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "Inconvenience, sir? What are you... Oh, that!"
                    her "Well, we are grown people, Professor. If a girl doesn't wear underwear, so what?..."
                    m "Hmm... Really."
                else:
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "Although I must admit..."
                    her "I was oddly free without underwear..."
                her "Hm..."
                $herView.hideshowQQ( "body_45.png", pos )
                her "Can I have my panties back now please?"
                m "Of course..."
                $herView.hideQQ()
                ">You give Hermione her panties back..."
                if have_cum_soaced_panties:
                    jump panties_soaked_in_cum
                else:
                    $herView.hideshowQQ( "body_45.png", pos )
                    her "And my payment?"
                    m "Yes, yes..."

    label back_from_panties:
    $ gryffindor +=15
    m "Fifteen points to Gryffindor, Miss Granger. Well deserved." 
    her "Thank you, sir..."
    m "You can go now."
    her "Good night, sir."
    m "Yes, good night..."

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



#    $ request_03_points += 1 #Leveling up the event.
    $ request_03 = False #When False - you gave her her panties back.
    $ hermione_sleeping = True

    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC

    if hermi.whoring<15:
        $SetHearts(GetStage(hermi.whoring, 3, 3, 3), this.new_request_03)
    else:
        $SetHearts(4, this.new_request_03)

    $wtevent.Finalize()    
    return 
    
    
    
### PANTIES SOAKED IN CUM ###
label panties_soaked_in_cum:
    $ have_cum_soaced_panties = False #TRUE when you have the panties in your possession (before you return them to Hermione).
    $ she_knows_about_cum = False
    $ pos = POS_120
    
    if hermi.whoring >= 3 and hermi.whoring <= 5: # LEVEL 02
        $herView.hideshowQQ( "body_71.png", pos )
        her "Hm....?"
        $herView.hideshowQQ( "body_05.png", pos )
        her "Sir? What is this?"
        her "What have you done to them?"
        $herView.hideshowQQ( "body_07.png", pos )
        her "They are covered in something slimy..."
        menu:
            "\"An experiment went wrong\"":
                $herView.hideshowQQ( "body_02.png", pos )
                her "An experiment went wrong, sir?"
                m "Yes... Or should I say..."
                g9 "\"An experiment went very right\"? He-he..."
                $herView.hideshowQQ( "body_07.png", pos )
                her ".....................?"
                her "What kind of experiment was it?"
                m "What? Oh..."
                m "Something having to do with ectoplasm.  It required a small personal item..."
                m "It's a bit advanced to discuss with a student."
                $herView.hideshowQQ( "body_05.png", pos )
                her "................................"
            "\"You gave them to me like this!\"":
                her "I most certainly did not, sir!"
                her ".........................."
        $herView.hideshowQQ( "body_71.png", pos )
        her "Well, these will require some serious cleaning before I can put them on again..."
        m "Or you could put them on now.  They aren't that bad."
        $herView.hideshowQQ( "body_14.png", pos )
        her "What?"
        $herView.hideshowQQ( "body_13.png", pos )
        her "I really would rather not, sir..."
        menu:
            "\"Put them on or lose the points!\"":
                $ hermi.liking -=7
                $herView.hideshowQQ( "body_72.png", pos )
                her "What?"
                her "Professor, you are joking, right?"
                m "I am not.  There is nothing wrong with them."
                $herView.hideshowQQ( "body_31.png", pos )
                her "B-but..."
                $herView.hideshowQQ( "body_33.png", pos )
                her "........................................"
                $herView.hideshowQQ( "body_47.png", pos )
                her "(Must you always have your way, sir?)"
                m "What was that, Miss Granger?"
                $herView.hideshowQQ( "body_30.png", pos )
                her "It's nothing, sir."
                her "(Imagine! Making me put my panties on when I don't want to wear them!)"
                $herView.hideQQ()
                show screen blktone8
                with d3
                ">Hermione hesitantly puts on her panties..."
                ">They leave a tiny smear of cum sliding down one of her legs..."
                ">Hermione looks very uncomfortable..."
                hide screen blktone8
                with d3
                $herView.hideshowQQ( "body_34.png", pos )
                her "......................"
            "\"Well, suit yourself...\"":
                pass
    if hermi.whoring >= 6 and hermi.whoring <= 8: # LEVEL 03 (SECOND EVENT)
        $herView.hideshowQQ( "body_71.png", pos )
        her "My panties..."
        $herView.hideshowQQ( "body_73.png", pos )
        her "What happened to them sir?"
        menu: 
            "\"An experiment went wrong.\"":
                her "Hm..."
                her "I see..."
            "\"You gave them to me like this!\"":
                her "Did I? Oh, well..."
        $herView.hideQQ()
        ">Hermione gives her cum-soaked underwear a quizzical look..."
        $herView.hideshowQQ( "body_71.png", pos )
        her "Seems like these will require some serious cleaning before I can put them on again..."
        m "Why not wear them now?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Hm....?"
        $herView.hideshowQQ( "body_71.png", pos )
        her "Well, I suppose I could wear them one more time before putting them into the laundry..."
        $herView.hideQQ()
        show screen blktone8
        with d3
        ">Hermione puts her panties on..."
        hide screen blktone8
        with d3
        $herView.hideshowQQ( "body_34.png", pos )
        her "Will this be all, sir?"
        $herView.hideshowQQ( "body_44.png", pos )
        her "(It doesn't feel that bad...)"
    if hermi.whoring >= 9: #LEVEL 04+ (THIRD EVENT)
        $herView.hideshowQQ( "body_71.png", pos )
        her "My panties..."
        if not IsFirstRun():
            her "They are covered in something slimy again..."
        else:
            her "They are covered in something slimy..."
        her "And they smell funny..."
        $herView.hideshowQQ( "body_29.png", pos )
        her "Hm... That smell..."
        her "It's familiar somehow..."
        $herView.hideshowQQ( "body_45.png", pos )
        her "What exactly did you do to them, sir?"
        menu:
            "\"An experiment went wrong\"":
                her "An experiment, huh?"
                her "Of what nature?"
                $herView.hideshowQQ( "body_46.png", pos )
                her "No, don't answer that... I think I know..."
            "\"You gave them to me like this!\"":
                her "I don't think so, sir."
                her "But it's alright if you don't want to tell me, sir..."
                her "I think I know exactly what happened to them..."
            "\"I came all over them!\"":
                $ she_knows_about_cum = True
                $herView.hideshowQQ( "body_64.png", pos )
                her "I knew it..."
                her "They reek of semen!"
        $herView.hideshowQQ( "body_68.png", pos )
        her "Hm..."
        her "Seems like these will require some serious cleaning before I can put them on..."
        $herView.hideshowQQ( "body_64.png", pos )
        her "Unless you want me to put them on now, sir...?"
        menu: 
            "\"Yes! Put them on now, girl!\"":
                her "Well, if you like..."
            "\"I don't care. Do what you want.\"":
                her "Why not put them on one more time?"
        
        $herView.hideshowQQ( "body_74.png", pos )
        her "I am only doing this to give my house a fair chance at winning the cup this year..."
        m "Right..."
        her "It isn't as though I enjoy the thought of someone's cum smeared all over my pussy, you know."
        m "I would never have considered such a thing."
        
        $herView.hideQQ()
        
        show screen blktone8
        with d3
        ">Hermione swiftly slides her drenched panties on..."
        hide screen blktone8
        with d3
        
        # NEW Branch :)
        $pos = POS_120
        if she_knows_about_cum == True and hermi.whoring >= 12:
            $herView.showQQ( "body_58.png", pos )
            her "...sir?"
            m "Yes?"
            $herView.hideQQ()
            
            $herView.showQQ( "body_58.png", pos )
            her "A girl I know told me that guys like all kinds of...perversions."
            $herView.hideshowQQ( "body_129.png", pos )
            her "Is that right, sir?"
            m "Hmm, well, I think it depends on what you consider a \"perversion\"..."
            m "What specifically are you talking about?"
            $herView.hideshowQQ( "body_84.png", pos )
            her "Well, for example..."
            $herView.hideQQ()
            
            $herView.data().saveState()
            #$herView.data().addPose( CharacterExItemSkirtLifted( herView.mPoseFolder, 'pose_skirt_up.png', G_Z_POSE ) )
            $herView.data().addItem( 'item_pose_lifted_skirt' )
            #$herView.data().addItemKey( 'panties_cum', CharacterExItem( herView.mMiscFolder, 'panties_sperm.png', G_Z_PANTIES + 1, 'panties' ) )
            $herView.data().addItem( 'item_panties_sperm' )
            
            $herView.showQQ( "185.png", pos )
            her "...if they were to see a girl wearing panties soaked in their cum?"
            pause
            menu:
                "\"Of course! Any man would be excited by that!\"":
                    $herView.hideshowQQ( "body_128.png", pos )
                    her "I thought so, Professor."
                    $herView.hideQQ()
                    $herView.data().loadState()
                    $herView.showQQ( "body_52.png", pos )
                    her "Then I may go?"
                    m "Hmm, Yes, Miss Granger..."
                    $herView.hideshowQQ( "body_64.png", pos )
                    her "You have not forgotten anything, sir?"
                    m "Оh..."
                    $herView.hideshowQQ( "body_45.png", pos )

                "\"I think that would be a sick pervert!\"":
                    $hermi.liking -= 15
                    $herView.hideQQ()
                    $herView.data().loadState()
                    $herView.showQQ( "body_51.png", pos )
                    her "Hmmph!"
                    $herView.hideshowQQ( "body_191.png", pos )
                    her "I would like my points, then!"
                    
                    
    jump back_from_panties
