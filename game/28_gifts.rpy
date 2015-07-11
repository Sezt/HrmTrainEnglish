label menu_gifts_actions:
    $item=hero.Items(choose.choice)
    $ gifted = True 

    if item.Name=="ball_dress" and hermi.Items.Count(item.Name)==0:
        show screen  blktone
        with d3
        m "(I feel that there's no going back after I give her this dress...)"
        m "(I'm ready to do this?)"
        hide screen blktone
        menu:
            "\"Yes, quite...\"":
                jump giving_thre_dress #27_final_events.rpy
            "\"No, not ready...\"":
                jump hermione_main_menu


    jump expression "giving_"+item.Name



label giving_xxxsmallskirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1
#    $ have_xxxsmallskirt = False # Turns TRUE when you have the skirt in your possession.
#    $ gave_xxxsmallskirt = True #Turns True when Hermione has the xxxsmallskirt.
    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"xxxsmallskirt")

    $ hermi.liking = 0
    m "Here... This is for you..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">You give the school miniskirt to Hermione..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Hm...? What is this?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "A skirt?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Thank you professor."
    m "Don't mention it."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu
    
    
    
### DRESS CODE ###
label mini_on:
    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_04.png", pos )
        her "You cannot be serious, sir!"
        her "A skirt this short?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...It barely covers anything, sir."
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "Gladly..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "well, alright..."
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Hm...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "But it's so short......"
        menu:
            m "..."
            "\"Just put it on!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Sir this is hardly the appropriate attire for a Hogwarts student."
                $herView.hideshowQQ( "body_09.png", pos )
                her "I refuse!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Hm..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Well, in that case..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "As long as it benefits my house..."
            "\"Fine. Forget it.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Alright..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Hm...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "But it's so short..."
        menu:
            m "..."
            "\"Just put it on!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Alright, Alright..."
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "hm..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Alright. I don't mind then."
            "\"Fine. Forget it\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Oh..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        


    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Yes, sir..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )
                                                                                                                                                                                                                          #HERMIONE
    
    
    $herView.data().setStyleKey( 'skirt', 'short' )
    #$ herView.data().addSkirt( CharacterExItem( herView.mClothesFolder, "skirt_short.png", G_Z_SKIRT ) )
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
                                                                                                                                                                                                                     #HERMIONE
    $herView.showQQ( None, pos )
    jump hermione_main_menu
    
    
label mini_off:
    $ pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_04.png", pos )
        her "I'm glad that you came to your senses, sir. "
        $herView.hideQQ()
        $herView.addFaceName( "body_03.png")
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_01.png", pos )
        her "Gladly, sir."

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_13.png", pos )
        her "Alright..."
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_28.png", pos )
        her "That boring thing again?"
    
    
    #$ herView.data().addSkirt( CharacterExItem( herView.mClothesFolder, "skirt_normal.png", G_Z_SKIRT ) )
    $herView.data().setStyleKey( 'skirt', 'default' )
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump hermione_main_menu
   
    
    
label badge_put:
    $herView.hideQQ()

    $ pos = POS_370
    $herView.showQQ( "body_01.png", pos )
    her "Of course, sir..."
    
    #$ herView.data().addItemKey( G_N_BADGE, CharacterExItem( herView.mClothesFolder, "badge.png", G_Z_DRESS + 1, 'dress' ) )
    $herView.data().addItem( 'item_badge' )
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump hermione_main_menu
    
    
label badge_take:
    $herView.hideQQ()
    
    $ pos = POS_370
    $herView.showQQ( "body_01.png", pos )
    her "As you wish, sir..."

    $ herView.data().delItem( 'item_badge' )
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump hermione_main_menu
    
    
### FISHNETS ###
label nets_put:
    $ pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_11.png", pos )
        her "fishnet stockings...?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "You cannot be serious, sir!"
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Gladly..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "well, alright..."
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Hm...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "I am not that kind of girl sir..."
        her "You may have better luck with someone from \"Slytherin\"..."
        menu:
            m "..."
            "\"Just put it on!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Sir this is hardly the appropriate attire for a Hogwarts student."
                $herView.hideshowQQ( "body_09.png", pos )
                her "I refuse!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Hm..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Well, in that case..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "As long as it benefits my house..."
            "\"Fine. Forget it\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Alright..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Hm...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Fishnet stockings?"
        $herView.hideshowQQ( "body_29.png", pos )
        her "I don't know about that sir..."
        menu:
            m "..."
            "\"Just put them on!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Alright, Alright..."
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Hm..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Alright. I don't mind then."
            "\"Fine. Forget it\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "oh..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        

    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "If you insist, sir..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )
                                                                                                                                                                                                                          #HERMIONE
    
     
    #$ herView.data().addItemKey( G_N_NETS, CharacterExItem( herView.mClothesFolder, "nets.png", G_Z_LEGS + 1, 'legs' ) )
    $herView.data().addItem( 'item_nets' )
    
    #$ legs_02 = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    pause.1
    $herView.showQQ( None, pos )
    jump hermione_main_menu
    
    
label nets_take:
    $ pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_04.png", pos )
        her "I'm glad that you came to your senses, sir."
        $herView.hideQQ()
        $herView.addFaceName( "body_03.png" )
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_01.png", pos )
        her "Gladly, sir."

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_12.png", pos )
        her "As you wish, sir."
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_28.png", pos )
        her "Really? Aw..."
    
    
    $ herView.data().delItem( 'item_nets' )
    #$ legs_02 = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    $herView.showQQ( None, pos )
    jump hermione_main_menu
    
    
    
    
    
    
    
    
   
    
    
    
    
    
    
       
label giving_lubricant: # JAR OF Anal lubricant.
    $herView.hideQ( d5 )                                                                                                                                                                                                           #HERMIONE
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 6
        $herView.showQ( "body_02.png", pos, d5 )                                                                                                                                                                                         #HERMIONE
        her "I don't know what this is..."
        $herView.hideshowQQ( "body_05.png", pos )
        her "But I have the feeling that the jar is full of something vile and inappropriate..."
        her "No, thank you, sir."
        $herView.hideQQ()
        call upset #Message saying that Hermione became upset with you.
        $herView.addFaceName( "body_03.png" )
       
        
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 2
        $herView.showQ( "body_73.png", pos, d5 )                                                                                                                                                                                                                      #HERMIONE
        her "Hm..."
        $herView.hideshowQQ( "body_66.png", pos )
        her "I think I know what this is..."
        her "But why would you give something like this to one of your pupils, sir?"
        $herView.hideshowQQ( "body_69.png", pos )
        her "No, thank you."
        $herView.hideQQ()
        call upset #Message saying that Hermione became upset with you.
   
        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $hermi.Items.Receive(hero.Items,item.Name) #$ anal_lube -= 1
        $herView.showQ( "body_118.png", pos, d5 )
        her "Anal lubricant??"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Ehm.. well... I know this girl..."
        her "I mean I don't know her, she is a friend of a friend..."
        her "Yes, I will take this for her..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/09.png" # Анальный лубрикант
        show screen gift
        with d3
        ">You give the jar to Hermione..."
        hide screen gift
        with d3
        $herView.hideshowQQ( "body_186.png", pos )
        her "Still, I think you should not give presents like this to your pupils, sir."
        $herView.hideQQ()
        call no_change #Message: Hermione's mood did not change.
        $herView.hideshowQQ( "body_79.png ", pos);
        
    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #$ anal_lube -= 1
        $ hermi.liking +=5
        $herView.showQ( "body_124.png", pos, d5 )
        her "Anal lubricant, sir?"
        $herView.hideshowQQ( "body_186.png", pos )
        her "I know a couple of girls who would do anything for a commodity like that."
        $herView.hideshowQQ( "body_128.png", pos )
        her "Thank for looking out for us, sir."
        $herView.hideQQ()
        call happy #Message that says that Hermione's mood has improved.
 
    $ pos = POS_370
    $herView.showQQ( None, pos )    
    jump hermione_main_menu
        
        
        
        
