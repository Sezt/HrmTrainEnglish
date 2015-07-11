################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label dap_interlude_02: #LV.1 (Whoring = 0 - 2)
    $screens.ShowD3("bld1")
    $daphne.ItemsCustomize(update={"stockings", "sleeves"})
    $daphne.chibi.State("center", appearance="d").Trans(d4, "blink")

    $daphne.State(pos="door").Visibility("body+")
    $screens.Show("ctc").Pause().Hide("ctc")
    $daphne("~55 00 1 def// Good afternoon, Professor Dumbledore.")

    $hero("Miss?// Is something wrong? All those clothes...")
    $daphne("~46 01 1 ehh// Nothing...I'm just a bit cold.")
    $hero("But you put on a lot items that we already, through hard work, decided where not needed.")
    $daphne("~37 01 1 ope// Sir! I do not believe that I should be standing half-naked in front of you.// The competition is one thing, but gradually undressing in front of a man is...// It's like getting ready to share his bed!")
    $hero("#Why the need for a bed? The Headmasters's desk is more then suitable.")
    $daphne("~37 00 1 def// What did you say, sir?")
    $hero("I said, miss. If you are unhappy with my sincere interest and participation...//"
        "Then you and your parents could find someone else who is interested in your position at Hogwarts and prepare you for the competition.//"
        "Would you find it easier to undress in front of Professor Snape?")
    $daphne("~37 w0 1 def")
    $hero("Or Minerva McGonagall? Maybe I should talk to her?")
    $daphne("~64 w0 1 def// Oh, sir, not Professor McGonagall. Everyone knows that she doesn't like girls!")
    $hero("Who is left...Snape?")
    $daphne("~64 01 1 pou// No, sir. No need for Professor Snape. I'm going to stick with you.")
    $hero("Well then, miss. Get rid of the sleeves and next please show up without them from the start. You will not need them in the future.// You need to get used to...less restricting clothing.")
    $daphne("~64 00 1 ope// But, sir!")
    $hero("Don't Sir me! Right now you should be wearing a top without sleeves. Leave the stockings on, makes you look like a bloody freak.")
    $daphne("~73 w0 1 neu// Like a bloody freak, sir? Then I will remove them as well.")
    $hero("No, dear. Keep wearing them, as small punishment...// Go ahead, I'm waiting.")

    $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
    $daphne.ItemsCustomize(delete={"sleeves"})("~64 01 1 pou").chibi.State(appearance="e").Refresh()
    $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
    $screens.Show("ctc").Pause().Hide("ctc")

    $hero("Here. Have a another small present...// Miss! You have a strange dreamy look...You hear me?")

    return wtevent.Finalize()
#    $event.Finalize("daphne_approaching") # возвращается в глвное меню
