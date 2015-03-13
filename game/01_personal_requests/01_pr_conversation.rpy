################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label new_request_01: #LV.1 (Whoring = 0 - 2)
    $herView.hideQQ()
    m "{size=-4}(All I'll do is have an innocent conversation with her...){/size}"
    menu:
        "\"(Yes, let's do that.)\"":
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    m "Alright then..."
    m "Just tell me some news about you."
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_08.png", pos )

    $ current_payout = 5 #Used when haggling about price of th favor.

    
    if IsFirstRun(): #First time this event taking place.
#    if request_01 == 0: #First time this event taking place.
        her "Ehm... Alright..."
        her "I just stand here and talk then...? Like this?"
    else:
        her "Here in the middle, right? I remember..."
    $herView.hideQQ()
    $ menu_x = 0.5 #Menu is moved to the left side.
    
    show screen blktone 
    with d3
    show screen ctc
    $herView.showQ( "body_01.png", pos )
    with Dissolve(.3)
    pause
    
    $pos = POS_140
    m "Well?"
    if IsFirstRun() and whoring <=5: #First time this event taking place.
#    if request_01 == 0 and whoring <=5: #First time this event taking place.
#        $  new_request_01_01 = True #Hearts on menu buttons.
        $SetHearts(1)
        $herView.hideshowQQ( "body_11.png", pos )
        her "Em... very well..."
        ">Hermione is feeling confused..."
        $herView.hideshowQQ( "body_12.png", pos )
        her "..................."
    if whoring >= 0 and  whoring <= 5: #LEVEL 01 and LEVEL 02
        if whoring >= 3 and whoring <= 5:
#            $ level = "02"
#            $ new_request_01_02 = True #Hearts on menu buttons.
            $SetHearts(2)
        $herView.hideshowQQ( "body_12.png", pos )
        her "My life has been quite uneventful lately to be honest..."
        her "Apart from that day when I failed that test..."
        her "Still can't believe it happened..."
        menu: 
            "-Jerk off while she is talking-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                $herView.hideQ()
                hide screen blktone
                with d3
                ">You reach under the desk and crab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                $herView.hideQQ()
                $ pos = POS_370
                $herView.showQQ( "body_14.png", pos )
                her "Professor, what are you doing?"
                m "What, oh it's nothing. Just scratching my leg."
                m "You were saying?"
                $herView.hideshowQQ( "body_14.png", pos )
                her "Yes... Well, that test I failed..."
            "-Participate in the conversation-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Yes, what a tragedy that was..."
                her "Exactly! I'm glad you understand, professor."
                pass
        her "Come to think of it, I don't feel like talking about it anymore..."
        m "Alright, what else has happened lately?"
        her "Em... Well, I'm doing pretty well at herbology lately..."
        her "I mean, I always score the top marks, but I have been studying really hard anyway..."
        her "And now I sort of feel like sometimes I know more than professor Sprout herself..."
        if d_flag_01:
            m "{size=-4}(Yes... ah...){/size}"
        else:
            m "(Professor Sprout... He-he, what a ridiculous name...)"
            #m "(...)"
        
        $herView.hideshowQQ( "body_07.png", pos )
        her "Did you say something professor?"
        m "It's nothing, keep going..."
        $herView.hideshowQQ( "body_14.png", pos )
        her "Well, some students are making fun of professor Quirell behind his back..."
        her "But I disapprove of such behavior of course."
        if d_flag_01:
            m "{size=-4}(Come on! Say something naughty!){/size}"
        else:
            m ".................."
        her "Oh, and my \"Men's Rights Movement\" group is gaining popularity..."
        her "I'm very happy about that..."
        $herView.hideshowQQ( "body_16.png", pos )
        her "I think, given time, we will be able to make a real difference..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Yes, it is so invigorating to know that you are doing the right thing!"
        her "Would't you agree professor?"
        if d_flag_01:
            m "{size=-4}(Dammit. Now she killed the mood completely...){/size}"
            show screen genie
            with d3
            $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
            pass
        else:
            m "Zzzz........"
            m "huh?"
            
        $herView.hideshowQQ( "body_05.png", pos )
        her "Professor?"
        m "Yes, yes, I'm totally listening..."
        m "This is all very self righteous, er..."
        m "I mean, very invigorating and stuff..."
        $herView.hideshowQQ( "body_07.png", pos )
        her ".........................."
  
    elif whoring >= 6 and whoring<=11: #LEVEL 03
