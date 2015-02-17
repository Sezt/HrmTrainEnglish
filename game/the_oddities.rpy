label menu_dahr_book:
    if choose==None:
        $ choose = RunMenu()
    else:
        $choose.Clear()
    python:
        for e in this.List:
            if e.GetValue("block")==_block: # Нужно ставить GetValue("block")  а не _block - у ивента такого объекта может не быть
                choose.AddItem("- Книга: "+e._caption+" - "+("{image=check_08.png}" if e._status>-2 else "{image=check_07.png}"), 
                    "menu_dahre_book_2", True, e)
        choose.AddItem("- Never mind -", "the_oddities", True, event)

    $ choose.Show()

    label menu_dahre_book_2:
        $ the_gift = event._img     # "03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3
        dahr "\"[event._caption]\". [event._description]\n"
        if event._status>-2: 
            call do_have_book
            jump the_oddities
        menu:
            "- Buy the book for [event._price] gold -":
                if gold >= event._price:
                    $ gold -= event._price
                    $ order_placed = True
                    $ event.IncValue("status",1)
#                            $ bought_book_01 = True
                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                    jump desk
                else:
                    call no_gold #Massage: m "I don't have enough gold".
                    jump expression _label
            "- Never mind -":
                hide screen gift
                jump expression _label #education_menu



