label mail:

    $ this.RunStep("MAIL")    
    if got_paycheck == True and finished_report >= 1 and letter_from_ficbook_fun == False:
        $ letters -= 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        $ got_paycheck = False #When TRUE the paycheck is in the mail. Can't do paper work.
        hide screen owl
        show screen owl_02
        ">You read your mail."
        play sound "sounds/money.mp3"  #Quiet...

        $dgold=([40, 70, 90, 110, 150, 200][finished_report-1])*turbo
        $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing two reports this week.\nHere is your payment:{/size} \n{size=+4}[dgold] galleons.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"    
        $ gold += dgold

        
        show screen bld1
        show screen letter
        show screen ctc
        pause
        hide screen letter
        hide screen bld1
        hide screen ctc
            

        $ finished_report = 0

        if (hermi._incomePercent>0):
            $dgold=dgold*hermi._incomePercent//100
            $gold-=dgold
            "> Согласно вашему соглашению с Гермионой [dgold] галеонов ([hermi._incomePercent]%%) перечисляются на ее счет"
        call screen main_menu_01
        
    ###"УЛУЧШЕННЫЕ" ОТЧЕТЫ###
    if got_paycheck == True and finished_report >= 1 and letter_from_ficbook_fun == True:
        $ one_of_ten = renpy.random.randint(1, 6)
        $ letters -= 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        $ got_paycheck = False #When TRUE the paycheck is in the mail. Can't do paper work.
        hide screen owl
        show screen owl_02
        ">Вы читаете свои сообщения."
        
        
        
        $dgold=([80, 140, 180, 220, 300, 400][finished_report-1])*turbo
        
        if one_of_ten == 1:
            play sound "sounds/money.mp3"  #Quiet...
            $ letter_text = "{size=-7}ОТ:Министерства Магии\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-2}Благодарим Вас за отчеты, присланные на этой неделе.\n Ваша оплата:{/size} \n{size=+4}[dgold] галеонов.{/size}\n\n\n{size=-3}-С уважением-{/size}"
            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc
        
        if one_of_ten == 2:
            play sound "sounds/money.mp3"  #Quiet...
            $ letter_text = "{size=-7}ОТ:Джоданны Кроулинг\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-4}Дорогой Альбус,\nмы всем офисом благодарим Вас за новую главу! Позвольте передать вам {size=-2}[dgold] галеонов.{/size} и наше искреннее восхищение.{/size}\n\n\n{size=-6}-С уважением-{/size}"
            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc
            
        if one_of_ten == 3:
            play sound "sounds/money.mp3"  #Quiet...
            $ letter_text = "{size=-7}ОТ:Джоданны Кроулинг\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-4}Дорогой Альбус,\nна правах человека, ведущего связь с Вами, могу ли я узнать, будут ли Педреро и Хуанито вместе? Отправляю вам {size=-2}[dgold]галеонов{/size} и скромную надежду на ответ.{/size}\n\n\n{size=-6}-С уважением-{/size}"
            show screen bld1
            show screen letter
            show screen ctc
            g9 "Хороший писатель никогда не раскрывает сюжетных поворотов!"
            m "..."
            m "Я и вправду сказал это?"
            hide screen letter
            hide screen bld1
            hide screen ctc
            
        if one_of_ten == 4:
            $ letter_text = "{size=-7}ОТ:Джоданны Кроулинг\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-3}Дорогой Альбус,\nновые главы вышли великолепными, особенно когда...{/size}"
            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc
            g1 "..."
            g1 "..."
            g1 "Fuck, no."
            m "Я ничего не хочу об этом знать."
            play sound "sounds/money.mp3"  #Quiet...
            g9 "Ну, по крайней мере, в конверте лежали мои [dgold]галеонов."
            
        if one_of_ten == 5:
            $ letter_text = "{size=-7}ОТ:Джоданны Кроулинг\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-4}Дорогой Альбус,\nна правах главы Вашего фан-клуба, позвольте пригласить Вас на пенную вечеренку, адрес и время написаны на приглашении. Мы ждем вас с нетерпением!{/size}"
            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc
            g9 "Вечеринка, полная фанаток-извращенок? Впишите меня!"
            m "Ах, ну да... \"Будь хорошим джином, Джинни и сиди взаперти весь день, как осел.\""
            m "Черт."
            play sound "sounds/money.mp3"  #Quiet...
            g4 "Зачем мне [dgold]галеонов, если я не могу их как следует потратить?!"
            
        if one_of_ten == 6:
            $ letter_text = "{size=-7}ОТ:XXX\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-2}У МЕНЯ БРАТ УМЕР ИЗ-ЗА ТАКИХ ИСТОРИЙ, ГОРИ В АДУ, ГРЯЗНЫЙ ИЗВРАЩЕНЕЦ!!!{/size}"
            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc
            m "..."
            g9 "О, монетки!"
            play sound "sounds/money.mp3"  #Quiet...
            "> Получено [dgold] галеонов"
            m "..."
            m "Смертные."
                
    #Слишком большое письмо      
    #   if one_of_ten == 7:
    #       $ letter_text = "{size=-7}ОТ:Джоданны Кроулинг\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-4}Дорогой Альбус,\nсегодня мне приснился странный сон. Я была обычным маглом, писателем. И писала истории о мальчике-котором-выжил. И когда издатель запретил мне убить Поттера в последнем бою, я проснулась в холодном поту. Странный сон, правда?{/size}"
            
    #    if one_of_ten == 8:
    #        $ letter_text =
            
    #    if one_of_ten == 9:
    #        $ letter_text =
            
    #    if one_of_ten == 10:
    #        $ letter_text =
            
        
        $ gold += dgold
            

        $ finished_report = 0

        if (hermi._incomePercent>0):
            $dgold=dgold*hermi._incomePercent//100
            $gold-=dgold
            "> Согласно вашему соглашению с Гермионой [dgold] галеонов ([hermi._incomePercent]%%) перечисляются на ее счет"
        call screen main_menu_01
    
    
