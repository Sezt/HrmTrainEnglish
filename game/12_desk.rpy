label menu_reading_book:
    $choose=None
    $RunMenu.event=None
    if choose==None:
        $ choose = RunMenu()
    else:
        $choose.Clear()
    python:
        for e in this.List:
            if e.GetValue("block")==_block and e._status>=0: # Нужно ставить GetValue("block")  а не _block - у ивента такого объекта может не быть
                choose.AddItem("- Book: "+e._caption+" - "+("{image=check_08.png}" if e.IsDone() else ""), 
                    "reading_book_done" if e.IsDone() else "menu_reading_book_2", True, e)
        choose.AddItem("- Never mind -", "books_list", True, event)

    $ choose.Show()

    label menu_reading_book_2:
        $ the_gift = event._img#"03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3

        "\"[event._caption]\"" "[event._description]"#" Вы хотите прочитать ее?"
        menu:
            "- Read book-":
# Проверяем, что освоены предыдущие ступени навыка:
                if event.GetValue("block")=="books_edu":
                    if event.prevInList.GetValue("block")!=event.GetValue("block") or event.prevInList.IsDone():
                        jump reading_book_xx
                    else:
                        m "This book is still too strong for me."
                        hide screen gift
                        jump books_list
                else:
                    if event.Name=="book_05_b" and not this.book_05.IsDone():
                        m "There are strange people who begin the book with the second part. But I'm not one of those."
                        jump expression _label
                    else:
                        jump reading_book_xx #"reading_book_01"
            "- Never mind -":
                hide screen gift
                jump expression _label #books_on_improvement

    label reading_book_done:
        $ the_gift = event._img#"03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3
        "\"[event._caption]\"" "[event._description]."


# Отдельная обработка для Вайфу - ее нужно читать несколько раз                                
        if event.Name=="book_07":
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
            if event._block=="books_edu" and event._conclusion!="":
                m "It gave me a new skill: [event._conclusion]"
            else:
                m "[event._conclusion]"

            if event.Name=="book_04":
                g4 "I have mastered the control over my spirit. Now I shall always complete an additional chapter when doing paperwork."
                g9 "My spirit is my bitch"

        hide screen gift
        jump expression _label

label desk:
    menu:
        "- inspect -" if not desk_examined:
            $ desk_examined = True
            m "ordinary table..."
            jump day_main_menu
        "- Do paperwork -" if finished_report < 6 and not got_paycheck and not day == 1 and work_unlock2:
            jump paperwork
        "{color=#858585}- Do paperwork -{/color}" if finished_report >= 6 and not got_paycheck:
            m "I have already completed six reports this week."
            jump desk
        "{color=#858585}- Do paperwork -{/color}" if got_paycheck: # When TRUE paycheck is in the mail.
            m "First, I need to get paid."
            jump desk
         
        "- Book Collection -" if not day == 1 and cataloug_found: 
            label books_list:
                $choose=None
                menu:
                    "- Educational books -":
                        label books_on_improvement:
                            $_label="books_on_improvement"
                            $_block="books_edu"
                            jump menu_reading_book

                    "- fiction books -":
                        label fiction_books:
                            $_label="fiction_books"
                            $_block="books_fict"
                            jump menu_reading_book

                    "- Never mind -":
                        jump desk

          
        
                    
                    
                    
        #"- The muggle oddities -" if have_catalogue: #Real thing
        "- Dahr's Magazin -" if cataloug_found: 
            if order_placed or package_is_here:
                show screen bld1
                with d3
                dahr "Please wait a little bit. Owl is on the way."
                hide screen bld1
                with d3
                jump desk
            else:
                 jump the_oddities
        
        
        

        # "- Подрочить на трусики Гермионы -" if request_03: #True when Hermione has no panties on.
        #     jump jerk_off
        "- jerk off -" if not day < 5:
            jump jerk_off 
        "- Hermione's status -" if this.Has("her_wants_buy"): #summoning_hermione_unlocked and buying_favors_from_hermione_unlocked: 
            "> Whoring: {color=#B40000}{size=+4}{b}[whoring]{/b}{/size}{/color}- degree."
            "> Mad: {color=#B40000}{size=+4}{b}[mad]{/b}{/size}{/color}- degree"
            if mad >=1 and mad < 3:
                "> Hermione still {b} a little upset {/ b} you ..."
            elif mad >=3 and mad < 10:
                "> You {b} upset {/ b} Hermione."
            elif mad >=10 and mad < 20:
                "> Hermione {b} very upset {/ b} you."
            elif mad >=20 and mad < 40:
                "> Hermione is angry {b} {/ b} for you."
            elif mad >=40 and mad < 50:
                "> Hermione {b} very angry {/ b} for you."
            elif mad >=50 and mad < 60:
                "> Hermione {b} in anger {/ b} for you."
            elif mad >=60:
                "> Hermione hates {b} {/ b} you."
            else:
                "> Hermione {b} is not angry {/ b} for you"
            jump desk
        "- Doze -" if daytime and not day == 1:
            jump night_start
        "- Sleep -" if not daytime and not day == 1:
            jump day_start
            

        "- Never mind -":
            call screen main_menu_01
            
            

        
  
            
            


    
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
        ">You are reading a book [event._caption], listening to the rain drumming on the roof of your tower."
    else:
        ">You are reading a book [event._caption]..."
   
    call chap_finished_xx
    
    call chapter_check_book_xx #Checks if the chapter just finished was the last one.
    
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl>0:
        $ speed_dummies = Rand([60,30,20][s_reading_lvl-1]//turbo)  # Массив содержит размер интервала для расчета вероятности. Первая книга 10/60 шансов прочитать доп. главу, вторая 10/30, 3-я 10/20 . В режиме турбо интервал уменьшается вдвое
        if speed_dummies <= 10: #Success.
            ">Using techniques learned your initial speed reading, you rationally use time and continue to read."
            call chap_finished_xx
            call chapter_check_book_xx #Checks if the chapter just finished was the last one.
#            ">There are still a few chapters."

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

    ">There are still a few chapters."       


    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start #pered_menu#
    else: 
        jump day_start
        
######    
label chap_finished_xx:
    if event.Name=="book_05":
        $event.IncValue("status", 1)  #+=1
        $renpy.say("Глава [event._status]", 
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
        ][event._status-1]
        )


    if event.Name=="book_05_b":
        $event.IncValue("status", 1)  #+=1
        $renpy.say("Глава [event._status]",
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
        ][event._status-1]
        )

    if event.Name=="book_06":
        $event.IncValue("status", 1)  #+=1
        $renpy.say("Глава [event._status]", 
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
        ][event._status-1]
        )

    if event.Name=="book_07":
        $ book_07_units +=1
        $event._status=book_07_units
        call waifu
        
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    if event._block=="books_edu": 
#        $event._status=this.GetCall(event.Name).SetValue("status", event._status+1)  #event.SetValue("status", event._status+1)  #+=1
        $event.IncValue("status", 1)    
    ">you finished \"chapter [event._status]\" this book."
    return
    
