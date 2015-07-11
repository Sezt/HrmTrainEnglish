label event_00:
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
   
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $snape.chibi.State("door", speed="go").Trans(d3, "blink")
    pause.3
    $screens.ShowD3("bld1")

    $hero(g4, "#(An Indigenous life form!?)")

    $screens.HideD3("bld1").ShowPos(d3, "thought", gMakePos( 650, 180 )).Pause(1).ShowD3("bld1")

    $hero(m,    "#(Looks human enough...)// #(Maybe if I just act cool he'll leave...?)")

    $screens.HideD3("bld1", "thought")

    $snape.LoadDefItemSets() # Эта функция просто перечитывает значения из xml. Актуальна, если что-то поменялось в наборах xml при отладке

    $snape.chibi.Trans("go center", "blink")
    $screens.ShowD3("bld1")
    $snape.State("doorleft").Visibility("body", transition=Dissolve(.5))
    $screens.ShowHide(d3, "ctc", 0.0)

    $snape("~01",    who2, "Альбус... есть минута?")
    $hero("#(\"Albus\"? Is that supposed to be my name or is it just how the humans of this world greet each other?)")

    menu:
        m "..."
        "\"Actually I'm a bit busy.\"":
            $snape("~04", who2, "Well, aren't you always, Albus?")                            
        "\"Of course. What is it?\"":
            pass                       
        "\"And Albus to you too.\"":
            $snape("~05", who2, "What?",
                   "~04", who2, "Albus, I'm not in the mood for your... shenanigans.") 
        "\"Take me to your leader.\"":
            $snape("~01", who2, "What?// Hm...// You mean the minster of magic?",
                   "~03", who2, "I would rather avoid having to deal with that bureaucrat...")
            $hero("Fine, never mind... How can I be of help?")

            
    $snape("~06", who2, "I have something important I need to discuss with you...// I think we need to revise our admittance policy.")
    $hero(              "................?")
    $snape("~03", who2, "Half of my... so-called \"pupils\" are nothing but annoying maggots that make my life miserable on a daily basis.")
    $hero(              "................")
    $snape("~07", who2, "Most of them belong to your precious \"Gryffindor\" house of course...")
    $hero(              "......?")
    $snape( "~07", who2,"The wretched Weasley family, that noisy Granger girl, and of course, the hero of all the juvenile delinquents around the wizarding globe....",
            "~08", who2,"The Potter boy!",
            "~01", who2,"Mark my words, Albus. The \"gryffindor house\" will become this school's undoing!")
    $hero(              "......................")

    $snape( "~01", who2,"Nothing but annoying maggots, the lot of them!",
            "~06", who2,"And if that wasn't enough, now they spread all sorts of nasty rumours about the teachers!// Particularly about yours truly...")
    $hero(              "......................")
    $snape("~05", who2,"You don't believe those rumours, do you Albus?")

    menu:
        m ".............."
        "\"Well, of course not!\"":
            $snape( "~09", who2,"Good...// You know me better than that. You know I wouldn't care for such things...")
        "\"Where there's smoke, there's fire.\"":
            $snape( "~10", who2,"Albus?! You can't be serious!?// Those are nothing but filthy lies, I'm telling you!")

    
    $hero(".........................")
    $snape( "~04", who2,"But speaking of them... those wretched kids left me completely exhausted. I think I will retire for today.",
            "~09", who2,"................")
    
    $snape.Visibility("body", False, Dissolve(.5))


    stop music fadeout 1.0
    $screens.HideD3("bld1")
    $snape.chibi.Trans("goout door")
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $snape.chibi.Hide(d4)
    pause.5
    $screens.ShowD3("bld1")

    $hero("Hm...// So that tall, broody dude mistook me for someone else...?// Which means I must be shrouded in a concealment spell...",
            ".........",
            "So basically, I'm a genie disguised as a human, who is in turn disguised as another human...// No, that's not stupid at all...",
        a4, "Shut it! Nobody understands a true genius.", m)

    $ days_without_an_event = 0
    
    $this.event_02.Finalize() # Сюда попадаем из ивента event_02
    jump day_start




###############################################################################################################################################################

label event_01: #First event in the game. Gennie finds himself at the desk.
    $screens.ShowD3("bld1")
    $hero(  m,  "..................?// Your majesty?// .......................................................",
            g4, "I did it again, didn't I?// Teleported myself to who knows where...",
            m,  "What's with those ingredients?// They seem to be way more potent that I thought.// Well, whatever this place is I have no business here...// Лучше обернуть заклинание вспять, иначе принцесса будет снова злиться на меня...//"
                ".....................// Although...// There is something odd about this place... it's...// It's almost brimming with.... // MAGIC?!//"
                " Yes... magic, I can feel it. So powerful and yet somehow...// ...alien.// Interesting...// I think I will stick around for a little bit...")

    $screens.HideD3("bld1")
    $this.event_01.Finalize()
    return
###############################################################################################################################################################
label event_02:
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
    #$ mail_from_her = True #Comented out because replaced with $ letters += 1 
    play sound "sounds/owl.mp3"  #Quiet...
    $screens.ShowD3("owl", "bld1")
    $hero("What? An owl?")
    $screens.HideD3("bld1")
    return
    
###############################################################################################################################################################
label event_03: 
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01 
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    pause.1
    show screen bld1
    with Dissolve(.3)
    m "{size=-3}(That broody guy again...){/size}"
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    with Dissolve(.3)
    who2 "Albus!"
    m "Hey.......... you..."
    who2 "You need to do something about that Granger girl..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Honestly... I'm running out of ways to punish that... that..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "That little witch!"
    menu:
        m "..."
        "\"Granger? Hermione Granger, right?\"":
            who2 "Yes, her..."
            who2 " She also happens to be a part of the \"Potter gang\"."
        "\"I got your back, Jack, witches be crazy!\"":
            who2 "What...? Albus you behave oddly lately."
            who2 "Is everything alright?"
            menu:
                m "..."
                "\"Yes, I'm fine. Go on.\"":
                    who2 "If you say so..."
                "\"You know me. I love my shenanigans.\"":
                    who2 "Hm....."

        "\".....................................................\"":
            pass        
    who2 "Remember how back in the days they used to publicly flog the students?"
    who2 "I swear if we could bring that back all of our problems would be solved..."
    who2 "Yes... I would gladly tie that girl to a flogging pole in front of the entire school..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_20.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Then lift her skirt up, and..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_12.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "*Khem!* Sadly, nowadays we teachers are severely limited in the disciplinary measures we have at our disposal..."
    who2 "I know you are just as powerless as I am in this matter, but I'm telling you, that girl should better stop testing my patience."
    menu:
        m "..."

        "\"I'll take care of that little whore!\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "...?!"
            who2 "Albus..."
            who2 "You are acting strange lately..."
        "\"Nobody ever said this job would be easy.\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Sometimes I feel like I would rather deal with a classroom full of Dementors..."
        "\"You will feel better tomorrow.\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "You are probably right..."
    who2 "Hm..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Perhaps I'd better go get some sleep."
    who2 "I need to be in my top shape every morning..."
    who2 "You can't show weakness to those kids or they will swallow you whole..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Good night, Albus."
    
    
    hide screen snape_main
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f 
    pause 3
    hide screen snape_walk_01_f 
    show screen snape_01_f #Snape stands still. (Mirrored).
    pause.2
    who2 "................."
    who2 "One more thing..."
    show screen bld1
    show screen snape_main
    with Dissolve(.3)
    who2 "You should ignore any lies you hear about me and those slytherin girls..."
    m "Got it."
    hide screen bld1
    hide screen snape_main
    hide screen snape_01_f #Snape stands still. (Mirrored).
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $this.event_03.Finalize()
    jump day_start
###############################################################################################################################################################
label event_04:
    m "Well, it's been three days now..."
    m "I wonder what has become of that two-faced dude?"
    return
###############################################################################################################################################################    
label event_05: #Snape comes in, has a talk with Genie, then the duel starts.
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01 
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    show screen ctc
    with Dissolve(.3)
    who2 "Good evening, Albus."
    who2 "I want to talk to you about those damn kids again..."
    who2 "But first I want to ask you something..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Did you notice anything strange going on around here lately?"
    menu:
        m "..."
        "{size=-2}\"Like you being especially whiny?\"{/size}":
            who2 "What? B-but... Those kids..."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Well, perhaps you are right..."
        "{size=-2}\"That owl is fetching my mail, man!\"{/size}":
            who2 "An owl? What about it?"
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "That's not what I mean..."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Well, never mind..."
#        "\"I Saw a dude with two faces the other day.\"":
#            who2 "?!"
#            who2 "What's that supposed to mean...?"
        "{size=-2}\"No, not really. It's just business as usual.\"{/size}":
            who2 "Hm... Maybe I'm just being paranoid..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "The reason why I'm here today is the \"Potter Gang\""
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "There are only so many points I can subtract from the Gryffindor house, you know..."
    who2 "And the Granger girl became the worst of them lately..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "She practically leads the onslaught."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Speaking of which, has she been sending you any letters lately?"
    menu:
        m "..."
        "\"Hermione Granger? No, Nothing from her.\"":
            who2 "I see... So she's been bluffing then."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "What an annoying young witch."
        "\"Yes... Every damn day...\"":
            who2 "Really now?"
            who2 "Any lies about me in particular?"
            who2 "I hope you know better than to listen to the likes of her..."
    
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "She would never admit it, but I know she's been spreading those nasty rumours about me around the school..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Tsk... Noisy little witch..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "I would never stoop so low as to trade house points in exchange for sexual favours..."
    who2 "I mean, sure, we use house points to motivate students, but that's completely different..."
    who2 "I can't speak for the rest of the staff though..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "The stories I hear about Minerva McGonagall and those poor Gryffindor freshmen may be true..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Well, I just wanted to make sure that you take those rumours about me for what they are..."
    who2 "Nasty lies made up by a bunch of spoiled kids."
    

    who2 "Oh.... Before I go..."
    who2 "There is one thing I meant to ask you for a while now..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "........................."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "What is my name?"
    menu:
        m "..."
        "\"What? What kind of question is that?\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "You are right..."
            who2 "Forgive me... I'm just being paranoid I suppose..."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "But you can never be too cautious with rumours about  \"you know who\" still being alive and all..."
        "\"Tall broody guy?\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Albus, lately you adopted a peculiar sense of humor, that I do not care for in a slightest..."
            who2 "Maybe you should spend a little less time in the company of that big oaf Hagrid."
        "-\{Use magic to get the right answer\}-":
            $ d_flag_01 = True
            hide screen snape_main
            with d3
            show screen blktone
            with d3
            ">You use your phenomenal cosmic powers to peek into the very fabric of the universe and get the correct answer."
            hide screen blktone
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "!!?"
            m "What kind of question is this, Severus?"
            who2 "Forgive me... I'm just being paranoid I suppose..."


    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Well, good night, Albus."
    hide screen snape_main
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f 
    pause 3
    hide screen snape_walk_01_f 
    show screen snape_01_f #Snape stands still. (Mirrored).
    pause.2
    
    
    
    
    stop music fadeout 1.0
    who2 "........................"
    hide screen snape_01_f
    hide screen bld1
    hide screen snape_main
    hide screen snape_02 #Snape stands still. 
    #hide screen genie
    show screen blkfade
    with d3
    $ renpy.play('sounds/07_run.mp3') 
    pause 2
    g4 "???"
    
    show screen snape_defends
    hide screen blkfade
    with d3
    show screen ctc
    
    
    
    play music "music/hitman.mp3" fadein 1 fadeout 1 # TENSE THEME 
    
    
    pause
    hide screen ctc
    show screen bld1
    with d3
    if d_flag_01:
        $sna_head_state = 6
        sna_head_main "Who are you, scum!"
        g4 "What? It's me... uhm... Abius! I mean, Albus!"
        $sna_head_state = 4
        sna_head_main "You cannot fool me."
        sna_head_main "Just now, you used some sort of alien magic!"
        $sna_head_state = 6
        sna_head_main "Reveal your true self to me now, fiend! Who are you?!"
    else:
        $sna_head_state = 1
        sna_head_main "My name is Severus Snape!"
        sna_head_main "Now, who might you be...?"
        
    g4 "!!!"
    sna_head_main "Easy now... Just answer my question."
    
    m "Alright, alright, just calm down, would you?..."
    sna_head_main "........"
    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label no_wait:
    menu:
        m "..."
        "\"I am not your enemy.\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            sna_head_main "That the first thing an enemy would say."
        "\"I'm just a tourist. I'll be leaving now.\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            sna_head_main "You are not going anywhere."
        "\"I work for Albis Doombldore!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            sna_head_main "It's Albus Dumbledore, you moron!"
    if d_points == 2:
        pass
    else:
        jump no_wait

    sna_head_main "Who sent you here? What did you do with the real Albus?"
    sna_head_main "Shed your disguise and reveal your true self at once, this is your last warning!"
    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label no_wait_2:
    menu:
        m "..."

        "\"I can't. It's hard to explain...\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            sna_head_main "I have no interest in your explanations. I wouldn't believe a single word you'd say anyway!"
        "\"Stop threatening me, human!\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            sna_head_main "\"Human\"?"
            sna_head_main "Are you implying that you are {size=+5}not{/size} one?"
            sna_head_main "What are you then?! Dispell your cloaking charm immediately or else!"
        "\"I mean you no harm, I swear!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            sna_head_main "Is that so?"
            sna_head_main "Prove it then. Dispel your cloaking charm now!"

    if d_points == 2:
        pass
    else:
        jump no_wait_2

            
            
    sna_head_main "I've heard enough!"
    g4 "By the great desert sands! Would you let me explain, human?!"
    sna_head_main "There is nothing left to explain!"
    sna_head_main "Since you refuse to cooperate, I'll be taking you into custody by force!"
    g4 "What?! Wait!"
    
    
    # Небольшое дополнение
    translators "You can just skip \"Battle\". Skip?"
    menu:
        "- Skip -":
            $ skip_duel = True 
        "- Start duel -":
            $ skip_duel = False
            stop music 
            $ renpy.play('sounds/glass_break.mp3') #Sound of a door opening.
            play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1
            # $ end_u_1_pic =  "glass"
            # pause.1
            # show screen end_u_1
            hide screen snape_defends
            # pause 3
    jump duel

