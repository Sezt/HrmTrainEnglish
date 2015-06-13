label new_personal_request:
    $ pos = POS_410
    if slytherin > gryffindor or slytherin == gryffindor:
        $ herView.showQ( None, pos )
        
        $ menu_x = 0.2 #Default: 0.5
        
        label not_now:
        menu:
            "-Personal favours-":
                label not_now2:
                ### LEVEL 01 ###
                menu:
#                    "Favour: \"Talk to me\" {image=heart_00.png}" if not new_request_01_01 and not new_request_01_02 and not new_request_01_03:
#                        jump new_request_01
#                    "Favour: \"Talk to me\" {image=heart_01.png}" if new_request_01_01 and not new_request_01_02 and not new_request_01_03:
#                        jump new_request_01
#                    "Favour: \"Talk to me\" {image=heart_02.png}" if new_request_01_02 and not new_request_01_03:
#                        jump new_request_01
#                    "Favour: \"Talk to me\" {image=heart_03.png}" if new_request_01_03:
#                        jump new_request_01
                    "Favour: [this.new_request_01._caption] {image=heart_4[this.new_request_01._heartCount].png}":
                        jump new_request_01

#                    "Favour: \"Nice panties\" {image=heart_00.png}" if not new_request_02_01 and not new_request_02_02 and not new_request_02_03: # LEVEL 1
#                        jump new_request_02
#                    "Favour: \"Nice panties\" {image=heart_01.png}" if new_request_02_01 and not new_request_02_02 and not new_request_02_03: # LEVEL 1
#                        jump new_request_02
#                    "Favour: \"Nice panties\" {image=heart_02.png}" if new_request_02_02 and not new_request_02_03: # LEVEL 1
#                        jump new_request_02
#                    "Favour: \"Nice panties\" {image=heart_03.png}" if new_request_02_03: # LEVEL 1
#                        jump new_request_02
                    "Favour: [this.new_request_02._caption] {image=heart_4[this.new_request_02._heartCount].png}":
                        jump new_request_02
                  
                    ### LEVEL 02 ###
                    "{color=#858585}--A vague idea-{/color}-" if imagination == 1:
                        call vague_idea
                        jump not_now2
#                    "Favour: \"Panty thief\" {image=heart_00.png}" if not new_request_03_01 and not new_request_03_02 and not new_request_03_03 and daytime and imagination >= 2:
#                        jump new_request_03
#                    "Favour: \"Panty thief\" {image=heart_01.png}" if new_request_03_01 and not new_request_03_02 and not new_request_03_03 and daytime and imagination >= 2:
#                        jump new_request_03
#                    "Favour: \"Panty thief\" {image=heart_02.png}" if new_request_03_02 and not new_request_03_03 and daytime and imagination >= 2:
#                        jump new_request_03
#                    "Favour: \"Panty thief\" {image=heart_03.png}" if new_request_03_03 and daytime and imagination >= 2:
#                        jump new_request_03
                    "Favour: [this.new_request_03._caption] {image=heart_4[this.new_request_03._heartCount].png}" if daytime and imagination >= 2:
                        jump new_request_03


                    
                    "{color=#858585}--A vague idea-{/color}-" if imagination == 1:
                        call vague_idea
                        jump not_now2
#                    "Favour: \"Breast molester\" {image=heart_00.png}" if not new_request_04_01 and not new_request_04_02 and not new_request_04_03 and imagination >= 2: 
#                        jump new_request_04
#                    "Favour: \"Breast molester\" {image=heart_01.png}" if new_request_04_01 and not new_request_04_02 and not new_request_04_03 and imagination >= 2: 
#                        jump new_request_04
#                    "Favour: \"Breast molester\" {image=heart_02.png}" if new_request_04_02 and not new_request_04_03 and imagination >= 2: 
#                        jump new_request_04
#                    "Favour: \"Breast molester\" {image=heart_03.png}" if new_request_04_03 and imagination >= 2: 
#                        jump new_request_04
                    "Favour: [this.new_request_04._caption] {image=heart_4[this.new_request_04._heartCount].png}" if imagination >= 2:
                        jump new_request_04
                        
                    "{color=#858585}--A vague idea-{/color}-" if imagination == 1:
                        call vague_idea
                        jump not_now2
#                    "Favour: \"Butt molester\" {image=heart_00.png}" if not new_request_05_01 and not new_request_05_02 and not new_request_05_03 and imagination >= 2:
#                        jump new_request_05
#                    "Favour: \"Butt molester\" {image=heart_01.png}" if new_request_05_01 and not new_request_05_02 and not new_request_05_03 and imagination >= 2: 
#                        jump new_request_05
#                    "Favour: \"Butt molester\" {image=heart_02.png}" if new_request_05_02 and not new_request_05_03 and imagination >= 2: 
#                        jump new_request_05
#                    "Favour: \"Butt molester\" {image=heart_03.png}" if new_request_05_03 and imagination >= 2: 
#                        jump new_request_05
                    "Favour: [this.new_request_05._caption] {image=heart_4[this.new_request_05._heartCount].png}" if imagination >= 2:
                        jump new_request_05
                        
                    ### LEVEL 03 ### IMAGINATION == 3
                    "{color=#858585}--A vague idea-{/color}-" if imagination < 3:
                        call vague_idea
                        jump not_now2
