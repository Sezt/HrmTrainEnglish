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

    $hero("Miss?// What is it with you? You many clothes...")
    $daphne("~46 01 1 ehh// Nothing... Just, I'm cold.")
    $hero("But it seems to me that you put on so many clothes that they were difficult to remove.")
    $daphne("~37 01 1 ope// Sir! I do believe that should not be half-naked in front of you.// The contest the contest, but gradually undress before a man is...// It's like preparing to sleep in his own bed!")
    $hero("#Why go to bed? The Professor's Desk is also very appropriate place.")
    $daphne("~37 00 1 def// What did you say, sir?")
    $hero("I say, miss, what you mean. If you dislike my sincere interest and participation...//"
        "Then you and your parents to find someone else that he was engaged in your position at Hogwarts and preparing you for the competition.//"
        "You may find it easier to undress in front of Professor Snape?")
    $daphne("~37 w0 1 def")
    $hero("Or Minerai Mcgonagal? Maybe I should talk to her?")
    $daphne("~64 w0 1 def// Oh, sir, not Professor Mcgonagal. Everyone knows that she doesn't like girls!")
    $hero("but who remains, Snape?")
    $daphne("~64 01 1 pou// No, sir. Don't need Professor Snape. I'm going to do with you.")
    $hero("well, Then, miss. If we got rid of the sleeves, so for the next time you come already sleeveless. And more than ever not to wear them.// You need to adjust the ogol... to be not very tight clothing.")
    $daphne("~64 00 1 ope// But, sir!")
    $hero("No Sirs! Right now you should wear a top without sleeves. Stockings can leave, you look like a bloody freak.")
    $daphne("~73 w0 1 neu// like a bloody freak, sir? Then I will remove them too.")
    $hero("No, honey. You wearing, so now pay the price...// Start miss, I'm waiting.")

    $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
    $daphne.ItemsCustomize(delete={"sleeves"})("~64 01 1 pou").chibi.State(appearance="e").Refresh()
    $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
    $screens.Show("ctc").Pause().Hide("ctc")

    $hero("Here. Now another thing...// Miss! You have a strange dreamy look,... You hear me?")

    return event.Finalize()
#    $event.Finalize("daphne_approaching") # возвращается в глвное меню