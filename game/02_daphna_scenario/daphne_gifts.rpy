#label daphne_giving_pre():
#    $item=itsDAHR(choose.choice)
#    $daphne_giving_return="daphne_pre_finish_menu"
#    jump daphne_givingf

label daphne_giving: #Переходит через меню, значит можно в меню добавить адрес ухода в ничего и не использовать вспомогательную, а сразу заходить по этой метке и разбирать переменные менею
    $item=itsDAHR(choose.choice)
    $daphne_giving_return=choose.escLabel

    if item.Name=="wine":
        if daphne.whoring<3:
            $daphne("~55 w0 1 ang// Wine, sir?// I ... I don't even know.//~55 01 ehh 1// I, of course, legal, but mom thinks that I still early."),
            $hero("But you do want to try miss Greengrass.") 
            $daphne("~64 00 1 smo// Yeah.//~55 01 1 pou// But at last \"Fall ball\" I tried this, and then... //~55 01 2 dis// I was told that... I even climbed to kiss the half-breed.// But I don't remember it.")
            $hero("Oh, I think it was just a coincidence. I am sure that you are ready to drink wine, now as a Mature woman."), 
            $daphne("~55 00 1 def// Yes sir, of course. Thanks for believing in me.")
            call daphne_changeliking(3)

        elif daphne.whoring<=6:
            if daphne.Items(item.Name)._count==0:
                $daphne("~55 w0 1 ang// Wine, sir?// I ... I don't even know.")
                $hero("This is a special gift for a special student, miss.") 
            $daphne("~55 00 1 smo// Thank you, sir. I'm keeping that none of THESE saw.")
            $hero("Waiting for your story as you like. However, if you want to sit in the company, I'm your man.")
            $daphne("~55 00 1 def// Thank you, sir.")
            call daphne_changeliking(6)


    if item.Name=="beer":
        if daphne.whoring<3:
            $daphne("~37 c0 1 pri// I don't think it's a good idea, sir.// You give beer to his student? Beer is banned at Hogwarts!")
            $hero("Miss Greengrass, for REGULAR students, of course, I wouldn't give the beer. But YOU... You - is another matter.")
            $daphne("~64 00 1 smo// O!...//.....//~55 00 1 smi// of course, You are right, sir.")
            call daphne_changeliking(+4)
        elif daphne.whoring<=6:
            $daphne("~55 00 1 smi// Beer banned at Hogwarts, sir.// But out of respect for you I'll take it.")
            call daphne_changeliking(+8)
        
    if item.Name=="candy":
        if daphne.whoring<=6:
            $daphne("~55 00 1 pri// candy? Sir, this is even offensive!// You think I'm little?")
            call daphne_changeliking(-5)

    if item.Name=="chocolate":
        if daphne.whoring<=6:
            $daphne("~55 00 1 neu// Hmm... Say, get fat from it.//~55 00 1 smi// I think I'll take them, sir. Just to show that I appreciate your concern.")
            call daphne_changeliking(0)

    if item.Name=="owl":
        if daphne.whoring<=6:
            $daphne("~37 00 1 pou// Similar to Chinese cheap toy stall for neovolcanic.//"
                "Probably some mugridge rejoice in this gift, sir.//"
                "~37 00 1 smo// But one of my birthday gift is worth more than all the owls out of the stall.//"
                "And the stall bargain with the seller."),
            call daphne_changeliking(-6)

    if item.Name=="mag1":
        if daphne.whoring<=6:
            $daphne("~55 00 1 pur// What a bore!// Why would you offer me this, sir?")
            call daphne_changeliking(-5)

    if item.Name=="mag2":
        if daphne.whoring<=6:
            $daphne("~55 00 1 neu// This is fiction for girls-a mongrel, sir... But I think I'll take them.//~55 00 1 ope// Just to make sure that they hold a candle to me no good...")
            call daphne_changeliking(+2)

    if item.Name=="mag3":
        if daphne.whoring<=6:
            $daphne("~55 01 1 neu// Hm... is This a hint that I have no boyfriend, sir?//~37 00 1 neu// And I mean, like this!//~46 00 1 def// OK, I'll take it.// Although all this I know. And about guys... and about everything else.")
            call daphne_changeliking(+1)

    if item.Name=="mag4":
        if daphne.whoring<=6:
            $daphne("~46 00 1 dis// What is all this, sir?! It's disgusting, pureblood girls do not do anything like that!")