#                    "Favour: \"Show them to me!\" {image=heart_00.png}" if not new_request_08_01 and not new_request_08_02 and not new_request_08_03 and imagination >= 3:
#                        jump new_request_08
#                    "Favour: \"Show them to me!\" {image=heart_01.png}" if new_request_08_01 and not new_request_08_02 and not new_request_08_03 and imagination >= 3: 
#                        jump new_request_08
#                    "Favour: \"Show them to me!\" {image=heart_02.png}" if new_request_08_02 and not new_request_08_03 and imagination >= 3: 
#                        jump new_request_08
#                    "Favour: \"Show them to me!\" {image=heart_03.png}" if new_request_08_03 and imagination >= 3: 
#                        jump new_request_08 
                    "Favour: [this.new_request_08._caption] {image=heart_4[this.new_request_08._heartCount].png}" if imagination >= 3:
                        jump new_request_08
 

#                    "Favour: \"Show {size=+5}it{/size} to me! (NOT FINISHED YET)":
#                        jump new_request_09
                    
                    ### LEVEL 04 ### IMAGINATION == 3
                    "{color=#858585}--A vague idea-{/color}-" if imagination < 3:
                        call vague_idea
                        jump not_now2
#                    "Favour: \"Dance for me!\" {image=heart_00.png}" if not new_request_11_01 and not new_request_11_02 and not new_request_11_03 and imagination >= 3:
#                        jump new_request_11
#                    "Favour: \"Dance for me!\" {image=heart_01.png}" if new_request_11_01 and not new_request_11_02 and not new_request_11_03 and imagination >= 3: 
#                        jump new_request_11
#                    "Favour: \"Dance for me!\" {image=heart_02.png}" if new_request_11_02 and not new_request_11_03 and imagination >= 3:
#                        jump new_request_11
#                    "Favour: \"Dance for me!\" {image=heart_03.png}" if new_request_11_03 and imagination >= 3: 
#                        jump new_request_11
                    "Favour: [this.new_request_11._caption] {image=heart_0[this.new_request_11._heartCount].png}" if imagination >= 3:
                        jump new_request_11

                    
                    "{color=#858585}--A vague idea-{/color}-" if imagination < 3:
                        call vague_idea
                        jump not_now2
#                    "Favour: \"Let me touch them!\" {image=heart_00.png}" if not new_request_12_01 and not new_request_12_02 and not new_request_12_03 and daytime and imagination >= 3: # LEVEL 4
#                        jump new_request_12
#                    "Favour: \"Let me touch them!\" {image=heart_01.png}" if new_request_12_01 and not new_request_12_02 and not new_request_12_03 and daytime and imagination >= 3: # LEVEL 4
#                        jump new_request_12
#                    "Favour: \"Let me touch them!\" {image=heart_02.png}" if new_request_12_02 and not new_request_12_03 and daytime and imagination >= 3: # LEVEL 4
#                        jump new_request_12
#                    "Favour: \"Let me touch them!\" {image=heart_03.png}" if new_request_12_03 and daytime and imagination >= 3: # LEVEL 4
#                        jump new_request_12
                    "Favour: [this.new_request_12._caption] {image=heart_0[this.new_request_12._heartCount].png}" if imagination >= 3:
                        jump new_request_12

                    
                    ### LEVEL 05 ### IMAGINATION == 4
                    "{color=#858585}--A vague idea-{/color}-" if imagination < 4:
                        call vague_idea
                        jump not_now2
#                    "Favour: \"touch me!\" {image=heart_00.png}" if not new_request_16_01 and not new_request_16_02 and not new_request_16_03 and imagination >= 4: # LEVEL 5
#                        jump new_request_16
#                    "Favour: \"touch me!\" {image=heart_01.png}" if new_request_16_01 and not new_request_16_02 and not new_request_16_03 and imagination >= 4: # LEVEL 5
#                        jump new_request_16
#                    "Favour: \"touch me!\" {image=heart_02.png}" if new_request_16_02 and not new_request_16_03 and imagination >= 4: # LEVEL 5
#                        jump new_request_16
#                    "Favour: \"touch me!\" {image=heart_03.png}" if new_request_16_03 and imagination >= 4:  # LEVEL 5
#                        jump new_request_16
                    "Favour: [this.new_request_16._caption] {image=heart_0[this.new_request_16._heartCount].png}" if imagination >= 4:
                        jump new_request_16

                       
                    ### LEVEL 06 ### IMAGINATION == 4
                    "{color=#858585}--A vague idea-{/color}-" if imagination < 4:
                        call vague_idea
                        jump not_now2
#                    "Favour: \"Suck it!\" {image=heart_00.png}" if not new_request_22_01 and not new_request_22_02 and not new_request_22_03 and imagination >= 4: # LEVEL 6
#                        jump new_request_22
#                    "Favour: \"Suck it!\" {image=heart_01.png}" if new_request_22_01 and not new_request_22_02 and not new_request_22_03 and imagination >= 4: # LEVEL 6
#                        jump new_request_22
#                    "Favour: \"Suck it!\" {image=heart_02.png}" if new_request_22_02 and not new_request_22_03 and imagination >= 4: # LEVEL 6
#                        jump new_request_22
#                    "Favour: \"Suck it!\" {image=heart_03.png}" if new_request_22_03 and imagination >= 4: # LEVEL 6
#                        jump new_request_22
                    "Favour: [this.new_request_22._caption] {image=heart_0[this.new_request_22._heartCount].png}" if imagination >= 4:
                        jump new_request_22

                    
                    ### LEVEL 07 ### IMAGINATION == 5
                    "{color=#858585}--A vague idea-{/color}-" if imagination < 5:
                        call vague_idea
                        jump not_now2
