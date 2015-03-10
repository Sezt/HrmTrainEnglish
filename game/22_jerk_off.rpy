label jerk_off:
    $ cum_on_desk = False
    $ cum_on_the_floor = False
    $ jerk_zorder = 5
    $ cum_on_panties = False #True when choose to cum on Hermione's panties.
    ">You decide to unwind a bit by jerking off..."
    m "Hmm... Who shall I think about today?"
    menu:
        "- Princess Jasmine -":
            m "Yes, Princess... Show how me how much you like being a dirty slut!"
            $ jerking_off_to_jasmine = True #Princess Jasmine has been chosen as a target for a jerk-off session
            pass
        " - Lara Croft - ":
            m "Why Miss Croft!  What a tight body you have!  I want to see just how adventurous you truly are!"
            $ jerking_off_to_lara = True
            pass
        "- Cancel -":
            jump desk


   ### JERKING OFF ###
    with d5
    show screen genie_jerking_off
    with d8
    if jerking_off_to_jasmine:
        ">You fantasize about Princess Jasmine..."
        $ checked = 'jas'
        g9 "Uh... she wants it bad... wants to feel my hot juice spurting all over her..."
        g9 "Yeah, you love my huge cock.  Take it all the way in you whore!"
        jump random_pics
    if jerking_off_to_lara:
        ">You fantasize about Lara Croft..."
        $ checked = 'lara'
        g9 "Oh yeah... she really knew how to suck a cock...  and those boots..."
        g9 "Come on, baby...let me hear you scream when you cum!"
        # show image "03_hp/22_dreams/lara/1.png" onlayer overlay at Transform(zoom=0.9)# CLEAR WEATHER.
        with d8 
        jump random_pics
       

    label finish_cum:
        ">You are ready to cum..."

    m "How should I finish?"   
    label how_to_finish:
        menu:
            "- On the floor! -":
                $ cum_on_the_floor = True #TRUE when chosen to cum on the floor.
                pass
            "- On the table -":
                $ cum_on_desk = True
                pass
            "{color=#858585}- (LOCKED) -{/color}" if not request_03: #True when Hermione has no panties on.:
                ">You lack the item required for this option."
                jump how_to_finish
            "- Hermione's panties -" if request_03: #True when Hermione has no panties on.
                $ cum_on_panties = True #True when choose to cum on Hermione's panties.
                pass
            "- Cancel -":
               jump jerk_off

        if one_out_of_three == 1:
            g4 "Argh! Whore!"
        elif one_out_of_three == 2:
            g4 "YES! GET IT SLUT! ARRH!"
        elif one_out_of_three == 3:
            g4 "Oh Yes! Wow... It's been way too long since I did that."
        # hide screen genie_jerking_off
        show screen genie_jerking_sperm
        if cum_on_desk:
            ">You cum on the table."
            g4 "I better wipe this up so my papers don't stick..."
        if cum_on_the_floor:
            ">You cum on the floor."
            g4 "Eh, it's probably good for the rug."
        if cum_on_panties:
            $ have_cum_soaced_panties = True #TRUE when you have the panties in your possession (before you return them to Hermione).
            ">You cum all over Hermione's panties, and then use them to wipe the cum off the floor..."
            g4 "Oh, yeah, girlie!  You are gonna like my spunk rubbing all over your pussy lips!"
            ">You received the item: \"Cum-soaked panties\"."
        hide screen genie_jerking_sperm
        g7 "Yeah, that was great! I wonder if things will ever be like they used to be?"
        g7 "Banging those hot sluts"
        g7 "... oooh, Lara ... she had such a wet pussy ..."
        g7 "And the Princess, I brought her down to being a cock-hungry whore."
        g7 "That perfect royal mouth, sucking on me... Uh..."
        g4 "Okay, I better get back to work.  I can do way better than jerking off with all the premium pussy around here!"
   ### SETTING ALL THE FLAGS BACK TO DEFAULT ###
    $ jerking_off_to_jasmine = False #Turns TRUE when Princess Jasmine has been chosen as a target for a jerk-off session.
    $ jerking_off_to_lara = False 
    $ cum_on_the_floor = False #TRUE when chosen to cum on the floor.
    $ cum_on_panties = False #True when choose to cum on Hermione's panties.
   
    if daytime:
        jump night_start
    else: 
        jump day_start
   
    label random_pics:
            $ list_of_files_jas = 10
            $ list_of_files_lara = 100
           
            if checked == 'jas':
                $ directory_of_images = '03_hp/22_dreams/jas'
                $ list_of_files = list_of_files_jas
            elif checked == 'lara':
                $ list_of_files = list_of_files_lara
                $ directory_of_images = '03_hp/22_dreams/lara'
            else:
                $ list_of_files = list_of_files_jas
                $ directory_of_images = '03_hp/22_dreams/jas'

           # About python code
            python:
                x = 0
                list_of_numbers = []
                while x < 10:
                    random_int = renpy.random.randint(1, list_of_files)
                    list_of_numbers.append(random_int)
                    x = x+1
                list_of_numbers = set(list_of_numbers)
            
                for i in list_of_numbers:
                    jerk_image = directory_of_images + '/%s.png' % i
                    renpy.show_screen("jerkingimage")
                    renpy.pause()
                    renpy.hide_screen("jerkingimage")
           # /About python code
           
            $ directory_of_images = False;
            $ list_of_files = False;
            jump finish_cum
