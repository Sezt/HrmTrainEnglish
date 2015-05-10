################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label dap_request_01: #LV.1 (Whoring = 0 - 2)

    $music("Daphne Theme")

    if IsRunNumber(1):
#    if daphne.whoring<3:
        $hero("Well, miss, so just tell about those around you. We need to understand who you are dealing with.")
        $daphne("~55 00 1 neu// Well, to me they are, in General, uninteresting.// Why would I pay attention to all sorts of neovolcanic?!")
        $hero("But, miss, that you took on the faculty in the proper position, someone needs to take inappropriate.// Number of positions is quite limited. Do you understand me?")
        $daphne("~46 01 pou 1// Understand... I think.")
        $hero("So I give you a task: you must be interested in other students.// To pay attention to what they are more popular. Bye.")
        $daphne("~37 00 1 ope// Yes, sir. It is \"until\"! You put it succinctly...")
        $hero("Finding their weaknesses, all kinds of disadvantages and maybe even skeletons in the closet...")
        $daphne("~26 00 1 ope// uh... You want me to knock, sir?// ~26 00 1 neu// It is unworthy of the sorceress in Merlin knows what generation!")
        $hero("it's Strange to me about this says a student of Slytherin.// You are not wrong faculty, dear? Maybe you road in straight as a Board, Gryffindor?")
        $daphne("~55 00 1 pri// Hmm... But I...")
        $hero("I'm not suggesting \"knock\", as you put it.// Just study your classmates. Let me remind you, many of them will be performing at the contest.//" 
            "Let's see what they can win and which to lose.//"
            "You need to take care not only about how beautifully presented themselves on stage during the contest, miss, but your place on the faculty.//"
            "The higher it is, the more likely you will vote students, and their voices count too.")
        $daphne("~46 00 1 dis// Professor. I can't believe my ears!// You want me to grovel before mproblem to improve my chances?!")
        $hero("I propose to be more flexible, miss.// Now concentrate on a simple task and learn of their competitors.")
        $daphne("~46 00 1 pou// Hmm... I'll try, Professor.")
        $hero("Excellent. Then, tonight.")
    elif IsRunNumberOrMore(2):
        $hero("So, miss Greengrass. Let's you again today will study your competitors.")
        $daphne("~64 00 1 neu// Again, sir?")
        $hero("Well, if you already know all about them...")
        $daphne("~55 00 1 neu// not Yet, sir.")
        $hero("Then go ahead, we are waiting for you in the evening with the report.")
    return



