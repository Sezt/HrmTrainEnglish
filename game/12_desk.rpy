label menu_reading_book:

    $ choose = RunMenu()
    python:
        for e in this.List:
            if e.GetValue("block")==_block and e._status>=0: # Нужно ставить GetValue("block")  а не _block - у ивента такого объекта может не быть
                choose.AddItem("- Book: "+e._caption+" - "+("{image=check_08.png}" if e.IsDone() else ""), 
                    "reading_book_done" if e.IsDone() else "menu_reading_book_2", e.Name)

    $ choose.Show("books_list")

    label menu_reading_book_2:
        $ the_gift = wtevent._img#"03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3

        "\"[wtevent._caption]\"" "[wtevent._description]"#" Вы хотите прочитать ее?"
        menu:
            "- Read book-":
# Проверяем, что освоены предыдущие ступени навыка:
### DR'S NEWSPAPER ooo ###
                if wtevent.GetValue("block")=="books_newsp":
                    if wtevent.Name=="nsp_newsp_book_p02a" and nsp_genie_writer < 1:
                        m "This book is too difficult for me."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p02b" and nsp_genie_writer < 2:
                        m "This book is too difficult for me."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p03a" and nsp_genie_writer < 3:
                        m "This book is too difficult for me."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p03b" and nsp_genie_writer < 4:
                        m "This book is too difficult for me."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p04" and nsp_genie_writer < 5:
                        m "This book is too difficult for me."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p05a" and nsp_genie_writer < 6:
                        m "This book is too difficult for me."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p05b" and nsp_genie_writer < 7:
                        m "This book is too difficult for me."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p06a" and nsp_genie_writer < 8:
                        m "This book is too difficult for me."
                        hide screen gift
                        jump books_list
                    if wtevent.Name=="nsp_newsp_book_p06b" and nsp_genie_writer < 9:
                        m "This book is too difficult for me."
                        hide screen gift
                        jump books_list
                    
                if wtevent.GetValue("block")=="books_newsp2":
                    if wtevent.Name == "nsp_newsp_book_typo1" and (nsp_genie_typographic < 0 or nsp_genie_typographic_exp < 2):
                        m "Lacking experience. It is necessary to publish at least two typographical sets of the previous level."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_typo2" and (nsp_genie_typographic < 1 or nsp_genie_typographic_exp < 2):
                        m "Lacking experience. It is necessary to publish at least two typographical sets of the previous level."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_typo3" and (nsp_genie_typographic < 2 or nsp_genie_typographic_exp < 2):
                        m "Lacking experience. It is necessary to publish at least two typographical sets of the previous level."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_typo4" and (nsp_genie_typographic < 3 or nsp_genie_typographic_exp < 2):
                        m "Lacking experience. It is necessary to publish at least two typographical sets of the previous level."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_typo5" and (nsp_genie_typographic < 4 or nsp_genie_typographic_exp < 2):
                        m "Lacking experience. It is necessary to publish at least two typographical sets of the previous level."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_typo6" and (nsp_genie_typographic < 5 or nsp_genie_typographic_exp < 2):
                        m "Lacking experience. It is necessary to publish at least two typographical sets of the previous level."
                        hide screen gift
                        jump books_list
                        
                if wtevent.GetValue("block")=="books_newsp2":
                    if wtevent.Name == "nsp_newsp_book_photo2" and (nsp_genie_photocamera < 1 or nsp_genie_photocamera_exp < 3):
                        m "Lacking experience. You need at least three shoots with a camera of the previous type."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_photo3" and (nsp_genie_photocamera < 2 or nsp_genie_photocamera_exp < 3):
                        m "Lacking experience. You need at least three shoots with a camera of the previous type."
                        hide screen gift
                        jump books_list

                    if wtevent.Name == "nsp_newsp_book_photo4" and (nsp_genie_photocamera < 3 or nsp_genie_photocamera_exp < 3):
                        m "Lacking experience. You need at least three shoots with a camera of the previous type."
                        hide screen gift
                        jump books_list
                        
                    if wtevent.Name == "nsp_newsp_book_video" and (nsp_genie_photocamera < 4 or nsp_genie_sphere_ruby_level_eff < 1 or nsp_genie_sphere_diamond_level_eff < 1 or nsp_genie_sphere_sapphire_level_eff < 3):
                        m "To develop skills in this book, you will need knowledge of all kinds of cameras, a crystal ball, level 3 sapphire, ruby and diamond."
                        hide screen gift
                        jump books_list
                        
############

                if wtevent.GetValue("block")=="books_edu":
                    if wtevent.prevInList.GetValue("block")!=wtevent.GetValue("block") or wtevent.prevInList.IsDone():
                        jump reading_book_xx
                    else:
                        m "This book is still too hard for me."
                        hide screen gift
                        jump books_list
                else:
                    if wtevent.Name=="book_05_b" and not this.book_05.IsDone():
                        m "There are strange people who begin the book with the second part. But I'm not one of those."
                        jump expression _label
                    else:
                        jump reading_book_xx #"reading_book_01"
            "- Never mind -":
                hide screen gift
                jump expression _label #books_on_improvement

    label reading_book_done:
        $ the_gift = wtevent._img#"03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3
        "\"[wtevent._caption]\"" "[wtevent._description]."


# Отдельная обработка для Вайфу - ее нужно читать несколько раз                                
        if wtevent.Name=="book_07":
            if waifu_book_completed:
                m "I do not think re-reading this book will give me anything."
                hide screen gift
                jump fiction_books

            if dear_waifu_completed_once:
                if book_07_units == 0:
                    m "I don't think reading this book again will give me any new ideas. Should I just read it for fun though?"
                    menu:
                        "- Read the book again -":
                            hide screen gift
                            jump reading_book_xx
                        "- Never mind -":
                            hide screen gift
                            jump fiction_books
                else:
                    m "I have already finished it, but decided to read again for the pleasure..."
                    hide screen gift
                    jump reading_book_xx
        else:
            m "I've already finished it. "
            if wtevent._block=="books_edu" and wtevent._conclusion!="":
                m "Она дала мне новый навык: [wtevent._conclusion]"
            else:
                m "[wtevent._conclusion]"

            if wtevent.Name=="book_04":
                g4 "I have mastered the control over my spirit. Now I shall always complete an additional chapter when doing paperwork."
                g9 "My spirit is my bitch"

        hide screen gift
        jump expression _label

