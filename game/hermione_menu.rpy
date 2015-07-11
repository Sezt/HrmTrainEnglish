#play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
#stop music fadeout 2.0
label hermione_approaching:     
         
    $ menu_x = 0.2 #Menu is moved to the left side.
    $ pos = POS_410
                
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    with d3

    python:
        for t in [
            (0, "body_01.png", her, "Yes, professor?"),
            (-2, "body_03.png", "", ">Looks like Hermione is still a little upset with you..."),
            (-9, "body_03.png", "", ">Hermione is upset with you."),
            (-19, "body_09.png", "", ">Hermione is very upset with you."),
            (-39, "body_05.png", "", ">Hermione is mad at you."),
            (-49, "body_47.png", "", ">Hermione is very mad at you."),
            (-59, "body_47.png", "", ">Hermione is furious at you."),
            (-100, "body_47.png", "", ">Hermione hates your guts.")
            ]:
            (_val, _img, _char, _text)=t
            if hermi.liking>=_val:
                herView.showQQ( _img, pos )
                renpy.say(_char, _text)
                break


    $ this.RunStep("HERMIENTER")      


    label hermione_main_menu:
    $ pos = POS_410
    menu:
### DR'S NEWSPAPER ooo ###

        "- Тренировка с Хрустальным шаром -" if nsp_newspaper_menu >= 15 and nsp_genie_sphere_sapphire_level >= 1 :
            jump nsp_hermione_train

        "- Поговорить о работе для редакции -" if nsp_newspaper_menu == 4 or nsp_newspaper_menu == 5 :
            jump nsp_hermione_pre1

        "{color=#858585}- Дать журналистское задание -{/color}" if nsp_newspaper_menu >= 6 and not daytime :
            ">Журналистские задания недоступны в это время суток."
            jump hermione_main_menu
             
        "- Дать журналистское задание -" if nsp_newspaper_menu >= 6 and daytime :
            if hermi.liking>=0:
                jump nsp_newsp_themes
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
                    if hermi.liking>=_val:
                        renpy.say(her, _text)
                        break
            jump hermione_main_menu
            
        "- Впечатления от газеты -" if nsp_newspaper_menu >= 6 :
            if hermi.liking >= -7:
                jump nsp_hermione_dialog_status
            else:
                her "Мне нечего сказать вам..."    
                jump hermione_main_menu            

###
        "- Поговорить -" if not chitchated_with_her:
            $ chitchated_with_her = True #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
            if hermi.liking >= -7:
                jump hermione_chat
            else:
                her "I have nothing to say to you sir..."    
                jump hermione_main_menu

        "-Tutoring-" if not daytime and not tut_happened and hermi.whoring <= 12:
            if hermi.liking>=0:
                jump tutoring
            python:
                for t in [
                (-2, "I'm sorry, maybe tomorrow..."),
                (-19, "I am not in the mood today..."),
                (-100, "After what you did, professor?\nI don't think so...")
                ]:
                    (_val, _text)=t
                    if hermi.liking>=_val:
                        renpy.say(her, _text)
                        break
            jump hermione_main_menu

        "-Buy \"sexual\" favours-" if this.Has("her_wants_buy"):#buying_favors_from_hermione_unlocked:
                if hermi.liking>=0:
                    jump new_personal_request
                python:
                    for t in [
                    (-2, "I'm sorry, professor, Maybe some other time..."),
                    (-9, "I don't feel like it today...\nMaybe in a couple of days..."),
                    (-19, "No thank you...."),
                    (-29, "After what you did, professor?\nI don't think so..."),
                    (-39, "You can't be serious!"),
                    (-100, "Is this some twisted joke to you, sir?!\nAfter what you did I don't feel like doing this ever again!")
                    ]:
                        (_val, _text)=t
                        if hermi.liking>=_val:
                            renpy.say(her, _text)
                            break
                jump hermione_main_menu
       
        
        
        "-Give her a present-" if not gifted:
            $ choose = RunMenu()
            python:
                for o in hero.Items():
                    if not o.Name in {"wine", "scroll"}:
                        choose.AddItem("- "+o._caption+" -", "menu_gifts_actions" , o.Name)

            $ choose.Show("hermione_main_menu")


                    
        
     
        "- Гардероб -" if dress_code and this.Has("her_wants_buy"):
            if hermi.liking>=0:
            
                jump wrd_menu

                    "-Put the long skirt on-" if herView.data().checkItemKeyStyle( G_N_SKIRT, 'short' ) and hermi.Items.Any("miniskirt"): #legs_02 and gave_miniskirt: #Turns True when Hermione has the miniskirt.
                        jump mini_off #28_gifts.rpy
                

                    "-Never mind-":
                        jump hermione_main_menu
            else:
                python:
                    for t in [
                    (-2, "I'm sorry, professor. Maybe some other time..."),
                    (-9, "What's wrong with my current attire?"),
                    (-19, "No, thank you...."),
                    (-29, "I don't think so..."),
                    (-39, "No!"),
                    (-100, "I will never let you tell me what to wear again, sir!")
                    ]:
                        (_val, _text)=t
                        if hermi.liking>=_val:
                            renpy.say(her, _text)
                            break
                jump hermione_main_menu
       
        
        "-Dismiss her-":