label giving_condoms: # A PACK OF CONDOMS
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 6
        $herView.showQ( "body_18.png", pos, d5 )
        her "Condoms?!"
        $herView.hideshowQQ( "body_30.png", pos )
        her "sir, I wouldn't even know what to do with them..."
        $herView.hideQQ()
        call upset #Message saying that Hermione became upset with you.
        $herView.addFaceName( "body_03.png" )
        
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.showQ( "body_07.png", pos, d5 )
        her "...Condoms?"
        $herView.hideshowQQ( "body_04.png", pos )
        her "Ehm... Is this a part of some new Hogwarts sex ed program or something?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "No, sir... It feels wrong to accept a thing like this from you..."
        $herView.hideQQ()
        call no_change 
   
        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $hermi.Items.Receive(hero.Items,item.Name) #$ condoms -= 1
        $ hermi.liking += 3
        $herView.showQ( "body_03.png", pos, d5 )
        her "A pack of condoms?"
        her "Sir, what possible use could I have for those?"
        $herView.hideshowQQ( "body_04.png", pos )
        her "Well, I shall accept them simply because it is rude to refuse a gift..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/10.png" # CONDOMS
        show screen gift
        with d3
        ">You give a pack of condoms to Hermione..."
        hide screen gift
        with d3
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_29.png" )
        

        
    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #$ anal_lube -= 1
        $ hermi.liking +=4
        $herView.showQ( "body_08.png", pos, d5 )
        her "A pack of condoms?"
        $herView.hideshowQQ( "body_128.png", pos )
        her "I appreciate your concern, sir. Thank you."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/10.png" # CONDOMS
        show screen gift
        with d3
        ">You give a pack of condoms to Hermione..."
        hide screen gift
        with d3
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_45.png" )
 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
        
        
     
label giving_perfume: # perfume
    if hero._perfumeused!=time.stamp:
        $Say("> You are going to give Hermione the spirits, but they miraculously not be given into the hands.//"
            "> You are going to give Hermione the spirits, but they miraculously not be given into the hands.")
    else:
        $hermi.Visibility("body+")
        $hermi("~body_15.png// Sir This smell... ...")
        $hero("What smell?")
        $hermi("~body_13.png// You have the tower... it smells like... it reminds me of the times when I was little.")
        if hermi.Items("perfume")._count==0:
            $hero("Really?")
            $hermi("~body_75.png// It's the smell of a dental office!")
            $hero("Oh, poor child, looks like you had a hard time.")
            $hermi("~body_06.png// No, sir, I liked the smell and the memories!")
            $hero("Uh Girl, I knew you were a bit of a masochist, but that is so...")
            $hermi("~body_04.png// SIR! My parents are dentists!")
            $hero("But!.. Oh!.. Well, if so, ...")
        else:
            $hero("Yeah, I just remembered that dental office smell.")
        menu:
            "\"Take this perfume as a gift\"":
                "> You are giving Hermione perfume."
                $hermi.Items.Receive(hero.Items,"perfume")
                $hermi("~body_01.png// Спасибо, сэр!")
                $hermi.IncValue("liking",9-hermi.whoring//3) # от 9 до 1 балла (падает с повышение развращенности), при этом отношение может стать положительным
                call happy #Message that says that Hermione's mood has improved.


            "\"I'm glad you liked it\"":
                pass
        $hermi.Visibility()

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu


     
     
### CANDY ###
label giving_candy: # CANDY.
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking += 5
        $hermi.Items.Receive(hero.Items,item.Name) # $ candy -= 1
        $herView.showQ( "body_01.png", pos, d5 )
        her "A lollipop?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">You give the candy to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Thank you, sir."
        call happy #Message that says that Hermione's mood has improved.

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 5
        $hermi.Items.Receive(hero.Items,item.Name) #$ candy -= 1
        $herView.showQ( "body_03.png", pos, d5 )
        her "candy?"
        $herView.hideshowQQ( "body_02.png", pos )
        her "Candy is for kids, sir."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">You give the candy to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_29.png", pos )
        her "Thank you, sir..."
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_06.png" )
        

        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 5
        $hermi.Items.Receive(hero.Items,item.Name) #$ candy -= 1
        $herView.showQ( "body_03.png", pos, d5 )
        her "candy?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">You give the candy to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_08.png", pos )
        her "Ehm... Sure, thanks..."
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_06.png" )
        
    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #$ candy -= 1
        $ hermi.liking +=5
        $herView.showQ( "body_06.png", pos, d5 )
        her "A lollipop?"
        $herView.hideshowQQ( "body_46.png", pos )
        her "Clever girls use candy like this as a \"weapon\"."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">You give the candy to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_74.png", pos )
        her "Thank you, sir."
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_128.png" )
 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
    
        
        
        

### CHOCOLATE ###
label giving_chocolate: # CHOCOLATE.
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) 
        $herView.showQ( "body_01.png", pos, d5 )
        her "A chocolate bar?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">You give the chocolate to Hermione"
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Thank you, sir."
        call happy #Message that says that Hermione's mood has improved.

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_03.png", pos, d5 )
        her "A chocolate bar?"
        $herView.hideshowQQ( "body_09.png", pos )
        her "Hm..."
        her "That thing about fairies..."
        $herView.hideshowQQ( "body_11.png", pos )
        her "That is a joke of some sort, right?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">You give the chocolate to Hermione"
        hide screen gift
        with d3
        $herView.showQQ( "body_15.png", pos )
        her "Thank you..."
        call happy #Message that says that Hermione's mood has improved.
        

        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_03.png", pos, d5 )
        her "A chocolate bar?"
        $herView.hideshowQQ( "body_24.png", pos )
        her "I just like the way it crunches, sir! N-not the taste..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">You give the chocolate to Hermione"
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Ehm... Sure, thanks..."
        call happy #Message that says that Hermione's mood has improved.
       
 
        
    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 10
        $herView.showQ( "body_06.png", pos, d5 )
        her "A chocolate bar?"
        $herView.hideshowQQ( "body_111.png", pos )
        her "You spoil me, sir."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">You give the chocolate to Hermione"
        hide screen gift
        with d3
        $herView.showQQ( "body_129.png", pos )
        her "Thank you."
        call happy #Message that says that Hermione's mood has improved.
        
 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
        

    ### VIBRATOR ###
label giving_vibrator: # VIBRATOR.
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 10
        $herView.showQ( "body_01.png", pos, d5 )
        her "A magic wand?"
        $herView.hideshowQQ( "body_15.png", pos )
        her "No, it doesn't look like--"
        her ".........?"
        $herView.hideshowQQ( "body_18.png", pos )
        her "!!!"
        $herView.hideshowQQ( "body_187.png", pos )
        her "Professor Dumbledore!"
        $herView.hideshowQQ( "body_30.png", pos )
        her "This is just beyond inappropriate!"
        call upset
        $herView.addFaceName( "body_120.png" )
    
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "Is this what I think it is?"
        $herView.hideshowQQ( "body_186.png", pos )
        her "Sir, let me remind you that I belong to the noble house of \"Gryffindor\"."
        $herView.hideshowQQ( "body_120.png", pos )
        her "A present like that would be appropriate for a girl from \"Slytherin\", sir."
        call upset

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_118.png", pos, d5 )
        her "Is that a... vibrator?"
        her "The design..."
        her "it reminds me of my wand..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "Did you have this custom made for me sir?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "This is inappropriate..."
        $herView.hideshowQQ( "body_29.png", pos )
        her "But I shall take it nonetheless..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/13.png" # VIBRATOR
        show screen gift
        with d3
        ">You give the vibrator to Hermione..."
        hide screen gift
        with d3
        call no_change
        

    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 10
        $herView.showQ( "body_11.png", pos, d5 )
        her "This vibrator..."
        $herView.hideshowQQ( "body_10.png", pos )
        her "It's... calling out for me..."
        $herView.hideshowQQ( "body_66.png", pos )
        her "But not in a dirty way, sir."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/13.png" # VIBRATOR
        show screen gift
        with d3
        ">You give the vibrator to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_124.png", pos )
        her "Thank you, sir."
        $herView.hideQQ()
        call happy #Message that says that Hermione's mood has improved.
        
 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
        ### STRAP-ON ###
