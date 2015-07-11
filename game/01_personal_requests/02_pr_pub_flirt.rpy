
###################REQUEST_02_b (LEVEL 01) ### FLIRT WITH CLASSMATES ###
label new_request_02_b:
    $herView.hideQQ()
    m "{size=-4}(Ask her to go flirt with some boys from \"Slytherin\"?){/size}"
    $ menu_x = 0.5 #Default menu position restored.
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $wtevent.NotFinished()
            jump new_personal_request
    
    m "Miss granger?"
    $ pos = POS_140
    $herView.showQQ( "body_13.png", pos )
    her "Yes?"
    
    if request_02_b_points == 0 and hermi.whoring <= 5: ### LEVEL 01 and LEVEL 02
        ### LEVEL 01 ### <===============================================================FIRST EVENT!
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        m "What is your opinion on the boys of the \"Slytherin\" house?"
        $herView.hideshowQQ( "body_05.png", pos )
        her "I detest them, sir."
        m "Well, too bad. Because I want you to get really friendly with a few of them today."
        $herView.hideshowQQ( "body_13.png", pos )
        her "If I must..."
        her "Yes, I think I can manage to be civil with them for one day."
        m "Yes, and when I say \"get friendly with them...\""
        m "I actually mean that I need you to flirt with them..."
        $herView.hideshowQQ( "body_48.png", pos )
        her "Flirt?!"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Professor Dumbledore!"
        $herView.hideshowQQ( "body_17.png", pos )
        her "I'm not even going to ask why you'd be interested in this, sir..."
        $herView.hideshowQQ( "body_11.png", pos )
        her "But why \"Slytherin\"?"
        her "If you need me to be flirtatious today, I think I can manage that..."
        her "But, please, can't be another house?"
        $herView.hideshowQQ( "body_44.png", pos )
        her "The \"Gryffindors\" maybe?"
        m "I am only trying to protect your reputation, miss Granger."
        $herView.hideshowQQ( "body_15.png", pos )
        her "Sir?"
        m "Do you value the opinion the \"Slytherin\" students have of you?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "I couldn't care less about the opinions of those Neanderthals."
        m "What about the students of the \"Gryffindor\" house?"
        $herView.hideshowQQ( "body_29.png", pos )
        her "Their opinion means the world to me--"
        $herView.hideshowQQ( "body_06.png", pos )
        her "Oh, I see..."
        m "Exactly... Just looking out for you miss Granger."
        her "Em... Thank you professor..."
        call music_block
    
    else:
        if hermi.whoring <= 2: ### LEVEL 01
            m "I need you to go make some new friends at \"Slytherin\" house."
            her "You mean you need me to flirt with the \"Slytherin\" boys again sir?"
            m "That's exactly what I need you to do today, Miss Granger."
            $herView.hideshowQQ( "body_02.png", pos )
            her "Must I really do this sir?"
            m "We have been through this, girl."
            m "Going to the \"Slytherin\" boys is in your best interests."
            $herView.hideshowQQ( "body_04.png", pos )
            her "Yes, I know, sir."
            her "But why must I this at all?"
            m "Nobody is forcing you, miss granger..."
            $herView.hideshowQQ( "body_05.png", pos )
            her "You don't need to remind me of that, sir..."
            $herView.hideshowQQ( "body_07.png", pos )
            her "Alright if I must... Sir..."


        else: #if whoring >= 3 and whoring >= 6: ### LEVEL 02 and higher ## <=========================================================== SECOND EVENT!
            m "I need you to flirt with some boys of the \"Slytherin\" house today."
            her "I will see what I can do, sir."
            m "Great. I'll be expecting your report today after classes."

    
    her "Well, I'd better go now. Classes are about to start..."
#    $ request_02_b = True

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

    $wtevent.Finalize()    

    jump day_main_menu
   
        
        
