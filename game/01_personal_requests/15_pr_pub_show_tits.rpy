###################REQUEST_15 (Level 04) (35 pt.) (Flash your tits to a boy). (Available during daytime only).
label new_request_15: #LV.4 (Whoring = 9 - 11)
    
    
    
    $herView.hideQQ()
    m "{size=-4}(Tell her to flash her tits to one of her classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request
            
    
    $ pos = POS_140
    
    if request_15_points == 0: # <================================================================================ FIRST TIME
        m "Miss Granger..."
        m "I would like to award \"Gryffindor\" with 25 house points today."
        $herView.hideshowQQ( "body_01.png", pos )
        her "Really?"
        her "Thank you, sir!"
        m "Yes, but first I will require your help with something..."
        her "Of course, sir! Anything!"
        m "I need you to go out there and show off your tits to people..."
        stop music fadeout 1.0
        $herView.hideshowQQ( "body_02.png", pos )
        her "...?"
        m "You know, flash your breasts to some boys..."
        $herView.hideshowQQ( "body_48.png", pos )
        her "?!!"
        if hermi.whoring <=8 or request_10_points <= 1: # request_10_points - counts how many times Hermione been sent to let boys touch her.
            jump too_much
        her "Professor Dumbledore!"
        $herView.hideshowQQ( "body_47.png", pos )
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "This is a completely new level of inappropriate, even for you, sir!"
        her "How can you ask one of your pupils to perform such a task?"
        m "So that's how you feel then? I see..."
        m "I suppose I will be awarding those points to some other house instead ..."
        m "\"Slytherin\" perhaps?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "................"
        m "But, you know, no pressure..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "Professor..."
        her "The fate of my house is very important to me, but..."
        m "Is it really?"
        m "Why don't you show it to me then?"
        m "Yes. Show me how important it is to you exactly, miss Granger."
        $herView.hideshowQQ( "body_47.png", pos )
        her "But this is inappropriate..."
        m "Are we really in any position to discuss what is appropriate and what is not at this point?"
        $herView.hideshowQQ( "body_69.png", pos )
        her ".................."
        m "I would say that ship has sailed a long time ago..."
        $herView.hideshowQQ( "body_66.png", pos )
        her ".............."
        m "All I ask you to do is to give some lucky boy a quick peek..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "But why? Why must I do things like this, sir?"
        m "A minute of your time for 25 house points..."
        m "A pretty nifty deal, wouldn't you agree?"
        her "I suppose..."
        her "Well alright, I'll see what I can do..."
        
    else: # <================================================================================ NOT FIRST TIME
        if hermi.whoring >= 9 and hermi.whoring <= 11: # LEVEL 04 FIRST EVENT.
            m "I think you need to show off your tits some more, girl."
            $herView.hideshowQQ( "body_44.png", pos )
            her "You mean to you, sir?"
            m "No, to your classmates..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "Oh..."
            m "Yes, go do that and then report back to me..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Will I get paid for this?"
            m "Of course you will get paid for this, girl. Don't be silly."
            m "Thirty five house points. The usual rate..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "................."
            $herView.hideshowQQ( "body_66.png", pos )
            her "Well alright... I will see what I can do, sir..."
            
        elif hermi.whoring >= 12 and hermi.whoring <= 14: # LEVEL 05
            m "Miss Granger. I have a question for you."
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Why do you think women have breasts?"
            $herView.hideshowQQ( "body_44.png", pos )
            her "...what do you mean, sir?"
            m "Alright, let me rephrase this..."
            m "What would you say is the most common application for the female mammary glands?"
            $herView.hideshowQQ( "body_15.png", pos )
            her "Oh..."
            $herView.hideshowQQ( "body_17.png", pos )
            her "Production of milk?"
            m "Good. What else do women use their tits for?"
            $herView.hideshowQQ( "body_13.png", pos )
            her "Hm.."
            $herView.hideshowQQ( "body_17.png", pos )
            her "...to attract men?"
            m "Yes. Let's concentrate on that."
            m "I need you to go out there..."
            m "Find some lucky bastard..."
            m "And flash him your tits..."
            $herView.hideshowQQ( "body_66.png", pos )
            her "{size=-3}(I just knew that this was exactly where this conversation was heading...){/size}"
            m "What was that, miss Granger?"
            $herView.hideshowQQ( "body_69.png", pos )
            her "I said I'd better go then, sir."
            her "my classes are about to start..."
            m "Thirty five house points will be waiting for you here upon your return, girl."
            $herView.hideshowQQ( "body_79.png", pos )
            her ".............."
            
        elif hermi.whoring >= 15: # LEVEL 06+
            m "Girl I need you to go out there and flash your tits to one of your classmates."
            $herView.hideshowQQ( "body_127.png", pos )
            her "I will do my best sir."
            m "Really? Just like that? No complaints or anything?"
            $herView.hideshowQQ( "body_128.png", pos )
            her "I am getting paid for this, am I not?"
            m "Of course."
            $herView.hideshowQQ( "body_127.png", pos )
            her "Why would I complain about a simple task like this then?"
            her "Thirty five house points is a fair prices for a few seconds of excitement... err..."
            $herView.hideshowQQ( "body_74.png", pos )
            her "...I mean, embarrassment."
            m "{size=-3}(She changed this much already?){/size}"
            g9 "{size=-3}(I'm so good at this training thing that it's starting to get creepy!){/size}"
            $herView.hideshowQQ( "body_45.png", pos )
            her "Classes are about to start... I'd better leave now."
            her "I will see you later tonight, sir."

    

    
    $ request_15 = True

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
    
    $event.Finalize()    

    jump day_main_menu
    
    
    
    

        



