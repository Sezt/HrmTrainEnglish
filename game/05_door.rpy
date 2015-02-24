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
            
            
       
            
        "{color=#858585}- Summon Hermione -{/color}" if this.Has("her_summon")  and hermione_takes_classes or hermione_sleeping:#summoning_hermione_unlocked
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
        
        "- Summon Hermione -" if this.Has("her_summon") and not hermione_takes_classes and not hermione_sleeping: #summoning_hermione_unlocked 
     
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
                #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                #stop music fadeout 2.0
                
                $ menu_x = 0.2 #Menu is moved to the left side.
                $ pos = POS_410
                
                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                show screen bld1
                with d3
                if mad >=1 and mad < 3:
                    $herView.showQQ( "body_03.png", pos )
                    her ">Looks like Hermione is still a little upset with you..."
                elif mad >=3 and mad < 10:
                    $herView.showQQ( "body_03.png", pos )
                    ">Hermione is upset with you."
                elif mad >=10 and mad < 20:
                    $herView.showQQ( "body_09.png", pos )
                    ">Hermione is very upset with you."
                elif mad >=20 and mad < 40:
                    $herView.showQQ( "body_05.png", pos )
                    ">Hermione is mad at you."
                elif mad >=40 and mad < 50:
                    $herView.showQQ( "body_47.png", pos )
                    ">Hermione is very mad at you."
                elif mad >=50 and mad < 60:
                    $herView.showQQ( "body_47.png", pos )
                    ">Hermione is furious at you."
                elif mad >=60:
                    $herView.showQQ( "body_47.png", pos )
                    ">Hermione hates your guts."
                else:
                    $herView.showQQ( "body_01.png", pos )
                    her "Yes, professor?"
                
                label day_time_requests:
                menu:
                    "- Chit chat -" if not chitchated_with_her:
                        $ chitchated_with_her = True #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
                        if mad <= 7:
                            jump chit_chat
                        else:
                            her "I have nothing to say to you sir..."    
                            jump day_time_requests
                    "- Tutoring -" if not daytime and not tut_happened and whoring <= 12:
                        if mad >=1 and mad < 3:
                            her "I'm sorry, maybe tomorrow..."
                            jump day_time_requests
                        elif mad >=3 and mad < 10:
                            her "I am not in the mood today..."
                            jump day_time_requests
                        elif mad >=20:
                            her "After what you did, professor?"
                            her "I don't think so..."
                            jump day_time_requests
                        else:
                            jump tutoring
                    "- Buy \"sexual\" favours -" if this.Has("her_wants_buy"):#buying_favors_from_hermione_unlocked:
                        if mad >=1 and mad < 3:
                            her "I'm sorry, professor, Maybe some other time..."
                        elif mad >=3 and mad < 10:
                            her "I don't feel like it today..."
                            her "Maybe in a couple of days..."
                        elif mad >=10 and mad < 20:
                            her "No thank you...."
                        elif mad >=20 and mad < 30:
                            her "After what you did, professor?"
                            her "I don't think so..."
                        elif mad >=30 and mad < 40:
                            her "You can't be serious!"
                        elif mad >=40:
                            her "Is this some twisted joke to you, sir?!"
                            her "After what you did I don't feel like doing this ever again!"
                        if mad==0:
                            jump new_personal_request
                        else:
                            jump day_time_requests
                   
                    
                    
                    
                    "-Give her a present-" if not gifted:
                        menu:
                            "-A lollipop candy-([candy])" if candy >= 1:
                                $ gifted = True 
                                jump giving_candy #28_gifts.rpy
                                
                            "-Chocolate-([chocolate])" if chocolate >= 1:
                                $ gifted = True 
                                jump giving_chocolate #28_gifts.rpy
                            
                            "-Stuffed Owl-([owl])" if owl >= 1:
                                $ gifted = True 
                                jump giving_owl #28_gifts.rpy
                                
                            "-Butterbeer-([beer])" if beer >= 1:
                                $ gifted = True 
                                jump giving_beer #28_gifts.rpy
                                
                            "-Educational magazines-([mag1])" if mag1 >= 1:
                                $ gifted = True 
                                jump giving_mag1 #28_gifts.rpy
                                
                            "-Girly magazines-([mag2])" if mag2 >= 1:
                                $ gifted = True 
                                jump giving_mag2 #28_gifts.rpy
                                
                            "-Adult magazines-([mag3])" if mag3 >= 1:
                                $ gifted = True 
                                jump giving_mag3 #28_gifts.rpy
                                
                            "-Porn magazines-([mag4])" if mag4 >= 1:
                                $ gifted = True 
                                jump giving_mag4 #28_gifts.rpy
                            
                            "-Viktor Krum Poster-([krum])" if krum >= 1:
                                $ gifted = True 
                                jump giving_krum #28_gifts.rpy
                            
                            "-Sexy lingerie-([lingerie])" if lingerie >= 1:
                                $ gifted = True 
                                jump giving_lingerie #28_gifts.rpy
                            
                            "-A pack of condoms-([condoms])" if condoms >= 1:
                                $ gifted = True 
                                jump giving_condoms #28_gifts.rpy
                                
                            "-A jar of anal lubricant-([anal_lube])" if anal_lube >= 1:
                                $ gifted = True 
                                jump giving_lube #28_gifts.rpy
                            
                            "-A vibrator-([vibrator])" if vibrator >= 1:
                                $ gifted = True 
                                jump giving_vibrator #28_gifts.rpy
                            
                            "-Ball gag and cuffs -([ballgag])" if ballgag >= 1:
                                $ gifted = True 
                                jump giving_ballgag #28_gifts.rpy
                                
                            "-Anal plugs -([plug])" if plug >= 1:
                                $ gifted = True 
                                jump giving_plug #28_gifts.rpy
                                
                            "- A Thestral strap-on -([strapon])" if strapon >= 1:
                                $ gifted = True 
                                jump giving_strapon #28_gifts.rpy
                            
                            "- Lady Speed Stick-2000 -([broom])" if broom >= 1:
                                $ gifted = True 
                                jump giving_broom #28_gifts.rpy
                                
                            "- Sex doll \"Joanne\" -([sexdoll])" if sexdoll >= 1:
                                $ gifted = True 
                                jump giving_sexdoll #28_gifts.rpy
                            
                            "-School miniskirt-" if have_miniskirt: # Turns TRUE when you have the skirt in your possession.
                                $ gifted = True
                                jump giving_skirt #28_gifts.rpy
                            
                            "-\"S.P.E.W.\" badge-" if badge_01 == 1:
                                $ gifted = True
                                jump giving_badge_01 #28_gifts.rpy
                            
                            "-Fishnet stockings-" if nets == 1:
                                $ gifted = True
                                jump giving_nets #28_gifts.rpy
                                
                                
                                
                                
                            "- The Ball Dress -" if "ball_dress" in gifts12 and not gave_the_dress:
                                show screen  blktone
                                with d3
                                m "(I have the feeling that there will be no turning back for me after I give her this dress...)"
                                m "(Am I ready for this?)"
                                hide screen blktone
                                menu:
                                    "\"Yes, I am...\"":
                                        jump giving_thre_dress #27_final_events.rpy
                                    "\"No, not yet...\"":
                                        jump day_time_requests
                            "- Never mind -":
                                jump day_time_requests
                
                    
                    # "- Ending \"Your whore\"- ":
                        #jump your_whore
                        
                    # "- Ending \"Public whore\"- ":
                        # $ public_whore_ending = True #If TRUE the game will end with "Public Whore Ending".
                        # jump your_whore
                        
                    "- Wardrobe -" if dress_code:
                        if mad >=1 and mad < 3:
                            her "I'm sorry, professor. Maybe some other time..."
                            jump day_time_requests
                        elif mad >=3 and mad < 10:
                            her "What's wrong with my current attire?"
                            jump day_time_requests
                        elif mad >=10 and mad < 20:
                            her "No, thank you...."
                            jump day_time_requests
                        elif mad >=20 and mad < 30:
                            her "I don't think so..."
                            jump day_time_requests
                        elif mad >=30 and mad < 40:
                            her "No!"
                            jump day_time_requests
                        elif mad >=40:
                            her "I will never let you tell me what to wear again, sir!"
                            jump day_time_requests
                        else:
                            pass
                        menu:
                            
                            "- Put the badge on -" if (herView.data().getItem( G_N_BADGE )==None) and  badge_01 == 7: #not ba_01 and badge_01 == 7:
                                jump badge_put
                            
                            "- Take the badge off -" if (herView.data().getItem( G_N_BADGE )!=None) and  badge_01 == 7: #ba_01 and badge_01 == 7:
                                jump badge_take
                            
                            "- Put the fishnets on -" if (herView.data().getItem( G_N_NETS )==None) and  nets == 7: #not ne_01 and nets == 7: # Не перевел
                                jump nets_put
                            
                            "- Take the fishnets off -" if (herView.data().getItem( G_N_NETS )!=None) and  nets == 7: #ne_01 and nets == 7:
                                jump nets_take
                            
                            "- Put the miniskirt on -" if herView.data().checkItem( G_N_SKIRT, 'skirt_normal.png' ) and gave_miniskirt: #not legs_02 and gave_miniskirt: #Turns True when Hermione has the miniskirt.:
                                jump mini_on #28_gifts.rpy

                            "- Put the long skirt on -" if herView.data().checkItem( G_N_SKIRT, 'skirt_short.png' ) and gave_miniskirt: #legs_02 and gave_miniskirt: #Turns True when Hermione has the miniskirt.
                                jump mini_off #28_gifts.rpy
                            
                           
  
                            "- Never mind -":
                                jump day_time_requests
                    
                        
