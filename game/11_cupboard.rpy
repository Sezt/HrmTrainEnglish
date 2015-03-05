label cupboard:
    menu:
        "-Examine the cupboard-" if not cupboard_examined:
            $ cupboard_examined = True
            show screen chair_02 #Empty chair near the desk.
            hide screen genie
            $ tt_xpos=-20
            $ tt_ypos=100
            show screen genie_stands_f
            show screen desk
            with Dissolve(0.5)
            m "Hm....."
            m "A cupboard..."
            m "Maybe I should rummage through this one later..."
            show screen genie
            hide screen genie_stands_f
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
            
            
            
        "-Rummage through the cupboard-" if not searched and not day == 1:
            jump rummaging
        "{color=#858585}-Rummage through the cupboard-{/color}" if searched and not day == 1:
            call already_did #Message that says that you have searched the cupboard today already.
            jump cupboard
        "-Your possessions-" if not day == 1:
            label possessions:
            menu:

                
                "-lollipop candy-([candy])" if candy >= 1:
                    $ the_gift = "03_hp/18_store/11.png" # CANDY.
                    show screen gift
                    with d3
                    ">A lollipop. Adult candy for kids or kid's candy for adults?"
                    hide screen gift
                    with d3
                    jump possessions
                    
                "-Chocolate-([chocolate])" if chocolate >= 1:
                    $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
                    show screen gift
                    with d3
                    call choco_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Plush owl-([owl])" if owl >= 1:
                    $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
                    show screen gift
                    with d3
                    call owl_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Butterbeer-([beer])" if beer >= 1:
                    $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER
                    show screen gift
                    with d3
                    call beer_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Educational magazines-([mag1])" if mag1 >= 1:
                    $ the_gift = "03_hp/18_store/17.png" #MAGAZINE # 1
                    show screen gift
                    with d3
                    call mag1_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Girly magazines-([mag2])" if mag2 >= 1:
                    $ the_gift = "03_hp/18_store/18.png" #MAGAZINE # 2
                    show screen gift
                    with d3
                    call mag2_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Adult magazines-([mag3])" if mag3 >= 1:
                    $ the_gift = "03_hp/18_store/19.png" #MAGAZINE # 3
                    show screen gift
                    with d3
                    call mag3_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "-Porn magazines-([mag4])" if mag4 >= 1:
                    $ the_gift = "03_hp/18_store/20.png" #MAGAZINE # 4
                    show screen gift
                    with d3
                    call mag4_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Viktor Krum Poster-([krum])" if krum >= 1:
                    $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
                    show screen gift
                    with d3
                    ">A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world."
                    hide screen gift
                    with d3
                    jump possessions

                "-Sexy lingerie-([lingerie])" if lingerie >= 1:
                    $ the_gift = "03_hp/18_store/24.png" # LENGERIE.
                    show screen gift
                    with d3
                    ">Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath."
                    hide screen gift
                    with d3
                    jump possessions

                "-A pack of condoms-([condoms])" if condoms >= 1:
                    $ the_gift = "03_hp/18_store/10.png" # CONDOMS.
                    show screen gift
                    with d3
                    call con_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "-Vibrator-([vibrator])" if vibrator >= 1:
                    $ the_gift = "03_hp/18_store/13.png" # VIBRATOR.
                    show screen gift
                    with d3
                    call vib_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "-Jar of anal lubricant-([anal_lube])" if anal_lube >= 1:
                    $ the_gift = "03_hp/18_store/09.png" # Anal lubricant.
                    show screen gift
                    with d3
                    call lub_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "-Ball gag and cuffs-([ballgag])" if ballgag >= 1:
                    $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
                    show screen gift
                    with d3
                    call ball_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Anal plugs-([plug])" if plug >= 1:
                    $ the_gift = "03_hp/18_store/16.png" # ANAL PLUG.
                    show screen gift
                    with d3
                    call anal_text
                    hide screen gift
                    with d3
                    jump possessions

                "- Thestral Strap-on -([strapon])" if strapon >= 1:
                    $ the_gift = "03_hp/18_store/14.png" # STRAP-ON.
                    show screen gift
                    with d3
                    call str_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Lady Speed Stick-2000 -([broom])" if broom >= 1:
                    $ the_gift = "03_hp/18_store/25.png" # BROOM.
                    show screen gift
                    with d3
                    ">The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!"
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Sex doll \"Joanne\" -([sexdoll])" if sexdoll >= 1:
                    $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
                    show screen gift
                    with d3
                    ">Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort."
                    hide screen gift
                    with d3
                    jump possessions
                    
                "-The Ball Dress-" if "ball_dress" in gifts12 and not gave_the_dress:
                    $ the_gift = "03_hp/18_store/01.png" # DRESS.
                    show screen gift
                    with d3
                    m "A fancy night dress I bought..."
                    m "I hope it's the right size."
                    hide screen gift
                    with d3
                    jump possessions
                    
                "-\"S.P.E.W.\" Badge-" if badge_01 == 1:
                    $ the_gift = "03_hp/18_store/29.png" # S.P.E.W. BADGE
                    show screen gift
                    with d3
                    m "A \"S.P.E.W.\" Badge..."
                    hide screen gift
                    with d3
                    jump possessions
                    
                "-Fishnet stockings-" if nets == 1:
                    $ the_gift = "03_hp/18_store/30.png" # FISHNETS.
                    show screen gift
                    with d3
                    call nets_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "-School miniskirt-" if have_miniskirt:
                    $ the_gift = "03_hp/18_store/07.png" # MINISKIRT.
                    show screen gift
                    with d3
                    m "A school miniskirt... Improves grades drastically."
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Dumbledor's Wine-([wine])" if wine >= 1:
                    $ the_gift = "03_hp/18_store/27.png" # WINE.
                    show screen gift
                    with d3
                    ">A bottle of wine from professor dumbledore's personal stash..." 
                    hide screen gift
                    with d3
                    jump possessions
                    
                    
                "-Unknown potion-([potions])" if  potions >= 1:
                    $ the_gift = "03_hp/18_store/32.png" # HEALING POTION.
                    show screen gift
                    with d3
                    ">A potion of some sort..." 
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Help -" if  day>1:
                    label cheat_help:
                    menu:
                        "Enable TURBO mode" if turbo==1: 
                            $turbo=2
                            "TURBO mode is enabled. Now your actions will bring you twice as much money and points the faculty slitherine.\n the Chance to read additional chapters twice."                    
                        "Disable TURBO mode" if turbo==2: 
                            $turbo=1
                            "TURBO mode is off. Now your actions will bring you the usual amount of money and points the faculty slitherine.\n The chance to read additional chapters standard"                    
                        "CHEAT: +100 points for Slytherin":
                            hide screen points
                            $slytherin+=100
                            show screen points
                        "CHEAT: +100 gold":
                            hide screen points
                            $gold+=100
                            show screen points
                        "Ticket":
                            $ vouchers += 1
                            "Obtained Voucher."
                            jump cheat_help   
                        "Imagination":
                            menu:
                                "Have you used this cheat already today? (Using it more than once can break the game)"
                                "Yes":
                                    jump cheat_help 
                                "No":
                                    $ imagination += 1
                                "- Never mind -":
                                    jump cupboard
                            jump cheat_help
                        "- Never mind -":
                            jump cupboard
                "- Never mind -":
                    jump cupboard

        "-Sacred scrolls volume I-" if not day == 1 and cataloug_found:
            label sc_col_men_1:
            menu:
                "-S.01: [scroll_01_name]-" if sscroll_01 or persistent.ss_01:
                    $ the_gift = "03_hp/19_extras/01.png" # SACRED SCROLL 01.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                    
                "-S.02: [scroll_02_name]-" if sscroll_02 or persistent.ss_02:
                    $ the_gift = "03_hp/19_extras/02.png" # SACRED SCROLL 02.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                    
                "-S.03: [scroll_03_name]-" if sscroll_03 or persistent.ss_03:
                    $ the_gift = "03_hp/19_extras/03.png" # SACRED SCROLL 03.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                    
                "-S.04: [scroll_04_name]-" if sscroll_04 or persistent.ss_04:
                    $ the_gift = "03_hp/19_extras/04.png" # SACRED SCROLL 04.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                    
                "-S.05: [scroll_05_name]-" if sscroll_05 or persistent.ss_05:
                    $ the_gift = "03_hp/19_extras/05.png" # SACRED SCROLL 05.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                    
                "-S.06: [scroll_06_name]-" if sscroll_06 or persistent.ss_06:
                    $ the_gift = "03_hp/19_extras/06.png" # SACRED SCROLL 06.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                    
                "-S.07: [scroll_07_name]-" if sscroll_07 or persistent.ss_07:
                    $ the_gift = "03_hp/19_extras/07.png" # SACRED SCROLL 07.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                    
                "-S.08: [scroll_08_name]-" if sscroll_08 or persistent.ss_08:
                    $ the_gift = "03_hp/19_extras/08.png" # SACRED SCROLL 08.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                    
                "-S.09: [scroll_09_name]-" if sscroll_09 or persistent.ss_09:
                    $ the_gift = "03_hp/19_extras/09.png" # SACRED SCROLL 09.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                    
                "-S.10: [scroll_10_name]-" if sscroll_10 or persistent.ss_10:
                    $ the_gift = "03_hp/19_extras/10.png" # SACRED SCROLL 10.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                
                "-S.11: [scroll_11_name]-" if sscroll_11 or persistent.ss_11:
                    $ the_gift = "03_hp/19_extras/11.png" # SACRED SCROLL 11.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                
                "-S.12: [scroll_12_name]-" if sscroll_12 or persistent.ss_12:
                    $ the_gift = "03_hp/19_extras/12.png" # SACRED SCROLL 12.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                
                "-S.13: [scroll_13_name]-" if sscroll_13 or persistent.ss_13:
                    $ the_gift = "03_hp/19_extras/13.png" # SACRED SCROLL 13.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                
                "-S.14: [scroll_14_name]-" if sscroll_14 or persistent.ss_14:
                    $ the_gift = "03_hp/19_extras/14.png" # SACRED SCROLL 10.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
                
                "-S.15: [scroll_15_name]-" if sscroll_15 or persistent.ss_15:
                    $ the_gift = "03_hp/19_extras/15.png" # SACRED SCROLL 15.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1

                "-Never mind-":
                    jump cupboard
            
            
        "-Sacred scrolls volume II-" if not day == 1 and cataloug_found:
            label sc_col_men_2:
            menu:
                "-S.16: [scroll_16_name]-" if sscroll_16 or persistent.ss_16:
                    $ the_gift = "03_hp/19_extras/16.png" # SACRED SCROLL 01.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                    
                "-S.17: [scroll_17_name]-" if sscroll_17 or persistent.ss_17:
                    $ the_gift = "03_hp/19_extras/17.png" # SACRED SCROLL 02.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                    
                "-S.18: [scroll_18_name]-" if sscroll_18 or persistent.ss_18:
                    $ the_gift = "03_hp/19_extras/18.png" # SACRED SCROLL 03.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                    
                "-S.19: [scroll_19_name]-" if sscroll_19 or persistent.ss_19:
                    $ the_gift = "03_hp/19_extras/19.png" # SACRED SCROLL 04.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                    
                "-S.20: [scroll_20_name]-" if sscroll_20 or persistent.ss_20:
                    $ the_gift = "03_hp/19_extras/20.png" # SACRED SCROLL 05.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                    
                "-S.21: [scroll_21_name]--" if sscroll_12 or persistent.ss_12:
                    $ the_gift = "03_hp/19_extras/21.png" # SACRED SCROLL 21.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                    
                "-S.22: [scroll_22_name]-" if sscroll_22 or persistent.ss_22:
                    $ the_gift = "03_hp/19_extras/22.png" # SACRED SCROLL 22.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                    
                "-S.23: [scroll_23_name]--" if sscroll_23 or persistent.ss_23:
                    $ the_gift = "03_hp/19_extras/23.png" # SACRED SCROLL 23.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                    
                "-S.24: [scroll_24_name]-" if sscroll_24 or persistent.ss_24:
                    $ the_gift = "03_hp/19_extras/24.png" # SACRED SCROLL 24.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                    
                "-S.25: [scroll_25_name]-" if sscroll_25 or persistent.ss_25:
                    $ the_gift = "03_hp/19_extras/25.png" # SACRED SCROLL 25.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                
                "-S.26: [scroll_26_name]-" if sscroll_26 or persistent.ss_26:
                    $ the_gift = "03_hp/19_extras/26.png" # SACRED SCROLL 26.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                
                "-S.27: [scroll_27_name]-" if sscroll_27 or persistent.ss_27:
                    $ the_gift = "03_hp/19_extras/27.png" # SACRED SCROLL 27.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                
                "-S.28: [scroll_28_name]-" if sscroll_28 or persistent.ss_28:
                    $ the_gift = "03_hp/19_extras/28.png" # SACRED SCROLL 28.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                
                "-S.29: [scroll_29_name]-" if sscroll_29 or persistent.ss_29:
                    $ the_gift = "03_hp/19_extras/29.png" # SACRED SCROLL 29.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2
                
                "-S.30: [scroll_30_name]-" if sscroll_30 or persistent.ss_30:
                    $ the_gift = "03_hp/19_extras/30.png" # SACRED SCROLL 30.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_2

                "-Never mind-":
                    jump cupboard
            
        "-Never mind-":
            jump day_main_menu
 
