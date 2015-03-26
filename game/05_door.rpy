label door:

    menu:
        "-Examine the door-" if not door_examined:
            $ door_examined = True
            hide screen genie
            $ tt_xpos=550
            $ tt_ypos=110
            show screen genie_stands
            show screen chair_02 #Empty chair near the desk.
            show screen desk
            with Dissolve(0.5)
            m "A sturdy looking door..."
            m "I wonder what's behind it."
            label examining_the_door:
            menu:
                "-Knock on the door-":
                    show screen blktone8
                    with d3
                    $ renpy.play('sounds/knocking.mp3')
                    "*Knock-knock-knock*"
                    "..................."
                    hide screen blktone8
                    with d3
                    m "No reply..."
                    jump examining_the_door
                "-Put your ear on it-":
                    show screen blktone8
                    with d3
                    ">You put your ear on the door and listen intently..."
                    m "I don't hear anything."
                    hide screen blktone8
                    with d3
                    jump examining_the_door
                "-Kick the door-":
                    show screen blktone8
                    with d3
                    $ renpy.play('sounds/kick.ogg')
                    pause.2
                    with hpunch
                    "*Thump!*"
                    ".............................."
                    hide screen blktone8
                    with d3
                    m "This door could take a thousand kicks like that and it still wouldn't break..." 
                    m "It doesn't look like it's locked though..."
                    jump examining_the_door
                "-Leave it alone-":
                    m "Who knows what kind of dangers could be lurking behind that door?"
                    m "I think I'll let it be for now..."
                    pass
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.2)
            jump day_main_menu
            
            
       
            
        "{color=#858585}-Summon Hermione-{/color}" if this.Has("her_summon")  and hermione_takes_classes or hermione_sleeping:#summoning_hermione_unlocked
            if hermione_takes_classes:
                show screen bld1
                with d3
                ">Hermione is taking classes."
                hide screen bld1
                with d3
                jump day_main_menu
            elif hermione_sleeping:
                show screen bld1
                with d3
                ">Hermione is already asleep."
                hide screen bld1
                with d3
                jump night_main_menu
        
        "-Summon Hermione-" if this.Has("her_summon") and not hermione_takes_classes and not hermione_sleeping: #summoning_hermione_unlocked 
     
            if hermione_takes_classes:
                show screen bld1
                with d3
                ">Hermione is taking classes."
                hide screen bld1
                with d3
                jump day_main_menu
            elif hermione_sleeping:
                show screen bld1
                with d3
                ">Hermione is already asleep."
                hide screen bld1
                with d3
                jump night_main_menu
                
            else:
                jump hermione_approaching
               
        "{color=#858585}- Позвать Снейпа -{/color}" if this.Has("snape_summon") and snape_busy:#hanging_with_snape
            ">Профессор Снейп недоступен."
            if daytime:
                jump day_main_menu
            else: 
                jump night_main_menu
            
        "-Summon Snape-" if this.Has("snape_summon") and not snape_busy:#hanging_with_snape
            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
            jump summon_snape
        "-Never mind-":
            jump day_main_menu                
                        

    
    
                
################
### LEVEL 01 ###                
###################REQUEST_01
label request_01: #LV.1 (Whoring = 0 - 2)
    "Hermione is looking at you with interest and blushes."
    "You dismiss Hermione."
    if hermi.whoring <= 2:
        $ hermi.whoring +=1
    $ gryffindor +=5
    "Gryffindor got +5 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

    
###################REQUEST_02 (Level 01)
label request_02:
    "Hermione reluctantly lifts her skirt and shows you her panties. She is blushing a lot."
    "You dismiss Hermione."
    if hermi.whoring <= 2:
        $ hermi.whoring +=1
    $ gryffindor +=5
    "Gryffindor got +5 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        

###################REQUEST_02_b (Level 01)
label request_02_b:
    "Hermione agrees to try and flirt with 3 classmates."
    "You dismiss Hermione."
    $ request_02_b = True
    if hermi.whoring <= 2:
        $ hermi.whoring +=1
    $ gryffindor +=5
    "Gryffindor got +5 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
label request_02_b_complete:
    "Hermione returns from her classes. She tells you about the guys she flirted with."
    $ request_02_b = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return
    
###################REQUEST_02_c (Level 01)
label request_02_c:
    "Hermione agrees to try and flirt with a teacher."
    "You dismiss Hermione."
    $ request_02_c = True
    if hermi.whoring <= 2:
        $ hermi.whoring +=1
    $ gryffindor +=5
    "Gryffindor got +5 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