# And then, you wondered where I put it? These mongrels will be only too happy to tell everyone kakka I izvrashai.
            call daphne_changeliking(-5)

    if item.Name=="condoms":
        if daphne.whoring<=6:
            $daphne("~37 c0 1 pri// Condoms? Why should I, I'm...//"
                "~37 00 1 pur// Um... I wanted to say...//~37 01 1 pur// No, of course I long to meet a decent, tall and handsome guy... And we...//~37 01 1 ope// In General, let them here, Professor!...// Although I don't need everything is good!"),
            call daphne_changeliking(0)

    if item.Name=="perfume":
        $Say("> You are going to give Daphne the spirits, but they miraculously not given to you.//"
            "> After several unsuccessful attempts to grab oborachivayutsya bottle, you decide to opt out from this idea, not to look a complete idiot.")
        $item=None # Must be assigned, to exit the menu will be checked on the offer of a gift, in this case the gift is not offered. And go
        jump expression daphne_giving_return 

    if item.Name=="vibrator":
        if daphne.whoring<=6:
            $daphne("~55 w0 1 def// Hmm, strange thing. Oh, it buzzes and shakes.// It's a mixer for the kitchen or something like that?//~37 s0 pou 1// PF! I'm not a cook, sir!")
            call daphne_changeliking(-8)

    if item.Name=="lubricant":
        if daphne.whoring<=6:
            $daphne("~64 s0 1 dis// some Kind of oily stuff.//~64 00 1 pou//... Although It looks like a sunblock.//~64 00 1 smi// Thank you, sir. I'll try to put them after school tomorrow!")
            call daphne_changeliking(+4)

    if item.Name=="ballgag":
        if daphne.whoring<=6:
            $daphne("~26 00 1 smi// Oh, sir!// With what pleasure I would wear it on any Mudblood, and then slupia her whip!//~26 00 gri 1// I Hope that day will ever come.")
            call daphne_changeliking(+10)

    if item.Name=="plug":
        if daphne.whoring<=6:
            $daphne("~64 00 1 ehh// 't Even understand what it is. Stopper from a bathtub?// Take her with you when I'm showering. Thank you, sir.")
            call daphne_changeliking(+1)

    if item.Name=="strapon":
        if daphne.whoring<=6:
            $daphne("~64 00 1 dis// This reminds me of...//~64 00 1 pou// No, cannot be. I don't think...")
            call daphne_changeliking(-1)

    if item.Name=="krum":
        if daphne.whoring<=6:
            $daphne("~55 00 1 smo// Oh, this guy. He, of course, base-born, but, in principle, nothing...//"
                "~46 00 1 pou// Just do not think that I am interested in base-born, Professor, and hang the poster over the bed!")
            call daphne_changeliking(+2)

    if item.Name=="lingerie":
        if daphne.whoring<=6:
            $daphne("~64 00 1 pur// Oh, uh... It's too bold.// And then...//~46 01 2 pur// Well, my kid told me he is tall and handsome and all that. Here he recently gave it to me.//~46 00 1 pur// So I will refrain, sir.")
            call daphne_changeliking(-2)

    if item.Name=="broom":
        if daphne.whoring<=6:
            $daphne("~55 00 1 neu// Hmm, broom... I'm not too fond of flying, sir.//~55 00 1 ehh// And then here's this ledge.// I do not understand why it did, it only hinders.//~55 01 2 ehh// keep stuck in... which is not necessary.")
            call daphne_changeliking(-3)

    if item.Name=="sexdoll":
        if daphne.whoring<=6:
            $daphne("~55 w0 2 ehh// this... This doll for sex?!//~55 01 2 ehh// Sir, sometimes I think you are a Perv... uh, quite a bit, of course.//"
                "~55 00 2 pur// But to offer such a girl?!")
            call daphne_changeliking(-10)

    if item.Name=="badge_01":
        if daphne.whoring<=6:
            $daphne("~37 00 1 dis// Professor, it's an icon of society bitches this mugridge Granger! Or any other of its society!//~26 00 1 dis// How can you offer me THAT?!")
            call daphne_changeliking(-20)

    if item.Name=="nets":
        if daphne.whoring<=6:
            $daphne("~55 00 1 smi// Happy pleasant thing, sir (although I've seen better).... Thank you!")
            call daphne_changeliking(+5)

    if item.Name=="miniskirt":
        if daphne.whoring<=6:
            $daphne("~55 00 1 pou// Hmm... It's too short. Don't think I'll want her to wear.")
            $hero("Well then, I'll offer this skirt miss Granger.")
            $daphne("~55 w0 1 ope// What?! You want to make a gift to the Mudblood?!")
            $hero("Miss, Hogwarts is expected to change in shape and I thought, you will first get the thing, which no one has.//"
                "But if you'll excuse me, I have to speak to miss Granger. The skirt should receive the first girl of the faculty, not just you, apparently it's Granger, still learning it...")
            $daphne("~37 s0 1 ope// GRRH!! Give me that, I'll see!")
            $daphne("~37 s0 1 pri// ........................")
            $daphne("~37 s0 1 pou// I take this skirt!//# And nothing she's not short, it was just me.")
            call daphne_changeliking(0)

    if daphne_giving_return=="daphne_main_menu":
        $daphne.CommitGift()
    jump expression daphne_giving_return

label daphne_item_on(item):
    if item.Name=="skirt":
        pass

label daphne_item_off(item):
    if item.Name=="skirt":
        pass

    
    
        
        
label daphne_changeliking(__liking):
    $daphne.liking+=__liking
    if __liking>=0:
        $daphne.Items.Receive(hero.Items, item.Name)

#    $daphne.Visibility()
    if __liking<0:
        ">The mood of Daphne has deteriorated...\n>Daphne {size=+5}angry{/size} on you..."
    elif __liking==0:
        ">The mood of Daphne has not changed..."
    else:
        if daphne.liking < 0:
            ">The mood of Daphne improved...\n>Daphne {size=+5}upset you{/size}..." 
        elif daphne.liking == 0:
            ">The mood of Daphne improved...\n>Daphne {size=+5}angry{/size} on you..."
        else:
            ">The mood of Daphne improved...\n>Daphne {size=+5}enjoy your company{/size}..."        
    return

        