#                        if daytime:
#                            play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
#                        else:
#                            play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
            $ menu_x = 0.5 #Menu position is back to default. (Center).
            if daytime:
                if hermi.liking>=-2:
                    her "Oh, alright. I will go to classes then."
                elif hermi.liking >= -6:
                    her "..............................."
                else: 
                    her "*Humph!*..."
            else:
                if hermi.liking>=-2:
                    her "Oh, alright. I will go to bed then."
                elif hermi.liking >= -6:
                    her "..............................."
                else: 
                    her "Tsk!..."

            label hermione_goout:
            hide screen bld1
            $herView.hideQ() 
            hide screen blktone 
            hide screen hermione_02
            hide screen ctc
            with d3

            if daytime:
                $ hermione_takes_classes = True
                jump day_main_menu
            else:
                $ hermione_sleeping = True
                jump night_main_menu

label hermione_chat:
    if not teacher_jinn_quest in {3,4}:
        jump chit_chat_hermione
    menu:
        "Ask about textbooks" if teacher_jinn_quest == 3:
            jump hermione_bookbuying
            
        "To buy textbooks" if teacher_jinn_quest == 4:
            jump hermione_bookbuying
            
        "Chit-chat":
            jump chit_chat_hermione             

        
### CHITCHAT WITH HERMIONE ###
label chit_chat_hermione:
    $ this.RunStep("HERMICHAT")
    $ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
    $ pos = POS_410
    
    if hermi.whoring >= 0 and hermi.whoring <= 2: # WHORING LEVEL 01.
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Maybe if I worked harder, I could squeeze a few more classes into my schedule..."
            $herView.hideshowQQ( "body_03.png", pos )
        
        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Actually I don't mind it to be called a \"know-it-all\"."
            her "I think it's rather flattering..."
            $herView.hideshowQQ( "body_03.png", pos )
        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_04.png", pos )
            her "The basilisk, also known as the king of serpents."
            her "Herpo the Foul was the first to breed a Basilisk."
            her "He accomplished that by--"
            $herView.hideshowQQ( "body_10.png", pos )
            her "Oh, I'm sorry, professor, we have another test tomorrow..."
            her "I Just want to make sure that I'm ready..."
            $herView.hideshowQQ( "body_01.png", pos )
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_10.png", pos )
            her "If my body wouldn't require sleep..."
            $herView.hideshowQQ( "body_18.png", pos )
            her "I would be able to spend twice as much time studying!?"
            $herView.hideshowQQ( "body_14.png", pos )
            her "I wonder if there's a spell for that..."
            $herView.hideshowQQ( "body_03.png", pos )
        
        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_04.png", pos )
            her "So far professor Trelawney hasn't taught me a single piece of any actual knowledge, sir."
            $herView.hideshowQQ( "body_03.png", pos )
       
        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_04.png", pos )
            her "If only more students were honest, responsible and diligent like me."
            $herView.hideshowQQ( "body_03.png", pos )
      
        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_04.png", pos )
            her "How can some people be so ignorant to the world's problems?"
            her "Personally, I think that every single one of us should work harder to make our world a better place."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_10.png", pos )
            her "It's been raining quite a lot lately..."
            $herView.hideshowQQ( "body_01.png", pos )
    
        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Very few people know this..."  
            $herView.hideshowQQ( "body_06.png", pos )
            her "...But I really like chocolate."
            $herView.hideshowQQ( "body_01.png", pos )
       
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_06.png", pos )
            her "I am sorry sir, but I don't really have time for idle chit chat..."
            $herView.hideshowQQ( "body_03.png", pos )


    if hermi.whoring >= 3 and hermi.whoring <= 5: # WHORING LEVEL 02
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_04.png", pos )
            her "I read somewhere that a full moon often makes it easier to concentrate at a task at hand..."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_06.png", pos )
            her "I love nothing more than to curl up by a fireplace during a rainstorm with a good book..."
            $herView.hideshowQQ( "body_01.png", pos )
            
        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_10.png", pos )
            her "A peculiar rumour concerning professor Snape has been circulating in the school lately..."
            $herView.hideshowQQ( "body_15.png", pos )
            her "Well its probably shouldn't..."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Despite the questionable nature of the favours you have been buying from me lately, sir..."
            her "I am grateful to you for your help..."
            $herView.hideshowQQ( "body_09.png", pos )
            her "Gryffindor needs those points now more than ever..."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Why Quidditch is so popular among the girls is simply beyond me..."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_04.png", pos )
            her "The \"Men's Rights Movement\" is steadily gaining popularity."
            her "It's very fulfilling to know that we are helping to improve our society."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_04.png", pos )
            her "The Hogwarts school library is considered to be quite extensive..."
            $herView.hideshowQQ( "body_08.png", pos )
            her "Still, I can't help but wish that it'd be bigger..."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_10.png", pos )
            her "As one of the top students in this school I have a reputation to keep..."
            her "People look up to me..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "...So, your discretion is very appreciated, sir."
            $herView.hideshowQQ( "body_29.png", pos )
            
        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_11.png", pos )
            her "That favour I sold you the other say, sir..."
            $herView.hideshowQQ( "body_33.png", pos )
            her "......."
            $herView.hideshowQQ( "body_87.png", pos )
            her "I only agreed to it because the needs of my house always come first."
            $herView.hideshowQQ( "body_120.png", pos )
            her "I just wanted you to know that, sir..."
            
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_04.png", pos )
            her "The \"Autumn Ball\" is still several months away..."
            $herView.hideshowQQ( "body_11.png", pos )
            her "But some girls are already discussing what kind of dress they are going to wear..."
            $herView.hideshowQQ( "body_185.png", pos )

  
    if hermi.whoring >= 6 and hermi.whoring <= 8: # WHORING LEVEL 03.
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Do you remember when you asked me to show you my panties for the first time sir?"
            her "I was so furious with you then..."
            $herView.hideshowQQ( "body_09.png", pos )
            her "Now I see that I was just being selfish..."
            her "After all, the honour of my house is at stake here..."
            $herView.hideshowQQ( "body_07.png", pos )
            her "And that shall be my one and only concern!"
            
        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_04.png", pos )
            her "The rate at which  Slytherin house has been gaining points lately is simply ridiculous."
            $herView.hideshowQQ( "body_05.png", pos )
            her "I think professor Snape might be behind it."
            $herView.hideshowQQ( "body_04.png", pos )
            her "You should look into this, sir."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Ashwinder eggs, rose thorns, moonstone..."
            $herView.hideshowQQ( "body_11.png", pos )
            her "Huh? Am I thinking out loud again?"
            $herView.hideshowQQ( "body_24.png", pos )
            her "I apologize..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "It's just that I have another Potions test soon..."

        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_77.png", pos )
            her "I dislike the entire house of Slytherin with all my heart, sir."
            
        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_16.png", pos )
            her "Hogwarts has really become a second home to me lately..."
            $herView.hideshowQQ( "body_71.png", pos )
            her "I don't even miss my parents nearly as much anymore..."
            $herView.hideshowQQ( "body_18.png", pos )
            her "Come to think of it I don't miss them at all..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "I'm an awful daughter..."

        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_70.png", pos )
            her "*Yawn!* I read about this technique that supposedly allows you to cut your sleep time in half..."
            $herView.hideshowQQ( "body_73.png", pos )
            her "It don't think it's working though.... *Yawn!*"

        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Even after I graduate from Hogwarts I plan to keep on working hard."
            $herView.hideshowQQ( "body_02.png", pos )
            her "If I give it my all I can make this world a better place, I know it!"
            $herView.hideshowQQ( "body_03.png", pos )
           
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_11.png", pos )
            her "Somehow I have the feeling that this year will become a pivotal turning point in my life..."
            $herView.hideshowQQ( "body_13.png", pos )
  
        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Some of the less travelled school corridors are not very well lit and rather dusty..."
            her "Please take care of this, sir..."
            $herView.hideshowQQ( "body_03.png", pos )
       
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_14.png", pos )
            her "I've read about this thing called a \"Time-Turner\"."
            her "It allows the user to control the flow of time..."
            $herView.hideshowQQ( "body_16.png", pos )
            her "Having a device like that would do wonders for my schedule..."
            $herView.hideshowQQ( "body_17.png", pos )
        

    if hermi.whoring >= 9 and hermi.whoring <= 11: # WHORING LEVEL 04.
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_11.png", pos )
            her "My \"men's rights movement\" has been losing its popularity lately..."
            $herView.hideshowQQ( "body_12.png", pos )
            her "It's as if people don't even care!"

        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Thank you for buying all those favours from me, sir."
            $herView.hideshowQQ( "body_07.png", pos )
            her "Some of them were borderline inappropriate, sure..."
            $herView.hideshowQQ( "body_04.png", pos )
            her "But I don't mind sacrificing my dignity if it will allow Gryffindor to compete with Slytherin on equal ground."
            $herView.hideshowQQ( "body_03.png", pos )

        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_77.png", pos )
            her "Quidditch is stupid!"
            $herView.hideshowQQ( "body_17.png", pos )
            her "There. I said it."
            
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_02.png", pos )
            her "Sir, there is something about professor Snape that I think you should know..."
            $herView.hideshowQQ( "body_10.png", pos )
            her "................."
            $herView.hideshowQQ( "body_09.png", pos )
            her "........................."
            $herView.hideshowQQ( "body_04.png", pos )
            her "uhm... Never mind..."
            $herView.hideshowQQ( "body_03.png", pos )
 
        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Some of the Slytherin girls sell sexual favours almost openly these days..."
            $herView.hideshowQQ( "body_02.png", pos )
            her "You need to put an end to such practices, sir."
            $herView.hideshowQQ( "body_69.png", pos )
            her "(I can barely keep up...)"

        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Life works in mysterious ways..."
            $herView.hideshowQQ( "body_08.png", pos )
            her "Wouldn't you agree, sir?"
            $herView.hideshowQQ( "body_13.png", pos )

        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_76.png", pos )
            her "Slytherins..."
            $herView.hideshowQQ( "body_77.png", pos )
            
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_10.png", pos )
            her "I've been spending so much time in your office lately, sir..."
            $herView.hideshowQQ( "body_11.png", pos )
            her "If I'm not careful some people may think that I have become your pet..."
            $herView.hideshowQQ( "body_34.png", pos )
            her "I meant to say the teacher's pet..."
            $herView.hideshowQQ( "body_33.png", pos )

        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_02.png", pos )
            her "My favourite colours?"
            $herView.hideshowQQ( "body_02.png", pos )
            her "scarlet and gold of course!"
            $herView.hideshowQQ( "body_03.png", pos )
       
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Is it weird that my best friends are boys?"
            $herView.hideshowQQ( "body_01.png", pos )
        

        
    if hermi.whoring >= 12 and hermi.whoring <= 14: # WHORING LEVEL 05.
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_07.png", pos )
            her "Sir, with all due respect..."
            her "Professor Snape's debauchery is getting out of hand!"
            $herView.hideshowQQ( "body_11.png", pos )
            her "You must do something, sir."
            $herView.hideshowQQ( "body_03.png", pos )

        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_04.png", pos )
            her "I am willing to go to great lengths to insure the superiority of my house..."
            her "But that does not mean that I take pleasure in selling myself out to you in exchange for house points, sir."
            $herView.hideshowQQ( "body_118.png", pos )
            her "{size=-4}(Like some sort of prostitute-witch...){/size}"

        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_79.png", pos )
            her "What will it be today, sir?"
            
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_11.png", pos )
            her "lately I have not been studying nearly as much as I used to..."
            $herView.hideshowQQ( "body_10.png", pos )
            her "Am I losing my motivation?"
            $herView.hideshowQQ( "body_13.png", pos )
            
        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_08.png", pos )
            her "My least favourite subject?"
            $herView.hideshowQQ( "body_09.png", pos )
            her "Divination." 
            
        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_14.png", pos )
            her "My father used to say: \"Magic is just science we don't understand yet\"."
            $herView.hideshowQQ( "body_10.png", pos )
            her "He could't be more wrong of course..."
            $herView.hideshowQQ( "body_13.png", pos )
            
        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Despite everything..."
            $herView.hideshowQQ( "body_10.png", pos )
            her "I am thankful that you keep on buying favours from me, sir..."
            $herView.hideshowQQ( "body_13.png", pos )
            
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_14.png", pos )
            her "It's quite cold outside today, isn't it?"
            $herView.hideshowQQ( "body_15.png", pos )
            
        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_14.png", pos )
            her "The \"Autumn Ball\" will be soon..."
            $herView.hideshowQQ( "body_15.png", pos )
            
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_10.png", pos )
            her "People hardly show up for my \"men's rights movement\" meetings at all anymore..."
            $herView.hideshowQQ( "body_13.png", pos )
    
    
    
    
    
    
        
    if hermi.whoring >= 15 and hermi.whoring <= 17:  # WHORING LEVEL 06.
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_87.png", pos )
            her "Would you like me to show you my breasts today, sir?"
            $herView.hideshowQQ( "body_78.png", pos )
            her "Yes... I would willingly expose myself to you, professor..."
            $herView.hideshowQQ( "body_79.png", pos )
            her "That's how selfless I am!"
           
        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_14.png", pos )
            her "I can't help but feel bad for the house elves who do my laundry..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "I mean, all those dreadful semen stains..."
            $herView.hideshowQQ( "body_118.png", pos )

        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_02.png", pos )
            her "it Doesn't matter how many times you ask me this, sir..."
            her "The answer shall remain the same..."
            $herView.hideshowQQ( "body_47.png", pos )
            her "I have nothing but resentment for the \"Slytherins\"!"
            $herView.hideshowQQ( "body_69.png", pos )
        
        
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_02.png", pos )
            her "When I think about all the favours I sold you over these last months, sir..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "Although I do feel a little bit embarrassed..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "I also feel very proud of myself."
            
        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_14.png", pos )
            her "I still dedicate a lot of my time to studying..."
            her "But not nearly as much of it as I used to..."
            $herView.hideshowQQ( "body_11.png", pos )
            her "Somehow I just don't enjoy studying at all anymore..."
            $herView.hideshowQQ( "body_13.png", pos )
        
        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Gryffindor shall get the house cup this year!"
            $herView.hideshowQQ( "body_118.png", pos )
            her "{size=-4}(Even if it should cost me my dignity...){/size}"
            $herView.hideshowQQ( "body_120.png", pos )
           
           
        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_14.png", pos )
            her "I don't mind the autumn weather..."
            $herView.hideshowQQ( "body_16.png", pos )
            her "But my favourite season is winter."
            $herView.hideshowQQ( "body_15.png", pos )
        
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_14.png", pos )
            her "I used to look down on girls who spend too much time with worrying about the way they look..."
            her "But I was wrong to do so..."
            her "I am starting to understand how important it really is for a girl to look pretty."
            $herView.hideshowQQ( "body_29.png", pos )
            her "..............."
            $herView.hideshowQQ( "body_122.png", pos )
            her "I've been on a diet lately..."
            $herView.hideshowQQ( "body_34.png", pos )
            $herView.hideshowQQ( "body_33.png", pos )
       
        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_14.png", pos )
            her "Lately I've been feeling rather confident around the boys..."
            $herView.hideshowQQ( "body_06.png", pos )
            her "I think I have you to thank for that, sir."
            
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_14.png", pos )
            her "My favourite subject?"
            $herView.hideshowQQ( "body_13.png", pos )
            her "Hm..."
            $herView.hideshowQQ( "body_14.png", pos )
            her "I suppose that would be \"charms\"..."
            $herView.hideshowQQ( "body_15.png", pos )
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    if hermi.whoring >= 18 and hermi.whoring <= 20: # WHORING LEVEL 07.
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Just let me know what will be required of me today, sir."
            $herView.hideshowQQ( "body_03.png", pos )
           
        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_11.png", pos )
            her "I barely study at all anymore..."
            her "Despite that my popularity among the other students seems to be growing..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "Hm..."
                 
        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_64.png", pos )
            her "I wouldn't say \"no\" to a bottle of butterbeer right about now..."
            $herView.hideshowQQ( "body_68.png", pos )
        
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_06.png", pos )
            her "What is it, sir? Do you have another present for me?"
            $herView.hideshowQQ( "body_12.png", pos )
            her "Oh... I see..."

        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_06.png", pos )
            her "I am doing well, thank you for asking."

        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_11.png", pos )
            her "Do I look fat to you sir?"
            $herView.hideshowQQ( "body_29.png", pos )
            her "I wonder if the diet is working..."
           
        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_16.png", pos )
            her "I remember that I used to say that books were my friends..."
            $herView.hideshowQQ( "body_24.png", pos )
            her "Now that sounds so lame."
            $herView.hideshowQQ( "body_15.png", pos )
        
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Add ashwinder egg to cauldron..."
            her "Then add horseradish and heat..."
            her "Then juice a squill bulb..."
            $herView.hideshowQQ( "body_10.png", pos )
            her "Or was it a dash of thyme first?"
            $herView.hideshowQQ( "body_13.png", pos )
            her ".............."
            $herView.hideshowQQ( "body_24.png", pos )
            her "Oh, who cares?"
            $herView.hideshowQQ( "body_06.png", pos )
       
        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_14.png", pos )
            her "Do You think I am wearing enough makeup, sir?" 
            her "Wearing too much would look vulgar..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "But wearing too little would make me look plain..."
            $herView.hideshowQQ( "body_12.png", pos )
            her "I don't want to look plain!"
            
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_64.png", pos )
            her "Would you like to see my tits today, sir?" 
            $herView.hideshowQQ( "body_111.png", pos )
            her "25 house points, please."
            $herView.hideshowQQ( "body_120.png", pos )
    
   
    if hermi.whoring >= 21: # hermi.whoring LEVEL 08+.
        
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_189.png", pos )
            her "Do You have any adult magazines you don't need, sir?"
            $herView.hideshowQQ( "body_188.png", pos )

        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_31.png", pos )
            her "I am sorry to bother you with this, sir..."
            her "But do you have any condoms?"
            $herView.hideshowQQ( "body_34.png", pos )
            her "This is not for me of course... I'm asking for a friend..."
                 
        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_14.png", pos )
            her "It's been getting so cold lately..."
            $herView.hideshowQQ( "body_06.png", pos )
            her "I hope that soon the snow falls..."
        
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_127.png", pos )
            her "Jump and scream for the Gryffindor team!"
            $herView.hideshowQQ( "body_80.png", pos )
            her "So daring and bold, sporting red and gold!"
            $herView.hideshowQQ( "body_06.png", pos )

        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_10.png", pos )
            her "I hope the ball goes smoothly..."
            $herView.hideshowQQ( "body_13.png", pos )

        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_06.png", pos )
            her "I wonder what Ginny is going to wear for the ball..."
        
        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_16.png", pos )
            her "Considering the nature of the favours you keep buying from me sir..."
            $herView.hideshowQQ( "body_11.png", pos )
            her "I seldom bother to put on underwear at all anymore..."
        
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_117.png", pos )
            her "Sir, could you put your penis in my mouth?"
            $herView.hideshowQQ( "body_135.png", pos )
            her "Sir, I am begging you..."
            $herView.hideshowQQ( "body_111.png", pos )
            her "Fifty five points, please!"
            $herView.hideshowQQ( "body_122.png", pos )

        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_127.png", pos )
            her "I read this one article about the positive effects of semen on a woman's skin..."
            $herView.hideshowQQ( "body_128.png", pos )
            her "I wonder where their information is coming from..."
            $herView.hideshowQQ( "body_122.png", pos )
            her "Did the magazine conduct research of some sort?"
            $herView.hideshowQQ( "body_128.png", pos )

        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_127.png", pos )
            her "It goes like this..."
            her "First Gryffindor, then Ravenclaw, then Hufflepuff..."
            $herView.hideshowQQ( "body_186.png", pos )
            her "And Slytherin is not even on the list!"
            $herView.hideshowQQ( "body_120.png", pos )

    jump hermione_main_menu