label giving_strapon: # STRAP-ON.
    $herView.hideQ( d5 )
    $ pos = POS_140
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking += 20
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_18.png", pos, d5 )
        her "What is that?"
        $herView.hideshowQQ( "body_14.png", pos )
        her "An artifact of some sort or a trophy?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "So well-crafted..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Are you sure that it's alright for me to have it, sir?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">You give the strap-on to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_16.png", pos )
        her "Thank you very much, sir. I promise to take good care of it."
        $herView.hideQQ()
        call happy
        $herView.addFaceName( "body_15.png" )
    
    
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 15
        $herView.showQ( "body_18.png", pos, d5 )
        her "!!!"
        $herView.hideshowQQ( "body_118.png", pos )
        her "That is..."
        her "But it doesn't even look... human..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "I mean..."
        $herView.hideshowQQ( "body_86.png", pos )
        her "Sir, do you have no shame?!"
        her "Presenting a thing like that to a pupil?!"
        $herView.hideshowQQ( "body_87.png", pos )
        her ".................."
        $herView.hideshowQQ( "body_47.png", pos )
        her "Please put it away, sir."
        $herView.hideQQ()
        call upset

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "That thing..."
        $herView.hideshowQQ( "body_117.png", pos )
        her "Is that the actual size of the... of the real \"thing\"?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "I mean..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "......................."
        $herView.hideshowQQ( "body_117.png", pos )
        her "Is this like a party prank prop?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "It's so well-crafted though..."
        $herView.hideshowQQ( "body_33.png", pos )
        her "I will take it..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">You give the strap-on to Hermione..."
        hide screen gift
        with d3
        call happy


    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 30
        $herView.showQ( "body_48.png", pos, d5 )
        her "It's... It's magnificent, sir..."     
        $herView.hideshowQQ( "body_189.png", pos )
        her "Is it really modeled after a thestral?"
        $herView.hideshowQQ( "body_190.png", pos )
        her "But the creatures are invisible..."
        $herView.hideshowQQ( "body_118.png", pos )
        her ".................."
        $herView.hideshowQQ( "body_123.png", pos )
        her "Breathtaking..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Not in the way you think, sir..."
        $herView.hideshowQQ( "body_127.png", pos )
        her "I am merely admiring the craftsmanship..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">You give the strap-on to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_129.png", pos )
        her "Thank you for the gift, sir."
        $herView.hideQQ()
        call happy

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
        
        
        
        
        
   
        ### BALL GAG ###
label giving_ballgag: # BALL GAG.
    $herView.hideQ( d5 )
    $ pos = POS_140
        
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "What is this?"
        $herView.hideshowQQ( "body_141.png", pos )
        her "Is this like one of those adult toys?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "What woman in her right mind would subject herself to a humiliation like that?"
        $herView.hideshowQQ( "body_186.png", pos )
        her "And what possible use could I have for such objects?"
        $herView.hideshowQQ( "body_187.png", pos )
        her "This is just insulting, sir..."                                                                                                                                                                                                                
        call upset

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 5
        $herView.showQ( "body_186.png", pos, d5 )
        her "Sir, do you not realize how inappropriate it would be for me to accept a present like that?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "And I would not even know what to do with them anyway..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "I mean these fluffy things are obviously handcuffs..."
        her "But this ball... ehm..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Sir, please..."
        her "Just put them away."
        call upset


    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 9
        $herView.showQ( "body_120.png", pos, d5 )
        her "A month ago I would've felt insulted to receive a gift like this..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "But by now I know that some girl really do find pleasure in toys like..."
        $herView.hideshowQQ( "body_117.png", pos )
        $herView.hideshowQQ( "body_120.png", pos )
        her "But I assure you that I am not one of them, sir."
        $herView.hideshowQQ( "body_189.png", pos )
        her "But I know a girl who knows a girl who is into things like..."
        $herView.hideshowQQ( "body_188.png", pos )
        her "Yes, I shall take these to her..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">You give the ball gag and cuffs to Hermione..."
        hide screen gift
        with d3
        call happy

    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 15
        $herView.showQ( "body_190.png", pos, d5 )
        her "A ball gag and handcuffs?"
        $herView.hideshowQQ( "body_122.png", pos )
        her "This is completely inappropriate, sir." # :)
        $herView.hideshowQQ( "body_129.png", pos )
        her "But a gift is a gift, right?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">You give the ball gag and cuffs to Hermione..."
        hide screen gift
        with d3
        call happy
        

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
        
        
        
        
        
        
        
        
        
        
        
        
        
  
      ### ANAL PLUGS ###
label giving_plug: 
    $herView.hideQ( d5 )
    $ pos = POS_140

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking += 8
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "Hm...?"
        $herView.hideshowQQ( "body_15.png", pos )
        her "Are those like key-chain toys?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/16.png" # ANAL PLUG.
        show screen gift
        with d3
        ">You give the anal plugs to Hermione..."
        hide screen gift
        with d3
        $herView.hideshowQQ( "body_185.png", pos )
        her "Thank you, sir."
        call happy


    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 15
        $herView.showQ( "body_186.png", pos, d5 )
        her "Sir, are those adult toys of some sort?"
        $herView.hideshowQQ( "body_187.png", pos )
        her "those are some of those anal things, aren't they?"
        her "Sir this is nothing but a weapon meant to oppress women!"
        $herView.hideshowQQ( "body_120.png", pos )
        her "Despicable!"
        call upset

        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.showQ( "body_120.png", pos, d5 )
        her "Yes, I know that some girls have uhm..."
        $herView.hideshowQQ( "body_186.png", pos )
        her "Have use for things such as these..."
        her "But not me, sir."
        $herView.hideshowQQ( "body_120.png", pos )
        her "No, thank you."
        call no_change

    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "Anal plugs?"
        $herView.hideshowQQ( "body_117.png", pos )
        her "I have no use for things like that, sir..."
        $herView.hideshowQQ( "body_122.png", pos )
        her "They are so pretty though..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "....................."
        $herView.hideshowQQ( "body_121.png", pos )
        her "Well, alright. I shall take them off your hands if I must, sir."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/16.png" # ANAL PLUGS.
        show screen gift
        with d3
        ">You give the anal plugs to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_127.png", pos )
        her "But I shall never use them of course..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "................"
        call happy
        

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu
        
        
        
        
        
        
        
          ### EDUCATIONAL MAGAZINES ###
label giving_mag1: 
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking += 15
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "\"Popular magic\" magazines?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of educational magazines to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Thank you, sir!"
        her "I will use them for my research!"
        call happy

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "Sometimes I find information in magazines that I could never find in a book..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of educational magazines to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Thank you, sir!"
        her "I will use them for my research!"
        call happy

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 3 
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_02.png", pos, d5 )
        her "oh..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Yes, I used to read magazines like that a lot..."
        $herView.hideshowQQ( "body_10.png", pos )
        her "Lately not so much though..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of educational magazines to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Thank you, sir!"
        call happy
     

    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_10.png", pos, d5 )
        her "Ehm..."
        $herView.hideshowQQ( "body_08.png", pos )
        her "To be honest, magazines like that lost their appeal to me completely lately..."
        $herView.hideshowQQ( "body_11.png", pos )
        her "But I don't mind taking them off you hands anyway, sir."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of educational magazines to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_13.png", pos )
        her "Thank you."
        call no_change 

 
    $ pos = POS_370
    $herView.showQQ( None, pos  )
    jump hermione_main_menu    
        
        
        
        
        
              ### GIRLY MAGAZINES ###
label giving_mag2: 
    $herView.hideQ( d5 )
    $ pos = POS_140

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.showQ( "body_15.png", pos, d5 )
        her "Hm?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "This is the sort of press some \"slytherin\" bimbo would appreciate."
        $herView.hideshowQQ( "body_16.png", pos )
        her "I am way above silly magazines like that, sir."
        call no_change
        $herView.addFaceName( "body_01.png" )
        
        
      
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 5
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_04.png", pos, d5 )
        her "I don't read magazines of that nature, sir..."
        $herView.hideshowQQ( "body_13.png", pos )
        her "................"
        $herView.hideshowQQ( "body_04.png", pos )
        her "But I could give it a try just to humour you I suppose..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of rather girly magazines to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_08.png", pos )
        her "Thank you, sir!"
        call happy
        $herView.addFaceName( "body_06.png" )

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 15 
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_10.png", pos, d5 )
        her "I ashamed to admit this, but..."
        $herView.hideshowQQ( "body_24.png", pos )
        her "I really enjoy reading magazines like that lately..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of rather girly magazines to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_08.png", pos )
        her "Thank you, sir."
        call happy
        $herView.addFaceName( "body_06.png" )
        

    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 15
        $herView.showQ( "body_18.png", pos, d5 )
        her "The Latest edition of \"Girlz\"?!"
        $herView.hideshowQQ( "body_24.png", pos )
        her "I can't have enough of that brilliant magazine!"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of rather girly magazines to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_08.png", pos )
        her "Thank you, sir."
        call happy
        $herView.addFaceName( "body_06.png" )

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu        
        
        
        
                  ### ADULT MAGAZINES ###