#                    "- Personal requests (lv.1)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Stand there. (I touch myself.)(5pt.)": #Request_01 (Level 01)
#                                    jump request_01
#                                "Lift your skirt.(5pt.)": #Request_02 (Level 01)
#                                    jump request_02
#                                "Flirt with 3 classmates.(5pt.)" if daytime: #Request_02_b (Level 01)
#                                    jump request_02_b
#                                "Flirt with a teacher.(5pt.)" if daytime:  #Request_02_c (Level 01)
#                                    jump request_02_c
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
#                    ###LEVEL 02###    
#                    "- Personal requests (lv.2)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Take her panties.(15pt.)" if daytime: #Request_03 (Level 02)
#                                    jump request_03
#                                "Touch her tits through her clothes. (15pt)": #Request_04 (Level 02)
#                                    jump request_04
#                                "Touch her butt though her clothes.(15pt)": #Request_05 (Level 02)
#                                    jump request_05
#                                "Flash panties to a classmate. (15pt)" if daytime: #Request_06 (Level 02)
#                                    jump request_06
#                                "Flash panties to a teacher.(15pt)" if daytime: #Request_07 (Level 02)
#                                    jump request_07
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
#                    ###LEVEL 03###
#                    "- Personal requests (lv.3)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Show me your tits. (25pt)":#Request_08 (Level 03)
#                                    jump request_08
#                                "Show me your pussy.(25pt)":#Request_09 (Level 03):
#                                    jump request_09
#                                "Flash a nipple to a classmate. (25pt)." if daytime:#Request_10 (Level 03)
#                                    jump request_10
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
                                    
