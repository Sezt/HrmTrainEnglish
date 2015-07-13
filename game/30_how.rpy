label howtoplay:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/silly_fun_loop.mp3" fadein 1 fadeout 1 # LOLA'S THEME.
    if not persistent.tut: #Turns TRUE after tutorial happened once already. EVENT_01
        
        
        
        
        $ lola_face = "03_hp/22_lola/01.png"
        $ lola_body = "03_hp/22_lola/body_01.png"
        
        $ l_things = True
        #$ l_blush = True
        $ lx = 490
        $ ly = 190
        show screen l_head
        l "Hello, pervs of the internet!"
        hide screen l_head
        a5 "Watch it, brat!"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/02.png"
        show screen l_head
        l "Huh...?"
        hide screen l_head
        a6 "What did I tell you about using the \"p\" word?"
        $ l_question = True
        $ lola_face = "03_hp/22_lola/03.png"
        show screen l_head
        l "Em... Use it as often as possible?"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}Wrong!{/size}"
        $ l_question = False
        $ l_drop = True
        $ lola_face = "03_hp/22_lola/04.png"
        show screen l_head
        l "ght!"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}We don't use it! Ever!{/size}"
        $ lola_face = "03_hp/22_lola/01.png"
        $ l_drop = False
        show screen l_head
        l "Because daddy is the biggest perv there is?"
        hide screen l_head
        a6 "Ght!"
        a6 "Did you enjoy starring in \"Princess Trainer\"?"
        $ l_hearts = True
        $ lola_face = "03_hp/22_lola/01.png"
        show screen l_head
        l "It was the best!"
        hide screen l_head
        a1 "Want to be in the \"gold edition\" as well?"
        $ l_hearts = False
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "!!!"
        $ lola_face = "03_hp/22_lola/06.png"
        show screen l_head
        l "Ladies and gentlemen, welcome to the \"Hermione Trainer\" tutorial."
        hide screen l_head
        a1 "Attagirl."
        $ l_drop = True
    else: # EVENT_02
        $ lx = 490
        $ ly = 190
        $ lola_body = "03_hp/22_lola/body_01.png"
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "Hm...?"
        l "You want to hear the tutorial again?"
        $ lola_face = "03_hp/22_lola/09.png"
        l "Hm...."
        $ lola_face = "03_hp/22_lola/11.png"
        l "You are not very bright, are you?"
        $ lola_face = "03_hp/22_lola/10.png"
        l "Hm..."
        $ l_things = True
        $ lola_face = "03_hp/22_lola/08.png"
        l "*Giggle!*"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/01.png"
        l "You want me to give you the tutorial topless?"
        hide screen l_head
        $ d_flag_01 = False
        menu:
            "\"You bet!\"":
                $ lola_face = "03_hp/22_lola/01.png"
                show screen l_head
                
                $ d_flag_01 = True
                l "Alrighty!"
                hide screen l_head
                pause.1
                show screen blkfade 
                with d3
                $ lola_body = "03_hp/22_lola/body_02.png"
                $ l_blush = True
                pause.5
                hide screen blkfade
                with d7
                
                
            "\"Not interested.\"":
                $ lola_face = "03_hp/22_lola/12.png"
                show screen l_head
                l "You're boring..."
                $ lola_face = "03_hp/22_lola/09.png"
                l "Well, whatever..."

                   
    ### THE TUTORIAL ###
    play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
    $ lola_face = "03_hp/22_lola/06.png"
    show screen l_head
    l "Here is a short list of things to keep in mind..."
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_02.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')   

    l "Hermione will only be willing to sell sexual favors in exchange for house points when house of gryffindor is falling behind."
    
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_01.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')   
    l "Making friends with professor Snape will make him trust you more, and will increase the rate at which slytherin house gets the points."
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_03.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    if d_flag_01: # TOPLESS.
        $ lola_face = "03_hp/22_lola/07.png"
    l "Reading educational books makes earning money easier, but is not mandatory."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_04.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    l "Buying the same sexual favor again could lead to a different outcome depending on how far along Hermione is in her training."
    $ lola_face = "03_hp/22_lola/06.png"

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_07.png" #<---- SCREEN
    l "All favors are organized into two groups: \"personal favors\" and \"public favors\"."
    l "Personal favors take place in the office and don't affect Hermione's reputation much."
    l "Public favors take place off-screen, during classes."
    l "Every public favor, except for the last one, has nine different outcomes."
    l "Also, buying personal favors is essential for Hermione's training, but public favors are optional."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_05.png" #<---- SCREEN

    $ renpy.play('sounds/boing02.mp3') 
    l "Treating Hermione poorly will worsen her mood and could make her very uncooperative..."
    l "She will cool off with time, but you can speed up the process by buying her something nice..."
    
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_06.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    l "And there is no timelimit. So feel free to take as many days to comlete the game as you want."
 
    
    
    
    $ end_u_1_pic =  "03_hp/22_lola/tut_00.png" #<---- SCREEN
    $ l_drop = False
    
    if not persistent.tut: # FIRST TIME TUTORIAL. Turns TRUE after tutorial happened once already. EVENT_01
        $ persistent.tut = True #Turns TRUE after tutorial happened once already.
        hide screen l_head
        a1 "Alright, that's enough..."
        $ l_question = True
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "How did I do?"
        hide screen l_head
        a1 "You did well. Good girl."
        $ l_question = False
        $ l_things = True
        $ lola_face = "03_hp/22_lola/08.png"
        show screen l_head
        l "Me-he-he. Lola is a good girl!"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/01.png"
        show screen l_head
        l "What do I get?"
        hide screen l_head
        a1 "What you want?"
        $ lola_face = "03_hp/22_lola/10.png"
        show screen l_head
        l "Hm..."
        $ l_exclamation = True
        $ lola_face = "03_hp/22_lola/01.png"
        l "Can we have a rape scene with me in the \"Gold Edition\"?"
        hide screen l_head
        a6 "Don't test my patience, girl."
        $ l_exclamation = False
        $ l_drop = True
        $ lola_face = "03_hp/22_lola/04.png"
        show screen l_head
        l "Sorry, daddy."
        $ l_drop = False
        hide screen l_head
        a5 "............"

    else: ### NOT FIRST TUTORIAL. EVENT_02
        if d_flag_01: #TOPLESS.
            hide screen l_head
            stop music fadeout 1.0
            a1 "What is going on here?"
            $ lola_face = "03_hp/22_lola/14.png"
            $ l_drop = True
            show screen l_head
            l "Yikes!"
            hide screen l_head
            a1 "What did I tell you about exposing yourself to complete strangers?"
            $ lola_face = "03_hp/22_lola/04.png"
            show screen l_head
            l "It's an important part of growing up?"
            hide screen l_head
            a6 "Wrong!"
            $ l_drop = False
            $ l_tears = True
            $ lola_body = "03_hp/22_lola/body_01.png"
            $ lola_face = "03_hp/22_lola/04.png"
            show screen l_head
            l "Daddy, I'm so sorry!"
            l "That mean random Internet person forced me, I swear!"
            hide screen l_head
            a1 "This tutorial is over."
            $ l_blush = False
            $ l_tears = False
            $ lola_face = "03_hp/22_lola/15.png"
            show screen l_head
            l "He-he! You got busted!"
        else:
            $ lola_face = "03_hp/22_lola/09.png"
            l "And that's that..."
            $ lola_face = "03_hp/22_lola/13.png"
            l "Did you get it this time?"
            
