label menu_dahr_book:
    $ choose = RunMenu()
    python:
        for e in this.List:
            if e.GetValue("block")==_block: # Нужно ставить GetValue("block")  а не _block - у ивента такого объекта может не быть
                choose.AddItem("- Книга: "+e._caption+" - "+("{image=check_08.png}" if e._status>-2 else "{image=check_07.png}"), 
                    "menu_dahre_book_2", e.Name)

    $ choose.Show("the_oddities")

    label menu_dahre_book_2:
        $ the_gift = event._img     # "03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3
        dahr "\"[event._caption]\". [event._description]\n"
        if event._status>-2: 
            call do_have_book
            jump the_oddities
        menu:
            "- Buy the book for [event._price] galleons -":
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


label menu_dahr_gifts_and_gears:
    $ choose = RunMenu()
    python:
        for o in itsDAHR():
            if not (o.Name in {"scroll"}): 
                _temp={"candy": fn0, "chocolate": fn0, "owl": fn0, "beer": fn3, "mag1": fn0, "mag2": fn0, "mag3": fn0, "mag4": fn3,
                     "condoms": fn3, "perfume": fn0,"vibrator": fn3, "lubricant": fn0,"ballgag": fn0, "plug": fn3, "strapon": fn3,
                     "ball_dress": lambda e: this.Has("sorry_about_hesterics"), "badge_01": fn0, "nets": fn0, 
                            "miniskirt": lambda e: hermi.whoring >= 3 and (hero.Items.Count("miniskirt")+hermi.Items.Count("miniskirt")+itsOWL.Count("miniskirt")==0)}[o.Name](o)

#            elif _block=="gears" and o._block=="gears": 
                if o._block==_block:
                    choose.AddItem("- "+o._caption+" - ("+str(o._price)+" gal.) -" if _temp and itsDAHR.Count(o.Name)>0 else "{color=#858585}- The product is temporary unavailable -{/color}", 
                        "menu_dahr_gift_order" if _temp else "out", o.Name)

    $ choose.Show("the_oddities") 



label menu_dahr_gift_order:
    if _block=="scroll":
        $item=itsDAHR("scroll")
    else:
        $item=itsDAHR(choose.choice)
    label menu_dahr_scroll_order:
    $ the_gift = item._img # CANDY.
    show screen gift
    with d3
    $itemCount=0
    if item.Name=="miniskirt":
        menu:
            "- Buy the skirt (---) -":
                if vouchers >= 1: #Shows the amount of DAHR's vouchers in your possession.
                    $ vouchers -= 1 #Shows the amount of DAHR's vouchers in your possession.
                    $ order_placed = True
                    $itsOWL.AddItem(item.Name)
                    $itsDAHR.AddItem(item.Name,-1)
                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                    jump desk
                else:
                    dahr "This item is only redeemable with a \"DAHR's voucher\"."
                    dahr "Something wrong..."
                    dahr "Damn Russian..."
                    dahr "Im..."
                    translators "That's better. This moment seemed all rather complicated. I'm on the skirt. Next will be a clue how to get it."
                    menu:
                        "- Look hint -":
                            translators "{size=14}Tip of the translator:\nYou can find it if right read the book {b}[book07]{/b}{/size}."
                            translators "{size=14}More details {a=http://wtrus.ixbb.ru/viewtopic.php?id=3#p4}here{/a}{/size}."
                        
                        "-I dont need this -":
                            translators "KEK."
                    hide screen gift
                    with d3
                    jump app
            "- Never mind -":
                hide screen gift
                with d3
                jump app

    if itsDAHR.Count(item.Name)>0:
        if item._block=="gears":
            menu:
                dahr "[item._description]"
                "- Buy for ([item._price] galleons) -":
                    $itemCount=1
                "- Never mind -":
                    hide screen gift
                    jump the_oddities
        else:
            $_price2=item._price*2
            $_price3=item._price*3
            if itsDAHR.Count(item.Name)>0:
                menu:
                    dahr "[item._description]"
                    "- Buy 1 for ([item._price] galleons) -":
                        $itemCount=1
                    "- Buy 2 for ([_price2] galleons) -" if itsDAHR.Count(item.Name)>1:
                        $itemCount=2
                    "- Buy 3 for ([_price3] galleons) -" if itsDAHR.Count(item.Name)>2:
                        $itemCount=3
                    "- Never mind -":
                        hide screen gift
                        jump the_oddities


        if gold >= item._price*itemCount:
            hide screen points
            $ gold -=item._price*itemCount
            show screen points
            $ order_placed = True
            $itsOWL.AddItem(item.Name,itemCount)
            if item.Name in {"scroll", "ball_dress"}:
                $itsDAHR.AddItem(item.Name,-itemCount)
    #        $ bought_candy = True #Affects 15_mail.rpy
            call thx_4_shoping #Massage that says "Thank you for shopping here!".
            jump desk
        else:
            call no_gold #Massage: m "I don't have enough gold".
            jump the_oddities

    else:
        ">Sorry, this item has ended"
        hide screen gift




label the_oddities:
    $choose=None
    menu:
        dahr "Welcome to \"Dahr's oddities\". Your preferences will not seem strange to us!"
        "- Educational books -":
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
                $_block="gifts"
                jump menu_dahr_gifts_and_gears
                
                            
                            
        "- Clothes -":
            label app:
                $_block="gears"
                jump menu_dahr_gifts_and_gears



        "- The sacred scrolls -":
            label sscrolls:
                $_block="scroll"
                jump menu_dahr_gift_order

        "- Never mind -":
            jump desk
        
        
### ALREADY HAVE THIS BOOK
label do_have_book:
    show screen bld1
    m "I already own this one."
    hide screen bld1
    hide screen gift
    with d3
    return
### THANK YOU FOR shopping here.
label thx_4_shoping:
# Пока не было объекта Item книги были сделаны через объект Event. Вероятно, надо переделать, через Item, но из-за спешки при подготовке к релизу пока пусть будет костыль
    if "books_" in _block:
        $_caption=event._caption
        $_price=event._price
        $itemCount=1
    else:
        $item=itsOWL()[0]
        $itemCount=itsOWL.Count(item.Name)
        $_caption=item._caption
        $_price=item._price
    $ days_in_delivery2 = one_of_five  #Generating one number out of three for various porpoises.
    if days_in_delivery2==1:
        $days_in_delivery2+=1 # Назавтра только экспресс
        $days_in_delivery2+=itemCount-1  # Удлинняется, если несколько предметов

    if gold >= _price*itemCount//2:
        menu:
            dahr "You ordered [itemCount] items \"[_caption]\". You pay for Express delivery?"
            "Express-delivery (+50%% for urgency)":
                $days_in_delivery2=1
                $gold -= _price*itemCount//2
                dahr "Thanks for buying in \"Dahr's oddities\". Your order will be delivered tomorrow."
            "Typical delivery":
                dahr "Thanks for buying in \"Dahr's oddities\".Your order shall be delivered in 1 to [days_in_delivery2] days."

        hide screen gift
        with d3
        return
    
### THANK YOU FOR shopping here. IMMEDIATE DELIVERY.
label thx_4_shoping2:
    dahr "Thank your for shopping at \"Dahr's oddities\"."
    hide screen gift
    with d3
    return
### NOT ENOUGH GOLD ###
label no_gold:
    m "I don't have enough money... This is depressing..."
    hide screen gift
    with d3
    return
    
### ITEM IS OUT OF STOCK ###

label out:
    dahr "This item is currently out of stock."
    jump the_oddities
#    return