###Hermione dialogues ###

label hermione_bookbuying:
    if teacher_jinn_quest == 3 : 
        m "Miss Granger."
        m "Can I buy your textbooks?"
        $herView.hideshowQQ( "body_15.png", pos )
        her "Excuse me?"
        m "I need your textbooks."
        $herView.hideshowQQ( "body_14.png", pos )
        her"But why would you, Albus Dumbledore, need school textbooks?"
        m "Hmm, you know..."
        m "I am working on complicated magic research."
        m "But recently, they are deadlocked."
        m "And I decided to use a last resort."
        m "I talked to Finch."
        $herView.hideshowQQ( "body_205.png", pos )
        her "What?!"
        m "Yes, with {i}thus{/i}."
        m "He told me that I should return to the basics."
        m "That truth is at the beginning, and similar crap."
        $herView.hideshowQQ( "body_09.png", pos )
        her "..."
        m "So I want to relearn all the material from the beginning."
        m "So... lend me your books?"
        $herView.hideshowQQ( "body_06.png", pos )
        her "Professor..."
        $herView.hideshowQQ( "body_14.png", pos )
        her "Of course, I would have gladly donated the books for the benefit of science!"
        $herView.hideshowQQ( "body_07.png", pos )
        her "But you understand that I need them now more than ever."
        $herView.hideshowQQ( "body_11.png", pos )
        her "Why don't you order them on osazone?"
        m "Where, sorry?"
        her "On osazone. Have you never heard of online store osazone.mag?"
        her "The largest magic store with worldwide delivery?"
        m "That Sounds... Familiar. Even too familiar."
        m "You know, I'm not too familiar with all this, could you make an order for me?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Of course. What books are you interested in?"
        m "All the books on all subjects that are taught in this school."
        $herView.hideshowQQ( "body_10.png", pos )
        her "Well, I think it would cost thousands, if not at least three..."
        m "..."
        g4 "{size=-4}Your \"training\" is becoming very expensive, little bitch...{/size}" #маленький размер
        g4 "{size=-4}Hell, maybe I should stop on the route, where I'm just making you a whore, selling your ass for points?{/size}" #маленький размер
        g9 "Ah, choices..."
        $herView.hideshowQQ( "body_08.png", pos )
        her "You said something?"
        m "No, I was just pondering over the choice of School policies...."
        $herView.hideshowQQ( "body_06.png", pos )
        her "So you decided to think about my suggestions..?"
        $herView.hideshowQQ( "body_12.png", pos )
        her "I thought you forgot..."
        m "I forget nothing, girl."
        $herView.hideshowQQ( "body_45.png", pos )
        her "..."
        m "Who knows, maybe with the next update..."
        $herView.hideshowQQ( "body_13.png", pos )
        her "What?"
        m "Ahem, no matter."
        m "Anyway, thanks for the help. I'll let you know when I got the correct amount."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Always happy to help."
        $ teacher_jinn_quest = 4
        jump hermione_main_menu
        
    elif teacher_jinn_quest == 4 and gold >= 3000:
        m "It's about buying textbooks, miss Granger."
        m "I have the correct amount."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Well, then I will immediately go and order all you need."
        # гермиона уходит
        hide screen bld1
        $herView.hideQ( Dissolve(.3) )
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=610 #Coordinates of it's movement. (To)
        $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01_f 
        pause 2
        hide screen hermione_walk_01_f 
        $ hermione_chibi_xpos = 610 #Near the desk.
        show screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)
        $ gold -=3000
        $ hermione_takes_classes = True
        $ hermione_sleeping = True
        $ teacher_jinn_quest = 5
        m "...."
        m "..."
        m "I wonder how many hookers you could buy with that money?"
        m "..."
        m "We should find out." #Not sure about this one.
                        
        if daytime:
            jump night_main_menu
                        
        else:
            jump day_main_menu
                            
    else:
        m "{size=-4}(Нужно больше золота!){/size}"
        m "(У меня такое ощущение, что где-то я уже слышал эту фразу...)"
        jump hermione_main_menu


