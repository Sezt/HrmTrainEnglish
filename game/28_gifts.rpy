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



label giving_miniskirt:
    $ dress_code = True # Turns TRUE when you gift the miniskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
#    $ have_miniskirt = False # Turns TRUE when you have the skirt in your possession.
#    $ gave_miniskirt = True #Turns True when Hermione has the miniskirt.
    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    $hermi.Items.Receive(hero.Items,"miniskirt")

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
            
   
    
    
        
        
    label happy:
        $herView.hideQQ()
#        if mad <= 0:
#            $ mad = 0
        if hermi.liking == 0:
            ">Hermione's mood has improved...\n>Hermione is {size=+5}not upset{/size} with you..."
        else:
            ">Hermione's mood has improved...\n>Hermione is {size=+5}still upset{/size} with you..."
        return



    label no_change:
        $herView.hideQQ()
        ">Hermione's mood didn't change much..."
        return
        
    label upset:
        $herView.hideQQ()
        ">Hermione's mood worsened...\n>Hermione is {size=+5}upset{/size} with you..."
        return
        
        


