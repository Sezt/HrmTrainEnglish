
###################REQUEST_20 (Level 05) (45 pt.) (MAKE OUT WITH A GIRL). (Available during daytime only). #####################################################################################
label new_request_20: #LV.5 (Whoring = 12 - 14)
    
        
        
    $herView.hideQQ()
    m "{size=-4}(Tell her to go make out with one of her female classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request
            
    
    $ pos = POS_140
    
    if request_20_points == 0: # <================================================================================ FIRST TIME
        m "Have You ever kissed another girl, miss Granger?"
        $herView.hideshowQQ( "body_07.png", pos )
        her "?!"
        
        if whoring <=11 or request_15_points <= 1: # Counts how many times you sent Hermione to flash a classmate.
            jump too_much
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $herView.hideshowQQ( "body_02.png", pos )
        her "I am not a... lesbian, sir."
        m "Silly girl... You don't need to be a lesbian to kiss girls."
        m "I mean, I do it and I am not a lesbian either."
        $herView.hideshowQQ( "body_05.png", pos )
        her "..............."
        her "Sir--"
        m "No, \"sirs\"! This is your task for today!"
        m "Go find a cute little thing and plant a \"smooch\" on her!"
        $herView.hideshowQQ( "body_11.png", pos )
        her "Sir, but I am--"
        m "Dismissed, miss Granger."
        $herView.hideshowQQ( "body_07.png", pos )
        her "Sir!......"
        m "I said you're dismissed."
        $herView.hideshowQQ( "body_09.png", pos )
        her "*Humph!*..."

    else: # <================================================================================ NOT FIRST TIME
        m "A forty five house points worth of favour is up for grabs!"
        m "Are you interested, miss Granger?"
        if whoring >= 12 and whoring <= 14: # LEVEL 05 FIRST EVENT.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $herView.hideshowQQ( "body_03.png", pos )
            her "It depends..."
            her "Will I have to do something depraved again?"
            m "\"Depraved\"??! When did I ever--?"
            $herView.hideshowQQ( "body_04.png", pos )
            her "Really, sir?"
            m "Fine, fine... But all I want you to do today is to make out with another girl."
            $herView.hideshowQQ( "body_05.png", pos )
            her "Oh, is that all?" # :(
            m "Yes... Pretty basic stuff for you, right?"
            m "And you will be getting forty five house points afterwards of course."
            $herView.hideshowQQ( "body_07.png", pos )
            her "............."
            m "So... Are you up for it?"
            $herView.hideshowQQ( "body_69.png", pos )
            her "I will see what I can do, sir..."
            m "Great. See you after your classes then."
            $herView.hideshowQQ( "body_79.png", pos )
            her "................"

        elif whoring >= 15 and whoring <= 17: # LEVEL 06. Event level 02.
            $herView.hideshowQQ( "body_70.png", pos )
            her "I suppose..."
            m "Great. All you need to do is make out with another girl."
            $herView.hideshowQQ( "body_71.png", pos )
            her "I see..."
            m "Up for the task, miss Granger?"
            $herView.hideshowQQ( "body_29.png", pos )
            her "I suppose..."
            m "Great. See you after your classes then."

            
        elif whoring >= 18: # LEVEL 07+ Event level 03.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $herView.hideshowQQ( "body_06.png", pos )
            her "Sure, why not?"
            m "Great."
            m "I want you to make out with another girl today."
            $herView.hideshowQQ( "body_45.png", pos )
            her "Alright."
            $herView.hideshowQQ( "body_64.png", pos )
            her "I know a couple of girls who are hungry for attention and wouldn't mind putting on a little show."
            m "Great. See you after your classes then."

    

    
    $ request_20 = True

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
    
    call music_block 
    
    jump day_main_menu
    
    

        