label wrd_menu :
    menu:
    
        "- Новые вещи ! -" if wrd_new_items > 0 or (wrd_standart02 == 0 and hermi.whoring >= 3) or (wrd_standart02 >= 1 and wrd_standart03 == 0 and hermi.whoring >= 6) or (wrd_standart03 >= 1 and wrd_standart04 == 0 and hermi.whoring >= 9) or (wrd_standart04 >= 1 and wrd_standart05 == 0 and hermi.whoring >= 15) :
            menu :
                
                "- Надеть значок \"А.В.Н.Э.\" -" if hermi.Items.Any("badge_01") and wrd_badge_01 == 0 :
                    jump wrd_badge_01_first_dress
            
                "- Надеть ажурные чулки -" if hermi.Items.Any("nets") and wrd_nets == 0 :
                    jump wrd_nets_first_dress
            
                "- Надеть колготки -" if hermi.Items.Any("tights") and wrd_tights == 0 :
                    jump wrd_tights_first_dress
                    
                "- Надеть укороченную школьную юбку -" if hermi.Items.Any("shortskirt") and wrd_shortskirt == 0 :
                    jump wrd_shortskirt_first_dress
            
                "- Надеть сильно укороченную школьную юбку -" if hermi.Items.Any("xshortskirt") and wrd_xshortskirt == 0 :
                    jump wrd_xshortskirt_first_dress
            
                "- Надеть короткую школьную юбку -" if hermi.Items.Any("xxshortskirt") and wrd_xxshortskirt == 0 :
                    jump wrd_xxshortskirt_first_dress
            
                "- Надеть школьную мини-юбку -" if hermi.Items.Any("xsmallskirt") and wrd_xsmallskirt == 0 :
                    jump wrd_xsmallskirt_first_dress
            
                "- Надеть укороченную школьную мини-юбку -" if hermi.Items.Any("xxsmallskirt") and wrd_xxsmallskirt == 0 :
                    jump wrd_xxsmallskirt_first_dress
            
                "- Надеть супер-короткую школьную мини-юбку -" if hermi.Items.Any("xxxsmallskirt") and wrd_xxxsmallskirt == 0 :
                    jump wrd_xxxsmallskirt_first_dress
                    
                "- Надеть юбку болельщицы Гриффиндора -" if hermi.Items.Any("skirt_cheerleader") and wrd_skirt_cheerleader == 0 :
                    jump wrd_skirt_cheerleader_first_dress
                    
                "- Надеть миниюбку бизнес-вумен -" if hermi.Items.Any("skirt_business") and wrd_skirt_business == 0 :
                    jump wrd_skirt_business_first_dress
                    
                "- Надеть школьную рубашку без жилетки -" if wrd_standart02 == 0 and hermi.whoring >= 3 :
                    jump wrd_standart02_first_dress
                    
                "- Надеть школьную рубашку без жилетки и галстука -" if wrd_standart02 >= 1 and wrd_standart03 == 0 and hermi.whoring >= 6 :
                    jump wrd_standart03_first_dress
                    
                "- Надеть школьную рубашку и расстегнуть верхние пуговицы -" if wrd_standart03 >= 1 and wrd_standart04 == 0 and hermi.whoring >= 9 :
                    jump wrd_standart04_first_dress
                    
                "- Надеть школьную рубашку, застегнутую на одну пуговицу -" if wrd_standart04 >= 1 and wrd_standart05 == 0 and hermi.whoring >= 15 :
                    jump wrd_standart05_first_dress
            
                "- Надеть школьную рубашку мини-топик -" if hermi.Items.Any("skimpyshirt") and wrd_skimpyshirt == 0 :
                    jump wrd_skimpyshirt_first_dress
                    
                "- Надеть кофту болельщицы Гриффиндора -" if hermi.Items.Any("shirt_cheerleader") and wrd_shirt_cheerleader == 0 :
                    jump wrd_shirt_cheerleader_first_dress
                    
                "- Надеть белую рубашку в деловом стиле -" if hermi.Items.Any("shirt_business") and wrd_shirt_business == 0 :
                    jump wrd_shirt_business_first_dress
            
                "- Ничего -":
                    jump wrd_menu
                    
    
        "- Юбки -":
            menu:

                "- Надеть длинную школьную юбку -" :
                    jump wrd_skirt_dress
            
                "- Надеть укороченную школьную юбку -" if wrd_shortskirt >= 1 :
                    jump wrd_shortskirt_dress
            
                "- Надеть сильно укороченную школьную юбку -" if wrd_xshortskirt >= 1 :
                    jump wrd_xshortskirt_dress
            
                "- Надеть короткую школьную юбку -" if wrd_xxshortskirt >= 1 :
                    jump wrd_xxshortskirt_dress
            
                "- Надеть школьную мини-юбку -" if wrd_xsmallskirt >= 1 :
                    jump wrd_xsmallskirt_dress
            
                "- Надеть укороченную школьную мини-юбку -" if wrd_xxsmallskirt >= 1 :
                    jump wrd_xxsmallskirt_dress
            
                "- Надеть супер-короткую школьную мини-юбку -" if wrd_xxxsmallskirt >= 1 :
                    jump wrd_xxxsmallskirt_dress
                    
                "- Надеть юбку болельщицы Гриффиндора -" if wrd_skirt_cheerleader >= 1 :
                    jump wrd_skirt_cheerleader_dress
                    
                "- Надеть миниюбку бизнес-вумен -" if wrd_skirt_business >= 1 :
                    jump wrd_skirt_business_dress
            
                "- Ничего -":
                    jump wrd_menu
        
        "- Верх -":
            menu:

                "- Надеть школьную рубашку с жилеткой -" :
                    jump wrd_standart01_dress

                "- Надеть школьную рубашку без жилетки -" if wrd_standart02 >= 1 :
                    jump wrd_standart02_dress
                    
                "- Надеть школьную рубашку без жилетки и галстука -" if wrd_standart03 >= 1 :
                    jump wrd_standart03_dress
                    
                "- Надеть школьную рубашку и расстегнуть верхние пуговицы -" if wrd_standart04 >= 1 :
                    jump wrd_standart04_dress
                    
                "- Надеть школьную рубашку, застегнутую на одну пуговицу -" if wrd_standart05 >= 1 :
                    jump wrd_standart05_dress
            
                "- Надеть школьную рубашку мини-топик -" if wrd_skimpyshirt >= 1 :
                    jump wrd_skimpyshirt_dress
                    
                "- Надеть кофту болельщицы Гриффиндора -" if wrd_shirt_cheerleader >= 1 :
                    jump wrd_shirt_cheerleader_dress
                    
                "- Надеть белую рубашку в деловом стиле -" if wrd_shirt_business >= 1 :
                    jump wrd_shirt_business_dress
            
                "- Ничего -":
                    jump wrd_menu
        
        
        "- Чулки/Колготки -":
            menu:
            
                "- Снять чулки/колготки -" :
                    jump wrd_nonets_dress
            
                "- Надеть ажурные чулки -" if wrd_nets >= 1 :
                    jump wrd_nets_dress
                    
                "- Надеть колготки -" if wrd_tights >= 1 :
                    jump wrd_tights_dress
            
                "- Ничего -":
                    jump wrd_menu
        