label desk:
    $ menu_x = 0.5 
    $ nsp_genie_sphere_video_txt = ""

    menu:
### DR'S NEWSPAPER ooo ###

        "- Find an directory application -" if nsp_pre_snape == 5 and nsp_pre_dahre == 0:
            $ nsp_pre_dahre = 1
            m "You found an additional catalog of books for the printing business."
            jump day_main_menu
            
        "- Search for other applications for the directory -" if nsp_newspaper_menu == 4:
            $ nsp_newspaper_menu = 5
            m "You found an additional directory of printing funding."
            jump day_main_menu
            
        "- Try to fix the crystal ball -" if nsp_newspaper_menu >= 9 and nsp_newspaper_menu < 15:
            
            if nsp_newspaper_menu == 9 :
                ">Вы внимательно осмотрели шар со всех сторон. На вид он кажется сделан из тусклого стекла, которое почти не пропускаяет свет."
                ">Никаких подсказок. В такой ситуации можно прибегнуть к внутреннему зрению джина."
                ">На это ушло много времени, но вам удалось обнаружить особую магическую ауру шара."
            elif nsp_newspaper_menu == 10 :
                ">После долгой медитации вы обнаружили, что аура шара чужда этому месту. возможно даже..."
                ">Нет, лучше это все-таки проверить."
            elif nsp_newspaper_menu == 11 :
                ">Новое исследование подтвердило вашу догадку. Этот предмет не из мира Хогвартса."
            elif nsp_newspaper_menu == 12 :
                ">Потраченное время все-таки принесло плоды. Вам удалось уловить отблески солнца, играющие на бескрайних песках."
                ">Сухость воздуха и остроту колючек. Чары и месть, отвагу и честь..."
                ">Этот хрустальный шар был сделан в мире Аграбы, в вашем родном мире !"
                ">Вот почему он работает не как шар для предсказаний ! В Аграбе правила магии совсем иные !"
                ">Теперь нет сомнений, что вы сможете его починить."
            elif nsp_newspaper_menu == 13 :
                ">Вы потратили много времени на попытки призвать свою космическую силу."
                $hero (g4,"Ыыыыыыыть.")
                $hero (g4,"Аргх!")
                $hero (g4,"Ааааать.")
                $hero (g4,"Ух.")
                ">И так в течение нескольких часов..."
                ">Безрезультатно."
            elif nsp_newspaper_menu == 14 :
                $hero (m,"Почему же все бесполезно ?")
                $hero ("Конечно я никогда не был по-настоящему {size=+4}всесильным{/size}, но это уже слишком.")
                $hero ("А ведь что-то могло бы задать моей магии необходимый импульс.")
                $hero (g6,"Хм.")
                $hero (g6,"Раньше лучшим стимулом было выполнение какого-нибудь желания.")
                $hero (g7,"Итак, Джин, сконцентрируйся. Снейп желает фотографии из самых укромных мест, и единственное средство - работающий шар.")
                $hero (g4,"Ну же ! Напрягись ! Ыыыыыы.")
                ">Кажется, у вас начало получаться !"
                $hero (g4,"Аргх !")
                $hero (g8,"Фу-ух !")
                ">На столе перед вами лежит целый хрстальный шар. Слабое свечение исходит изнутри"
                ">Теперь вы способны легко понять, как он устроен, и составляете небольшую инструкцию."
                $hero (m,"Наконец-то !")
                $ nsp_genie_sphere = True
                
            $ nsp_newspaper_menu += 1
            
            if daytime:
                jump night_start
            else: 
                jump day_start  

###
        "- Осмотреть -" if not desk_examined:
            $ desk_examined = True
            m "Seems like an ordinary enough desk..."
            m "Somewhat cluttered."

#===TG MODS START===

            m "Hm............ There's a calendar?"
            $ renpy.say(m, "And if I'm reading it right.....\n\nIt's........... \"%s %d, %s\"?" % (month_info[cal_month][5], cal_day, week_info[day_of_date((cal_month, cal_day))][1]))
            m "Whatever that means......"
            m "But, by the looks of it someone's been doodling notes on it."
            m "Could be worth studying it a little...."

            # Let's say Dumblegenie learns of the Hogsmeade dates from Dumbledore previously marking them down on the
            # in the calendar.
            $ known_dates['hogsmeade_weekends'] = True

            # Further, let's then allow those dates to show up by adding them to the places they need to go.
            $ dates_list = important_dates['hogsmeade_weekends']
            $ add_cal_notes(dates_list, 'hogsmeade_weekends')

            show screen cal_button_flash
            pause(1.5)
            hide screen cal_button_flash

#===TG MODS STOP===

            jump day_main_menu

## DR'S DEBUG TEST           
        "- Тест 1 -" if False :
            $ menu_x = 0.2 #Menu is moved to the left side.
            $ pos = POS_410
                
            $ hermi.whoring = 24
            
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            $ hermione_chibi_xpos = 400 #Near the desk.
            $ hermione_chibi_ypos = 250 #Добавил, т.к. без этого иногда падает игра.
            show screen hermione_02 #Hermione stands still.
            show screen bld1
            with d3
            
            $ nsp_germiona_kviddich_1_statimg = "New"
            $ nsp_germiona_kviddich_1_photo = "dis"
            $ nsp_event_kviddich_1 = 0
            $ cur_level = 1
            call wrd_dress_change_silent
            call nsp_event_kviddich_1
            jump hermione_goout
            
        "- Тест 2 -" if False :
        
            $ menu_x = 0.2 #Menu is moved to the left side.
            $ pos = POS_410
                
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            $ hermione_chibi_xpos = 400 #Near the desk.
            $ hermione_chibi_ypos = 250 #Добавил, т.к. без этого иногда падает игра.
            show screen hermione_02 #Hermione stands still.
            show screen bld1
            with d3
            $ hermi.whoring = 24
            jump hermione_approaching