label new_request_02_b_complete:
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
        "\"Great. You earned your points.\"":
            pass
        "\"Give me the details.\"":
            $herView.hideQQ()
            m "How many boys did you flirt with today, miss Granger?"
            m "Give me the details."
            show screen blktone
            with d3
            if hermi.whoring >= 0 and hermi.whoring <= 2: ### LEVEL 01
                if one_out_of_three == 1: ### EVENT (A)
                    
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Well..."
                    her "There was this one freshman boy..."
                    her "........."
                    m "I'm listening..."
                    her "Well... I went to him and I said \"Hey, handsome!\"."
                    m "And?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_07.png", pos )
                    her "He showed me his tongue and ran off, sir."
                    m "Did you try to lure him in with a lolipop?"
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "I did not, sir..."
                    her "The thought never crossed my mind, but--"
                    m "That was a joke, miss Granger."
                    $herView.hideshowQQ( "body_07.png", pos )
                    her "Sir?"
                    m "I didn't send you out there to harass little kids!"
                    $herView.hideshowQQ( "body_09.png", pos )
                    her "............."
                    m "I told you to flirt with boys {size=+5}your{/size} age!"
                    $herView.hideshowQQ( "body_07.png", pos )
                    her "I wanted to at first, but..."
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "I guess I got scared..."
                    her "I mean I despise those \"Slytherins\" way too much to flirt with them, sir!"
                    $herView.hideshowQQ( "body_05.png", pos )
                    her "I would have to fight my gag-reflex the entire time!"
                    menu:
                        "\"Fine. Just try harder next time.\"":
                            $herView.hideshowQQ( "body_06.png", pos )
                            her "Thank you, sir."
                            her "I will, I promise!"
                        "\"Favour failed! No points for you!\"":
                            stop music fadeout 1.0
                            $herView.hideshowQQ( "body_07.png", pos )
                            her "I understand..."
                            m "Get out of my sight..."
                            $herView.hideshowQQ( "body_09.png", pos )
                            her "Yes, Sir...Sorry, Sir..."
                            jump could_not_flirt
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Well, I tried to complement an upperclassman..."
                    m "Did he appreciate it?"
                    $herView.hideshowQQ( "body_76.png", pos )
                    her "He called me a \"Gryffindor whore\", sir!"
                    m "I see..."
                    m "What did you do then?"
                    $herView.hideshowQQ( "body_04.png", pos )
                    her "Well that was not the proper way to address a fellow \"Hogwarts\" student..."
                    her "So I told him that I would report him."
                    m "A truly captivating story..."
                    m "Anything else?"
                    $herView.hideshowQQ( "body_09.png", pos )
                    her "Yes, there was also this one student at the library..."
                    her "He was obviously struggling with a problem..."
                    her "So I offered my help..."
                    m "And?"
                    $herView.hideshowQQ( "body_76.png", pos )
                    her "He called me a \"Patronizing Gryffindor Whore\", sir..."
                    m "Did you threaten to report him as well?"
                    $herView.hideshowQQ( "body_04.png", pos )
                    her "Of course, sir."
                    m "*sigh*"
                    m "Anything else?"
                    $herView.hideshowQQ( "body_09.png", pos )
                    her "Well, there was one more incident but the outcome was pretty much the same..."
                    m "\"The Gryffindor whore\"?"
                    $herView.hideshowQQ( "body_66.png", pos )
                    her ".........yes, sir."
                    m "You are doing it all wrong, miss Granger."
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "I am sorry, professor. I thought this would be easy..."
                    menu:
                        "\"Well, at least you are trying.\"":
                            $herView.hideshowQQ( "body_34.png", pos )
                            her "Apparently flirting is not my forte..."
                        "\"Favour failed! No points of you!\"":
                            stop music fadeout 1.0
                            $herView.hideshowQQ( "body_11.png", pos )
                            $ hermi.liking -=15
                            her "You are not going to pay me, sir?"
                            $herView.hideshowQQ( "body_21.png", pos )
                            her "But, you promised!"
                            $herView.hideshowQQ( "body_20.png", pos )
                            her "................"
                            call music_block
                            jump could_not_flirt
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Well, the \"Slytherin\" quidditch team was practicing in the stadium today..."
                    her "I thought I could sneak into the bleachers and cheer them on..."
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "But..."
                    m "Yes?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_77.png", pos )
                    her "A whole flock of those \"Slytherin\" harlots was already there, sir."
                    her "They were cheering and yelling..."
                    $herView.hideshowQQ( "body_47.png", pos )
                    her "And one of them even exposed herself in an inappropriate manner to the players, sir..."
                    her "I cannot believe our school accepts such behavior..."
                    m "So... how did this captivating drama end?"
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "I just left sir..."
                    menu:
                        m "Hm..."
                        "\"Well, here are your points.\"":
                            $herView.hideshowQQ( "body_16.png", pos )
                            her "Thank you, sir..."             
                            
                        "\"Favour failed! No points for you!\"":
                            stop music fadeout 1.0
                            $herView.hideshowQQ( "body_12.png", pos )
                            her "I don't feel like I deserved any this time anyway..."
                            call music_block
                            jump could_not_flirt
                    
                    
                    
                    
            elif hermi.whoring >= 3 and hermi.whoring <= 5: ### LEVEL 02
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    $herView.hideQQ()
                    $ pos = POS_140
                    $herView.showQQ( "body_10.png", pos )
                    her "Well, there was this one guy at the library..."
                    her "He was obviously struggling with some assignment, so I offered my help..."
                    m "And?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "Well, to my surprise he accepted it..."
                    her "He let me finish the assignment for him..."
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "While I was working he made a couple of inappropriate comments but I just smiled in response..."
                    m "So, basically, he was the one doing the flirting..."
                    $herView.hideshowQQ( "body_24.png", pos )
                    her "well... yes."
                    $herView.hideshowQQ( "body_45.png", pos )
                    her "But, despite my better judgment I did encourage his improper behavior..."
                    m "By being quiet?"
                    her "Yes sir..."
                    her "I mean, this does amount to something, right?"
                    m "Meh..."
                    m "What else do you have for me?"
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "Right..."
                    her "Later in a corridor these two other guys complemented my appearance in a very vulgar manner..."
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "But I just smiled at them..."
                    m "You were on the receiving end again, then..."
                    m "This is not what I ordered you to do, miss Granger."
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "I know, sir!"
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "But I am so busy. Between the \"MRM\" meetings and the classes..."
                    her "I barely have any time--"
                    m "Is this all you got for me this time then?"
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "No, sir."
                    her "Just an hour ago or so I ran into Draco Malfoy, sir."
                    m "No way!!! (No idea who that is...)"
                    her "I forced myself to be friendly with him and..."
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "We ended up having a decent conversation for a change." 
                    m "I see... That \"Dark-oh\" guy..."
                    m "Was he looking at your legs at all?"
                    m "He looked at your feet?"
                    $herView.hideshowQQ( "body_02.png", pos )
                    her "What?"
                    m "Did he stare at your legs or not, girl?"
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "Em... He might have..."
                    m "What about your tits?"
                    $herView.hideshowQQ( "body_47.png", pos )
                    her "Professor!!!"
                    m "Fine. You get your points. Keep up the good work."
                    $herView.hideshowQQ( "body_29.png", pos )
 
                elif one_out_of_three == 2: ### EVENT (B)
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Well..."
                    her "This morning I did flirt with this one guy..."
                    $herView.hideshowQQ( "body_13.png", pos )
                    her "Then after the second period there was this other guy..."
                    $herView.hideshowQQ( "body_28.png", pos )
                    her "And then something bizarre happened..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "This angry-looking guy from the \"Slythetin\" came to me and asked me out on a date..."
                    $herView.hideshowQQ( "body_13.png", pos )
                    her "I told him \"no\" at first, but we ended up taking a walk together."
                    m "Did you enjoy yourself, miss Granger?"
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "I think I did sir... To my own astonishment..."
                    $herView.hideshowQQ( "body_45.png", pos )
                    her "There was something about his \"devil-may-care\" attitude..."
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "He was so confident and calm and..."
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "I still loathe the \"Slytherin\" house of course!"
                    $herView.hideshowQQ( "body_73.png", pos )
                    her "But..."
                    her "Maybe some of the students got there by mistake?"
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Could the \"sorting hat\" make... miscalculations ?"
                    menu:
                        "\"Just take your points and go!\"":
                            $herView.hideshowQQ( "body_07.png", pos )
                            her "................"
                        "\"The almighty hat is never wrong!\"":
                            $herView.hideshowQQ( "body_13.png", pos )
                            her "Yes, of course... Everybody knows that..."
                        "\"Could what make what?\"":
                            $herView.hideshowQQ( "body_13.png", pos )
                            her "Oh, nevermind me, sir."
                            her "Everyone knows that the \"Sorting Hat\" is never wrong."
                    
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "Five guys, sir!"
                    m "Really?"
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Yes!"
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "This one guy this morning."
                    her "Then another two right after the first period."
                    her "And then another one before the third period."
                    $herView.hideshowQQ( "body_68.png", pos )
                    her "And after that I had a surprisingly pleasant conversation with one more."
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "That last one was quite smart and well mannered too."
                    her "............................"
                    her "................"
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "But I still refuse to change my opinion about the \"Slytherin\" house, sir."
                    m "I'm not asking you to, miss Granger."
                    her "I am only doing this to help my own house!"
                    $herView.hideshowQQ( "body_32.png", pos )
                    her "The proud house of \"Gryffndor\"!"
                    m "Alright, alright, calm down, girl."
                    $herView.hideshowQQ( "body_74.png", pos )

            elif hermi.whoring >= 6: # LEVEL 03 and higher.
                if one_out_of_three == 1: ### EVENT (A)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "Eleven boys, sir!"
                    m "Eleven? Really? Your personal best, miss Granger."
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Yes."
                    $herView.hideshowQQ( "body_68.png", pos )
                    her "Let's see..."
                    her "Those two handsome guys right before the first period started..."
                    $herView.hideshowQQ( "body_64.png", pos )
                    her "Then I exchanged a few rather inappropriate messages with this other guy, during the the first period."
                    $herView.hideshowQQ( "body_68.png", pos )
                    her "After that there was this one other guy..."
                    $herView.hideshowQQ( "body_73.png", pos )
                    her "Then those three guys..."
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Then one more right before the last period..."
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "And finally this last guy that walked me right to your tower, sir..."
                    m "So, eleven then?"
                    m "Those \"Slytherin\" boys are really starting to like you, huh?"
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "I suppose so..."
                    $herView.hideshowQQ( "body_73.png", pos )
                    her "Well, not all of them were nice to me at first..."
                    $herView.hideshowQQ( "body_64.png", pos )
                    her "But I use this trick to \"tame\" them."
                    m "A trick?"
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Yes... Whenever a boy from \"Slytherin\" is being mean to me or calls me a name..."
                    her "I just swallow my pride and smile in response."
                    m "Hm..."
                    m "So, if for example, somebody were to call you a \"whore\" you would just smile at them?"
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Well, yes, sir..."
                    m "Yeah, I'm sure that wins them over."
                    m "Great job, miss Granger."
                    $herView.hideshowQQ( "body_68.png", pos )
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "Two dates, seven quite pleasant conversations..."
                    $herView.hideshowQQ( "body_68.png", pos )
                    her "And I even let this one guy kiss me..."
                    m "Quite impressive, miss Granger."
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "I think so too, sir. Thank you."
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "Oh, and there was also this little freshman kid..."
                    her "I tried to flirt with him too, but we ended up just chatting..."
                    her "He kept calling me \"Miss Hermione\"..."
                    her "So adorable..."
                    m "Well I didn't send you to harass little kids, miss Granger."
                    $herView.hideshowQQ( "body_66.png", pos )
                    her "I didn't haras--"
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Sir! Seven flirts and two dates amount to something, don't they?"
                    m "Oh, absolutely."
                    $herView.hideshowQQ( "body_30.png", pos )
                    her "Then I would like to receive my payment now..."
                    $herView.hideshowQQ( "body_33.png", pos )
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_33.png", pos )
                    her "Sir, I am sorry, but..."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_47.png", pos )
                    her "I hate those \"Slytherin\" tramps, sir!"
                    m "Tell me what happened."
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "I don't want to talk about it..."
                    m "Tell me what happened, girl!"
                    $herView.hideshowQQ( "body_76.png", pos )
                    her "I don't want to talk about it, sir."
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "Please don't make me..."
                    menu:
                        "\"Fine. I'll let it go for today.\"":
                            $herView.hideshowQQ( "body_33.png", pos )
                            her "Thank you, sir."
                            m "No luck with the flirting today then?"
                            $herView.hideshowQQ( "body_34.png", pos )
                            her "Oh, quite the opposite, sir."
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            her "One of the boys actually took me to the \"Slytherin\" common room today..."
                            $herView.hideshowQQ( "body_03.png", pos )
                            her "There were at least a dozen of them there..."
                            $herView.hideshowQQ( "body_04.png", pos )
                            her "All of the boys knew who I was..."
                            her "I was the center of attention at first..."
                            $herView.hideshowQQ( "body_78.png", pos )
                            her "And it felt sort of wonderful..."
                            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                            $herView.hideshowQQ( "body_66.png", pos )
                            her "Then a bunch of those \"Slytherin\" harlots stumbled in and..."
                            m "And?"
                            $herView.hideshowQQ( "body_69.png", pos )
                            her "Well, they started saying stuff and doing things..."
                            her "Anyway, I had to leave..."
                            m "I see..."
                            m "Well, I say you deserve your points anyway, miss Granger."
                            $herView.hideshowQQ( "body_74.png", pos )

                        "\"Tell me now, or lose the points!\"":
                            $ hermi.liking -=10
                            $herView.hideshowQQ( "body_66.png", pos )
                            her "Sir, please, I don't want to discuss this with you, sir."
                            m "No one is forcing you, miss Granger."
                            m "You are free to leave."
                            $herView.hideshowQQ( "body_47.png", pos )
                            her "{size=-4}(Stubborn old man!){/size}"
                            jump could_not_flirt
                            
                            
    
    $ gryffindor +=5
    m "The \"Gryffindor\" house gets 5 points!"
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




    $ request_02_b_points += 1
#    $ request_02_b = False 
    $ hermione_sleeping = True
    
    $ p_level_02_active = True #When turns TRUE public favors of level 02 become available. 

    $wtevent.Finalize()    
    
    if hermi.whoring <= 2:
        $ hermi.whoring +=1
        
    call music_block
    return        