label request_02_c_complete:
    "Hermione returns from her classes. She tells you about flirting with her teacher."
    $ request_02_c = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return    
    
    
################
### LEVEL 02 ###    
###################REQUEST_03 (Level 02) (Available during daytime only).
label request_03: #(Whoring = 3 - 5)
    if hermi.whoring <=2:
        jump too_much
        
    if hermi.whoring >= 3: #Level 02
        "Hermione hesitantly pulls her panties down and hands them over to you."
        "You dismiss Hermione."
        $ request_03 = True #True when Hermione has no panties on.
        if hermi.whoring <= 5:
            $ hermi.whoring +=1
        $ gryffindor +=15
        $ hermione_takes_classes = True
        "Gryffindor got +15 points."
        jump day_main_menu
        
label request_03_complete:
    "Hermione returns from her classes. You give her her panties back."
    $ request_03 = False #When False - you gave her her panties back.
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return


###################REQUEST_04 (Level 02) (Touch tits's through fabric.)
label request_04:
    if hermi.whoring <=2:
        jump too_much
    if hermi.whoring >= 3: #Level 02
        "Hermione lets you fondle her tits a little."
        "You dismiss Hermione."
        if hermi.whoring <= 5:
            $ hermi.whoring +=1
        $ gryffindor +=15
        "Gryffindor got +15 points."
        if daytime:
            $ hermione_takes_classes = True
            jump day_main_menu
        else:
            $ hermione_sleeping = True
            jump night_main_menu
            
###################REQUEST_05 (Level 02) (Touch butt through fabric.)
label request_05:
    if hermi.whoring <=2:
        jump too_much
    if hermi.whoring >= 3: #Level 02
        "Hermione lets you fondle her butt a little."
        "You dismiss Hermione."
        if hermi.whoring <= 5:
            $ hermi.whoring +=1
        $ gryffindor +=15
        "Gryffindor got +15 points."
        if daytime:
            $ hermione_takes_classes = True
            jump day_main_menu
        else:
            $ hermione_sleeping = True
            jump night_main_menu

###################REQUEST_06 (Level 02) (Flash panties to classmate.)
label request_06:
    if hermi.whoring <=2:
        jump too_much
    if hermi.whoring >= 3: #Level 02
        "Hermione agrees to try and flash her panties to a classmate."
        "You dismiss Hermione."
        $ request_05 = True
        if hermi.whoring <= 5:
            $ hermi.whoring +=1
        $ gryffindor +=15
        "Gryffindor got +15 points."
        $ hermione_takes_classes = True
        jump day_main_menu
       
label request_05_complete:
    "Hermione returns from classes. She tells you about her attempts to flash her panties to a classmate."
    $ request_05 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return
    

###################REQUEST_07 (Level 02) (Flash panties to a teacher).(Daytime only).
label request_07:
    if hermi.whoring <=2:
        jump too_much
    if hermi.whoring >= 3: #Level 02
        "Hermione agrees to try and flash her panties to a teacher."
        "You dismiss Hermione."
        $ request_06 = True
        if hermi.whoring <= 5:
            $ hermi.whoring +=1
        $ gryffindor +=15
        "Gryffindor got +15 points."
        $ hermione_takes_classes = True
        jump day_main_menu
        

label request_06_complete:
    "Hermione returns from her classes and tells you about her attempts to flash her panties to a teacher."
    $ request_06 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return
    
################
### LEVEL 03 ###
###################REQUEST_08 (Level 03) (Show me tits).
label request_08: #LV.3 (Whoring = 6 - 8)
    if hermi.whoring <=5:
        jump too_much
    "Hermione shows you her tits."
    "You dismiss Hermione."
    if hermi.whoring <= 8:
        $ hermi.whoring +=1
    $ gryffindor +=25
    "Gryffindor got +25 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_09 (Level 03) (Show me pussy).
label request_09: #LV.3 (Whoring = 6 - 8)
    if hermi.whoring <=5:
        jump too_much
    "Hermione shows you her pussy."
    "You dismiss Hermione."
    if hermi.whoring <= 8:
        $ hermi.whoring +=1
    $ gryffindor +=25
    "Gryffindor got +25 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_10 (Level 03) (25 pt.) (Flash nipple to a classmate). (Available during daytime only).
label request_10:
    if hermi.whoring <=5:
        jump too_much
    "Hermione agrees to try and flash her nipple to a classmate."
    "You dismiss Hermione."
    $ request_10 = True 
    if hermi.whoring <= 8:
        $ hermi.whoring +=1
    $ gryffindor +=25
    $ hermione_takes_classes = True
    "Gryffindor got +25 points."
    jump day_main_menu
        
