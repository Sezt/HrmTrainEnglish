label sexy_tutoring:
    $ dates += 1
    if dates == 3:
        jump date_01
       
        
#    if dates >=3:
#        menu:
#            "Touch her thigh."
#            "Touch yourself."
#            "Touch her tits."
    "You tutor Hermione."
    jump day_start 
    
###DATE - 1#######
label date_01:
    "You touch her leg with your hand."
    her "Professor? What are you doing?"
    her "Alright, I'll let you touch my leg, but only if you promise me 5 points in exchange."
    "You promise her 5 points and keep touching her thigh."
    "The Tutoring session is over."
    jump day_start 

###DATE - 2#######
label date_02:
    menu:
        "Touch her leg with yours.":
            if hermi.whoring < 3:
                "Hermione pays no attention to your touch at all..."
            elif hermi.whoring >= 3 and hermi.whoring < 6:
                "Hermione is aware of your touch but says nothing."
            elif hermi.whoring >= 6:
                "Hermione gets closer to you. Her legs move ever slightly in response to your touch."
            "Tutoring is over. Hermione leaves."
            $ hermi.whoring +=1
            jump day_start 
        "Touch her leg with your hand." if hermi.whoring >= 7:
            pass
        "{color=#858585}...(LOCKED)...{/color}" if hermi.whoring <=7:
            jump locked
        "Put her hand on your crotch." if hermi.whoring >= 14:
            pass
        "{color=#858585}...(LOCKED)...{/color}" if hermi.whoring <=14:
            jump locked
        "Jerk off." if hermi.whoring >= 21:
            pass
        "{color=#858585}...(LOCKED)...{/color}" if hermi.whoring <=21:
            jump locked
        "Make her stroke your cock." if hermi.whoring >= 28:
            pass
        "{color=#858585}...(LOCKED)...{/color}" if hermi.whoring <=28:
            jump locked
        "Finger her." if hermi.whoring >= 35:
            pass
        "{color=#858585}...(LOCKED)...{/color}" if hermi.whoring <=35:
            jump locked
        "Make her suck your cock." if hermi.whoring >= 42:
            pass
        "{color=#858585}...(LOCKED)...{/color}" if hermi.whoring <=42:
            jump locked
        "Fuck her while she's reading." if hermi.whoring >= 49:
            pass
        "{color=#858585}...(LOCKED)...{/color}" if hermi.whoring <=49:
            jump locked
        "Fuck her ass." if hermi.whoring >= 56:
            pass
        "{color=#858585}...(LOCKED)...{/color}" if hermi.whoring <=56:
            jump locked
        "-Cancel-":
            jump home_assignment
            
            
###LOCKED MASSAGE###
label locked:
    "Not enough whoring."
    jump sexy_tutoring