###############################################################################################################################################################
label event_06: #THE TALK AFTER THE DUEL ENDS.
    $ potions = 0 #Makes sure there are no potions left in the possessions. 
    
    #play music "music/Final Fantasy VII - Victory Fanfare.mp3" fadein 1 fadeout 1 
    stop music fadeout 2.0
    g4 "*Panting*"
    g4 "Ready to talk now?!"
    $sna_head_state = 8
    sna_head_main "(...i-impossible...)"
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    
    hide ch_gen
    show image "03_hp/04_duel/no_magic.png" at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    
    m "I told you you are no match for me..."
    show screen bld1
    with d3
    m "You did give me a good run for my money though..."
    $sna_head_state = 1
    sna_head_main "The way you conjure the spells with your bare hands..."
    sna_head_main "No human could do that... who--"
    $sna_head_state = 4
    sna_head_main "{size=+5}What are you?{/size}"
    $sna_head_state = 1
    sna_head_main "Some sort of shape-shifting demon summoned by \"you know who\"?"
    m "Summoned by whom?"
    $sna_head_state = 2
    sna_head_main "By \"you know who\"!"
    m "What?"
    $sna_head_state = 7
    sna_head_main "......................"
    m "............................"
    m "Listen, I'm not a demon..."
    m "And I sure as heck don't work for \"I don't know who\"!"
    $sna_head_state = 1
    sna_head_main "............................."
    m "I've been ehm..."
    m "...Conducting an experiment back in my world, during which something went wrong and I ended up here."
    m "That's all..."
    sna_head_main ".........................."
    sna_head_main "What became of to the real Albus Dumbledore then?"
    m "I'm sure he is fine."
    m "He's Probably feeling as surprised about finding himself in my world as I am about finding myself here..."
    sna_head_main "...................................."
    sna_head_main "When did this happen?"
    m "Four days ago..."
    sna_head_main "Can you go back?"
    m "I think so..."
    $sna_head_state = 2
    sna_head_main "Why didn't you then?"
    m "Not sure..."
    m "The Magic of this world is so bizarre... Perhaps I just got curious."
    $sna_head_state = 1
    sna_head_main "..................."
    sna_head_main "You need to fix this..."
    m "Fix what?"
    $sna_head_state = 4
    sna_head_main "Everything. You need to bring back Albus and leave our world."
    menu:
        m "..."

        "\"Yes, yes, I know. Off I go then.\"":
            m "Yes, yes, I know..."
            m "Well, off I go then. Sorry for the ruckus."
            $sna_head_state = 1
            sna_head_main "No harm done..."
        "\"But I like it here! Can't I stay?\"":
             sna_head_main "Absolutely not."
             sna_head_main "Whoever you are, you are not from this plane of existence."
             sna_head_main "Your very presence here upsets the natural order of things."
             sna_head_main "And these days this school needs a proper headmaster more than ever."
    sna_head_main "Have a save trip home now."
    m "Ehm... Thank you, mr. Severus. Good luck with your students and the \"potter gang\"."
    sna_head_main "\"The potter gang\"?"
    $sna_head_state = 7
    sna_head_main "Oh, right, those buggers..."
    menu:
        "-Undo the spell-":
            pass
    menu:
        "-Undo the spell-":
            pass
    menu:
        "-Undo the spell-":
            pass

    $sna_head_state = 1
    sna_head_main "Did it work? Albus, is that really you?"
    menu:
        m "..."
        "\"Yeah, that's me. So good to be back!\"":
            sna_head_main "Glad to have you back, old friend. Are you alright?"
            m "I'm fine, Severus, thank you."
            sna_head_main "How was it, in that other world?"
            m "A lot of sand and very hot, but other than that quite pleasant."
            sna_head_main "I see... Did you miss your brother?"
            menu:
                m "..."
                "\"Yes, I missed you so much!\"":
                    sna_head_main "......................."
                    sna_head_main "Yeah, right...."
                "\"I don't have a brother, Severus.\"":
                     sna_head_main "........................"
                     sna_head_main "You may not have one, but the real Albus Dumbledore does."
                "-Use magic to get the right answer-":
                    show screen bld1
                    with d3
                    ">You use your phenomenal cosmic powers to peek into the very fabric of the universe and get the correct answer."
                    hide screen bld1
                    with d3
                    m "My little brother Aberforth? Why would I miss him?"
                    sna_head_main "I can feel it whenever you use your alien magic..."
        "\"Nope. It's still me. The non-human guy.\"":
            pass


    sna_head_main "Why are you still here, creature?"
    m "I'm not sure... I tried to undo the spell but nothing happened..."


    $sna_head_state = 7
    sna_head_main "Marvelous..."
    $sna_head_state = 1
    sna_head_main "What does this mean? So You're staying here for good?"
    m "Of course not..."
    m "Me being here at all is only possible because the spell is compensating for the unbalance caused by itself..."
    m "said spell will wear off eventually and I shall be pulled back into my world."
    m "Likewise, your Dumbledore-friend shall be pulled back here."
    sna_head_main "I see..."
    sna_head_main "How long until the spell wears off?"
    menu:
        m "..."
        "\"A couple of days.\"":
            sna_head_main "I see..."
        "\"A week or so...\"":
            sna_head_main "Hm.... A week, huh..."
        "\"Could be months...\"":
             sna_head_main "That long?"
             sna_head_main "Now isn't that just \"perfect\"?"
        "\"I have no clue...\"":
            sna_head_main "....................."
            $sna_head_state = 2
            sna_head_main "Splendid..."

    m "Alright, to be honest I'm not sure where to go from here..."
    m "All this time I thought I could undo the spell whenever I want to..."
    $sna_head_state = 1
    sna_head_main "..................................................."
    sna_head_main ".................................."
    sna_head_main "..................."
    m "Snape?"
    sna_head_main "..................................................."
    m "Severus?"
    $sna_head_state = 6
    sna_head_main "Yes, yes..."
    $sna_head_state = 1
    sna_head_main "Listen, it's very late, and too much happened already..."
    $sna_head_state = 7
    sna_head_main "I need to process all of this."
    $sna_head_state = 1
    sna_head_main "I will come to see you tomorrow, after my classes."
    $sna_head_state = 6
    sna_head_main "Until then, keep your true identity and our conversation a secret, alright?"
    m "Not a problem."
    $sna_head_state = 1
    sna_head_main "Alright then..."
    sna_head_main "But before I go, I have one more question..."
    m "I'm listening..."
    $sna_head_state = 2
    sna_head_main "........"
    $sna_head_state = 1
    sna_head_main "If you are not a human, then..."
    $sna_head_state = 7
    sna_head_main "What are you?"
    m "...I'm a genie."
    $sna_head_state = 1
    sna_head_main "A genie?"
    m "Yes, I possess phenomenal cosmic powers and all that..."
    sna_head_main "Seriously?"
    m "Oh, yes."
    sna_head_main "Unbelievable..."
    sna_head_main "Well, I'll see you tomorrow.... genie."
    m "I'll be here..."

    $sna_head_state = 7
    sna_head_main "(A genie? Now that's new...)"
    $this.event_05.Finalize()
    jump day_start
###############################################################################################################################################################        
label event_07: #THE TALK WITH SNAPE THE DAY AFTER THE DUEL.
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01 
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    show screen ctc
    with Dissolve(.3)
    sna "..................."
    hide screen snape_main
    with d3
    m "Good evening..."
    show screen snape_main
    with d3
    sna "Is the spell still in effect?"
    hide screen snape_main
    with d3
    m "Yes. very much so."
    show screen snape_main
    with d3

    sna "I see..."
    sna "Last night I gave our little.... conundrum some thought."
    sna "And I think I came up with a solution..."
    m "Really? Great! I'm listening."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ tt_xpos=300 #Defines position of the Snape's full length sprite. Right - 300  # 120 - center.          #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Let's just roll with it..."
    m "Excuse me?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Well what else could we do?"
    sna "Normally I would alert the ministry of magic and let them take care of this mess..."
    sna "But I'd rather avoid any dealings with those rotten bureaucrats this time..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Also, losing a headmaster, even temporarily could hurt the school's reputation..."
    sna "And what if your spell wears out tomorrow, or even tonight?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "I see no reason to start a commotion..."
    m "Hm..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "So we shall keep the charade going for now..."

    m "By doing what exactly?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Just act like Albus always does: never leave this tower and try to avoid any human contact..." 
    m "That...."
    m "Sounds..."
    g4 "Incredibly boring!"
    g4 "What am I supposed to do here?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "You are a Genie. Conjure up some sort of entertainment for yourself."
    m "My magic does not working properly here for some reason..."
    m "And my lamp is literally worlds away..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Well, what do you expect me to about that?"
    sna "Send you a couple of girls from Slytherin maybe?"
    g9 "No idea what \"Slytherin\" is but I think that would work..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "That was a joke, obviously."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Although..."
    sna "Hm..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Well, in any case I don't see how entertaining {size=+7}you{/size} is {size=+7}my{/size} problem."
    m "Oh, but it is!"
    m "I'm immortal and all-powerful..."
    m "Being bored is like the worst thing that could happen to me!"
    g4 "And I have a thing against being cooped up in small spaces with nothing to do!"
    g4 "I may lose my mind..."
    g4 "Oh! Ah! I think it's happening already!"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "......."
    g4 "I'm losing my mind! It's getting hard to breathe!"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "...."
    g4 "It's so dark..."
    g4 "Are you still here?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "..."
    m "........."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Are you done?"
    m "Yes..."
    m "Seriously though, I don't see how this whole affair benefits me at all."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Do you have any choice?"
    m "I do..."
    m "Instead of sitting here on my ass all day and being quiet I could explore your world..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Hm..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Well, alright, what do you want?" 
    m "Teach me your magic..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "My magic?"
    m "Yes... The way you conjure up your spells is..."
    m "Intriguing..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Hm..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "So be it..."
    m "Oh, and send me some of those \"Slytherin\" girls as well.."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "..............."
    sna "........................."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ha-ha-ha!!!"
    m "What? What did I say?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "A-ha-ha-ha-ha..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "No, no, my apologies..."
    sna "It's just that to me you still look and sound like Albus..."
    sna "To hear Professor Dumbledore say things like \"Send me those girls up\"..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "It's hysterical... "
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "But you would't understand..."
    m "Heh..."
    g9 "Send those whores up, Severus. I'm feeling lonely tonight."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ha-ha-ha! Stop it, you're killing me!"
    sna "A-Ha-ha-ha!"
    m "No, I'm serious... Is it possible?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Hm..."
    sna "We'll see..."
    sna "You being our new headmaster sure presents me with interesting possibilities..."
    sna "I need some time to figure out how to use our situation for my advantage."
    m "You mean {size=+7}our{/size} advantage, right?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Oh, yes, yes, of course..."
    sna "Well, I think we are done for today..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Good night... genie."
    m "Yes, good night, Severus."

    hide screen snape_main
    hide screen ctc
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f 
    pause 3
    hide screen snape_walk_01_f 
    show screen snape_01_f #Snape stands still. (Mirrored).
    pause.2
    
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "................."
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "\"Send those whores up, Severus!\" Ha-ha-ha..."
    hide screen s_head2  
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_01_f #Snape stands still. (Mirrored).
    with d3
    m "Hm... "
    m "I Suppose I'll just curl up in a ball on top of this desk as usual..."
    pause.2
    show screen notes
    $ renpy.play('sounds/win2.mp3') 
    show screen blktone
    with d3
    ">You've unlocked the ability to summon Severus Snape to your office."
    hide screen blktone
    with d3