label request_10_complete:
    "Hermione returns from classes. She tells you how she flashed her nipple to a classmate."
    $ request_10 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return

################
### LEVEL 04 ###
###################REQUEST_11 (Level 04) (Get naked.) (Day/Night)
label request_11: #LV.4 (Whoring = 9 - 11)
    if hermi.whoring <=8:
        jump too_much
    "Hermione undresses before you and Then puts her clothes back on."
    "You dismiss Hermione."
    if hermi.whoring <= 11:
        $ hermi.whoring +=1
    $ gryffindor +=35
    "Gryffindor got +35 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_12 (Level 04) (Play with her tits.) (Day/Night)
label request_12: #LV.4 (Whoring = 9 - 11)
    if hermi.whoring <=8:
        jump too_much
    "Hermione bares her tits. You play with them for a while."
    "You dismiss Hermione."
    if hermi.whoring <= 11:
        $ hermi.whoring +=1
    $ gryffindor +=35
    "Gryffindor got +35 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_13 (Level 04) (35 pt.) (Wear see-though shirt to classes). (Available during daytime only).
label request_13: #LV.4 (Whoring = 9 - 11)
    if hermi.whoring <=8:
        jump too_much
    "Hermione agrees to put on a see-through shirt and go to class."
    "You dismiss Hermione."
    $ request_13 = True 
    if hermi.whoring <= 11:
        $ hermi.whoring +=1
    $ gryffindor +=35
    $ hermione_takes_classes = True
    "Gryffindor got +35 points."
    jump day_main_menu
        
label request_13_complete:
    "Hermione returns from her classes and tells you how everyone was starring at her tits today."
    $ request_13 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return

###################REQUEST_15 (Level 04) (35 pt.) (Flash a nipple to a teacher). (Available during daytime only).
label request_15: #LV.4 (Whoring = 9 - 11)
    if hermi.whoring <=8:
        jump too_much
    "Hermione agrees to try and flash a nipple to a teacher."
    "You dismiss Hermione."
    $ request_15 = True 
    if hermi.whoring <= 11:
        $ hermi.whoring +=1
    $ gryffindor +=35
    $ hermione_takes_classes = True
    "Gryffindor got +35 points."
    jump day_main_menu
        
label request_15_complete:
    "Hermione returns from her classes. She tells you how she flashed her nipples to a teacher."
    $ request_15 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return

################
### LEVEL 05 ###   
###################REQUEST_16 (Level 05) (Finger her pussy) (Day/Night)
label request_16: #LV.5 (Whoring = 12 - 14)
    if hermi.whoring <=11:
        jump too_much
    "Hermione lets you finger her pussy."
    "You dismiss Hermione."
    if hermi.whoring <= 14:
        $ hermi.whoring +=1
    $ gryffindor +=45
    "Gryffindor got +45 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_17 (Level 05) (Stick a finger up her but thole.) (Day/Night)
label request_17: #LV.5 (Whoring = 12 - 14)
    if hermi.whoring <=11:
        jump too_much
    "Hermione lets you stick a finger up her butthole."
    "You dismiss Hermione."
    if hermi.whoring <= 14:
        $ hermi.whoring +=1
    $ gryffindor +=45
    "Gryffindor got +45 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


###################REQUEST_18 (Level 05) (Handjob) (Day/Night)
label request_18: #LV.5 (Whoring = 12 - 14)
    if hermi.whoring <=11:
        jump too_much
    "Hermione gives you a handjob."
    "You dismiss Hermione."
    if hermi.whoring <= 14:
        $ hermi.whoring +=1
    $ gryffindor +=45
    "Gryffindor got +45 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_19 (Level 05) (Rub your dick against her cheeks.) (Day/Night)
label request_19: #LV.5 (Whoring = 12 - 14)
    if hermi.whoring <=11:
        jump too_much
    "Hermione sits still while you rub your cock against her face."
    "You dismiss Hermione."
    if hermi.whoring <= 14:
        $ hermi.whoring +=1
    $ gryffindor +=45
    "Gryffindor got +45 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_20 (Level 05) (45 pt.) (Grab a classmate's cock). (Available during daytime only).
label request_20: #LV.5 (Whoring = 12 - 14)
    if hermi.whoring <=11:
        jump too_much
    "Hermione agrees to try and grab a classmate's cock."
    "You dismiss Hermione."
    $ request_20 = True 
    if hermi.whoring <= 14:
        $ hermi.whoring +=1
    $ gryffindor +=45
    $ hermione_takes_classes = True
    "Gryffindor got +45 points."
    jump day_main_menu
        