#        $  new_request_01_03 = True #Hearts on menu buttons.
        $ SetHearts(3)
        $herView.hideshowQQ( "body_12.png", pos )
        her "My life has been quite uneventful lately to be honest..."
        her "Hm..."
        her "There is a fierce competition going on between the \"Slytherin\" and the \"Gryffindor\" house."
        her "To be honest, professor, there should be none..."
        her "\"Gryffindor\" would have been in the lead if not for those \"Slytherin\" harlots..."
        her "The things I hear those girls do simply to get a few extra points..."
        $herView.hideshowQQ( "body_04.png", pos )
        her "How despicable!"
        m "What does this make you then, miss Granger?"
        $herView.hideshowQQ( "body_03.png", pos )
        her "Exactly!"
        m "Huh?"
        $herView.hideshowQQ( "body_04.png", pos )
        her "I have to work even harder to compensate for the damage those nasty girls are doing..."
        $herView.hideshowQQ( "body_03.png", pos )
        her "Thank you for helping me out, professor."
        menu: 
            "-Start jerking off-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                $herView.hideQ()
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                $herView.hideQQ()
                $ pos = POS_370
                $herView.showQQ( "body_14.png", pos )
                her "Professor, what are you doing?"
                her "You are not.....?"
                $herView.hideshowQQ( "body_29.png", pos )
                her "Are you...?"
                m "What, it's nothing. Keep going."
                $herView.hideshowQQ( "body_07.png", pos )
                her "Hm..."
                m "{size=-4}(Is she onto me? Nah...){/size}"
            "-Participate in the conversation-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Don't mention it."
                pass
        $herView.hideshowQQ( "body_16.png", pos )
        her "Well, like I was saying..."
        her "I heard that this one girl sold one of the professors some naughty pictures of herself for ten house points..."
        if d_flag_01:
            m "{size=-4}(What a slut... ah... Yes...){/size}"
        else:
            m "Ten points, huh?"
        her "Yes..."
        if d_flag_01:
            $herView.hideshowQQ( "body_29.png", pos )
            her "And these two other girls..."
            her "There is a rumor that they are actually sleeping with professor snape..."
            m "{size=-4}(Yes... Those little, nasty, \"slytherin\" sluts!){/size}"
            $herView.hideshowQQ( "body_45.png", pos )
            her "Also there was this one girl, who gave a teacher a handjob, right during class..."
            m "{size=-4}(Yes... This is good stuff, go on!){/size}"
            $herView.hideshowQQ( "body_29.png", pos )
            her "And this other girl, she sucked off a teacher!"
            m "{size=-4}(Yes! Yes!){/size}"
            $herView.hideshowQQ( "body_46.png", pos )
            her "And another girl let a teacher cum in her mouth..."
            her "And she swallowed it all and loved it!"
            m "{size=-4}(Wait... Is she making this up?){/size}"
            $herView.hideshowQQ( "body_64.png", pos )
            her "I'm a very dirty girl..."
            g4 "what?!"
            $herView.hideshowQQ( "body_65.png", pos )
            her "I just want to suck a cock..."
            her "I want men to cum on my face like in those videos I saw!"
            g4 "{size=-4}(You little slut! That did it!) *Argh!*{/size}"
            $herView.hideQQ()
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            g4 "Argh! YES!"
            $herView.hideQQ()
            hide screen bld1
            with d3
            show screen genie_jerking_sperm
            with d3
            #pause 3
            pause
            
            $ mad = +7
            
            show screen bld1
            with d3
            $herView.showQQ( "body_47.png", pos )
            her "I knew it! You were touching yourself, professor!"
            show screen genie_jerking_sperm_02
            with d3
            g4 "What? No, I was just... ah, shit, this feels good..."
            show screen genie
            #show screen genie_jerking_off
            with d3
            $herView.hideshowQQ( "body_32.png", pos )
            her "This is disgusting! How could you!?"
            her "Sir, you are the headmaster! You are supposed to set a good example!"
            m "Hey, little missy, are you going to judge me or do you want your points?"
            $herView.hideshowQQ( "body_34.png", pos )
            her "My points please, I believe I earned those."
            m "Yes you did."
            $herView.hideshowQQ( "body_47.png", pos )
            her "Ew... I feel so dirty now..."
            hide screen genie_jerking_sperm_02
            with d3
        else:
            her "We need to put an end to this behavior, professor!"
            m "Yeah, sure..."
            her "So you agree with me then?"
            her "I think we need to implement a new penalty system to punish girls who are known to sell favours..."
            m "(All I heard was \"punish girls\"...)"
            her "This will also help the boys in our school to feel less discriminated against!"
            m "The boys?"
            m "Oh, right... Nobody wants to buy sexual favours from them... Poor bastards."
            $herView.hideQQ()
            $herView.showQ( "body_03.png", pos, d3 )
            her "I'm so glad that you understand my concerns, Sir."
            m "Yes, yes, sure..."

    elif whoring >= 13: #Хотя бы один раз дрочила
        her "Sir, you really called me here because these poor 5 points?"
        her "I am sorry to spend time talking, which is almost nothing will bring."
        $herView.hideshowQQ( "body_10.png", pos )
        her "Maybe we will work with you something....mmm... interesting?"
        her "In the sense of giving more points?"
        menu: 
            "\"And what you want to do?\"":
                m "And what you want to do, miss Granger?"
                $herView.hideshowQQ( "body_68.png", pos )
                her "I do not know, sir. There are different options!"
                jump new_personal_request
            "\"Since when did you become to choose their assignments, Miss Granger?":
                $ SetHearts(4)
                m "Since when did you become to choose their assignments, Miss Granger?\""
                m "This seems to be here, I decide which service is paid."
                m "So, today paid your story."
                $herView.hideshowQQ( "body_202.png", pos )
                her "Excuse me, sir! Of Course."
                m "And?"
                $herView.hideshowQQ( "body_93.png", pos )
                her "Well, I have everything, as always. I study a lot, sit up late in the library, exams coming up..."
                her "Then meeting \"MRM\"... "
                her "By the way, we decided to extend our work further!" 
                her "We will not only defend the rights of men."
                m "Really?"
                her" We will consistently speak out against injustice and unrighteousness"
                if not this.flag_SCUKO_presented:
                    $this.flag_SCUKO_presented=True
                    her "We want now to call our society A.n.a.a.l."
                    g4 "What?! \"ANAL\"?!"
                    $herView.hideshowQQ( "body_05.png", pos )
                    her "Not \"anal\", sir!  A.n.a.a.l!"
                    her "\"Alliance necessary African ants low-spirited!\""
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "However, with a name yet to be decided..." #Цель
                    g9 "Oh, it's just a wonderful name!"
                    $herView.hideshowQQ( "body_208.png", pos )
                    her "You think?"
                    g9 "Don't doubt, girl."
                else:
                    g9 "Yes, I remembered you renamed in the alliance ana..."
                    $herView.hideshowQQ( "body_30.png", pos )
                    her "Not in the society ana-, sir! But in A.n.a.a.l!"
                    her "Alliance necessary African ants low-spirited!"
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "However, with a name yet to be decided..."
                    her "............................."
                $herView.hideshowQQ( "body_16.png", pos )
                her "Well, that's probably all."
                m "Thats all?"
                if not end.IsEnding(const_ENDING_STRONG_GIRL):
                    her "Yes, sir. Please pay me and I'll go - I have things to do."
                    m "Hmm... today you are not in the mood, miss Granger."
                    $herView.hideshowQQ( "body_14.png", pos )
                    her "Well, Professor, you had asked, I told. If you asked other service..."
                    m "Okay, okay..."
                else:
                    $herView.hideshowQQ( "body_14.png", pos )
                    her "Well, five points, I'm sure enough."
                    m "You again, young lady?"
                    $herView.hideshowQQ( "body_102.png", pos )
                    her "Sir, log in my position. I am ready to tell you something about the depraved girls..."
                    $herView.hideshowQQ( "body_189.png", pos )
                    her "And you touched..." 
                    $herView.hideshowQQ( "body_101.png", pos )
                    her "And can even talk to until you rapidly not cum."
                    m "But?..."
                    $herView.hideshowQQ( "body_58.png", pos )
                    her "But all of this should be paid fairly!"
                    m "As you become selfish, miss Granger."
                    her "Not at all, sir. I just know a price. And an additional 15 points for the story of depraved girls - quite fair fee."
                    menu: 
                        "\"No!\"":
                            m "You're free to go, miss Granger!"
                            her "As you say, sir. In this case, I would like to receive your payment."
                        "\"Well, another 15 points. Tell me!":
                            $current_payout+=15
                            m "Okay, I'll pay you. Tell me!"
                            $herView.hideshowQQ( "body_102.png", pos )
                            her "Yes, sir. And you can start fucking around."
                            m "Damn, you got him off, girl! I will decide when and what do I do."
                            $herView.hideshowQQ( "body_13.png", pos )
                            her "Sorry, Professor."
                            her "Well, I heard two girls talking in the bedroom, as they put in their mouths guys."
                            $herView.hideshowQQ( "body_50.png", pos )
                            her "Of course, they are not from Gryffindor, sir!"
                            m "Of course. Gryffindor girls take nothing in his mouth."
                            $herView.hideshowQQ( "body_120.png", pos )
                            her "All it is, sir. We are too proud for that and ..."
                            m "Miss Granger!"
                            $herView.hideshowQQ( "body_55.png", pos )
                            her "Sir?"
                            m "This is how you earn 15 points?"
                            her "Excuse me, sir! .. Well, one of them, blonde, told me that her boyfriend cums so much that she even pours from the nose."
                            $herView.hideshowQQ( "body_55.png", pos )
                            her "Well, if the truth, sir, it just boasted before the brunette."
                            her "There are not so many sperm, she just specially stiffened to sperm hit in the nose."
                            m "How do you know, Miss Granger?"
                            m "You also took part in this?"
                            $herView.hideshowQQ( "body_103.png", pos )
                            her "No, sir, I do not do this! I just know ... I have my sources."
                            m "Sources of sperm? Hehe."
                            $herView.hideshowQQ( "body_30.png", pos )
                            her "Argh! If you have something to say so, sir, I'll just leave."
                            m "Miss Granger! You promised to tell me something, but so far I have not heard anything."
                            m "A little more, I finally give up on you, and you do not get points."
                            $herView.hideshowQQ( "body_28.png", pos )
                            her "Just do not knock me down, sir. Okay?"
                            $herView.hideshowQQ( "body_56.png", pos )
                            her "Well ... One girl confessed to me that she likes to go without underwear."
                            her "When she walks down the stairs and guys look below her skirt, she feels ... she is excited, sir."
                            m "{size=-4}(Oh, that's better...){/size}"

                            $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                            $herView.hideQ()
                            hide screen blktone
                            with d3
                            ">You put your hands under the table and grasped cock..."
                            hide screen blktone8
                            with d3
                            hide screen genie
                            show screen genie_jerking_off
                            with d3
                            pause
                            $herView.hideQQ()
                            $ pos = POS_370

                            $herView.hideshowQQ( "body_122.png", pos )
                            her "There is another girl..."
                            her "When she was in Hogsmeade, she did something with dwarf..."
                            m "{size=-4}(What a slut ... ah ... yes ...){/size}"
                            her "And two other girls..."
                            $herView.hideshowQQ( "body_187.png", pos )
                            her "They masturbated each other at recess. And the guys looked at it. It's just disgusting, Professor!"
                            m "{size=-4}(Oh, yeah-e-ah ... I'm sure it was a sight!){/size}"
                            $herView.hideshowQQ( "body_118.png", pos )
                            her "And then that little girl. They say she goes, put a carrot in his a... well, you understand me."
                            her "It's like, she develops ... so that it was easier to go..."
                            m "{size=-4}(Yeah ... that's because ... slut slut diligent ... more!){/size}"
                            $herView.hideshowQQ( "body_68.png", pos )
                            her "And another girl, she jerk off once the two of..."
                            m "{size=-4}(Yes! Yes!){/size}"
                            $herView.hideshowQQ( "body_56.png", pos )
                            her "And then knelt down and took in his mouth from a third..."
                            m "{size=-4}(Oh, whores, I now gonna...){/size}"
                            $herView.hideshowQQ( "body_122.png", pos )
                            her "That's all, Professor."
                            g4 "What?!"
                            $herView.hideshowQQ( "body_111.png", pos )
                            her "You pay me 15 points for the story. But the end is worth the same amount."
                            g4 "Small stuff!"
                            menu: 
                                "\"Get nothing!\"":
                                    with d3
                                    hide screen genie_jerking_off
                                    show screen genie
                                    with d3
                                    m "Get nothing!"
                                    m "No points!"
                                    $herView.hideshowQQ( "body_05.png", pos )
                                    her "Very well, Professor! In this case, do not expect that I will continue to meet your every whim!"
                                    $mad = +30
                                    jump request_01_done
                                "\"Fair Enough. That's all...\"":
                                    m "Argh! Well, all ... Enough."
                                    with d3
                                    hide screen genie_jerking_off
                                    show screen genie
                                    with d3
                                    $herView.hideshowQQ( "body_04.png", pos )
                                    her "As you say, sir. I'm ready to get their [current_payout] points."
                                "\"Go on, will you points!\"":
                                    $current_payout+=15
                                    m "Do not stop, I'll give you points! Go Ahead!"
                                    $herView.hideshowQQ( "body_127.png", pos )
                                    her "Yes, sir. These whores, sir, every day they suck a couple of guys and ask them to put an end to the face."
                                    her "And go with the face smeared with sperm. They say that it is good for the skin."
                                    m "{size=-4}(Да, давай,... продолжай!){/size}"
                                    her "And Slytherin girl promised the guys from the Quidditch team that will wake them blowjob week if they win."
                                    her "And yet, sir, told one girl wanker one teacher..." 
                                    her "And then immediately went to another wank..."
                                    m "{size=-4}(Oh, yeah-ah ... these whores!){/size}"
                                    $herView.hideshowQQ( "body_78.png", pos )
                                    her "And then, I heard there was a new game. it is called \"Guess hole\"."
                                    m "{size=-4}(Guess ... Ahh ... yes ....){/size}"
                                    $herView.hideshowQQ( "body_58.png", pos )
                                    her "In wooden partitions make a hole below the belt, where several girls expose their..."
                                    her "Charms, sir. And if the guy guessed who it is..."
                                    m "{size=-4}(Oh, yeah ... yeah ... I have ... already!){/size}{size=+2} * Argh! *{/size}"
                                    $herView.hideQQ()
                                    show screen white 
                                    pause.1
                                    hide screen white
                                    pause.2
                                    show screen white 
                                    pause .1
                                    hide screen white
                                    with hpunch
                                    g4 "Argh! YES!"
                                    $herView.hideQQ()
                                    hide screen bld1
                                    with d3
                                    show screen genie_jerking_sperm
                                    with d3
                                    #pause 3
                                    pause
                                    
                                    $MusicStart("Supergirl")                                   
                                    show screen bld1
                                    with d3
                                    $herView.showQQ( "body_64.png", pos )
                                    her "Oh, you are so powerfully ejaculate, Professor! Did you like it?"
                                    show screen genie_jerking_sperm_02
                                    with d3
                                    g4 "Oh, shit, it's so... It's incredibly fucking amazing!..."
                                    show screen genie
                                    #show screen genie_jerking_off
                                    with d3
                                    $herView.hideshowQQ( "body_111.png", pos )
                                    her "I'm glad the Professor that you commit. And yet, can I get your points? Just [current_payout] points."
                                    m "Oh-x... Ufff... Yes, you can but..."
                                    m "... what's up with the game \"Guess hole\"? You still have not told before."
                                    $herView.hideshowQQ( "body_46.png", pos )
                                    her "You and so finished, sir. But if you want to learn..."
                                    m "What ?! You again extortion points?"
                                    her "A total of 15 points, sir."
                                    m "You run up, girl!"
                                    $herView.hideshowQQ( "body_58.png", pos )
                                    her "Excuse me, sir, then I'll just get my [current_payout] points and go."
                                    menu: 
                                        "\"Go away!\"":
                                            m "Go away. And remember me blackmail will not work!"
                                            $herView.hideshowQQ( "body_58.png", pos )
                                            her "Yes,sir..."
                                        "\"Fair Enough. 15 points, tell me. But this is the last time!\"":
                                            $current_payout+=15
                                            m "Okay, but remember, this is the last time!"
                                            $herView.hideshowQQ( "body_64.png", pos )
                                            her "Of course, I understand."
                                            $herView.hideshowQQ( "body_56.png", pos )
                                            her "In general, if a guy whose guess is..."
                                            her "Um ... well, guess whose it is, then she should give him the way he wants."
                                            her "And if you did not guess, it is becoming common for the whole night."
                                            m "Commin?"
                                            her "Yes, sir. The girls take him to his bedroom and he has to do everything for them."
                                            m "?!..."
                                            $herView.hideshowQQ( "body_122.png", pos )
                                            her "{size=+4}Absolutely{/size} everything that each of them will say, sir!"
                                            m "Oh shit!"
                                            her "Professor, I think you once again rises. If you want to continue, then only 15 Pts ..."
                                            m "No !!! Enough for today!"
                                            $herView.hideshowQQ( "body_58.png", pos )
                                            her "Of course, the professor."
                                    her "...................."
                                    hide screen genie_jerking_sperm_02
                                    with d3
                                    $MusicStop()




    stop music fadeout 2.0
    
#    $ gryffindor +=5
    $ gryffindor += current_payout
    
    $herView.hideQQ()
    $herView.showQ( None, pos, d3 )
    m "[current_payout] points to \"Gryffindor\" miss Granger. Well done." 
    
    #$herView.showQ( "body_07.png", pos, d3 )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Will this be all then?"
    if whoring >= 0 and whoring <= 2: #LEVEL 01
        her "*sigh of relief*"
    m "Yes, you can go now."
    if IsFirstRun():
#    if request_01 == 0:
        $herView.hideshowQQ( "body_01.png", pos )
        her "Another [current_payout] points... The Guys will be so happy."
        her "Thank you, professor."

    label request_01_done:
    if whoring <= 2:
            $ whoring +=1
 
#    $ request_01 += 1
    
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

    if current_payout>=35:
        m "................................."
        m "\"Guess the hole\", wow..." 
        m "What did not come up with these sluts!"
        $posHead=gMakePos( 390, 235 )
    
    
    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