#            jump hermione_goout            
            
        "- Тест 3 -" if False :

            $ hermi.whoring = 24
            $ cataloug_found = True
            call the_oddities
            jump desk
            
        "- Тест 4 -" if False :

            $ hermi.whoring = 24
            $ cataloug_found = True
            call daphne_main_menu
            jump desk
            
### DR'S NEWSPAPER ooo ###

        "- Писать статьи для газеты -" if nsp_newspaper_articles < 8 and nsp_newspaper_menu > 0 and nsp_newspaper_ready == False and nsp_newspaper_published == False:
            jump nsp_articles_work
        "{color=#858585}- Писать статьи для газеты -{/color}" if nsp_newspaper_articles >= 8 and nsp_newspaper_menu > 0 and nsp_newspaper_published == False:
            m "Я уже приготовил достаточно материала, газета готова к публикации."
            jump desk
        "{color=#858585}- Писать статьи для газеты -{/color}" if nsp_newspaper_ready == True and nsp_newspaper_menu > 0 and nsp_newspaper_published == False:
            m "Я уже приготовил достаточно материала, газета готова к публикации."
            jump desk
        "{color=#858585}- Писать статьи для газеты -{/color}" if nsp_newspaper_menu > 0 and nsp_newspaper_published == True:
            m "Газета была недавно опубликована. Перед продолжением работы нужно прочитать отзыв из министерства."
            jump desk
            
###   
            
        "- Делать бумажную работу -" if finished_report < 6 and not got_paycheck and not day == 1 and work_unlock2:
            jump paperwork
        "{color=#858585}-Do paperwork-{/color}" if finished_report >= 6 and not got_paycheck:
            m "I have already completed six reports this week."
            jump desk
        "{color=#858585}-Do paperwork-{/color}" if got_paycheck: # When TRUE paycheck is in the mail.
            m "First, I need to get paid."
            jump desk
         
        "-Book Collection-" if not day == 1 and cataloug_found: 
            label books_list:
                $choose=None
                menu:
### DR'S NEWSPAPER ooo ###

                    "- Книги о газетном деле -" if nsp_pre_dahre >= 1:
                        label books_on_newspaper:
                            $_label="books_on_newspaper"
                            $_block="books_newsp"
                            jump menu_reading_book
                            
                    "- Мануалы инструментов для газетного дела -" if nsp_newspaper_menu >= 5:
                        label manuals_on_newspaper:
                            $_label="manuals_on_newspaper"
                            $_block="books_newsp2"
                            jump menu_reading_book
                            
###
                    "- Обучающие книги -":
                        label books_on_improvement:
                            $_label="books_on_improvement"
                            $_block="books_edu"
                            jump menu_reading_book

                    "-Novels-":
                        label fiction_books:
                            $_label="fiction_books"
                            $_block="books_fict"
                            jump menu_reading_book

                    "-Never mind-":
                        jump desk

        "- Continue reading -" if currentBook!=None:
            $wtevent=this(currentBook)
            jump reading_book_xx 
          
        
                    
                    
                    
        #"- The muggle oddities -" if have_catalogue: #Real thing
        "-DAHR's oddities-" if cataloug_found: 
            if order_placed or package_is_here:
                show screen bld1
                with d3
                dahr "Please be patient. The owl has been dispatched."
                hide screen bld1
                with d3
                jump desk
            else:
                 jump the_oddities
        
        
        

        # "- Jerk off on Hernione's panties -" if request_03: #True when Hermione has no panties on.
        #     jump jerk_off
        "-Jerk off-" if not day < 5:
            jump jerk_off 
        "-Take a nap-" if daytime and not day == 1:
            jump night_start
        "-Go to sleep-" if not daytime and not day == 1:
            jump day_start
            
