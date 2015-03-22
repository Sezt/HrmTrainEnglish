
###################REQUEST_10 (Level 03) (25 pt.) (Let a classmate touch you). (Available during daytime only).
label new_request_10:
    
    $herView.hideQQ()
    m "{size=-4}(Tell her to go get touched by one of her classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request
            
    $ pos = POS_140

    if request_10_points == 0: # <================================================================================ FIRST TIME
        m "Miss Granger?"
        $herView.showQQ( "body_01.png", pos )
        her "Sir?"
        m "You do like boys your age, don't you?"
        $herView.hideshowQQ( "body_03.png", pos )
        her "...?"
        m "one of your classmates maybe?"
        $herView.hideshowQQ( "body_10.png", pos )
        her "Well..."
        her "Must I really discuss things like this with you, sir?"
        $herView.hideshowQQ( "body_29.png", pos )
        her "It's a bit embarrassing..."
        m "Sure, I understand. I don't need to know the details..."
        m "But here is what I need you to do today, miss Granger."
        m "Go confront that boy you fancy. The one you think is \"just so dreamy\"..."
        $herView.hideshowQQ( "body_31.png", pos )
        her ".......?"
        m "And let him touch you..."
        if hermi.whoring <=5 or request_02_c_points <= 1: # Counts how many times Hermione been sent to flirt with teachers.
            jump too_much
        $herView.hideshowQQ( "body_31.png", pos )
        her "Let him... touch me, sir?"
        m "Yes, touch you. The way boys touch girls?"
        m "How old are you, girl? You look mature enough..."
        m "Haven't you had \"the talk\" with your parents already?"
        $herView.hideshowQQ( "body_34.png", pos )
        her "\"The talk\", sir?"
        m "Yes, \"the talk\"! About how boys are different than the girls...?"
        m "Boys have a \"pee-pee\" and girls like to put that  \"pee-pee\" in their mouths?"
        $herView.hideshowQQ( "body_03.png", pos )
        her "!!!"
        $herView.hideshowQQ( "body_47.png", pos )
        her "What kind of demented parent would have such a talk with their child?"
        m "I bet Akabur would."
        $herView.hideshowQQ( "body_17.png", pos )
        her "I beg your parodon, sir?"
        m "*Khem!* I said, a responsible and caring one!"
        m "Well, in any case. That is your task for today, miss Granger."
        m "Find a way to persuade one of your classmates to fondle you a little..."
        $herView.hideshowQQ( "body_69.png", pos )
        her ".........."
        m "You are a pretty girl, it shouldn't be too hard."
        her "....................."
        $herView.hideshowQQ( "body_66.png", pos )
        her "How many points would I receive after completing such a task, sir?"
        m "Hm... Twenty five should do..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "Twenty five house points..."
        her "...."
        $herView.hideshowQQ( "body_66.png", pos )
        her "Well, so be it then..."
        m "Great..."
        $herView.hideshowQQ( "body_05.png", pos )
        her "I'd better go now. The classes are about to start..."
        $herView.hideQ()
    else:
        if hermi.whoring >= 6 and hermi.whoring <= 8: # LEVEL 03 
            m "Miss Granger?"
            $herView.showQQ( "body_01.png", pos )
            her "Sir?"
            m "How about you go let one of your classmates molest you a little again?"
            $herView.hideshowQQ( "body_120.png", pos )
            her "........"
            m "Twenty five house points, girl."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Sir, it's just..."
            $herView.hideshowQQ( "body_79.png", pos )
            her "I do not understand why I must do things like that..."
            m "To help out your house?"
            $herView.hideshowQQ( "body_66.png", pos )
            her "That's not what I meant..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Oh, never mind..."
            her "The classes are about to start, I'd better go..."
            m "Will you do it?"
            $herView.hideshowQQ( "body_66.png", pos )
            her "I don't know... Maybe..."
            $herView.hideQ()
        elif hermi.whoring >= 9 and hermi.whoring <= 11: # LEVEL 04
            m "Miss Granger, I need you to go out there, and make one of your classmates molest you a little."
            $herView.showQQ( "body_01.png", pos )
            her "I understand, sir..."
            m "Off you go then."
            her "..........."
            $herView.hideQ()
        elif hermi.whoring >= 12: # LEVEL 05+
            m "Miss Granger, I need you to go out there..."
            m "Find a handsome guy and force yourself on him!"
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $herView.showQQ( "body_01.png", pos )
            her "You mean like..."
            $herView.hideshowQQ( "body_122.png", pos )
            her "In a sexual way, sir?"
            m "What? No, I mean just let him get under your uniform that's all..."
            $herView.hideshowQQ( "body_24.png", pos )
            her "Oh, I see..."
            $herView.hideshowQQ( "body_68.png", pos )
            her "I wonder who it should be this time..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "More than one boy, is not a problem, is it, sir?"
            m "A problem? Of course not!"
            m "If anything - it is encouraged." 
            $herView.hideshowQQ( "body_122.png", pos )
            her "Great. I will see you after the classes then, sir. As usual."
            m "Yes. Good luck."
            $herView.hideQ()

   

