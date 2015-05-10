#play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
#stop music fadeout 2.0
label daphne_approaching(isKnocking=False):   

#    $ menu_x = 0.2 #Menu is moved to the left side.
#    $ pos = POS_410
                
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    $ hermione_chibi_xpos = 400 #Near the desk.
#    show screen hermione_02 #Hermione stands still.
#    show screen bld1
#    with d3
#    $daphne.LoadDefItemSets()

#    if this.IsStep("DAPHENTER"):
    if hero._perfumeused==time.stamp:
        $daphne.chibi.State("center").Trans(d4, "blink")
        $daphne.Visibility("body+", False)
        $daphne("~55 01 1 dis// Sir... Ahhm... Sorry, but...")
        $hero ("Yes, girl?")
        $daphne("~55 00 1 dis// What you talking about?...")
        $hero("?!")
        $daphne("~55 s0 1 dis// what rats poisoned?!// I can't single second here to stay!")
        $daphne.liking-=5
        $daphne.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        pause.5
        call music_block
# Завершение ивента, который исполнялся 
        jump expression ["day_main_menu", "night_main_menu"][1-daytime]   


    $this.RunStep("DAPHENTER")  

    $daphne.chibi.State("center").Trans(d4, "blink")
    $daphne.Visibility("body+", False)


    python:
        for t in [
            (0, ["~55 00 1 def// Yes, Professor?"]),
            (-2, ["~55 00 1 neu// >looks Like Daphne is still a little upset you..."]),
            (-9, ["~55 00 1 pri// >You upset Daphne."]),
            (-19, ["~37 00 1 pri// >Daphne really upset you."]),
            (-39, ["~26 00 1 dis// >Daphne gets mad at you."]),
            (-49, ["~26 00 1 dis// >Daphne is very mad at you."]),
            (-59, ["~26 s0 1 dis// >Daphne is angry with you."]),
            (-100, ["~26 s0 1 dis// >Daphne hates you."])
            ]:
            (_val, _texts)=t
            if daphne.liking>=_val:
                for s in _texts:
                    daphne(s)
                break

    

    label daphne_main_menu:
    menu:
        "- Chit-chat -" if not daphne.IsTalk():
            $daphne.CommitTalk() #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
            if daphne.liking >= -7:
                jump daphne_chat
            else:
                $daphne("~37 00 1 pri// I have nothing to say to you...")    
                jump daphne_main_menu

        "- Training -" if this.daphne_pre_finish.IsFinished():#buying_favors_from_hermione_unlocked:
            if daphne.liking<0:
                python:
                        for t in [
                        (-2, "~55 00 1 neu// I'm sorry, Professor, maybe another time..."),
                        (-9, "~55 00 1 pri// I don't want today...\nMay be a couple of days..."),
                        (-19, "~37 00 1 pri// No, thanks...."),
                        (-29, "~26 00 1 dis// After what you did?\nI don't think so..."),
                        (-39, "~26 00 1 dis// are You serious!?"),
                        (-100, "~26 s0 1 dis// This is a corny joke?!\nAfter what you did, I don't want to repeat it!")
                        ]:
                            (_val, _text)=t
                            if daphne.liking>=_val:
                                daphne(_text)
                                break
                jump daphne_main_menu
            else:
                label daphne_main_menu_requests:
                    $choose = RunMenu()
                    python:
                        for o in this.List:
                            if o._points!=None:
                                if (("daphne_public" in o._points and daytime) or "daphne_private" in  o._points):
                                    choose.AddItem(str(o._caption), None, o.Name)        
                        choose.Show("daphne_main_menu")

                    $daphne.Visibility("body+")
                    $hero(m,this(choose.choice)._eventPlan)
                    menu:
                        "\"(Yes, lets do it.)\"":
                            if this(choose.choice)._finishCount>=3:
                                pause 1.0
                                skaz "Sorry to interrupt the most interesting place? "
                                skaz "Us too. But this storyline so far finished only up to this point..."
                                skaz "(however, you have access to the other storylines)."
                                skaz "Leave your questions, thanks and wishes on our {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}FORUM{/a}. \Ptak you stimulate us and the continuation will appear faster. :)"
                                jump daphne_main_menu_requests 

                            call expression this(choose.choice).Name
                        "\"(Not now.)\"":
                            jump daphne_main_menu_requests 
                    
                    if not event.Name in {"dap_request_01"}: # Дневные задания или задания на которых не обещается подрок
                        call daphne_pre_menu(_return) # Вызов меню подарков
                    else:
                        $screens.HideD3("bld1")
                        $daphne.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        pause.5
                        call music_block