label request_20_complete:
    "Hermione returns from her classes and tells you how she grabbed the cock of one of her classmates."
    $ request_20 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then, Sir."
    return
    
###################REQUEST_21 (Level 06) (55 pt.) (Cum on tits). 
#As this request levels up, there are an option appears to offer some extra points if Hermione will put her clothes
#on top of her sperm covered tits and go to classes like that.
label request_21: #LV.6 (Whoring = 15 - 17)
    if hermi.whoring <=14:
        jump too_much
    "Hermione bares her tits. You jerk off and cum all over them."
    "You dismiss Hermione."
    if hermi.whoring <= 17:
        $ hermi.whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "Gryffindor got +55 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_22 (Level 06) (55 pt.) (Blowjob). 
label request_22: #LV.6 (Whoring = 15 - 17)
    if hermi.whoring <=14:
        jump too_much
    "Hermione gives you a blowjob."
    "You dismiss Hermione."
    if hermi.whoring <= 17:
        $ hermi.whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "Gryffindor got +55 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_23 (Level 06) (55 pt.) (Give handjob to a classmate). (Available during daytime only).
label request_23: #LV.6 (Whoring = 15 - 17)
    if hermi.whoring <=14:
        jump too_much
    "Hermione agrees to try and give a handjob to a classmate."
    "You dismiss Hermione."
    $ request_23 = True 
    if hermi.whoring <= 17:
        $ hermi.whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "Gryffindor got +55 points."
    jump day_main_menu
        
label request_23_complete:
    "Hermione returns from her classes and tells you how she gave a handjob to one of her classmates during class."
    $ request_23 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then, Sir."
    return

###################REQUEST_24 (Level 06) (55 pt.) (Flash your tits to a teacher). (Available during daytime only).
label request_24: #LV.6 (Whoring = 15 - 17)
    if hermi.whoring <=14:
        jump too_much
    "Hermione agrees to try and flash her tits to a teacher."
    "You dismiss Hermione."
    $ request_24 = True 
    if hermi.whoring <= 17:
        $ hermi.whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "Gryffindor got +55 points."
    jump day_main_menu
        
label request_24_complete:
    "Hermione returns from her classes. She tells you how she flashed her tits to a teacher."
    $ request_24 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then, Sir."
    return
    
###################REQUEST_25 (Level 07) (65 pt.) (Cum on face). 
label request_25: #LV.7 (Whoring = 18 - 20)
    if hermi.whoring <=17:
        jump too_much
    "Hermione sits still while you jerk off in her face."
    "You dismiss Hermione."
    if hermi.whoring <= 20:
        $ hermi.whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "Gryffindor got +65 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_26 (Level 07) (65 pt.) (Cum in open mouth before class). (Available during daytime only).
label request_26: #LV.7 (Whoring = 18 - 20)
    if hermi.whoring <=17:
        jump too_much
    
    "Hermione sits still with her mouth wide open while you jerk off and cum in it. You tell her to only swallow it when she gets to class."
    "You dismiss Hermione with her mouth full of your cum."
    
    $ request_26 = True 
    if hermi.whoring <= 20:
        $ hermi.whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "Gryffindor got +65 points."
    jump day_main_menu
        
label request_26_complete:
    "Hermione returns from her classes and tells you that she couldn't speak to her classmates because her mouth was filled with your cum."
    $ request_26 = False 
    $ hermione_sleeping = True
    her "Oh, alright, Sir. I will go to bed then."
    return

###################REQUEST_27 (Level 07) (65 pt.) (Blow two classmates). (Available during daytime only).
label request_27: #LV.7 (Whoring = 18 - 20)
    if hermi.whoring <=17:
        jump too_much
    "Hermione agrees to try and blow two classmates during classes."
    "You dismiss Hermione."
    $ request_27 = True 
    if hermi.whoring <= 20:
        $ hermi.whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "Gryffindor got +65 points."
    jump day_main_menu
        
label request_27_complete:
    "Hermione returns from her classes. She tells you how she gave a blowjob to two classmates during classes."
    $ request_27 = False 
    $ hermione_sleeping = True
    her "Oh, alright, Sir. I will go to bed then."
    return

###################REQUEST_28 (Level 07) (65 pt.) (Give handjob to a teacher). (Available during daytime only).
label request_28: #LV.7 (Whoring = 18 - 20)
    if hermi.whoring <=17:
        jump too_much
    "Hermione agrees to try and give a handjob to a teacher during classes."
    "You dismiss Hermione."
    $ request_28 = True 
    if hermi.whoring <= 20:
        $ hermi.whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "Gryffindor got +65 points."
    jump day_main_menu
        