### MAIL FROM HERMIONE ###
if day == 1:
    #$ letter_text = "{size=-4}-To professor Dumbledore-\n\nI am writing you to bring the current situation in our school to your attention.\n I'm afraid I'll need your help to sort this out.\n\n\n-Sincerely yours Hermione Granger-{/size}"
    $ letter_text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sure that you remember the reason why I'm writing you this letter from my last one, sir.\n\nI beg of you, please hear my plea this time. This injustice simply cannot go on...\n\nNot in this day and age, not in our school.\n\nPlease take action.\n\n{size=-3}With deepest respect,\nHermione Granger{/size}"    
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
    #$ letter_text = "{size=-4}-To professor Dumbledore-\n\nI am writing you to bring the current situation in our school to your attention.\n I'm afraid I'll need your help to sort this out.\n\n\n-Sincerely yours Hermione Granger--{/size}"
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
    m "Оплата? Хм..."
    show screen blktone8
    with d3
    $ renpy.play('sounds/win2.mp3')   #Not loud.
    ">Теперь вы можете писать отчеты в Министерство магии, чтобы заработать золото..."
    hide screen blktone8
    with d3
    call screen main_menu_01
    
###Mail about improved "reports"###
if total_report >= 10 and letter_from_ficbook_fun == False:
    $ letters -= 1
    $ letter_from_ficbook_fun = True
    hide screen owl
    show screen owl_02
    $ letter_text = "{size=-7}От: Жодана Кроулинг\nКому: Профессору Альбусу Дамблдору\n\n{/size}{size=-4}Дорогой Альбус Дамблдор.\nВ связи с открывшимся в Вас новым даром, Комитет Образования решил удвоить финансирование вашей отчетности.\nЖдем от вас больше захватывающих отчетов, в особенности про потомственного волшебника Педреро.\n\n{size=-3}С уважением,\nваша преданная фанатка и секретарь Комитета Образования,\nЖодана Кроулинг.{/size}"
    label letter_funletter:
    show screen bld1
    show screen letter
    show screen ctc
    with Dissolve(.3)
    pause
    menu:
        "- Закончить чтение -":
            pass    
        "- Продолжить чтение -":
            jump letter_work
    hide screen letter
    hide screen bld1
    hide screen ctc
    with Dissolve(.3)
    m "..."
    m "Это определенно самый странный мир из увиденных мною."
    show screen blktone8
    with d3
    $ renpy.play('sounds/win2.mp3')   #Not loud.
    ">Теперь вы получаете в два раза больше денег за... \nОтчеты."
    ">Оно того стоит?"
    m "Деньги не пахнут."
    hide screen blktone8
    with d3
    call screen main_menu_01
    
