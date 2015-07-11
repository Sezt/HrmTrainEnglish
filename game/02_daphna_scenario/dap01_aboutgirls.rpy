################################
########### LEVEL 01 ############
################################
##### REQUEST_01  About Girls #####
################################
label dap_request_01: #LV.1 (Whoring = 0 - 4)

    $music("Daphne Theme")

if IsRunNumber(1):
#    if daphne.whoring<3:
        $hero("Alright, miss, tell me a bit about the girls around you. We need to understand who you are dealing with.")
        $daphne("~55 00 1 neu// Well, in General most of them are pretty uninteresting.// Why would I pay attention to all these upstarts?!")
        $hero("But, miss, if we are trying to elevate you to your proper position, you need to beat all of them.// Knowledge is power. If you know what I mean?")
        $daphne("~46 01 pou 1// I understand... I think.")
        $hero("So I will give you this task: You must keep an eye on the other students.// Pay attention to who is popular and why.")
        $daphne("~37 00 1 ope// Yes, sir. \"Knowledge\"! I get it now...")
        $hero("Find their weaknesses, their disadvantages and, if we are lucky, even some skeletons in their closet...")
        $daphne("~26 00 1 ope// Uh...you want me to spy on them, sir?// ~26 00 1 neu// That would be unworthy of a sorceress directly descended from Merlin!")
        $hero("Strange, I thought you where a Slytherin student?// Is that not your house, dear? You seem more like a straitlaced member of Gryffindor?")
        $daphne("~55 00 1 pri// Hmm...but I...")
        $hero("I'm not suggesting you \"spy\", as you put it.// Just study your classmates. Let me remind you, many of them will be performing at the competition.//" 
            "Let's learn about how they could win and how to make them lose.//"
            "You need to care not only about how beautifully you present yourself on stage, miss, but also your popularity in school.//"
            "The higher it is, the more likely the students will vote for you, and their votes count a lot.")
        $daphne("~46 00 1 dis// Professor. I can't believe my ears!// You want me to grovel before commoners to improve my chances?!")
        $hero("I propose that you try to be are a bit more flexible, miss.// Now concentrate on your simple task and learn about your competitors.")
        $daphne("~46 00 1 pou// Hmm... I'll try, Professor.")
        $hero("Excellent. Report back tonight.")
elif IsRunNumberOrMore(2):
    if IsRunNumber(5) or IsRunNumber(6) or IsRunNumber(7):
        pause 1.0
        felix "К большому сожалению, данная сюжетная линия пока дописана только до этого момента..."
        felix "{size=-3}(Но, вам остаются доступны другие сюжетные линии){/size}"
        felix "Оставьте ваши вопросы, благодарности и пожелания на нашем {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}ФОРУМЕ{/a}."
        felix "Так вы простимулируете нас, и продолжение появится быстрее. :)"
        call daphne_main_menu_requests
    else:
        $hero("Так, мисс Гринграсс. Давайте-ка вы сегодня снова займетесь изучением ваших конкуренток.")
        $daphne("~64 00 1 neu// Опять, сэр?")
        $hero("Ну, если вы уже все о них знаете...")
        $daphne("~55 00 1 neu// Пока не все, сэр.")
        $hero("Тогда вперед, жду вас вечером с отчетом.")
return