#    $ hanging_with_snape = True
    $this.event_07.Finalize()
    jump day_start

###############################################################################################################################################################
label event_08: # HERMONE SHOWS UP FOR THE FIRST TIME. IN USE.
    #"EVENT_08"
    stop music fadeout 1.0
    pause 1
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock*"
    $hero("Huh?")
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock*"
    pause.7

    $hero("Somebody is knocking on the door...// Crap... I'm supposed to avoid any human contact!// Hm... What are the chances that the thing knocking on my door is not human?// Yeah, quite slim...")
    m "Hm... What are the chances that the thing knocking on my door is not human?"
    m "Yeah, quite slim..."
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock*"

    $hero("Persistent little bastard...")
    $ d_flag_01 = False #When False Genie doesn't know Hermione's name.
    $ d_flag_02 = False #When TRUE Genie knows it's a girl knocking on the door.
    $hermi.Visibility()
    menu:
        m "..."
        "\"Who is it?\"":
            $ d_flag_01 = True
            $hermi(who, "It's me, professor...// Hermione Granger. Can I come in?")
            $hero("#(It's that wretched woman who's been harassing me with her letters lately...)")
            $hermi(her)
            menu: 
                m "..."
                "\"Go away, please. I'm busy.\"":
                    jump event_08_saygoout
                "\"Yes, yes, you can come in.\"":
                    pass          
        "\"Come in!\"":
            pass
        "\"Go away!\"":
            label event_08_saygoout:
            $ d_flag_02 = True #When TRUE Genie knows it's a girl knocking on the door.
            $hermi(who, "But, professor, I really need to talk to you...")
            $hero("...........................................")
            $hermi("Professor? I'm coming in")
            $hero("#(Crap...)")
        "\"................\"":
            $hermi(who, "Professor, are you there?")
            $hero("#(Go away...)")
            jump event_08_saygoout


    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

# Нельзя комментировать, переменные должны быть инициированы, используются в старом коде
    $ hermione_chibi_xpos = 610  
    $ hermione_chibi_ypos = 250
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ pos = POS_370  # Присвоение не комментировать, будет использовать дальше в старом коде
                        #    $herView.showQ( "body_01.png", pos )
                        #    $herView.hideQ( )
    $ posHead = gMakePos( 390, 235 )

    $hermi.chibi.State("door", speed="go").Trans(Dissolve(.5), "blink")
    

    pause.3
    if not d_flag_01:
        m "?!!"
    if not d_flag_02: #When TRUE Genie knows it's a girl knocking on the door.
        m "{size=-3}(A girl?){/size}"
        
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1

    $hermi.chibi.Trans("go center", "blink")
    pause.5
    $screens.ShowD3("bld1" )

    $hermi.Visibility("body+", transition=d3)

    $screens.ShowD3("ctc").Pause()
    $hermi("Good morning professor.","~body_03.png")
    $screens.HideD3("ctc")
    menu:
        "\"Good morning... girl.\"":
            $hermi("#(\"Girl\"?)")
        "\"Good morning, Hermione.\"" if d_flag_01:
            pass
        "\"Good morning, Child.\"":
            $hermi("#(\"Child\"?)")
        "\"................................\"":
            pass
    $hermi(                 "I am very busy with my class schedule, but I kept my morning free today so that I could see you, professor.",
                            "You probably know why I am here too.",
            "~body_04.png", "The issue I have been fruitlessly trying to bring to your attention lately...",
                            "I cannot understand why you are not acting to stop that nonsense, professor!",
            "~body_02.png", "The inequality is starting to affect all of the houses...",
                            "Simply because we have more integrity than the rest...",
                            "Do you think it's fair that the people who deserve to be in the lead are being pushed back instead?",
                            "Do you think that's fair, professor? Do you?", 
            "~body_03.png")

    $hero("#(Would you look at that pretty, little thing?)// #(Look at her going on and on about something... She's adorable!)// #(Damn, I haven't seen a woman in weeks!)")

    menu:
        "\"(I will jerk off a little while she talks.)\"":
            $ jerk_off_session = True #Affects next conversation with Snape.
            $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
        "\"(No, that's stupid! I Need to behave!)\"":
            $ d_flag_01 = False #NOT JERKING OFF.
            pass
    if d_flag_01:
        $hermi.Visibility()
        $screens.HideD3("bld1").ShowD3( "blktone8" )
        ">You reach under the desk and grab your cock..."
        $screens.HideD3( "blktone8", None, "genie" ).ShowD3( "genie_jerking_off")

    $hero("Yes, keep on going, dear.")
    $screens.ShowD3( "bld1" )

    $hermi.Visibility("body+")("~body_05.png",  "\"Yes\"?! So you think it's fair?")
    $hero(                  "Oh, of course not, I meant \"no\". But Keep on going anyway...")
    $hermi("~body_03.png",  "That's a relief. I'm glad that you agree with me, professor...",
           "~body_04.png",  "As I was saying, the whole issue is simply ridiculous and I cannot believe that it is taking place in our day and age!")

    if d_flag_01:
        $hermi.Visibility()
        $screens.HideD3("bld1").ShowD3( "blktone8").Say(">*Fap!* *Fap!* *Fap!*// >You keep on stroking you cock...").HideD3( "blktone8").ShowD3( "bld1")
        $hermi.Visibility("body+")
    else:
        m "I see..."

    $hermi("I mean, I would understand if something like this were to occur during the middle ages...// But we left the middle ages behind a long time ago, did we not?")

    if d_flag_01:
        $hero(g9, "#(Would you look at those rosy cheeks? I want to poke'em with my cock.)",m)
        $hermi.Visibility()
        $screens.ShowD3( "blktone8").Say(">You continue stroke your cock...").HideD3( "blktone8")
        $hermi.Visibility("body+")
    else:
        $hero("Ehm... I suppose you did. I mean, we did.")

    $hermi("So it hurts the whole house-point-distribution system.// It hurts our entire educational system as well// And more importantly the motivation among students is steadily decreasing due to it!!")

    if d_flag_01:
        $hero(  "#(Look at those huge knockers on you, girl!)// #(Yes... I want to squeeze my dick between them...)")

    $hermi("As you can see the situation is dire...// ~body_02.png// But we can still set everything right...// As the representative of our school's Student Representative Body...// I have a few suggestions on how to do that more efficiently.")


    if not d_flag_01:
        $hero ("..............")

    $hermi("First of all the house point system needs to be reinforced!// ~body_03.png// You need to control the point distribution better, sir.")        
    if d_flag_01:
        $hero (g4, "#(Yes, you are a whore... A nasty little whore... I bet you love to suck cocks... Don't you? Yes, I bet you do...)")
        $hermi.Visibility()
        $screens.Show(d4, "blktone8").Say(">You stroke you diamond-hard cock ferociously!").Hide(d4, "blktone8")
        $hermi.Visibility("body+")
    $hermi("Of course you agree with me on this, professor, do you not?")
    if d_flag_01:
        $hero(g4,               "{size=-4}*Panting heavily*{/size}")
        $hermi("~body_07.png// Professor...?")
        $hero("#(Crap. What does she want now?)// Yes, it's all true. Please keep going...")
        $hermi(                 "Ehm... So, as I was saying...")
        $hermi.Visibility()
        $hero(m,"#(Oh... That was a good jerkoff session, but I'm getting dangerously close to the \"grand finale\".)// #(Maybe I should stop before I get myself into trouble?)")
        menu:
            "\"(Yes, time to actually listen to her.)\"":
                $screens.ShowD3("genie")
                $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
            "\"(No! I want to keep on jerking off!)\"":
                pass
        $hermi.Visibility("body+")
    else:
        $hero("#(Do I? I honestly don't give a damn...)// Uhm... I suppose I do...")
        $hermi("#(Suppose?)// #(When did Professor Dumbledore become so... apathetic?...)")

    $hermi("~body_04.png// Another measure you could take in consideration is tightening the control over your staff...// Especially the teachers...",
           "~body_03.png// I hope I'm not stepping out of line here, sir, but some of the teachers really do require supervision...")

    if d_flag_01:
        $hero(g4,            "{size=-4}(Yes! You little whore! You fucking little whore!) *Panting*{/size}")
    else:
        $hero(m,            ".......................")
    $hermi("~body_04.png",  "I understand that you may not have time for this, professor, After all you are the headmaster of our school and a very busy and important man.",
                            "Being a top student is hard on me as well sometimes...")

    if d_flag_01:
#        translators "{size=-4}(Здесь была игра слов \"hard on(тяжело)\" и \"hard-on(стояк)\") которую мы не смогли перевести. \nПростите нас :({/size}"
        $hero(g4, "{size=-4}(She said \"hard-on\"!?) *задыхаясь*{/size}")
    $hermi("But you could delegate that task to me...// Just put your faith in me professor!" )

    if d_flag_01: 
        $hermi("~body_01.png", "Yes, you can do it! Just put it in me, sir!")

        stop music fadeout 1.0
        $screens.ShowHide("white", 0.1).Pause(0.2).Show("white").Pause(0.1).Hide(hpunch,"white")

        $hero(g4, "{size=-4}(Oh crap, that did it!) *Argh!*{/size}")
        $hermi.Visibility()

        $screens.HideD3("bld1").ShowD3("genie_jerking_sperm").Pause(3.0).ShowD3("bld1")

        $hermi.Visibility("body+")("~body_18.png", "Professor?! What is going on...?")
        $screens.ShowD3("genie_jerking_sperm_02")
        $hero(g4, "Ah... YESSSSS.....!")
        $hermi("???")
        $hero(g4, "*Breathing heavily* Yes! yes....")
        $screens.ShowD3("genie")
        $hero(g4, "Yes, girl. It's all exactly as you say and I will.... take care of it all.", m)
    else:
        $hero(m,       "Alright... I will think about your proposal, I promise.")   

    $hermi("~body_07.png// Really?// Hm...........")

    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    $hermi("~body_04.png",  "That's a relief! Thank you, professor.")

    if d_flag_01:
        $hero("No, no, thank you...")
        $hermi("~body_07.png// Hm...")

    $hermi("~body_04.png// My classes are about to start so I'd better go now.// Thank you for your time...")

    $screens.HideD3("bld1")
    $hermi.Visibility(transition=d3)
    $hermi.chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    if d_flag_01:
        $hero("#(This was awesome...) *Panting*// #(My pants are ruined though...)")  
    else: 
        $hero(".................// #(She is cute, but quite a piece of work...)")

    $screens.HideD3("bld1").HideD3("genie_jerking_sperm_02")

    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    $this.event_08.Finalize()
    return

### FOLLOWING EVENT IS NOT IN USE ANYMORE ###
###############################################################################################################################################################    
label event_08_02:
#    "EVENT_08_02"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    menu:
        "\"Who is it?\"":
            $hermi("It's me, Hermione Granger.")
            $hero("#(It's that young witch again...)")
            jump event_08_02_inmenu
        "\"Yes, come in...\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Knock-knock-knock!*"
#            m "............................."
            label event_08_02_inmenu:
            $hermi("Professor, I'm coming in...")
            $hero("#(Crap!)")
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $hermi.chibi.State("door", speed="go").Trans(d4, "go center", "blink")
    pause.5
    $screens.ShowD3("bld1")

    $hermi("~body_01.png").Visibility("body+", transition=d3)("Good morning, professor Dumbledore.")
    menu:
        "\"Good morning, miss Granger.\"":
            pass
        "\"Good morning, child.\"":
            $hermi("~body_07.png// #(\"Child\"? Must you be so condescending all the time?)")
            $hero("What was that?")
            $hermi("~body_202.png// It's nothing sir...")
        "\"Good morning, whore.\"":
            $hermi("~body_18.png// Em... What?")
            $hero(g4, "#OK, that was stupid. Damage control, damage control!.",
                    m, "*Khem* Excuse me, something stuck in my throat... Good morning, miss Granger.")
            $hermi("~body_202.png// #(Did he just called me a.... no, no way.)")
            
    $hermi("~body_02.png// Professor Dumbledore, I am here to talk to you as the \"MRM\" president...")
    $hero(".............")
    $hermi("We held an emergency assembly yesterday...// The matter in question was the \"Hogwarts\" uniform for girls...//"
        " We came to the conclusion that the currently employed dress-code is highly inappropriate for an educational institution...")

    $screens.Show("ctc").Pause()

    $hermi("...")
    $hero("Seriously?")

    $screens.Hide("ctc")

    $hermi("~body_04.png//Yes, professor, I assure you, we are very serious.// The way you force our poor girls to dress is unacceptable  ...//"
        "Such frivolous attire distracts male students from studying, putting them at a disadvantage...// ~body_07.png// All those distractions they have to deal with...// The poor souls...")
    $hero("Did any of the boys actually complain about this?")
    $hermi("~body_04.png//We won't wait for the issue to manifest, sir! We'll prevent it!!//"
        "~body_07.png//No individual shall be at a disadvantage based on his or her gender.// This is what they call \"Sexism\" in the muggle world, sir.")
    $hero("Your explanations are getting way too convoluted for my liking, miss Granger.// Tell me what you are proposing exactly, to Put every woman in the school in a burqa?")
    $hermi("~body_207.png//Officially doubling the length of the girls' skirts in the school regulations would suffice...")

    menu:

        "{size=-4}\"That is laughable. Request refused!\"{/size}":
            $ d_flag_05 = True #Notion refused. Will take affect in the next event.
            $hermi("~body_05.png//What... B-but? We made a decision...")
            $hero("Miss Granger, I'm sorry to break this to you, but I am still the headmaster of this school...// And the only decisions that matter are mine!")
            $hermi("~body_07.png//So you ignore the voice of the people, sir?")
            $hero("The only voice I hear is yours, miss Granger.")
            $hermi("~body_05.png//Don't You know what happens to tyrants who underestimate the power of the masses?// They get overthrown!")
            $hero("Careful, now. Your words smell of treason, young lady.// Don't You know what happens to traitors?// The get hung!")
            $hermi("~body_47.png//!!!// Tsk!// I will make you take me seriously, professor!")
        
        "{size=-4}\"Boys must study in peace. request approved!\"{/size}":
            $hermi("~body_01.png//Splendid. I will everyone know.// Thank you professor.")
          
    $screens.HideD3("bld1")
    $hermi.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    $hero("...................................// I'm Starting to enjoy our meetings less and less...")

    $this.event_08_02.Finalize()
    return
