label phoenix:
    if bird_interact == 15: # Counts how many times you have interacted with the bird.
        stop music fadeout 3.0
        $ bird_interact += 1 # Counts how many times you have interacted with the bird.
        show screen blktone8
        with d7
        a1 "Alright, let's clear something up..."
        a1 "Interacting with this bird does literally nothing."
        a1 "There is a counter that starts this event after a certain amount of interactions, but that is it."
        a1 "I did have some rather ambitious plans for this foul bastard at first."
        a1 "Something about buying food for it, petting it and eventually getting a nice reward..."
        a1 "The whole thing got cut along with a ton of other things..."
        a1 "Normally I would take out the bird altogether, but I couldn't bring myself to do it..."
        a1 "Not after I spent so much time with animating that damn falling feather..."
        a1 "From now on you will be able to continue to feed and pet the bird but I just want you to know that it will not lead to anything."
        a2 "Sorry for this interruption. Enjoy the game now."
        hide screen blktone8
        with d3
        call music_block
        jump day_main_menu
    
    menu:
        "-Examine-" if not bird_examined:
            $ bird_examined = True
            hide screen genie
            $ tt_xpos=270
            $ tt_ypos=90
            show screen genie_stands
            show screen chair_02 #Empty chair near the desk.
            show screen desk
            with Dissolve(0.5)
            m "Hm....."
            m "Even this weird looking bird radiates magic..."
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
            
            
            
        "-Feed the bird-" if not phoenix_is_feed and bird_examined:
            $ phoenix_is_feed = True
            jump feeding
            
        "-Pet the bird-" if bird_examined:
            jump petting
        "-Never mind-":
            call screen main_menu_01    
            
            
### FEEDING ###
label feeding:
    $ bird_interact += 1 # Counts how many times you have interacted with the bird.
    hide screen genie
    show screen feeding 
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    $ genie_speaks = renpy.random.randint(1, 3) #Determines what phrase if any Genie will use.
    if genie_speaks == 1:
        m "There you go..."
    else:
        pause.5
    show screen genie
    hide screen feeding 
    with Dissolve(0.3)
    call screen main_menu_01    
    

### PETTING ###
label petting:
    $ bird_interact += 1 # Counts how many times you have interacted with the bird.
    hide screen genie
    show screen petting
    with Dissolve(0.3)
    pause 3
    show screen sad_phoenix #SMILEY
    pause 1.5
    m "The bird doesn't look good. Is it sick or something?"
    pause.5
    
    
    
    show screen genie
    hide screen sad_phoenix #SMILEY
    hide screen petting
    with Dissolve(0.3)
    call screen main_menu_01
    
    
    
    
   