### DR'S NEWSPAPER ooo ###

        "- Newspaper -" if nsp_newspaper_menu >= 2 and cataloug_found: 
            label nsp_newspaper_list:
                $choose=None
                menu:

                    "- Publish newspaper -" if nsp_newspaper_ready == True:
                        label nsp_newspaper_publication:

                            $choose=None
                            menu:

                                "- Yes -":
                                    $ nsp_newspaper_ready = False 
                                    $ nsp_newspaper_qual = (10 * (1 + nsp_genie_writer) * (1 + nsp_genie_typographic)) + (5 * nsp_genie_photocamera)
                                    $ nsp_newspaper_qual_last = nsp_newspaper_qual
                                    $ nsp_newspaper_cur_money = int((nsp_newspaper_qual + (nsp_newspaper_bonus_point/10) ) * (0.7 + (one_of_ten * 0.06) ))
                                    
                                    $ nsp_newspaper_published = True
                                    $ nsp_genie_typographic_exp += 1
                                    
                                    ">Вы поставили на свежий выпуск газеты магический штамп и лист исчез с тихим шуршанием, чтобы спустя мгновение возникнуть на стенде главного холла вместо прежнего."
                                    
                                    $ nsp_newspaper_bonus_point_last = nsp_newspaper_bonus_point
                                    $ nsp_newspaper_bonus_text = "нет"
                                    $ nsp_newspaper_bonus_point = 0
                                    
                                    if nsp_newspaper_menu == 7 :
                                        $ nsp_newspaper_menu = 8
                                    
                                    call screen main_menu_01
                            
                                "- Nevermind -":
                                    jump desk
                                    
                    "{color=#858585}- Publish newspaper -{/color}" if nsp_newspaper_ready == False:
                         ">Not enough material to publish an article."
                         jump desk
                
                    "- Newspaper options -" if nsp_newspaper_menu >= 4:
                        jump newsp_stats_00


                    "- Nevermind -":
                        jump desk
                        
        "- Crystal Ball -" if nsp_genie_sphere :
                
            $choose=None
            if nsp_genie_sphere_video :
                $ nsp_genie_sphere_video_txt = "\nВозможен перенос видео в газету"
            else :
                $ nsp_genie_sphere_video_txt = ""

            menu:
            
                "Уровень владения: [nsp_genie_sphere_level]\nСила сапфира [nsp_genie_sphere_sapphire_level_eff]\nСила рубина [nsp_genie_sphere_ruby_level_eff]\nСила алмаза [nsp_genie_sphere_diamond_level_eff][nsp_genie_sphere_video_txt]"
                
                "- Инструкции -":
                
                    call bigtext(["Инструкция к Хрустальному Шару.\n\nШар позволяет получать изображение на расстоянии. К сожалению, для вызова и поддержания данной магии необходимо "
                    "специальное простое заклинание со стороны другого волшебника. Иначе говоря, подсмотреть за кем-то вряд ли получится.\n\nКроме того, нужны три фокусных камня: сапфир, рубин и алмаз.\n\n"
                    "Сапфир отвечает за интенсивность связи. В зависимости от уровня он обеспечивает: 1 - разговор, 2 - слышимость звуков вокруг другого, 3 - изображение головы, 4 - изображение тела, 5 - полную картину.\n\n",
                    "Рубин отвечает за время четкого фокуса (влияет на возможности любой записи изображения): 1 - 30 секунд в день, 2 - 1 минута, 3 - 2 минуты, "
                    "4 - 5 минут, 5 - 10 минут.\n\nАлмаз отвечает за дальность действия шара: 1 - только комната, 2 - главное здание Хогвартса, 3 - основная территория Хогвартса, "
                    "4 - все окрестности Хогвартса (Запретный лес, Хогсмид), 5 - неограничено.\n\nКроме того, недостаточный навык владения шаром будет ограничивать силу камня.\n\n",
                    "Навык будет постепенно расти за счет любого применения шара. Если параметры шара не позволяют проводить съемку, то после журналистского задания будет получена "
                    "только статья, которая принесет намного меньше популярности.\n\n"
                    "Для начала нужно купить любой сапфир и поговорить с Гермионой. В дальнейшем понадобятся сапфир не ниже 3 уровня, рубин и алмаз. Фотоъемка в студии не использует "
                    "шар. После приобретения рубина, алмаза, сапфира 3 уровня и наилучшего фотоаппарата появится новая возможность, не забудьте внимательно изучить доступные книги в инструментах для газеты.\n\n"])

                    jump desk
                
                "- Ничего -":
                    jump desk

###
        "- Ничего -":
            call screen main_menu_01
            
            

 #===TG MODS START===

        "- Study calendar -" if desk_examined and not day == 1:
            menu:
                # This is when playing an old game, and the above event didn't happen (since the mod wasn't installed,
                # and the desk is now set to (forever) examined.)
                #
                # I might later turn this into a general function to refresh the calendar. Possibly allow purging of
                # data to make a clean slate. Possibly only to correct things.
                #
                # I'll do that kind of thing later, once more has been implemented.
                "-Перепроверить даты-" if desk_examined and not known_dates['hogsmeade_weekends']:
                    m "Перелистывая страницы........"
                    m "Кто-то.... явно любит все эти \"Хогсмид по выходным\"."
                    m "Кто-то пьянчуга, судя по ним."
                    $ known_dates['hogsmeade_weekends'] = True
                    $ dates_list = important_dates['hogsmeade_weekends']
                    $ add_cal_notes(dates_list, 'hogsmeade_weekends')
                    show screen cal_button_flash
                    pause(1.5)
                    hide screen cal_button_flash
                    if daytime:
                        jump day_main_menu
                    else:
                        jump night_main_menu

                "-Ничего-":
                    if daytime:
                        jump day_main_menu
                    else:
                        jump night_main_menu

#===TG MODS STOP===
    
  
            
            


    
### READING ###

label reading_book_xx:

### Plays sound effects appropriate for reading. 
# Music
    stop music fadeout 2.0
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else:
        call fire_out #Shows Genie reading a book near the window.

    if daytime and not raining:
        #play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        play weather "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    
    if not daytime and not raining:
        play weather "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...


    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...


    hide screen gift
    with d3
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.


    if raining:
        ">Вы читаете книгу [wtevent._caption], слушая дождь, барабанящий по крыше вашей башни."
    else:
        ">Вы читаете книгу [wtevent._caption]..."
   
    call chap_finished_xx
    
    call chapter_check_book_xx #Checks if the chapter just finished was the last one.
    