#                    ###LEVEL 04###
#                    "- Personal requests (lv.4)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Strip completely.(35pt)":#Request_11 (Level 04)
#                                    jump request_11
#                                "Play with her tits.(35pt)":#Request_12 (Level 04):
#                                    jump request_12   
#                                "Wear a see-through shirt.(35pt)" if daytime:#Request_13 (Level 04):
#                                    jump request_13   
#                                "wear Cum-soaked panties": #Request_14 (Level 04) #To be added later when ability to jerk off and cum on panties added.
#                                    pass
#                                "Flash a nipple to a teacher.(35pt)" if daytime:#Request_15 (Level 04):
#                                    jump request_15   
#                                "Cancel.":
#                                    jump day_time_requests                    
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
#                    ###LEVEL 05###
#                    "- Personal requests (lv.5)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Finger her pussy.(45pt)":#Request_16 (Level 05)
#                                    jump request_16
#                                "Finger her butthole.(45pt)":#Request_17 (Level 05)
#                                    jump request_17
#                                "Handjob.(45pt)":#Request_18 (Level 05)
#                                    jump request_18
#                                "Rub your dick against her cheeks.(45pt)": #Request_19 (Level 05)
#                                    jump request_19
#                                "Grab a classmate's cock.(45pt)" if daytime: #Request_20 (Level 05)
#                                    jump request_20
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
                     
