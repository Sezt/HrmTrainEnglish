label mail:
    if finished_report >= 1:
        $ letters -= 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        $ got_paycheck = False #When TRUE the paycheck is in the mail. Can't do paper work.
        hide screen owl
        show screen owl_02
        ">You read the message."
        play sound "sounds/money.mp3"  #Quiet...

        $dgold=([40, 70, 90, 110, 150, 200][finished_report-1])*turbo
        $ letter_text = "{size=-7} FROM: Ministry of Magic\n To: Professor Dumbledore \n \n \n {/ size} {size=-2} Thank you for reports sent this week. \n Your payment: {/size} \n {size=+4} [dgold] gold coins. {/size} \n \n \n {size=-3} - With respect - {/size}"    
        $ gold += dgold

        
        show screen bld1
        show screen letter
        show screen ctc
        pause
        hide screen letter
        hide screen bld1
        hide screen ctc
            
        $ finished_report = 0

        call screen main_menu_01
    
    
### MAIL FROM HERMIONE ###
if day == 1:
    #$ letter_text = "{size=-4}-Для профессора Дамблдора-\n\nЯ пишу Вам, что бы довести до Вашего внимания текущию ситуацию в нашей школе .\n Я боюсь мне будет нужна Ваша помощь, чтобы разобраться в этом.\n\n\n-С уважениям Ваша Гермиона Грейнджер-{/size}"
    $ letter_text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sure that you remember the reason why I'm writing you this letter from my last one, sir.\n\nI beg of you, please hear my plea this time. This injustice simply cannot go on...\nNot in this day and age, not in our school.\n\nPlease take action.\n\n{size=-3}With deepest respect,\nHermione Granger{/size}"    
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label letter01_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "- Done reading -":
            pass    
        "- Not yet -":
            jump letter01_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    show screen bld1
    with d3
    m "Ehm..............................."
    m "What?"
    m "................................."
    hide screen bld1
    with d3
    jump event_00
    #call screen main_menu_01
    


if letter_from_hermione_02: #Letter from Hermione #02.
    $ letter_from_hermione_02 = False
    #$ letter_text = "{size=-4}-Для профессора Дамблдора-\n\nЯ пишу Вам, что бы довести до Вашего внимания текущию ситуацию в нашей школе.\n Я боюсь мне будет нужна Ваша помощь, чтобы разобраться в этом.\n\n\n-С уважениям Ваша Гермиона Грейнджер--{/size}"
    $ letter_text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sorry to disturb you again, professor. I just want to make sure that you take this problem seriously.\n\nLast night another classmate confided inme... I gave my word to keep it a secret, so I cannot go into any details.\n\nAll I can say is that one of the Professors was involved.\n\nPlease take action soon.\n\n{size=-3}With deepest respect,\nHermione Granger.{/size}"
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label letter02_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "- Done reading -":
            pass    
        "- Not yet -":
            jump letter02_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    call screen main_menu_01





### MAIL THAT UNLOCKS ABILITY TO WORK ###
if work_unlock: # Send a letter that will unlock an ability to write reports
    $ work_unlock = False # Send a letter that will unlock an ability to write reports
    $ letters -= 1
    $ work_unlock2 = True # Unlocks the "Paperwork" button.
    hide screen owl
    show screen owl_02
    $ letter_text = "{size=-7}From: Ministry of Magic\nTo: Professor Albus Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore.\nWe remind you that only upon providing us with a completed report we will be able to make a paymentin your name.\n\n{size=-3}With deepest respect,\nThe Ministry of Magic.{/size}"
    label letter_work:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "- Done reading -":
            pass    
        "- Not yet -":
            jump letter_work
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    m "Payments? Hm..."
    show screen blktone8
    with d3
    $ renpy.play('sounds/win2.mp3')   #Not loud.
    ">From now on you can do paperwork at your desk in order to earn additional gold..."
    hide screen blktone8
    with d3
    call screen main_menu_01


    