#NOT IN USE###############################################################################################################################################################    
label event_08_03:
#    "EVENT_08_03"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    $hero("Who is...")
    $hermi("Professor, I'm coming in...")

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $hermi.chibi.State("door", speed="go").Trans(d4, "go center", "blink")
    pause.5
    $screens.ShowD3("bld1")

    $hermi("~body_01.png").Visibility("body+")("Good morning, professor Dumbledore.")

    menu:
        "\"Good morning, miss Granger.\"":
            pass
        "\"Good morning, child.\"":
            $hermi("~body_07.png// (\"Child\"? Must you be so condescending all the time? Nasty old prick!)")
            $hero("What was that?")
            $hermi("~body_202.png// Nothing sir....")
        "\"Good morning, miss president.\"":
            $hermi("~body_202.png// #(Is he being sarcastic?...)")
            
    if not d_flag_05:
        $hermi("~body_07.png// You promised me to take action, professor...// But nothing changed since our last conversation...")

        menu:
            "\"I lied...\"":
                $hermi("~body_203.png// B-but...// But you are the headmaster, sir. You word should mean something...")
            "\"I forgot\"":
                $hermi("~body_05.png// You forgot, sir?// Did you really?// Or Maybe you just didn't care enough to remember?")
            "\"I just don't care.\"":
                $hermi("~body_203.png// B-but....?// Professor Dumbledore, this is a serious matter!")

    else:
         $hermi("~body_07.png// Professor Dumbledore, you rejected the offer I made you last time we met...// And now we reap the results...")

    $hermi("The boys are still having a hard time concentrating on their studies...")
    $hero("Oh, I do have a cure for that!// Lets put a paper bag over every girl's head!")
    $hermi("That would be mistreatment of a human being based on her gender...// Another example of sexism...// Or better yet \"Misogyny\".")
    $hero("\"Misogyny\" is a general dislike towards women, miss Granger.// A healthy male is biologically incapable of disliking all the females of his kind...// Otherwise humanity would've gone extinct a long time ago already...")
    $hermi("~body_202.png// Professor, we have no time for semantics.// The entire school is in peril!")
    $hero("Is it...?")
    $hermi("~body_04.png// The \"MRM\" had another meeting yesterday, and--")
    $hero("No, not again...// Are there are any male members in your little \"Men's rights movement\"?")
    $hermi("~body_50.png// That is beside the point.")
    $hero("Right...")
    $hermi("~body_191.png// That is irrelevant...")
    $hero("How is it irrelavant? That's the only thing that {size=+7}IS{/size} relevant!")
    $hermi("~body_206.png// Let me finish my sentence, please.// I am officially addressing you as the \"MRM\" president now...// And as a representative of this school's student body ...//"
        "We demand these new regulations to be enforced...// ~body_120.png// Number one...// No teacher is allowed to raise a voice towards a student or call the said student an unflattering name...")
    $hero("What?")
    $hermi("Number two...// All the school ghosts have to be confined to the abandoned tower in the north wing of the school.")
    $hero("You have school ghosts? That's pretty cool!")
    $hermi("Number three...// ~body_186.png// Every teacher, and especially Professor Severus Snape need to take a qualification test every three months...")
    $hero("Is that all?")
    $hermi("That is all, sir.")

    menu:
        m "..."
        "\"Fine. Your demands shall be satisfied.\"":
            $hermi("~body_03.png// Thank you, professor.// I, as a representative of the student's will, thank you for your cooperation.")
        "\"Sounds like bullshit. You're dismissed\"":
            $hermi("~body_47.png// What? I...// But this is... you can't...")
            $hero("Dismissed!")
            $hermi("~body_51.png// Tsk!")

    $screens.HideD3("bld1")
    $hermi.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    $hero("....................")

    $this.event_08_03.Finalize()
    return

            
            
            
##################################################################################################################
label event_09: #Second visit from Hermione. Says she sent a letter to the Minestry. 
                #Takes place after first special event with Snape, where he just complains about Hermione.
    
    #"EVENT_09"
    stop music fadeout 3.0
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger." 
            m "(It's that young witch again...)" 
            her "Can I come in, sir?"
            menu:
                m "..."
                "\"Absolutely not! I'm busy! Come back later!\"":
                    her "But..."
                    her "Alright... I will come back tomorrow then..."
                    $event.NotFinished()
                    return 
                "\"Of course. Come on in.\"":
                    pass
        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well alright..."
            $event.NotFinished()
            return 
        "\"Yes, come in.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"

    $ event09 = True #You let Hermione in. This event will stop looping now.
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
    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    
    $ pos = POS_370
    $herView.showQ( "body_03.png", pos )
    show screen hermione_02
    with Dissolve(.3)
    show screen ctc
    pause
    $herView.hideshowQQ( "body_04.png", pos )

    her "Good morning, professor Dumbledore."
    hide screen ctc
    menu:

        "\"Good morning, child.\"":
            $herView.hideshowQQ( "body_09.png", pos )
            her "{size=-4}(Again with the \"child\"...){/size}"
            $herView.hideshowQQ( "body_04.png", pos )
            her "Sir, I would appreciate it if you would treat me as an equal..."
            m "{size=-4}(I'm literally millions of years older than you, witch. We are anything but equal.){/size}"
            m "...................."
            $herView.hideshowQQ( "body_09.png", pos )
            her "................"
        "\"Good morning, miss Granger.\"":
            her "Ehm... so, about the reason of me being here today then..."
        "\"Yeah, yeah, whatever...\"":
            pass
    
    her "I see that no matter what I do I simply cannot get through to you, sir."
    $herView.hideshowQQ( "body_04.png", pos )
    her "So in light of your negligence towards your duties I decided to take the initiative myself!"
    m "Did you now...?"
    her "Yes! We, the proud students of Hogwarts, detest sexism..."
    her "No individual shall be treated differently based on his or her gender."
    m "But--"
    $herView.hideshowQQ( "body_05.png", pos )
    her "Please, let me finish, professor!"
    $herView.hideshowQQ( "body_04.png", pos )
    her "I'm organizing the \"Men's rights movements\" in our school!"
    g4 "Oh, boy, this is just so typical!"
    g4 "Blame everything on--"
    stop music fadeout 1.0
    m "Wait, did you say {size=+5}MEN'S{/size} rights movement?"
    $herView.hideshowQQ( "body_11.png", pos )
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    her "You have no idea how hard it is to be a boy in our school these days..."
    menu:
        "\"Didn't see this one coming...\"":
            $herView.hideshowQQ( "body_04.png", pos )
            her "No, you did not, because you, as an authority figure, refuse to listen to us, sir!"
            her "But we will make you hear us..."
        "{size=-3}\"That's literally the dumbest idea I've ever heard.\"{/size}":
            $herView.hideshowQQ( "body_07.png", pos )
            her "I knew you would say something like that..."

    $herView.hideshowQQ( "body_09.png", pos )
    her "Did you know that some of the girls in this school are now selling favours for house points...?"
    her "Sometimes even for good grades..."
    m "Really?"
    $herView.hideshowQQ( "body_04.png", pos )
    her "Nobody from the \"Gryffindor\" house of course..."
    her "And that's what puts us at a disadvantage - our integrity!"
    her "As for the boys - they have to work ten times harder than the girls simply to pass a test..."
    her "Or, if they are lucky enough, to get one meagre house-point..."
    $herView.hideshowQQ( "body_02.png", pos )
    her "This is sexism in its purest form!"
    menu:
        m "..."
        "\"What you want me to do?\"":
            $herView.hideshowQQ( "body_03.png", pos )
            her "Nothing!"
            m "Great. I'm good at that."
        "\"I'm Not sure what to say...\"":
            $herView.hideshowQQ( "body_03.png", pos )
            her "You do not need to say anything anymore, professor."
        "\"You are being ridiculous!\"":
            $herView.hideshowQQ( "body_07.png", pos )
            her "Am I? Well, we'll see..."

    $herView.hideshowQQ( "body_04.png", pos )
    her "I already sent a letter to the ministry of magic."
    with hpunch
    g4 "{size=+7}You did what?!{/size}"
    m "{size=-4}(Wait, do I really give a damn about that?){/size}"
    her "I'm sorry, but you left me no choice, professor."

    her "Now, if you excuse me I must get to my classes..."
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "...................."
    

#    $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
#    $ snape_against_hermione_02 = True #Turns True after event_09. Activates second event when hanging out with Snape.
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    $this.event_09.Finalize()
    return






            
            
            
            
            
            
            
            
            
            
            
            

#NOT IN USE###############################################################################################################################################################
label event_09_2: #Takes place after second special event with Snape, where he just complains about Hermione.
    "EVENT_09"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger." 
            m "(It's that young witch again...)" 
            her "Can I come in, sir?"
            menu:
                m "..."
                "\"Absolutely not! I'm busy! Come back later!\"":
                    her "But..."
                    her "Alright... I'll come back tomorrow then..."
                    return
                "\"Of course. Come on in.\"":
                    pass
        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well alright..."
            return
        "\"Yes, come in.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"

    $ event09 = True #You let Hermione in. This event will stop looping now.
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
    her "Good morning, professor Dumbledore."
    menu:
        "\"Good morning, miss Granger.\"":
            pass
        "\"Good morning, child.\"":
            her "{size=-5}(\"Child\"? Must you be so condescending all the time? Nasty old prick!){/size}"
            m "What was that?"
            her "nothing sir..."
        "\"...............\"":
            her "...................."
            
            
    her "My classes are about to start so I don't have much time..."
    her "Being a top student is not easy, so I hope you understand that the Other kids in our school are looking up to me."
    m "{size=-4}(Is that so...?){/size}"
    her "I realize that you are a important very person as well..."
    her "But do you think you could spare a little of your time to actually perform your duties as the headmaster of this school?"
    menu:
        "\"Excuse me?\"":
            her "Yes, I refuse to sugarcoat this any longer!"
        "\"...................\"":
            pass
    her "I brought so many problems this school has to your attention..."
    her "And you, sir, ignored every single one of them!"
    her "Did you know that some of the girls from \"Slytherin\" offer sexual favours in exchange for house points?"
    m "Do they?"
    her "What message does it send to the rest of the houses?"
    her "Students don't have to work hard anymore, don't have to study, all they need to do is show a little skin..."
    her "This is deplorable!"
    her "I'm warning, professor..."
    menu:
        "\" You are \"Warning me\" miss Granger?\"":
            her "Yes, professor. I am warning you."
            her "If you are not willing to listen to me, I will find someone who will!"
        "\"..............................................................\"":
            pass
    her "If you will not take action soon you will be leaving me no choice, professor..."
    her "I will have to contact the ministry of magic..."
    m "{size=-4}(The ministry of magic? Should I care?){/size}"
    menu:

        "\"Calm down, miss Granger, please.\"":
            her "I cannot stay calm in the face of your ignorance, sir!"
        "\"I hear you. I will take action, I promise.\"":
            her "Really? Well I am glad we finally came to an understanding, sir."
            her "Or are you just going to ignore my pleas as usual?"
        "\"Out of my office, girl! Out, I said!!!\"":
            her "What?"
            m "Get out of my office!"
            her "B-but..."
            with hpunch
            g4 "{size=+7}OUT I SAID!!!{/size}"
            her "{size=-6}(Wow... Never seen old man lose it like that...){/size}"
            her "{size=-6}(I'd better leave before he has a hart attack or something...){/size}"
            her "..............."
            jump pissed_me_off

    her "Oh... I am already late for my classes. I must go now."
    m "You have a nice day... {size=-5}witch!{/size}"
    her "Thank you, professor."
    label pissed_me_off:
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "...................."
    