label the_oddities:
    $choose=None
    menu:
        dahr "Welcome to the \"Muggle oddities catalog\". Your taste is never too odd for us!"
        "- Educational Books -":
            label education_menu:
                $_label="education_menu"
                $_block="books_edu"
                jump menu_dahr_book
        "- Fiction books -":
            label fiction_menu:
                $_label="fiction_menu"
                $_block="books_fict"
                jump menu_dahr_book


         
                
         



















        "- Gifts -":
            label gifts_menu:
            menu:
                #dahr "Gifts that you can gift to that special someone."
                
                "- A lolipop (20 g.) -":
                    $ the_gift = "03_hp/18_store/11.png" # CANDY.
                    show screen gift
                    with d3
                    dahr "Lollipop. Adult candy to children or children's candy for adults?"
                    menu:
                        "- buy (20 gold) -":
                            if gold >= 20:
                                $ gold -=20
                                $ order_placed = True
                                $ bought_candy = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu
                            
                "- CHOCOLATE (40 g.) -":
                    $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
                    show screen gift
                    with d3
                    call choco_text
                    menu:
                        "- buy (40 gold) -":
                            if gold >= 40:
                                $ gold -= 40
                                $ order_placed = True
                                $ bought_chocolate = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu
                            
                "- plush owl (35 g.) -":
                    $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL
                    show screen gift
                    with d3
                    call owl_text
                    menu:
                        "- buy (35 gold) -":
                            if gold >= 35:
                                $ gold -= 35
                                $ order_placed = True
                                $ bought_owl = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu
                            
                
                "{color=#858585}- Item us out of stock -{/color}" if whoring < 3: # BUTTERBEER.
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump gifts_menu
                "- butterbeer (50 g.) -" if whoring >= 3: # LEVEL 02.
                    $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER
                    show screen gift
                    with d3
                    call beer_text
                    menu:
                        "- buy (50 gold) -":
                            if gold >= 50:
                                $ gold -= 50
                                $ order_placed = True
                                $ bought_beer = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu

                    
                    
                "- scientific magazine (30 g.) -":
                    $ the_gift = "03_hp/18_store/17.png" # MAGAZINE # 1
                    show screen gift
                    with d3
                    call mag1_text
                    menu:
                        "- buy (30 gold) -":
                            if gold >= 30:
                                $ gold -= 30
                                $ order_placed = True
                                $ bought_mag1 = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu
                
                "- women's magazine (45 g.) -":
                    $ the_gift = "03_hp/18_store/18.png" # MAGAZINE # 2
                    show screen gift
                    with d3
                    call mag2_text
                    menu:
                        "- buy (45 gold) -":
                            if gold >= 45:
                                $ gold -= 45
                                $ order_placed = True
                                $ bought_mag2 = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu


                "- Adult magazine (60 g.) -":
                    $ the_gift = "03_hp/18_store/19.png" # MAGAZINE # 3
                    show screen gift
                    with d3
                    call mag3_text
                    menu:
                        "- buy (60 gold) -":
                            if gold >= 60:
                                $ gold -= 60
                                $ order_placed = True
                                $ bought_mag3 = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu
                            
                
                "{color=#858585}- This item is not in stock -{/color}" if whoring < 3: # PORN MAGAZINES.
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump gifts_menu
                "- porn magazine  (80 g.) -" if whoring >= 3: # LEVEL 02.
                    $ the_gift = "03_hp/18_store/20.png" # MAGAZINE # 4
                    show screen gift
                    with d3
                    call mag4_text
                    menu:
                        "- buy (80 gold) -":
                            if gold >= 80:
                                $ gold -= 80
                                $ order_placed = True
                                $ bought_mag4 = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu


                "{color=#858585}- This item is not in stock -{/color}" if whoring < 3: # CONDOMS.
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump gifts_menu
                "- condoms (50 g.) -" if whoring >= 3: # LEVEL 02.
                    $ the_gift = "03_hp/18_store/10.png" # CONDOMS
                    show screen gift
                    with d3
                    call con_text
                    menu:
                        "- buy (50 gold) -":
                            if gold >= 50:
                                $ gold -= 50
                                $ order_placed = True
                                $ bought_condoms = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu
                
                "{color=#858585}- This item is not in stock -{/color}" if whoring < 3: # VIBRATOR
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump gifts_menu
                "- vibrator (55 g.) -" if whoring >= 3: # LEVEL 02.
                    $ the_gift = "03_hp/18_store/13.png" # VIBRATOR.
                    show screen gift
                    with d3
                    call vib_text
                    menu:
                        "- buy (55 gold) -":
                            if gold >= 55:
                                $ gold -=55
                                $ order_placed = True
                                $ bought_vibrator = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu
                
                "- Bank lubricant (60 g.) -":
                    $ the_gift = "03_hp/18_store/09.png" # ANAL LUBRICANT
                    show screen gift
                    with d3
                    call lub_text
                    menu:
                        "- buy (60 gold) -":
                            if gold >= 60:
                                $ gold -= 60
                                $ order_placed = True
                                $ bought_anal_lube = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu
                

                "- Gag and handcuffs (70 g.) -":
                    $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
                    show screen gift
                    with d3
                    call ball_text
                    menu:
                        "- buy (70 gold) -":
                            if gold >= 70:
                                $ gold -= 70
                                $ order_placed = True
                                $ bought_ballgag = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu
                
                "{color=#858585}- This item is not in stock -{/color}" if whoring < 3: # VIBRATOR
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump gifts_menu
                "- Butt plugs (85 g.) -" if whoring >= 3: # LEVEL 02.
                    $ the_gift = "03_hp/18_store/16.png" # ANAL PLUGS.
                    show screen gift
                    with d3
                    call anal_text
                    menu:
                        "- buy (85 gold) -":
                            if gold >= 85:
                                $ gold -= 85
                                $ order_placed = True
                                $ bought_plug = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu
                
                "{color=#858585}- This item is not in stock -{/color}" if whoring < 3: # VIBRATOR
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump gifts_menu
                "- Strapon \"Thestral\" (200 g.) -" if whoring >= 3: # LEVEL 02.
                    $ the_gift = "03_hp/18_store/14.png" # STRAP-ON.
                    show screen gift
                    with d3
                    call str_text
                    menu:
                        "- buy (200 gold) -":
                            if gold >= 200:
                                $ gold -=200
                                $ order_placed = True
                                $ bought_strapon = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "- Never mind -":
                            hide screen gift
                            jump gifts_menu
                
                
                
                
                "- Never mind -":
                            hide screen gift
                            with d3
                            jump the_oddities
                
                
                
                
                            
                            
        "- Clothes -":
            label app:
                pass
            menu:

                    
           