label giving_mag3: 
    $herView.hideQ( d5 )
    $ pos = POS_140

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 7
        $herView.showQ( "body_02.png", pos, d5 )
        her "Are that...?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "Adult magazines, sir?"
        $herView.hideshowQQ( "body_69.png", pos )
        her "Given to me by An esteemed wizard of your status?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "Sir, surely you could find a more productive way to spend your free time."
        $herView.hideshowQQ( "body_47.png", pos )
        her "And I most definitely would not have use for those..."
        call upset
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 3
        $herView.showQ( "body_05.png", pos, d5 )
        her "Adult magazines?"
        $herView.hideshowQQ( "body_69.png", pos )
        her "Sir, I have no interest in things like that."
        $herView.hideshowQQ( "body_47.png", pos )
        her "And how is this an appropriate present for one of your students, sir?"
        call upset
        $herView.addFaceName( "body_29.png" )


    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 8 
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_31.png", pos, d5 )
        her "Adult magazines?"
        $herView.hideshowQQ( "body_34.png", pos )
        her "Sir, this is such an inappropriate present for a girl my age..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/19.png" # ADULT MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of adult magazines to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_79.png", pos )
        her "I shall throw these away myself..."
        call happy
        $herView.addFaceName( "body_120.png" ) 


    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 15
        $herView.showQ( "body_75.png", pos, d5 )
        her "The New edition of \"L.o.v.e.\"!!!"
        $herView.hideshowQQ( "body_122.png", pos )
        her "Err.. I mean, adult magazines?"
        her "This is a little inappropriate..."
        $herView.hideshowQQ( "body_74.png", pos )
        her "But I will take them..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/19.png" # ADULT MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of adult magazines to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_74.png", pos )
        her "thank you, sir."
        call happy
       

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu            
        
        
        
        
        
                      ### PORN MAGAZINES ###
label giving_mag4: 
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 15
        $herView.showQ( "body_01.png", pos, d5 )                                                                                                                                                                                       #HERMIONE
        her "Hm... What is this?"
        $herView.hideshowQQ( "body_130.png", pos )
        her "Sir, those are porn magazines!"
        $herView.hideshowQQ( "body_187.png", pos )
        her "Shame on you, sir!"
        call upset
        


    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 8
        $herView.showQ( "body_48.png", pos, d5 )
        her "Porn magazines?"
        $herView.hideshowQQ( "body_87.png", pos )
        her "Sir, what do you expect me to do with those?"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Research them?"
        $herView.hideshowQQ( "body_86.png", pos )
        her "Despicable!"
        call upset
        $herView.addFaceName( "body_120.png" )
        

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_31.png", pos, d5 )
        her "That's hardcore porn, sir."
        $herView.hideshowQQ( "body_34.png", pos )
        her "Which is a completely inappropriate gift for a girl my age!"
        $herView.hideshowQQ( "body_118.png", pos )
        her ".............."
        $herView.hideshowQQ( "body_117.png", pos )
        her "But I will take them..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/20.png" # PORN MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of porn magazines to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_79.png", pos )
        her "And I shall throw them in the trash, where they and... girls who like these things belong..."
        call no_change
        $herView.addFaceName( "body_120.png" )

    if hermi.whoring >= 18: # Lv 7+  
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 15
        $herView.showQ( "body_48.png", pos, d5 )
        her "Pornography?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "................"
        $herView.hideshowQQ( "body_117.png", pos )
        her "How can women even agree to do things like that, sir?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "................."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Alright, I shall accept them..."
        $herView.hideshowQQ( "body_189.png", pos )
        her "Solely for research purposes of course..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/20.png" # PORN MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of porn magazines to Hermione..."
        hide screen gift
        with d3
        call happy
        $herView.addFaceName( "body_45.png" )

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                
        
        
        
        
           
                      ### BUTTERBEER ###
label giving_beer: 
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 3
        $herView.showQ( "body_01.png", pos, d5 )
        her "Butterbeer?"
        $herView.hideshowQQ( "body_08.png", pos )
        her "Are you sure about that, sir?"
        $herView.hideshowQQ( "body_06.png", pos )
        her "It does contain alcohol, you know..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">You give the bottle to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Thank you."
        call happy
        


    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_11.png", pos, d5 )
        her "Butterbeer, sir?"
        $herView.hideQQ()
        
        $herView.showQQ( "body_14.png", pos )
        her "To let you in on a little secret, sir..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "I'm a big fan of this completely harmless beverage."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">You give the bottle to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Thank you, sir."
        call happy
        

        

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 15
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "Butterbeer?"
        $herView.hideshowQQ( "body_24.png", pos )
        her "Thank you, sir."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">You give the bottle to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "I shall drink this with the girls later."
        call happy
        

    if hermi.whoring >= 18: # Lv 7+  
        $ hermi.liking += 20
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_06.png", pos, d5 )
        her "Butterbeer...?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Thank you, sir."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">You give the bottle to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "I shall drink this later with the boys."
        $herView.hideshowQQ( "body_189.png", pos )
        her "Err... I meant to say with the girls, of course."
        call happy
        $herView.addFaceName( "body_01.png" )

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                
            
        
        
        
        
        
                   ### PLUSH OWL ###
label giving_owl: 
    $herView.hideQ( d5 )

    $ pos = POS_140

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $ hermi.liking += 7
        $herView.showQ( "body_01.png", pos, d5 )
        her "A stuffed owl?"
        $herView.hideshowQQ( "body_06.png", pos )
        her "It's cute..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">You give the owl to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Thank you, sir."
        call happy
        
      

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_11.png", pos, d5 )
        her "A plush toy?"
        $herView.hideshowQQ( "body_06.png", pos )
        her "I like it!"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">You give the owl to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Thank you, sir."
        call happy

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 15
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "A toy?"
        $herView.hideshowQQ( "body_02.png", pos )
        her "Toys are for kids, sir."
        $herView.hideshowQQ( "body_29.png", pos )
        her "But I'll take it..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">You give the owl to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Thank you, sir."
        call happy
        
        
        
      
    if hermi.whoring >= 18: # Lv 7+  
        $ hermi.liking += 4
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_66.png", pos, d5 )
        her "This is one of those adult toys isn't it?"
        $herView.hideshowQQ( "body_87.png", pos )
        her "There's got to be a switch or a button somewhere..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "So... Does it vibrate or something?"
        $herView.hideshowQQ( "body_190.png", pos )
        her "Oh...?"
        her "So it is really just a plush toy then?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "Shame..."
        $herView.hideshowQQ( "body_34.png", pos )
        her "I mean, thank you, sir."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">You give the owl to Hermione..."
        hide screen gift
        with d3
        $herView.addFaceName( "body_01.png" )
        call happy

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                
    
    
    
        
     ### SEX DOLL ###
label giving_sexdoll: 
    $herView.hideQ( d5 )
   
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 20
        $herView.showQ( "body_48.png", pos, d5 )
        her "Is this..."
        $herView.hideshowQQ( "body_34.png", pos )
        her "A sex doll?!"
        $herView.hideshowQQ( "body_32.png", pos )
        her "Professor Dumbledore!!!"
        call upset
        $herView.addFaceName( "body_33.png" )

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking -= 20
        $herView.showQ( "body_48.png", pos, d5 )
        her "A sex doll?"
        $herView.hideshowQQ( "body_120.png", pos )
        her "This is just so unbecoming for an esteemed wizard such as yourself, sir..."
        call upset

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 10
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_118.png", pos, d5 )
        her "A sex doll..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "This is a little inappropriate..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "But maybe we could use it for a prank or something..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
        show screen gift
        with d3
        ">You give the blow-up doll to Hermione......"
        hide screen gift
        with d3
        $herView.showQQ( "body_124.png", pos )
        her "Thank you, sir."
        call happy
        
    if hermi.whoring >= 18: # Lv 7+  
        $ hermi.liking += 30
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_73.png", pos, d5 )
        her "the Joanne sex doll?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "I Can't say that I approve of this..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "But I know Harry would love to have a go at it..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
        show screen gift
        with d3
        ">You give the blow-up doll to Hermione......"
        hide screen gift
        with d3
        $herView.showQQ( "body_188.png", pos )
        her "Thank you, sir."
        call happy
        

        
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                
        
        
      ### SEXY LINGERIE ###
label giving_lingerie: 
    $herView.hideQ( d5 )

    $ pos = POS_140

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking -= 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "lingerie?"
        $herView.hideshowQQ( "body_120.png", pos )
        her "Sir, I cannot accept a gift like this from you..."
        call upset
       
      

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.showQ( "body_118.png", pos, d5 )
        her "sexy lingerie?"
        $herView.hideshowQQ( "body_117.png", pos )
        her "You know I cannot possibly accept a gift like that from you, sir."
        $herView.hideshowQQ( "body_118.png", pos )
        her "(It's pretty though)........."
        call no_change

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 7
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_124.png", pos, d5 )
        her "sexy lingerie?"
        $herView.hideshowQQ( "body_122.png", pos )
        her "Sir that is so inappropriate..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/24.png" # SEXY LINGERIE.
        show screen gift
        with d3
        ">You give the lingerie to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_188.png", pos )
        her "Thank you, sir."
        call happy

        
    if hermi.whoring >= 18: # Lv 7+  
        $ hermi.liking += 15
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_124.png", pos, d5 )
        her "sexy lingerie?"
        $herView.hideshowQQ( "body_123.png", pos )
        her "Do You think it will make me look like one of the witches in those adult magazines, sir?"
        $herView.hideshowQQ( "body_122.png", pos )
        her "Oh... I mean, thank you, sir."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/24.png" # SEXY LINGERIE.
        show screen gift
        with d3
        ">You give the lingerie to Hermione..."
        hide screen gift
        with d3
        call happy
        

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                
        
    ### BROOM ###
