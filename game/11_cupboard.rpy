label cupboard:
    $ menu_x = 0.5 

    menu:
        "-Examine the cupboard-" if not cupboard_examined:
            $ cupboard_examined = True
            show screen chair_02 #Empty chair near the desk.
            hide screen genie
            $ tt_xpos=-20
            $ tt_ypos=100
            show screen genie_stands_f
            show screen desk
            with Dissolve(0.5)
            m "Hm....."
            m "A cupboard..."
            m "...that seems full of old junk!"
            m "Maybe I should rummage through this a bit later anyway."
            show screen genie
            hide screen genie_stands_f
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
            
            
            
        "-Rummage through the cupboard-" if not searched and not day == 1:
            jump rummaging
        "{color=#858585}-Rummage through the cupboard-{/color}" if searched and not day == 1:
            call already_did #Message that says that you have searched the cupboard today already.
            jump cupboard
        "-Your possessions-" if not day == 1:
            label possessions:
                $ choose = RunMenu()
                python:
                    for o in hero.Items():
                            choose.AddItem("- "+o._caption+" ("+str(hero.Items.Count(o.Name))+") -", "menu_cupboard_description" , o.Name)
                    if  day>4: 
                        choose.AddItem("Help", "cheat_help", "")
#                    choose.AddItem("- Never mind -", "cupboard", True, "")

                $ choose.Show("cupboard")

            label menu_cupboard_description:
                $item=itsDAHR(choose.choice)
                $ the_gift = item._img
                show screen gift
                with d3
                ">[item._description]"
                if item.Name=="perfume":
                    "> You tried to smell this perfume when received it and found it disgusting."
                    "> But maybe you where wrong? You smell the bottle..."
                    "> What the hell! Your first impression was correct..."
                    $hero.SetValue("perfumeused", time.stamp)
                hide screen gift
                with d3
                jump possessions                

                   
                label cheat_help:
                menu:
                    "Enable TURBO mode" if turbo==1: 
                        $turbo=2
                        "TURBO mode is enabled. Your actions will now give you twice as much money and points for the Slytherin house.\n Also twice the chance to read additional chapters."                    
                    "Disable TURBO mode" if turbo==2: 
                        $turbo=1
                        "TURBO mode is off. Your actions will now give you the usual amount of money and points for the Slytherin house.\n Also the normal chance to read additional chapters."                    
                    "CHEAT: +100 points for Slytherin":
                        hide screen points
                        $slytherin+=100
                        show screen points
                    "CHEAT: Hermione is no longer angry at you":
                        hide screen points
                        $hermi.liking=0
                        show screen points
                        "Ready"
                    "CHEAT: +100 galleons":
                        hide screen points
                        $daphne.liking=0
                        show screen points
                        "Запрос выполнен"
#                    "ЧИТ: Дафна становиться более распутной":
#                        hide screen points
#                        $daphne.whoring+=1
#                        show screen points
#                        "Готово"
                    "ЧИТ: +100 галеонов":
                        hide screen points
                        $gold+=100
                        show screen points
                    "Walkthrough":
                        "Walkthrough and answers to frequently asked questions can be found {a=http://wtrus.ixbb.ru/viewtopic.php?id=19}HERE{/a}."

                    "-Never mind-":
                        jump cupboard
                jump cheat_help


        "-Sacred scrolls volume I-" if not day == 1 and cataloug_found:
            label sc_col_men_1:
                $_scrollSection=0
                jump sc_col

        "-Sacred scrolls volume II-" if not day == 1 and cataloug_found:
            label sc_col_men_2:
                $_scrollSection=1
                jump sc_col

        "-Sacred scrolls volume III-" if not day == 1 and cataloug_found:
            label sc_col_men_3:
                $_scrollSection=2
                jump sc_col

        "- Священные свитки. Часть IV -" if not day == 1 and cataloug_found:
            label sc_col_men_4:
                $_scrollSection=3
                jump sc_col

        "- Священные свитки. Часть V -" if not day == 1 and cataloug_found:
            label sc_col_men_5:
                $_scrollSection=4
                jump sc_col_part

