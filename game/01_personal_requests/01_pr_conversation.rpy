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
    if IsFirstRun() and hermi.whoring <=5: #First time this event taking place.
#    if request_01 == 0 and hermi.whoring <=5: #First time this event taking place.
#        $  new_request_01_01 = True #Hearts on menu buttons.
        $SetHearts(1)
        $herView.hideshowQQ( "body_11.png", pos )
        her "Em... very well..."
        ">Hermione is feeling confused..."
        $herView.hideshowQQ( "body_12.png", pos )
        her "..................."
    if hermi.whoring >= 0 and  hermi.whoring <= 5: #LEVEL 01 and LEVEL 02
        if hermi.whoring >= 3 and hermi.whoring <= 5:
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
  
    elif hermi.whoring >= 6 and hermi.whoring<=11: #LEVEL 03
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
            
            $ hermi.liking -= 7
            
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

    elif hermi.whoring >= 12: 
        her "Sir, you really called me here because of these measly 5 points?"
        her "I am sorry to spend time talking, when it will give me almost nothing."
        $herView.hideshowQQ( "body_10.png", pos )
        her "Maybe we could do something more....mmm... interesting?"
        her "Something that gives more points?"
        menu: 
            "\"And what do you want to do?\"":
                m "And what do you want to do, miss Granger?"
                $herView.hideshowQQ( "body_68.png", pos )
                her "I do not know, sir. There are different options!"
                jump new_personal_request
            "\"Since when do you choose your own assignments, Miss Granger?":
                $ SetHearts(4)
                m "Since when do you choose your own assignments, Miss Granger?\""
                m "Here I decide which service I pay you for."
                m "So today I pay for your story."
                $herView.hideshowQQ( "body_202.png", pos )
                her "Excuse me, sir! Of Course."
                m "And?"
                $herView.hideshowQQ( "body_93.png", pos )
                her "Well, as always. I study a lot, stay up late in the library, exams are coming up..."
                her "Then a \"MRM\" meeting... "
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
                    her "\"Alliance necessary African ants low-spirited!\"" #Is this supposed to be this weird
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "However, the name is not yet final..." #Цель
                    g9 "Oh, it's just a wonderful name!"
                    $herView.hideshowQQ( "body_208.png", pos )
                    her "You think so?"
                    g9 "No doubt, girl."
                else:
                    g9 "Yes, I remembered you renamed the society ana..."
                    $herView.hideshowQQ( "body_30.png", pos )
                    her "Not the ana-society, sir! But A.n.a.a.l!"
                    her "Alliance necessary African ants low-spirited!"
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "However, the name is not yet final..."
                    her "............................."
                $herView.hideshowQQ( "body_16.png", pos )
                her "Well, that's probably all."
                m "Thats all?"
                if not end.IsEnding(const_ENDING_STRONG_GIRL):
                    her "Yes, sir. Please pay me and I'll go - I have things to do."
                    m "Hmm... your not in the mood today, miss Granger?"
                    $herView.hideshowQQ( "body_14.png", pos )
                    her "Well, Professor, you asked, I answered. If you had asked for another service..."
                    m "Okay, okay..."
                else:
                    $herView.hideshowQQ( "body_14.png", pos )
                    her "OK, five points, that should do."
                    m "Come again, young lady?"
                    $herView.hideshowQQ( "body_102.png", pos )
                    her "Sir, see things from my perspective. I am ready to tell you something about the depraved girls..."
                    $herView.hideshowQQ( "body_189.png", pos )
                    her "And you could touch youself..." 
                    $herView.hideshowQQ( "body_101.png", pos )
                    her "And I could even talk until you cum slowly."
                    m "But?..."
                    $herView.hideshowQQ( "body_58.png", pos )
                    her "But all of this should be paid fairly!"
                    m "Have you become selfish, miss Granger?"
                    her "Not at all, sir. I just know the price. An additional 15 points for the story of depraved girls - quite a fair fee."
                    menu: 
                        "\"No!\"":
                            m "You're free to go, miss Granger!"
                            her "As you say, sir. In this case, I would like to receive my payment."
                        "\"Alright, another 15 points. Tell me!":
                            $current_payout+=15
                            m "Okay, I'll pay you. Tell me!"
                            $herView.hideshowQQ( "body_102.png", pos )
                            her "Yes, sir. And you can start touching yourself."
                            m "Damn, how dare you, girl! I will decide when and what I do."
                            $herView.hideshowQQ( "body_13.png", pos )
                            her "Sorry, Professor."
                            her "Well, I heard two girls in the bedroom talking about how they take their boyfriends in their mouths."
                            $herView.hideshowQQ( "body_50.png", pos )
                            her "Of course, they are not from Gryffindor, sir!"
                            m "Of course. Gryffindor girls take nothing in their mouth."
                            $herView.hideshowQQ( "body_120.png", pos )
                            her "You are right, sir. We are too proud for that and ..."
                            m "Miss Granger!"
                            $herView.hideshowQQ( "body_55.png", pos )
                            her "Sir?"
                            m "Is this how you earn 15 points?"
                            her "Excuse me, sir! .. Well, one of them, a blonde, talked about how her boyfriend cums so much that it even pours from her nose."
                            $herView.hideshowQQ( "body_55.png", pos )
                            her "Well, to tell you the truth, sir, she must just have boasted to the brunette."
                            her "There is never that much sperm, she must have taken it directly in the nose."
                            m "How do you know, Miss Granger?"
                            m "You also took part in this?"
                            $herView.hideshowQQ( "body_103.png", pos )
                            her "No, sir, I do not do that! I just know ... I have my sources."
                            m "Sources of sperm? Hehe."
                            $herView.hideshowQQ( "body_30.png", pos )
                            her "Argh! If you are going to talk like that, sir, I'll just leave."
                            m "Miss Granger! You promised to tell me something interesting, but so far I have not heard anything."
                            m "More of this and I will give up on you and you do not get any points."
                            $herView.hideshowQQ( "body_28.png", pos )
                            her "Give me a chance, sir. Okay?"
                            $herView.hideshowQQ( "body_56.png", pos )
                            her "Well ... One girl confessed to me that she likes to walk around without underwear."
                            her "When she walks down the stairs and guys look up her skirt, she feels ... she is excited, sir."
                            m "{size=-4}(Oh, that's better...){/size}"

                            $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                            $herView.hideQ()
                            hide screen blktone
                            with d3
                            ">You put your hands under the table and grasp your cock..."
                            hide screen blktone8
                            with d3
                            hide screen genie
                            show screen genie_jerking_off
                            with d3
                            pause
                            $herView.hideQQ()
                            $ pos = POS_370

                            $herView.hideshowQQ( "body_122.png", pos )
                            her "There is this other girl..."
                            her "When she was in Hogsmeade, she did something with a dwarf..."
                            m "{size=-4}(What a slut ... ah ... yes ...){/size}"
                            her "And two other girls..."
                            $herView.hideshowQQ( "body_187.png", pos )
                            her "They fingered each other at recess. And the guys watched. It's just disgusting, Professor!"
                            m "{size=-4}(Oh, yeah-e-ah ... I'm sure it was a sight!){/size}"
                            $herView.hideshowQQ( "body_118.png", pos )
                            her "And then this little girl. They say, she puts a carrot in her a... well, you know."
                            her "It's like she practices ... so that it will be easier to get..."
                            m "{size=-4}(Yeah ... that's it ... a diligent slut ... more!){/size}"
                            $herView.hideshowQQ( "body_68.png", pos )
                            her "And another girl, she jerked off two at once..."
                            m "{size=-4}(Yes! Yes!){/size}"
                            $herView.hideshowQQ( "body_56.png", pos )
                            her "And then knelt down and took a third in her mouth..."
                            m "{size=-4}(Oh, whores, I'm gonna...){/size}"
                            $herView.hideshowQQ( "body_122.png", pos )
                            her "That's all, Professor."
                            g4 "What?!"
                            $herView.hideshowQQ( "body_111.png", pos )
                            her "You pay me 15 points for the story. But the end is worth the same amount."
                            g4 "Little bitch!"
                            menu: 
                                "\"You get nothing!\"":
                                    with d3
                                    hide screen genie_jerking_off
                                    show screen genie
                                    with d3
                                    m "You get nothing!"
                                    m "No points!"
                                    $herView.hideshowQQ( "body_05.png", pos )
                                    her "Very well, Professor! In that case, do not expect that I will continue to meet your every whim!"
                                    $hermi.liking -= 30
                                    jump request_01_done
                                "\"Fair. That's good enough...\"":
                                    m "Argh! Well, allright ... good enough"
                                    with d3
                                    hide screen genie_jerking_off
                                    show screen genie
                                    with d3
                                    $herView.hideshowQQ( "body_04.png", pos )
                                    her "As you say, sir. I'm ready to get the [current_payout] points."
                                "\"Go on, you will get your points!\"":
                                    $current_payout+=15
                                    m "Do not stop, I'll give you the points! Go Ahead!"
                                    $herView.hideshowQQ( "body_127.png", pos )
                                    her "Yes, sir. These whores, sir, every day they suck a couple of guys and ask them to cum on their face."
                                    her "And go around with their face covered in sperm. They say that it is good for the skin."
                                    m "{size=-4}(Yeah, come on...more!){/size}"
                                    her "And this Slytherin girl promised the guys from the Quidditch team that she will blow them all if they win."
                                    her "Also, sir, one girl wanked a teacher..." 
                                    her "And then immediately went to another and wanked him..."
                                    m "{size=-4}(Oh, yeah-ah ... these whores!){/size}"
                                    $herView.hideshowQQ( "body_78.png", pos )
                                    her "I heard there was a new game. it is called \"Guess a hole\"."
                                    m "{size=-4}(Guess ... Ahh ... yes ....){/size}"
                                    $herView.hideshowQQ( "body_58.png", pos )
                                    her "They make a hole in a wooden partition, where several girls expose their..."
                                    her "Charms, sir. And if the guy guessed who it is..."
                                    m "{size=-4}(Oh, yeah ... yeah ... I will ... already!){/size}{size=+2} * Argh! *{/size}"
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
                                    
                                    $music("Supergirl")                                   
                                    show screen bld1
                                    with d3
                                    $herView.showQQ( "body_64.png", pos )
                                    her "Oh, what a powerfull ejaculate, Professor! Did you like it?"
                                    show screen genie_jerking_sperm_02
                                    with d3
                                    g4 "Oh, shit, it's so... It's incredibly fucking amazing!..."
                                    show screen genie
                                    #show screen genie_jerking_off
                                    with d3
                                    $herView.hideshowQQ( "body_111.png", pos )
                                    her "I'm glad that you came Professor. But still, can I get my points? Just [current_payout] points."
                                    m "Oh-x... Ufff... Yes, you can but..."
                                    m "... what's up with the game \"Guess a hole\"? You did not tell me."
                                    $herView.hideshowQQ( "body_46.png", pos )
                                    her "You already finished, sir. But if you want to learn..."
                                    m "What?! Are you extorting points again?"
                                    her "A total of 15 points, sir."
                                    m "You abuse me, girl!"
                                    $herView.hideshowQQ( "body_58.png", pos )
                                    her "I am sorry, sir, then I'll just get my [current_payout] points and go."
                                    menu: 
                                        "\"Go away!\"":
                                            m "Go away. And remember blackmail will not work!"
                                            $herView.hideshowQQ( "body_58.png", pos )
                                            her "Yes,sir..."
                                        "\"Fair Enough. 15 points, tell me. But this is the last time!\"":
                                            $current_payout+=15
                                            m "Okay, but remember, this is the last time!"
                                            $herView.hideshowQQ( "body_64.png", pos )
                                            her "Of course, I understand."
                                            $herView.hideshowQQ( "body_56.png", pos )
                                            her "In general, if a guy guesses..."
                                            her "Um ... well, guesses whose it is, then she would have to let him have her anyway he wants."
                                            her "And if he does not guess, he becomes common for the night."
                                            m "Common?"
                                            her "Yes, sir. The girls take him to his bedroom and he has to do everything for them."
                                            m "?!..."
                                            $herView.hideshowQQ( "body_122.png", pos )
                                            her "{size=+4}Absolutely{/size} everything that each of them wants, sir!"
                                            m "Oh shit!"
                                            her "Professor, I think you rise once again. If you want to continue, then only 15 Pts ..."
                                            m "No !!! Enough for today!"
                                            $herView.hideshowQQ( "body_58.png", pos )
                                            her "Of course, professor."
                                    her "...................."
                                    hide screen genie_jerking_sperm_02
                                    with d3
                                    $music()




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
    if hermi.whoring >= 0 and hermi.whoring <= 2: #LEVEL 01
        her "*sigh of relief*"
    m "Yes, you can go now."
    if IsFirstRun():
#    if request_01 == 0:
        $herView.hideshowQQ( "body_01.png", pos )
        her "Another [current_payout] points... The Guys will be so happy."
        her "Thank you, professor."

    label request_01_done:
    if hermi.whoring <= 2:
            $ hermi.whoring +=1
 
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
        m "\"Guess a hole\", wow..." 
        m "What can't these sluts come up with!"
        $posHead=gMakePos( 390, 235 )
    
    
    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###

    $event.Finalize()    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