label giving_broom: 
    $herView.hideQ( d5 )
    
    $ pos = POS_140

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $ hermi.liking += 20
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "A broom...?"
        $herView.hideshowQQ( "body_03.png", pos )
        her "Hm..."
        $herView.hideshowQQ( "body_07.png", pos )
        her "What is that silly-looking thing attached to it?"
        $herView.hideshowQQ( "body_08.png", pos )
        her "Is it like a saddle...?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">You give the broom to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_11.png", pos )
        her "Thank you for the gift, sir."
        $herView.addFaceName( "body_06.png" )
        call happy
       
      

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 20
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_01.png", pos, d5 )
        her "A broom...?"
        $herView.hideshowQQ( "body_07.png", pos )
        her "Hm..."
        $herView.hideshowQQ( "body_05.png", pos )
        her "It's a sex-toy of some sort, isn't it?"
        $herView.hideshowQQ( "body_87.png", pos )
        her "But it is so well crafted..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">You give the broom to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_120.png", pos )
        her "Thank you, sir."
        call happy
        
        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 30
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_118.png", pos, d5 )
        her "A broom...?"
        her "Hm..."
        $herView.hideshowQQ( "body_66.png", pos )
        her "What kind of saddle is that...?"
        $herView.hideshowQQ( "body_127.png", pos )
        her "Well, doesn't matter."
        her "Refusing an expensive gift like that would be rude..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">You give the broom to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_120.png", pos )
        her "Thank you, sir."
        call happy

    if hermi.whoring >= 18: # Lv 7+  
        $ hermi.liking += 30
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_124.png", pos, d5 )
        her "A broom..."
        her "Hm..."
        $herView.hideshowQQ( "body_189.png", pos )
        her "That saddle, sir..."
        $herView.hideshowQQ( "body_190.png", pos )
        her "It was designed especially for witches, was it not?"
        $herView.hideshowQQ( "body_185.png", pos )
        her "I am not sure whether this is inappropriate or clever..."
        $herView.hideshowQQ( "body_129.png", pos )
        her "But this is a brilliant piece of engineering eitherway..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">You give the broom to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_128.png", pos )
        her "Thank you, sir."
        call happy


    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                
        
    ### KRUM POSTER ###
label giving_krum: 
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.showQ( "body_73.png", pos, d5 )
        her "A Quidditch poster?"
        $herView.hideshowQQ( "body_185.png", pos )
        her "What am I supposed to do with it, sir?"
        $herView.hideshowQQ( "body_184.png", pos )
        her "No, thank you."
        call no_change
        $herView.addFaceName( "body_71.png" )


    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $ hermi.liking += 1
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_73.png", pos, d5 )
        her "A Quidditch poster?"
        $herView.hideshowQQ( "body_185.png", pos )
        her "Hm..."
        $herView.hideshowQQ( "body_71.png", pos )
        her "I think I saw this player once or twice..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "He is that Durmstrang student, right?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">You give the poster to Hermione..."
        hide screen gift
        with d3
        call happy
        

        
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $ hermi.liking += 15
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_73.png", pos, d5 )
        her "A Viktor Krum poster, sir?"
        $herView.hideshowQQ( "body_08.png", pos )
        her "Can't say that I care much for Quidditch, but..."
        $herView.hideshowQQ( "body_87.png", pos )
        her "I can see why the girls find the brutish physique of some players appealing..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">You give the poster to Hermione..."
        hide screen gift
        with d3
        call happy
        
        
       
    if hermi.whoring >= 18: # Lv 7+  
        $ hermi.liking += 25
        $hermi.Items.Receive(hero.Items,item.Name) #        
        $herView.showQ( "body_72.png", pos, d5 )
        her "A Viktor Krum poster?!"
        $herView.hideshowQQ( "body_24.png", pos )
        her "Thank you, sir!"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">You give the poster to Hermione..."
        hide screen gift
        with d3
        $herView.showQQ( "body_46.png", pos )
        her "Can't wait to hang it over my bed!"
        $herView.hideshowQQ( "body_64.png", pos )
        her "The girls will go green with envy..."
        call happy


    $ pos = POS_370
    jump hermione_main_menu                    
        
        
        
        
        
     ### S.P.E.W. BADGE ###
label giving_badge_01: 
    $herView.hideQ( d5 )
    $ wrd_new_items += 1
    $ pos = POS_140

    $ hermi.liking += 30
    $hermi.Items.Receive(hero.Items,item.Name) #        
    $herView.showQ( "body_01.png", pos, d5 )
    her "A badge?"
    $herView.hideQQ()
    $ the_gift = "03_hp/18_store/29.png" # S.P.E.W. BADGE.
    show screen gift
    with d3
    ">You give the badge to Hermione...\n>The \"S.P.E.W. badge has been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $herView.showQQ( "body_06.png", pos )
    her "Thank you, sir."
    call happy


    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                    
            
        
        
        
    ### FISHNET STOCKINGS ###
label giving_nets: 
    $herView.hideQ( d5 )
    $ wrd_new_items += 1
    $ pos = POS_140

    $ hermi.liking += 30
    $hermi.Items.Receive(hero.Items,item.Name) #        
    $herView.showQ( "body_03.png", pos, d5 )
    her "A pair of stockings?"
    $herView.hideQQ()
    $ the_gift = "03_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">You give the stockings to Hermione...\n>Fishnet stockings have been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $herView.showQQ( "body_04.png", pos )
    her "Thank you, sir."
    call happy
    
    $herView.addFaceName( "body_03.png" )

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu                    
            
   
label giving_tights: 
    $herView.hideQ( d5 )
    $ wrd_new_items += 1
    $ pos = POS_140

    $ hermi.liking += 30
    $hermi.Items.Receive(hero.Items,item.Name) #        
    $herView.showQ( "body_03.png", pos, d5 )
    her "Колготки ?"
    $herView.hideQQ()
    $ the_gift = "03_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">Вы даете Гермионе колготки..."
    hide screen gift

    $ dress_code = True

    $herView.showQQ( "body_04.png", pos )
    her "Спасибо, сэр."
    call happy
    
    $herView.addFaceName( "body_03.png" )

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump hermione_main_menu        
    
        
        
    label happy:
        $herView.hideQQ()
#        if mad <= 0:
#            $ mad = 0
        $Say([">The Hermione's mood improved...\n>Hermione {size=+5}upset you{/size}...", 
              ">The Hermione's mood improved...\n>Hermione {size=+5}not mad{/size} on you...",
              ">The Hermione's mood improved...\n>Hermione {size=+5}you pleasant{/size}..."][Sign(hermi.liking)+1])
        return



    label no_change:
        $herView.hideQQ()
        ">Hermione's mood didn't change much..."
        return
        
    label upset:
        $herView.hideQQ()
        ">Hermione's mood worsened...\n>Hermione is {size=+5}upset{/size} with you..."
        return
        
        
label giving_shortskirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"shortskirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали укороченную школьную юбку Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu

    
label giving_xshortskirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"xshortskirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали сильно укороченную школьную юбку Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu
    
    
label giving_xxshortskirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"xxshortskirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали короткую школьную юбку Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu
    
    
label giving_xsmallskirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"xsmallskirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали школьную мини-юбку Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu
    
    
label giving_xxsmallskirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"xxsmallskirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали укороченную школьную мини-юбку Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu    
  
    
label giving_skirt_cheerleader:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"skirt_cheerleader")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали юбку болельщицы Гриффиндора Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu 
    
    
label giving_skirt_business:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"skirt_business")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали миниюбку бизнес-вумен Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu 
    
    
label giving_skimpyshirt:
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"skimpyshirt")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали школьную рубашку-минитопик Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Рубашка ? У нее какой-то странный размер."
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu   
    
label giving_shirt_business :
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"shirt_business")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали белую рубашку в деловом стиле Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Рубашка ?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu  
    
label giving_shirt_cheerleader :
    $ dress_code = True # Turns TRUE when you gift the xxxsmallskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ wrd_new_items += 1

    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"shirt_cheerleader")

    $ hermi.liking = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали кофту болельщицы Гриффиндора Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Кофта ?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump hermione_main_menu 
    