return

### ABOUT GAME ####
label abouttrainer:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1 
    
    a1 "Hm... Let's see..."
    a1 "I started to work on \"Hermione Trainer\" right after the release of \"Princess Trainer\"."
    a1 "In my mind I had an idea for a cute little game the development of which should not have taken me longer the a couple of month."
    a1 "As we all know now it actually took me longer then half a year..." 
    a1 "And that it despite countless compromises I had to make simply to prevent the damn thing taking even longer to develop."
    a1 "Working on this game was quite fun at times..."
    a1 "But it was also challenging..."
    a1 "Sometimes I had to wrestle with some ideas and gameplay mechanics that didn't want to work properly..."
    a1 "Also working on this game taught me a lot about my abilities as a game developer and of my limitations."
    a2 "I almost feel like I should be getting an achievement diploma or something."
    a1 "Well, I am off to my next project now. {size=-4}(\"Princess Trainer Gold Edition\"){/size}"
    a1 "Thank you for supporting me, guys. And I hope this game will brighten up your day a bit."
    a2 "Until next time..."

    return

### F.A.Q. ###
label faq:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1 
    with flashbb#<---- SCREEN
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 
    
    a1 "Hello. My name is Akabur. I am the creator of this game and I'm here to answer your questions." 
label faq2:    
    menu:
        "How can I show my support?":
            a1 "Well, there are few ways to do that..."  
            a1 "The easiest way would be to contact me (akaburfake2@yahoo.com) and let me know that you enjoyed the game."
            a1 "You could also support me personally at {a=http://www.patreon.com/akabur}www.patreon.com/akabur{/a}"
            a1 "Another way to support me though would be to follow this link: {a=http://akabur.hentaiunited.com}akabur.hentaiunited.com{/a}."
            a1 "For an independent artist like myself every buck counts..."
            a6 "I'm serious. Because of the way I make living the damn bank won't even issue me a creditcard still..."