#                    "Favour: \"Let's have sex!\" {image=heart_00.png}" if not new_request_29_01 and not new_request_29_02 and not new_request_29_03 and imagination >= 5: # LEVEL 7
#                        jump new_request_29
#                    "Favour: \"Let's have sex!\" {image=heart_01.png}" if new_request_29_01 and not new_request_29_02 and not new_request_29_03 and imagination >= 5: # LEVEL 7
#                        jump new_request_29
#                    "Favour: \"Let's have sex!\" {image=heart_02.png}" if new_request_29_02 and not new_request_29_03 and imagination >= 5: # LEVEL 7
#                        jump new_request_29
#                    "Favour: \"Let's have sex!\" {image=heart_03.png}" if new_request_29_03 and imagination >= 5: # LEVEL 7
#                        jump new_request_29
                    "Favour: [this.new_request_29._caption] {image=heart_0[this.new_request_29._heartCount].png}" if imagination >= 5:
                        jump new_request_29
                        
                    ### LEVEL 08 ###
                    "{color=#858585}--A vague idea-{/color}-" if imagination < 5:
                        call vague_idea
                        jump not_now2
#                    "Favour:  \"Time for anal!\" {image=heart_00.png}" if not new_request_31_01 and not new_request_31_02 and not new_request_31_03 and imagination >= 5: # LEVEL 8
#                        jump new_request_31
#                    "Favour:  \"Time for anal!\" {image=heart_01.png}" if new_request_31_01 and not new_request_31_02 and not new_request_31_03 and imagination >= 5: # LEVEL 8
#                        jump new_request_31
#                    "Favour:  \"Time for anal!\" {image=heart_02.png}" if new_request_31_02 and not new_request_31_03 and imagination >= 5: # LEVEL 8
#                        jump new_request_31
#                    "Favour:  \"Time for anal!\" {image=heart_03.png}" if new_request_31_03 and imagination >= 5: # LEVEL 8
#                        jump new_request_31
                    "Favour: [this.new_request_31._caption] {image=heart_0[this.new_request_31._heartCount].png}" if imagination >= 5:
                        jump new_request_31

                            
                    "- Cancel -":
                        jump new_personal_request
                
            "{color=#858585}-Public favours-{/color}" if not daytime:
                show screen blktone
                $herView.hideQQ()
                ">Public favours are available during the daytime only."
                hide screen blktone
                $herView.showQ( None, pos )
                with d3
                jump not_now
            "- Public favours -" if daytime:
                if lock_public_favors:
                    her "Em... Sir..."
                    her "I do not mind to keep selling you the favours..."
                    her "But only as long as we keep them private..."
                    jump new_personal_request
                else:
                    label not_now3:
                    menu:
                        ### LEVEL 01 ### 
                        "Favour: \"She's a flirt\"" if daytime:
                            jump new_request_02_b
                            
                        ### LEVEL 02 ### IMAGINATION == 2
                        "{color=#858585}--A vague idea-{/color}-" if imagination < 2:
                            call vague_idea
                            jump not_now3
                        "Favour: \"She's bait\"" if daytime  and imagination >= 2:
                            jump new_request_02_c
                        
                        ### LEVEL 03 ### IMAGINATION == 3
                        "{color=#858585}--A vague idea-{/color}-" if imagination < 3:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Let a classmate molest you.\"" if imagination >= 3: # LEVEL 3
                            jump new_request_10
                        
                        ### LEVEL 04 ### IMAGINATION == 3
                        "{color=#858585}--A vague idea-{/color}-" if imagination < 3:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Flash your tits to a classmate.\"" if imagination >= 3: # LEVEL 4
                            jump new_request_15
                        
                        
                        ### LEVEL 05 ### IMAGINATION == 4
                        "{color=#858585}--A vague idea-{/color}-" if imagination < 4:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Kiss a girl.\"" if imagination >= 4: # LEVEL 5
                            jump new_request_20
                            
                        ### LEVEL 06 ### IMAGINATION == 4
                        "{color=#858585}--A vague idea-{/color}-" if imagination < 4:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Give a handjob to a classmate.\"" if imagination >= 4: # LEVEL 6
                            jump new_request_23
                            
                        ### LEVEL 07 ### IMAGINATION == 5
                        "{color=#858585}--A vague idea-{/color}-" if imagination < 5:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Give a blowjob to a classmate\"" if imagination >= 5:# LEVEL 7
                            jump new_request_24
                                
                         ### LEVEL 08 ### IMAGINATION == 5
                        "{color=#858585}--A vague idea-{/color}-" if imagination < 5:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Have sex with a classmate\"" if imagination >= 5:# LEVEL 8
                            jump new_request_30
                        
                        "-Cancel-":
                            jump new_personal_request
                
                
            "- Never mind -":
                jump hermione_main_menu
    
        
        
        
        
                   
                    
                    
                        
                 
                     
                    
                   
                        