#    $ request_10 = True

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

    $event.Finalize()    

    jump day_main_menu

        


label new_request_10_complete: #<==========================================================================EVENING
    
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
            m "Give me the details."
            show screen blktone
            with d3
            
            if hermi.whoring >= 6 and hermi.whoring <= 8: # LEVEL 03 # EVENT LEVEL 01.
                stop music fadeout 3.0
                $herView.hideshowQQ( "body_12.png", pos )
                her "......"
                $herView.hideshowQQ( "body_13.png", pos )
                her "Well... Em..."
                m "Speak up, girl."
                m "Did you let some lucky guy feel you up or what?"
                    
                if one_out_of_three == 1: ### EVENT (A)
                    her "I did, sir..."
                    m "So? Tell me more."
                    her "Well, there is not much to tell..."
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "I told that one guy I know that he could touch me a little if he wants..."
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "He thought I was joking at first..."
                    $herView.hideshowQQ( "body_33.png", pos )
                    her "So embarrassing..."
                    m "So, did he cop a feel or not?"
                    $herView.hideshowQQ( "body_33.png", pos )
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "He did..."
                    m "Well, where did he touch you, girl?"
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "Ehm... My legs..."
                    her "And my breasts a little I suppose..."
                    m "That's all?"
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "Yes, sir..."
                    $herView.hideshowQQ( "body_33.png", pos )
                    her "It's getting late... I think I'd better leave now..."
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "I'm sorry, sir..."
                    m "Nothing to be sorry about, girl."
                    m "You did good. This will do for now."
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    stop music fadeout 3.0
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "I did, sir."
                    her "But it was all very awkward and embarrassing..."
                    m "That's the whole point of it, girl."
                    m "Tell me where you were touched today..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Ehm..."
                    $herView.hideshowQQ( "body_117.png", pos )
                    her "Well he touched me under my skirt a little..."
                    her "Then I let him rub my..."
                    $herView.hideshowQQ( "body_118.png", pos )
                    her "...my pussy through the panties, sir."
                    m "Very good. Then what happened?"
                    $herView.hideshowQQ( "body_131.png", pos )
                    her "Then he sort of started to touch himself sir..."
                    her "So, I decided to leave..."
                    m "I see..."
                    $herView.hideshowQQ( "body_33.png", pos )
                    her "............."
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    her "I did, sir..."
                    $herView.hideshowQQ( "body_31.png", pos )
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "I led this one guy from \"Hufflepuff\" to an empty classroom and I told him that he can touch me if he wants."
                    her "That I don't mind..."
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "..........."
                    m "and?"
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "Well, he did touch me a little at first..."
                    $herView.hideshowQQ( "body_33.png", pos )
                    her "......"
                    m "Don't make me pull every word out of you, girl!"
                    m "Then what happened?"
                    $herView.hideshowQQ( "body_87.png", pos )
                    her "Well..." 
                    stop music fadeout 1.0
                    her "I think he was more interested in {size=+5}me{/size} molesting {size=+5}him{/size}..."
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "He asked me to call him a \"sissy boy\"..."
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "And he kept on reassuring me that he has a very small penis..."
                    $herView.hideshowQQ( "body_22.png", pos )
                    her "He just kept repeating that *sob!*..."
                    $herView.hideshowQQ( "body_21.png", pos )
                    her "Why would anyone be like this?"
                    her "*Sob!* I Could not stay in his company a moment longer, so I just ran."
                    m "I'm sorry to hear this..."
                    $herView.hideshowQQ( "body_21.png", pos )
                    her "It was truly awful, sir..."
                    m "There, there..."
                    $herView.hideshowQQ( "body_23.png", pos )
                    her "*Sob!*"
                    m "Will ten extra points make you feel better?"
                    $herView.hideshowQQ( "body_19.png", pos )
                    her "Huh? That would be very sweet of you sir."
                    $ gryffindor += 10
                    m "Of course... Ten extra points to \"Gryffindor\"."
                    $herView.hideshowQQ( "body_140.png", pos )
                    her "Thank you sir..."
                    m "And the rest of your payment..."
            
            elif hermi.whoring >= 9 and hermi.whoring <= 11: # LEVEL 04
                if one_out_of_three == 1: ### EVENT (A)
                    $herView.hideshowQQ( "body_16.png", pos )
                    her "Well... There is not much to tell..."
                    her "I found this one boy from \"Ravenclaw\"..."
                    her "Led him to one of the empty classrooms in the eastern wing..."
                    her "He thought I wanted to make out with him..."
                    her "But I told him that I just want him to touch me..."
                    $herView.hideshowQQ( "body_33.png", pos )
                    her "...so he did."
                    m "I see..."
                    m "Well done, miss Granger."
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "Will I be getting my points now?"
                    m "In a minute, miss Granger. I have a question I would like to ask you before that."
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "???"
                    m "Did you enjoy it?"
                    m "Did it feel good to be touched by that boy?"
                    $herView.hideshowQQ( "body_127.png", pos )
                    her "Oh..."
                    her "Well, he was rather handsome I suppose..."
                    $herView.hideshowQQ( "body_120.png", pos )
                    her "I didn't hate it, if that's what you mean, sir..."
                    m "I see..."
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    $herView.hideshowQQ( "body_16.png", pos )
                    her "Well..."
                    her "I'm not sure whether or not this counts, but..."
                    her "During the herbology class today..."
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "I let this one boy slide his hand under my skirt..."
                    her "So while Professor Sprout explained the differences between \"mandrake\" and \"mandragore\"..."
                    $herView.hideshowQQ( "body_08.png", pos )
                    her "Something I already knew of course..."
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "I let my lab partner massage my buttocks..."
                    her "And that is all..."
                    m "Hm..."
                    menu:
                        "\"You can do better than that, girl.\"":
                            $herView.hideQQ()
                            $herView.showQQ( "body_31.png", pos )
                            her "Yes, I know, sir. I am sorry."
                            m "Just make sure you try harder next time."
                            her "I will, sir."
                        "\"Kudos on doing this during class.\"":
                            $herView.hideQQ()
                            $herView.showQQ( "body_74.png", pos )
                            her "Thank you, sir."
                            m "I say you deserve to get paid."
                            
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "................."
                    m "???"
                    $herView.hideshowQQ( "body_69.png", pos )
                    
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    
                    her "I don't want to talk about it, sir..." 
                    m "What happened, girl. Spit it out."
                    $herView.hideshowQQ( "body_79.png", pos )
                    her "................."
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "But... it's so embarrassing..."
                    $herView.hideshowQQ( "body_33.png", pos )
                    her "Do I really have to, sir?"
                    m "Yes, I happen to love embarrassing things!"
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "................."
                    her "Well, alright..."
                    her "I approached this one guy that I always found attractive..."
                    her "Managed to muster up enough courage to ask him to follow me..."                                              
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "Normally I wouldn't dare..."
                    her "But the fact that I was doing this as a task entrusted to me by someone else..."
                    her "made it easier somehow..."
                    m "Happy to help, Miss Granger."
                    $herView.hideshowQQ( "body_87.png", pos )
                    her "I led him to the library..."
                    her "We found a secluded spot behind one of the book shelves..."
                    her "And I told him that he can touch me wherever he wants..."                 
                    her "And...."
                    $herView.hideshowQQ( "body_88.png", pos )
                    her ".........."
                    m "What?"
                    $herView.hideshowQQ( "body_33.png", pos )
                    her "....................."
                    $herView.hideshowQQ( "body_32.png", pos )
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    her "He started to touch my... feet, sir."
                    m "Huh?"
                    m "Your \"Feet\"? Is that what kids call tits these days?"
                    $herView.hideshowQQ( "body_66.png", pos )
                    her "I'd wish, sir..."
                    her "He asked me to take off my shoes..."
                    her "Then he..."
                    $herView.hideshowQQ( "body_21.png", pos )
                    her "He started to smell my toes, sir!"
                    $herView.hideshowQQ( "body_22.png", pos )
                    her "I felt so... violated!"
                    m "So he didn't touch your tits, or your butt?"
                    $herView.hideshowQQ( "body_143.png", pos )
                    her "No, sir... *sob!*"
                    m "Alright, then what happened?"
                    $herView.hideshowQQ( "body_142.png", pos )
                    her "Nothing! I couldn't bear the humiliation... I just ran..."
                    her "I even left my shoes behind and had to come back later to pick them up..."
                    $herView.hideshowQQ( "body_145.png", pos )
                    her "*Sob!*............"
                    m "Hm..."
                    m "Well, you did get molested..."
                    m "Although in a rather unconventional manner..."
                    $herView.hideshowQQ( "body_145.png", pos )
                    her "*Sob!* I wish he would have just touched my breasts like a descent boy would, sir... *Sob!*"
                    m "There, there..."
                    m "You earned you pay today..."
        
        
        
            elif hermi.whoring >= 12: # LEVEL 05+
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "......"
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "Well..."
                    her "During the potions class today..."
                    her "I wrote a note on a piece of paper..."
                    her "I was about to slide it to my lab partner when..."
                    $herView.hideshowQQ( "body_69.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Professor Snape snatched it right out of my hand..."
                    $herView.hideshowQQ( "body_79.png", pos )
                    her "He then read it out loud before the entire class..."
                    m "What did the note say?"
                    $herView.hideshowQQ( "body_87.png", pos )
                    her "Well..."
                    her "It said: \"You can touch my butt if you want. I bet professor Snape would never notice.\""
                    $herView.hideshowQQ( "body_118.png", pos )
                    her "Everyone was laughing..."
                    her "It was so embarrassing I wanted to die..."
                    $herView.hideshowQQ( "body_47.png", pos )
                    her "I really hate professor Snape, sir..."
                    m "What happened then?"
                    $herView.hideshowQQ( "body_87.png", pos )
                    her "Nothing..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "But when the class was over..."
                    her "Those three nasty-looking boys from \"Slytherin\" cornered me..."
                    her "Actually they weren't mean to me or anything..."
                    her "So we just waited for everyone to leave the classroom..."
                    $herView.hideshowQQ( "body_117.png", pos )
                    her "And then I let them touch me..."
                    her "They touched me everywhere, professor..."
                    m "\"Everywhere\", huh?"
                    her "Yes... Everywhere, sir..."
                    $herView.hideshowQQ( "body_128.png", pos )
                    her "There were hands under my skirt, under my shirt..."
                    her "And then I started to breathe heavily..."
                    $herView.hideshowQQ( "body_121.png", pos )
                    her "So one of them just put his hand over my mouth..."
                    her "And their hands were so... thorough..." 
                    her "My head started to spin..."
                    $herView.hideshowQQ( "body_128.png", pos )
                    her "It was most exhilarating, sir."
                    m "Very good, miss Granger. Very good indeed."
                    
                    
                if one_out_of_three == 2: ### EVENT (B)
                    $herView.hideshowQQ( "body_01.png", pos )
                    her "Actually something quite unexpected happened to me today, sir..."
                    her "Right after the Defence Against the Dark Arts class..."
                    her "This stocky \"Hufflepuff \" boy came up to me..."
                    $herView.hideshowQQ( "body_122.png", pos )
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "He said someone told him that I let boys touch me..."
                    $herView.hideshowQQ( "body_128.png", pos )
                    her "Normally I would deny everything..."
                    her "But I decided not to waste the opportunity..."
                    $herView.hideshowQQ( "body_78.png", pos )
                    her "I took the boy to a quiet spot and let him touch me..."
                    her "I let him run his hands up and down my thighs..."
                    her "I let him fondle my breasts..."
                    $herView.hideshowQQ( "body_128.png", pos )
                    her "All the usual things..."
                    m "Well done, miss Granger."
                    
                if one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "Well..."
                    her "I did what you told me to do, sir..."
                    her "But... it sort of... ehm..."
                    $herView.hideshowQQ( "body_78.png", pos )
                    her "Well, it sort of escalated into something else..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    m "Hm?"
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "uhm..."
                    her "I sort of... got caught while I was letting this one boy fondle my breasts..."
                    m "You got caught? By one of the teachers?"
                    $herView.hideshowQQ( "body_45.png", pos )
                    her "No, sir..."
                    $herView.hideshowQQ( "body_46.png", pos )
                    her "By the boy's girlfriend..."
                    m "Interesting..."
                    $herView.hideshowQQ( "body_117.png", pos )
                    her "She was furious with him at first..."
                    $herView.hideshowQQ( "body_122.png", pos )
                    her "But then..."
                    $herView.hideshowQQ( "body_124.png", pos )
                    her "Ehm... She started to touch my breasts as well..."
                    $herView.hideshowQQ( "body_111.png", pos )
                    her "Almost the same way her boyfriend did just a moment ago..."
                    her "Then she turned to him and she said..."
                    $herView.hideshowQQ( "body_16.png", pos )
                    her "\"I love you baby, and I want to share everything with you...\""
                    her "\"...And that includes your whores.\""
                    $herView.hideshowQQ( "body_117.png", pos )
                    her "I did not appreciate being called a whore of course..."
                    $herView.hideshowQQ( "body_06.png", pos )
                    her "But that was such a sweet and romantic gesture..."
                    her "Wouldn't you agree, sir?"
                    m "Totally..."
                    m "Seems that true love {size=+5}does{/size} exist after all."
                    m "Then what happened?"
                    $herView.hideshowQQ( "body_24.png", pos )
                    her "Ehm... Well, they kissed of course..."
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "And then they both started to touch me again..."
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "And then he was kind of only touching her and she was only touching him..."
                    her "And they kissed..."
                    her "I suddenly felt like the third wheel in that situation, so I just slipped away quietly..."
                    m "I see..."
                    

    $ gryffindor +=25
    m "The \"Gryffindor\" house gets 25 points!"
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



    $ touched_by_boy = True #Makes sure that Public favours do not get locked after reaching Whoring level 05.
    
    call music_block
    
    $ request_10_points += 1 
#    $ request_10 = False 
    $ hermione_sleeping = True

    $event.Finalize()    

    return