### DR'S Wardrobe

label wrd_badge_01_first_dress :
    $ wrd_new_items -= 1
    $ wrd_badge_01 = 1

    $herView.hideQQ()

    $ pos = POS_370
    $herView.showQQ( "body_01.png", pos )
    her "Конечно, сэр..."
    ""
    
    jump wrd_badge_01_dress

    
label wrd_nets_first_dress :

    $ pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_11.png", pos )
        her "Ажурные чулки...?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "Вы, должно быть, не серьезно, сэр!"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "С радостью..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, хорошо..."
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset
        
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Я не из таких девушек, сэр..."
        her "Попытайте удачу с одной из \"Слизеринских\" шлюх..."
        menu:
            m "..."
            "\"Просто надень это!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, это врядли соответствует форме студента Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, раз так..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Ажурные чулки?"
        $herView.hideshowQQ( "body_29.png", pos )
        her "Я не уверена насчет этого, сэр..."
        menu:
            m "..."
            "\"Просто надень их!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, Ладно..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        

    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Если вы настаиваете, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_nets = 1
    jump wrd_nets_dress
    
label wrd_tights_first_dress :

    $ pos = POS_370
    $herView.hideshowQQ( "body_02.png", pos )
    her "Колготки, сэр ?"
    her "Это довольно неожиданно."
    if hermi.whoring <= 12 and hermi.whoring >= 3 :
        her "(Интересно, в чем тут подвох ?)"
    $herView.hideshowQQ( "body_07.png", pos )
    her "Мне кажется, что они не относятся к обычной форме ученицы..."
    her "С другой стороны, тут нет ничего плохого."

    $ wrd_new_items -= 1
    $ wrd_tights = 1
    jump wrd_tights_dress

label wrd_shortskirt_first_dress :

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Это короткая юбка?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_shortskirt = 1
    jump wrd_shortskirt_dress

label wrd_xshortskirt_first_dress :

    if wrd_shortskirt == 0 :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка еще короче прежней?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она еще короче..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_xshortskirt = 1
    jump wrd_xshortskirt_dress

    
label wrd_xxshortskirt_first_dress :

    if wrd_xshortskirt == 0 :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка еще короче прежней?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 14
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она еще короче..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 7
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )


    $ wrd_new_items -= 1
    $ wrd_xxshortskirt = 1
    jump wrd_xxshortskirt_dress

    
label wrd_xsmallskirt_first_dress :

    if wrd_xxshortskirt == 0 :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой жалкой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                $ hermi.liking -= 5
                call upset
                jump hermione_main_menu
            "\"Я дам тебе 35 очков.\"":
                $herView.hideshowQQ( "body_21.png", pos )
                her "{size=+3}Засуньте себе свои очки в ...{/size}"
                $herView.hideshowQQ( "body_33.png", pos )
                her "Простите, сэр."
                her "Я хочу сказать, что отказываюсь !"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset
                jump hermione_main_menu
    
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта мини-юбка совсем коротенькая!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Из под нее всем будут видны мои трусики !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 35 очков.\"":
                her "........................"
                her "..............................."
                her "Этого мало, сэр !"
                
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"45 очков ?\"" :
                        $ gryffindor +=45
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Чувствую, что я еще пожалею об этом..."
                        her "(Нужно будет поменьше наклоняться.)"
                        $herView.hideQQ()
                        $ hermi.liking -= 16
                        call upset
                    
        
        

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она совсем коротенькая..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 12
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 35 очков.\"":
                $ gryffindor +=35
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 18 and hermi.whoring <= 20: # Lv 7.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она совсем коротенькая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 35 очков.\"":
                $ gryffindor +=35
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 21: # Lv 8+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )


    $ wrd_new_items -= 1
    $ wrd_xsmallskirt = 1
    jump wrd_xsmallskirt_dress

label wrd_xxsmallskirt_first_dress :

    if wrd_xsmallskirt == 0 :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Да это и юбкой-то назвать нельзя!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370

    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой жалкой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Это абсолютно неприемлимо !"
        $ hermi.liking -= 18
        call upset
        jump hermione_main_menu
    
    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой жалкой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Это исключено !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()         
                $ hermi.liking -= 8
                call upset
                jump hermione_main_menu
            "\"Я дам тебе 50 очков.\"":
                $herView.hideshowQQ( "body_21.png", pos )
                her "{size=+3}Засуньте себе свои очки в ...{/size}"
                $herView.hideshowQQ( "body_33.png", pos )
                her "Простите, сэр."
                her "Я хочу сказать, что категорически отказываюсь !"
                $herView.hideQQ()
                $ hermi.liking -= 8
                call upset
                jump hermione_main_menu
    
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта мини-юбка совсем крошечная!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Из под нее мои трусики будут видны из другого конца коридора!"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 50 очков.\"":
                her "........................"
                her "..............................."
                her "Этого мало, сэр !"
                
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"70 очков ?\"" :
                        $ gryffindor +=70
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Уверена, что я еще пожалею об этом..."
                        her "(Ох... Что же я делаю...)"
                        $herView.hideQQ()
                        $ hermi.liking -= 20
                        call upset
                    
        
        

    if hermi.whoring >= 18 and hermi.whoring <= 20: # Lv 7.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Как... ?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она короткая-прекороткая..."
        her "Я хочу сказать, у всего же должен быть предел !"
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, это однозначно не соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 16
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 50 очков.\"":
                $ gryffindor +=50
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 21 : # Lv 8.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Но она же..."
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она совсем, совсем коротенькая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Как скажете, сэр"
            "\"Я дам тебе 50 очков.\"":
                $ gryffindor +=50
                $herView.hideshowQQ( "body_07.png", pos )
                her "Ох-хо-хо"
                $herView.hideshowQQ( "body_68.png", pos )
                her "Да, сэр."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Да, сэр"
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu


    $ wrd_new_items -= 1
    $ wrd_xxsmallskirt = 1
    jump wrd_xxsmallskirt_dress

label wrd_xxxsmallskirt_first_dress :

    if wrd_xxsmallskirt == 0 :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы издеваетесь, сэр?!"
        her "Да это и юбкой-то назвать нельзя!"
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить юбку подлиннее.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        jump hermione_main_menu

    $pos = POS_370

    if hermi.whoring >= 0 and hermi.whoring <= 11: # Lv 1-4
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этом клочке материи ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Да им даже с доски не сотрешь !"
        her "Нет, это невозможно !"
        $ hermi.liking -= 25
        call upset
        jump hermione_main_menu
    
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этом клочке материи ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Это исключено !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                $ hermi.liking -= 10
                call upset
                jump hermione_main_menu
            "\"Я дам тебе 80 очков.\"":
                $herView.hideshowQQ( "body_21.png", pos )
                her "{size=+3}Засуньте себе свои очки в ...{/size}"
                $herView.hideshowQQ( "body_33.png", pos )
                her "Простите, сэр."
                her "Я хочу сказать, что категорически отказываюсь !"
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
                jump hermione_main_menu
    
    if hermi.whoring >= 18 and hermi.whoring <= 23: # Lv 7-8
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка микроскопическая!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Из под нее мои трусики будут видны из другого здания!"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 80 очков.\"":
                her "........................"
                her "..............................."
                her "Этого мало, сэр !"
                
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"100 очков ?\"" :
                        $ gryffindor +=100
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Уверена, что я еще пожалею об этом..."
                        her "(Не могу поверить, что я на это иду...)"
                        $herView.hideQQ()
                        $ hermi.liking -= 25
                        call upset
                    
        
        

    if hermi.whoring >= 24 : # Lv Max.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Как... ?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она микроскопическая"
        her "Я хочу сказать, у всего же должен быть предел !"
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, это немыслимо для Хогвартса!"
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 20
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 80 очков.\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Мммммм"
                $herView.hideshowQQ( "body_08.png", pos )
                her "Мне трудно решиться..."
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"100 очков ?\"" :
                        $ gryffindor +=100
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Постараюсь смириться."
                        her "(Не могу поверить, что я на это иду...)"
                        $herView.hideQQ()
                        call upset
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    $ wrd_new_items -= 1
    $ wrd_xxxsmallskirt = 1
    jump wrd_xxxsmallskirt_dress
    