#                    "...flash your panties to a teacher.{image=3_stars_00.png}" if request_07_points == 0:
#                        jump new_request_07
#                    "...flash your panties to a teacher.{image=3_stars_01.png}" if request_07_points == 1:
#                        jump new_request_07
#                    "...flash your panties to a teacher.{image=3_stars_02.png}" if request_07_points == 2:
#                        jump new_request_07
#                    "...flash your panties to a teacher.{image=3_stars.png}" if request_07_points >= 3:
#                        jump new_request_07
                        
                    

#                    "\"Let me stick a finger up your butt.\"{image=3_stars_00.png}" if request_17_points == 0:
#                        jump new_request_17
#                    "\"Let me stick a finger up your butt.\"{image=3_stars_01.png}" if request_17_points == 1:
#                        jump new_request_17
#                    "\"Let me stick a finger up your butt.\"{image=3_stars_02.png}" if request_17_points == 2:
#                        jump new_request_17
#                    "\"Let me stick a finger up your butt.\"{image=3_stars.png}" if request_17_points >= 3:
#                        jump new_request_17
                        
#                    "\"Touch my cock a little.\"{image=3_stars_00.png}" if request_18_points == 0:
#                        jump new_request_18
#                    "\"Touch my cock a little.\"{image=3_stars_01.png}" if request_18_points == 1:
#                        jump new_request_18
#                    "\"Touch my cock a little.\"{image=3_stars_02.png}" if request_18_points == 2:
#                        jump new_request_18
#                    "\"Touch my cock a little.\"{image=3_stars.png}" if request_18_points >= 3:
#                        jump new_request_18
                    
#                    "\"Rub my cock against your cheeks.\"{image=3_stars_00.png}" if request_19_points == 0:
#                        jump new_request_19
#                    "\"Rub my cock against your cheeks.\"{image=3_stars_01.png}" if request_19_points == 1:
#                        jump new_request_19
#                    "\"Rub my cock against your cheeks.\"{image=3_stars_02.png}" if request_19_points == 2:
#                        jump new_request_19
#                    "\"Rub my cock against your cheeks.\"{image=3_stars.png}" if request_19_points >= 3:
#                        jump new_request_19
                        
                    
                   
#                    "\"Let me cum on your tits\"{image=3_stars_00.png}" if request_21_points == 0: # LEVEL 6
#                        jump new_request_21
#                    "\"Let me cum on your tits\"{image=3_stars_01.png}" if request_21_points == 1:
#                        jump new_request_21
#                    "\"Let me cum on your tits\"{image=3_stars_02.png}" if request_21_points == 2:
#                        jump new_request_21
#                    "\"Let me cum on your tits\"{image=3_stars.png}" if request_21_points >= 3:
#                        jump new_request_21
                            
                    


            
            

    else:
        her "The Gryffindors are in the lead. I don't need to do this."
        jump hermione_main_menu
                


    
  


###################REQUEST_06 (Level 02) (Flash Трусики to classmate.) #################################################################################
label new_request_06:
    if hermi.whoring <=2:
        jump too_much
    if hermi.whoring >= 3: #Level 02
        m "I want you now to do something in class, show her panties to one of his classmates."
        if request_06_points == 0: #One star.
            her "Ohh..."
            "Hermione reluctantly agrees."
        elif request_06_points == 1: #Two stars.
            her "If..."
            "Hermione agreed."
            
        elif request_06_points == 2: #Three stars.
            her "Of course..."
            "Hermione agreed. willingly."
            
        elif request_06_points >= 3: #Master.
            her "of course, professor."
            ">Hermione happily agree."
        

        "You send Hermione."
        $ request_05 = True
        $ hermione_takes_classes = True
        
        if hermi.whoring <= 5:
            $ hermi.whoring +=1
            
        if request_05_points <= 2:
            $ gryffindor +=15
            "Gryffindor gets +15 points."
        else:
            $ gryffindor +=5
            "Gryffindor gets +5 points."

        jump day_main_menu
       
label new_request_05_complete:
    "Hermione returns to training."
    m "How was your day, Miss Granger?"
    if request_06_points == 0: #One star.
        her "Hmm ... I tried to show her panties to one of my classmates saw, but instead I think five or six of them briefly. So ashamed ..."
    elif request_06_points == 1: #Two stars.
        her "I showed her panties to one of my classmates."
    elif request_06_points == 2: #Three stars.
        her "I have long demonstrated their panties to one of my classmates."
    elif request_06_points >= 3: #Three stars.
        her "I was able to show her panties so that one of my classmates stared at them."
        her "It was super!"
    
    "You let go of Hermione."
    $ request_06_points += 1 #Leveling up the event.
    $ request_05 = False 
    $ hermione_sleeping = True
    her "Well, okay. I'll go to sleep then."     
    return


###################REQUEST_07 (Level 02) (Flash Трусики to a teacher).(Daytime only). #######################################################################
label new_request_07:
    if hermi.whoring <=2:
        jump too_much
    if hermi.whoring >= 3: #Level 02
        m "I want you now to do something in class, show her panties to one of his teachers."
        if request_07_points == 0: #One star.
            her "Ohh..."
            "Hermione reluctantly agrees."
            
        elif request_07_points == 1: #Two stars.
            her "if only..."
            "Hermione agreed."
            
        elif request_07_points == 2: #Three stars.
            her "of course..."
            "Hermione agreed. willingly."
            
        elif request_07_points >= 3: #Master.
            her "of course, professor."
            ">Hermione happily agree."
        

        "You let go of Hermione."
        $ request_06 = True
        if hermi.whoring <= 5:
            $ hermi.whoring +=1
        
        if request_05_points <= 2:
            $ gryffindor +=15
            "Gryffindor gets +15 points."
        else:
            $ gryffindor +=5
            "Gryffindor gets +5 points."
        $ hermione_takes_classes = True
        jump day_main_menu
        

