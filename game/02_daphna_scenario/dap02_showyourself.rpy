################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label dap_request_02: #LV.1 (Whoring = 0 - 2)
    $music("Daphne Theme")

    if IsRunNumber(1):
        $hero("so, miss Greengrass. The time has come to teach you to stand on the stage. Are you ready?")
        $daphne("~55 00 1 def// Yes, sir, what must I do? To walk?")
        $hero("No, miss, lie down.")
        $daphne("~46 w0 1 def// ...?!")
        $hero(g4, "Oh, I'm sorry, miss, I looked at you and suddenly dreaming...")
        $daphne("~37 s0 1 neu// what are you dreaming?")
        $hero("I? Dreaming about... about the problems of the faculty, Yes...",
            m," no No, don't need anything complicated \"walk, lie down\"... Just reduce the amount of your clothes.")
        $daphne("~37 c0 1 dis// Clothes, sir? But... I'm still wearing that mom would've thought it was a clothes whore!")
        $hero("Miss Greengrass, the competition will not be your mom but be submitted to a jury, which expects to see the contestants in suitable outfits.// Of course, you can go to the podium in Russki... v tulup.//"
         "But I don't think your style will appreciate. You must remain a minimum of clothing to the members of the jury noted your appearance.")
        $daphne("~73 c0 1 pri// Oh, sir. This is terrible. I will consider, as a thoroughbred horse...!")
        $hero("#Hehe. Option \"bitch\" I liked more.")
        $daphne("~73 00 1 pri// You said something, sir?")
        $hero("Oh, it's not worth your attention, miss. So from what you get at the beginning?")
        $daphne("~73 00 1 ehh// Well, I can change the top to a more open. I hope this is enough?")
        $hero("Miss, this is your competition, your success and your failure. You decide this is enough.")
        $daphne("~73 01 1 pur// Hmm... Well, I hope it's enough.")

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $daphne.chibi.Hide()
        $daphne.ItemsCustomize(delete={"sleeves"}).chibi.State(appearance="c").Refresh()
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("you Have lovely hands, miss Greengrass, I've never seen them naked.")
        $daphne("~73 00 2 ang// Oh, sir, please.")
        $hero ("Green straps of the bra is not too in tune.")
        $daphne("~73 00 2 pou// Oh, sir, I figured that would have...")
        $hero("to be Naked before a man?")
        $daphne("~73 n2 3 def// Well, yeah...")
        $hero("it's All right, miss. You look very attractive. I think you deserved a small reward.")
    elif IsRunNumber(2):
        $hero("Well, miss Greengrass. Let's continue to learn to stand on the stage.")
        $daphne("~55 00 2 def// I go... or?")
        $hero("Or! You need to unload the other one items of clothing.")
        $daphne("~46 00 2 ehh// Well, have long wanted to make these stockings, I look like a bloody freak.")

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $daphne.ItemsCustomize(delete={"stockings"}).chibi.State(appearance="c").Refresh()
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
        $screens.Show("ctc").Pause().Hide("ctc")


        $hero("Here is enthusiasm! You should keep it, miss, while you can remove all other clothing.")
        $daphne("~46 w0 1 ehh// ENTIRE?!...")
        $hero(g4, "Um... just a figure of speech, miss.",m ,"let's see what I can donate.")
    elif IsRunNumber(3):
        $hero("so, miss Greengrass, your shape is close to the one in which you will act.")
        $daphne("~55 00 1 neu// Sir, she is already almost one!")
        $hero("Not at all, miss, we still have much. It's time to get rid of another thing.")
        $daphne("~55 00 1 ehh// From what?")
        $hero("Decide for yourself, miss.")
        $daphne("~26 01 2 ope// You do not expect, sir, that I'll show you my underwear?! What will it look like?!")
        $hero("On stage you should only be what you call underwear, miss.//"
            "By the way, I'm sure YOUR underwear is of the highest quality and matched with the inherent grace...//"
            "So he's not ashamed to show in the most elegant society.")
        $daphne("~26 01 smi 2// Uh... You are certainly right, sir.")
        $hero("#(Fucking Sands, all the while having to keep track of the language to not blurt out \"On your knees, slut!\")")
        $daphne("~37 00 smi 2// I say, you are right, about the grace...//~73 00 smi 2// Sir?")
        $hero("Huh? Yeah, so I -- I will gladly admire your underwear, miss. When you are ready, of course.")
        $daphne("~01 2 73 ehh// Oh... I don't even know... It is really graceful, in the end I'm a sorceress in Merlin knows what!...")
        $hero("#(it begins to carry this Blizzard, my prick omitted...)")
        $daphne("~73 01 2 pur// But I'm not ready, sir. And now need something to remove...//~55 01 2 pou// Then I will take it off. Turn away, sir!//~55 01 3 pou// better yet, I'll turn away.")

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"}).chibi.State(appearance="f").Refresh()
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") 
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("Urgh, you decided to show me your nipples standing? I appreciated, they are excellent!")
        $daphne("~37 00 2 ope// What?! Sir!")
        $hero("Miss Greengrass, you could take off your blouse and your tight bra I would not have seen the dramatic details.// But you chose to show me that excited.")
        $daphne("~26 00 wo 3// What? No! How dare you!")
        $hero("Miss Greengrass, don't be angry, this is good news that you get excited when exposing yourself to the man.// This will help you not only on competition.")
        $daphne("~26 00 3 ope// It's not due to the fact that I took off my bra, just so you know!")
        $hero("Hmm. Are you so stirred up the conversation about how you will stand before the audience in his underwear?")
        $daphne("~26 00 3 dis// Sir, this is just beyond!!! I will immediately complain to your parents!")
        $hero("you never even told me that trying to become Miss Hogwarts?//"
            "They don't really read \"the prophet\", isn't it?")
        $daphne("~55 s0 3 pou")
        $hero("I Suppose you wanted to officially return with a victory, or to keep secret, if you fail.//"
            "But unlikely, girl, from Mrs. Greengrass manages to hide it if you're with a whistle you get knocked out in the first round.//"
            "Your enemies, the faculty will take care of that.//")
        $daphne("~37 01 3 dis// ........................")
        $hero("#(so I guess I jumped the gun a little... But I think the girl has too much at this competition, so it will be fine.)//"
            "Miss, of course, what to do, you decide.// But as a sign of my special to you is a gift to you I still made it.")
        $daphne.liking-=15

    if daphne.whoring<=2:
        $daphne.whoring=event._finishCount+1
    return

