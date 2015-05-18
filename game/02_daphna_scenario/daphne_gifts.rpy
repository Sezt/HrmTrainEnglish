#label daphne_giving_pre():
#    $item=itsDAHR(choose.choice)
#    $daphne_giving_return="daphne_pre_finish_menu"
#    jump daphne_givingf

label daphne_giving: #Переходит через меню, значит можно в меню добавить адрес ухода в ничего и не использовать вспомогательную, а сразу заходить по этой метке и разбирать переменные менею
    $item=itsDAHR(choose.choice)
    $daphne_giving_return=choose.escLabel

    if item.Name=="wine":
        if daphne.whoring<3:
            $daphne("~55 w0 1 ang// Wine, sir?// I ... I don't even know.//~55 01 ehh 1// I am, of course, legal, but mom thinks that It is still too early."),
            $hero("But you do want to try, miss Greengrass?") 
            $daphne("~64 00 1 smo// Yeah.//~55 01 1 pou// At the last \"Fall Ball\" I tried it, and then... //~55 01 2 dis// I was told that...I tried to kiss this half-breed.// But I don't remember any of it.")
            $hero("Oh, I think that was just a coincidence.// I am sure that you are ready to enjoy some wine, now that you have grown into a mature woman."), 
            $daphne("~55 00 1 def// Yes sir, of course. Thanks for believing in me.")
            call daphne_changeliking(3)

        elif daphne.whoring<=6:
            if daphne.Items(item.Name)._count==0:
                $daphne("~55 w0 1 ang// Wine, sir?// I ... I don't know.")
                $hero("This is a special gift for a special student, miss.") 
            $daphne("~55 00 1 smo// Thank you, sir. I hope none of the other students see me drinking.")
            $hero("You can do with it what you like. However, if you want to enjoy it with some company, I'm your man.")
            $daphne("~55 00 1 def// Thank you, sir.")
            call daphne_changeliking(6)


    if item.Name=="beer":
        if daphne.whoring<3:
            $daphne("~37 c0 1 pri// I don't think it's a good idea, sir.// Giving beer to a student? Beer is banned at Hogwarts!")
            $hero("Miss Greengrass, of course I wouldn't give beer to any REGULAR student. But YOU... You are another matter.")
            $daphne("~64 00 1 smo// Oh!...//.....//~55 00 1 smi// Of course, You are right, sir.")
            call daphne_changeliking(+4)
        elif daphne.whoring<=6:
            $daphne("~55 00 1 smi// Beer is banned at Hogwarts, sir.// But out of respect for you I'll take it.")
            call daphne_changeliking(+8)
        
    if item.Name=="candy":
        if daphne.whoring<=6:
            $daphne("~55 00 1 pri// Candy? Sir, is this a joke!// How old do you think I am?")
            call daphne_changeliking(-5)

    if item.Name=="chocolate":
        if daphne.whoring<=6:
            $daphne("~55 00 1 neu// Hmm...this might make me fat.//~55 00 1 smi// I will take it, sir. Just to show that I appreciate your gesture.")
            call daphne_changeliking(0)

    if item.Name=="owl":
        if daphne.whoring<=6:
            $daphne("~37 00 1 pou// Similar to the cheap Chinese toys you get from fairground stalls.//"
                "Some mudblood would probably enjoy this gift, sir.//"
                "~37 00 1 smo// Each of my birthday gifts is worth more than all the owls in that stall.//"
                "Most likely including the stall and seller as well."),
            call daphne_changeliking(-6)

    if item.Name=="mag1":
        if daphne.whoring<=6:
            $daphne("~55 00 1 pur// What a bore!// Why would you offer me this, sir?")
            call daphne_changeliking(-5)

    if item.Name=="mag2":
        if daphne.whoring<=6:
            $daphne("~55 00 1 neu// This is fiction for underclass girls, sir... But I think I'll take them.//~55 00 1 ope// Just to make sure that they don't compare to someone like me...")
            call daphne_changeliking(+2)

    if item.Name=="mag3":
        if daphne.whoring<=6:
            $daphne("~55 01 1 neu// Hm... is this a hint that I don't have a boyfriend, sir?//~37 00 1 neu// A bit bold of you, sir!//~46 00 1 def// OK, I'll take it.// Although there is nothing I could learn from this. About guys... and everything else.")
            call daphne_changeliking(+1)

    if item.Name=="mag4":
        if daphne.whoring<=6:
            $daphne("~46 00 1 dis// What is this, sir?! It's disgusting, pureblood girls do not do anything like that!")