#    $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
#    $ snape_against_hermione_02 = True #Turns True after event_09. Activates second event when hanging out with Snape.
    return

   



#NOT IN USE###############################################################################################################################################################
label event_10: #Takes place after second special even with Snape where Ginie is worried that Hermione is still in power.
    #Hermione says that she sent the letter to the Ministry of Magic."
    "EVENT_10"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger." 
            m "(It's that young witch again...)" 
            her "Can I come in, sir?"
            menu:
                m "..."
                "\"Absolutely not! I'm busy! Come by later!\"":
                    her "But..."
                    her "Alright... I will come back tomorrow then..."
                    return
                "\"Of course. Come on in.\"":
                    pass
        "\"I'm busy. Come by later.\"":
            her "But..."
            her "Well alright..."
            return
        "\"Yes, come in.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"

    $ event10 = True #You let Hermione in. This event will stop looping now.
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
    her "Good morning, Professor Dumbledore."
    menu:
        "\"Good morning, child.\"":
            her "{size=-4}(Again with the \"child\"...){/size}"
            her "Sir, I would appreciate it if you could treat me as an equal..."
            m "{size=-4}(I'm literally millions years older then you, witch. We are anything but equal.){/size}"
        "\"Good morning, miss Granger.\"":
            her "Em... so, to the reason of me being here today then..."
        "\"Yeah, yeah, whatever...\"":
            her "Em..."
    her "I see that no matter what I do I simply cannot get through to you, sir."
    her "So in light of your negligence towards your duties as a headmaster of this school..."
    her "I decided to take initiative in my own hands!"
#    m "Did you now...?"
#    her "Yes! And since I detest sexism..."
#    m "You do, do you?"
#    her "Yes, I do. No individual shall be treated differently based on his or her gender."
#    m "This doesn't make any sence, girl!"
#    her "Let me finish, professor!"
#    her "I'm organizing a \"Men's rights movement\" in our school!"
#    m "Oh, this is just typical! Blame everything on-"
#    m "Wait, did you say {size=+5}MEN'S{/size} rights?"
#    her "You have no idea how hard it is to be a boy in our school these days..."
#    menu:
#        "\"Didn't see this one coming...\"":
#            her "No, you did not, because you refuse to listen to me, sir!"
#        "\"Literally stupidest thing I've ever heard.\"":
#            her "I knew you will say something like that..."
    her "Half of the girls in this school are now selling favours for house points..."
    her "Sometimes even for good grades..."
    her "Nobody from the \"Gryffindor\" house of course..."
    her "And that's what puts us into disadvantage - our integrity!"
    her "Unthinkable..."
    her "As for the boys - they have to work ten times harder then the girls simply to pass a test..."
    her "Or, if they are lucky enough, get one meager house-point..."
    her "This is sexism in it's purest form!"
    menu:
        "\"What you want {size=+7}me{/size} to do?\"":
            her "Nothing!"
        "\"Not sure what to say...\"":
            her "You do not need to say anything anymore, professor."
        "\"You are being ridiculous!\"":
            her "Am I? Well, we'll see..."
    her "I already sent a letter to the ministry of magic."
    with hpunch
    g4 "{size=+7}You did what?!{/size}"
    m "{size=-4}(Wait, do I really give a damn about that?){/size}"
    her "I am sorry, but you left me no choice, professor."
    her "Now, if you excuse me I must get to my classes..."

    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "The little woman quite literary sucks out all the happiness out of me..."
   
    $ hermione_takes_classes = True
   
#    $ hermione_is_waiting_02 = False #Makes sure this event is not repeated.
#    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    return

###############################################################################################################################################################
label event_11: #Third visit, after second special date with Snape. Hermione complains that she almost failed a test. (EVENING EVENT!)
    #"EVENT_11"
    stop music fadeout 1.0
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    her "Professor, I'm coming in!"
    m "...."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 

    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.1 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    # show screen hermione_walk_01 
    show screen hermione_chibi_robe #Hermione. Chibi. Walking. Wearing a robe.
    with d4
    pause 1.8
    $ hermione_chibi_xpos = 400 #Near the desk.
    #show screen hermione_02 #Hermione stands still.
    show screen hermione_02_b #Hermione stands still wearing a robe.
    show screen bld1
    with Dissolve(.3)
    
    #$ herView.data().addItemKey( 'robe', CharacterExItemRobe( herView.mClothesFolder, "robe.png", G_Z_DRESS + 1, 'body' ) )
    $herView.data().addItem( 'item_robe_study' )
    
    $ pos = POS_370
    $herView.showQ( "body_09.png", pos )
    show screen ctc
    with Dissolve(.3)   
    pause

    $herView.hideshowQQ( "body_12.png", pos )
    her "Good evening professor."
    hide screen ctc
    menu:
        "\"-stare full of hatred-\"":
            $herView.hideshowQQ( "body_07.png", pos )
            her "You can stare at me all you want, sir."
            her "It will not make the problems of this school go away."
        "*sigh of exasperation*":
            $herView.hideshowQQ( "body_03.png", pos )
            her "Is this a bad time?"
            $herView.hideshowQQ( "body_02.png", pos )
            her "Well, since I'm already here..."
        "\"....................................\"":
            $herView.hideshowQQ( "body_02.png", pos )
            her "Professor?"
            m "Yes, yes..."
    $herView.hideshowQQ( "body_04.png", pos )
    her "Something... bizarre has happened today..."
    $herView.hideshowQQ( "body_07.png", pos )
    her "I'm Not sure how to describe this..."
    $herView.hideshowQQ( "body_09.png", pos )
    her "................................"
    $herView.hideshowQQ( "body_12.png", pos )
    her "I think I almost failed a test..."
    menu:
        "\"That happens to students sometimes.\"":
            $herView.hideshowQQ( "body_12.png", pos )
            her "To other students, yes. But not to me, sir!"
            $herView.hideshowQQ( "body_13.png", pos )
            her "Never to me..."
        "\"(Way to go, Snape!)\"":
            $herView.hideshowQQ( "body_03.png", pos )
            her "Excuse me?"
            m "What?"
            m "Oh, I said, that's too bad. How're you holding up?"
            $herView.hideshowQQ( "body_07.png", pos )
            her "................."
        "\"So why tell me?\"":
            her "Because... this is not an ordinary event!"

    her "I'm not sure what is going on here..."
    m "An evil scheme against you, miss Granger?"
    $herView.hideshowQQ( "body_03.png", pos )
    her "This is not a laughing matter, sir."
    $herView.hideshowQQ( "body_04.png", pos )
    her "You should consider me a \"measuring stick\" for our educational system."
    her "If I \"almost\" fail a test, the rest of the students will definitely fail it."
    m "Is that so...?"
    $herView.hideshowQQ( "body_07.png", pos )
    her "Yes, professor. Something went terribly wrong today..."
    $herView.hideshowQQ( "body_12.png", pos )
    her "................................."
    $herView.hideshowQQ( "body_11.png", pos )
    her "But what if it did not?"
    her "What if all the tests will be this difficult from now on?"
    $herView.hideshowQQ( "body_10.png", pos )
    her "I need to study harder!"
    label cant_say:
    menu:
        "\"I could tutor you, miss Granger.\"":
            $herView.hideshowQQ( "body_14.png", pos )
            her "You professor?"
            $herView.hideshowQQ( "body_15.png", pos )
            her "Oh, thank you for your offer but I don't think that would be necessary, sir."
            $herView.hideshowQQ( "body_16.png", pos )
            her "The best tutor is a book, and I have the entire Hogwarts library at my disposal."
        "\"A wise decision, miss Granger.\"":
            $herView.hideshowQQ( "body_15.png", pos )
            her "Thank you, professor."
        "\"You need to put my cock in your mouth.\"":
            m "You need to put my co--"
            $herView.hideshowQQ( "body_15.png", pos )
            her "Huh?"
            m "{size=-4}(No, I can't actually say that...){/size}"
            $herView.hideshowQQ( "body_17.png", pos )
            her "......?"
            jump cant_say
    m "............"
    $herView.hideshowQQ( "body_16.png", pos )
    her "Well, if there is nothing else, I have a studying schedule to keep."
    m "By all means..."
    
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_chibi_robe_f #Hermione. Chibi. Walking. Wearing a robe.
    #show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_chibi_robe_f #Hermione. Chibi. Walking. Wearing a robe.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    
    $ herView.data().delItem( 'item_robe_study' )
    
    $ event11_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
    $this.event_11.Finalize()
    return


###############################################################################################################################################################
label event_12: # Hermione complains that she did failed a test. (EVENING EVENT!)
    #"EVENT_12"
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    
    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.1 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.8
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    with d3
    her "Professor! I need to talk to you!"
    m "(So She doesn't even bother to knock anymore?)"
    show screen bld1
    with Dissolve(.3)
    $ pos = POS_370
    $herView.hideshowQQ( "body_11.png", pos )

    her "Professor, something awful happened today!"
    her "I failed a test today..."
    her "I cannot believe this is happening!"
    $herView.hideshowQQ( "body_18.png", pos )
    her "How this even possible?!"
    menu:
        "\"You should study more, girl!\"":
            $herView.hideshowQQ( "body_19.png", pos )
            her "But I did study all night!"
        "\"There, there... It'll be alright.\"":
            $herView.hideshowQQ( "body_20.png", pos )
            her "No it won't! This is a catastrophe!" 

    $herView.hideshowQQ( "body_21.png", pos )
    her "And the worst part is that I think I might be the only one who has failed..."
    $herView.hideshowQQ( "body_22.png", pos )
    her "How will it make me look like?"
    $herView.hideshowQQ( "body_23.png", pos )
    her "I will know for sure when we get the results though..."
    $herView.hideshowQQ( "body_13.png", pos )
    her "Yes, I'm sure everyone else failed as well..."
    $herView.hideshowQQ( "body_11.png", pos )
    her "I mean, they must have, right?"
    $herView.hideshowQQ( "body_13.png", pos )
    her "....................."
    $herView.hideshowQQ( "body_11.png", pos )
    her "....right?"
    menu:
        "{size=-3}\"Of course. You are a top student after all.\"{/size}":
            $herView.hideshowQQ( "body_09.png", pos )
            her "Exactly..."
            her "Or at least I used to be until today..."
            $herView.hideshowQQ( "body_20.png", pos )
            her "I cannot believe this is happening!"
        "{size=-3}\"You could get smarter if I tutor you.\"{/size}":
            $ tutoring_offer_made = True #Affects conversation in the next event.
            $herView.hideshowQQ( "body_17.png", pos )
            her "hm..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "Yes, that could help I suppose..."
            $herView.hideshowQQ( "body_14.png", pos )
            her "I appreciate your offer, professor, but..."
            her "May I think about it?"
            m "Don't take too long..."
        "{size=-3}\"I suppose we'll know soon enough.\"{/size}":
            $herView.hideshowQQ( "body_15.png", pos )
            her "Yes, I suppose we will..."

    $herView.hideshowQQ( "body_24.png", pos )
    her "I'm sorry, professor, I'm probably just overreacting anyway..."
    $herView.hideshowQQ( "body_14.png", pos )
    her "But you must understand that my reputation is at stake here!"
    $herView.hideshowQQ( "body_12.png", pos )
    her "There's gotta be something wrong with the test..."
    her "And although I failed I probably still got the most points in the test..."
    her "As usual..."
    $herView.hideshowQQ( "body_04.png", pos )
    

    her "Well I'd better go now. We have another \"MRM\" meeting today."
    her "I will let you know about the new ideas we will come up with tonight."
    m "I can hardly wait..."



    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5





    $ event12_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    $this.event_12.Finalize()
    return


###############################################################################################################################################################
label event_13: # Hermione complains that she almost failed a test. (EVENING EVENT!)
    #"EVENT_13"
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    


    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=500 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    with d4
    pause 1.3
    $ hermione_chibi_xpos = 500 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    with d3
    her "....................."
    m "???"
    
    $ walk_xpos=500 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    hide screen hermione_02 #Hermione stands still.
    pause 1.8
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    with d3
    her "............"
    m "Miss Granger?" 
    her "..............................."
    m "Miss Granger?!!" 
    show screen bld1
    with d3
    $ pos = POS_370
    $herView.hideshowQQ( "body_26.png", pos )
    show screen ctc
    pause
    her "Huh?"
    hide screen ctc
    her "Oh, I am already here?"
    her "I'm sorry sir... I..."
    her ".................."
    her "It seems that I did..."
    her "I did... uhm..."
    her "... I failed that test after all."
    her "I..."
    $herView.hideshowQQ( "body_27.png", pos )
    her "I am sorry, professor..."
    her "I'm not sure why I am here..."
    her "I think I'd better go..."
    m "..................."
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    
    
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 01.0 #The speed of moving the walking animation across the screen.
    hide screen bld1
    with d3
    show screen hermione_run

    pause.9
    hide screen hermione_run
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
  
    pause.3
    m "............."
    m "She will be alright..."
    m "I think..."



    
    
    
    
    
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    $ hermione_chibi_xpos = 400 #Middle of the room.
#    show screen hermione_01_f #Hermione stands still.
#    with d3
#    her "................."
#    $ walk_xpos=400 #Animation of walking chibi. (From)
#    $ walk_xpos2=510 #Coordinates of it's movement. (To)
#    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
#    show screen hermione_walk_01_f 
#    pause 2
#    hide screen hermione_walk_01_f 
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    $ hermione_chibi_xpos = 500 #Middle of the room.
#    show screen hermione_01_f #Hermione stands still.
#    with Dissolve(.3)
#    her "................"
    