label dap_request_01_complete:
    $daphne.Visibility()
    $daphne.chibi.State("door", speed="go").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")

    $daphne.State(pos="door").Visibility("body+")("~55 00 1 smi// Добрый вечер, профессор Дамблдор.") 


    $music("Daphne Theme")

    if IsRunNumber(1):
        $hero("Итак, мисс Гринграсс, каковы успехи?")
        $daphne("~55 00 1 neu// Ну, я наблюдала за Джесси. Похоже, она не слишком прилежно учится.")
        $hero("И?")
        $daphne("~55 00 1 pur// Это пока все, сэр.")
        $hero("И как это поможет вам завоевать положение и подняться выше Джесси, мисс? Хотите сказать, что ее плохая учеба влияет на ее популярность?")
        $daphne("~55 00 1 pou// В общем-то, нет. Я потому и выбрала ее, что она довольно популярна.//"
            "~55 01 1 pou// К тому же она хвалилась, что может окрутить любого парня, вот я и решила...//"
            "~37 00 1 pou// Профессор, только не подумайте, что мне надо кого-то там окручивать!//"
            "Я выше этого! Просто вы дали задание и мне показалось, что она подойдет.")
        $hero("Я уже слышал, что вы выше этого, мисс.// Но получается, что задание вы сегодня не выполнили.")
        $daphne("~73 00 1 pou// Похоже, что так.")
        $hero("И тем не менее, я готов вас простимулировать, потому что верю в вас.// В конце концов вы волшебница древнего рода.// Уверен, в следующий раз у вас получится лучше.")
        $daphne("~73 00 1 smo// Спасибо, сэр, я буду очень стараться!")
        $daphne.whoring += 1
        $wtevent.Finalize("daphne_pre_menu")
    elif IsRunNumber(2):
        $daphne("~55 00 1 neu// Сегодня, профессор Дамблдор, я решила подойти к вопросу системно.")
        $hero("Вот как?")
        $daphne("~46 00 1 neu// Да, сэр. Мне кажется, я начинаю понимать, почему одни девчонки популярнее других.")
        $hero("#(Тоже мне бином Ньютона.)// Слушаю вас, мисс.")
        $daphne("Мне надо еще кое-что проверить, сэр, в следующий раз я смогу рассказать вам.//" 
            "~46 00 1 pou// А сегодня я присматривалась к Мелиссе, она заигрывала с парнями.")
        $hero("И как вам это?")
        $daphne("~37 00 1 pur// Отвратительно, сэр. Как она может это делать – среди них были не только полукровки, но и мугродье!")
        $hero("Не может быть!")
        $daphne("Да, сэр, представьте себе.")
        $hero("И что же?")
        $daphne("~37 00 1 pri// Парни вились вокруг нее, сэр!//"
            "~37 00 1 dis// И знаете, мне показалось, что некоторые были не прочь зайти с ней дальше заигрываний.")
        $hero("Вот это неожиданность!")
        $daphne("~37 00 1 pri// Я тоже была шокирована, сэр!// Я никогда не обращала на это внимания, никогда об этом не задумывалась.//"
            "~37 n0 1 pou// Я была уверена, что чистая кровь откроет любые двери и всякие заигрывания никому не нужны.//"
            "~37 n2 1 pou// Но почему-то сегодня вокруг меня не было ни одного парня, а к этой девице они летели, как мухи на...")
        $hero("На мед?")
        $daphne("~37 00 1 pou// Я хотела употребить более сильное слово, сэр. Но пусть будет «мед»...")
        $hero("И что же теперь, мисс?")
        $daphne("~37 00 1 neu// Мне нужно время, чтобы во всем этом разобраться, сэр.")
        $hero("Хорошо, мисс Гринграсс, похоже, вы движетесь в верном направлении. Думаю, стоит вас наградить.")
        $daphne.whoring += 1
        $wtevent.Finalize("daphne_pre_menu")
    elif IsRunNumber(3):
        $daphne("I think I understand, sir.")
        $hero("Huh?")
        $daphne("~55 00 1 ope// Popularity is based on your grades, your popularity with boys, and of course, purity of blood.")
        $hero("#(Oh, great Sands! Enough with the platitudes, finally her beautiful mouth says something useful!)// I, um... I see you have done some serious digging, miss, I was not mistaken in you.")
        $daphne("~73 00 1 smi// Thank you, sir.")
        $hero("Well, your purity of blood should be pretty safe.")
        $daphne("~55 00 1 ope// Yes it is sir! The purest blood of anyone at Hogwarts.// ~55 c0 1 ope// The Greengrass family descends from Salazar Slee...")
        $hero("#(She's back!) Wait a minute, miss. Miss! What about your grades?")
        $daphne("~55 00 1 pur// I don't think pureblood witches should depend on assessments made by some teachers with questionable pedigree.//"
            "~37 00 1 dis// Let mudbloods, like that Granger whore, suck up to the teachers.//"
            "I know that I am the better then her.")
        $hero("Hmm. That removes one path to popularity.// I don't think your blood-status is enough, miss.")
        $daphne("~55 00 1 pou// I thought that too, sir.")
        $hero("So your only remaining options is men?")
        $daphne("~73 01 1 ang// What?...men, sir?")
        $hero("According to your theory, that I deeply respect...")
        $daphne("~73 01 1 smo//...")
        $hero("...there are three ways of obtaining popularity.//"
            "What we have learned so far: you blood-status is a positive, your grades are a negative.//"
            "Finally we are left with men - they can tip the scales for or against you.")
        $daphne("~55 00 1 pou// Uh...// But, sir, I am not going to jump out of my panties to gain the favor of some guys.")
        $hero("#(Jump out of her panties, hehe, lovely metaphor. Think that will happen sooner then you think, dear).//"
            "Well, miss. Then at the competition, these guys will vote for their impure girlfriends,...// and the girl who deserves to win will fail miserably.")
        $daphne("~37 00 1 pou// Sir, I can't!")
        $hero("I really hope that you will reconsider your stance, miss Greengrass.")
        $daphne("~26 00 1 ope// Professor Dumbledore! Don't forget that Salazar Slytherin was my ancestor!")
        $hero("The one who founded the house you belong to, right?")
        $daphne("Yes, sir, and you should know that!")
        $hero("Please remind me, what are the qualities of Slytherin")
        $daphne("~55 neu 01 1// Cunning, ambition, resourcefulness, sir.")
        $hero("Have you demonstrated these qualities to achieve victory in the competition (especially regarding men)?")
        $daphne("~55 01 1 pou// .........................")
        $hero("Идите, девушка, и подумайте, достойны ли вы своего великого предка!//" 
            "Впрочем, поскольку вы усердно работали, думаю, будет неправильно оставить вас совсем без подарка.")
        $daphne.whoring += 1
        $wtevent.Finalize("daphne_pre_menu")
    elif IsRunNumber(4):
        $daphne("Эм....// Сэр...")
        $hero("Да мисс Гринграсс....// вы готовы мне что-то рассказать?")
        $daphne("..........//~55 00 1 ope// Вы оказались правы, профессор.//~37 n0 1 pou// Парням совсем наплевать на то, какая у меня кровь....//~37 00 2 dis//  ...Почему профессор?!//~37 02 2 dis//  ...Почему мой флирт, им важнее?!")
        $hero("Хм.....// Я так понял, вы пытались заигрывать с парнями мисс Гринграсс?")
        $daphne("~73 01 1 ang// Э-э... Я не хотела...// Просто....// Ну.... мне нужно было еще раз все проверить.")
        $hero("Мисс Гринграсс...// А вы бы не могли по конкретнее мне рассказать, с кем из парней вы флиртовали?")
        $daphne("~37 00 2 dis// Эм....// Нет профессор...// Я не стану делиться этим с вами, сэр...")
        $hero("...Почему же?")
        $daphne("~73 02 3 ang// Это очень низко...//  #(До сих пор не могу поверить что я решилась на это)")
        $hero("Низко?// Вы уже научились решаться на то, о чем раньше не могли даже думать.// По моему это достойно похвалы....// Как считаете?")
        $daphne("~55 00 1 ope// Эм... Я не знаю, сэр.//~46 00 1 neu//  Мне все еще не по себе от этого.")
        $hero(g9, "#(Ты у меня и не такое будешь вытворять, когда я закончу с тобой)")
        $daphne("~46 00 1 neu// Что вы сказали, сэр?")
        $hero(m, "Эм.... Я подумал, что на сегодня с вас достаточно того, что вы сделали.")
        $daphne("~37 00 1 dis// #(Черт... Лучше не напоминайте мне об этом)")
        $hero("На сегодня вы можете быть свободны, мисс Гринграсс.")
        $daphne("~46 00 1 neu// ...Хорошо, профессор.")
        $hero("И да... мисс Гринграсс, я думаю вы заслужили поощрение сегодня.")
        $daphne.whoring += 1
        $wtevent.Finalize("daphne_pre_menu")

    return