label mail_02: #Packages only. <=====================================================================### PACKAGES ###=================================================== 

    $evn=None
    python:
        for e in this.List:
            if "book_" in e.Name and e._status==-1:
                e.SetValue("status", 0)
                evn=e 

    if evn!=None:
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        $ the_gift = evn._img #"03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3
        ">Book [evn._caption] has been added to your collection."
        hide screen gift
        with d3
        call screen main_menu_01  


    
    
    
    
    
### ITEMS ###    
    
    if bought_ball_dress:
        $ bought_ball_dress = False
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        #$ gifts12 += ["ball_dress"]
        $ bought_dress_already = True #Makes sure that you won't buy the dress twice.
        
        $ gifts12.append("ball_dress")
        $ the_gift = "03_hp/18_store/01.png" # THE NIGHT DRESS.
        show screen gift
        with d3
        ">A fancy nightdress has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
        
        
    if bought_miniskirt:
        $ bought_miniskirt = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        #$ gifts12 += ["ball_dress"]
        $ bought_skirt_already = True #Makes sure that you won't buy the skirt twice.
        $ have_miniskirt = True # Turns TRUE when you have the skirt in your possession.
        $ the_gift = "03_hp/18_store/07.png" # MINISKIRT.
        show screen gift
        with d3
        ">A School miniskirt has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01

    
    if bought_anal_lube:
        $ bought_anal_lube = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ anal_lube += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/09.png" # ANAL LUBRICANT.
        show screen gift
        with d3
        ">A jar of anal lubricant has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
    
    if bought_condoms:
        $ bought_condoms = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ condoms += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/10.png" # CONDOMS.
        show screen gift
        with d3
        ">A pack of condoms has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
    
    
    if bought_candy:
        $ bought_candy = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ candy += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/11.png" # CANDY.
        show screen gift
        with d3
        ">A lollipop has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
        
    if bought_chocolate:
        $ bought_chocolate = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ chocolate += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
        show screen gift
        with d3
        ">A bar of chocolate has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_vibrator:
        $ bought_vibrator = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ vibrator += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/13.png" # VIBRATOR.
        show screen gift
        with d3
        ">A vibrator has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
        
    if bought_strapon:
        $ bought_strapon = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ strapon += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON.
        show screen gift
        with d3
        ">A Thestral strapon has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
        
        
    if bought_ballgag:
        $ bought_ballgag = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ ballgag += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">A ball gag and a pair of cuffs have been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_plug:
        $ bought_plug = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ plug += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/16.png" # ANAL PLUG.
        show screen gift
        with d3
        ">An assortment of anal plugs has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_mag1:
        $ bought_mag1 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag1 += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/17.png" # MAGAZINE # 1
        show screen gift
        with d3
        ">An assortment of educational magazines has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_mag2:
        $ bought_mag2 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag2 += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/18.png" # MAGAZINE # 2
        show screen gift
        with d3
        ">An assortment of rather girly magazines has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_mag3:
        $ bought_mag3 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag3 += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/19.png" # MAGAZINE # 3
        show screen gift
        with d3
        ">An assortment of adult magazines has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_mag4:
        $ bought_mag4 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag4 += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/20.png" # MAGAZINE # 4
        show screen gift
        with d3
        ">An assortment of porn magazines has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_beer:
        $ bought_beer = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ beer += 1 

        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">A bottle of butterbeer has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_owl:
        $ bought_owl = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ owl += 1 

        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">An owl plushy has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_badge_01:
        $ bought_badge_01 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ badge_01 = 1 

        $ the_gift = "03_hp/18_store/29.png" # S.P.E.W. Badge.
        show screen gift
        with d3
        ">A \"S.P.E.W.\" badge has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
    
    
    if bought_nets:
        $ bought_nets = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ nets = 1 

        $ the_gift = "03_hp/18_store/30.png" # FISHNETS.
        show screen gift
        with d3
        ">A pair of fishnet stockings have been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01