#    $ walk_xpos=500 #Animation of walking chibi. (From)
#    $ walk_xpos2=610 #Coordinates of it's movement. (To)
#    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
#    show screen hermione_walk_01_f 
#    pause 2
#    hide screen hermione_walk_01_f 
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    with Dissolve(.3)
#    pause.5



    $ event13_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    $this.event_13.Finalize()
    return



###############################################################################################################################################################
label event_14: # Hermione comes after her breakdown (when she failed the test). She is asking for tutoring. Tutoring unlocked.
    #"EVENT_14"
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 

    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.1 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.8
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    with d3
    show screen bld1
    with Dissolve(.3)
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    show screen hermione_02
    with Dissolve(.3)   

    her "Good morning, Professor."
    m "How can I help you today, miss Granger?"
    $herView.hideshowQQ( "body_04.png", pos )
    her "Well, first of all I am terribly sorry about yesterday's display, sir..."
    $herView.hideshowQQ( "body_08.png", pos )
    her "I never failed a test in my life, so I wasn't sure how to react..."
    $herView.hideshowQQ( "body_04.png", pos )
    her "But I am all better now..."
    m "I see..." 
    her "I will not take much of your time, I promise..."
    if tutoring_offer_made:
        her "I am here to take you up on your offer."
        menu:
            "\"What offer?\"":
                her "A while back you offered to tutor me, sir..."
                menu:
                    "\"Oh... That offer has expired.\"":
                        $herView.hideshowQQ( "body_14.png", pos )
                        her "It..."
                        her "Expired, sir?"
                        her "B-but...."
                        $herView.hideshowQQ( "body_11.png", pos )
                        her "But I require tutoring, and you are the smartest wizard I know..."
                        $herView.hideshowQQ( "body_28.png", pos )
                        her "Please, sir, I really need your help."
                        menu:
                            "\"Show me your tits and it's a deal!\"":
                                $herView.hideshowQQ( "body_18.png", pos )
                                her "m-my...?"
                                $herView.hideshowQQ( "body_29.png", pos )
                                her "............"
                                her "....."
                                $herView.hideshowQQ( "body_30.png", pos )
                                with hpunch
                                her "{size=+5}Professor Dumbledore!!!{/size}"
                                m "{size=-5}(Well, at least I tried...){/size}"
                                her "I am not some \"Slytherin\" floozy!"
                                m "Of course not, miss Granger."
                                m "It was a test... You passed. Good job."
                                $herView.hideshowQQ( "body_31.png", pos )
                                her "What...?"
                                $herView.hideshowQQ( "body_24.png", pos )
                                her "Oh, of course. I'm so silly sometimes. Sorry about the yelling, sir."
                                m "My offer is still valid. If you want me to then I can tutor you."
                                $herView.hideshowQQ( "body_29.png", pos )
                                her ".............."
                            "\"Well, alright, alright...\"":
                                pass
                    "\"Oh, that's right. Great.\"":
                        pass

            "\"Splendid! Starting today?\"":
                pass
    else:
        $herView.hideshowQQ( "body_07.png", pos )
        her "I... uhm..."
        her "Sir Dumbledore, I hope this is not too much to ask..."
        m "Yes?"
        her "Ehm... would it be alright if..."
        her "..............."
        $herView.hideshowQQ( "body_09.png", pos )
        her "do You think you could tutor me a little, sir?"
        menu:
            "\"I suppose that is possible\"":
                pass
            "\"Hm... I'm quite busy actually.\"":
                $herView.hideshowQQ( "body_11.png", pos )
                her "Sir, please, you are the smartest wizard I know!"
                m "{size=-4}(You have no idea, little witch.){/size}"
                m "Well, it could be arranged, I suppose..."
    $herView.hideshowQQ( "body_01.png", pos )
    her "Thank you, sir. I am very grateful."
    $herView.hideshowQQ( "body_16.png", pos )

    her "Just let me know when, and I will bring my books!"

    $herView.hideshowQQ( "body_09.png", pos )
    her "I must study even harder from now on..."
    $herView.hideshowQQ( "body_06.png", pos )
    her "And I'll be taking private lessons from you sir, as often as possible."
    $herView.hideshowQQ( "body_07.png", pos )
    her "But that's not all..."
    her "The \"MRM\" shall investigate our education system much closer now..."
    her "I think some sort of foul-play might be taking place..."
    m "No way!"
    her "I have a list of suspects already but I will get back to you on this later...."
    m "Ehm... alright..."
    $herView.hideshowQQ( "body_10.png", pos )
    her "Oh, the classes are about to start. I'd better go..."
    
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5



    stop music fadeout 1.0

    $ event14_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    show screen blktone
    with d3
    show screen notes
    $ renpy.play('sounds/win2.mp3') 
    ">You unlocked an ability to summon Hermione Granger to your office."
    hide screen blktone
    with d3
#    $ summoning_hermione_unlocked = True #Unlocks after event_14. Adds "Summon Hermione" button to the door.
    $ hermione_takes_classes = True
#    $ tutoring_hermione_unlocked = True
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    $this.event_14.Finalize()
    return




###############################################################################################################################################################
label event_15: # Hermione comes and asks to buy a favour from her.
    
    #"EVENT_15"
    
#    $ slytherin +=49
#    hide screen s_p_u
#    $ s_p_u_pic = "what_49_points"
#    show screen s_p_u
    
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger." 
            m "(It's that young witch again...)" 
            her "Can I come in, sir?"
            menu:
                m "..."
                "\"Absolutely not! I'm busy! Come back later!\"":
                    her "But..."
                    her "Alright... I will come back tomorrow then..."
                    $event.NotFinished()
                    return 
                "\"Of course. Come on in.\"":
                    pass
        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well, alright..."
            $wtevent.NotFinished()
            return
        "\"Yes, come in.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"

   
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
    $herView.showQ( "body_13.png", pos )
    show screen hermione_02
    with Dissolve(.3)
    her "Good evening, professor..."
    her "........................"
    $herView.hideshowQQ( "body_29.png", pos )
    her "........................"
    her "........................"
    $herView.hideshowQQ( "body_31.png", pos )
    her "Ehm......"
    $herView.hideshowQQ( "body_29.png", pos )
    her "................."
    m "What is it, miss Granger?"
    $herView.hideshowQQ( "body_31.png", pos )
    her "Well, ehm..."
    her "You see... The \"Gryffindor\" house is not in the lead anymore..."
    $herView.hideshowQQ( "body_29.png", pos )
    her "And... everyone is working so hard..."
    her "And they look up to me for help but I don't know what to do..."
    m "............................"
    her "Professor Dumbledore...."
    $herView.hideshowQQ( "body_32.png", pos )
    stop music fadeout 2.0
    her "I want you to buy a favour from me!"
    $herView.hideshowQQ( "body_33.png", pos )
    menu:
        "\"You mean like a sexual favour?\"":
            $herView.hideshowQQ( "body_34.png", pos )
            her "Ehm... I'm not sure..."
            her "The kind that would gain our house additional points..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "I could write an essay for you or..."
            $herView.hideshowQQ( "body_34.png", pos )
            her "Or maybe clean your tower..?"
            m "{size=-4}(Clean my tower? Heh... There's gotta be dirty joke in there somewhere...){/size}"
            m "Well, alright then, I think we can figure something out."
        "\"Well, if you insist...\"":
            pass
        "\"I don't think so, miss Granger.\"":
            $herView.hideshowQQ( "body_31.png", pos )
            her "B-but... We need the points..."
            her "Professor, please, I am really desperate..."
            m "Desperate you say..?"
            m "Well alright..."
    $herView.hideshowQQ( "body_01.png", pos )
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    her "Thank you, professor..."
    label choose_favor_agagin:
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    $ d_flag_04 = False
    her "So... What will it be?"
    menu:
        "\"Show me your tongue...\"":
            $ d_flag_01 = True
            pass
        "\"Stand there. Let me look at you.\"":
            $ d_flag_02 = True
            pass
        "\"Make a silly face...\"":
            $ d_flag_03 = True
            pass
        "\"Say \"I've been a bad girl\".\"":
            $ d_flag_04 = True
            pass

    her "Em..."
    her "How many house points will I get for that...?"
    $ d_flag_05 = False # 20 Points.
    $ d_flag_06 = False # 40 Points.
    $ d_flag_07 = False # 10 Points.
    $ d_flag_08 = False # 1 Point.
    menu:
        "\"1 point.\"":
            if d_flag_02: #Stand there.
                $ d_flag_08 = True # 1 Point.
                pass
            else:
                her "I don't think it's worth it then..."
                jump choose_favor_agagin
        "\"10 points.\"":
            if d_flag_02: #Stand there.
                $ d_flag_07 = True # 10 Points.
                pass
            else:
                her "I don't think it's worth it then..."
                jump choose_favor_agagin
        "\"20 points.\"":
            $ d_flag_05 = True
            her "So little...?"
            pass
        "\"40 points.\"":
            $ d_flag_06 = True
            pass

    
    
    $ pos = POS_140
    her "Em, alright..."
    if d_flag_01: #Show me your tongue.
        $herView.hideshowQQ( "body_24.png", pos )
        her "M-my... tongue, sir?"
        m "Yes, girl, open your mouth and show me your tongue."
        $herView.hideshowQQ( "body_12.png", pos )
        her "{size=-7}(What a weirdo...){/size}"
        $herView.hideQQ()
        
        $ herView.showQQ( "body_07.png", pos )
        her "Ehm... well, alright then..."
        $ herView.hideQQ()
        
        $ herView.showQQ( "body_08.png", pos )
        her "Here..."
        $herView.hideshowQQ( "body_35.png", pos )
        her "............."
        her "............."
        $herView.hideshowQQ( "body_36.png", pos )
        her "................."
        show screen ctc
        pause
        menu: 
            "\"Very good. Here are your points.\"":
                pass
            "\"Not good enough. You can do better\"":
                $herView.hideshowQQ( "body_12.png", pos )
                her "..............."
                her "Alright, I will try to do better, sir..."
                $herView.hideshowQQ( "body_11.png", pos )
                her "How about this?"
                $herView.hideshowQQ( "body_37.png", pos )
                her "A-a-ah.................."
                $herView.hideshowQQ( "body_38.png", pos )
                "............................"
                $herView.hideshowQQ( "body_39.png", pos )
                her "......................................"
                her "..................................................."
                her "...................................................................."
                $herView.hideshowQQ( "body_40.png", pos )
                her "......................................................................................................."

    if d_flag_02: #Stand still...
#    if d_flag_01: #STAND STILL.
        $herView.hideshowQQ( "body_06.png", pos )
        her "So, I just have to stand here then...?"
        m "Good... Now turn around... slowly."
        her "uhm... alright..."
        $herView.hideQ()
        hide screen bld1
        with d3
        pause.5
        show screen hermione_01_f #Hermione stands still.
        with Dissolve(.7)

        $her_head_state = 2
        her_head_main "................................."
        menu:
            m "Hm..."
            "\"The uniform suits you, miss Granger...\"":
                $her_head_state = 1
                her_head_main "............"
                $her_head_state = 5
                her_head_main "Thank you, professor Dumbledore..."
            "\"You have a nice body, miss Granger...\"":
                $her_head_state = 3
                her_head_main "!?"
                $her_head_state = 4
                her_head_main ".............."
                her_head_main "Thank you, professor..."
            "\"That's enough. Here are your points...\"":
               
                
               
                show screen hermione_01 #Hermione stands still.
                with Dissolve(.7)
                pause.5
                show screen bld1
                with d3
                jump stupid_enogh
                                                        
            

        
        
        m "Very good, you can turn back now..."
        show screen hermione_01 #Hermione stands still.
        with Dissolve(.7)
        pause.7
        $ herView.showQQ( None, pos )
        show screen bld1
        with d3
        her "................."
   
    
    