label new_request_06_complete:
    "Hermione returns to training."
    m "How was your day, Miss Granger?"
    if request_07_points == 0: #One star.
        her "Hmm ... I tried to show her panties to the teacher that he had seen them, but instead I think five or six of them classmates saw briefly. So ashamed ..."
    elif request_07_points == 1: #Two stars.
        her "I showed her panties to one of the teachers."
    elif request_07_points == 2: #Three stars.
        her "I have long demonstrated their panties to one of the teachers."
    elif request_07_points >= 3: #Three stars.
        her "I have long demonstrated their panties to one of the teachers."
        her "It was super!"
    
    $ request_07_points += 1 
    $ request_06 = False 
    $ hermione_sleeping = True
    her "Well, okay. I'll go to sleep then."
    return
      
###################REQUEST_09 (Level 03) (Show me pussy).###############################################################################################
label new_request_09: #LV.3 (Whoring = 6 - 8)
    $herView.hideQQ()
    if request_09_points == 0:
        m "{size=-4}(Ask a girl to show me her pussy?){/size}"
    else:
        m "{size=-4}(Ask a girl to show me her pussy again?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let him show!)\"":
            show screen blktone
            with d3
            pass
        "\"(not now.)\"":
            jump new_personal_request
    
    
    if request_09_points == 0 and hermi.whoring <= 11: # LEVEL 04 # FIRST TIME.
        m "Miss Granger..."
        m "Today's award for  \"Gryffindor\" 25 points."
        $herView.hideQQ()
        $ pos = POS_370
        $herView.showQQ( "body_03.png", pos )
        her "The Truth?"
        her "Thank you so much, sir!"
        m "Yes, but I need your help ..."
        her "of course, sir! Anything!"
        m "Pick up skirt..."
        her "...?"
        m "Drain panties..."
        her "?!!"
        m "And show her pussy!"
        if hermi.whoring <=5:
            jump too_much
        her "professor Dumbledore!"
        her "This is a whole new level inappropriate, even for you, sir!"
        her "How can you ask such a thing of your student?"
        m "So, how do you feel? I can see..."
        m "Then I think to reward other houses..."
        m "\"Slytherin\" ?"
        her "................"
        m "But you know,..."
        her "professor..."
        her "The fate of my faculty very important for me..."
        m "Really?"
        m "Why then did you show it to me?"
        m "Yes I Am. Show me how it's important to you, Miss Granger."
        her "But it is not just..."
        m "We have no time to discuss what is appropriate and what is not, Miss Granger?"
        her ".................."
        m "I would say that the ship sailed..."
        her ".............."
        m "All I want to do is quickly see..."
        her "But why? Why should I do it, sir?"
        m "minute of your time and \"Gryffindor\" receives 25 points..."
        m "Very good deal, do not you agree?"
        her "I think..."
    else:
        m "Miss Granger?"
        her "Yes..."
        m "I need to see your pussy..."
        if hermi.whoring >= 6 and hermi.whoring <= 8: #LEVEL 03 <=========================================================================================== FIRST EVENT
            her "Argh ... Not again, sir..."
            her "{size=-5}...so ashamed...{/size}"
            m "25 points, Miss Granger..."
            her ".............."
        if hermi.whoring >= 9 and hermi.whoring <= 11: #LEVEL 04 <=========================================================================================== SECOND EVENT
            her "*Huh*... provided that..."      
        if hermi.whoring >= 12 and hermi.whoring <= 14: # LEVEL 05 <=========================================================================================== THIRD EVENT
            her "Really?"
            her "Ok..."

  
#    if whoring >= 6 and whoring <= 8: #LEVEL 03 <=========================================================================================== FIRST EVENT

#    if whoring >= 9 and whoring <= 11: #LEVEL 04 <=========================================================================================== SECOND EVENT
  