#            label payments:
#            menu:
#                "-WebMoney info-":
#                    a1 "My RUBLES WebMoney purse: R133931000745"
#                    a1 "My USD WebMoney purse: Z319925489258"
#                    a1 "My EURO WebMoney purse: E800599783938"
#                    jump payments
#                "-YandexMoney Info-":
#                    a1 "My Yandex Purse Number: 41001849167270"
#                    jump payments
#                "-PayPal Info-":
#                    a1 "Contact me via email and i will give you my PayPal."
#                    jump payments
#                "-Credit Card-":
#                    a1 "Here: {a=http://www.test.akabur.com/donate}how to donate with Credit Card.{/a}"
#                    jump payments
#                "-Cancel-":
#                    jump faq2
            jump faq2
            
        "How to stay tuned?":
            a1 "Well, follow this link: {a=http://akabur.hentaiunited.com}akabur.hentaiunited.com{/a} and subscribe. Or visit my site: {a=http://akabur.com}akabur.com{/a}."
            a1 "There is also Patreon of course {a=http://www.patreon.com/akabur}www.patreon.com/akabur{/a}.\nAnd {a=https://twitter.com/AKABUR}my twitter{/a}." 
            jump faq2
        "I have another question.":
            a1 "If you have a question that is not covered in this \"F.A.Q.\", feel free to email it to me: akaburfake2@yahoo.com"
            a1 "Or leave your question here: {a=http://ask.fm/AKABUR}ask.fm/AKABUR{/a}"
            jump faq2
        "I want to report a bug/error.":
            a1 "This game has been tested many many many times, but the best testers are always the players."
            a1 "So if you did encounter a bug, typo or even a grammatical error - feel free to contact me (akaburfake2@yahoo.com) and I will fix the problem in the next version of the game."
            jump faq2
        "Who helped you create this game?":
            a1 "Nobody helped me! I did everything myself!"
            a1 "I wrote all the scripts, created all the art, and composed all the music!"
            a7 "Me! {size=+3}Me! I created everything! Me!{/size}"
            a2 "Heh..."
            a1 "Well, in truth I did most of the work. But I had a lot of help also."
            a1 "My friend and colleague Dahr provided me graciously (and free of charge) with a lot sorts of additional art (among other things)."
            a1 "Feel free to throw a coin or two the man's way at {a=http://www.patreon.com/DAHR}www.patreon.com/DAHR{/a}"
            a1 "Xaljio was always there for me whenever I needed help with coding. (quite often). Fell free to visit his page at {a=http://www.patreon.com/xaljio}www.patreon.com/xaljio{/a}"
            a1 "And of course patreon and hentaiunited community. You guys are awesome."
            a1 "Thank you for being so supportive and for financing the development of this game. You guys made this world a bit better place."
            jump faq2
        "Будет ли продолжение этой игры?":
            a1 "Как я уже говорил, я не стою на месте."
            a1 "И уже начал разработку нового проекта. {size=-4}(\"Тренер Принцессы Золотое Издание\"){/size}"
            a1 "..."
            a1 "..."
            a1 "Но если тебе понравилась конкретно эта часть, ты можешь найти группу программистов-энтузиастов занимающихся модифицированием..."
            a1 "А возможно и продолжением клиента."
            a6 "И хоть я и против этого..."
            a2 "Но от них не избавиться."
        "Можно взломать и перевести эту игру?":
            a1 "..."
            a1 "..."
            a5 "Нет."
            define nyor = Character('Nyarkohotep', color="#9F42AB")
            nyor "Странный вопрос, не находишь?"
            nyor "И это после того, как я полтора гребанных часа возился, чтобы перевести никому не нужные FAQ и обучалки!"
            nyor "Агрх!"
            nyor "А вообще, молодец, что заглянул."
            nyor "Минута славы."
            nyor "Перевод для вас пилили \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=14141420}Ave_Fletch{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=15155170}Discordnk90{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=8041771}maniac4a{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=4472572}Rio-Violente{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=16957111}MrFrost1991{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=18304384}babaylolxz{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=15179745}Khan32{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=11908608}sn0rk95{/a}, \
            и любимец публики {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=16733487}Nyarkohotep{/a}."
            nyor "Извините, если кого-то забыли :3!"
            nyor "Не забывайте пользоваться салфетками, ребята, пока-пока!"
            a1 "..."
            a5 "А спросить моего разрешения на перевод, не нужно?"
            felix "Ты вроде как ушел..."
            a1 "..."
            a6 "Это ничего не меняет..."
            felix "Да конечно..."
            jump faq2

        "Неважно. Выпусти меня отсюда!":
            return

    
    return