label wrd_skirt_cheerleader_first_dress :

    if nsp_event_kviddich_1 < 1 or hermi.whoring < 9 or nsp_germiona_mediawhoring < 10 or nsp_germiona_impudence < 0 :
        $herView.hideshowQQ( "body_02.png", pos )
        her "Сэр, я не болельщица, не люблю болельщиц и не вижу смысла одеваться как одна из них !"
        her "Поэтому мой окончательный ответ - нет."
        m "(Похоже, для начала нужно будет приучить ее воспринимать себя по-другому.)"
        m "Хорошо, не буду настаивать."
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка слишком короткая?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 10
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она слишком короткая !"
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_skirt_cheerleader = 1
    jump wrd_skirt_cheerleader_dress
    
label wrd_skirt_business_first_dress :

    if nsp_event_magls_1 < 1 or hermi.whoring < 9 or nsp_germiona_mediawhoring < 10 or nsp_germiona_impudence < 0 :
        $herView.hideshowQQ( "body_02.png", pos )
        her "Сэр, я не магл, кто бы что ни говорил. Зачем давать лишний повод ?"
        her "Поэтому мой окончательный ответ - нет."
        m "(Похоже, для начала нужно будет приучить ее воспринимать себя по-другому.)"
        m "Хорошо, не буду настаивать."
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 5: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта юбка недопустимо коротка !"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ hermi.liking -= 14
                call upset
        
        

    if hermi.whoring >= 6 and hermi.whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 7
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu

    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )


    $ wrd_new_items -= 1
    $ wrd_skirt_business = 1
    jump wrd_skirt_business_dress

label wrd_standart02_first_dress :

    if hermi.whoring >= 0 and hermi.whoring <= 8:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но это не соответствует форме Хогвартса."
        menu:
            m "..."
            "\"Я дам тебе 10 очков.\"":
                $ gryffindor +=10
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 9:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_standart02 = 1
    jump wrd_standart02_dress

    
label wrd_standart03_first_dress :

    if hermi.whoring >= 0 and hermi.whoring <= 11:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но это не соответствует форме Хогвартса."
        menu:
            m "..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 12:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_standart03 = 1
    jump wrd_standart03_dress

label wrd_standart04_first_dress :

    if hermi.whoring >= 0 and hermi.whoring <= 14:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но это не соответствует правилам Хогвартса."
        menu:
            m "..."
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 15:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_standart04 = 1
    jump wrd_standart04_dress

label wrd_standart05_first_dress :

    if hermi.whoring >= 0 and hermi.whoring <= 20:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Сэр ?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Вы же это не серьезно ? Ведь все-таки тут школа."
        menu:
            m "..."
            "\"Я дам тебе 25 очков.\"":
                $ gryffindor +=25
                $herView.hideshowQQ( "body_07.png", pos )
                her "О, сэр."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я постараюсь к этому привыкнуть."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 21:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_standart05 = 1
    jump wrd_standart05_dress

label wrd_skimpyshirt_first_dress :

    if wrd_standart05 == 0 :
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы шутите, сэр?!"
        her "Да это не рубашка, а сплошной разврат."
        her "Я не стану показываться на людях в таком виде!"
        m "(Похоже, для начала нужно будет предложить ей менее оьткровенные варианты.)"
        m "Прежде, чем ты продолжишь, хочу заметить, что я просто пошутил."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Лучше бы это и вправду была шутка, профессор!"
        jump hermione_main_menu

    $pos = POS_370

    if hermi.whoring >= 0 and hermi.whoring <= 11: # Lv 1-4
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Да ей даже с доски не сотрешь !"
        her "Нет, это невозможно !"
        $ hermi.liking -= 15
        call upset
        jump hermione_main_menu
    
    if hermi.whoring >= 12 and hermi.whoring <= 17: # Lv 5-6
        $herView.hideshowQQ( "body_04.png", pos )
        her "Сэр, как вы можете просить меня ходить по школе в этой тряпочке ?!"
        her "Может быть в следующий раз я должна буду пойти на урок голой ?!"
        m "(Мне нравится ход ее мыслей.)"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Это исключено !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                $ hermi.liking -= 5
                call upset
                jump hermione_main_menu
            "\"Я дам тебе 40 очков.\"":
                $herView.hideshowQQ( "body_21.png", pos )
                her "{size=+3}Засуньте себе свои очки в ...{/size}"
                $herView.hideshowQQ( "body_33.png", pos )
                her "Простите, сэр."
                her "Я хочу сказать, что категорически отказываюсь !"
                $herView.hideQQ()
                $ hermi.liking -= 5
                call upset
                jump hermione_main_menu
    
    if hermi.whoring >= 18 and hermi.whoring <= 20: # Lv 7-8
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта рубашка слишком откровенная!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Мои буф... мою грудь будет видно всем !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 40 очков.\"":
                her "........................"
                her "..............................."
                her "Этого мало, сэр !"
                
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"40 очков ?\"" :
                        $ gryffindor +=50
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Уверена, что я еще пожалею об этом..."
                        her "(Не могу поверить, что я на это иду...)"
                        $herView.hideQQ()
                        $ hermi.liking -= 20
                        call upset
                    
        
        

    if hermi.whoring >= 21 and hermi.whoring <= 23: # Lv 7-8
        $herView.hideshowQQ( "body_15.png", pos )
        her "Эта рубашка такая открытая... ?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "И совсем маленькая!"
        her "Сэр, вы уверены, что мне нужно это делать ?"
        her "Мне кажется, это плохая идея..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, заставлять меня делать это недопустимо!"
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ hermi.liking -= 15
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 40 очков.\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Мммммм"
                $herView.hideshowQQ( "body_08.png", pos )
                her "Мне трудно решиться..."
                menu:
                    "\"Ладно. Забудь.\"":
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "С удовольствием..."
                        $herView.hideQQ()
                        $herView.showQQ( None, pos )
                        jump hermione_main_menu
                    "\"50 очков ?\"" :
                        $ gryffindor +=50
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ох... ладно..."
                        her "Постараюсь смириться."
                        her "(Не могу поверить, что я на это иду...)"
                        $herView.hideQQ()
                        call upset
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
                
    if hermi.whoring >= 24 : # Lv Max.                
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_skimpyshirt = 1
    jump wrd_skimpyshirt_dress
    
label wrd_shirt_cheerleader_first_dress :

    if nsp_event_kviddich_1 < 1 or hermi.whoring < 9 or nsp_germiona_mediawhoring < 10 or nsp_germiona_impudence < 0 :
        $herView.hideshowQQ( "body_02.png", pos )
        her "Сэр, я не болельщица, не люблю болельщиц и не вижу смысла одеваться как одна из них !"
        her "Поэтому мой окончательный ответ - нет."
        m "(Похоже, для начала нужно будет приучить ее воспринимать себя по-другому.)"
        m "Хорошо, не буду настаивать."
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu

    $pos = POS_370
    if hermi.whoring >= 0 and hermi.whoring <= 17: # Lv 1-2
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Эта кофта слишком открытая !"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она не полностью прикрывает мои буф... мою... мой бюст !"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump hermione_main_menu
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
        
    
    if hermi.whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_shirt_cheerleader = 1
    jump wrd_shirt_cheerleader_dress
    
    
label wrd_shirt_business_first_dress :

    if nsp_event_magls_1 < 1 or hermi.whoring < 9 or nsp_germiona_mediawhoring < 10 or nsp_germiona_impudence < 0 :
        $herView.hideshowQQ( "body_02.png", pos )
        her "Сэр, я не магл, кто бы что ни говорил. Зачем давать лишний повод ?"
        her "Поэтому мой окончательный ответ - нет."
        m "(Похоже, для начала нужно будет приучить ее воспринимать себя по-другому.)"
        m "Хорошо, не буду настаивать."
        $herView.hideshowQQ( "body_01.png", pos )
        jump hermione_main_menu


    if hermi.whoring >= 0 and hermi.whoring <= 14:
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но это не соответствует правилам Хогвартса."
        menu:
            m "..."
            "\"Я дам тебе 20 очков.\"":
                $ gryffindor +=20
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Как скажете."
                $herView.hideshowQQ( None, pos )
                jump hermione_main_menu
        
    
    if hermi.whoring >= 15:
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )

    $ wrd_new_items -= 1
    $ wrd_shirt_business = 1
    jump wrd_shirt_business_dress

    
label wrd_nobadge_dress :
    call wrd_badges_undress
    call wrd_dress_change
    jump hermione_main_menu

label wrd_badge_01_dress :
    call wrd_badges_undress
    $ wrd_badge_01 = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_nonets_dress :
    call wrd_nets_undress
    call wrd_dress_change
    jump hermione_main_menu

label wrd_nets_dress :
    call wrd_nets_undress
    $ wrd_nets = 1
    call wrd_dress_change
    jump hermione_main_menu
    