label new_request_15_complete:
    
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

    if hermi.whoring >= 9 and hermi.whoring <= 11: # LEVEL 04 <=============================================================EVENT LEVEL 01                    
        if one_out_of_three == 1: ### EVENT (A)
                

                $herView.showQ( "body_31.png", pos )
                show screen hermione_02
                with Dissolve(.3)
                her "Good evening, sir..."
                m "Miss Granger..."
                m "So, how did it go?"
                $herView.hideshowQQ( "body_34.png", pos )
                her "Ehm... Not too well, actually..."
                her "................................"
                m "Just tell me what happened, girl."
                $herView.hideshowQQ( "body_31.png", pos )
                her "That is the thing, sir..."
                her "Nothing happened..."
                $herView.hideshowQQ( "body_87.png", pos )
                her "I just couldn't bring myself to do it..."
                m "I see..."
                m "Well, I can't just give you the points for nothing, girl."
                $herView.hideshowQQ( "body_16.png", pos )
                her "Of course, sir... I understand..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "I shall try harder next time... I promise..."
                m "Then I will just put these thirty five points aside for now..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Thank you, sir..."
                her "..."
                her "I'd better go now."
                $ request_15 = False 
                $ hermione_sleeping = True
                $ request_15_points += 1 
                jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).

        elif one_out_of_three == 2: ### EVENT (B)
            m "Miss Granger, did you complete your task?"
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $herView.hideshowQQ( "body_29.png", pos )
            her "Ehm... Sort of..."
            m "Sort of?"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Yes... uhm..."
            her "Well, I decided to try and flash them to this \"hufflepuff\" boy..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "I've been waiting for the right moment..."
            her "I was worried that something would go wrong..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "And, of course, everything that could - did..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "When I tried to expose myself to the boy..."
            her "At first I only pulled up my vest..."
            her "Then I tried to pull my shirt up as well..."
            her "And one of my breasts got entangled in the fabric and was pulled up along with the shirt..."
            $herView.hideshowQQ( "body_32.png", pos )
            her "So only one of my breasts was naked and I was desperately trying to free the other one."
            her "Other students started to pay attention to me..."
            her "So I had to fix my clothes back into place quickly..."
            her "And then the moment was gone..."
            $herView.hideshowQQ( "body_33.png", pos )
            her "............"
            m "Hm..."
            m "What about the boy? Did he see your tits or not?"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Well, I think he may have seen one of them..."
            her "But from the way he was looking at me..."
            her "I doubt that he understood that the whole commotion was for his benefit."
            $herView.hideshowQQ( "body_29.png", pos )
            her "......................"
            $herView.hideshowQQ( "body_31.png", pos )
            her "I'm sorry, sir..."
            m "That's alright..."
            m "I wouldn't expect you to perform perfectly this early in your training..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "(My training?)"
            
        elif one_out_of_three == 3: ### EVENT (C)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_29.png", pos )
            her "Yes I did, sir."
            m "Good. Tell me more."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Ehm... There is not much to tell, really..."
            her "I spent the first half of the day with studying in the library..."
            her "It is usually quite deserted during that time..."
            her "Apart from me there was only one student..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "Some boy from \"Ravenclaw\"..."
            her "So I waved to him and when he looked up at me..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "I quickly pulled my shirt up..."
            m "Good job."
            m "How did he react to the sight of your naked tits?"
            $herView.hideshowQQ( "body_118.png", pos )
            her "I'm not sure..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "He looked rather shocked I suppose..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "After I showed him my breasts it got too embarrassing for me to stay there any longer..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "So I just gathered all my books and left..."
            m "I see..."
            
    elif hermi.whoring >= 12 and hermi.whoring <= 14: # LEVEL 05 <=============================================================EVENT LEVEL 02
        if one_out_of_three == 1: ### EVENT (A)
            stop music fadeout 1.0
            show screen blktone
            with d3
            m "Miss Granger. Did you complete your task?"
            $herView.hideshowQQ( "body_44.png", pos )
            her "Yes I did, sir."
            $herView.hideshowQQ( "body_118.png", pos )
            her "............."
            m "Well? How did it go?"
            $herView.hideshowQQ( "body_118.png", pos )
            her "................"
            $herView.hideshowQQ( "body_69.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "Just for the record, sir..."
            m "Hm?"
            $herView.hideshowQQ( "body_30.png", pos )
            her "I think that forcing your pupils to do things like this..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "Is beneath an esteemed wizard such as yourself..."
            m "\"Forcing\"? Nobody is forcing you to do anything, girl."
            m "You came to me, remember?"
            $herView.hideshowQQ( "body_31.png", pos )
            her ".........."
            m "You begged me to buy a sexual favour from you."
            $herView.hideshowQQ( "body_29.png", pos )
            her "...I...."
            $herView.hideshowQQ( "body_31.png", pos )
            her "I never said \"sexual\"..."
            m "Nevertheless, you can stop selling me these favours at any moment, miss Granger."
            $herView.hideshowQQ( "body_69.png", pos )
            her "I suppose..."
            m "And yet you keep on coming back..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "............................"
            m "I think you may actually be taking some twisted form of pleasure from this."
            $herView.hideshowQQ( "body_47.png", pos )
            her "What?"
            m "Shame on you, miss Granger. Shame on you."
            $herView.hideshowQQ( "body_47.png", pos )
            her "Sir, I never...!"
            m "Enough of this. Did you complete your task or not?"
            $herView.hideshowQQ( "body_120.png", pos )
            her "Yes I did..."
            m "And?"
            $herView.hideshowQQ( "body_87.png", pos )
            her "And that is all I am going to say..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "........"
            m ".........."
            her "........"
            m "Oh, whatever. Just take your points and go."
            $herView.hideshowQQ( "body_120.png", pos )
            her "Thank you, sir."

        elif one_out_of_three == 2: ### EVENT (B)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Miss Granger..."
            $herView.hideshowQQ( "body_33.png", pos )
            her "Good evening, sir..."
            m "Did you complete your task?"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Yes, I did, sir..."
            $herView.hideshowQQ( "body_33.png", pos )
            her ".........."
            m "................"
            her "..............."
            m "Well?"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Can I get paid now please?"
            m "Not before you tell me what exactly you did today."
            $herView.hideshowQQ( "body_33.png", pos )
            her "...................."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Do I really have to, sir?"
            m "When you are being coy like this..."
            m "It only makes me more curious. You know that, right?"
            $herView.hideshowQQ( "body_117.png", pos )
            her "Aww..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Well... Ehm..."
            her "Well, alright, here it goes..."
            $herView.hideshowQQ( "body_32.png", pos )
            her "I flashed my tits to that \"Slytherin\" underclassman in a corridor..."
            her "But I was standing too close to him..."
            $herView.hideshowQQ( "body_33.png", pos )
            her "...."
            her "...."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Well, he sort of grabbed one of my breasts, sir..."
            her "he squeezed it hard and just wouldn't let go..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "He made me promise to meet him after my classes..."
            her "And let him..."
            $herView.hideshowQQ( "body_131.png", pos )
            her "\"Play with my tits\" some more..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "You see, that is why I hate \"slytherin\" boys, sir..."
            her "They don't have a shred of honour.."
            her "..."
            m "Did you keep your promise?"
            $herView.hideshowQQ( "body_117.png", pos )
            her "No, not yet..."
            her "I'm planning to meet that awful boy after we are done here, sir."
            m "I see..."
            m "Well, I shouldn't keep you waiting then, should I?"
            
        elif one_out_of_three == 3: ### EVENT (C)
            m "Miss Granger, did you complete your task?"
            show screen blktone 
            with d3
            $herView.hideshowQQ( "body_14.png", pos )
            her "I did sir..."
            m "I'm listening..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Well..."
            her "I had to spend a big portion of the day at the school library..."
            her "So I didn't really have the time to perform your task properly, sir..."
            m "Hm...?"
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Instead I just went to the library window and..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "...I just pulled my shirt up and pressed my bare breasts against the glass..."
            her "I stood there like that for several seconds..."
            her "To make sure that at least someone sees me from the outside..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "I hope this still counts, sir..."
            m "Hm..."
            m "How many students would you say saw you standing behind that window?"
            $herView.hideshowQQ( "body_118.png", pos )
            her "I am not sure, sir... A couple maybe...?"
            m "\"Maybe\"?"
            $herView.hideshowQQ( "body_182.png", pos )
            her "I don't know, sir..."
            her "To be honest I kept my eyes closed..."
            m "How do you know that anyone saw you at all then, girl?"
            $herView.hideshowQQ( "body_141.png", pos )
            her "I heard someone shout: \"Look! At that window over there!\"."
            her "When I heard that I covered up and quickly left..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "...."
            m "Hm..."
            m "Well, alright... I think this counts..."

    elif hermi.whoring >= 15: # LEVEL 06+ <=============================================================EVENT LEVEL 03
        if one_out_of_three == 1: ### EVENT (A)
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_45.png", pos )
            her "I did sir..."
            m "I'm listening..."
            $herView.hideshowQQ( "body_44.png", pos )
            her "Well... I had to spend a big portion of the day in the school library..."
            her "So I didn't really have the time to perform your task properly, sir..."
            m "Hm...?"
            $herView.hideshowQQ( "body_117.png", pos )
            her "Instead I just went to the library window..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Pulled my shirt up and pressed my naked breasts against the glass..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "And then I just stood there like that for a while..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "It did not take long before someone in the yard noticed me..."
            her "I don't think they were able to see my face from there..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Or at least I hope so..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "But they definitely saw my breasts being pressed against that cold window glass, sir..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "A small crowd gathered up rather quickly..."
            $herView.hideshowQQ( "body_121.png", pos )
            her "People were shouting and cheering and pointing at my bare chest..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "Then I saw several of the boys running towards the library entrance..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "I had to leave quickly to avoid being discovered..."
            m "Hm..."
            m "How many people would you say saw your tits today, miss Granger?"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Hard to say, sir..."
            her "Two dozen boys or so I suppose..."
            $herView.hideshowQQ( "body_29.png", pos )
            her "A few girls as well..."
            her "I think the school librarian may have seen me too..."
            m "Hm... Well, I'd say that's a job well done."
            
        elif one_out_of_three == 2: ### EVENT (B)
            stop music fadeout 1.0
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_45.png", pos )
            her "Yes I did, sir."
            m "Well, tell me all about it, then."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Ehm... Alright..."
            her "I was flashing my tits to this boy in the \"Gryffindor\" common room..."
            $herView.hideshowQQ( "body_14.png", pos )
            her "When my friend, Ginny walked in on us..."
            m "Another boy?"
            $herView.hideshowQQ( "body_13.png", pos )
            her "A boy? No, Ginny is a girl's name, sir."
            m "....."
            $herView.hideshowQQ( "body_14.png", pos )
            her "Ginny Weasley, sir."
            m "Alright, fine, continue..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "em..."
            her "......."
            $herView.hideshowQQ( "body_24.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "*Giggle*"
            m "Hm...?"
            $herView.hideshowQQ( "body_46.png", pos )
            her "Then Ginny grabbed my breasts..."
            her "And started to squeeze them..."
            her "then she started to kiss my breasts passionately..."
            m "............"
            $herView.hideshowQQ( "body_111.png", pos )
            her "to kiss and suck on my nipples..."
            $herView.hideshowQQ( "body_128.png", pos )
            her "And I couldn't help myself - I started to moan..."
            m ".............."
            $herView.hideshowQQ( "body_129.png", pos )
            her "And then the boy took out his throbbing cock..."
            her "And sprayed his hot spunk all over me and Ginny!"
            $herView.hideshowQQ( "body_111.png", pos )
            her "And then me and Ginny, we licked his hot sperm off of our young bodies..."
            m ".............."
            m "Are you making this up, girl?"
            $herView.hideshowQQ( "body_24.png", pos )
            her "...maybe."
            $herView.hideshowQQ( "body_128.png", pos )
            her "I just thought that you would like to hear something like that, sir..."
            m "What I would like to hear, girl, is the truth."
            $herView.hideshowQQ( "body_127.png", pos )
            her "Even if it's incredibly dull, sir?"
            m "Dull or not..."
            m "I only want to know what actually happened..."
            m "Keep your fantasies to yourself, girl."
            $herView.hideshowQQ( "body_70.png", pos )
            her "As you wish, sir."
            her "My friend Ginny walked in on my flashing my tits to that guy."
            her "But She promised me that she won't tell anyone."
            $herView.hideshowQQ( "body_15.png", pos )
            her "And that's all that happened, sir..."
            m "I see..."
            m "I still prefer this to some made up stories..."
            
        elif one_out_of_three == 3: ### EVENT (C)
           
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_45.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "Yes I did, sir..."
            m "Alright, tell me how did it go."
            $herView.hideshowQQ( "body_29.png", pos )
            her "Well, let's see..."
            her "First I flashed them to that one boy from \"Ravenclaw\"..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Then to that upperclassman from \"Hufflepuff\"..."
            $herView.hideshowQQ( "body_45.png", pos )
            her "Then there was this other boy from \"Ravenclaw\"."
            m "???"
            $herView.hideshowQQ( "body_34.png", pos )
            her "After that I flashed my tits to some \"Gryffindor\" underclassman by mistake..."
            $herView.hideshowQQ( "body_29.png", pos )
            her "No, wait...  the boy from \"Gryffindor\" was after that other boy..."
            m "How many boys did you flash your tits to today, miss Granger?"
            $herView.hideshowQQ( "body_117.png", pos )
            her "Half a dozen or so?"
            $herView.hideshowQQ( "body_122.png", pos )
            her "I had an opening in my schedule..."
            her "So I decided to go for some extra credit with your assignment, sir."
            m "This is not an assignment, miss Granger..."
            m "And there are no extra credits..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Oh...?"
            m "You are still getting your usual payment, girl, and that's it."
            $herView.hideshowQQ( "body_29.png", pos )
            her "Oh... I see..."
            m "But, miss Granger..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Yes, sir?"
            g9 "That was very well done."
            $herView.hideshowQQ( "body_128.png", pos )
            her "Thank you, sir."
        


    $ gryffindor +=35
    m "The \"Gryffindor\" house gets 35 points!"
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
    
    $ posHead = gMakePos( 390, 340 )
    if one_out_of_three == 2 and hermi.whoring >= 12 and hermi.whoring <= 14: #Event level 02.
        $ hermione_chibi_xpos = 610 # Stands near the door.
        show screen hermione_01_f #Hermione stands still.
        pause.3
        $herViewHead.showQ( "body_120.png", posHead )
        her "\"Slytherin\"..."
        $herViewHead.hideQ()
        hide screen hermione_01_f #Hermione stands still.
    
    if one_out_of_three == 3 and hermi.whoring >= 12 and hermi.whoring <= 14: #Event level 02.
        $ hermione_chibi_xpos = 610 # Stands near the door.
        show screen hermione_01_f #Hermione stands still.
        pause.3
        $herViewHead.showQ( "body_120.png", posHead )
        her "(I can't believe I did that today...)"
        her2 "(What if Harry or Ron saw me like that?)"
        her "(Standing there...)"
        her "(Pressing my breasts against that window glass...)"
        her2 "(I would probably just die of embarrassment right there on the spot...)"
        her2 "(No. Protecting the honor of the \"Gryffindor\" house is my number one priority.)"
        her2 "(We must get the cup this year, no matter the cost...)"
        her "(........)"
        $herViewHead.hideQ()
        hide screen hermione_01_f #Hermione stands still.
    
    if hermi.whoring >= 15 and one_out_of_three == 1: # LEVEL 06+ <=============================================================EVENT LEVEL 03
        $ hermione_chibi_xpos = 610 # Stands near the door.
        show screen hermione_01_f #Hermione stands still.
        pause.3
        $herViewHead.showQ( "body_123.png", posHead )
        her "........................."
        $herViewHead.hideQ()
        hide screen hermione_01_f #Hermione stands still.

            
            
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)


 
 
 
 
    
    $ request_15_points += 1 
    $ request_15 = False 
    $ hermione_sleeping = True

    call music_block

    $event.Finalize()    

    return
    
    
    
    
    
    
    