label new_request_20_complete: # <=================================================================================================== EVENING
    
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

    $ request_20 = False 

    if whoring >= 12 and whoring <= 14: # LEVEL 05                    
        if one_out_of_three == 1: ### EVENT (A)
            stop music fadeout 1.0
            m "Miss Granger..."
            m "Did you succeed in completing your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_11.png", pos )
            her "I..."
            m "I told you to make out with another girl..."
            m "Did you do it?"
            $herView.hideshowQQ( "body_10.png", pos )
            her "I..."
            her "I tried, sir. I really did."
            m "And?"
            $herView.hideshowQQ( "body_29.png", pos )
            her "Well..."
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "It was awkward and embarrassing..."
            m "did you do it or not?"
            $herView.hideshowQQ( "body_69.png", pos )
            her "...no I did not, sir..."
            her "All I did was making a complete fool out of myself..."
            $herView.hideshowQQ( "body_47.png", pos )
            her "In front of the entire class..."
            m "Tell me what happened, girl."
            $herView.hideshowQQ( "body_69.png", pos )
            her "No, I will not, sir."
            her "Not in a million years!"
            $herView.hideshowQQ( "body_132.png", pos )
            her "Why do I have to perform such ridiculous tasks anyway?!"
            her "What is the point of all this?"
            $herView.hideshowQQ( "body_30.png", pos )
            her "I hate this!"
            $herView.hideshowQQ( "body_69.png", pos )
            her "..............."
            her "................."
            m ".............."
            m "You are not getting paid, you know that, right?"
            $herView.hideshowQQ( "body_30.png", pos )
            her "I don't care..."
            $ mad +=25
            jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
            
        elif one_out_of_three == 2: ### EVENT (B)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_16.png", pos )
            her "I did, sir..."
            m "Good. Give me the details."
            $herView.hideshowQQ( "body_17.png", pos )
            her "Well, I kissed a girl. Just like you told me to, sir."
            m "I guess it was embarrassing for you, girl?"
            $herView.hideshowQQ( "body_69.png", pos )
            her "Very much so, sir." # :( D: :D::D:D:D::D::D::D::DDD:DD
            m "Did you enjoy it though?"
            $herView.hideshowQQ( "body_79.png", pos )
            her "*Humph!*..."
            m "So you kissed a girl and you liked it?"
            $herView.hideshowQQ( "body_66.png", pos )
            her "Yes..."
            m "Did your tongues touch?"
            $herView.hideshowQQ( "body_66.png", pos )
            her "Yes..."
            her "It was a proper deep kiss, if that's what you want to know."
            her "Can I just get my payment now?"
            $herView.hideshowQQ( "body_69.png", pos )
            her "Please, sir..."
            m "Well, alright..."

        elif one_out_of_three == 3: ### EVENT (C)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_16.png", pos )
            her "Yes, I did, sir."
            m "Good. Tell me how it went."
            $herView.hideshowQQ( "body_16.png", pos )
            her "It went well, sir."
            m "Great. Give me the details."
            $herView.hideshowQQ( "body_04.png", pos )
            her "What would you like to know, sir?"
            m "Tell me everything! Was the girl pretty?"
            m "Did she return your kiss?"
            $herView.hideshowQQ( "body_08.png", pos )
            her "She was relatively pretty, sir."
            her "And she did return my kiss..."
            $herView.hideshowQQ( "body_184.png", pos )
            her "..........."
            $herView.hideshowQQ( "body_08.png", pos )
            her "Anything else, sir?"
            m "...."
            m "Why are you being difficult, girl?"
            $herView.hideshowQQ( "body_04.png", pos )
            her "With all due respect, sir..."
            her "You told me to make out with another girl, and I did..."
            $herView.hideshowQQ( "body_03.png", pos )
            her "Now, I would like to get paid if you would be so kind."
            m "......................"
            menu:
                "\"I don't appreciate your attitude, girl.\"":
                    $herView.hideshowQQ( "body_04.png", pos )
                    her "Well, that is unfortunate, sir."
                    m "Sure is..."
                    m "Because you are not getting paid you insolent, little witch."
                    $herView.hideshowQQ( "body_03.png", pos )
                    stop music fadeout 1.0
                    her "What?"
                    $herView.hideshowQQ( "body_11.png", pos )
                    her "Sir, you can't do that!"
                    m "Dismissed."
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "B-but--"
                    $herView.hideshowQQ( "body_11.png", pos )
                    her "Sir, please!"
                    her "The girl was from \"Hufflepuff\" and--"
                    m "Too late for that, miss Granger."
                    m "You are dismissed."
                    $herView.hideshowQQ( "body_21.png", pos )
                    her "......"
                    $ mad +=25
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                            
                "\"Fine. Here is your payment, girl.\"":
                    pass



    elif whoring >= 15 and whoring <= 17: # LEVEL 06. Event level 02.     
        if one_out_of_three == 1: ### EVENT (A)
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_16.png", pos )
            her "I did, sir..."
            m "Well, don't just stand there. Give me the details."
            $herView.hideshowQQ( "body_14.png", pos )
            her "Ehm, alright..."
            her "The girl was from \"Ravenclaw\"..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "I think she may have been an underclassman, but I did not ask..."
            her "We got to talking about boys..."
            $herView.hideshowQQ( "body_16.png", pos )
            her "And she told me that she never kissed one..."
            her "And that she is worried that she might be very bad at it..."
            $herView.hideshowQQ( "body_06.png", pos )
            her "So I just offered my help..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "And then we spent some time in one of the bathroom stalls..."
            $herView.hideshowQQ( "body_45.png", pos )
            her "Making out..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "She caught on real quick... I think she could be really good at it with some practice..."
            $herView.hideshowQQ( "body_45.png", pos )
            her "Also she was quite adorable..."
            $herView.hideshowQQ( "body_46.png", pos )
            her "She kept calling me \"Miss Granger\"..."
            m "Hm..."
            m "I Don't recall sending you out with a task to confuse little kids, miss Granger."
            $herView.hideshowQQ( "body_64.png", pos )
            her "\"Little kids\"? Sir, please..."
            her "You should have seen that girl..."
            her "A little petite? Maybe... But definitely not a \"kid\"."
            $herView.hideshowQQ( "body_111.png", pos )
            her "And I assure you that she was anything but confused."
            her "In fact, at the end of our \"Study session\" she got rather obnoxious..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "And it sort of felt as if she was taking advantage of me..."
            m "Oh... Well, in that case..."
            $herView.hideshowQQ( "body_45.png", pos )

            
        elif one_out_of_three == 2: ### EVENT (B)
            m "Miss Granger. Did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_16.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "I did, sir."
            m "Tell me how it went."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Well... Ehm..."
            her "There is this one girl who is into girls..."
            her "I thought she would be the ideal candidate for my task..."
            her "so I told her that I am curious and that I would like to kiss her..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "She said that we should go to the girls' restroom for that..."
            her "But I just kissed her right there in the corridor..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "And she kissed me back but..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "It got weird really fast..."
            her "The way she kissed me..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "She did it like a boy would, sir..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Aggressive but confident..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "Naturally a small group of spectators gathered up around us right away..."
            $herView.hideshowQQ( "body_183.png", pos )
            her "Mostly boys of course..."
            $herView.hideshowQQ( "body_182.png", pos )
            her "Some of them even cheered us on..."
            $herView.hideshowQQ( "body_129.png", pos )
            her "....."
            her "By the way, the girl I kissed, sir..."
            m "Hm...?"
            $herView.hideshowQQ( "body_127.png", pos )
            her "She is one of those unpopular kids..."
            her "I know that other students make fun of her sometimes..."
            $herView.hideshowQQ( "body_129.png", pos )
            her "But today changed everything..."
            her "I Single-handedly turned that girl from a social outcast..."
            $herView.hideshowQQ( "body_111.png", pos )
            her "Into \"that lesbian girl who made out with Hermione Granger\"!"
            m "Wow... You are just like some kind of hero or something..."
            $herView.hideshowQQ( "body_128.png", pos )
            her "I suppose I am, sir..."
            her "I changed that poor girl's life..."
            m "Now you are just pulling on my heartstrings..."

            
            
        elif one_out_of_three == 3: ### EVENT (C)
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_16.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "Professor Dumbledore?"
            m "Yes, miss Granger?"
            $herView.hideshowQQ( "body_31.png", pos )
            her "May I ask you a question, sir?"
            m "By all means."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Ehm..."
            $herView.hideshowQQ( "body_66.png", pos )
            her "Why are boys so into watching girls make out with each other, sir?"
            menu:
                m "..."
                "\"Who knows? Boys are weird.\"":
                    $herView.hideshowQQ( "body_118.png", pos )
                    her "Yes, they are, aren't they...?"
                    m "Yes, yes..."
                    m "And that is why young girls such as yourself...."
                    m "Are often interested in a much older gentleman..."
                    $herView.hideshowQQ( "body_117.png", pos )
                    her "??!"
                    $herView.hideshowQQ( "body_79.png", pos )
                    her "That is not what I meant, sir..."
                "\"You wouldn't understand, girl.\"":
                    $herView.hideshowQQ( "body_120.png", pos )
                    her "Hm..."
                    $herView.hideshowQQ( "body_117.png", pos )
                    her "What about you, sir?"
                    her "Where you like that when you were a boy?"
                    m "You mean if I enjoyed watching two girls going at it?"
                    m "Well of course."
                    m "I still do..."
                    $herView.hideshowQQ( "body_120.png", pos )
                    her "Oh..."
                "\"Kissing girls? Where?!!\"":
                    $herView.hideshowQQ( "body_76.png", pos )
                    her "Tsk!......................" # :(
            
            
            $herView.hideshowQQ( "body_87.png", pos )
            her "Well, I am only asking you this, sir, because..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "...it is sort of becoming a new trend in our school..."
            her "Some girls are willing to do this simply to catch the attention of the boy they fancy..."
            m "Are you one of those girls, Miss Granger?"
            $herView.hideshowQQ( "body_118.png", pos )
            her "I suppose..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "I mean, only because of the favours you buy from me, sir..."
            m "Good... Tell me more."
            $herView.hideshowQQ( "body_80.png", pos )
            her "Well, as you know, I am quite popular..."
            $herView.hideshowQQ( "body_74.png", pos )
            her "So all I had to do is just mention that I would not mind doing it today..."
            her "And I had half a dozen girls lined up instantly..."
            $herView.hideshowQQ( "body_45.png", pos )
            her "I chose a girl from \"Gryffindor\" of course..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "And we put on a little show right in the middle of the classroom..."
            m "Good... Tongue and everything?"
            $herView.hideshowQQ( "body_29.png", pos )
            her "Tongue and everything, sir."
            m "Nicely done."
            $herView.hideshowQQ( "body_45.png", pos )

    elif whoring >= 18: # LEVEL 07+                  
        if one_out_of_three == 1: ### EVENT (A) # Snowballing
            label snowballing:
                pass
            m "Miss Granger..."
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_16.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "Good evening, sir."
            m "Did you complete your task, girl?"
            $herView.hideshowQQ( "body_15.png", pos )
            her "I did, sir."
            m "I'm all ears..."
            $herView.hideshowQQ( "body_17.png", pos )
            her "Well, I kissed that annoying blond girl from \"Slytherin\"..."
            m "Hm... \"annoying\", huh?"
            m "Because she happens to be from \"Slytherin\"."
            $herView.hideshowQQ( "body_16.png", pos )
            her "Precisely so, sir."
            m "Hm..."
            m "Don't you think that that's a little bit of prejudice on your part?"
            m "Or shall I say that you are being a \"housist\"?"
            $herView.hideshowQQ( "body_185.png", pos )
            her "...a \"housist\", sir?"
            m "Well, you know... It's like \"sexist\" or \"ageist\"..."
            m "You just put an \"ist\" after something and it automatically becomes a bad thing..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "\"housist\" is not an actual word, sir..."
            m "It's not? Well, give it time..."
            $herView.hideshowQQ( "body_185.png", pos )
            her ".............?"
            m "\"Housophobic\"...?"
            m "No, wait, I got it!"
            m "\"Housophobe\"!"
            $herView.hideshowQQ( "body_07.png", pos )
            her "Stop it, sir. I am not any of those weird words..."
            her "\"Slytherins\" are evil and annoying. Nobody likes them, and that is a fact!"
            m "Fine, whatever. Back to the \"girl-kissing\" then."
            $herView.hideshowQQ( "body_29.png", pos )
            her "..............."
            her "Like I was saying..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "I kissed that girl from \"Slytherin\"..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Normally I would never do it, of course..."
            her "Not with someone from that wretched house anyways..."
            $herView.hideshowQQ( "body_79.png", pos )
            her "But she approached me first and practically begged me to do it with her..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "And today of all days..."
            her "to be honest..."
            $herView.hideshowQQ( "body_79.png", pos )
            her "She was quite attractive..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "For someone from \"slytherin\" that is..."
            $herView.hideshowQQ( "body_127.png", pos )
            her "I did not ask her why she needed this so desperately..."
            her "She was probably just trying to boost her own popularity at my expense..."
            her "Or it could also be that someone from the school staff bought this favour from her..."
            $herView.hideshowQQ( "body_186.png", pos )
            her "The same way you buy favours from me, sir..."
            m "(Snape?)"
            $herView.hideshowQQ( "body_47.png", pos )
            her "If that is the case I am sure that it was professor Snape..."
            m "What? He would never..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "You should really investigate Professor Snape's activities, sir..."
            m "Of course..."
            m "Putting him on my \"naughty boys list\" as we speak..."
            $herView.hideshowQQ( "body_66.png", pos )
            her ".........."
            m "What happened next, girl?"
            $herView.hideshowQQ( "body_87.png", pos )
            her "Oh, right..."
            her "Well, we made out for a while..."
            her "She was very... passionate."
            $herView.hideshowQQ( "body_122.png", pos )
            her "So I imagine it was quite a spectacle..."
            her "The boys were cheering and whistling..."
            $herView.hideshowQQ( "body_124.png", pos )
            her "So we decided to \"snowball\" a little..."
            m "I'm sorry, you decided to do what?"
            $herView.hideshowQQ( "body_122.png", pos )
            her "To \"snowball\", sir."
            $herView.hideshowQQ( "body_128.png", pos )
            her "It is when one girl spits into another girl's mouth..."
            her "We call it \"snowballing\"..."
            her "The boys really go crazy from that for some reason..."
            m "I imagine they do..."
            $herView.hideshowQQ( "body_127.png", pos )
            her "So she spat into my mouth..."
            her "And then I spat into hers..."
            $herView.hideshowQQ( "body_187.png", pos )
            her "Although I would much rather spit in her face!"
            $herView.hideshowQQ( "body_69.png", pos )
            her "Then she returned my spit..."
            $herView.hideshowQQ( "body_187.png", pos )
            her "And I had to fight the urge to slap her smug face for doing that..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "But I don't think the boys would appreciate that..."
            m "Well... You would be surprised..."
            $herView.hideshowQQ( "body_124.png", pos )
            her "In any case, After that we kissed some more..."
            her "And then the break was over..."
            $herView.hideshowQQ( "body_122.png", pos )
            her "And we had to run to class..."
            m "*Sigh...* Nonchalant and innocent schooldays..."
            m "Home assignments... Classes..."
            m "Schoolgirls \"snowballing\" in the courtyard..."
            m "Well done, miss Granger."
            $herView.hideshowQQ( "body_68.png", pos )
            

        elif one_out_of_three == 2: ### EVENT (B)
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_16.png", pos )
            her "I did, sir."
            $herView.hideshowQQ( "body_68.png", pos )
            her "Only... ehm..."
            m "What is it?"
            $herView.hideshowQQ( "body_45.png", pos )
            her "Well... I have this friend..."
            her "Her name is Ginny Weasley..."
            $herView.hideshowQQ( "body_188.png", pos )
            her "And... uhm..."
            her "I'm Not sure how to say this..."
            m "Just say it, girl."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Well, we decided to skip the potions class together..."
            her "And study for the upcoming Herbology test instead..."
            her "So me and Ginny, we were studying..."
            her "And we got to talking about boys..."
            m "Naturally..."
            $herView.hideshowQQ( "body_189.png", pos )
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "And then I sort of kissed her..."
            $herView.hideshowQQ( "body_128.png", pos )
            her "And Ginny returned my kiss with such passion..."
            her "that we sort of ended up doing more than just kissing..."
            g9 "And afterwards you had a pillow fight in lingerie?"
            $herView.hideshowQQ( "body_190.png", pos )
            her "Err... No..."
            m "What did you do then?"
            $herView.hideshowQQ( "body_188.png", pos )
            her "I am not telling you, sir." # :)
            her "You sent me out to kiss a girl..."
            her "And I did just that."
            $herView.hideshowQQ( "body_122.png", pos )
            her "The rest shall remain private."
            m "Now you are just being cruel, you little witch."
            $herView.hideshowQQ( "body_64.png", pos )
            her "My points please." # :)
            m "Fine..."

            
        elif one_out_of_three == 3: ### EVENT (C) Only takes place once
            if lazy_aka_not_yet:
                pass
            else:
                jump snowballing
                
            $ lazy_aka_not_yet = False #Makes sure this event only takes place once.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_45.png", pos )
            her "Yes I did, sir."
            m "Splendid. Tell me more."
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_64.png", pos )
            her "Of course."
            her "I decided to go for a different approach today..."                                                                                                                                                                                                           
            $ pos.xpos = 500

            # use CharacterExItemPoseParade to hide all items
            #$ herView.data().addPose( CharacterExItemPoseParade( herView.mPoseFolder, "hermione_bugged_branch.png", G_Z_FACE + 5 ) )
            $ herView.data().addItem( 'item_pose_bug' )
            $herView.showQ( "body_63.png", pos )
            stop music
            her "I figured that iffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
            m "Huh?"
            $herView.hideQ()
            $herView.data().delPose()
            her "If I coulddddddddddddddddddd"
            pause
            pause
            pause
            
            with hpunch
            g4 "{size=+5}Goddammit!!!{/size}"
            g4 "{size=+5}AKABUR?!!!{/size}"
            a4 "Huh...? WHAT?!! What do you want from me?"
            a4 "There is no release date set! Stop asking me!"
            g4 "What are you talking about?"
            a5 "I mean, I'm not sleeping..." 
            a7 "*Yawn*..."
            a5 "................"
            m "So Is Hermione going to stutter from now on? Is that what this is?"
            pause
            pause
            g4 "Are you still there?"
            a1 "I'm not sleeping..."
            a5 "Just resting my eyes..."
            g4 "Dammit, man."
            g4 "Just go catch up on some sleep before you ruin the whole thing."
            m "Get some shuteye and then finish this event properly."
            a1 "I can't..."
            a1 "I want this game to be released as soon as possible..."
            a1 "No, scratch that. I want it to be released sooner than possible..."
            a1 "People trust me... and..."
            a7 "*yawn*..."
            a1 "And...."
            pause
            pause
            
            m "Akabur?"
            m "Dude?"
            
            pause
            pause
            
            m "*Sigh*...well, we could let this one event slide I suppose."
            m "Just this once though..."
            m "And Hermione's \"perversion\" level did increase..."
            m "So there is no need for save-scumming..."
            
            aa "Zzzz....zzz....."
            aa "Zzz.... Lola? no... Put your tits away I said... Zzzz....."
            aa "Zzz.... And don't call me that.... Zzz...."
            
            m "*Sigh...* That's just sad..."
            

            
    $ gryffindor +=45
    m "The \"Gryffindor\" house gets 45 points!"
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


 
 
 
 
    
    $ request_20_points += 1 
    $ request_20 = False 
    $ hermione_sleeping = True

    call music_block
    
    return
    
    