label wrd_tights_dress :
    call wrd_nets_undress
    $ wrd_tights = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_skirt_dress :
    call wrd_skirts_undress
    $ wrd_skirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_shortskirt_dress :
    call wrd_skirts_undress
    $ wrd_shortskirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_xshortskirt_dress :
    call wrd_skirts_undress
    $ wrd_xshortskirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_xxshortskirt_dress :
    call wrd_skirts_undress
    $ wrd_xxshortskirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_xsmallskirt_dress :
    call wrd_skirts_undress
    $ wrd_xsmallskirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_xxsmallskirt_dress :
    call wrd_skirts_undress
    $ wrd_xxsmallskirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_xxxsmallskirt_dress :
    call wrd_skirts_undress
    $ wrd_xxxsmallskirt = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_skirt_cheerleader_dress :
    call wrd_skirts_undress
    $ wrd_skirt_cheerleader = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_skirt_business_dress :
    call wrd_skirts_undress
    $ wrd_skirt_business = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_standart01_dress :
    call wrd_shirts_undress
    $ wrd_standart01 = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_standart02_dress :
    call wrd_shirts_undress
    $ wrd_standart02 = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_standart03_dress :
    call wrd_shirts_undress
    $ wrd_standart03 = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_standart04_dress :
    call wrd_shirts_undress
    $ wrd_standart04 = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_standart05_dress :
    call wrd_shirts_undress
    $ wrd_standart05 = 1
    call wrd_dress_change
    jump hermione_main_menu

label wrd_skimpyshirt_dress : 
    call wrd_shirts_undress
    $ wrd_skimpyshirt = 1  
    call wrd_dress_change 
    jump hermione_main_menu

label wrd_shirt_cheerleader_dress : 
    call wrd_shirts_undress
    $ wrd_shirt_cheerleader = 1  
    call wrd_dress_change
    jump hermione_main_menu

label wrd_shirt_business_dress : 
    call wrd_shirts_undress
    $ wrd_shirt_business = 1  
    call wrd_dress_change 
    jump hermione_main_menu       

    
label wrd_badges_undress :

    if wrd_badge_01 == 1 :
        $ wrd_badge_01 = 2
    return

label wrd_nets_undress :

    if wrd_nets == 1 :
        $ wrd_nets = 2
    if wrd_tights == 1 :
        $ wrd_tights = 2
    return

label wrd_skirts_undress :

    if wrd_skirt == 1 :
        $ wrd_skirt = 2
    if wrd_shortskirt == 1 :
        $ wrd_shortskirt = 2
    if wrd_xshortskirt == 1 :
        $ wrd_xshortskirt = 2
    if wrd_xxshortskirt == 1 :
        $ wrd_xxshortskirt = 2
    if wrd_xsmallskirt == 1 :
        $ wrd_xsmallskirt = 2
    if wrd_xxsmallskirt == 1 :
        $ wrd_xxsmallskirt = 2
    if wrd_xxxsmallskirt == 1 :
        $ wrd_xxxsmallskirt = 2
    if wrd_skirt_cheerleader == 1 :
        $ wrd_skirt_cheerleader = 2
    if wrd_skirt_business == 1 :
        $ wrd_skirt_business = 2
    return

label wrd_shirts_undress :
    if wrd_standart01 == 1 :
        $ wrd_standart01 = 2
    if wrd_standart02 == 1 :
        $ wrd_standart02 = 2
    if wrd_standart03 == 1 :
        $ wrd_standart03 = 2
    if wrd_standart04 == 1 :
        $ wrd_standart04 = 2
    if wrd_standart05 == 1 :
        $ wrd_standart05 = 2
    if wrd_skimpyshirt == 1 :
        $ wrd_skimpyshirt = 2
    if wrd_shirt_cheerleader == 1 :
        $ wrd_shirt_cheerleader = 2
    if wrd_shirt_business == 1 :
        $ wrd_shirt_business = 2
    return

label wrd_dress_undress :

    call wrd_dress_undress_skirts
    call wrd_dress_undress_shirts
    call wrd_dress_undress_stockings
    call wrd_dress_undress_badge

    return
    
label wrd_dress_undress_skirts :

    $ herView.data().delItem( 'item_skirt' )
    $ herView.data().delItem( 'item_skirts_skirt02_short' )
    $ herView.data().delItem( 'item_skirts_skirt03_xshort' )
    $ herView.data().delItem( 'item_skirts_skirt04_xxshort' )
    $ herView.data().delItem( 'item_skirts_skirt05_xsmall' )
    $ herView.data().delItem( 'item_skirts_skirt06_xxsmall' )
    $ herView.data().delItem( 'item_skirts_skirt07_xxxsmall' )
    $ herView.data().delItem( 'item_skirts_skirt_business' )
    $ herView.data().delItem( 'item_skirts_cheerleader_gryffindor' )

    return
    
label wrd_dress_undress_shirts :

    $ herView.data().delItem( 'item_tits' )
    $ herView.data().delItem( 'item_tits_no' )

    $ herView.data().delItem( 'item_dress' )
    $ herView.data().delItem( 'item_shirts_standard02_untucked_tie' )
    $ herView.data().delItem( 'item_shirts_standard03_untucked' )
    $ herView.data().delItem( 'item_shirts_standard04_untucked_unbuttoned' )
    $ herView.data().delItem( 'item_shirts_standard05_untucked_unbuttoned_double' )
    $ herView.data().delItem( 'item_shirts_standard06_skimpy_tied' )
    $ herView.data().delItem( 'item_shirts_blouse_business' )
    $ herView.data().delItem( 'item_shirts_cheerleader_gryffindor' )

    return
    
label wrd_dress_undress_stockings :

    $ herView.data().delItem( 'item_nets' )
    $ herView.data().delItem( 'item_stockings_tights' )

    return
    
label wrd_dress_undress_badge :

    $ herView.data().delItem( 'item_badge' )

    return
    
label wrd_dress_change :

    $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
    
    call wrd_dress_change_silent

    $herView.hideshowQQ( "body_01.png", pos )
    
    pause.5
    $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
    $screens.Show("ctc").Pause().Hide("ctc")
    
    return
    
label wrd_dress_change_silent :
    
    call wrd_dress_undress
    
    if wrd_tits == 1 :
        $ herView.data().addItem( 'item_tits' )
    if wrd_tits_no == 1 :
        $ herView.data().addItem( 'item_tits_no' )   
    
    if wrd_badge_01 == 1 :
        $ herView.data().addItem( 'item_badge' )
        
    if wrd_nets == 1 :
        $ herView.data().addItem( 'item_nets' )
    if wrd_tights == 1 :
        $ herView.data().addItem( 'item_stockings_tights' )

    if wrd_skirt == 1 :
        $ herView.data().addItem( 'item_skirt' )
    if wrd_shortskirt == 1 :
        $ herView.data().addItem( 'item_skirts_skirt02_short' )
    if wrd_xshortskirt == 1 :
        $ herView.data().addItem( 'item_skirts_skirt03_xshort' )
    if wrd_xxshortskirt == 1 :
        $ herView.data().addItem( 'item_skirts_skirt04_xxshort' )
    if wrd_xsmallskirt == 1 :
        $ herView.data().addItem( 'item_skirts_skirt05_xsmall' )
    if wrd_xxsmallskirt == 1 :
        $ herView.data().addItem( 'item_skirts_skirt06_xxsmall' )
    if wrd_xxxsmallskirt == 1 :
        $ herView.data().addItem( 'item_skirts_skirt07_xxxsmall' )
    if wrd_skirt_business == 1 :
        $ herView.data().addItem( 'item_skirts_skirt_business' )
    if wrd_skirt_cheerleader == 1 :
        $ herView.data().addItem( 'item_skirts_cheerleader_gryffindor' )
    
    if wrd_standart01 == 1 :
        $ herView.data().addItem( 'item_dress' )
    if wrd_standart02 == 1 :
        $ herView.data().addItem( 'item_shirts_standard02_untucked_tie' )
    if wrd_standart03 == 1 :
        $ herView.data().addItem( 'item_shirts_standard03_untucked' )
    if wrd_standart04 == 1 :
        $ herView.data().addItem( 'item_shirts_standard04_untucked_unbuttoned' )
    if wrd_standart05 == 1 :
        $ herView.data().addItem( 'item_shirts_standard05_untucked_unbuttoned_double' )
    if wrd_skimpyshirt == 1 :
        $ herView.data().addItem( 'item_shirts_standard06_skimpy_tied' )
    if wrd_shirt_business == 1 :
        $ herView.data().addItem( 'item_shirts_blouse_business' )
    if wrd_shirt_cheerleader == 1 :
        $ herView.data().addItem( 'item_shirts_cheerleader_gryffindor' )
    
    return

    
    