# And then, you wondered where I put it? These mongrels will be only too happy to tell everyone kakka I izvrashai.
            call daphne_changeliking(-5)

    if item.Name=="condoms":
        if daphne.whoring<=6:
            $daphne("~37 c0 1 pri// Condoms? Why should I, I'm...//"
                "~37 00 1 pur// Um... I wanted to say...//~37 01 1 pur// No, of course I long to meet a decent, tall and handsome guy...and we...//~37 01 1 ope// Alright, hand them over, Professor!...// Although I don't need them!"),
            call daphne_changeliking(0)

    if item.Name=="perfume":
        $Say("> You where going to give Daphne the perfume, but can't seem to get ahold of it.//"
            "> After several unsuccessful attempts to grab the annoying bottle, you decide to opt out of this idea, not to look like a complete idiot.")
        $item=None # Must be assigned, to exit the menu will be checked on the offer of a gift, in this case the gift is not offered. And go
        jump expression daphne_giving_return 

    if item.Name=="vibrator":
        if daphne.whoring<=6:
            $daphne("~55 w0 1 def// Hmm, strange thing. Oh, it buzzes and shakes.// Is it a kitchenmixer or something like that?//~37 s0 pou 1// PF! I'm not a cook, sir!")
            call daphne_changeliking(-8)

    if item.Name=="lubricant":
        if daphne.whoring<=6:
            $daphne("~64 s0 1 dis// Some kind of oily stuff.//~64 00 1 pou//...it looks a bit like sunblock.//~64 00 1 smi// Thank you, sir. I'll try to put it on after school tomorrow!")
            call daphne_changeliking(+4)

    if item.Name=="ballgag":
        if daphne.whoring<=6:
            $daphne("~26 00 1 smi// Oh, sir!// I would love to put this on the Mudblood and then give her a good whipping!//~26 00 gri 1// I hope that day will come.")
            call daphne_changeliking(+10)

    if item.Name=="plug":
        if daphne.whoring<=6:
            $daphne("~64 00 1 ehh// Don't even know what this is. A bathtub plug?// I will take it with me the next time I shower. Thank you, sir.")
            call daphne_changeliking(+1)

    if item.Name=="strapon":
        if daphne.whoring<=6:
            $daphne("~64 00 1 dis// This reminds me of...//~64 00 1 pou// No, that cannot be. I don't think...")
            call daphne_changeliking(-1)

    if item.Name=="krum":
        if daphne.whoring<=6:
            $daphne("~55 00 1 smo// Oh, this guy. He is, of course, a commoner, but pretty muscular...//"
                "~46 00 1 pou// Just don't think that I am so interested in this commoner, Professor, that I would hang this poster over my bed!")
            call daphne_changeliking(+2)

    if item.Name=="lingerie":
        if daphne.whoring<=6:
            $daphne("~64 00 1 pur// Oh, uh... this is too bold.// Then again...//~46 01 2 pur// Well, I might meet a tall and handsome guy soon, but this is a bit too early .//~46 00 1 pur// Thanks, but no thanks, sir.")
            call daphne_changeliking(-2)

    if item.Name=="broom":
        if daphne.whoring<=6:
            $daphne("~55 00 1 neu// Hmm, a broom... I'm not too fond of flying, sir.//~55 00 1 ehh// My last broom never worked that well.// I do not understand why but it only rocked slightly back and forth.//~55 01 2 ehh// Very impractical but not that unpleasent....")
            call daphne_changeliking(-3)

    if item.Name=="sexdoll":
        if daphne.whoring<=6:
            $daphne("~55 w0 2 ehh// This...this is a doll sex?!//~55 01 2 ehh// Sir, sometimes I think you are a perv... uhm, into weird stuff.//"
                "~55 00 2 pur// But to offer this to a girl?!")
            call daphne_changeliking(-10)

    if item.Name=="badge_01":
        if daphne.whoring<=6:
            $daphne("~37 00 1 dis// Professor, this is a badge from that club the mudblood bitch Granger is president of!//~26 00 1 dis// How can you offer me THAT?!")
            call daphne_changeliking(-20)

    if item.Name=="nets":
        if daphne.whoring<=6:
            $daphne("~55 00 1 smi// Pretty lovely, sir (Although I've seen better quality)....Thank you!")
            call daphne_changeliking(+5)

    if item.Name=="miniskirt":
        if daphne.whoring<=6:
            $daphne("~55 00 1 pou// Hmm... It's too short. Don't think I'll want to wear that.")
            $hero("Alright then, I'll offer this skirt to miss Granger.")
            $daphne("~55 w0 1 ope// What?! You want give a gift to that mudblood?!")
            $hero("Miss, Hogwarts is expected to change with the times and I thought that you would like to wear this new item first.//"
                "But if you'll excuse me, I have to speak to miss Granger. The skirt should go to the highest ranked girl in the school. Apparently that's Granger, still figuring that out...")
            $daphne("~37 s0 1 ope// GRRH!! Give me that, let me see!")
            $daphne("~37 s0 1 pri// ........................")
            $daphne("~37 s0 1 pou// I will take it!//# It is not that short, hmph.")
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
        ">Daphnes has deteriorated...\n>Daphne is {size=+5}angry{/size} with you..."
    elif __liking==0:
        ">Daphnes mood has not changed..."
    else:
        if daphne.liking < 0:
            ">Daphnes mood has improved...\n>Daphne is {size=+5}upset{/size} with you..." 
        elif daphne.liking == 0:
            ">Daphnes mood has improved...\n>Daphne is {size=+5}angry{/size} with you..."
        else:
            ">Daphnes mood has improved...\n>Daphne {size=+5}enjoys your company{/size}..."        
    return

        