#        "- Платья-":

        
        "- Прочее -":
            menu:
            
                "- Снять значки -" :
                    jump wrd_nobadge_dress
            
                "- Надеть значок \"А.В.Н.Э.\" -" if wrd_badge_01 >= 1 :
                    jump wrd_badge_01_dress
            
                "- Ничего -":
                    jump wrd_menu
                
                    
        "- Примерка вещей напрокат -" :
            jump wrd_hermi_rent_menu
            

        "- Ничего -":
            jump hermione_main_menu
        

label wrd_hermi_rent_menu :

    menu:
        "- Форма веселой школьницы -" if wrd_rent_happy_schoolgirl == 1 :
        
           if hermi.whoring < 3 :
               $herView.hideshowQQ( "body_31.png", pos )
               "Извините, сэр, но этот наряд слишком нескромный."
               $herView.hideshowQQ( "body_01.png", pos )
               jump wrd_menu
           else :
               $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
    
               call wrd_dress_undress
    
               $ herView.data().addItem( 'item_tits_no' )
               $ herView.data().addItem( 'item_skirts_skirt03_xshort' )
               $ herView.data().addItem( 'item_shirts_standard03_untucked' )

               $herView.hideshowQQ( "body_01.png", pos )
    
               pause.5
               $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
               $screens.Show("ctc").Pause().Hide("ctc")
               pause 1
               
               "Надеюсь, вам понравилось, сэр."
    
               call wrd_dress_change

               $herView.hideshowQQ( "body_01.png", pos )
               
               jump wrd_menu
           
        
        "- Форма игривой школьницы -" if wrd_rent_playful_schoolgirl == 1:
        
           if hermi.whoring < 12 :
               $herView.hideshowQQ( "body_31.png", pos )
               "Извините, сэр, но этот наряд слишком нескромный."
               $herView.hideshowQQ( "body_01.png", pos )
               jump wrd_menu
           else :
               $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
    
               call wrd_dress_undress
    
               $ herView.data().addItem( 'item_tits_no' )
               $ herView.data().addItem( 'item_skirts_skirt05_xsmall' )
               $ herView.data().addItem( 'item_shirts_standard05_untucked_unbuttoned_double' )

               $herView.hideshowQQ( "body_01.png", pos )
    
               pause.5
               $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
               $screens.Show("ctc").Pause().Hide("ctc")
               pause 1
               
               "Надеюсь, вам понравилось, сэр."
    
               call wrd_dress_change

               $herView.hideshowQQ( "body_01.png", pos )
               
               jump wrd_menu

        
        "- Форма болельщицы Гриффиндора -" if wrd_rent_cheerleader == 1 :
        
           if hermi.whoring < 6 :
               $herView.hideshowQQ( "body_31.png", pos )
               "Извините, сэр, но этот наряд слишком нескромный."
               $herView.hideshowQQ( "body_01.png", pos )
               jump wrd_menu
           else :
               $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
    
               call wrd_dress_undress
    
               $ herView.data().addItem( 'item_tits_no' )
               $ herView.data().addItem( 'item_skirts_cheerleader_gryffindor' )
               $ herView.data().addItem( 'item_shirts_cheerleader_gryffindor' )

               $herView.hideshowQQ( "body_01.png", pos )
    
               pause.5
               $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
               $screens.Show("ctc").Pause().Hide("ctc")
               pause 1
               
               "Надеюсь, вам понравилось, сэр."
    
               call wrd_dress_change

               $herView.hideshowQQ( "body_01.png", pos )
               
               jump wrd_menu

        
        "- Одежда бизнес-леди -" if wrd_rent_business == 1 :
        
           if hermi.whoring < 9 :
               $herView.hideshowQQ( "body_31.png", pos )
               "Извините, сэр, но этот наряд слишком нескромный."
               $herView.hideshowQQ( "body_01.png", pos )
               jump wrd_menu
           else :
               $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
    
               call wrd_dress_undress
    
               $ herView.data().addItem( 'item_tits_no' )
               $ herView.data().addItem( 'item_stockings_tights' )
               $ herView.data().addItem( 'item_skirts_skirt_business' )
               $ herView.data().addItem( 'item_shirts_blouse_business' )

               $herView.hideshowQQ( "body_01.png", pos )
    
               pause.5
               $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
               $screens.Show("ctc").Pause().Hide("ctc")
               pause 1
               
               "Надеюсь, вам понравилось, сэр."
    
               call wrd_dress_change

               $herView.hideshowQQ( "body_01.png", pos )

               jump wrd_menu
        
        "- Ничего -" :
            jump wrd_menu

            
            