# Завершение ивента, который исполнялся 
                    if event._scenario==None: 
                        $event.Finalize("day_main_menu" if daytime else "night_main_menu")    
                    else:
                        $event.Finalize("night_start" if daytime else "day_start")    


                     
        
        
        "- Give her a gift -" if not daphne.IsGift():
            $ choose = RunMenu()
            python:
                for o in hero.Items():
                    if not o.Name in {"scroll", "ball_dress"}:
                        choose.AddItem("- "+o._caption+" -", 
                            "daphne_giving" , o.Name)

            $ choose.Show("daphne_main_menu")


                    
        

# Пока комментировать? сделать в следующих версиях
#        "- Гардероб -" if dress_code:
#            python:
#                if daphne.liking<0:
#                    for t in [
#                    (-2, "Мне жаль, профессор, может быть в другой раз..."),
#                    (-9, "Мне не хочется сегодня...\nМожет быть через пару дней..."),
#                    (-19, "Нет, спасибо...."),
#                    (-29, "После того, что вы сделали?\nЯ так не думаю..."),
#                    (-39, "Вы серьезно!?"),
#                    (-100, "Это какая-то ваша пошлая шутка?!\nПосле того, что вы сделали, я не хочу повторять это!")
#                    ]:
#                        (_val, _text)=t
#                        if daphne.liking>=_val:
#                            renpy.say(her, _text)
#                            break
#                else:
#                    choose = RunMenu()
#                    for o in daphne.Items():
#                        if o.Name in {"badge_01", "nets", "miniskirt"}:
#                            choose.AddItem("- "+("Надеть" if o._status==0 else "Снять")+" "+o._caption+" -", 
#                                "daphne_item_"+("on" if o._status==0 else "off"), True, o.Name)

#                    choose.Show("daphne_main_menu")                            
#            jump daphne_main_menu            




       
        
        "- Ask people to leave -":
#                        if daytime:
#                            play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
#                        else:
#                            play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
            $ menu_x = 0.5 #Menu position is back to default. (Center).

            if daphne.liking>=-2:
                $daphne(["Oh, good! Then I'll go to class.", "Oh, good! Then I'll go to sleep."][0 if daytime else 1])
            elif daphne.liking >= -6:
                $daphne("...............................")
            else: 
                $daphne(["*Ahem!*...", "Pfff!..."][0 if daytime  else 1])


            label daphne_goout:
#            hide screen bld1
#            $herView.hideQ() 
#            hide screen blktone 
#            hide screen hermione_02
#            hide screen ctc
#            with d3

            $daphne.Visibility()
            $daphne.chibi.Hide()
            $screens.Hide("bld1", "blktone", d3, "ctc")

            if daytime:
#                $ hermione_takes_classes = True
                jump day_main_menu
            else:
#                $ hermione_sleeping = True
                jump night_main_menu

       

        
### CHITCHAT WITH DAPHNE ###
label daphne_chat:
    if this.IsStep("DAPHNECHAT"):
        $ this.RunStep("DAPHNECHAT")
    else:
        $daphne("~55 00 1 def")
        if daphne.whoring in {0,1,2}:
            $daphne([
            "~46 00 1 ope// Lugradio - fight!// That should be a commandment for each real wizard!",
            "~37 00 1 pri// Today, the Mudblood Granger again received the highest score. Where to watch the Ministry?!//"
                "~37 01 1 pri// So soon among certified wizards won't be a pureblood.",
            "~55 00 1 smi// Today \"Thoroughbred news\" has published a list of pureblood Wizarding England. Greengrassi - in the first dozen!//"
                "~55 00 1 gri// You there too - on the penultimate line.",
            "~55 00 1 ehh// my Mom says that I will be able to discover their real talents, only if I get the right position. You think so too?",
            "~55 00 1 pou// My owl Puhle you drink too much bird feed and are now unable to fly anywhere.//"
                "~55 00 1 smi// But I will never change to another.//"
                "~55 c0 1 smo// It is also very pureblood!"
            ][Rand(5)-1])
        elif daphne.whoring in {3,4,5}:
            $daphne([
            "~64 00 1 dis// the Contest is approaching, and I felt really bad. Sometimes I want to drink, to relax a little...//"
                "~55 01 2 ehh// Oh, sorry, Professor, snapped. I'm not that mean!",
            "~64 00 1 def// Today, some half-breed spoke to me.//~64 00 1 dis// I even thought that he was trying me to glue.//"
                "~55 00 1 pri// what an ego some!",
            "~55 00 1 def// This Ghost - PEPs, you know it, today in confidence told me that too, from some ancient kind.//"
                "And I imagine he was very convincing.//~55 00 1 neu// Strange - he usually doesn't act.",
            "~37 00 1 pur// I hope that with your help, Professor, I morning the nose is all that base-born, half-blood, and of course, mugatu.",
            "~55 00 1 def// Today was a match and I did a dance cheer me with its elegance.//"
                "~37 n2 2 def// Some guys were staring at me...// ~37 00 2 pou// But doesn't do any good, sir!"
            ][Rand(5)-1])


    jump daphne_main_menu