### DR'S NEWSPAPER ooo ###

if day > 20 and nsp_pre_jobs_max >= 4 and nsp_pre_letter == 1:
    jump newsp_pre_letter

if nsp_newspaper_published_mail == True:
    jump newsp_letter
    
if nsp_letter_1 == 1:
    jump nsp_text_letter_1
    
if nsp_letter_2 == 1:
    jump nsp_text_letter_2
    
if nsp_letter_3 == 1:
    jump nsp_text_letter_3
    
if nsp_letter_4 == 1:
    jump nsp_text_letter_4
    
if nsp_letter_5 == 1:
    jump nsp_text_letter_5
    
if nsp_letter_6 == 1:
    jump nsp_text_letter_6
    
if nsp_letter_7 == 1:
    jump nsp_text_letter_7
    
if nsp_letter_8 == 1:
    jump nsp_text_letter_8
   
if nsp_letter_9 == 1:
    jump nsp_text_letter_9
    
if nsp_letter_10 == 1:
    jump nsp_text_letter_10
    
if nsp_letter_11 == 1:
    jump nsp_text_letter_11
    
if nsp_letter_12 == 1:
    jump nsp_text_letter_12
    
if nsp_letter_13 == 1:
    jump nsp_text_letter_13

###    
    
label mail_02: #Packages only. <=====================================================================### PACKAGES ###=================================================== 

    $evn=None
    python:
        for e in this.List:
            if "book_" in e.Name and e._status==-1:
                e.SetValue("status", 0)
                evn=e 

    if evn!=None:
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.

        $screens.ShowD3("gift", par1=evn._img).Say(">Book [evn._caption] has been added to your collection.").HideD3("gift")

#        $ the_gift = evn._img #"03_hp/18_store/08.png" # Copper book of spirit.
#        show screen gift
#        with d3
#        ">Книга [evn._caption] была добавлена в Вашу коллекцию."
#        hide screen gift
#        with d3
        call screen main_menu_01  


    
    
    
    
    
### ITEMS ###  
    if itsOWL.Any():
        $item=itsOWL()[0]
        $_count=itsOWL.Count(item.Name)
        $hero.Items.AddItem(item.Name, _count)  
        $itsOWL.Clear()
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.

        $screens.ShowD3("gift", par1=item._img).Say(">Added to your things: [item._caption], [_count] . ").HideD3("gift")

#        $ the_gift = item._img 
#        show screen gift
#        with d3
#        ">Добавлено к вашим вещам: [item._caption], [_count] шт. "
#        hide screen gift
#        with d3
        call screen main_menu_01


$letters=0 # иначе если человек накопит кучу непрочитанных писем, то пападем по следующей метке с пустым параметром и будет критическая ошибка

label bigletter(__pages): #Письмо родителей Дафны Дамблдору
    $screens.Hide("owl").Show("owl_02")
    $ letters -= 1

    $__pageIndex=0
    label letterbig_newpage:
    $screens.Show("letterbig", par1=__pages[__pageIndex])
    $screens.Show("ctc", d3, "bld1").Pause()

    menu:
        "<<< Return " if __pageIndex>0:
            $__pageIndex-=1                
            jump letterbig_newpage
        " Continue >>>" if __pageIndex<len(__pages)-1:
            $__pageIndex+=1
            jump letterbig_newpage
        "- Complete -":
            pass    
    $screens.Hide("letterbig", "ctc", d3, "bld1")
    return