#    if d_flag_02: #Pretend to be a monkey.
#        her "A monkey then..."
#        her "ooh ooh...."
#        her "ooh ooh ooh...."
#        m "Good, but you can do better..."
#        her "ooh ooh ooh...."
#        her "ooh ooh ooh... eee eee eee aah aah aah..."
#        m "Very well..."
    if d_flag_03: #STUPID FACE
        $herView.hideshowQQ( "body_24.png", pos )

        her "A silly face then..."
        her "Let's see..."
        label stupid_faces:
        $herView.hideshowQQ( "body_41.png", pos )
        her "How about this one?"
        menu:
            "\"Good! Very stupid! I mean, silly.\"":
                jump stupid_enogh
            "\"Not stupid enough.\"":
                pass
        $herView.hideshowQQ( "body_12.png", pos )
        her "........."
        $herView.hideshowQQ( "body_43.png", pos )
        her "What about this one then?"
        menu:
            "\"Ha-ha! You look like an idiot!\"":
                jump stupid_enogh
            "\"No, not stupid enough.\"":
                pass
        $herView.hideshowQQ( "body_12.png", pos )
        her "........."
        $herView.hideshowQQ( "body_42.png", pos )
        her "What if I do it like this?"
        menu:
            "\"Good! Very stupid.\"":
                jump stupid_enogh
            "\"Not stupid enough.\"":
                jump stupid_faces
    
    if d_flag_04: #BAD GIRL
        $herView.hideshowQQ( "body_07.png", pos )
        her "I..."
        her "I have been a very bad girl..."
        g9 "Have you been a very, very, very bad girl?"
        her "Yes, sir..."
        her "I have been very, very, very, very bad..."
        label to_early_for_sucking_cocks:
        menu:
            g9 "..."
            "\"Do you need to be punished?\"":
                $herView.hideshowQQ( "body_11.png", pos )
                her "Do I need to... be punished?"
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ehm..."
                her "....................."
                $herView.hideshowQQ( "body_12.png", pos )
                her "Well, I am not perfect, if that's what you mean, sir..."
                $herView.hideshowQQ( "body_13.png", pos )
                her "But do I need to be punished... hm?"
                $herView.hideshowQQ( "body_07.png", pos )
                her "Is this really for me to decide...? I mean..."
                her "What does this have to do with anything?"
                m "You are overanalyzing this, girl."
                m "Just say that you need to be punished!"
                $herView.hideshowQQ( "body_05.png", pos )
                her "Fine. I need to be punished!"
                $herView.hideshowQQ( "body_33.png", pos )
                her "{size=-5}(And I truly do think so sometimes...){/size}"
                m "That's a good girl."
                $herView.hideshowQQ( "body_44.png", pos )
                her "................??"
                m "Now that wasn't hard at all, was it?"
                $herView.hideshowQQ( "body_29.png", pos )
                her "n-no , sir..."
                m "Alrighty, then..."
            "\"Do you want to get spanked?\"":
                $herView.hideshowQQ( "body_11.png", pos )
                her "Do I want to..."
                $herView.hideshowQQ( "body_18.png", pos )
                her "Get s-spanked??"
                $herView.hideshowQQ( "body_05.png", pos )
                her "Tsk!"
                $herView.hideshowQQ( "body_04.png", pos )
                her "Professor, I don't think I'm comfortable with--"
                m "My bad, let me rephrase the question..."
                m "How badly do you need those points?"
                $herView.hideshowQQ( "body_09.png", pos )
                her ".................."
                $herView.hideshowQQ( "body_04.png", pos )
                her "Yes, sir. I do need to get spanked."
                m "Alright, that's good enough for now..."
                $herView.hideshowQQ( "body_07.png", pos )
                her "{size=-4}(For now?){/size}"
            "\"Come here and suck my cock!\"":
                m "{size=-5}(Too early for this... I need to reel her in first.){/size}"
                jump to_early_for_sucking_cocks
            
        

    label stupid_enogh:
    if d_flag_05:
        m "20 points to the \"Gryffindor\" house."
        $ gryffindor +=20
    elif d_flag_06:
        m "40 points to the \"Gryffindor\" house."
        $ gryffindor +=40
    elif d_flag_07:
        m "10 points to the \"Gryffindor\" house."
        $ gryffindor +=10
    elif d_flag_08:
        m "1 point to the \"Gryffindor\" house."
        $ gryffindor +=1
    
    
    $herView.hideshowQQ( "body_24.png", pos )
    her "Yay!.............."
    her "This was quite easy..."
    her "You think you could buy some more favours from me in the future, professor?"
    menu:
        "\"I don't think that's a good idea.\"":
            $herView.hideshowQQ( "body_28.png", pos )
            her "Please, professor..."
            her "We really need those points..."
            m "......."
            $herView.hideshowQQ( "body_29.png", pos )
            her "You are an esteemed wizard and to be honest..."
            her "The only person in this school whom I don't mind asking for this..."
            m "Well, when you put it that way..."
        "\"That's a possibility...\"":
            pass
            
    $herView.hideshowQQ( "body_06.png", pos )
    her "Thank you professor. Thank you so much."
    $herView.hideshowQQ( "body_01.png", pos )
    her "Well, I suppose, I'd better go now..."
    m "............"

    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    $ hermione_chibi_xpos = 610 #Near the desk.
    hide screen hermione_walk_01_f 
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)

    if d_flag_01: #Show me your tongue
        her "{size=-4}(Hm...){/size}"
        her "{size=-4}(Students show teachers their tongues all the time...){/size}"
        her "{size=-4}(Although that's usually when the teacher is not looking...){/size}"
        her "{size=-4}(But there is nothing wrong with what I did today...){/size}"
        her "{size=-4}(I earned my house extra points...){/size}"
        
    if d_flag_02: #Stand still...
        her "{size=-4}(I can just stand there and let the professor look at me...){/size}"
        her "{size=-4}(There is nothing wrong with that... nothing at all...){/size}"
#        her "{size=-4}(ooh ooh ooh... eee eee eee aah aah aah...){/size}"
#        her "{size=-4}(I'm a monkey... I'm a money... I need to practice more...){/size}"
    if d_flag_03:
        her "{size=-4}(Stupid face...){/size}"
        her "{size=-4}(Stupid face...){/size}"
        her "{size=-4}(I need to practice this.){/size}"
    if d_flag_04:
        her "{size=-4}(I'm a bad girl...){/size}"
        her "{size=-4}(I am very bad...){/size}"
        her "{size=-4}(Yes, I can say things like that easily...){/size}"
        her "{size=-4}(There is nothing wrong with that... nothing at all...){/size}"


    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)


    $ event15_happened = True #Allows next event to start. This one stops looping when you not let Hermione in.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    stop music fadeout 1.0
    show screen blktone
    with d3
    show screen notes
    $ renpy.play('sounds/win2.mp3') 
    ">You unlocked an ability to buy sexual favours from Hermione Granger."
    hide screen blktone
    with d3
    $ buying_favors_from_hermione_unlocked = True 
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    $ event15_happened = True #Turns TRUE after event_15
    $this.event_15.Finalize()
    
    if daytime:
        $ hermione_takes_classes = True
    else:
        $ hermione_sleeping = True
    
    return