#                "{color=#858585}-This item is not in stock-{/color}"
#                    show screen bld1
#                    with d3
#                    call out # Message "Item us out of stock".
#                    hide screen bld1
#                    with d3
#                    jump app
                "- \"S.P.E.W.\" badge (100 gold) -" if not badge_01 == 7:
                    $ the_gift = "03_hp/18_store/29.png" # SPEW BADGE.
                    show screen gift
                    with d3
                    dahr "badge \"S.P.E.W.\". simulates the work..."
                    menu:
                        "- buy (100 gold) -":
                            if badge_01 == 7 or badge_01 == 1: # == 7 means "gifted already" # badge_01 == 1 because otherwise you could still buy it in the shop, even if you have 1 already.
                                call do_have_book # "I already own this one."
                                jump app
                            else:
                                if gold >= 100:
                                    $ gold -=100
                                    $ order_placed = True
                                    $ bought_badge_01 = True #Affects 15_mail.rpy
                                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                    jump desk
                                else:
                                    call no_gold #Massage: m "I don't have enough gold".
                                    hide screen gift
                                    with d3
                                    jump app
                        "- Never mind -":
                            hide screen gift
                            with d3
                            jump app
                            
                
                
#                "{color=#858585}-This item is not in stock-{/color}" if whoring < 3: # $ level = "02":
#                    show screen bld1
#                    with d3
#                    call out # Message "Item us out of stock".
#                    hide screen bld1
#                    with d3
#                    jump app
                "- fishnet stockings (800 gold) -" if not nets == 7:
                    $ the_gift = "03_hp/18_store/30.png" # FISHNETS.
                    show screen gift
                    with d3
                    call nets_text
                    menu:
                        "- buy (800 gold) -":
                            if nets == 7 or nets == 1: # == 7 means "gifted already"
                                call do_have_book # "I already own this one."
                                jump app
                            else:
                                if gold >= 800:
                                    $ gold -= 800
                                    $ order_placed = True
                                    $ bought_nets = True #Affects 15_mail.rpy
                                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                    jump desk
                                else:
                                    call no_gold #Massage: m "I don't have enough gold".
                                    hide screen gift
                                    with d3
                                    jump app
                        "- Never mind -":
                            hide screen gift
                            with d3
                            jump app





#                "{color=#858585}-This item is not in stock-{/color}" if whoring < 3: # $ level = "02": MINI SKIRT.
#                    show screen bld1
#                    with d3
#                    call out # Message "Item us out of stock".
#                    hide screen bld1
#                    with d3
#                    jump app
                "- School miniskirt (---) -" if not bought_skirt_already and not gave_miniskirt and whoring >= 3:
                    $ the_gift = "03_hp/18_store/07.png" # MINISKIRT
                    show screen gift
                    with d3
                    dahr "School miniskirt. Dramatically improves the evaluation."
                    menu:
                        "- buy miniskirt (---) -":
                            if vouchers >= 1: #Shows the amount of DAHR's vouchers in your possession.
                                $ vouchers -= 1 #Shows the amount of DAHR's vouchers in your possession.
                                $ order_placed = True
                                $ bought_miniskirt = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                dahr "You can buy this thing only with \" Dahr's voucher\"."
                                dahr "Something wrong..."
                                dahr "damn Russian..."
                                dahr "Im..."
                                translators "That's better. This moment seemed all rather complicated. I'm on the skirt. Next will be a clue how to get it."
                                menu:
                                    "- look hint -":
                                        translators "{size=14}Tip of the translator:\nYou can find it if right read the book {b}[book07]{/b}{/size}."
                                        translators "{size=14}more details {a=http://wtrus.ixbb.ru/viewtopic.php?id=19}here{/a}{/size}."
                                    
                                    "- dont need -":
                                        translators "at will."
                                hide screen gift
                                with d3
                                jump app
                        "- Never mind -":
                            hide screen gift
                            with d3
                            jump app
