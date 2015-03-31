label snape_tutor_1:
    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    show screen fireplace_fire
    hide screen genie
    hide screen chair
    hide screen desk
    show screen desk
    
    hide screen snape_02 #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3

    
    with fade
    $ fire_in_fireplace = True
    
    show screen bld1
    with d3
    m "... speaking of Granger girl..."
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen s_head2      
    sna2 "..."   #snape
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2 
    sna2 "But the evening promised to be a pleasant..."    #snape
    sna2 "What she got this time?" #snape
    hide screen s_head2
    m "I'm afraid I can't teach her."
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                         # SNAPE
    show screen s_head2
    sna2 "Ha! Now you know what I mean!" #snape
    sna2 "I bet you did not last ten minutes." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2
    sna2"Although I can understand you. And even a little sympathy..." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_08.png"                                         # SNAPE
    show screen s_head2
    sna2 "Damn, she again tomorrow \"defense against the dark arts\"." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                         # SNAPE
    show screen s_head2
    sna2 "Pour me another." #snape
    hide screen s_head2
    m "I didn't say give up."
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen s_head2
    sna2 "Hm?" #snape
    hide screen s_head2
    m "The problem is that anything I can't teach."
    m "You know, I don't have to teach her anything worthwhile."
    m "But I should at least pretend to have something useful."
    m "I'm afraid that the trick with Finch won't work twice."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2
    sna2 "\"The trick Finch\"?" #snape
    hide screen s_head2
    m "... you don't want to know, trust me."
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen s_head2
    sna2 "Хм." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2
    sna2 "In General, you mean me to be your tutor?" #snape
    hide screen s_head2
    m "Look, I am not thrilled."
    m "But if I teach it, it will greatly simplify our task with you."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2
    sna2 "Yes, I get it, got it." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen s_head2
    sna2 "Hmm..."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2
    sna2 "However, we can go the other way." #snape
    hide screen s_head2
    m "How, I wonder?"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2
    sna2 "Nerd potion." #snape
    hide screen s_head2
    m "..."
    g4 "You called me a nerd?"
    g4 "YOU FUCKING CALLED ME A NERD??!"
    g4 "YES, I WORE GLASSES, AND WAS ALWAYS SITTING BEHIND BOOKS, BUT THAT IS NO REASON TO CALL ME \"THE NERD\"!!!"
    g4 "AND WHERE ARE NOW THOSE OF PITCHING THAT GRABBED MY GARTER?! I BET LICK ANUS SOME GREASY WIFE OF THE SULTAN!"
    g4 "AND EVEN THE SULTAN HIMSELF!"
    g4 "AND I FUCK IN ALL HOLES FUCKING PRINCESS OF AGRABAH!!!"
    g4 "NOW WHO'S THE LOSER??!"
    $ s_sprite = "03_hp/10_snape_main/snape_11.png"                                         # SNAPE
    show screen s_head2
    sna2 "..." # snape
    hide screen s_head2
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_11.png"                                         # SNAPE
    show screen s_head2
    sna2 "..." # snape
    hide screen s_head2
    m ".. You said {i}forbidden word{/i}?"
    $ s_sprite = "03_hp/10_snape_main/snape_11.png"                                         # SNAPE
    show screen s_head2
    sna2 "\"Forbidden word\"?" # snape
    hide screen s_head2
    m "Yes, the letter \"n\"."
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2
    sna2 "You mean..." # snape
    hide screen s_head2
    g4 "SHUT up!!!"
    m "There are scars that do not heal even after nine thousand years."
    m "Just don't mention {i}is{/i} the word aloud, and we should be fine, right?"
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                         # SNAPE
    show screen s_head2
    sna2 "You know, it sounds funny." #snape
    hide screen s_head2
    g4 "Kill." #поставить маленький шрифт, сейчас мне лень
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2
    sna2 "Okay, 't be offended. Not to say the word with the letter \"n\", okay." #snape
    hide screen s_head2
    m "That's nice. So what were we talking about?"
    $ s_sprite = "03_hp/10_snape_main/snape_23.png"                                         # SNAPE
    show screen s_head2
    sna2 "In General, there is... a potion that can help you." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2
    sna2 "Just drink it, and you will be able to learn the whole school program for the night" #snape
    hide screen s_head2
    g9 "Sounds cheat."
    m "What is a meaning in all this school if all you can learn literally overnight?"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2
    sna2 "Well, first of all, most of the ingredients are very rare and they need a lot of damn money." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen s_head2
    sna2 "Secondly, the process of cooking a damn complicated." #snape
    sna2 "Oh, and third, the very famous recipe is not for everyone." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_02.png" 
    sna2 "Judge for yourself - if people find out the recipe, then nobody will need schools, and this sea of lost money." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    sna2 "In fact, almost the entire economy of the mages kept on magic schools." #snape
    hide screen s_head2
    m "Okay, okay, I get it. Big shots don't want this potion has become a popular."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2
    sna2 "Exactly." #snape
    hide screen s_head2
    m "So all I need is to buy the ingredients, right?"
    $ s_sprite = "03_hp/10_snape_main/23.png"                                         # SNAPE
    show screen s_head2
    sna2 "Exactly." #snape
    hide screen s_head2
    m "The beauty of it. As if this game had a few issues."
    m "And how expensive is this joy?"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2
    sna2 "Well... Some of prohibited ingredients, so I will have to attract their channels..." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_23.png"
    sna2 "So, I think, ten thousand." #snape
    show screen s_head2
    m "..."
    m "You threw yourself a couple of thousand, Yes?"
    $ s_sprite = "03_hp/10_snape_main/snape_30.png"                                         # SNAPE
    show screen s_head2
    sna "How could you think that?!" #snape
    $ s_sprite = "03_hp/10_snape_main/snape_27.png"                                         # SNAPE
    show screen s_head2
    sna2 "We're friends..." #snape
    hide screen s_head2
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_27.png"                                         # SNAPE
    show screen s_head2
    sna2 "..." #snape
    hide screen s_head2
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2
    sna2 "Okay, eight thousand." #snape
    hide screen s_head2
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen s_head2
    sna2 "Look, I can't throw." #snape
    hide screen s_head2
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                         # SNAPE
    show screen s_head2
    sna "..." #snape
    hide screen s_head2
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2
    sna2 "Seven thousand. My last word." #snape
    hide screen s_head2
    g9 "Gorgeous! Agreed."
    "Job updated! To get seven thousand galleons for Snape."
    m "Only it's still pretty damn healthy heap of gold."
    g9 "I think I need to look for a job on the side."
    g9 "Rumor has it that gigolo is well earned..."
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen s_head2
    sna2 "You cannot leave this room and nobody needs to see, remember?" #snape
    m "..."
    m "Nerd."
    hide screen s_head2
    $ teacher_jinn_quest = 2
    stop music fadeout 1.0
    $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    else: 
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
    $ snape_busy = True
    hide screen snape_02 #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    jump day_start
    