#                    ###LEVEL 06###
#                    "- Personal requests (lv.6)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Cum on tits.(55pt)":#Request_21 (Level 06)
#                                    jump request_21
#                                "Blowjob.(55pt)":#Request_22 (Level 06)
#                                    jump request_22
#                                "Give a handjob to a classmate.(55pt)" if daytime:#Request_23 (Level 06)
#                                    jump request_23
#                                "Flash your tits to a teacher.(55pt)" if daytime:#Request_24 (Level 06)
#                                    jump request_24
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests 
                    
#                    ###LEVEL 07###
#                    "- Personal requests (lv.7)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Cum on face.(65pt)":#Request_25 (Level 07)
#                                    jump request_25
#                                "Cum in her mouth before class.(65pt)" if daytime:#Request_26 (Level 07)
#                                    jump request_26
#                                "Blow two classmates.(65pt)" if daytime:#Request_27 (Level 07)
#                                    jump request_27
#                                "Give a handjob to a teacher.(65pt)" if daytime:#Request_28 (Level 07)
#                                    jump request_28
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests  
                            
#                    ###LEVEL 08###
#                    "- Personal requests (lv.8)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Sex.(75pt)":#Request_29 (Level 08)
#                                    jump request_29
#                                "Blow a teacher.(75pt)" if daytime: #Request_30 (Level 08)
#                                    jump request_30
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests 
                    
#                    ###LEVEL 09###
#                    "- Personal requests (lv.9)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Anal sex.(85pt)" if not daytime:#Request_31 (Level 09)
#                                    jump request_31
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests 
                    
#                    ###LEVEL 10###
#                    "- Personal requests (lv.10)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Wear a revealing outfit to class.(100pt)" if daytime:#Request_32 (Level 10)
#                                    jump request_32
#                                "Cum covered face.(100pt)" if daytime:#Request_33 (Level 10)
#                                    jump request_33
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests 
                    
                    
                    
                    "-Dismiss her-":
#                        if daytime:
#                            play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
#                        else:
#                            play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
                        $ menu_x = 0.5 #Menu position is back to default. (Center).
                        if daytime:
                            $ hermione_takes_classes = True
                            if mad >=3 and mad <= 6:
                                her "..............................."
                            elif mad >=7:
                                her "*Humph!*..."
                            else:
                                her "Oh, alright. I will go to classes then."
                            hide screen bld1
                            $herView.hideQ() 
                            hide screen blktone 
                            hide screen hermione_02
                            hide screen ctc
                            with d3
                            jump day_main_menu
                        else:
                            if mad >=3 and mad <= 6:
                                her "..............................."
                            elif mad >=7:
                                her "Tch..."
                            else:
                                her "Oh, alright. I will go to bed then."
                            hide screen bld1
                            $herView.hideQ()
                            hide screen blktone 
                            hide screen hermione_02
                            hide screen ctc
                            with d3
                            $ hermione_sleeping = True
                            jump night_main_menu
                            
                            
            
        "{color=#858585}- Summon Snape -{/color}" if this.Has("snape_summon") and snape_busy:#hanging_with_snape
            ">Professor Snape is unavailable."
            if daytime:
                jump day_main_menu
            else: 
                jump night_main_menu
            
        "- Summon Snape -" if this.Has("snape_summon") and not snape_busy:#hanging_with_snape
            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
            jump summon_snape
        "- Never mind -":
            jump day_main_menu
    
    
                