########################
# From developers

label devel:

    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1
    
    dr "Итак, вы уже обратили внимание, что это не оригинальная игра Акабура..."
    menu :
        "Что ???" :
            dr "(facepalm)"
            dr "Я так и знал, что нужно давать больше информации общественности..."
        
        "Это же шутка ?" :
            dr "..........."  
        
        "А разве ты не Акабур ?" :
            dr "В рот мне ноги..."
            
    dr "{size=+3}Т.е. вы все по-прежнему считаете, что игру для вас продолжает улучшать Акабур ?{/size}"
    dr "И это после того, как он сообщил, что считает ее законченной ?"
    dr "После того, как он решил никогда ее не переводить на русский ?"
    dr "После того, как я написал всю эту гору кода, не говоря уж об остальной команде разработчиков, переводчиков и художников, месяцами бесплатно трудящихся для вас ?"
    dr "{size=+4}Аргх...{/size}"
    dr "......."
    dr "Простите, наболело."
    
    dr "Итак, для вас трудились :"
    dr "Главный координатор (встречайте стоя !): {color=4F4F4F}Хан ( Khan ){/color}"
    dr "Главный разработчик : {color=00FF00}Дрон (dron12355){/color}"
    dr "Разработка и ивенты Дафны : {color=7789CA}Феликс{/color}"
    dr "Поддержка игры (на плаву) : {color=0000FF}Сказочник{/color}"
    dr "Перевод на английский язык : {color=0089BE}Хан и Sezt{/color}"
    dr "Разработка и обучающие ивенты : {color=FF0000}Nyarkohopter{/color}"
    dr "Чибики Дафны : {color=2F2F2F}Grending{/color}"
    dr "Дафна : {color=6F6F6F}Zio Dyne{/color}"    
    
    dr "Список особых благодарностей :"
    dr "{color=0F0F0F}Евгений aka Afar{/color} - за великолепный кодинг и неоценимый вклад в развитие проекта !"
    
    $ hx = 370
    $ hy = 0
    $ h_red_angry = True
    $ h_angry = False
    $ h_smile = False
    
    dr "И несравненная Гермиона Грейнджер в роли офисной шл..."
    show screen l_hermiona
    her "Что-о-о-о ???"
    hide screen l_hermiona

    dr "Прости, в роли секретут..."
    $ h_red_angry = False
    $ h_angry = True
    $ h_smile = False
    show screen l_hermiona
    her "А на тебя давно в последний раз подавали в суд\n за половую дискриминацию ?"
    hide screen l_hermiona
    dr "Бхм. И наша главная офис-леди - мисс Грейнджер."
    $ h_red_angry = False
    $ h_angry = False
    $ h_smile = True
    show screen l_hermiona    
    her "Так то лучше !"
    her "Всем до встречи в игре."
    hide screen l_hermiona 
    dr "Недотрога..."
    dr "Ушла наконец."
    
    dr "Итак, приятной игры, друзья !"
    
    dr "А если хотите пообщаться с людьми, которые продолжают совершенствование и расширение игры, милости просим."
    dr "{a=http://wtrus.ixbb.ru}НАШ ФОРУМ ТУТ{/a}"


return

label forum:

    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    
    dr "Итак, перед вами модификация игры, которая развивается независимой (от Акабура) командой разработчиков. Добро пожаловать на {a=http://wtrus.ixbb.ru}НАШ ФОРУМ{/a}."

return