#Проверка на концентрацию
    if concentration>0:
        if concentration == 1:
            $ concentraton_check = renpy.random.randint(1, 6) #Copper book.
            if concentraton_check == 1:
                call concetrationg_reading
        if concentration == 2:
            $ concentraton_check = renpy.random.randint(1, 4) #Bronze book.
            if concentraton_check == 1:
                call concetrationg_reading
        if concentration == 3:
            $ concentraton_check = renpy.random.randint(1, 2) #Silver book.
            if concentraton_check == 1:
                call concetrationg_reading
        if concentration == 4:                                                               #Golden book.
            call concetrationg_reading
        
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl>0:
        $ speed_dummies = Rand([60,30,10][s_reading_lvl-1]//turbo)  # Массив содержит размер интервала для расчета вероятности. Первая книга 10/60 шансов прочитать доп. главу, вторая 10/30, 3-я 10/20 . В режиме турбо интервал уменьшается вдвое
        if speed_dummies <= 10: #Success.
            ">Using speed reading techniques, you rationally use your time and continue to read."
            call chap_finished_xx
            call chapter_check_book_xx #Checks if the chapter just finished was the last one.
#            ">There are still some chapters left."

#===#############################################       

    if raining:
        if not fire_in_fireplace:
            ">Rain outside the window calms you and you feel great reading ..."
            ">You are trying to continue to read, but soon realize that the air in the room is too humid."
        else:
            ">Rain outside the window calms you and you feel great reading ..."
            call chap_finished_xx
            call chapter_check_book_xx #Checks if the chapter just finished was the last one.
#            ">There are still a few chapters."

    ">There are still some chapters left."       
    $currentBook=wtevent.Name

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start #pered_menu#
    else: 
        jump day_start
        
###### Concentration reading
label concetrationg_reading:
    ">Во время чтения вы идеально сконцентрированы, что позволяет вам прочитать дополнительную главу."
    call chap_finished_xx
    call chapter_check_book_xx
    return
label chap_finished_xx:
    if wtevent.Name=="book_05":
        $wtevent.IncValue("status", 1)  #+=1
        $renpy.say("Глава [wtevent._status]", 
        [
         "Galadriel - a gentle and gracious elven princess is introduced into the story.",
         "Galadriel's father - King Methis and his childhood friend Mofothelis are introduced into the story.",
         "King Methis makes an announcement. His daughter, princess Galadriel is to be wed to chancellor Mofothelis.",
         "Galadriel refuses to marry a man who is thrice her age and whom, up until now, she considered only as her uncle.",
         "King Methis dismisses her daughter's \"foolish\" complaints. Galadriel decides to run away.",
         "Galadriel manages to leave the royal residence at night unnoticed...",
         "King Methis is furious about his daughter's escape. He decides to personally lead the search party.",
         "Galadriel rides her mare \"white dove\" through the forest. The Princess enjoys her freedom... After a while she meets a rather handsome human nobleman on a horse...",
         "Galadriel rides alongside the nobleman. They exchange meaningless pleasantries. He makes her laugh. Suddenly the nobleman attacks the princess and knocks her out!...",
         "Galadriel comes about. To her horror she realizes that the nobleman is having his way with her. Galadriel is screaming for help but The handsome man keeps on raping her.",
         "Galadriel tries to fight the nobleman off. Only now she notices that about half a dozen men are surrounding them. The men are sneering viciously.",
         "After the nobleman is done with Galadriel, every one of his men in turn has a go at the elven princess. Galadriel cries and begs them to stop.",
         "Galadriel finds herself in a cage at some sort of market. Her hands are tied, Her noble garments are ripped to shreds and her hair is full of twigs and dry semen.",
         "A fat, rich looking man buys Galadriel and brings her to his house. The princess does not cry anymore. She is happy to be out of the cage.",
         "Galadriel is allowed to take a bath after which a servant brings her clean clothes and some food.",
         "Galadriel is starting to feel hopeful but it does not last. Soon she realizes what kind of establishment this is: a whorehouse.",
         "The elven princess is forced to work as a whore. She detests her new life but has very little choice.",
         "Galadriel gains popularity quickly. Humans, Dark Elves and even the occasional dwarf - she spreads her legs for everyone.",
         "The fame of the young and beautiful elven whore spreads. Galadriel accepts her new life in the brothel.",
         "Suddenly and abruptly everything changes. Galadriel finds out that she is pregnant. -End of book one-"
        ][wtevent._status-1]
        )


    if wtevent.Name=="book_05_b":
        $wtevent.IncValue("status", 1)  #+=1
        $renpy.say("Глава [wtevent._status]",
        [   
         "Galadriel has been pregnant for several months now. To the princess' own surprise her popularity grows seemingly in direct correlation to the size of her belly.",
         "Although Galadriel maintains the appearance of an obedient whore, in truth she contemplates her escape from the brothel",
         "The Elven Princess-Whore knows nothing of the life outside the of walls of the brothel. But it does not affect her determination to escape.",
         "It takes a lot of preparation and careful planning but Galadriel manages to successfully escape from the brothel.",
         "Galadriel soon gets lost in the vast city and is forced to spend the night on the street.",
         "Food is hard to come by on the streets. Galadriel fights a pack of stray dogs over some scraps and one of them bites her hand badly.",
         "The Pregnant Galadriel offers her company to a couple of filthy looking homeless men in exchange for food. She spends the night with them.",
         "Galadriel realizes that her live back in the brothel was a heaven compared to the live she's been leading for the past several days. She decides to return.",
         "Galadriel's owner - the fat, wealthy man does not punish Galadriel for escaping. He is happy to have one of his most popular girls back.",
         "Galadriel is, yet again, warm, clean and well fed. She is glad to be back and as popular as ever.",
         "Galadriel keeps servicing the clients throughout the rest of her pregnancy. The baby is due any day now...",
         "A wealthy man wearing a mask booked Galadriel for an entire day. Galadriel is wondering about the man's true identity rather lazily while pleasuring him.",
         "The mystery man spends the entire day by having his way with Galadriel. Her engorged breasts drip milk heavily as the man fucks her.",
         "The masked man splatters Galadriel's face with cum for the second time today. He then chooses to reveal his identity and takes his mask offо.",
         "Galadriel recognizes the man as her father - King Methis. Only now he realizes that the pregnant whore he fucked for hours is his daughter.",
        # Only now he realizes that the pregnant whore he fucked for hours is his daughter.
         "The man embraces his speechless child. Galadriel's eyes have a vacant look in them as her father's semen drips down her face...",
         "Galadriel screams in terror. To her surprise she finds herself back in the royal residence and in her own bed.",
         "It takes the elven princess several minutes to realize that she was never pregnant. The entire adventure was nothing but a dream.",
         "Galadriel rushes to her father's chambers and embraces him. The girl is relived to have her old life \"back\". She happy agrees to marry chancellor Mofothelis.",
         "{size=-1}Galadriel is at the altar. She is content and happy. Suddenly she notices something that fills her heart with horror. There is a scar on her hand. The mark of a dog's bite. -The End-{/size}"
        ][wtevent._status-1]
        )

    if wtevent.Name=="book_06":
        $wtevent.IncValue("status", 1)  #+=1
        $renpy.say("Глава [wtevent._status]", 
        [
        "A family of noble northmen is introduced into the story.",
        "The royal family and the king are introduced into the story.",
        "Another family is introduced into the story.",
        "Some incest action between a brother and his sister, the queen, is taking place.",
        "Attempted child murder takes place. The kid barely survives and is now in a coma.",
        "Some more characters are introduced into the story.",
        "Some characters hatch an evil scheme against some other characters.",
        "The king gets poisoned and dies. Some more brother on sister incest takes place.",
        "A certain character you've been especially rooting for gets executed.", # НЕ ПЕРЕВЕДЕНо
        "Some new characters are introduced into the story.",
        "Some female characters get raped and then killed brutally.",
        "Some more members of the noble family of northmen find their untimely demise.",
        "Some more women get raped. Some of them manage to survive. (Surely only to get raped some more later).", 
        "The characters you hate clash in an epic battle against the characters you are rooting for.",
        "Most of the characters you hate survive the battle. Every single character you were rooting for is dead.",
        "Some more rapes take place, then some more murders... (You don't even care anymore...)", 
        "A new group of characters is introduced into the story. You sort of starting to root for one of them.",
        "The character you were rooting for falls in love with a pretty girl.",
        "he character you were rooting for gets brutally murdered. His girl gets raped and then murdered as well.",
        "A new race of half-frozen undead monsters is introduced into the story. To be continued..."
        ][wtevent._status-1]
        )

    if wtevent.Name=="book_07":
        $ book_07_units +=1
        $wtevent._status=book_07_units
        call waifu

### DR'S NEWSPAPER ooo ###
    if wtevent.Name=="nsp_newsp_book_pre":
        $wtevent.IncValue("status", 1)  #+=1
        $renpy.say("Глава [wtevent._status]", 
        [
        "Во вводной главе говорится об истории появления и развития газет в мире магов.",
        "Вы изучаете основы написания газетных статей.",
        "Вы изучаете основы написания газетных статей.",
        "Вы изучаете основы написания газетных статей.",
        "Вы изучаете основы редактирования газет.",
        "Вы изучаете основы редактирования газет.",
        "Вы изучаете основы оформления газет.",
        "Вы изучаете основы оформления газет.",
        "Вы изучаете основы оформления газет.",
        "В заключительной главе приводится краткий перечень советов начинающему редактору.",
        ][wtevent._status-1]
        )

    if wtevent.Name in ["nsp_newsp_book_p01", "nsp_newsp_book_p02a", "nsp_newsp_book_p02b", "nsp_newsp_book_p03a", "nsp_newsp_book_p03b"]:
        $wtevent.IncValue("status", 1)  #+=1
            
    if wtevent.Name in ["nsp_newsp_book_p04", "nsp_newsp_book_p05a", "nsp_newsp_book_p05b", "nsp_newsp_book_p06a", "nsp_newsp_book_p06b"]:
        $wtevent.IncValue("status", 1)  #+=1

    if wtevent.Name in ["nsp_newsp_book_typo1", "nsp_newsp_book_typo2", "nsp_newsp_book_typo3", "nsp_newsp_book_typo4", "nsp_newsp_book_typo5", "nsp_newsp_book_typo6"]:
        $wtevent.IncValue("status", 1)  #+=1
            
    if wtevent.Name in ["nsp_newsp_book_photo1", "nsp_newsp_book_photo2", "nsp_newsp_book_photo3", "nsp_newsp_book_photo4"]:
        $wtevent.IncValue("status", 1)  #+=1
            
    if wtevent.Name=="nsp_newsp_book_video":
        $wtevent.IncValue("status", 1)  #+=1
        $renpy.say("Глава [wtevent._status]", 
        [
        "Во вводной главе говорится об истории появления и развития прорицательства в мире магов. И только в конце вы сообразили, что это вообще вас не касается.",
        "Вы изучаете принципы компоновки видеокадра.",
        "Вы изучаете художественные правила видеомонтажа.",
        "Глава содержит в себе биографию автора. Безобразие.",
        "Вы изучаете заклинания для переноса информации из шара на бумагу.",
        "Вы продолжаете изучать заклинания для переноса информации из шара на бумагу.",
        "Внезапно, целая глава посвящена философским мыслям автора о жизни. Пожалуй, эти страницы стоит приберечь для борьбы с бессонницей.",
        "Вы продолжаете изучать заклинания для переноса информации из шара на бумагу. Кажется, начинает понемногу получаться.",
        "Вы завершаете изучать заклинания для переноса информации из шара на бумагу. Остается прочитать заключительную главу.",
        "Ну разумеется, в последней главе находится фотография автора и его благодарности жене, детям, домашним животным и маглам по соседству.",
        ][wtevent._status-1]
        )

###        
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    if wtevent._block=="books_edu": 
#        $wtevent._status=this.GetCall(wtevent.Name).SetValue("status", wtevent._status+1)  #wtevent.SetValue("status", wtevent._status+1)  #+=1
        $wtevent.IncValue("status", 1)    
    ">Вы закончили \"главу [wtevent._status]\" этой книги."
    return
    
###
label chapter_check_book_xx: #Checks if the chapter just finished was the last one.
    if (wtevent.IsDone() and wtevent.Name!="book_07") or (wtevent.Name=="book_07" and book_07_units == 20):#book_xx_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">This was the last chapter. You have finished this book."
        $currentBook=None

        if wtevent.Name=="book_06":
            g4 "What kind of garbage! I hate the person who wrote it!"
            m "However, all the rape led me to a couple of ideas..."


        if wtevent.Name=="book_07":
            if complited_leena_already and complited_shea_already and complited_stevens_already and victoria >= 1 and shea >= 1 and leena >= 1: #Harem ending. The DAHR's ticket.
                m "Wow! What a great book! That was intense!"
                
                #m "No, I mean it! What a great peace of fiction! That Akabur dude must be a genius!"
                if not found_dahrs_ticket_once:
                    m "Hm...?"
                    m "What is that...? A bookmark?"
                    $ the_gift = "03_hp/18_store/06.png" # The DAHR's ticket.
                    show screen gift
                    with d3
                    $ renpy.play('sounds/win2.mp3') #Sound of finding an item.
                    ">You found a DAHR's voucher."
                    hide screen gift
                    with d3
                    m "Hm..."
                    $ vouchers += 1 #Shows the amount of DAHR's vouchers in your possession.
                    $ found_dahrs_ticket_once = True # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.
                    $ waifu_book_completed = True
            elif shea_waifu and shea >= 8: 
                if not complited_shea_already: #Finished with Shea for the first time.
                    m "Not bad. I really grew to care about that Shea girl..."
                    g9 "Well, her and her anal virginity..."
                    $ complited_shea_already = True
                else: #Finished with Shea for the second time.
                    m "So I ended up with Shea again, huh?"
                    m "Hm... Maybe I should try and make different choices next time...?"
            elif victoria_waifu and victoria >= 7:
                if not complited_stevens_already: #Finished with Ms.Stevens for the first time.
                    m "Not bad, not bad. That Miss Stevens Lady turned out to be one dirty slut..."
                    $ complited_stevens_already = True
                else: #Finished with Shea for the second time.
                    m "So I ended up with Miss Stevens again?"
                    m "Hm... Maybe I should try and make different choices next time?"
            elif leena_waifu and leena >= 8:
                if not complited_leena_already: #Finished with Leena for the first time.
                    g9 "Sweet! I love happy endings!"
                    $ complited_leena_already = True
                else: #Finished with Shea for the second time.
                    m "So I ended up with that blond chick again?"
                    m "Hm... Maybe I should try and make different choices next time?"

            else:
                m "Hm... What an anticlimactic ending..."
                m "Maybe I should read it again sometime."
            
            $ book_07_units = 0 #RESTING THE BOOK FOR ANOTHER PLAYTHORUGH.
            $ shea = 0 #RESETING SHEA'S POINTS FOR THE NEXT PLAYTHOURGH.
            $ victoria = 0
            $ leena = 0

            if not dear_waifu_completed_once:
                $ dear_waifu_completed_once = True # Turns TRUE when complete the book for the first time with any ending. Makes sure you get +1 imagination only once.
                $ imagination +=1


        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        if wtevent._conclusion!="":
            if wtevent._block=="books_edu":
                m "Новый навык: [wtevent._conclusion]"
            else:
                m "[wtevent._conclusion]"

# Изменения навыка по завершению книги (кроме Вайфу - book_07 в ней навык меняется отдельно)
# Можно было сделать через событие, но тогда получится более громоздко. Так что пока так:
        if wtevent.Name in ["book_01", "book_02", "book_03", "book_04"]:
            $ concentration += 1
        if wtevent.Name in ["book_05", "book_05_b", "book_06"]:     
            $ imagination +=1
        if wtevent.Name in ["book_08", "book_09", "book_10"]:
            $ s_reading_lvl +=1
        if wtevent.Name in ["book_12", "book_13", "book_14", "book_15"]:
            $ speedwriting += 1

### DR'S NEWSPAPER ooo ###

        if wtevent.Name=="nsp_newsp_book_pre" and nsp_newspaper_menu == 0:
            $ nsp_newspaper_menu = 1
            
        if wtevent.Name in ["nsp_newsp_book_p01", "nsp_newsp_book_p02a", "nsp_newsp_book_p02b", "nsp_newsp_book_p03a", "nsp_newsp_book_p03b"]:
            $ nsp_genie_writer += 1
            
        if wtevent.Name in ["nsp_newsp_book_p04", "nsp_newsp_book_p05a", "nsp_newsp_book_p05b", "nsp_newsp_book_p06a", "nsp_newsp_book_p06b"]:
            $ nsp_genie_writer += 1

        if wtevent.Name in ["nsp_newsp_book_typo1", "nsp_newsp_book_typo2", "nsp_newsp_book_typo3", "nsp_newsp_book_typo4", "nsp_newsp_book_typo5", "nsp_newsp_book_typo6"]:
            $ nsp_genie_typographic += 1
            $ nsp_genie_typographic_exp = 0
            
        if wtevent.Name in ["nsp_newsp_book_photo1", "nsp_newsp_book_photo2", "nsp_newsp_book_photo3", "nsp_newsp_book_photo4"]:
            $ nsp_genie_photocamera += 1
            $ nsp_genie_photocamera_exp = 0
            
        if wtevent.Name == "nsp_newsp_book_video" :
            $ nsp_genie_sphere_video = True
            
###
            
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return        
    
 

###
label fire_in: #Shows Genie reading a book near the fireplace.
    hide screen chair
    hide screen genie
    show screen reading_near_fire
    with Dissolve(0.3)
    return
###
label fire_out: #Shows Genie reading a book near the window.
    hide screen chair
    hide screen genie
    show screen reading
    with Dissolve(0.3)
    return
    
 
 
    
    
    
    
        
    
    
### PAPERWORK ###
label paperwork:
    stop music fadeout 1.0
    if daytime:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else: 
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        stop bg_sounds 
    
    
    hide screen genie
    show screen paperwork
    with Dissolve(0.3)
    ">You do some paperwork."
    
    call finished_working_chapter #Chapter finished. $ report_chapters += 1
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
        
    if daytime: # Makes sure that check happens only at nighttime. 
        pass
    else:
        if wather_generator >= 31 and wather_generator <= 40: # FULL MOON
            call f_moon_bonus
        if wather_generator >= 51 and wather_generator <= 60: # FULL MOON
            call f_moon_bonus
           
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### CONCENTRATION CHECK ###========================================================================
    if concentration == 1:
        $ concentraton_check = renpy.random.randint(1, 6) #Copper book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 2:
        $ concentraton_check = renpy.random.randint(1, 4) #Bronze book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 3:
        $ concentraton_check = renpy.random.randint(1, 2) #Silver book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 4:                                                               #Golden book.
        call concentration_label
#    if concentration == 5:
#        $ concentraton_check = renpy.random.randint(1, 2) #Platinum book.
#        if concentraton_check == 1:
#            call concentration_label
#    if concentration == 6:
#            call concentration_label
    ###==============================================================================================
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### SPEEDWRITING CHECK ###========================================================================
    if speedwriting == 1:
        $ speedwriting_check = renpy.random.randint(1, 6) #"\"Speedwriting for dummies.\"" # 1/10 chance
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 2:
        $ speedwriting_check = renpy.random.randint(1, 4) #"\"Speedwriting for beginners.\"" # 1/8 chance of it to pop up.
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 3:
        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for intermediate.\"" # 1/6 chance of it to pop up.
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 4:
            call speedwriting_label
#    if speedwriting == 5:
#        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for experts.\"" # 1/2 chance of it to pop up.
#        if speedwriting_check == 1:
#            call speedwriting_label
#    if speedwriting == 6:
#        call speedwriting_label #""\"Speedwriting for maniacs.\"" # 1 (sure) chance of it to pop up.
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
            

    show screen genie
    hide screen paperwork
    
    
    
    if daytime:
        jump night_start
    else: 
        jump day_start    
    
### 
label report_chapters_check:
    if report_chapters >= 7:
        ">You've completed a report."
        $ report_chapters = 0
        $ finished_report += 1
        $ total_report += 1
    return
### FULL MOON BONUS ###
label f_moon_bonus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">The Full moon makes you feel more productive.\n>You finished [report_chapters] chapters so far."
    return
###
label finished_working_chapter:
    $ report_chapters += 1
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">You finished [report_chapters] chapters so far."
    return
### CONCENTRATION
label concentration_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">You maintain perfect concentration during your work.\n>And finish another chapter of the report.\n>You finished [report_chapters] chapters so far."
    return

    
### SPEEDWRITING
label speedwriting_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">You use your speedwriting skills.\n>And finish another chapter of the report.\n>You finished [report_chapters] chapters so far."
    return

### DR'S NEWSPAPER ooo ###

label nsp_articles_work:
    stop music fadeout 1.0
    if daytime:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else: 
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        stop bg_sounds 
    
    
    hide screen genie
    show screen paperwork
    with Dissolve(0.3)
    ">Вы пишете статьи для газеты."
    
    call nsp_finished_working_chapter #Chapter finished. $ report_chapters += 1
    
    call nsp_report_chapters_check #Checks whether or not the completed chapter was the final one.
        
    if daytime: # Makes sure that check happens only at nighttime. 
        pass
    else:
        if wather_generator >= 31 and wather_generator <= 40: # FULL MOON
            call nsp_f_moon_bonus
        if wather_generator >= 51 and wather_generator <= 60: # FULL MOON
            call nsp_f_moon_bonus
           
    call nsp_report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### CONCENTRATION CHECK ###========================================================================
    if concentration == 1:
        $ concentraton_check = renpy.random.randint(1, 6) #Copper book.
        if concentraton_check == 1:
            call nsp_concentration_label
    if concentration == 2:
        $ concentraton_check = renpy.random.randint(1, 4) #Bronze book.
        if concentraton_check == 1:
            call nsp_concentration_label
    if concentration == 3:
        $ concentraton_check = renpy.random.randint(1, 2) #Silver book.
        if concentraton_check == 1:
            call nsp_concentration_label
    if concentration == 4:                                                               #Golden book.
        call nsp_concentration_label
#    if concentration == 5:
#        $ concentraton_check = renpy.random.randint(1, 2) #Platinum book.
#        if concentraton_check == 1:
#            call nsp_concentration_label
#    if concentration == 6:
#            call nsp_concentration_label
    ###==============================================================================================
    
    call nsp_report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### SPEEDWRITING CHECK ###========================================================================
    if speedwriting == 1:
        $ speedwriting_check = renpy.random.randint(1, 6) #"\"Speedwriting for dummies.\"" # 1/10 chance
        if speedwriting_check == 1:
            call nsp_speedwriting_label
    if speedwriting == 2:
        $ speedwriting_check = renpy.random.randint(1, 4) #"\"Speedwriting for beginners.\"" # 1/8 chance of it to pop up.
        if speedwriting_check == 1:
            call nsp_speedwriting_label
    if speedwriting == 3:
        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for intermediate.\"" # 1/6 chance of it to pop up.
        if speedwriting_check == 1:
            call nsp_speedwriting_label
    if speedwriting == 4:
            call nsp_speedwriting_label
#    if speedwriting == 5:
#        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for experts.\"" # 1/2 chance of it to pop up.
#        if speedwriting_check == 1:
#            call nsp_speedwriting_label
#    if speedwriting == 6:
#        call nsp_speedwriting_label #""\"Speedwriting for maniacs.\"" # 1 (sure) chance of it to pop up.
    
    call nsp_report_chapters_check #Checks whether or not the completed chapter was the final one.
            

    show screen genie
    hide screen paperwork
    
    
    
    if daytime:
        jump night_start
    else: 
        jump day_start    
###

### 
label nsp_report_chapters_check:
    if nsp_newspaper_articles >= 8:
        ">Вы закончили статью."
        $ nsp_newspaper_articles = 0
        $ nsp_newspaper_ready = True
        if nsp_newspaper_menu == 1:
            $ nsp_newspaper_menu = 2
    return
### FULL MOON BONUS ###
label nsp_f_moon_bonus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ nsp_newspaper_articles += 1
    ">Полнолуние сделало вас более продуктивным.\n>Вы закончили [nsp_newspaper_articles]-ю статью."
    return
###
label nsp_finished_working_chapter:
    $ nsp_newspaper_articles += 1
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Вы закончили [nsp_newspaper_articles]-ю статью."
    return
### CONCENTRATION
label nsp_concentration_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ nsp_newspaper_articles += 1
    ">Во время работы вы идеально сконцентрированы.\n>И заканчиваете дополнительную статью.\n>Вы закончили [nsp_newspaper_articles]-ю статью."
    return
### SPEEDWRITING
label nsp_speedwriting_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ nsp_newspaper_articles += 1
    ">Вы используете свой навык скорописания.\n>И заканчиваете дополнительную статью.\n>Вы закончили [nsp_newspaper_articles]-ю статью."
    return
    
### READING GALADRIEL BOOKS IN PROPER ORDER ###
label gal_proper:
    m "Reading books out of order won't do me any good."
    hide screen gift
    return
    
    
    
### READING A BOOK BLOCK ### Sends here to make sure that proper SFX is played during reading a book.
label reading_block:
    stop music fadeout 2.0
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else:
        call fire_out #Shows Genie reading a book near the window.

    if daytime and not raining:
        #play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        play weather "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    
    if not daytime and not raining:
        play weather "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...


    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    return