################
### LEVEL 01 ###                
###################REQUEST_01
label request_01: #LV.1 (Whoring = 0 - 2)
    "Hermione is looking at you with interest and blushes."
    "You dismiss Hermione."
    if whoring <= 2:
        $ whoring +=1
    $ gryffindor +=5
    "gryffindor got +5 points."
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
    if whoring <= 2:
        $ whoring +=1
    $ gryffindor +=5
    "gryffindor got +5 points."
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
    if whoring <= 2:
        $ whoring +=1
    $ gryffindor +=5
    "gryffindor got +5 points."
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
    if whoring <= 2:
        $ whoring +=1
    $ gryffindor +=5
    "gryffindor got +5 points."
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
    if whoring <=2:
        jump too_much
        
    if whoring >= 3: #Level 02
        "Hermione hesitantly pulls her panties down and hands them over to you."
        "You dismiss Hermione."
        $ request_03 = True #True when Hermione has no panties on.
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        $ hermione_takes_classes = True
        "gryffindor got +15 points."
        jump day_main_menu
        
label request_03_complete:
    "Hermione returns from her classes. You give her her panties back."
    $ request_03 = False #When False - you gave her her panties back.
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return


###################REQUEST_04 (Level 02) (Touch tits's through fabric.)
label request_04:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        "Hermione lets you fondle her tits a little."
        "You dismiss Hermione."
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        "gryffindor got +15 points."
        if daytime:
            $ hermione_takes_classes = True
            jump day_main_menu
        else:
            $ hermione_sleeping = True
            jump night_main_menu
            
###################REQUEST_05 (Level 02) (Touch butt through fabric.)
label request_05:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        "Hermione lets you fondle her butt a little."
        "You dismiss Hermione."
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        "gryffindor got +15 points."
        if daytime:
            $ hermione_takes_classes = True
            jump day_main_menu
        else:
            $ hermione_sleeping = True
            jump night_main_menu

###################REQUEST_06 (Level 02) (Flash panties to classmate.)
label request_06:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        "Hermione agrees to try and flash her panties to a classmate."
        "You dismiss Hermione."
        $ request_05 = True
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        "gryffindor got +15 points."
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
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        "Hermione agrees to try and flash her panties to a teacher."
        "You dismiss Hermione."
        $ request_06 = True
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        "gryffindor got +15 points."
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
    if whoring <=5:
        jump too_much
    "Hermione shows you her tits."
    "You dismiss Hermione."
    if whoring <= 8:
        $ whoring +=1
    $ gryffindor +=25
    "gryffindor got +25 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_09 (Level 03) (Show me pussy).
label request_09: #LV.3 (Whoring = 6 - 8)
    if whoring <=5:
        jump too_much
    "Hermione shows you her pussy."
    "You dismiss Hermione."
    if whoring <= 8:
        $ whoring +=1
    $ gryffindor +=25
    "gryffindor got +25 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_10 (Level 03) (25 pt.) (Flash nipple to a classmate). (Available during daytime only).
label request_10:
    if whoring <=5:
        jump too_much
    "Hermione agrees to try and flash her nipple to a classmate."
    "You dismiss Hermione."
    $ request_10 = True 
    if whoring <= 8:
        $ whoring +=1
    $ gryffindor +=25
    $ hermione_takes_classes = True
    "gryffindor got +25 points."
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
    if whoring <=8:
        jump too_much
    "Hermione undresses before you and Then puts her clothes back on."
    "You dismiss Hermione."
    if whoring <= 11:
        $ whoring +=1
    $ gryffindor +=35
    "gryffindor got +35 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_12 (Level 04) (Play with her tits.) (Day/Night)
label request_12: #LV.4 (Whoring = 9 - 11)
    if whoring <=8:
        jump too_much
    "Hermione bares her tits. You play with them for a while."
    "You dismiss Hermione."
    if whoring <= 11:
        $ whoring +=1
    $ gryffindor +=35
    "gryffindor got +35 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_13 (Level 04) (35 pt.) (Wear see-though shirt to classes). (Available during daytime only).