#                "- Item Sold Out -" if bought_skirt_already:
#                    "This item has been sold out."
#                    jump app
                            
                            
                            
                "- Item Sold Out -" if bought_dress_already:
                    "This item has been sold out."
                    jump app
                "{color=#858585}- This item is not in stock -{/color}" if not sorry_for_hesterics: # NIGHT DRESS.
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump app
                "- Evening dress (1500 gold) -" if sorry_for_hesterics and not bought_dress_already:
                    $ the_gift = "03_hp/18_store/01.png" # DRESS.
                    show screen gift
                    with d3
                    dahr "Evening dress for special occasions."
                    menu:
                        "- buy (1500 gold) -":
                            if gold >= 1500:
                                $ gold -=1500
                                $ order_placed = True
                                $ bought_ball_dress = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                with d3
                                jump app
                        "- Never mind -":
                            hide screen gift
                            with d3
                            jump app
                            
                "- Never mind -":
                        jump the_oddities
                        
        "- SACRED SCROLL. Chapter I -":
            label sscrolls:
            menu:

                "- С.01: [scroll_01_name] -" if not sscroll_01:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_01 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                
                "- С.02: [scroll_02_name] -" if not sscroll_02:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_02 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                
                "- С.03: [scroll_03_name] -" if not sscroll_03:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_03 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.04: [scroll_04_name] -" if not sscroll_04:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_04 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.05: [scroll_05_name] -" if not sscroll_05:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_05 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.06: [scroll_06_name] -" if not sscroll_06:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_06 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.07: [scroll_07_name] -" if not sscroll_07:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_07 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.08: [scroll_08_name] -" if not sscroll_08:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_08 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.09: [scroll_09_name] -" if not sscroll_09:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_09 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.10: [scroll_10_name] -" if not sscroll_10:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_10 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                                
                "- С.11: [scroll_11_name] -" if not sscroll_11:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_11 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                
                "- С.12: [scroll_12_name] -" if not sscroll_12:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_12 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                
                "- С.13: [scroll_13_name] -" if not sscroll_13:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_13 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
        
                "- С.14: [scroll_14_name] -" if not sscroll_14:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_14 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                
                "- С.15: [scroll_15_name] -" if not sscroll_15:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_15 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls
                
                
                "- Never mind -":
                    jump the_oddities
                    
        "- SACRED SCROLL. Chapter II -":
            label sscrolls2:
            menu:

                "- С.16: [scroll_16_name] -" if not sscroll_16:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_16 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                
                "- С.17: [scroll_17_name] -" if not sscroll_17:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_17 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                
                "- С.18: [scroll_18_name] -" if not sscroll_18:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_18 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.19: [scroll_19_name] -" if not sscroll_19:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_19 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.20: [scroll_20_name] -" if not sscroll_20:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_20 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.21: [scroll_21_name] -" if not sscroll_21:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_21 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.22: [scroll_22_name] -" if not sscroll_22:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_22 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.23: [scroll_23_name] -" if not sscroll_23:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_23 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.24: [scroll_24_name] -" if not sscroll_24:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_24 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.25: [scroll_25_name] -" if not sscroll_25:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_25 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                                
                "- С.26: [scroll_26_name] -" if not sscroll_26:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_26 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                
                "- С.27: [scroll_27_name] -" if not sscroll_27:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_27 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                
                "- С.28: [scroll_28_name] -" if not sscroll_28:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_28 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
        
                "- С.29: [scroll_29_name] -" if not sscroll_29:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_29 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2
                
                "- С.30: [scroll_30_name] -" if not sscroll_30:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Buy scroll (30 gold) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_30 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Never mind -":
                            hide screen gift
                            jump sscrolls2





                "- Never mind -":
                    jump the_oddities

        "- Never mind -":
            jump desk
        
        
### ALREADY HAVE THIS BOOK
label do_have_book:
    show screen bld1
    m "У меня уже есть эта книга."
    hide screen bld1
    hide screen gift
    with d3
    return
