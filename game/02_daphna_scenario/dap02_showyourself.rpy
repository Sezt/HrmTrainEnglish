#########################
######### LEVEL 02 ##########
#########################
####REQUEST_02 Show Your Self####
#########################
label dap_request_02: #LV.2 (Whoring = 3 - 9)
    
    $music("Daphne Theme")

label dap_request_02_complete:
    if daphne.whoring < 3:
        $hero("Похоже что она еще не готова к этому разговору...// Может позже....")
        call daphne_main_menu_requests
    pass
    if IsRunNumber(1):
        $hero("Alright, miss Greengrass. The time has come to work on your stage presence. Are you ready?")
        $daphne("~55 00 1 def// Yes, sir, what do you want me to do? Walk around?")
        $hero("No, miss, lie down.")
        $daphne("~46 w0 1 def// ...?!")
        $hero(g4, "Oh, I'm sorry, miss, I looked at you and suddenly started daydreaming...")
        $daphne("~37 s0 1 neu// About what?")
        $hero("What? About... about some faculty problems, Yeah...",
            m," And no, we want to start with something less complicated then \"walk or lie down\"...you should reduce the amount clothes you wear.")
        $daphne("~37 c0 1 dis// Clothes, sir? But... I'm already wearing, what my mom would consider, a whore outfit!")
        $hero("Miss Greengrass, the competition is not for your mom. You have to focus on the jury, who expect to see the contestants in suitable outfits.// Of course, you could go to the podium in your usual uniform.//"
         "But I don't think it would show of your style. A minimum of clothes would really show of your appearance to the members of the jury.")
        $daphne("~73 c0 1 pri// But, sir. That is terrible. I will be thought of as a price pony...!")
        $hero("#Hehe, I think \"bitch\" would be better.")
        $daphne("~73 00 1 pri// You said something, sir?")
        $hero("Oh, nevermind, miss. So where would you like to begin?")
        $daphne("~73 00 1 ehh// Well, I can change my top to be a bit more revealing. I hope that is enough?")
        $hero("Miss, it is your competition, your success or your failure. You decide what is enough.")
        $daphne("~73 01 1 pur// Hmm... Well, I hope it is.")

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $daphne.ItemsCustomize(delete={"sleeves"}).chibi.State(appearance="c")#.Refresh()
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("You have lovely hands, miss Greengrass, I've never seen them naked.")
        $daphne("~73 00 2 ang// Oh please, sir.")
        $hero ("The green straps of your bra clash a bit with the rest.")
        $daphne("~73 00 2 pou// But, sir, I figured that I would be almost...")
        $hero("naked in front of a man?")
        $daphne("~73 n2 3 def// Well, yeah...")
        $hero("It's all right, miss. You look very attractive. I think you deserved a small reward.")
        $daphne.whoring += 1
    elif IsRunNumber(2):
        $hero("Well, miss Greengrass. Let's continue to work on your stage presence.")
        $daphne("~55 00 2 def// Should I walk or something else?")
        $hero("Something else! You need to remove another item of clothing.")
        $daphne("~46 00 2 ehh// Well alright, I have long wanted to take off these stockings, I look like a bloody freak.")

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $daphne.ItemsCustomize(delete={"stockings"}).chibi.State(appearance="c")#.Refresh()
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("Вот это энтузиазм! Вам следует сохранять его, мисс, пока вы будете снимать всю остальную одежду.")
        $daphne("~46 w0 1 ehh// ���?!...")
        $hero(g4, "Эм... Это я образно, мисс.",m ,"Давайте лучше посмотрим, что я сегодня смогу вам подарить.")
        $daphne.whoring += 1
    elif IsRunNumber(3):
        $hero("Alright, miss Greengrass, we are getting close to a pleasant outfit for the compitition.")
        $daphne("~55 00 1 neu// Sir, I thought this was the final look!")
        $hero("Not at all, miss, we still have some work ahead of us. It's time to lose another item.")
        $daphne("~55 00 1 ehh// Like what?")
        $hero("You decide for yourself, miss.")
        $daphne("~26 01 2 ope// You don't think, sir, that I'll show you my underwear?! What would that look like?!")
        $hero("On stage you should only be in what you call underwear, miss.//"
            "By the way, I'm sure YOUR underwear is of the highest quality and matched with your inherent style and grace...//"
            "You shouldn't be ashamed to show that of even in the most elegant enviroment.")
        $daphne("~26 01 smi 2// Uhm...you are certainly right, sir.")
        $hero("#(Fucking Sands, having to watch my language and not blurt out \"On your knees, slut!\")")
        $daphne("~37 00 smi 2// I mean, you are certainly right about my gracefulness...//~73 00 smi 2// Sir?")
        $hero("Huh? Yeah, so I...I would gladly admire your underwear, miss. When you are ready, of course.")
        $daphne("~01 2 73 ehh// Oh... I don't know...is it really graceful, as a sorceress descended from Merlin I should know that!...")
        $hero("#(Not this again. My dick is the only part that is not tired of her...)")
        $daphne("~73 01 2 pur// I'm not ready, sir. But I need to remove something...//~55 01 2 pou// Then I will take this off. Turn around, sir!//~55 01 3 pou// Better yet, I'll turn around.")

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"}).chibi.State(appearance="f")#.Refresh()
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") 
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("Urgh, you decided to show me your erect nipples? I appreciate that, they are excellent!")
        $daphne("~37 00 2 ope// What?! Sir!")
        $hero("Miss Greengrass, you could have taken off your shirt and I would not have been able to see such beautiful details.// But you decided to show me your excitement.")
        $daphne("~26 00 wo 3// What? No! How dare you!")
        $hero("Miss Greengrass, don't be angry, that you get excited when exposing yourself to the man is very good news.// This will not only help you during the competition.")
        $daphne("~26 00 3 ope// That is not because I took off my bra, just so you know!")
        $hero("Hmm. Are you excited about the thought that you will stand in front of an audience in your underwear?")
        $daphne("~26 00 3 dis// Sir, this is going to far!!! I will immediately complain to my parents!")
        $hero("You never told them that you are trying to become Miss Hogwarts.//"
            "They don't even read \"The Daily Prophet\", right?")
        $daphne("~55 s0 3 pou")
        $hero("I suppose you wanted to come home with a victory or keep it a secret if you failed.//"
            "Very unlikely you will be able to hide that from your mother, girl, when you get knocked out in the first round.//"
            "Your enemies or the faculty will take care of that.//")
        $daphne("~37 01 3 dis// ........................")
        $hero("#(Похоже, я все же немного перегнул палку... Но думаю, девушка слишком много поставила на этот конкурс, так что все обойдется.)//"
            "Мисс, конечно, как поступить, решать вам.// Но в знак моего особого к вам отношения подарок вам я все равно приготовил.")
        $daphne.whoring += 1
        $daphne.liking-=7
    elif IsRunNumber(4):
        $hero("Ну что ж, мисс Гринграсс, вы выглядите потрясающе....")
        $daphne("~73 01 1 smi// ....Спасибо профессор.")
        $hero("За исключением одного «но»....")
        $daphne("~37 n0 1 pou// «но»....// Что-то не так, сэр?//~37 00 2 neu// Мне ведь уже нечего снимать....")
        $hero(g9, "#(Это мы еще проверим)")
        $daphne("~73 00 2 pri// Что, сэр?")
        $hero(m, "Эм.... Я говорю, что сегодня вам нужно научиться правильно демонстрировать свое нижнее белье.")
        $daphne("~26 00 3 dis// {size=+5}Всмысле?!{/size}")
        $daphne("{size=+5}Сэр, это не позволительно!{/size}")
        $hero(".................// А два дня назад мне показалось, что для вас это в порядке вещей.....// Ну тогда надейтесь на удачу.....// Только она сможет вам помочь.....// Можете быть свободны мисс Гринграсс....")
        $daphne("~55 00 2 dis// Пф!...")
        $daphne.liking-=15
        $wtevent.Finalize("daphne_goout")
        $hero(g4, "#(Не умеешь ты держать рот на замке, Джинни)")
    elif IsRunNumber(5):
        if daphne.whoring < 5:
            $daphne("Сэр, у меня сейчас есть дела...// Давайте продолжим позже....")
            call daphne_goout
        pass
        $daphne("..............//~46 00 1 neu// Сэр, простите меня за то что было....// Просто я...//~73 01 1 ang// .....Я не могу профессор.")
        $hero(m, "Ничего Дафна....// Я не сержусь....// Просто мне показалось, что вы готовы к этому....")
        $daphne("~37 n0 1 pou// ....Я тоже так думала, сэр....//~46 w0 1 dis// Но... я не могу находиться в нижнем белье, когда на меня пялиться куча народу.")
        $hero("Ну во первых мисс Гринграсс, сдесь кроме меня никого нет.")
        $hero("А во вторых - что плохого в том, что вы в нижнем белье?// Вас же не просят полностью раздеваться....")
        $daphne("~26 00 3 dis// Профессор?!....")
        $hero("Не предирайтесь к словам....// Это в качестве примера...")
        $daphne("~37 00 2 neu// Эм........// Ну... я даже не знаю....// ................")
        $hero("....Вы же хотели сделать сюрприз родителям.... мисс Гринграсс?!")
        $daphne("~73 n0 1 pri// .................// .....Ну хорошо профессор.//~46 00 1 neu// Вы правы.... сдесь нет ничего постыдного.")
        $hero(g9, "#(Хе-хе, никто и не сомнивался)")
        $daphne("~73 01 2 ehh// ....Сэр?!")
        $hero(m, "Эм... Я говрю, что рад тому, что вы разобрались в себе.// Ну мисс... если вы готовы...")
        $daphne("~73 01 2 pur// Да, да...// ......Я готова.")
        $hero("Хорошо.....// ....Так что бы вы хотели снять?")
        $daphne("~37 02 3 dis// Эм... «Хотела бы...»//~73 00 2 pri// ......Незнаю, профессор...")
        $hero(".......................// Скажем так - мисс Гринграсс...// Что вы бы не постеснялись снять?")
        $daphne(".....Не постеснялась бы, сэр?//~73 c0 1 pri// #..........................//~37 00 2 ope// Думаю я могла бы снять блузку....//~37 00 2 neu// Дайте мне минуту...")
        "> Вы замечаете, что Дафна немного не уверенна в себе, но она все-таки снимает блузку."

        $screens.Show(Dissolve(1), "blkfade") #Черный экран
        $daphne.ItemsCustomize(delete={"combi"}, update={"bra"}) #delete - снять (одетую) вешь. update - одеть вещь.
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") 
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("Хорошо мисс Гринграсс....// Чувствуете себя не ловко?")
        $daphne(".... Нет, сэр.//~73 01 3 ang// #(На самом деле мне немного не по себе)")
        $hero("Я же говорил...// Здесь нет ничего постыдного...")
        $daphne("~55 00 1 neu// ............// ....Думаю я смогу больше, сэр...")
        $hero(g9, "#(Разумеется....)")
        $daphne("~37 s0 2 ope// Э-э..... Сэр....")
        $hero(m, "Я вас понял Дафна....// Мне отвернуться?")
        $daphne("~37 01 1 neu// Я хотела сказать....// Эм....// ....Мне же все ровно нужно будет стоять на сцене.... перед этими.....// ................")
        $hero("....Вы имеете ввиду, когда на вас будут смотреть, мисс Гринграсс?")
        $daphne("~73 01 3 ang// .....Да, профессор.")
        $hero("#(А Снейп был прав....)")
        $hero(g9, "#(Мне стоило с ней повозиться...)")
        $hero(m, "Да, вы правы Дафна....// Ну хорошо....// Я смотрю....// Можете приступать....")
        $daphne("~37 00 2 neu")
        "> Ваши слова пошли на пользу Дафне...."
        "> Она хоть и смущенно, но снимает с себя юбку."

        $screens.Show(Dissolve(1), "blkfade") #Черный экран
        $daphne.ItemsCustomize(delete={"skirt"}) #delete - снять (одетую) вешь. update - одеть вещь.
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") 
        $screens.Show("ctc").Pause().Hide("ctc")

        $daphne("~73 01 2 smi// Вот.... сэр....")
        menu:
            "\"Ваше белье бесподобно мисс Гринграсс\"":
                $daphne("~55 00 1 neu// Спасибо, сэр...")
                $hero("Хм....// «Спасибо... сэр...»// Что-то это мне напоминает....// Ах да....")
                stop music
                $screens.Show(Dissolve(1), "blkfade") #По хорошему здесь должен быть whitefade, но игру выкидывает, когда я его ставлю. Хз почему.
                pause 1.5
                "Мне нравятся ваши трусики Гермиона..."
                "Спасибо, профессор..."
                $hero("..................")
                $hero("#(Хм....)")
                $hero(g9, "#(Интересно... что сейчас делает Гермиона)")
                $daphne("~55 02 2 ehh// #.....Сэр?!")
                $hero(m, "......?!")
                $screens.Hide(Dissolve(1), "blkfade")
                $daphne("~37 00 2 neu// ...Сэр, вы меня слышите?// ....Я что-то сделала не так?!")
                $hero("Оу... Я извеняюсь...// Кажется я немного призадумался....")
                play music "music/Bittersweet Symphony (Instrumental).mp3"
                $hero("#(Ах да, белье....)")
            "\"Ну, а теперь снимайте остальное мисс Гринграсс\"":
                $daphne("~77 w0 2 wo// {size=+7}ЧТО!?{/size}// Ну, знаете....// Это переходит все границы...")
                $daphne("~55 01 2 dis//")

                $screens.Show(Dissolve(1), "blkfade")
                $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"})
                $daphne.ItemsCustomize(update={"skirt:cheer_long"})
                pause.5
                $screens.Hide(Dissolve(1), "blkfade") 
                $screens.Show("ctc").Pause().Hide("ctc")

                $wtevent.Finalize("daphne_goout")
                $hero(g4, "Кажется я перегнул....")
                $daphne.liking -= 20
                $wtevent.Finalize ("night_start")

        $hero(m, "Отлично мисс Гринграсс...// Видите... все это может только казаться сложным.")
        $daphne("....Да?!//~73 01 1 smi// .....Наверное вы правы, профессор.")
        $hero(m, "#(Хм....)// #(Сиськи и в прямь маловаты....)")
        $hero(g9, "#(....Что-бы с ними сделать?!)")
        a6 "Ты задолбал..."
        a7 "Мне напомнить из-за чего ты тут застрял?"
        $hero(m, "#(.....Точно)// #(Похоже что ты прав....)// #(И так сойдет....)")
        a6 "Если бы не твоя самодеятельность, ничего этого небыло бы."
        $daphne("~55 s0 1 pou// Эм....// ....Профессор, вы меня слышите?")
        $hero("Гхм..... Простите... я не на долго задумался.// ....Вы что-то сказали?")
        $daphne("~73 02 3 ang// Я говорю, мне долго еще так стоять?")

        menu:
            "- Отпустить её -":
                $hero("Можете одеваться мисс Гринграсс....")
                $daphne("~73 01 1 smi// Хорошо, сэр...")

                $screens.Show(Dissolve(1), "blkfade")
                $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"})
                $daphne.ItemsCustomize(update={"skirt:cheer_long"})
                pause.5
                $screens.Hide(Dissolve(1), "blkfade") 
                $screens.Show("ctc").Pause().Hide("ctc")

                $daphne.liking += 3
                $hero("Не спешите мисс Гринграсс...// Вы сегодня хорошо постарались, и заслуживаете поощрение....")
            "- Она может больше -": #Немного разглядываем, Дафна стесняется, и мы её отпускаем(нужны чибики в нижнем белье). Они есть?
                $hero("Подойдите ко мне Дафна....// Я хочу на вас посмотреть по ближе...")
                $daphne("~37 00 2 neu// Эм... Ну если так нужно, сэр...")
                pause 1.0
                felix "К большому сожалению, данная сюжетная линия пока дописана только до этого момента..."
                felix "{size=-3}(Но, вам остаются доступны другие сюжетные линии){/size}"
                felix "Оставьте ваши вопросы, благодарности и пожелания на нашем {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}ФОРУМЕ{/a}."
                felix "Так вы простимулируете нас, и продолжение появится быстрее. :)"
            
                $screens.Show(Dissolve(1), "blkfade")
                $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"})
                $daphne.ItemsCustomize(update={"skirt:cheer_long"})
                pause.5
                $screens.Hide(Dissolve(1), "blkfade") 
                $screens.Show("ctc").Pause().Hide("ctc")
            
                $hero("Не спешите мисс Гринграсс...// Вы сегодня хорошо постарались, и заслуживаете поощрение....")
        $daphne.whoring += 2
    elif IsRunNumber(6):
        pause 1.0
        felix "К большому сожалению, данная сюжетная линия пока дописана только до этого момента..."
        felix "{size=-3}(Но, вам остаются доступны другие сюжетные линии){/size}"
        felix "Оставьте ваши вопросы, благодарности и пожелания на нашем {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}ФОРУМЕ{/a}."
        felix "Так вы простимулируете нас, и продолжение появится быстрее. :)"
        call daphne_main_menu_requests

    return