label snape_tutor_2:
    #вступление пределать бы
    g9 "Here the gold for textbooks."
    $ renpy.play('sounds/money.mp3')
    $gold -=7000
    "You gave Snape 7000 galleons."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen snape_main  
    with d3 
    sna "Excellent! I will immediately make all the arrangements." #snape
    hide screen snape_main                                                                                                                   #SNAPE
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen snape_main
    with d3 
    sna "Brew potions that level takes a heck of a lot of time and effort..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3             #snape
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen snape_main  
    with d3 
    sna "And it is very perishable. So keep books at the ready." #snape
    m "... books?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen snape_main  
    with d3 
    sna "Well, Yes. Textbooks." #snape
    m "And weren't you going to lend them to me for old time's sake?"
    sna "What makes you think that I am?" #snape
    m "Uh, well..." #jinnie
    g4 "Dammit." #jinnie
    hide screen snape_main                                                                                                                   #SNAPE
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen snape_main  
    with d3 
    sna "Even if I had lying around and a couple of old books on potions, it won't be enough." #snape
    m "Then any idea where to get them?" #jinnie
    sna "Well, usually in such cases go to Diagon alley, but..."
    m "But?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                         # SNAPE
    show screen snape_main
    with d3 
    sna "But I'm too busy, and you're not allowed to leave the tower."
    m "How about to send miss Granger carry bags with books, while we were sipping wine by the fireplace?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen snape_main
    with d3 
    sna "Don't work. Diagon alley far enough, and to transgressively on the territory of Hogwarts impossible."
    g9 "It's not that bad. Transvection was never a good idea, trust me on this."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen snape_main  
    with d3 
    sna "..?"
    m "In General, I'll try and work something out."
    "Quest updated: is it necessary to get textbooks"
    sna "Well, good luck."
    $ teacher_jinn_quest = 3
    $ snape_busy = True
    hide screen snape_02 #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    if daytime:
        jump day_main_menu
    else: 
        jump night_main_menu