label request_13: #LV.4 (Whoring = 9 - 11)
    if whoring <=8:
        jump too_much
    "Hermione agrees to put on a see-through shirt and go to class."
    "You dismiss Hermione."
    $ request_13 = True 
    if whoring <= 11:
        $ whoring +=1
    $ gryffindor +=35
    $ hermione_takes_classes = True
    "gryffindor got +35 points."
    jump day_main_menu
        
label request_13_complete:
    "Hermione returns from her classes and tells you how everyone was starring at her tits today."
    $ request_13 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return

###################REQUEST_15 (Level 04) (35 pt.) (Flash a nipple to a teacher). (Available during daytime only).
label request_15: #LV.4 (Whoring = 9 - 11)
    if whoring <=8:
        jump too_much
    "Hermione agrees to try and flash a nipple to a teacher."
    "You dismiss Hermione."
    $ request_15 = True 
    if whoring <= 11:
        $ whoring +=1
    $ gryffindor +=35
    $ hermione_takes_classes = True
    "gryffindor got +35 points."
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
    if whoring <=11:
        jump too_much
    "Hermione lets you finger her pussy."
    "You dismiss Hermione."
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    "gryffindor got +45 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_17 (Level 05) (Stick a finger up her but thole.) (Day/Night)
label request_17: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Hermione lets you stick a finger up her butthole."
    "You dismiss Hermione."
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    "gryffindor got +45 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


###################REQUEST_18 (Level 05) (Handjob) (Day/Night)
label request_18: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Hermione gives you a handjob."
    "You dismiss Hermione."
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    "gryffindor got +45 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_19 (Level 05) (Rub your dick against her cheeks.) (Day/Night)
label request_19: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Hermione sits still while you rub your cock against her face."
    "You dismiss Hermione."
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    "gryffindor got +45 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_20 (Level 05) (45 pt.) (Grab a classmate's cock). (Available during daytime only).
label request_20: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Hermione agrees to try and grab a classmate's cock."
    "You dismiss Hermione."
    $ request_20 = True 
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    $ hermione_takes_classes = True
    "gryffindor got +45 points."
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
    if whoring <=14:
        jump too_much
    "Hermione bares her tits. You jerk off and cum all over them."
    "You dismiss Hermione."
    if whoring <= 17:
        $ whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "gryffindor got +55 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_22 (Level 06) (55 pt.) (Blowjob). 
label request_22: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    "Hermione gives you a blowjob."
    "You dismiss Hermione."
    if whoring <= 17:
        $ whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "gryffindor got +55 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_23 (Level 06) (55 pt.) (Give handjob to a classmate). (Available during daytime only).
label request_23: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    "Hermione agrees to try and give a handjob to a classmate."
    "You dismiss Hermione."
    $ request_23 = True 
    if whoring <= 17:
        $ whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "gryffindor got +55 points."
    jump day_main_menu
        
label request_23_complete:
    "Hermione returns from her classes and tells you how she gave a handjob to one of her classmates during class."
    $ request_23 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then, Sir."
    return

###################REQUEST_24 (Level 06) (55 pt.) (Flash your tits to a teacher). (Available during daytime only).
label request_24: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    "Hermione agrees to try and flash her tits to a teacher."
    "You dismiss Hermione."
    $ request_24 = True 
    if whoring <= 17:
        $ whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "gryffindor got +55 points."
    jump day_main_menu
        
label request_24_complete:
    "Hermione returns from her classes. She tells you how she flashed her tits to a teacher."
    $ request_24 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then, Sir."
    return
    
###################REQUEST_25 (Level 07) (65 pt.) (Cum on face). 
label request_25: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    "Hermione sits still while you jerk off in her face."
    "You dismiss Hermione."
    if whoring <= 20:
        $ whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "gryffindor got +65 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_26 (Level 07) (65 pt.) (Cum in open mouth before class). (Available during daytime only).