#    if whoring >= 12 and whoring <= 14: # LEVEL 05 <=========================================================================================== THIRD EVENT
    

        
    
    
    
    
    if hermi.whoring <=5:
        jump too_much
        

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    m "Show me your pussy..."
    if request_09_points == 0: #One star.
        her "Ohh... "
        ">Hermione pulls up her skirt and pulls down her panties. She blushed and looks angry."
    
    elif request_09_points == 1: #Two stars.
        her "...Yes, Professor."
        ">Hermione pulls up her skirt and pulls down her panties. It looks impatient."
        
    elif request_09_points == 2: #Three stars.
        her "of course, sir..."
        ">Hermione pulls up her skirt and pulls down her panties. It looks playful."
        
    elif request_09_points >= 3: #Master.
        her "Here you go, Headmaster."
        ">Hermione pulls up her skirt and pulls down her panties. She is smiling to you."
    
    "You let go of Hermione."
        
    if hermi.whoring <= 8:
        $ hermi.whoring +=1

    if request_09_points <= 2:
        $ gryffindor +=25
        "Gryffindor received +25 points."
    else:
        $ gryffindor +=7
        "Gryffindor received  +7 points."
       
    $ request_09_points += 1
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu    
    

     

        

    

     
###################REQUEST_17 (Level 05) (Stick a finger up her butthole.) (Day/Night)
label new_request_17: #LV.5 (Whoring = 12 - 14)
    if hermi.whoring <=11:
        jump too_much
        
    m "Come here and let me poke a finger in your ass."
    if request_17_points == 0: #One star.
        her "Oh... "
        ">Hermione reluctantly agrees."
    elif request_17_points == 1: #Two stars.
        her "...Yes, Professor."
        ">Hermione agrees."
    elif request_17_points == 2: #Three stars.
        ">Hermione happily agrees."
    elif request_17_points >= 3: #Master.
        her "Here, Professor."
        ">Hermione playfully agrees."
        
    "You let Hermione."
        
    if hermi.whoring <= 14:
        $ hermi.whoring +=1

    if request_17_points <= 2:
        $ gryffindor +=45
        "Gryffindor gets 45 points."
    else:
        $ gryffindor +=11
        "Gryffindor gets 11 points."
       
    $ request_17_points += 1
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        
###################REQUEST_18 (Level 05) (Handjob) (Day/Night)
label new_request_18: #LV.5 (Whoring = 12 - 14)
    if hermi.whoring <=11:
        jump too_much
        
    m "Come and touch my dick."
    if request_18_points == 0: #One star.
        her "Oh... "
        ">Hermione reluctantly agrees."
    elif request_18_points == 1: #Two stars.
        her "...Yes, Professor."
        ">Hermione agrees."
    elif request_18_points == 2: #Three stars.
        ">Hermione happily agrees."
    elif request_18_points >= 3: #Master.
        her "Here, Professor."
        ">Hermione playfully agrees."
        
    "You let go of Hermione."
        
    if hermi.whoring <= 14:
        $ hermi.whoring +=1

    if request_18_points <= 2:
        $ gryffindor +=45
        "Gryffindor gets 45 points."
    else:
        $ gryffindor +=11
        "Gryffindor gets 11 points."
       
    $ request_18_points += 1
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        
    
###################REQUEST_19 (Level 05) (Rub her dick against her cheeks.) (Day/Night)
label new_request_19: #LV.5 (Whoring = 12 - 14)
    if hermi.whoring <=11:
        jump too_much
    
    m "Come here and rub my cock on her cute cheeks."
    if request_19_points == 0: #One star.
        her "Oh... "
        ">Hermione reluctantly agrees."
    elif request_19_points == 1: #Two stars.
        her "...Yes, Professor."
        ">Hermione agrees."
    elif request_19_points == 2: #Three stars.
        ">Hermione happily agrees."
    elif request_19_points >= 3: #Master.
        her "As you say, Professor."
        ">Hermione would agree."
        
    "You ask Hermione leave."
        
    if hermi.whoring <= 14:
        $ hermi.whoring +=1

    if request_19_points <= 2:
        $ gryffindor +=45
        "Gryffindor gets 45 points."
    else:
        $ gryffindor +=11
        "Gryffindor gets 11 points."
       
    $ request_19_points += 1
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        

    
    
    
#############################################################################################################################################
### LEVEL 06 ################################################################################################################################       
###################REQUEST_21 (Level 06) (55 pt.) (Cum on tits). ############################################################################ 
#As this request levels up, there are an option appears to offer some extra points if Hermione will put her clothes
#on top of her sperm covered tits and go to classes like that.
label new_request_21: #LV.6 (Whoring = 15 - 17)
    if hermi.whoring <=14:
        jump too_much
    
    m "Come here and give your boobs masturbate."
    if request_21_points == 0: #One star.
        her "oh... "
        ">Hermione reluctantly agrees."
        ">You ended up on her bare chest."
    elif request_21_points == 1: #Two stars.
        her "...Yes, Professor."
        ">Hermione agrees."
        ">You ended up on her bare chest."
    elif request_21_points == 2: #Three stars.
        ">Hermione happily agrees."
        ">You ended up on her bare chest."

    elif request_21_points >= 3: #Master.
        her "As you wish, dire... master."
        ">Hermione eagerly agrees."
        ">You ended up on her bare chest."
    
    her "You can give me a towel so I could wipe?"
    menu:
        "\"of course.\"":
            ">You give Hermione a towel and she wipes your sperm."
        "\"Go so.\"":
            m "Just fasten her blouse and Go so."
            
            if request_21_points <= 1:
                her "What? I can not, please give the towel."
                ">You give Hermione a towel and she wipes your sperm."
           
            else:
                her "What? But ..."
                her "Okay, but only if you give me extra points."
                menu:
                    "- Give extra points -":
                        m "Ok..."
                        her "All right, then..."
                        ">Hermione buttons her blouse."
                        $ gryffindor +=10
                        "Gryffindor gets 10 points."
                        $ request_21 = True
                    "- forget It -":
                        ">You give Hermione a towel and she wipes your sperm."
            
    "You let go of Hermione."
        
    if hermi.whoring <= 14:
        $ hermi.whoring +=1

    if request_21_points <= 2:
        $ gryffindor +=55
        "Gryffindor gets 55 points."
    else:
        $ gryffindor +=12
        "Gryffindor gets 12 points."
       
    $ request_21_points += 1 
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        
        