label request_28_complete:
    "Hermione returns from classes and tells you how she gave a handjob to a teacher during classes."
    $ request_28 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then, Sir."
    return
    
################
### LEVEL 08 ###
###################REQUEST_29 (Level 08) (75 pt.) (Sex). 
label request_29: #LV.8 (Whoring = 21 - 23)
    if hermi.whoring <=20:
        jump too_much
    if daytime:
        "You have sex with Hermione and send her to her classes afterwards."
    else:
        "You have sex with Hermione."
        "You send her to bed."
    if hermi.whoring <= 23:
        $ hermi.whoring +=1
    $ gryffindor +=75
    "Gryffindor got +75 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_30 (Level 08) (75 pt.) (Blow a teacher). (Available during daytime only).
label request_30: #LV.8 (Whoring = 21 - 23)
    if hermi.whoring <=20:
        jump too_much
    "Hermione agrees to try and blow a teacher."
    "You dismiss Hermione."
    $ request_30 = True 
    if hermi.whoring <= 23:
        $ hermi.whoring +=1
    $ gryffindor +=75
    $ hermione_takes_classes = True
    "Gryffindor got +75 points."
    jump day_main_menu
        
label request_30_complete:
    "Hermione returns from her classes. She tells you how she gave a blowjob to a teacher during classes."
    $ request_30 = False 
    $ hermione_sleeping = True
    her "Oh, alright, Sir. I will go to bed then, Sir."
    return

################
### LEVEL 09 ###
###################REQUEST_31 (Level 09) (85 pt.) (Anal sex). (Nighttime)
label request_31: #LV.9 (Whoring = 24 - 26)
    if hermi.whoring <=23:
        jump too_much
    "You have anal sex with Hermione."
    "You order her to go to bed afterwards."
    if hermi.whoring <= 26:
        $ hermi.whoring +=1
    $ gryffindor +=85
    "Gryffindor got +85 points."
    $ hermione_sleeping = True
    jump day_start


################
### LEVEL 10 ###
###################REQUEST_32 (Level 10) (100 pt.) (Wear a very revealing outfit to class). (Daytime only)
label request_32: #LV.10 (Whoring = 27 - 29)
    if hermi.whoring <=26:
        jump too_much
    "Hermione puts on a very slutty outfit and goes to her classes."
    $ request_32 = True
    if hermi.whoring <= 29:
        $ hermi.whoring +=1
    $ gryffindor +=100
    $ hermione_takes_classes = True
    "Gryffindor got +100 points."
    jump day_main_menu

label request_32_complete:
    "Hermione returns from classes. She tells you that people treated her like a whore today."
    $ request_32 = False 
    $ hermione_sleeping = True
    her "Oh, as you wish, Sir. I will go to bed then, Sir."
    return

###################REQUEST_33 (Level 10) (100 pt.) THIS REQUEST IS NOW CAN ONLY BE ACCESSED THROUGH REQUEST_25 (CUM ON FACE) when hermi.whoring > 26. (Go to class with cum on your face). (Daytime only)
label request_33: #LV.10 (Whoring = 27 - 29)
    if hermi.whoring <=26:
        jump too_much
    "You cum all over hermione's face and send her to her classes."
    $ request_33 = True
    if hermi.whoring <= 29:
        $ hermi.whoring +=1
    $ gryffindor +=100
    $ hermione_takes_classes = True
    "Gryffindor got +100 points."
    jump day_main_menu

label request_33_complete:
    "Hermione returns from her classes. She tells you that people treated her like trash and laughed at her today."
    $ request_33 = False 
    $ hermione_sleeping = True
    her "Oh, as you wish, Sir. I will go to bed then, Sir."
    return





#############This massage shows when you make a request, and Hermione refuses because she is not slutty enough yet.
label too_much:
    if IsEventOnlyAfter("new_personal_request"): # Если попали сюда после ивента, запущенного через меню "new_personal_request", значит ивент не завершен
        $event.NotFinished()
    stop music fadeout 2.0
    $herView.hideQQ()
    $ pos = POS_120
    $herView.showQQ( "body_48.png", pos )
    her "Professor Dumbledore??!"
    her "How could ask for such a thing!?"
    $herView.hideQQ()
    $herView.showQQ( "body_34.png", pos )
    her "I think I better leave."

    hide screen blktone
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ hermione_chibi_xpos = 610 #Near the desk.
    with Dissolve(.3)    
    
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    
    $ hermi.liking -= 7
    
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


