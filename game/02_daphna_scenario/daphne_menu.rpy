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
    $this.RunStep("DAPHENTER")  

    $daphne.chibi.State("center").Trans(d4, "blink")


    $daphne.Visibility("body+", False)

    $felixblock = False
    
    python:
        for t in [
            (0, ["daphne:> ~55 00 1 def// Да, профессор?"]),
            (-2, [">Похоже, Дафна по-прежнему немного расстроена вами..."]),
            (-9, [">Вы расстроили Дафну."]),
            (-19, [">Дафна очень расстроена вами."]),
            (-39, [">Дафна злится на вас."]),
            (-49, [">Дафна очень злится на вас."]),
            (-59, [">Дафна гневается на вас."]),
            (-100, [">Дафна ненавидит вас."])
            ]:
            (_val, _texts)=t
            if daphne.liking>=_val:
                for s in _texts:
                    Say(s)
                break

    

    label daphne_main_menu:
    menu:
        "- Chit-chat -" if not daphne.IsTalk():
            $daphne.CommitTalk() #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
            if daphne.liking >= -7:
                jump daphne_chat
            else:
                $daphne("Мне нечего сказать вам...")    
                jump daphne_main_menu

        "- Training -" if this.daphne_pre_finish.IsFinished():#buying_favors_from_hermione_unlocked:
            if daphne.liking<0:
                python:
                        for t in [
                        (-2, "Мне жаль, профессор, может быть в другой раз..."),
                        (-9, "Мне не хочется сегодня...\nМожет быть через пару дней..."),
                        (-19, "Нет, спасибо...."),
                        (-29, "После того, что вы сделали?\nЯ так не думаю..."),
                        (-39, "Вы серьезно!?"),
                        (-100, "Это какая-то ваша пошлая шутка?!\nПосле того, что вы сделали, я не хочу повторять это!")
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
                                skaz "Жаль прерываться на самом интересном месте?"
                                skaz "Нам тоже. Но данная сюжетная линия пока дописана только до этой точки..."
                                skaz "{size=-3}(впрочем, вам доступны другие сюжетные линии){/size}"
                                skaz "Оставьте ваши вопросы, благодарности и пожелания на нашем {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}ФОРУМЕ{/a}."
                                skaz "Так вы простимулируете нас и продолжение появится быстрее. :)"
                                jump daphne_main_menu_requests 

                            call expression this(choose.choice).Name
                        "\"(Not now.)\"":
                            jump daphne_main_menu_requests 
                    
                    if not wtevent.Name in {"dap_request_01", "IsRunNumber(4)"}: # Дневные задания или задания на которых не обещается подрок
                        call daphne_pre_menu(_return) # Вызов меню подарков
                    else:
                        $screens.HideD3("bld1")
                        $daphne.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        pause.5
                        call music_block
# Завершение ивента, который исполнялся 
                    if wtevent._scenario==None: 
                        $wtevent.Finalize("day_main_menu" if daytime else "night_main_menu")    
                    else:
                        $wtevent.Finalize("night_start" if daytime else "day_start")    


                     
        
        
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




       
        
        "- Ask her to leave -":
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
        if daphne.whoring in {0,1,2,3,4,5,6}: 
            $daphne([
            "~46 00 1 ope// Fight the Mudbloods!// That should be a commandment for each true wizard!",
            "~37 00 1 pri// Today, that Mudblood Granger again received the highest score. Where is the Ministry when you need them?!//"
                "~37 01 1 pri// Soon there won't be a pureblood anomg certified wizards.",
            "~55 00 1 smi// Today \"Pureblood Post\" has published a list of pureblood Wizards in England. Greengrass are in the top 10!//"
                "~55 00 1 gri// You where listed as well - second to last.",
            "~55 00 1 ehh// My mother says that I will only be able to discover my real talents, if I get to the right position. Do you agree?",
            "~55 00 1 pou// My owl Puglia ate too much food and is now unable to fly anywhere.//"
                "~55 00 1 smi// But I would never replace her.//"
                "~55 c0 1 smo// She is also a true pureblood!"
            ][Rand(5)-1])
        elif daphne.whoring in {7,8,9,10,11,12}:
            $daphne([
            "~64 00 1 dis// The competition is approaching and the stress is getting to me. I could us a to drink sometimes, to relax a little...//"
                "~55 01 2 ehh// Oh, sorry, Professor, that slipped out. I didn't mean it!",
            "~64 00 1 def// Today, some half-breed boy spoke to me.//~64 00 1 dis// I even thought that he was trying to get close to me.//"
                "~55 00 1 pri// He doesn't know his place!",
            "~55 00 1 def// This Ghost - Myrtle, you know her, told me today in confidence that you come very from a ancient linage as well.//"
                "And she was very convincing.//~55 00 1 neu// Strange, she usually doesn't talk to me.",
            "~37 00 1 pur// I hope that with your help, Professor, I can put all these muggles, half-bloods, and of course, mudbloods in their place.",
            "~55 00 1 def// There was a match today and my cheerleading was more then elegant.//"
                "~37 n2 2 def// Some guys were staring at me...// ~37 00 2 pou// Not sure I approve of that, sir!"
            ][Rand(5)-1])

# Добавить новую ветку разговоров # Придумывать надо

    jump daphne_main_menu