label new_request_21_complete:
    "Hermione returns to her class."
    m "How was your day?"
    if request_21_points == 3: #One star.
        her "Um ... I was sitting in class and I felt like my boobs are completely covered in cum. It was so unpleasant ..."
    elif request_21_points >= 4: #Two stars.
        her "In class, I sat and felt like my boobs are completely covered in cum. It is simply super."
             

    
    $ request_21 = False 
    $ hermione_sleeping = True
    her "Oh, okay. Then I go to sleep."
    return        
        
        
    

    

#############################################################################################################################################
### LEVEL 07 ################################################################################################################################  
#############################################################################################################################################
    
###################REQUEST_25 (Level 07) (65 pt.) (Cum on face). 
label new_request_25: #LV.7 (Whoring = 18 - 20)
    if hermi.whoring <=17:
        jump too_much
    
    m "Come here and let me cum on your face."
    if request_25_points == 0: #One star.
        her "О... "
        ">Hermione reluctantly agrees."
        ">You end on her face."
    elif request_25_points == 1: #Two stars.
        her "...Yes, Professor."
        ">Hermione agrees."
        ">You end on her face."
    elif request_25_points == 2: #Three stars.
        ">Hermione happily agrees."
        ">You end on her face."

    elif request_25_points >= 3: #Master.
        her "of course, dire...master."
        ">Hermione eagerly agrees."
        ">You end on her face."
    
    her "Can I take a towel to wipe?"
    menu:
        "\"of course.\"":
            ">You give Hermione a towel and she wipes your sperm."
        "\"Go so.\"":
            m "Go to the lessons covered with cum face."
            
            if hermi.whoring <=26:
                her "What? No, I can not, please give me a towel!."
                ">You give Hermione a towel and she wipes your sperm."
           
            else:
                her "What? But ..."
                her "Okay, but only if you give me extra points."
                menu:
                    "- Give extra points -":
                        m "ok..."
                        her "okay then..."
                        ">Hermione does not touch your face."
                        $ gryffindor +=30
                        "Gryffindor gets 30 points."
                        $ request_25 = True
                    "- Forget It -":
                        ">You give Hermione a towel and she wipes your sperm."
            
    "You let go of Hermione."
        
    if hermi.whoring <= 20:
        $ hermi.whoring +=1

    if request_21_points <= 2:
        $ gryffindor +=65
        "Gryffindor gets 65 points."
    else:
        $ gryffindor +=14
        "Gryffindor gets 14 points."
       
    $ request_25_points += 1 
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        
        
label new_request_25_complete:
    "Hermione returned from school."
    m "How was your day, Miss Granger?"
    her "Um ... I spent most of the day with a face covered in semen. I'm constantly asked questions."
    
    
    $ request_25 = False 
    $ hermione_sleeping = True
    her "Okay. Then I'll go to sleep."
    return        
        

###################REQUEST_26 (Level 07) (65 pt.) (Cum in open mouth before class). (Available during daytime only).
label new_request_26: #LV.7 (Whoring = 18 - 20)
    if hermi.whoring <=17:
        jump too_much
    m "I want to cum in your face before you go to class."
    if request_26_points == 0: #One star.
        her "О..."
        "Hermione reluctantly agrees."
    elif request_26_points == 1: #Two stars.
        her "If i..."
        "Hermione agrees."
    elif request_26_points == 2: #Three stars.
        her "of course... professor."
        "Hermione agrees. On it you can see how she wants it."    
    elif request_26_points >= 3: #Master.
        her "of course, direc..master"
        ">Hermione happily agrees."
    
    "You let go of Hermione."
    
    $ request_26 = True 
    if hermi.whoring <= 20:
        $ hermi.whoring +=1
        
    if request_26_points <= 2:
        $ gryffindor +=65
        "Gryffindor gets 65 points."
    else:
        $ gryffindor +=14
        "Gryffindor gets 14 points."

    $ hermione_takes_classes = True
    jump day_main_menu
        

label new_request_26_complete:
    "Hermione returns to training."
    m "How was your day, Miss Granger?"
    if request_26_points == 0: #One star.
        her "Um ... I spent half the lesson with sperm in mouth"
    elif request_26_points == 1: #Two stars.
        her "Something else about cum. LVL 2"
    elif request_26_points == 2: #Three stars.
        her "LVL3"
    elif request_26_points >= 3: #Three stars.
        her "LVL4"
        her "It was wonderful!"
    
    $ request_26_points += 1 
    $ request_26 = False 
    $ hermione_sleeping = True
    her "Oh, okay. Then I go to sleep."
    return
    
###################REQUEST_27 (Level 07) (65 pt.) (Blow two classmates). (Available during daytime only).
label new_request_27: #LV.7 (Whoring = 18 - 20)
    if hermi.whoring <=17:
        jump too_much
    m "I want you to do something for me today: aspirate two classmates"
    if request_27_points == 0: #One star.
        her "oh..."
        "Hermione reluctantly agrees."
    elif request_27_points == 1: #Two stars.
        her "if i..."
        "Hermione agrees."
    elif request_27_points == 2: #Three stars.
        her "of course, professor"
        "Hermione agreed. She longs for it."    
    elif request_27_points >= 3: #Master.
        her "of course master..."
        ">Hermione gladly accepts."
    
    "You let go of Hermione."
    
    $ request_27 = True 
    if hermi.whoring <= 20:
        $ hermi.whoring +=1
        
    if request_27_points <= 2:
        $ gryffindor +=65
        "Gryffindor gets 65 points."
    else:
        $ gryffindor +=14
        "Gryffindor gets 14 points."

    $ hermione_takes_classes = True
    jump day_main_menu
        