###
label chapter_check_book_xx: #Checks if the chapter just finished was the last one.
    if (event.IsDone() and event.Name!="book_07") or (event.Name=="book_07" and book_07_units == 20):#book_xx_units == 10:
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

        if event.Name=="book_06":
            g4 "What kind of garbage! I hate the person who wrote it!"
            m "However, all these rape led me to a couple of ideas..."


        if event.Name=="book_07":
            if complited_leena_already and complited_shea_already and complited_stevens_already and victoria >= 1 and shea >= 1 and leena >= 1: #Harem ending. The DAHR's ticket.
                m "Wow! Excellent book! It was pretty good!"
                
                #m "No, I mean it! What a great peace of fiction! That Akabur dude must be a genius!"
                if not found_dahrs_ticket_once:
                    m "Hmm ...?"
                    m "It is ...? Bookmark?"
                    $ the_gift = "03_hp/18_store/06.png" # The DAHR's ticket.
                    show screen gift
                    with d3
                    $ renpy.play('sounds/win2.mp3') #Sound of finding an item.
                    ">You've found a Dahr's voucher."
                    hide screen gift
                    with d3
                    m "Hm..."
                    $ vouchers += 1 #Shows the amount of DAHR's vouchers in your possession.
                    $ found_dahrs_ticket_once = True # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.
                    $ waifu_book_completed = True
            elif shea_waifu and shea >= 8: 
                if not complited_shea_already: #Finished with Shea for the first time.
                    m "Not Bad. I'm really ready to take care of Shea ..."
                    g9 "Well, about her and her anal virginity..."
                    $ complited_shea_already = True
                else: #Finished with Shea for the second time.
                    m "then at the end I'm back with Shea?"
                    m "Hmm ... Maybe I should try and choose other options next time ...?"
            elif victoria_waifu and victoria >= 7:
                if not complited_stevens_already: #Finished with Ms.Stevens for the first time.
                    m "Not bad, not bad. Mrs. Stevens was one more whore ..."
                    $ complited_stevens_already = True
                else: #Finished with Shea for the second time.
                    m "So in the end I am again with Mrs. Stevens?"
                    m "Hmm ... Maybe I should try and choose other options next time ...?"
            elif leena_waifu and leena >= 8:
                if not complited_leena_already: #Finished with Leena for the first time.
                    g9 "Great! I love happy endings!"
                    $ complited_leena_already = True
                else: #Finished with Shea for the second time.
                    m "So, in the end I am again with  girl?"
                    m "Hmm ... Maybe I should try and choose other options next time ...?"

            else:
                m "Hmm ... The end is very disappointed ..."
                m "Maybe I should read it again someday..."
            
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
        if event._conclusion!="":
            if event._block=="books_edu":
                m "new skill: [event._conclusion]"
            else:
                m "[event._conclusion]"

# Изменения навыка по завершению книги (кроме Вайфу - book_07 в ней навык меняется отдельно)
# Можно было сделать через событие, но тогда получится более громоздко. Так что пока так:
        if event.Name in ["book_01", "book_02", "book_03", "book_04"]:
            $ concentration += 1
        if event.Name in ["book_05", "book_05_b", "book_06"]:     
            $ imagination +=1
        if event.Name in ["book_08", "book_09", "book_10"]:
            $ s_reading_lvl +=1
        if event.Name in ["book_12", "book_13", "book_14", "book_15"]:
            $ speedwriting += 1

        
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
    ">You make a paperwork."
    
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
        ">You have completed a paperwork."
        $ report_chapters = 0
        $ finished_report += 1
    return
### FULL MOON BONUS ###
label f_moon_bonus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">The full moon will make you more productive.\n>you finished [report_chapters] chapter."
    return
###
label finished_working_chapter:
    $ report_chapters += 1
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">you finished [report_chapters] chapter."
    return
### CONCENTRATION
label concentration_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">During the work you perfectly centered.\n>And ends with an additional chapter.\n>you finished [report_chapters] chapter."
    return
### SPEEDWRITING
label speedwriting_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">You use your skill speedwriting.\n>And ends with an additional chapter.\n>you finished [report_chapters] chapter."
    return
    
    
### READING GALADRIEL BOOKS IN PROPER ORDER ###
label gal_proper:
    m "Reading books does not give me anything."
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