label bigtext(__pages): #То же, что и bigletter , но не вычетает единичку из писем
    $screens.Hide("owl").Show("owl_02")

    $__pageIndex=0
    label letterbig_newpage:
    $screens.Show("letterbig", par1=__pages[__pageIndex])
    $screens.Show("ctc", d3, "bld1").Pause()

    menu:
        "<<< Вернуться " if __pageIndex>0:
            $__pageIndex-=1                
            jump letterbig_newpage
        " Продолжить >>>" if __pageIndex<len(__pages)-1:
            $__pageIndex+=1
            jump letterbig_newpage
        "- Завершить -":
            pass    
    $screens.Hide("letterbig", "ctc", d3, "bld1")
    return



label daphne_pre_04: #Письмо родителей Дафны Дамблдору
    call bigletter(["{size=-7}From: Olivia Greengrass\nTo: Professor Dumbledore\n\n{/size}"
    "{size=-4}Professor Dumbledore!\n\nMy husband and I are seriously concerned that our daughter is not getting enough attention at Hogwarts. Especially considering her linage. \n\n "
    "Professor Severus Snape has informed us that you finally realized this and offered to give her private lessons.\n\n You took a long time to take this step, Professor!\n\n "
    "We hope your belated action will have enough of an effect...{/size}\n\n ",
    "{size=-4}...As you know, in the Ministry the next scheduled meeting regarding the allocation of funds for magic schools.\n\n "
    "Just to let you know that if you do not make sufficient progress, Daphne will be transferred to Durmstrang Academy - where they know how to appreciate a true pureblood mage.\n\n "
    "Should this happen we will make every effort for Hogwarts to receive minimum funding.{/size}\n\n "
    "{size=-3}Without much hope for your success,\nOlivia Greengrass.{/size}"])

    $hero(g4, "Great Sands!..",
        m,"Snape is sending letters on my behalf and I'm not sure that I like it.//"
        "Sufficient progress?! Pretty sure we don't expect the same results, a good fuck and not good grades!//"
        "She had more then enough time to snitch to her parents and didn't do it...thats lucky at least//"
        "How am I going to teach her, if I don't have any school knowledge?! And most importantly: how do I keep her mouth shut?")

    $wtevent.Finalize()

    call screen main_menu_01


label daphne_pre_06: #Выписка из личного дела Дафны, присланная Снейпом
    $music("Daphne Privacy")

    call bigletter(["{size=-7}From: Severus Snape\nTo: Professor Dumbledore\n\n{/size}"
    "{size=+2}Extract from the Daphne Greengrass file\n\n{/size}"
    "{size=-4}Height: 5' 8\", Weight: 53 kg breast Size: 34B\n\n"
    "Orientation: Presumably heterosexual.\n\n"
    "A virgin: No evidence to the contrary.\n\n"
    "Fingering: Yes? (Indirect evidence: classmate, who happened to be nearby, heard her moans in the lockerroom showers)\n\n"
    "Watching porn: Yes? (Indirect evidence: a porn magazine disappeared from the Slytherin living room, only Greengrass' room wasn't checked)\n\n"
    "Voyeurism: Yes? (Indirect evidence: she was caught near a peephole into the men's shower room, but was not peeping at the time){/size}",
    "{size=-4}Beliefs and fears:\n\n" 
    "* Has an inferiority complex that her breasts are too small\n"
    "* Believes that she will only sleep with a pureblood wizard, tall, masculine, etc.\n"
    "* Afraid she will not be able to satisfy a tall masculine pureblood wizard.\n"
    "* Insecure about her minor (nonexistant?) sexual experience\n\n"
    "Perversions: None found{/size}\n\n "
    "{size=-3}Success, my friend!\nSeverus Snape.{/size}\n\n"
    "{size=-4}P. S. Miss Greengrass received a farewell letter from her parents. I think it would be best, my friend, if you don't provoke her, and she will come to you for the first lesson.{/size}"])

    $hero(m,"Pretty good info. Using words like \"evidence\"...Is he going to write a crimenovel? //"
        "No wonder he is tired all the time...// Hmm, how should I prepare for her arrival?")

    call music_block
    $wtevent.Finalize()

    call screen main_menu_01