label event_16: #Учебники доставлены
    $ teacher_jinn_quest = 6
    m "..."
    m "Is there a point in your life?"
    m "..."
    g4 "Who does porn games in which the protagonists have time to be distracted by such crap?"
    #стук-перестук, заходит гермиона
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    with d3
    $herView.hideshowQQ( "body_01.png", pos )
    her "Good evening, Professor Dumbledore."
    her "Your textbooks profit."
    m "Three days, Yes..?"
    m "Why is everyone so often use the number 3 in the fictional stories?"
    g4 "Figure 29 also stylish looks!"
    $herView.hideshowQQ( "body_09.png", pos )
    her "Um... Professor?"
    m "... something I digress."
    m "Philosophical mood, you know."
    m "You said something about the textbooks?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Uh, yeah... Your books delivered."
    g9 "Perfect! And where are they?"
    $herView.hideshowQQ( "body_15.png", pos )
    her "Lie behind the door. So many of them that Harry and Ron took a half hour to move them all out of the Gryffindor tower."
    g4 "(And she even said something about equality of the sexes... Hypocritical bitch!)"
    m "Excellent! Bring them here!"
    $herView.hideshowQQ( "body_11.png", pos )
    her "I'm afraid that Harry and Ron had already left, and this room is too small."
    m "Too small? How many books are there?"
    her "438, Not including brochures Harry Thompson of taming the Kraken."
    m "(This is definitely a hot night...)"
    m "Thank you, will not help to bring them here?"
    $herView.hideshowQQ( "body_10.png", pos )
    her "But where we..."
    m "Don't worry, I have an idea where they can be put..."
    show screen blkfade 
    "..."
    hide screen blkfade
    $herView.hideshowQQ( "body_13.png", pos )
    her "I never thought that such a wizard as you have a magic wardrobe?"
    g9 "Well, it's rather a magical wine cellar. Although it fits perfect and other stuff."
    $herView.hideshowQQ( "body_184.png", pos )
    her "..."
    m "Anyway, thank you very much, you have given me and science a great service!"
    m "Now, if you'll allow me, I need to start the research."
    $herView.hideshowQQ( "body_14.png", pos )
    her "But sir, I've helped you, right?"
    $herView.hideshowQQ( "body_13.png", pos )
    her "And Harry and Ron tried very hard..."
    m "... and?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "It would be fair to award the points Gryffindor faculty, right?"
    m "Hm..."
    menu:
        "Give 5 points":
            m "Okay, okay..."
            m "Five points to Gryffindor!"
            $ gryffindor +=5
            $herView.hideshowQQ( "body_16.png", pos )
            her "How?! Five measly points?!"
            $herView.hideshowQQ( "body_28.png", pos )
            her "I spent two hours of his life working as a loader and received five points?!"
            $herView.hideshowQQ( "body_110.png", pos )
            her "Miser!"
            hide screen bld1
            $herView.hideQ( Dissolve(.3) )
            $ walk_xpos=400 #Animation of walking chibi. (From)
            $ walk_xpos2=610 #Coordinates of it's movement. (To)
            $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
            show screen hermione_walk_01_f 
            pause 2
            hide screen hermione_walk_01_f 
            $ hermione_chibi_xpos = 610 #Near the desk.
            show screen hermione_01_f #Hermione stands still.
            with Dissolve(.3)
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            hide screen hermione_01_f #Hermione stands still.
            with Dissolve(.3)
            $hermi.liking -= 15 #Потом возможно добавить больше?
            m "You've had enough of those ten thousand that I'm investing in this quest."
        "Give 15 points":
            m "Well, I think you deserve."
            m "Fifteen points to Gryffindor!"
            $ gryffindor +=15
            $herView.hideshowQQ( "body_01.png", pos )
            her "Thank you, sir."
            her "Good night."
            hide screen bld1
            $herView.hideQ( Dissolve(.3) )
            $ walk_xpos=400 #Animation of walking chibi. (From)
            $ walk_xpos2=610 #Coordinates of it's movement. (To)
            $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
            show screen hermione_walk_01_f 
            pause 2
            hide screen hermione_walk_01_f 
            $ hermione_chibi_xpos = 610 #Near the desk.
            show screen hermione_01_f #Hermione stands still.
            with Dissolve(.3)
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            hide screen hermione_01_f #Hermione stands still.
            with Dissolve(.3)
        "Give 100 points":
            m "Sure, why not?"
            m "A hundred points to Gryffindor!"
            $ gryffindor +=100
            $herView.hideshowQQ( "body_72.png", pos )
            her "A hundred points?!"
            $herView.hideshowQQ( "body_15.png", pos )
            her "But we had only brought books..."
            m "Not satisfied with something? I can always take them back..."
            $herView.hideshowQQ( "body_75.png", pos )
            her "No... of Course not!"
            $herView.hideshowQQ( "body_15.png", pos )
            her "Thank you very much, sir."
            $herView.hideshowQQ( "body_16.png", pos )
            her "If you ever need anything, just call, Gryffindor is always ready to help!"
            $herView.hideshowQQ( "body_06.png", pos )
            her "Good night."
            hide screen bld1
            $herView.hideQ( Dissolve(.3) )
            $ walk_xpos=400 #Animation of walking chibi. (From)
            $ walk_xpos2=610 #Coordinates of it's movement. (To)
            $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
            show screen hermione_walk_01_f 
            pause 2
            hide screen hermione_walk_01_f 
            $ hermione_chibi_xpos = 610 #Near the desk.
            show screen hermione_01_f #Hermione stands still.
            with Dissolve(.3)
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            hide screen hermione_01_f #Hermione stands still.
            with Dissolve(.3)
            show screen bld1
            with d3
            m "Ten thousand coins and a hundred points of the faculty..."
            m "My budget for a long time to recover from this."
        "Cost!":
            m "Of course not, that's silly."
            $herView.hideshowQQ( "body_18.png", pos )
            her "What..?"
            $herView.hideshowQQ( "body_76.png", pos )
            her "But..."
            m "After all, you did it for the good of science, and not for selfish motives, right?"
            m "That is why I entrusted it to you, the students proud Gryffindor!"
            m "I thought you didn't want the reward."
            $herView.hideshowQQ( "body_16.png", pos )
            her "But the scoring system was invented in order to pokerati for students..."
            m "You are absolutely right. But, judging by your words, I was wrong. I was wrong about you. You can pick up your glasses and get out of my office."
            $herView.hideshowQQ( "body_77.png", pos )
            her "..."
            $herView.hideshowQQ( "body_73.png", pos )
            her "..."
            her "{size=-4}Sorry...{/size}" #мелким шрифтом
            m "Excuse me, what?"
            $herView.hideshowQQ( "body_07.png", pos )
            her "You... You are absolutely right..."
            $herView.hideshowQQ( "body_01.png", pos )
            her "In the pursuit of victory, we began to forget about something important."
            $herView.hideshowQQ( "body_11.png", pos )
            her "I need to think about it..."
            $herView.hideshowQQ( "body_07.png", pos )
            her "I'm sorry." #Возможно после этого Гермиона перестанет продавать очки обучения? На будущее 
            hide screen bld1
            $herView.hideQ( Dissolve(.3) )
            $ walk_xpos=400 #Animation of walking chibi. (From)
            $ walk_xpos2=610 #Coordinates of it's movement. (To)
            $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
            show screen hermione_walk_01_f 
            pause 2
            hide screen hermione_walk_01_f 
            $ hermione_chibi_xpos = 610 #Near the desk.
            show screen hermione_01_f #Hermione stands still.
            with Dissolve(.3)
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            hide screen hermione_01_f #Hermione stands still.
            with Dissolve(.3)
            show screen bld1
            with d3
            m "I hope I haven't overdone...?"
            m "However, what's the difference? My job is inaccessible to turn girls to whores and not to worry about their feelings."
    m "Well, it's time to call Snape."
    m "Hmm... Interesting how the system works call people in this room?"
    m "Like I'm not doing anything, and they..."
    #входит Снейп
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01 
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
    show screen snape_main
    with Dissolve(.3)                                                                                                               #SNAPE
    with d3  
    sna "You called, Ginny?"
    m "..."
    m "How do you do it?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3  
    sna "What do you mean?"
    m "How you show up in this room, I just have to think about it?"
    sna "Unless your magic Secretary with a spell of gromkogovorya does not shout it to the whole school the name of the person you want to call?"
    m "Hmm... Sounds about right..."
    stop music 
    $ renpy.play('sounds/scratch.wav')
    m "..!"
    m "I..."
    m "have..."
    g4 "{size=+4}FUCKING THE SECRETARY??!{/size}"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_11.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3  
    sna "Well, yeah... didn't you know?"
    "{size=+4}WHERE?!{/size}"
    "{size=+4}HOW COULD YOU HIDE FROM ME A FEMALE CHARACTER??!!{/size}"
    "{size=+4}BRING HER HERE!!!{/size}"
    sna"..."
    "{size=+4}WHAT UP?!! QUICKLY GET HER IN HERE!!!{/size}"
    sna "..."
    "{size=+4}ARE YOU DEAF?!{/size}"
    sna "..."
    "Hmm... Snape?"
    sna "..."
    m "..."
    sna "..."
    m "Come on, it's not funny!"
    sna "..."
    g9 "Okay, we can fuck her together!"
    sna"..."
    m "Well, he hung."
    g4  "Who did the optimization and testing, huh?!"
    "Mystical voice" "would you stop?" #мистический голос
    "Mystical voice" "already got All the jokes about the fact that you know that you are in the game!"
    m "But.."
    "Mystical voice" "And forget about the Secretary. At least not yet."#мистический голос
    m "Right..."
    "Mystical voice" "Will argue - your Secretary will become the owner of the brothel from Agraba." #мистический голос
    "Mystical voice" "And she'll be a nympho."
    m  "*gulp*"
    g9 "Okay, I think I can do without a Secretary..."
    g4 "*Oh* And how can you work in such conditions?"
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3  
    sna "You said something, Ginny?" #snape
    m "Ahem, Yes, I asked her if tincture?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3  
    sna "\"Potion\", Ginny."
    #Шутки про "зелье" возможно допишу позже
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3  
    sna "Yes, I just finished cooking it."
    sna "You seems to be working quite well for the moment."
    g4 "{size=-4}Well, how not to joke about the developers?{/size}" #мелкий шрифт
    m "Okay... let's get started Then?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3  
    sna "Of course, you can start. Here's your balanoidea potion, and I should Clean boilers Botanic...."
    hide screen snape_main
    hide screen bld1
    with d3
    hide screen snape_01_f
    hide screen bld1
    hide screen snape_main
    hide screen snape_02 #Snape stands still. 
    #hide screen genie
    show screen blkfade
    with d3
    $ renpy.play('sounds/07_run.mp3') 
    pause 2
    $ renpy.play('sounds/door.mp3')
    show screen bld1
    g4 "{size=+4}WHAT DID YOU CALL ME??!!{/size}"
    g4 "Grrr, I will remember him..."
    "A new quest! To Take Revenge On Snape."
    m "I hope this potion would calm me down."
    #желательно-звук открывающийся бутылки
    "*ping!*"
    g4 "Wow, what a smell..."
    m "I doubt that after a bottle of this stuff in the morning I'll be something to remember..."
    m "Well, at least this thing is expensive."
    #звук того, как кто-то пьет :D
    m "Hmm... I feel nothing."
    g4 "Did Snape just fucked me?"
    m "Yes, and these jokes with the name..."
    m "Okay, I think he stands a chance..."
    if zyablik_switch == 1:
        m "Let's start with the biggest books."
        m "It's called... \"Mythological biology for dummies\"."
        "\"Chapter 1 - The Manticore\"..."
        #найти звук удара по клавишам
        g4 "{size=+4}Seriously?!{/size}"
        m "Here also pictures there..."
        m "..."
        m "..."
        m "Fuck it."
        "After a night filled with learning and... Well, you know what."
        $ renpy.play('sounds/door.mp3')                                                                                                                                                  #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                         # SNAPE
        show screen s_head2                                                                                                                  #SNAPE  
        sna2 "Hey, how's our..."
        hide screen s_head2                                                                                                                  #SNAPE                                                                                                                                                  #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_11.png"                                         # SNAPE
        show screen s_head2
        sna2 "!!!"
        sna2 "{size=+4}WHAT THE HELL IS GOING ON HERE??!!{/size}"
        hide screen s_head2
        m "{size=-4}Oh, Snape, buddy...{/size}" #хорошо бы нарисовать измотанного Джина, но это уже на совести художников
        m "{size=-4}How are you doing, friend?{/size}"
        $ s_sprite = "03_hp/10_snape_main/snape_15.png" 
        sna2"{size=+4}IT'S YOU I HAVE TO ASK!!!{/size}"
        hide screen s_head2                                                                                                                   #SNAPE                                                                                                                                                #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                                                            #SNAPE
        show screen s_head2                                                                                              #SNAPE
        sna2 "The room looks as if it was a herd of Minotaurs in the mating season."
        hide screen s_head2                                                                                                                   #SNAPE                                                                                                                                                #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
        show screen s_head2                                                                                                                  #SNAPE
        sna2 "Don't tell me that..."
        m "Don't worry, tincture worked."
        g9 "I have studied the whole school program Thoroughly...."
        hide screen s_head2                                                                                               #SNAPE                                          #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_08.png"                                                                            #SNAPE
        show screen s_head2                                                                                                                  #SNAPE
        sna2 "Then, what the hell..."
        hide screen s_head2                                                                                                                   #SNAPE                                                                                                                                                 #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
        show screen s_head2                                                                                                                  #SNAPE
        sna2 "Though, forget it. I definitely don't want to know."
        hide screen s_head2                                                                                                                  #SNAPE                                                                                                                                                 #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
        show screen s_head2                                                                                                                  #SNAPE
        sna2 "See you later."
        sna2 "..."
        hide screen s_head2                                                                                                                   #SNAPE                                                                                                                                               #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
        show screen s_head2                                                                                                                 #SNAPE
        sna "And here's another, clean it up."
        hide screen s_head2 
        $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
        show screen s_head2
        sna2 "I don't want to slip on... and crack your skull."
        hide screen s_head2 
        m "Of course, no problem."
        $ renpy.play('sounds/door.mp3')
        m "..."
        m "I get the feeling that the plot is going in the wrong direction."
        m "Okay, we gotta get organized here..."
        "Quest completed! Ginny gets +50 to intelligence and the ability to teach Hermione! (in future updates, of course)"
        "Bonus reward! Genie receives a strange fetish!"
        g4 "Not true! This is the last time!"
    else:
        m "Perhaps I'll start with this strange books..."
        stop music
        m "..!"
        # тут должна быть эпичная музыка
        g4 "{size=+4}I feel... the POWER!{/size}"
        "{size=+4}RACED!!!!{/size}"
        "{size=+4}GIGA-GINNIE-BREEEEKAAAAAR!!!!!{/size}"
        "{size=+4}After a night full of studying and pathetic cries.{/size}"
        $ renpy.play('sounds/door.mp3')                                                                                                                 #SNAPE                                                                                                                                               #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_17.png"                                                                            #SNAPE
        show screen s_head2                                                                                                                 #SNAPE
        sna2 "How is our Bo... hard-working student?"
        hide screen s_head2
        m "{size=-4}... Snape...{/size}" #again, Picchu tired Jinnah would not have prevented
        m "{size=-4}... tincture working...{/size}"
        m "{size=-4}... even too much.{/size}"
        m "{size=-4}There is something a hangover..?{/size}"                                                                                                                   #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
        show screen s_head2  
        sna2 "..."
        $ s_sprite = "03_hp/10_snape_main/snape_17.png"                                                                            #SNAPE
        sna2 "Happy day, Genie."
        hide screen s_head2                                                                                                                                                #SNAPE
        $ renpy.play('sounds/door.mp3')
        g4 "{size=-4}Come back...{/size}"
        g4 "{size=-4}Traitor...{/size}"
        "A new quest! Cruel revenge on Snape!"
        m "... stinker."
        m "At least I can start training girls..."
        "Quest completed! Genie gets +50 to intelligence and the ability to teach Hermione! (in future updates, of course)"
        g4 "Future updates? Then it was all in vain?"
        m "...fuck it..."
    if daytime:
        jump night_start
    else: 
        jump day_start


label bad_reports:              
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01 
    with d3
    pause 1.5
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"  
    show screen snape_02 #Snape stands still.#SNAPE
    show screen bld1                                                                         #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3
    sna "Добрый вечер, Джинни."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3
    sna "Ты не занят?"
    m "Как будто я могу чем-то занят, кроме чтения глупых книжек и клепания отчетов в министерство."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3
    sna "\"Клепание отчетов\"? Серьезно? И что ты туда пишешь?"
    m "Хм, ну..."
    m "..."
    m "А действительно, что я там пишу..?"
    sna "Ты уже не помнишь?"
    m "Если честно, я просто беру в руку перо и отключаюсь на полдня."
    m "А когда просыпаюсь, то нахожу парочку написанных страниц."
    sna "Серьезно?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_08.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3
    sna "Тебе никогда не было интересно, что ты пишешь, находясь в бессознательном состоянии и отправляешь парням, которые могут упечь нас с тобой за решетку?"
    m "..."
    m "Упс."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_07.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3
    sna "Дело в том, что, возможно, на перо наложено заклятие легилименции."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3
    sna "И тогда у нас с тобой большие неприятности."
    m "А что делает эта лега..."
    m "Легулиме..."
    g1 "{size=+5}ЧЕРТ ВОЗЬМИ, КТО ВЫДУМЫВАЛ ВСЕ ЭТИ НАЗВАНИЯ?!!{/size}"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3
    sna "Кто знает? Это искусство очень древнее, так что, я думаю, что ее так назвал какой-нибудь могущественный маг..."
    g9"... или женщина, пишущая глупые книжки для подростков." #jinnie
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3
    sna "..." #sna
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3
    sna "В общем, если рассказывать вкратце, то легилименция позволяет магу читать чужие мысли и воспоминания."
    g9 "Звучит круто."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3
    sna "Да, но если твои мысли читают шишки из министерства, то удивительно что мы с тобой еще не оказались в Азкабане."
    m "..."
    m "Что не говори, а все эти названия выдумывал явно не великий волшебник."
    m "Если ты так волнуешься, то мы можем прочесть парочку страниц."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3
    sna" И почему у меня на этот счет такое плохое предчувствие..?" #sna
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3
    sna "Ладно, давай."
    m "Так, посмотрим..."
    m "А! Вот, пара страниц, которые я забыл отправить."
    sna "Что ж, валяй."
    $ letter_text = "{size=-4}Аграба!.. Торговец, \nТоржествуя,\nУж ослика торопит в путь;\nЕго глаза, барыш почуя,\nБоятся лишний раз моргнуть;\nПески великие вздымая,\nБежит принцесса удалая;\nНо вот, за нею по пятам - \nИ Джинн, Джафар, Бхагаватам!\n... Они её в углу поймали...{/size}"

    





