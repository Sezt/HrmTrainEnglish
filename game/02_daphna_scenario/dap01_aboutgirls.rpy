################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label dap_request_01: #LV.1 (Whoring = 0 - 2)

    $music("Daphne Theme")

    if IsRunNumber(1):
#    if daphne.whoring<3:
        $hero("Alright, miss, tell me a bit about the girls around you. We need to understand who you are dealing with.")
        $daphne("~55 00 1 neu// Well, in General most of them are pretty uninteresting.// Why would I pay attention to all these upstarts?!")
        $hero("But, miss, if we are trying to elevate you to your proper position, you need to beat all of them.// Knowledge is power. If you know what I mean?")
        $daphne("~46 01 pou 1// I understand... I think.")
        $hero("So I will give you this task: You must keep an eye on the other students.// Pay attention to who is popular and why.")
        $daphne("~37 00 1 ope// Yes, sir. \"Knowledge\"! I get it now...")
        $hero("Find their weaknesses, their disadvantages and, if we are lucky, even some skeletons in their closet...")
        $daphne("~26 00 1 ope// Uh...you want me to spy on them, sir?// ~26 00 1 neu// That would be unworthy of a sorceress directly descended from Merlin!")
        $hero("Strange, I thought you where a Slytherin student?// Is that not your house, dear? You seem more like a straitlaced member of Gryffindor?")
        $daphne("~55 00 1 pri// Hmm...but I...")
        $hero("I'm not suggesting you \"spy\", as you put it.// Just study your classmates. Let me remind you, many of them will be performing at the competition.//" 
            "Let's learn about how they could win and how to make them lose.//"
            "You need to care not only about how beautifully you present yourself on stage, miss, but also your popularity in school.//"
            "The higher it is, the more likely the students will vote for you, and their votes count a lot.")
        $daphne("~46 00 1 dis// Professor. I can't believe my ears!// You want me to grovel before commoners to improve my chances?!")
        $hero("I propose that you try to be are a bit more flexible, miss.// Now concentrate on your simple task and learn about your competitors.")
        $daphne("~46 00 1 pou// Hmm... I'll try, Professor.")
        $hero("Excellent. Report back tonight.")
    elif IsRunNumberOrMore(2):
        $hero("So, miss Greengrass. Today you should study your competitors again.")
        $daphne("~64 00 1 neu// Again, sir?")
        $hero("Well, unless you already know all about them...")
        $daphne("~55 00 1 neu// Not yet, sir.")
        $hero("Then go ahead, will be waiting for your report in the evening.")
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
        $hero("Alright, miss Greengrass, did you succed?")
        $daphne("~55 00 1 neu// Well, I watched Jessie. She seems pretty easy to figure out.")
        $hero ("And?")
        $daphne("~55 00 1 pur// That's all, sir.")
        $hero("And how will it help your situation and let you rise above Jessie, miss? Did you learn anything that could affect her popularity?")
        $daphne("~55 00 1 pou// Not really, no. But the reason I chose her was because she is very popular.//"
            "~55 01 1 pou// Besides, she bragged that she can charm any guy, so I wanted to learn how...//"
            "~37 00 1 pou// Professor, please don't think that I would require any such info!//"
            "I'm better than that! You gave me a job and I thought it was what you where looking for.")
        $hero("I heard that you where better than that, miss.// You belive the job is done then?")
        $daphne("~73 00 1 pou// I think so.")
        $hero("Alright, I am willing to let it slide, because I believe in you.// Since you are a sorceress from an ancient family.// I'm sure you'll do better next time.")
        $daphne("~73 00 1 smo// Thank you, sir, I'll try harder!")
    elif IsRunNumber(2):
        $daphne("~55 00 1 neu// Today, Professor Dumbledore, I decided to approach the issue systematically.")
        $hero("Oh yeah?")
        $daphne("~46 00 1 neu// Yes, sir. I think I'm beginning to understand why some girls are more popular than others.")
        $hero("#(I have a slut theory as well.)// Go head miss, I am listening.")
        $daphne("I have one more thing to check, sir, Before I will be able to tell you.//" 
            "~46 00 1 pou// And today I studied Melissa as she was flirting with some guys.")
        $hero("Really?")
        $daphne("~37 00 1 pur// Disgusting, sir. How can she do it – some of them where half-breeds and even mudbloods!")
        $hero("Can't be!")
        $daphne("Yes, sir, I am sorry to say.")
        $hero("What happened?")
        $daphne("~37 00 1 pri// Guys circled around her, sir!//"
            "~37 00 1 dis// And you know what, I think some of them where even willing to go along with her flirtations.")
        $hero("That is a surprise!")
        $daphne("~37 00 1 pri// I was shocked too, sir!// I never paid attention to stuff like that, never thought about it.//"
            "~37 n0 1 pou// I was sure that the purity of my blood would open all doors and that sort of flirting wouldn't be necessary.//"
            "~37 n2 1 pou// But for some reason today I was standing alone and the guys flew around this girl, like flies on...")
        $hero("honey?")
        $daphne("~37 00 1 pou// I wanted to use a stronger word, sir. But let's go with honey...")
        $hero("And now what, miss?")
        $daphne("~37 00 1 neu// I need time to figure it all out, sir.")
        $hero("Well, miss Greengrass, it looks like you are moving in the right direction. I think you should be rewarded.")
    elif IsRunNumber(3):
        $daphne("I think I understand, sir.")
        $hero("Huh?")
        $daphne("~55 00 1 ope// Popularity is based on your grades, your popularity with boys, and of course, purity of blood.")
        $hero("#(Oh, great Sands! Enough with the platitudes, finally her beautiful mouth says something useful!)// I, um... I see you have done some serious digging, miss, I was not mistaken in you.")
        $daphne("~73 00 1 smi// Thank you, sir.")
        $hero("Well, your purity of blood should be pretty safe.")
        $daphne("~55 00 1 ope// Yes it is sir! The purest blood of anyone at Hogwarts.// ~55 c0 1 ope// The Greengrass family descends from Salazar Slee...")
        $hero("#(She's back!) Wait a minute, miss. Miss! What about your grades?")
        $daphne("~55 00 1 pur// I don't think pureblood witches should depend on assessments made by some teachers with questionable pedigree.//"
            "~37 00 1 dis// Let mudbloods, like that Granger whore, suck up to the teachers.//"
            "I know that I am the better then her.")
        $hero("Hmm. That removes one path to popularity.// I don't think your blood-status is enough, miss.")
        $daphne("~55 00 1 pou// I thought that too, sir.")
        $hero("So your only remaining options is men?")
        $daphne("~73 01 1 ang// What?...men, sir?")
        $hero("According to your theory, that I deeply respect...")
        $daphne("~73 01 1 smo//...")
        $hero("...there are three ways of obtaining popularity.//"
            "What we have learned so far: you blood-status is a positive, your grades are a negative.//"
            "Finally we are left with men - they can tip the scales for or against you.")
        $daphne("~55 00 1 pou// Uh...// But, sir, I am not going to jump out of my panties to gain the favor of some guys.")
        $hero("#(Jump out of her panties, hehe, lovely metaphor. Think that will happen sooner then you think, dear).//"
            "Well, miss. Then at the competition, these guys will vote for their impure girlfriends,...// and the girl who deserves to win will fail miserably.")
        $daphne("~37 00 1 pou// Sir, I can't!")
        $hero("I really hope that you will reconsider your stance, miss Greengrass.")
        $daphne("~26 00 1 ope// Professor Dumbledore! Don't forget that Salazar Slytherin was my ancestor!")
        $hero("The one who founded the house you belong to, right?")
        $daphne("Yes, sir, and you should know that!")
        $hero("Please remind me, what are the qualities of Slytherin")
        $daphne("~55 neu 01 1// Cunning, ambition, resourcefulness, sir.")
        $hero("Have you demonstrated these qualities to achieve victory in the competition (especially regarding men)?")
        $daphne("~55 01 1 pou// .........................")
        $hero("You should go and have a think about if you are worthy of this great ancestor!//" 
            "However, because you worked so hard, I think it would be wrong to let you leave without a gift.")

    if daphne.whoring<=2:
        $daphne.whoring=event._finishCount+1
    call daphne_pre_menu
    return event.Finalize()
