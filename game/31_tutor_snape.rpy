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
    m "... speaking of the Granger girl..."
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen s_head2      
    sna2 "..."   #snape
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2 
    sna2 "But the evening promised to be pleasant..."    #snape
    sna2 "What is she doing this time?" #snape
    hide screen s_head2
    m "I'm afraid I can't teach her."
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                         # SNAPE
    show screen s_head2
    sna2 "Ha! Now you know what I mean!" #snape
    sna2 "I bet you did not last ten minutes." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2
    sna2 "Although I do understand you. And even have a little sympathy..." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_08.png"                                         # SNAPE
    show screen s_head2
    sna2 "Damn, she has \"defense against the dark arts\" again tomorrow." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                         # SNAPE
    show screen s_head2
    sna2 "Pour me another." #snape
    hide screen s_head2
    m "I didn't say that I give up."
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen s_head2
    sna2 "Hm?" #snape
    hide screen s_head2
    m "The problem is that I can't teach anything."
    m "You know, I don't have to teach her anything worthwhile."
    m "But I should at least pretend to have something useful."
    m "I'm afraid that Finch Trick won't work twice."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2
    sna2 "\"The Finch Trick\"?" #snape
    hide screen s_head2
    m "... you don't want to know, trust me."
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen s_head2
    sna2 "Hmm." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2
    sna2 "You are talking about being able to tutor her?" #snape
    hide screen s_head2
    m "Look, I am not thrilled."
    m "But if I could teach something, it would greatly simplify our task with her."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2
    sna2 "Yes, I get it." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen s_head2
    sna2 "Hmm..."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2
    sna2 "However, there is an easier route." #snape
    hide screen s_head2
    m "How, I wonder?"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2
    sna2 "Nerd potion." #snape
    hide screen s_head2
    m "..."
    g4 "You called me a nerd?"
    g4 "YOU FUCKING CALLED ME A NERD??!"
    g4 "YES, I WORE GLASSES, AND WAS ALWAYS SITTING BEHIND BOOKS, BUT THAT IS NO REASON TO CALL ME A \"NERD\"!!!"
    g4 "AND WHERE ARE THOSE BASTARDS THAT GAVE ME WEDGIES NOW?! I BET THEY LICK THE ANUS OF THE SULTANS GREASY WIFE!"
    g4 "AND EVEN THE SULTAN HIMSELF!"
    g4 "AND I FUCKED ALL THE HOLES OF THE FUCKING PRINCESS OF AGRABAH!!!"
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
    m ".. You said the {i}forbidden word{/i}?"
    $ s_sprite = "03_hp/10_snape_main/snape_11.png"                                         # SNAPE
    show screen s_head2
    sna2 "\"Forbidden word\"?" # snape
    hide screen s_head2
    m "Yes, the \"n-word\"."
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2
    sna2 "You mean..." # snape
    hide screen s_head2
    g4 "SHUT up!!!"
    m "There are scars that never heal even after nine thousand years."
    m "Just don't mention {i}that{/i} word aloud, and we should be fine, alright?"
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                         # SNAPE
    show screen s_head2
    sna2 "You know, it sounds funny." #snape
    hide screen s_head2
    g4 "Die." #поставить маленький шрифт, сейчас мне лень
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2
    sna2 "Okay, don't be offended. I am not going to say the \"n-word\", okay." #snape
    hide screen s_head2
    m "Okay then. So what were we talking about?"
    $ s_sprite = "03_hp/10_snape_main/snape_23.png"                                         # SNAPE
    show screen s_head2
    sna2 "There is... a potion that can help you." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2
    sna2 "Just drink it, and you will be able to learn the whole school program overnight" #snape
    hide screen s_head2
    g9 "Sounds cheat."
    m "What is the meaning of this school if you can learn everything literally overnight?"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2
    sna2 "Well, first of all, most of the ingredients are very rare and they cost a lot of damn money." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen s_head2
    sna2 "Secondly, the process of cooking it is damn complicated." #snape
    sna2 "Oh, and finally, the very powerfull recipe is not for everyone." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_02.png" 
    sna2 "Think about it - if people find out about the recipe, then nobody will need schools, and that is a lot of lost money." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    sna2 "In fact, almost the entire mage economy is kept going by magic schools." #snape
    hide screen s_head2
    m "Okay, okay, I get it. Big shots don't want this potion to become popular."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2
    sna2 "Exactly." #snape
    hide screen s_head2
    m "So all I need is to buy the ingredients, right?"
    $ s_sprite = "03_hp/10_snape_main/23.png"                                         # SNAPE
    show screen s_head2
    sna2 "Exactly." #snape
    hide screen s_head2
    m "Lovely. At last something that is straighforward."
    m "And how expensive is this wonder?"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2
    sna2 "Well... Some of the ingredients are prohibited, so I will have to use the right channels..." #snape
    $ s_sprite = "03_hp/10_snape_main/snape_23.png"
    sna2 "So, I would think, ten thousand." #snape
    show screen s_head2
    m "..."
    m "You can knock of a couple of thousand, right?"
    $ s_sprite = "03_hp/10_snape_main/snape_30.png"                                         # SNAPE
    show screen s_head2
    sna "Why would you think that?!" #snape
    $ s_sprite = "03_hp/10_snape_main/snape_27.png"                                         # SNAPE
    show screen s_head2
    sna2 "Because we are friends..." #snape
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
    sna2 "Look, I can't go any lower." #snape
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
    g9 "Beautiful! Agreed."
    "Job updated! Get seven thousand galleons for Snape."
    m "It's still a pretty damn big heap of gold."
    g9 "I think I need to look for a job on the side."
    g9 "Rumor has it that gigolos earn pretty well..."
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen s_head2
    sna2 "You cannot leave this room and nobody can see you, remember?" #snape
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
    g9 "Here is the money for the potion."
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
    sna "Brewing potions of that level take a heck of a lot of time and effort..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3             #snape
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen snape_main  
    with d3 
    sna "And it is very perishable. So keep your books at the ready." #snape
    m "... books?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen snape_main  
    with d3 
    sna "Well, Yes. Textbooks." #snape
    m "And weren't you going to lend them to me for old time's sake?"
    sna "What makes you think that I could do that?" #snape
    m "Uh, well..." #jinnie
    g4 "Dammit." #jinnie
    hide screen snape_main                                                                                                                   #SNAPE
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen snape_main  
    with d3 
    sna "Even if I didn't need them. I only have a couple of old books on potions, it won't be enough." #snape
    m "Any idea where I can get them?" #jinnie
    sna "Well, usually in such cases you go to Diagon alley, but..."
    m "But?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                         # SNAPE
    show screen snape_main
    with d3 
    sna "But I'm too busy, and you're not allowed to leave the tower."
    m "How about you send miss Granger to fetch the books, while we are sipping wine by the fireplace?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen snape_main
    with d3 
    sna "Won't work. Diagon alley is too far away, and teleportation on the Hogwarts grounds is impossible."
    g9 "Alright. Teleportation is never a good idea, trust me on this."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen snape_main  
    with d3 
    sna "..?"
    m "I'll try and work something out."
    "Quest updated: You need to get textbooks"
    sna "Well, good luck."
    $screens.Hide("snape_main")
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