label dap_request_01_complete:
    if event._finishCount>3: # Заглушка, нужно будет снять когда будут написаны последующие ивенты
        return event.Finalize()
    $daphne.Visibility()
    $daphne.chibi.State("door", speed="go").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")

    $daphne.State(pos="door").Visibility("body+")("~55 00 1 smi// Good evening, Professor Dumbledore.") 

    $music("Daphne Theme")

    if IsRunNumber(1):
        $hero("so, miss Greengrass, what is your success?")
        $daphne("~55 00 1 neu// Well, I watched Jesse. She seems not too hard to learn.")
        $hero ("and?")
        $daphne("~55 00 1 pur// That's all, sir.")
        $hero("And how it will help you to win the situation and rise above Jessie, miss? Want to say that its a bad study affect its popularity?")
        $daphne("~55 00 1 pou// In General, no. That's why I chose her is that she's very popular.//"
            "~55 01 1 pou// besides, she boasted that can charm any guy, so I decided...//"
            "~37 00 1 pou// Professor, please don't think that I need someone there to screw with!//"
            "I'm better than this! You just gave the job and I thought that it would fit.")
        $hero("I have heard that you are better than that, miss.// But it turns out that the job was done.")
        $daphne("~73 00 1 pou// I think so.")
        $hero("nevertheless, I am willing to stimulate, because I believe in you.// In the end you sorceress ancient clan.// I'm sure next time you'll do better.")
        $daphne("~73 00 1 smo// Thank you, sir, I'll try harder!")
    elif IsRunNumber(2):
        $daphne("~55 00 1 neu// Today, Professor Dumbledore, I decided to approach the issue systematically.")
        $hero("Oh yeah?")
        $daphne("~46 00 1 neu// Yes, sir. I think I'm beginning to understand why some girls are more popular than others.")
        $hero("#(me Too the binomial theorem.)// Listening to you, miss.")
        $daphne("I have one more thing to check, sir, I will be able to tell you.//" 
            "~46 00 1 pou// And today I looked to Melissa, she was flirting with guys.")
        $hero("what?")
        $daphne("~37 00 1 pur// Disgusting, sir. How she can do it – among them were not only half-breeds, but mugridge!")
        $hero("can't be!")
        $daphne("Yes, sir, I imagine.")
        $hero("what?")
        $daphne("~37 00 1 pri// Guys circled around her, sir!//"
            "~37 00 1 dis// And you know, I thought that some were willing to go with her flirting.")
        $hero("Here is a surprise!")
        $daphne("~37 00 1 pri// I was shocked too, sir!// I never paid attention to it, never thought about it.//"
            "~37 n0 1 pou// I was sure that clean the blood will open all doors and all sorts of flirting are necessary to nobody.//"
            "~37 n2 1 pou// But for some reason today I was a single guy, and this girl they flew, like flies on...")
        $hero("honey?")
        $daphne("~37 00 1 pou// I wanted to use a stronger word, sir. But let it be honey...")
        $hero("And now what, miss?")
        $daphne("~37 00 1 neu// I need time to figure it all out, sir.")
        $hero("Well, miss Greengrass, it looks like you are moving in the right direction. I think you should reward.")
    elif IsRunNumber(3):
        $daphne("I think I understand, sir.")
        $hero("Huh?")
        $daphne("~55 00 1 ope// Popularity depends on the school, popularity, boys, and of course, purity of blood.")
        $hero("#(Oh, great Sands! Enough with the platitudes and take, finally, her beautiful mouth useful!)// I, um... I see you are serious digging, miss, I was not mistaken in you.")
        $daphne("~73 00 1 smi// Thank you, sir.")
        $hero("Well, with purity of blood you have everything in order.")
        $daphne("~55 00 1 ope// Yes it is sir! So clean no blood from anyone at Hogwarts, but in Dormany.// ~55 c0 1 ope// We - Greengrassi descend from the Salazar Slee...")
        $hero("#(She's back!) Wait a minute, miss. Miss! What about school?")
        $daphne("~55 00 1 pur// I don't think that pureblood witches have to strain to make an assessment of some teachers with questionable pedigree.//"
            "~37 00 1 dis// Let this push all mugridge like krasnogrosk Granger.//"
            "I know that I am the best.")
        $hero("Hmm. Then the path to popularity strike.// But one of purity of blood, is not enough, miss.")
        $daphne("~55 00 1 pou// I thought that too, sir.")
        $hero("Remain, men?")
        $daphne("~73 01 1 ang// What?... Men, sir?")
        $hero("According to your theory, before the depth of which I take my hat off...")
        $daphne("~73 01 1 smo//...")
        $hero("...there are three ways of obtaining popularity.//"
            "As I understand it: for you - blood, mind you - in their studies.//"
            "Are men - they can tip the scales in one and in other side.")
        $daphne("~55 00 1 pou// Uh...// But, sir, I don't think I have to jump out of the panties, to achieve the favor of some guys.")
        $hero("#(Hehe, to jump out of the panties is a nice metaphor. Think soon you will be one to jump out, honey).//"
            "Well, miss. Then at the competition, these guys will vote for their raznotravya girlfriends,...// and the girl who deserves the best will fail miserably.")
        $daphne("~37 00 1 pou// Sir as you can!")
        $hero("I Just really hope that you will reconsider your views, miss Greengrass.")
        $daphne("~26 00 1 ope// Professor Dumbledore! Don't forget that my ancestor was Salazar Slytherin!")
        $hero("The one who founded the Department in which you study, you think?")
        $daphne("Yes, sir, and you know better than I do!")
        $hero("Probably still not very good. Remind me, please, what are the qualities of slitherine")
        $daphne("~55 neu 01 1// Cunning, ambition, resourcefulness, sir.")
        $hero("And how you have demonstrated these qualities to achieve victory in the competition (for example, relative to men)?")
        $daphne("~55 01 1 pou// .........................")
        $hero("you will have to Go and think, if you are worthy of his great ancestor!//" 
            "However, because you worked hard, I think it would be wrong to leave you without a gift.")

    if daphne.whoring<=2:
        $daphne.whoring=event._finishCount+1
    call daphne_pre_menu
    return event.Finalize()