label rummaging:  
    
    $ searched = True #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
    
    $ rum_times += 1 # Counts how many times have you rummaged the cupboard. +1 every time you do that. Needed to make to grand 2 potions before the fight.
    
    hide screen cupboard
    hide screen genie
    show screen rum_screen
    with Dissolve(0.3)
    show screen bld1
    with d3
    ">You rummage through the cupboard for a while..." 
    
    if day <= 4:
        if rum_times == 2 or rum_times == 3:
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ potions += 1
            $ the_gift = "03_hp/18_store/32.png" # CANDY.
            show screen gift
            with d3
            ">You found some sort of potion..." 
            hide screen gift
            with d3
            show screen cupboard
            show screen genie
            hide screen rum_screen
            
            hide screen bld1
            with d3
            
            if daytime:
                jump night_start
            else: 
                jump day_start

    if rum_times == 15 and not cataloug_found:
        $ renpy.play('sounds/win2.mp3')   #Not loud.
        $ cataloug_found = True # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.
        $ the_gift = "03_hp/18_store/dahr2.png" # DAHR's oddities catalog. 
        show screen gift
        with d3
        ">You found the dahr's oddities catalog...\n>You can now use the catalog to order goods via owl post."
        hide screen gift
        with d3
        show screen cupboard
        show screen genie
        hide screen rum_screen
        
        hide screen bld1
        with d3
        
        if daytime:
            jump night_start
        else: 
            jump day_start
        
    
    if i_of_iv == 4: # Found something.
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            if one_of_tw == 20:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ sexdoll += 1
                $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
                show screen gift
                with d3
                ">You found the Sex doll \"Joanne\"!" 
                hide screen gift
                with d3
            elif one_of_tw == 1 or one_of_tw == 2:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ candy += 1
                $ the_gift = "03_hp/18_store/11.png" # CANDY.
                show screen gift
                with d3
                ">You found some candy..." 
                hide screen gift
                with d3
            elif one_of_tw >= 3 and one_of_tw <= 9  or one_of_tw == 18: # GOLD.
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ the_gift = "03_hp/18_store/28.png" # GOLD.
                show screen gift
                with d3
                ">You found [gold1] galleons..." 
                $ gold = gold + gold1
                hide screen gift
                with d3
            elif one_of_tw >= 10 and one_of_tw <= 16: # WINE.
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ wine += 1
                $ the_gift = "03_hp/18_store/27.png" # WINE
                show screen gift
                with d3
                ">You found a bottle of wine from professor dumbledore's personal stash..." 
                hide screen gift
                with d3
            elif one_of_tw == 17: # CHOCOLATE.
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ chocolate += 1
                $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
                show screen gift
                with d3
                ">You found a bar of chocolate..."
                hide screen gift
                with d3
            elif one_of_tw == 19: # LINGERIE.
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ lingerie += 1
                $ the_gift = "03_hp/18_store/24.png" # LINGERIE
                show screen gift
                with d3
                ">You found sexy lingerie..."
                hide screen gift
                with d3
                
          
        ### EVENT LEVEL 02 ###  ### ###  ### ###  ###  ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ###
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            if one_of_tw == 20:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ sexdoll += 1
                $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
                show screen gift
                with d3
                ">You found the Sex doll \"Joanne\"!" 
                hide screen gift
                with d3
            elif one_of_tw == 1 or one_of_tw ==2:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ candy += 1
                $ the_gift = "03_hp/18_store/11.png" # CANDY.
                show screen gift
                with d3
                ">You found some candy..." 
                hide screen gift
                with d3
            elif one_of_tw >= 3 and one_of_tw <= 10 or one_of_tw == 18:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ the_gift = "03_hp/18_store/28.png" # GOLD.
                show screen gift
                with d3
                ">You found [gold2] galleons..." 
                $ gold = gold + gold2
                hide screen gift
                with d3
            elif one_of_tw >= 11 and one_of_tw <= 15:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ wine += 1
                $ the_gift = "03_hp/18_store/27.png" # WINE
                show screen gift
                with d3
                ">You found a bottle of wine from professor dumbledore's personal stash..." 
                hide screen gift
                with d3
            elif one_of_tw == 16:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ lingerie += 1
                $ the_gift = "03_hp/18_store/24.png" # LINGERIE
                show screen gift
                with d3
                ">You found sexy lingerie..."
                hide screen gift
                with d3
            elif one_of_tw == 17:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ chocolate += 1
                $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
                show screen gift
                with d3
                ">You found a bar of chocolate..."
                hide screen gift
                with d3
            elif one_of_tw == 19:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ krum += 1
                $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
                show screen gift
                with d3
                ">You found a poster..."
                hide screen gift
                with d3
         
         
         
         
        ### EVENT LEVEL 03 ###  ### ###  ### ###  ###  ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ###
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            if one_of_tw == 20:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ sexdoll += 1
                $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
                show screen gift
                with d3
                ">You found the Sex doll \"Joanne\"!" 
                hide screen gift
                with d3
            elif one_of_tw >= 1 and one_of_tw <= 4:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ owl += 1
                $ the_gift = "03_hp/18_store/22.png" # OWL.
                show screen gift
                with d3
                ">You found a plush toy..." 
                hide screen gift
                with d3
            elif one_of_tw == 5 or one_of_tw == 6:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ candy += 1
                $ the_gift = "03_hp/18_store/11.png" # CANDY.
                show screen gift
                with d3
                ">You found some candy..." 
                hide screen gift
                with d3
            elif one_of_tw >= 7 and one_of_tw <= 14:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ the_gift = "03_hp/18_store/28.png" # GOLD.
                show screen gift
                with d3
                ">You found [gold3] galleons..." 
                $ gold = gold + gold3
                hide screen gift
                with d3
            elif one_of_tw >= 15 and one_of_tw <= 18:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ wine += 1
                $ the_gift = "03_hp/18_store/27.png" # WINE
                show screen gift
                with d3
                ">You found a bottle of wine from professor dumbledore's personal stash..." 
                hide screen gift
                with d3
            elif one_of_tw == 19:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ krum += 1
                $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
                show screen gift
                with d3
                ">You found a poster..."
                hide screen gift
                with d3
            
        ### EVENT LEVEL 04 ###  ### ###  ### ###  ###  ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ###
        if whoring >= 18: # Lv 7+  
            if one_of_tw == 20:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ sexdoll += 1
                $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
                show screen gift
                with d3
                ">You found the Sex doll \"Joanne\"!" 
                hide screen gift
                with d3
            elif one_of_tw >= 1 and one_of_tw <= 4:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ owl += 1
                $ the_gift = "03_hp/18_store/22.png" # OWL.
                show screen gift
                with d3
                ">You found a plush toy..." 
                hide screen gift
                with d3
            elif one_of_tw >= 5 and one_of_tw <= 8:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ chocolate += 1
                $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
                show screen gift
                with d3
                ">You found a bar of chocolate..."
                hide screen gift
                with d3
            elif one_of_tw >= 9 and one_of_tw <= 16:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ the_gift = "03_hp/18_store/28.png" # GOLD.
                show screen gift
                with d3
                ">You found [gold4] galleons..." 
                $ gold = gold + gold4
                hide screen gift
                with d3
            elif one_of_tw == 17:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ broom += 1
                $ the_gift = "03_hp/18_store/25.png" # BROOM.
                show screen gift
                with d3
                ">You found a broom..."
                hide screen gift
                with d3
            elif one_of_tw == 18:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ krum += 1
                $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
                show screen gift
                with d3
                ">You found a poster..."
                hide screen gift
                with d3
            elif one_of_tw == 19:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ lingerie += 1
                $ the_gift = "03_hp/18_store/24.png" # LINGERIE
                show screen gift
                with d3
                ">You found sexy lingerie..."
                hide screen gift
                with d3
            

    else: #Didn't find anything.
        ">...You find nothing of value." 
    

    
    show screen cupboard
    show screen genie
    hide screen rum_screen
    
    hide screen bld1
    with d3
    
    if daytime:
        jump day_main_menu
    else: 
        jump night_main_menu
        
        
        
        
        
        
        
######################
label already_did:
    show screen bld1
    with d3
    m "I already did that today..."
    hide screen bld1
    with d3
    return
