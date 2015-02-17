###################REQUEST_24 (Level 07) (65 pt.) (Blowjob to a boy). (Available during daytime only).
label new_request_24: #LV.7 (Whoring = 18 - 20)
    
    $herView.hideQQ()
    m "{size=-4}(Tell her to go give a blowjob to one of her classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            $event.NotFinished()
            jump new_personal_request
            
    
    $ pos = POS_140

    if request_24_points == 0: # <================================================================================ FIRST TIME
        
        m "Miss Granger, I will be buying another favour from you today."
        $herView.hideshowQQ( "body_16.png", pos )
        her "Thank you, sir. I really appreciate it."
        m "Sure, Happy to help."
        m "I need you to go give a blowjob to one of your classmates."
        $herView.hideshowQQ( "body_48.png", pos )
        stop music fadeout 1.0
        her "!!!"
        her "...with my mouth?"
        if whoring <=17 or request_23_points <= 1: # Counts how many times you sent Hermione to give a handjob to a boy.
            jump too_much
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        m "Yes, that's how it's usually done..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Sir, I..."
        $herView.hideshowQQ( "body_186.png", pos )
        her "I refuse to sell you a depraved favour like that, sir."
        $herView.hideshowQQ( "body_131.png", pos )
        her "Can't I just kiss another girl instead?"
        her "I do not mind that..." 
        m "Miss Granger, please stop wasting my time..."
        m "If you are not in the mood to sell favours today..."
        m "Then there is the door."
        $herView.hideshowQQ( "body_120.png", pos )
        her "But I need the points, sir. You know that."
        m "It's as the saying goes, miss Granger..."
        m "\"If you won't suck a dick for it - you don't need it.\""
        $herView.hideshowQQ( "body_187.png", pos )
        her "Tch..."
        her "............................"
        m ".........................................."
        $herView.hideshowQQ( "body_69.png", pos )
        her "...alright."
        her "I'll do it..."
        m "Go do it, then!"
        m "Report back to me after your classes."
        $herView.hideshowQQ( "body_187.png", pos )
        her "......................................................................"
        her "......................................................................"
        her "......................................................................"
        m "You may leave, miss Granger."
        her "........."
        
    else: # <================================================================================ NOT FIRST TIME
        if whoring >= 18 and whoring <= 20: # LEVEL 07 FIRST EVENT.
            m "Go give some lucky boy another blowjob, girl."
            $herView.hideshowQQ( "body_66.png", pos )
            her "......Again?"
            m "Yes, again."
            $herView.hideshowQQ( "body_79.png", pos )
            her ".........."
        elif whoring >= 21: # LEVEL 08+ SECOND EVENT.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Miss Granger..."
            m "Do you believe in horoscopes?"
            $herView.hideshowQQ( "body_12.png", pos )
            her "Not even a little bit, sir..."
            m "Well, maybe you should..."
            $herView.hideshowQQ( "body_14.png", pos )
            her "...?"
            m "Because I got yours right here and it says..."
            m "\"Dedicate today to something you do well\"..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "Something I do well...?"
            m "Go suck on some cocks, girl."
            $herView.hideshowQQ( "body_79.png", pos )
            her "....................." # :(
            m "Report back to me after your classes as usual..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Of course..."
        
        
    
    
   
    
    
    $ request_24 = True

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
    jump day_main_menu
    
    
    
    

    

        