label new_request_27_complete:
    "Hermione returns to training."
    m "How was your day, Miss Granger?"
    if request_27_points == 0: #One star.
        her "Em... Lvl.1."
    elif request_27_points == 1: #Two stars.
        her "Something else about LVL 2"
    elif request_27_points == 2: #Three stars.
        her "LVL3"
    elif request_27_points >= 3: #Three stars.
        her "LVL4"
        her "It was wonderful!"
    
    $ request_27_points += 1 
    $ request_27 = False 
    $ hermione_sleeping = True
    her "oh, okay. Perhaps I'll go to sleep."
    return
    
    
###################REQUEST_28 (Level 07) (65 pt.) (Give handjob to a teacher). (Available during daytime only).
label new_request_28: #LV.7 (Whoring = 18 - 20)
    if hermi.whoring <=17:
        jump too_much
    m "I want you to masturbate his teacher"
    if request_28_points == 0: #One star.
        her "Oh..."
        "Hermione reluctantly agrees"
    elif request_28_points == 1: #Two stars.
        her "If you must..."
        "Hermione agrees."
    elif request_28_points == 2: #Three stars.
        her "of course, professor."
        "Hermione agrees. She longs for it."    
    elif request_28_points >= 3: #Master.
        her "Of course master..."
        ">Hermione gladly accepts."
    
    "You let go of Hermione."
    
    $ request_28 = True 
    if hermi.whoring <= 20:
        $ hermi.whoring +=1
        
    if request_28_points <= 2:
        $ gryffindor +=65
        "Gryffindor gets 65 points."
    else:
        $ gryffindor +=14
        "Gryffindor gets 14 points."

    $ hermione_takes_classes = True
    jump day_main_menu

        
label new_request_28_complete:
    "Hermione returns to training."
    m "How was your day, Miss Granger?"
    if request_28_points == 0: #One star.
        her "Em... Lvl.1."
    elif request_28_points == 1: #Two stars.
        her "Something else about LVL 2"
    elif request_28_points == 2: #Three stars.
        her "LVL3"
    elif request_28_points >= 3: #Three stars.
        her "LVL4"
        her "It was wonderful!"
    
    $ request_28_points += 1 
    $ request_28 = False 
    $ hermione_sleeping = True
    her "Oh, okay. Then I go to sleep."
    return
    


   
    
    


    
###############################################################################################################################################
### LEVEL 10 ##################################################################################################################################
###################REQUEST_32 (Level 10) (100 pt.) (Wear a very revealing outfit to class). (Daytime only) ####################################
label new_request_32: #LV.10 (Whoring = 27 - 29)
    if hermi.whoring <=26:
        jump too_much
    m "I want you to wear it."
    if request_32_points == 0: #One star.
        her "Oh..."
        "Hermione reluctantly agrees."
    elif request_32_points == 1: #Two stars.
        her "If so you need to..."
        "Hermione agrees."
    elif request_32_points == 2: #Three stars.
        her "of course, professor."
        "Hermione agrees. She longs for it."    
    elif request_32_points >= 3: #Master.
        her "of course, master..."
        ">Hermione gladly accepts."
    
    "Hermione puts on a very rakish outfit and goes to school."
    
    $ request_32 = True 
    if hermi.whoring <= 29:
        $ hermi.whoring +=1
        
    if request_32_points <= 2:
        $ gryffindor +=100
        "Gryffindor gets 100 points."
    else:
        $ gryffindor +=23
        "Gryffindor gets 23 points."

    $ hermione_takes_classes = True
    jump day_main_menu


label new_request_32_complete:
    "Hermione returns to training."
    m "How was your day, Miss Granger?"
    if request_32_points == 0: #One star.
        her "Em... Lvl.1. She tells you how people treated her like a whore today."
    elif request_32_points == 1: #Two stars.
        her "Something else about LVL 2. She tells you how people treated her like a whore today."
    elif request_32_points == 2: #Three stars.
        her "LVL3. She tells you how people treated her like a whore today."
    elif request_32_points >= 3: #Three stars.
        her "LVL4. She tells you how people treated her like a whore today."
        her "It was wonderful!"
    
    $ request_32_points += 1
    $ request_32 = False 
    $ hermione_sleeping = True
    her "Oh, okay. Then I go to sleep."
    return
    
    
    

    
    
    
    
    
### MUSIC BLOCK ###
label music_block:
    $music()
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    return
    ### END OF BLOCK ###    
    
    


### YOU LUCK IMAGINATION ###
label vague_idea:
    show screen blktone8
    ">You do not have the imagination for such."
    hide screen blktone8
    return


label could_not_flirt: #Sent here when choose "Задание провалено! Ты не получишь очки!" (Hermione is leaving without getting any points).
    hide screen blkfade
    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen chair_02
    hide screen hermione_02
    hide screen jerking_off_01 #Hermione topless. Genie jerking off.
    hide screen ctc
    show screen genie
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
    $ request_02_b = False 
    $event.Finalize() # Увеличиваем счетчик выполнений ивента. Если этого не делать, то после фейла Гермионы в публичных (фейл приводит в эту ветку), начинает рассинхронизироваться счетчик заданий и отчетов

#    if daytime:
#        $ hermione_takes_classes = True
#    else:
#        $ hermione_sleeping = True
#    return

    label finish_daytime_event:
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