label request_26: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    
    "Hermione sits still with her mouth wide open while you jerk off and cum in it. You tell her to only swallow it when she gets to class."
    "You dismiss Hermione with her mouth full of your cum."
    
    $ request_26 = True 
    if whoring <= 20:
        $ whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "gryffindor got +65 points."
    jump day_main_menu
        
label request_26_complete:
    "Hermione returns from her classes and tells you that she couldn't speak to her classmates because her mouth was filled with your cum."
    $ request_26 = False 
    $ hermione_sleeping = True
    her "Oh, alright, Sir. I will go to bed then."
    return

###################REQUEST_27 (Level 07) (65 pt.) (Blow two classmates). (Available during daytime only).
label request_27: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    "Hermione agrees to try and blow two classmates during classes."
    "You dismiss Hermione."
    $ request_27 = True 
    if whoring <= 20:
        $ whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "gryffindor got +65 points."
    jump day_main_menu
        
label request_27_complete:
    "Hermione returns from her classes. She tells you how she gave a blowjob to two classmates during classes."
    $ request_27 = False 
    $ hermione_sleeping = True
    her "Oh, alright, Sir. I will go to bed then."
    return

###################REQUEST_28 (Level 07) (65 pt.) (Give handjob to a teacher). (Available during daytime only).
label request_28: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    "Hermione agrees to try and give a handjob to a teacher during classes."
    "You dismiss Hermione."
    $ request_28 = True 
    if whoring <= 20:
        $ whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "gryffindor got +65 points."
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
    if whoring <=20:
        jump too_much
    if daytime:
        "You have sex with Hermione and send her to her classes afterwards."
    else:
        "You have sex with Hermione."
        "You send her to bed."
    if whoring <= 23:
        $ whoring +=1
    $ gryffindor +=75
    "gryffindor got +75 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_30 (Level 08) (75 pt.) (Blow a teacher). (Available during daytime only).
label request_30: #LV.8 (Whoring = 21 - 23)
    if whoring <=20:
        jump too_much
    "Hermione agrees to try and blow a teacher."
    "You dismiss Hermione."
    $ request_30 = True 
    if whoring <= 23:
        $ whoring +=1
    $ gryffindor +=75
    $ hermione_takes_classes = True
    "gryffindor got +75 points."
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
    if whoring <=23:
        jump too_much
    "You have anal sex with Hermione."
    "You order her to go to bed afterwards."
    if whoring <= 26:
        $ whoring +=1
    $ gryffindor +=85
    "gryffindor got +85 points."
    $ hermione_sleeping = True
    jump day_start


################
### LEVEL 10 ###
###################REQUEST_32 (Level 10) (100 pt.) (Wear a very revealing outfit to class). (Daytime only)
label request_32: #LV.10 (Whoring = 27 - 29)
    if whoring <=26:
        jump too_much
    "Hermione puts on a very slutty outfit and goes to her classes."
    $ request_32 = True
    if whoring <= 29:
        $ whoring +=1
    $ gryffindor +=100
    $ hermione_takes_classes = True
    "gryffindor got +100 points."
    jump day_main_menu

label request_32_complete:
    "Hermione returns from classes. She tells you that people treated her like a whore today."
    $ request_32 = False 
    $ hermione_sleeping = True
    her "Oh, as you wish, Sir. I will go to bed then, Sir."
    return

###################REQUEST_33 (Level 10) (100 pt.) THIS REQUEST IS NOW CAN ONLY BE ACCESSED THROUGH REQUEST_25 (CUM ON FACE) when whoring > 26. (Go to class with cum on your face). (Daytime only)
label request_33: #LV.10 (Whoring = 27 - 29)
    if whoring <=26:
        jump too_much
    "You cum all over hermione's face and send her to her classes."
    $ request_33 = True
    if whoring <= 29:
        $ whoring +=1
    $ gryffindor +=100
    $ hermione_takes_classes = True
    "gryffindor got +100 points."
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
    
    $ mad += 7
    
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