label new_request_24_complete:  # <=================================================================================================== EVENING
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
    $ herView.data().saveState()

    if whoring >= 18 and whoring <= 20: # LEVEL 07                    
        if one_out_of_three == 1: ### EVENT (A)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "You know the drill, girl. Start talking."
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_66.png", pos )
            her "I have completed your task, sir."
            m "Good. Tell me more."
            $herView.hideshowQQ( "body_69.png", pos )
            her "What is there to tell, sir?"
            her "I sucked off one of my classmates today..."
            her "And that's it..."
            m "Hm... I see..."
            m "..............."
            $herView.hideshowQQ( "body_118.png", pos )
            her "...................................."
            m "Did you swallow?"
            $herView.hideshowQQ( "body_79.png", pos )
            her "..........................."
            m "Miss Granger, did you swallow the load properly?"
            $herView.hideshowQQ( "body_47.png", pos )
            her "Yes I did, sir."
            m "Well, I suppose that will do for now..."

            
        elif one_out_of_three == 2: ### EVENT (B)
            m "Miss Granger, did you complete your task?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_118.png", pos )
            play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
            her "Sir, I..."
            her "I tried, but..."
            $herView.hideshowQQ( "body_67.png", pos )
            her "The boy turned me down, sir..."
            $herView.hideshowQQ( "body_22.png", pos )
            her "I cannot believe that actually happened..."
            her "I am one of the top students in this school!"
            her "One of the most popular ones too..."
            
            $herView.data().addItem( 'tears', CharacterExItem( herView.mMiscFolder, "tears_01.png", G_Z_FACE + 1 ) )
            
            $herView.hideshowQQ( "body_47.png", pos )
            her "And he turns me down?"
            her "Why would he insult me like that?!"
            m "So you're insulted because that boy refused to put his cock in your mouth?"
            $herView.hideQQ()
            $herView.data().addItem( 'tears', CharacterExItem( herView.mMiscFolder, "tears_02.png", G_Z_FACE + 1 ) )
            $herView.showQQ( "body_47.png", pos )
            her "Wouldn't you be, sir?"
            m "I think I would get over it rather quickly..."
            $herView.hideshowQQ( "body_187.png", pos )
            her "He rejected me sir..."
            her "Who does he think he is?!"
            $herView.hideshowQQ( "body_186.png", pos )
            her "With all due respect, sir, you wouldn't understand..."
            m "Well, in any case. I can't pay you for this."
            $herView.hideQQ()
            $herView.data().addItem( 'tears', CharacterExItem( herView.mMiscFolder, "tears_01.png", G_Z_FACE + 1 ) )
            $herView.showQQ( "body_79.png", pos )
            her "Of course... I would not expect you to, sir."
            her "I failed to complete my task and deserve no praise of any kind..."
            her "And should you pay me out of pity..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Then That would only worsen the insult..."
            m "Hm... In that case, maybe I should pay you anyway..."
            $herView.hideshowQQ( "body_79.png", pos )
            her "No, sir. I would not accept it..."
            m "Hm... Well, this will be all then."
            her "Have a good night, sir."
            $herView.hideQQ()
            $herView.data().delItem('tears')
            
            $ request_24_points += 1 
            $ request_24 = False 
            $ hermione_sleeping = True
            call music_block
            jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).

        elif one_out_of_three == 3: ### EVENT (C)
            #play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
            m "Miss Granger, how did it go?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_69.png", pos )
            her "I still find the idea of selling a favour like this appalling, sir."
            $herView.hideshowQQ( "body_79.png", pos )
            her "But other than that it well surprising well..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "I gave a proper blowjob to this handsome boy from \"Ravenclaw\"..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "And he was such a gentleman about it..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "He even warned me when he was about to cum."
            m "A true gentleman indeed."
            m "Did you swallow?"
            $herView.hideshowQQ( "body_120.png", pos )
            her "Of course I did, sir."
            her "I told you - I gave the boy a proper blowjob."
            $herView.hideshowQQ( "body_118.png", pos )
            her "The least I could do for someone who treated me with respect for a change..."
            m "Well, in that case."
            
    if whoring >= 21: # LEVEL 08 =+               
        if one_out_of_three == 1: ### EVENT (A)
            stop music fadeout 1.0
            # HERMIONE ALL MESSED UP, WITH RUNNING MASCARA.
            $herView.data().addItem( 'tears', CharacterExItem( herView.mMiscFolder, "tears_03.png", G_Z_FACE + 1 ) )
            $herView.data().addItem( 'sperm', CharacterExItem( herView.mMiscFolder, "sperm_05.png", G_Z_FACE + 2 ) )
            $herView.data().addItem( 'sperm_after', CharacterExItem( herView.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 3 ) )

            show screen blktone
            with d3
            $herView.hideshowQQ( "body_47.png", pos )
            show screen ctc
            pause
            hide screen ctc
            m "Miss Granger..."
            m "You look like hell..."
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $herView.hideshowQQ( "body_30.png", pos )
            her "Sir, I have been raped."
            m "Seriously?"
            $herView.hideshowQQ( "body_79.png", pos )
            her "Yes, sir."
            her "That nasty boy from \"Slytherin\" raped me..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "Or raped my face rather I suppose..."
            her "And--"
            $herView.hideshowQQ( "body_132.png", pos )
            play sound "sounds/burp.mp3"
            her "*Burp!*..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Excuse me."
            $herView.hideshowQQ( "body_86.png", pos )
            her "He came so much I was barely able to swallow it all..."
            her "Bloody bastard!"
            $herView.hideshowQQ( "body_187.png", pos )
            her "You think I could file a complaint, sir?"
            m "Hm... I suppose..."
            m "But keep in mind that the moment we bring the ministry into this..."
            m "All this \"favour selling business\" will have to stop immediately."
            $herView.hideshowQQ( "body_189.png", pos )
            her "Оh...?"
            her ".................."
            $herView.hideshowQQ( "body_74.png", pos )
            her "Please, never mind what I just said then..."
            m "Are you sure? You look pretty messed up."
            her "No, no. It's nothing really..."
            her "After all I was the one who offered him a free blowjob..."
            her "He just got a bit rough with me closer to the end, that's all..."
            her "I think I am just overreacting..."
            m "I see..."
            her "Can I just--"
            $herView.hideshowQQ( "body_48.png", pos )
            play sound "sounds/burp.mp3"
            her "*Burp!*..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Excuse me, sir."
            $herView.hideshowQQ( "body_34.png", pos )
            her "{size=-3}(He just kept on cumming... My stomach feels so full...){/size}"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Can I get my payment now, please?"
            
        elif one_out_of_three == 2: ### EVENT (B)
            # HERMIONE COVERED IN CUM
            label suked_off_them_both:
                pass
            stop music fadeout 1.0
            $herView.data().addItem( 'sperm', CharacterExItem( herView.mMiscFolder, "sperm_06.png", G_Z_FACE + 1 ) )
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_78.png", pos )
            show screen ctc
            pause
            hide screen ctc
            her "Good evening, sir..."
            g4 "Miss Granger?!"
            g4 "What happened to you, girl?"
            g4 "All I asked you to do was to give a blowjob to one of your classmates."
            $herView.hideshowQQ( "body_118.png", pos )
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "That... that was exactly what I did, sir."
            m "Girl, you are covered in cum head to toe."
            $herView.hideshowQQ( "body_121.png", pos )
            her "I am?"
            her "Oh... Did I forget to clean myself up?"
            $herView.hideshowQQ( "body_128.png", pos )
            her "How embarrassing..."
            her "That thing at the boy's restroom sort of escalated I suppose..."
            her "Before I knew what happened I was surrounded with hard throbbing cocks..."
            $herView.hideshowQQ( "body_133.png", pos )
            her "Oh... Just talking about it makes me shiver with excitement... err.."
            $herView.hideshowQQ( "body_136.png", pos )
            her "...I mean, with fear... no, not fear..."
            $herView.hideshowQQ( "body_188.png", pos )
            her "Embarrassment?"
            m "Are you asking me?"
            $herView.hideshowQQ( "body_123.png", pos )
            her "Oh, excuse me, sir... I feel a little lightheaded..."
            her "I think I need to go lie down for a while..."
            m "Don't forget to take a shower first."
            $herView.hideshowQQ( "body_128.png", pos )
            her "A shower? Why?"
            m "Never mind..."
            show screen ctc
            pause
            hide screen ctc


        elif one_out_of_three == 3: ### EVENT (C)
            if  suked_off_ron_and_har:
                jump suked_off_them_both
            else:
                 $ suked_off_ron_and_har = True #In public events. Give blowjob to a classmate. Event level 03. Event # 3. "Sukerd off Harrt and Ron". Turns True after that.


            m "MIss Granger, how did it go?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_74.png", pos )
            her "Splendid, sir. Simply splendid."
            m "Really? Do tell."
            $herView.hideshowQQ( "body_78.png", pos )
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Today I did something I wanted to do for such a long time now..."
            her "But never could muster up enough courage for..."
            m "Hm..?"
            $herView.hideshowQQ( "body_121.png", pos )
            her "Today I sucked off my two best friend in the entire world!"
            $herView.hideshowQQ( "body_124.png", pos )
            her "And it was every bit as exciting as I thought it would be."
            $herView.hideshowQQ( "body_123.png", pos )
            her "I made their cocks all sloppy with saliva..."
            her "I sucked on their balls too..."
            $herView.hideshowQQ( "body_134.png", pos )
            her "But the best part was to see their faces..."
            her "The boys could not believe it was actually happening..."
            $herView.hideshowQQ( "body_133.png", pos )
            her "To be honest, neither could I..."
            her "I, Hermione granger - the girl they knew for years..."
            $herView.hideshowQQ( "body_135.png", pos )
            her "Sucking on their cocks..."
            $herView.hideshowQQ( "body_139.png", pos )
            her "Like some nasty little slut..."
            m "Are you in love with those boys, girl?"
            $herView.hideshowQQ( "body_74.png", pos )
            her "I don't know, sir... Maybe..."
            her "Could I get paid now please?"
            m "Sure..."
            
            

    
    
    $ gryffindor += 65 #65
    m "The \"Gryffindor\" house gets 65 points!"
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


 


    $herView.data().loadState()

#    $ public_whore_ending = True #Activates "Public Whore" ending.
    $ end.SetEndingValue(const_ENDING_PUBLIC_WHORE,2)
    
    $ request_24_points += 1 
    $ request_24 = False 
    $ hermione_sleeping = True

    call music_block
    
    return