### THANK YOU FOR shopping here.
label thx_4_shoping:
    $ days_in_delivery2 = one_of_five  #Generating one number out of three for various porpoises.

    if one_of_five ==  1:
        dahr "Спасибо gа покупку в \"Приблудах Дахра\". Ваш gакаg будет доставлен gавтра."
        hide screen gift
        with d3
        return
    else:
        dahr "Спасибо gа покупку в \"Приблудах Дахра\". Ваш gакаg будет доставлен в течении 1 - [one_of_five] дней."
        hide screen gift
        with d3
        return
    
### THANK YOU FOR shopping here. IMMEDIATE DELIVERY.
label thx_4_shoping2:
    dahr "Спасибо gа покупку в \"Приблудах Дахра\"."
    hide screen gift
    with d3
    return
### NOT ENOUGH GOLD ###
label no_gold:
    m "У меня нет столько gold... Это удручает..."
    hide screen gift
    with d3
    return
    
### This item is not in stock ###

label out:
    dahr "This item is not in stock"
    return

### SACRED SCROLL MASSAGE ###
label sscroll:
    dahr "SACRED SCROLL.\n(Может содержать спойлеры)."
    return
    
### BOUGHT SACRED SCROLL MESSAGE ###
label sscroll_bought:
    ">Новый свиток был добавлен в вашу коллекцию."
    hide screen gift
    with d3
    return
    
### CHOCOLATE BAR DESCRIPTION ###
label choco_text:
    dahr "Рецепт этого восхитительного молочного шоколада держится в секрете. (По слухам, он содержит сушеных фей)."
    return

### TOY OWL ###
label owl_text:
    dahr "Игрушечная сова, набитая перьями настоящей совы. Она такая мягкая!"
    return
    
### BUTTERBEER ###
label beer_text:
    dahr "Девушки не могут устоять перед этим вкусом. Поэтому всегда польgуются большим спросом среди мальчиков. \n {size=-4}. Предупреждение: употребление алкоголя не допускается несовершеннолетними, беg присмотра вgрослых {/size}"
    return
          
### MAGAZINES ###
label mag1_text:
    dahr "Обраgовательный журнал. \nВерный спутник каждого иgгоя."
    return
          
label mag2_text:
    dahr "Женский журнал. \nВсе крутые девчонки читают их."
    return
    
label mag3_text:
    dahr "Ваш парень превращается в хорошего мальчика? \nВаш муж больше не испольgует вас по наgначению?\nВсе, что вы ждали о отношениях, любви и сексе. В основном о сексе."
    return
    
label mag4_text:
    dahr "Дайте их своей девушке, чтобы проверить ее, своей жене, чтобы постыдить ее и вашей дочери, чтобы иgбежать \"раgговоров\"."
    return
    
### CONDOMS ###
label con_text:
    dahr "\"Преgервативы Роgовый единорог\". \nПокажите всем однорогое существо!\n{size=-4}Может содержать слюну реального единорога.{/size}"
    return
    
### VIBRATOR ###
label vib_text:
    dahr "Великолепный, волшебный усиленный вибратор иgготовлен иg лоgы дерева, с ядром жилы дракона."
    return
    
### ANAL LUBRICANT ###
label lub_text:
    dahr "Банка анальной смаgки. Купите это любимому человеку - покажите, что вы gаботитесь о нем/ней."
    return

### BALL GAG AND CUFFS ###
label ball_text:
    dahr "Кляп и манжеты, превратите свою вторую половинку в вашего сокамерника."
    return
          
### ANAL PLUGS ###
label anal_text:
    dahr "Анальные пробки украшены настоящими хвостами. \n Раgные раgмеры, чтобы удовлетворить экспертов, практиков и начинающих."
    return
          
### STRAP-ON ###
label str_text:
    dahr "Cтрапон \"Фестрал\".\nКогда вы его увидите - потеряете дар речи."
    return

### FISHNETS ###
label nets_text:
    dahr "Ажурные чулки. Вопреки распространенному мнению, они не были иgобретены рыбаком."
    return