#        "- Священные свитки. Часть VI -" if not day == 1 and cataloug_found:
#            label sc_col_men_6:
#                $_scrollSection=5
#                jump sc_col


                label sc_col:
                    $ choose = RunMenu()
                    python:
                        _itemCount=hero.Items.Count("scroll")
                        for i in range(_scrollSection*15, _scrollSection*15+15):
                            if i<_itemCount:
                                choose.AddItem("- C."+str(i+1)+": Священный свиток #"+str(i+1)+" -", "menu_cupboard_scroll_show" , i)
                    $ choose.Show("cupboard")
                    
                label sc_col_part:
                    $ choose = RunMenu()
                    python:
                        _itemCount=hero.Items.Count("scroll")
                        for i in range(_scrollSection*15, _scrollSection*15+8):
                            if i<_itemCount:
                                choose.AddItem("- C."+str(i+1)+": Священный свиток #"+str(i+1)+" -", "menu_cupboard_scroll_show" , i)
                    $ choose.Show("cupboard")


                label menu_cupboard_scroll_show:

                    $ the_gift = "03_hp/19_extras/"+str(choose.choice+1).zfill(2)+".png"
 # SACRED SCROLL 01.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump expression "sc_col_men_"+str((choose.choice)//15+1)
            
        "-Never mind-":
            jump day_main_menu
 
label rummaging:  
    
    $ searched = True #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
    
    $ rum_times += 1 # Counts how many times have you rummaged the cupboard. +1 every time you do that. Needed to make to grand 2 potions before the fight.
    
    hide screen cupboard
    hide screen genie
    show screen rum_screen
    with Dissolve(0.3)
    show screen bld1
    with d3
    ">You rummage through the cupboard for a while..." 
    
    if day <= 4:
        if rum_times == 2 or rum_times == 3:
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ potions += 1
            $ the_gift = "03_hp/18_store/32.png" # CANDY.
            show screen gift
            with d3
            ">You found some sort of potion..." 
            hide screen gift
            with d3
            show screen cupboard
            show screen genie
            hide screen rum_screen
            
            hide screen bld1
            with d3
            
            if daytime:
                jump night_start
            else: 
                jump day_start

    if rum_times == 15 and not cataloug_found:
        $ renpy.play('sounds/win2.mp3')   #Not loud.
        $ cataloug_found = True # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.
        $ the_gift = "03_hp/18_store/dahr2.png" # DAHR's oddities catalog. 
        show screen gift
        with d3
        ">You found the dahr's oddities catalog...\n>You can now use the catalog to order goods via owl post."
        hide screen gift
        with d3
        show screen cupboard
        show screen genie
        hide screen rum_screen
        
        hide screen bld1
        with d3
        
        if daytime:
            jump night_start
        else: 
            jump day_start
        
    
    if i_of_iv == 4: # Found something.
        $arrProb={"candy":[2,2,2,0], "wine": [7,5,4,0], "chocolate":[1,1,0,4], "lingere":[1,1,0,1], "sexdoll":[1,1,1,1],
        "krum":[0,1,1,1],"owl":[0,0,4,4], "broom":[0,0,0,1]} #"gold":[8, 9, 8, 8]

        $_level=GetStage(hermi.whoring, 0, 4, 6)-1
        $_randValue=one_of_tw
        $debug.SaveString(str(_randValue))
        $_name="gold"
        python:
            for o in arrProb:
                _randValue-=arrProb[o][_level]
                if _randValue<=0:
                    _name=o

        $debug.SaveString(_name)
        $ renpy.play('sounds/win2.mp3')   #Not loud.
        if _name=="gold":
            $_gold=[gold1,gold2,gold3,gold4][_level]
            hide screen points
            $gold+=_gold
            show screen points
            $ the_gift="03_hp/18_store/28.png"
            $_caption="You found some "+str(_gold)+" galleons"
        else:
            $item=hero.Items.AddItem(_name)
            $ the_gift=item._img
            $_caption=item._caption

        $screens.ShowD3("gift").Say(">You found: \"[_caption]!\"").HideD3("gift")



    else: #Didn't find anything.
        ">...You find nothing of value." 
    

    
    show screen cupboard
    show screen genie
    hide screen rum_screen
    
    hide screen bld1
    with d3
    
    if daytime:
        jump day_main_menu
    else: 
        jump night_main_menu
        
        
        
        
        
        
        
######################
label already_did:
    show screen bld1
    with d3
    m "I already did that today..."
    hide screen bld1
    with d3
    return
