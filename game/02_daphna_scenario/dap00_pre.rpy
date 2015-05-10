################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label daphne_pre_01: #Снейп обещает, что пришлет шлюху

    $snape.State(pos2=gMakePos( 340, 420 )).Visibility("head", transition=None)
    $hero("Look, Severus. You have promised to send me a couple slesinski whores.")
    $snape("~29// Urgh...")
    $hero("What do you mean «um»?... I know you have a whore!// You told me recently boasted that can do what they want with whomever I want.")
    $snape("~03// You see, my friend, all is not so simple.//~04// These girls... They're sure that,... that is, the Director is not aware of our little pranks.")
    $hero("And?")
    $snape("~03// And if it turns out that the Director is also no stranger to the pursuit of potas...\n of beauty, it'll destroy all of their worldview...")
    $hero("Listen, buddy. I don't care about ideology whores, I'm interested in quite other details.") 
    $snape("~06// Yes, but if they find out about your interest, they may not want to do this anymore.//~16// #(I Hope he will swallow this crap)//"
        "~29// #Actually I'm not going to send him hookers -//"
        " #He, his mother, Genie, having steep cosmic power and all that!//~26// #Who knows how good he is in THIS.")
    $hero("You think I'll swallow this crap?")
    $snape("~05//The fuck?//~04// My friend! I care about you! They really can stop giving!")
    $hero("To give someone, buddy?// 't you?// I think you just like to be the only rooster in the henhouse.//"
        "I don't sleep nights, working hard to train the girl,...// and you ride like cheese in butter and don't want to help me with a little entertainment.")
    $snape("~01// What's wrong with that?!// ~02//I heard you have a very good record with miss Granger.")
    $hero("Do you want to switch? I'm ready to give you the education that girls in just a couple of whores.") 
    $snape("~29// Em...")
    $hero("I warn you, Severus, if you will continue to hide from me girls,...// Director may stop hiding in the tower and came out on a quest!")
    $snape("~01// But you can't!..")
    $hero("Keep up the spirit and you will see I can or not...")
    $snape("~06//......")
    $hero("......")
    $snape("~02//............")
    $hero("............")
    $snape("~23// Okay, okay...// You had me convinced. I'll send you a slut.")
    $hero("Two whores, Severus.")
    $snape("~28// I'm sure THAT you will replace two at once.")
    $hero("Look, if this is some kind of freak...")
    $snape("~01// What do you take me!// Pure blood in Merlin knows what generation, was on the cover of the \"Witch\"...//"
        "~02// #(is extreme in the fifth row)// ~01// ...cheerleader who slitherine, finally!//"
        "~23// Girl - yum!")
    $hero("Well, this is her concern... lick...// So what's the catch?")
    $snape("~05// The catch?")
    $hero("You're too quickly agreed. So I ask: what's the catch? ")
    $snape("~23// No catch, my friend!// ~02//You will see for yourself. Give it a few days. Just a couple of days!")
    $snape.Visibility()
    "> You decide to trust Snape and wait two days."
    "> The rest of the evening you listen to the cries of Severus\n about the plight of the teacher and\n fantasize about the promised whore."

    $event.Finalize("day_start")
#    jump day_start


label daphne_pre_02: #LV.1 (Whoring = 0 - 2)
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    $daphne.Visibility()
    menu:
        "\"Who?\"":
            $daphne(who, "Sir, I sent Professor Snape...")
            $hero("#(Excellent! Whore has arrived!)// #(Hopefully, it's nothing. However, after so many days of abstinence I'm not very picky.)// Yes, come in!")
        "\"Yes, come in...\"":
            pass

#    skaz "Жаль прерываться на самом интересном месте? "
#    skaz "Нам тоже. Но данная сюжетная линия пока дописана только до этой точки..."
#    skaz "(впрочем, вам доступны другие сюжетные линии)."
#    skaz "Оставьте ваши вопросы, благодарности и пожелания на нашем {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}ФОРУМЕ{/a}. \nТак вы простимулируете нас и продолжение появится быстрее. :)"
    $daphne.LoadDefItemSets()
    $music("Daphne Theme")
#    $daphne.chibi.SetValue("appearance","a")
    $daphne.chibi.State("door", speed="go", appearance="a").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")



    $daphne.State(pos="door").Visibility("body+")("~55 00 1 smi// Добрый день, профессор Дамблдор.") 
#    $hermi.Visibility("body+")(".....")

    $screens.Show("ctc").Pause().Hide("ctc")

    $hero (m, "#(Oh, what a slut! I love leggy blondes!...)",g9,"#(...and also brunettes, brunette and redheads. I can cum from one of their kind!)",m," #(That's just Tits are too small. Maybe they grow up spell?..)", 
        g4, "#(No, Ginny, curb your fantasies. Remember what happened when you raised Tits Princess... hmm)", 
        m, "Hello, miss uh...// #(Great Sands, why didn't he say her name?).") 
    $daphne("~55 00 1 def// Professor Snape said that you wanted to see me.") 
    $hero ("Oh yeah, girl! No doubt, no doubt wanted to see, yeah.// But, he said, why are you sent?") 
    $daphne("~55 00 1 smi", "No, sir. He didn't say.") 
    $hero ("#(I Think, have a little chat. Just to warm up.)") 

    menu: 
        "Talk about education": 
            $hero ("well, miss, I wanted to talk to you about your studies.") 
            $daphne("Education is not what worries me, sir.// ~37 n0 1 def// I am much more interested why enrolls at Hogwarts Granarolo mugridge.//" 
                "You're a pureblood wizard, sir?") 
            $hero (g4, "Who? I?.. Ah, Yes. Sort of.") 
            $daphne("~37 00 1 pur", "Hmm. You really confused.// On the antiquity of the genus with Greengrassi nobody is equal, and you should feel embarrassed.") 
            $hero (m,"#(What is this... greengrassi?)// #As bawdy rhymes... Probably means some crap.)") 
            $daphne("~37 00 1 pri", "But be that as it may, sir. Mom said you were supposed to make sure that mugrage not feel at ease.", 
                "And you instead, every year new.//~46 neu 01 1// pureblood girls must feel the pinch.") 
            $hero ("Pureblood girls?") 
            $daphne("~26 00 1 neu", "Yes, sir! Why is this called a Mudblood best on the course?//"
                "Why mugatu allowed to learn close to the true wizards?//" 
                "~55 00 1 pri// I can still be around with all sorts of Malfoy or Parkinson.//" 
                "Family is so-so, second grade. But some no christocracy, and this girl!!!") 
        "To talk about the faculty": 
            $hero ("well, miss, I wanted to talk about the situation in the Department.") 
            $daphne("~37 00 1 def", "the Atmosphere at the Department, sir? She is disgusting!// Granarolo mugridge invaded Hogwarts.") 
            $hero ("#(What's this?..)") 
            $daphne("~55 n0 1 ope", "And you pretend not to notice. Although your father...// Mother told me that he was a true pureblood wizard and was not afraid to kill three Muggles. Him and put him in Azkaban.") 
            $hero  ("Really? #(Well, and the gallows in a relationship with a local Director!)") 
            $daphne("~55 00 1 dis", "don't pretend you don't remember it, sir!// But if forgotten, it does you no credit!", 
                "~55 00 1 pou// Greengrassi always stood for purity of blood and when you see a wizard who betrays our ideals...")  

    $hero ("#(Um, great expression! Interestingly, she Fucks just as vigorously?)// Wait, miss, it's all very exciting, but can we finish the foreplay and get down?") 
    $daphne("~64 00 1 smi// get Down to what, sir?") 
    $hero ("Well, to this most... chpok-chpok, titi-Mitya?") 
    $daphne("~64 w0 1 pur", "\"Chpok-chpok\", sir?") 
    $hero ("I don't know how you girls called.// In General, what you do with the Professor and why he sent you here.") 
    $daphne("~64 w0 1 pou// I don't understand, sir.") 
    $hero ("the great Sands of the desert!// #(She slowly moves his brains. Hope that moves his hips faster.)//" 
        "I say, do what you usually do Hor... girls like you.") 
    $daphne("~55 00 1 dis// what are you insinuating?!") 
    $hero ("I'm referring to? Yeah I just say!...") 
    $daphne("~37 s0 1 dis", "If you dare to hint at what some person with teachers, it's disgusting!") 
    $hero ("#(er, Snape, is that a joke?)") 
    $daphne("~37 s0 1 ope", "I shall send an owl to parents and report on the dirty you I'm doing here.", 
        "And so they will inform about it to the Ministry, to be sure.") 
    $hero (g4, "#(can't believe it!... Bloody Snape!!!)// Um, wait, miss, you misunderstood!") 
    $daphne("~55 s0 1 dis// I got that right! And you won't have to sit in this chair!")

    $music()
    $screens.HideD3("bld1")
    $daphne.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    $hero("...................................")

    return event.Finalize()

label daphne_pre_03: #Разборки со Снейпом после того, как шлюха оказалась не шлюхой

    $screens.Hide("snape_main")#.Pause(0.3)

    if not daytime:
        $hero(m, "As you drink, buddy? Fit well, comfortable?// Then, tell me...")
    $hero(g1, "What was that?!.. Answer me, in the name of the fucking desert!")

    $snape.State("doorleft")("~01").Visibility("body" if daytime else "head")

    $snape("~05// what are You talking about, my friend?")
    $hero("don't be sheep! I asked you a whore, your mother, and you tell me who sent you?")
    $snape("~03// Well, technically she's a whore.")
    $hero(m, "What does that even mean technically she's a whore?")
    $snape("~13// Well, it has everything you need for whores. All right um, details. And what an expression!")
    $hero("Yes, the expression was hard to miss.")
    $snape("~20// I would gladly laid on the floor.")
    $hero("I would have it with pleasure...",g4," Wait, so you haven't fucked her?!")
    $snape("~02// what do you take me, my friend? Why would I offer you a used product?// Pureblood...")
    $hero(g4, "About purebred I've had enough!")
    $snape("~23// Thoroughbred untouched young sorceress who is just waiting for someone it has traveled.")
    $hero(m,"And you decided I was best suited for this role.")
    $snape("~02// Well, you're pretty good with Hermione Granger. I was sure that you were not saved before and Daphne Greengrass.")
    $hero("If you, my friend, at least warned me, I would maybe something came up.//"
        "But now this young bitch will squeal parents and Ministerial inspection is the least that we are waiting for.//"
        "I warn you, if I will make from this office, you will put after #(if I can't find a way to slip away before)")
    $snape("~06// Not all so tragic, my friend. I talked with miss Greengrass, and she's not ready to announce anything to the parents.// Bye.")
    $hero("the Word until is particularly encouraging, fucking sand...//"
        "I'm not asking how you did it. And yet, forgive my curiosity,...//"
        "...if you get along so great with this bitch,...// why you still haven't fucked her?!")
    $snape("~29// My friend. It's one thing to convince an arrogant bitch that the buzz around such a sensitive subject, as her innocence, not in its interests.//"
        "And quite another to get in her pants.// ~23// I want to give this honor to you.")
    $hero("I'm Not going to meet her again!")
    $snape("~29// I'm Afraid you have no choice.")
    $hero("I see...// What I don't know?")
    $snape("~10// don't want to pressure you, my friend.// So just let events take their course. Can all cost.//"
        "But I'd already started thinking how to gain a charming girl of an ancient and noble family.//"
        "~03// now if you'll excuse me, I must go.")

    $screens.Hide("snape_02", "bld1", d3 )
    $snape.Visibility(transition=d3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $event.Finalize("night_start" if daytime else "day_start")



label daphne_pre_05: #Разборки со Снейпом после письма от родителей Дафны, само письмо лежит в 15_mail:daphne_pre_04

    $screens.Hide("snape_main")#.Pause(0.3)

    if not daytime:
        $hero(m, "I did Not expect from you, buddy...")
    $hero(m, "You set me up!")

    $snape.State("doorleft")("~01").Visibility("body" if daytime else "head")

    $snape("~05// Calm down, my friend, calm down. It was the only possible solution.")
    $hero("Oh, really?")
    $snape("~03// of Course. These Greengrassi, these snobs... They were ready to take the girl from Hogwarts.")
    $hero("Excellent! It solves all problems.")
    $snape("~01// You think, what is the probability that she will spin a about you what was and what was not, her closed door.// And how they will be pissed. And so regard them. Oh... this can write a book.// And while she's here...")
    $hero("That's it, she's here and can now see me every day.// She was humming as overheated kettle! Think, you'll forget all about it?")
    $snape("~10// I Think you've lost your touch, my friend.// It is not what she CAN see you, and the fact that it is OBLIGED to come to you, because she told her old men.//~20// Capture opportunities?//"
        "Until the holidays she's all yours, you're being given another chance.// And I believe that you will take advantage of this chance by 100%%.")
    $hero("You're a damn hypocrite Severus Snape!// I have to puff to invent, how to fuck two girls, and you'll be entertained with whores.")
    $snape("~02// Yes, we each have a destiny, my friend.")
    $hero(g4, "Oh, you!.. Aren't you all doing this?")
    $snape("~09// I just tried to fulfill your desire.// If you followed our original plan and just trained miss Granger, none of this would have happened.//"
        "~06// But you wanted more, my friend and I did everything in my power.")
    $hero(m,"was In your power to send me an ordinary slut!")
    $snape("~05// the next day the whole Hogwarts discussed what the Director knew him.//"
        "~06// These whores when their mouth is not busy with useful work, and only do what they talk, and gossip spreads faster than the spell of hiccups.//"
        "~13// But if you'll get miss Greengrass, you can tear it like a slut, and outside your office all will be quiet, grandly and nobly.//"
        "~22// That girl is too obsessed with his blue blood to admit what gives.")
    $hero("\"If\" the key word here, buddy. But if it fails? You, incidentally, have not coped with it.")
    $snape("~23// Hm... My friend, I don't refuse to help you. If you need anything...")
    $hero(m,"Yeah, I need something. Tell me about it what you know!")
    $snape("~03// This is so boring. How about I send you an owl with the extracts from my file on her.// I was, seriously when planning to fill up.//"
        "~04// And yet, I think you need to read clever books, to learn to treat girls this kind.// Again, there is a special potion...")
    $hero("Potion?! But from this point on more in detail...")
    $snape("~06// All in clever books, my friend, everything in them.")

    if not daytime:
        $snape("let's not ruin such a wonderful moment and just have a drink.")
        "> You are trying to extract from Snape, something else, but he just gushes liquor cups - looks like the students it seriously got."
        "> In the end, he starts screaming that all he need is cigarettes and alcohol. You could hardly pacify and sent to bed."
    else:
        $snape("I after 5 minutes starts potions in Gryffindor, so I forced you to leave, my friend.")



    $screens.Hide("snape_02", "bld1", d3 )
    $snape.Visibility(transition=d3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $event.Finalize("night_start" if daytime else "day_start")


label daphne_pre_07: #Разговор с Гермионой о Дафне. В зависимости от ветки и развращенности реакция. 
# После того, как будет получена информация о выпивке Дафны ивент заканчивается. А так с интервалом в 2 дня при попытке поговорить возобновляется.
    
    $hermi.State("door").Visibility("body+")
    $music("music/Chipper Doodle v2.mp3") # fadein 1 fadeout 1 # HERMIONE'S THEME.
    $hero (m, "I would like to talk to you, miss, about some of the girls from your school.//")
    if not event.IsExec( 1, "start1"): # If not a day passed since the beginning of the very first start, i.e. this is the first start
        $hermi("~body_04.png// what About the girls?") 
        $hero ("Yes about all sorts of different ways.") 
        $hermi("~body_06.png// I don't understand, sir. At the faculty a lot of girls.") 
        $hero ("just look at the first one that comes along. Who is the first...") 
        $hermi("~body_01.png// alphabetically, sir? Alicia.") 
        $hero ("And here the alphabet, the great Sands! First girl - not this...")
        $hermi("~body_84.png// Oh, sir! I understand. You want to talk about me, because I am the first in academic achievement. But you hesitate...// this... This is so touching...") 
        $hero("no, no! This Is Daphne Greengrass.") 
        $hermi("~body_185.png// I don't understand, sir. Why is it first?") 
    else:
        $hermi("~body_09.png// Again will inquire about Daphne?")

    $hero("Whatever, just tell me about it.") 
    $hermi("~body_09.png// Hmm...// I hate to talk about it. She brags that pureblood.")
    $hero("any More information?") 
    $hermi("~body_03.png// What kind, sir?")
    $hero("Well, maybe some... how should I put this... vulnerable?") 
    $hermi("~body_05.png// Sir! How can you expect me to tell you about another student! It is unworthy!")

    if hermi.whoring<12:
        $hermi("~body_04.png// I will leave immediately!")
        $hermi.liking-=30
    else:
        $hero("Miss Granger, hold on. Please note that Daphne - slitherine, and by providing this information you are helping to Gryffindor.//"
            "Especially if she has no sins, then you couldn't possibly tell. And if there ' I guess she must be punished.") 
        $hermi("~body_29.png// still, sir, it's...")
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            $music("Supergirl")
            $hermi("~body_206.png// All this is reminiscent of the methods of MI6, sir, as show in the series. You wouldn't happen to work for the secret service?") 
            $hero ("Very funny!") 
            $hermi("~body_186.png// Then laugh, sir. I'll send an owl to Mr. and Mrs. Griquas, with a letter stating that you ferret out embarrassing information about their daughter.") 
            $hero (g4, "Wait! Who says \"obscene\"? I haven't said that word!") 
            $hermi("~body_100.png// You did not say, sir. And I'll say it!") 
            $hero (m, "In the name of the fucking sand! Well, I know what you mean. You want more points?") 
            $hermi("~body_186.png// Ten points, sir...") 
            $hero  (g9, "Ha! Is that all? Was worth a fuss.") 
            $hermi("~body_195.png// For each of her visits.") 
            $hero (g4, "What? For each?... But if she's... uh...") 
            $hermi("~body_83.png// If she will not, sir? Well this is not my problem, right? And another 10%% of all your income.") 
            $hero (g4, "the Great Sands! Why do you need money, girl? You're here on full Board!") 
            $hermi("~body_111.png// I can be a little girly desires, right?") 
            $hero (m, "Miss Granger, lately you behave...") 
            $hermi("~body_206.png// You are not satisfied with something in that agreement, sir?")
            $hero (m, "#That's petty blackmailer!") 
            $hermi("~body_186.png// Sir?")

            menu: 
                "\".....Agree!\"":
                    $hermi.SetValue("incomePercent",10)
                    $hermi.SetValue("pointsPerDaphneVisit",10)
                    $hero ("In General,.... satisfied. Well, miss Granger, now tell me.")
                    jump daphne_pre_06_OK

                "\"Go away, miss, with such agreements!\"":
                    jump daphne_pre_06_Cancel

        else:
            $hermi("~body_29.png// Sir, you like her, huh?")
            $hero("don't be ridiculous, I just want the information.") 
            $hermi("~body_69.png// I am amazed that you noticed this... on the bitch, sir.//"
                "She goes down your nose and doesn't notice anyone, because no one has enough pure blood.//"
                "~body_120.png// Strange that she became a cheerleader. It's so low half-dressed, dancing in front of a crowd of half-breeds and Mudbloods.")
            $hero("What else?") 
            $hermi("~body_29.png// still you like it...// ~body_50.png// You want to get to know her, sir?")
            $hero("What? What are you talking about?!") 
            $hermi("~body_30.png// I'm just saying what's on your mind!//"
                "It's disgusting, sir, that you want something to do with his student. And where?! In this very office, where...//")
            $hero("#...where all the Directors are generally and students boning.") 
            $hermi("~body_191.png// You said something, sir?")
            $hero("pay No attention. But I'm here doing something with you, miss Granger. It's too disgusting?") 
            $hermi("~body_206.png// Yes, shockingly, don't think I like it!// But it can be justified, it is for the benefit of a proud Gryffindor!//"
                "~body_30.png// And then you just want to fuck this... this! This!!!...") 
            if hermi.liking>0:
                $hero("Miss Granger, you know that I may distinguish you among other students.")
                $hermi("~body_29.png// I... I think so, sir. But after what's going on here, as I can trust you?") 
                $hero("What do you mean, miss?")
                $hermi("You know, sir. All these Laponia... and everything else.") 
                $hero("Miss Granger...")
                $hermi("~body_50.png// Pretty, sir. I will tell you what you want to know. To help you understand what a trashy girl.//"
                    "~body_61.png// of Course, that for a second you can't stop...// But I have one condition!") 
                $hero("................?")
                $hermi("~body_47.png// That girl must not appear more than once in two days!")
                menu: 
                    "\"Have it your way...\"":
                        label daphne_pre_06_OK:

                        $music("Daphne Privacy")
                        $daphne.SetValue("visitInterval",48)

                        $hermi("~body_50.png// Well...// that your love is real bitch I told you.")
                        $hero ("Miss Granger! She's not my love.")
                        $hermi("~body_120.png// Well, let it be \"Mat\".")
                        $hero ("It's not...")
                        $hermi("Okay, while not a doormat. You will be.")
                        $hero ("Miss! You forget yourself! One more thing...")
                        $hermi("~body_103.png// As you command, sir. Now, this... person has no friends except for a Cow.")
                        $hero ("What a cow, miss?")
                        $hermi("~body_186.png// Excuse me, sir, I about Pansy Parkinson. And even that friend can be called a stretch - not enough purebred for her.//"
                             "No boyfriend. In his spare time he roams the halls with a thoughtful expression.//"
                            "~body_61.png// Favorite conversations about purity - all already sick of them, even slitherine't believe me.//"
                            "~body_120.png// On last Fall ball pissed as fuck, sorry for being rude sir, but the comparison is very accurate.//"
                            "Although claimed almost didn't put in her mouth.//"
                            "~body_111.png// What it takes in his mouth, already sorry, don't know.")
                        $hero ("Miss Granger! You become obnoxious! You jealous?")
                        $hermi("~body_66.png// Jealous? To whom, sir? //~body_186.png// THIS?// What nonsense... // ~body_193.png// I'm just telling you how things really are, don't embellish.")
                        $hermi("~body_83.png// will Allow to continue?..// Loves getting praised. Especially the looks.// ~body_111.png// And this despite the fact that Boobs can be found only with a magnifying glass...")
                        $hero ("Hermione Granger!")
                        $hermi("~body_50.png// Sir, you needn't be troubled, it is true! I could watch them in the shower as you now!")
                        $hero ("find Without a magnifying glass, miss?")
                        $hermi("~body_195.png// I was very lucky, sir, well fell light.//"
                            "~body_100.png// What...// is Very afraid to drop their honor.//"
                            "~body_111.png// Maybe somewhere already dropped, but the details are unknown to me.")
                        $hero ("Miss!")
                        $hermi("~body_100.png// Still afraid of his moms, and she is afraid that people will say - other christocracy.//"
                            "Not all other people - their opinion is not interested in.// Family does not write \"the Daily prophet\" - this newspaper is not sufficiently aristocratic.//"
                            "Instead, read \"Thoroughbred news\" where they write about the balls, routs and measured the length of the genealogical tree.//"
                            "~body_50.png// it is likely that all, sir...//"
                            "~body_103.png// Ah! Even her owl Puglia - eater still the same, and only seeks to devour. Don't know if you found it interesting that...")
                        $hero ("Hmm... Thank you, miss Granger.")
                        $hermi("~body_50.png// Hope you got what you wanted, sir. And now I have to go.")
                        $event.Finalize()

                    "\"Not!\"":
                        label daphne_pre_06_Cancel:
                        $hermi("~body_206.png// whatever. In that case, sir, my answer is no!// I have to go...")
                        $hermi.liking-=30
            else:
                $hermi("~body_191.png// 't Even hope that I'll help you, sir!..// I have to go!")
                $hermi.liking-=30
    call music_block
    $hermi.Visibility()
    jump hermione_goout



label daphne_pre_finish: #LV.1 (Whoring = 0 - 2)
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock!*"
    $daphne.Visibility()
    if IsNextRun(): # Начиная со второго посещения Дафна в форме чирлидера
        $daphne.ItemSetsCustomize({"body","cheer_start_clothes"},True)
        $daphne.ItemsCustomize(update={"combi:cheer_topbase", "skirt:cheer_long"}).chibi.State(appearance="b")

    menu:
        "\"Who?\"":
            $daphne("this is... This is Daphne Greengrass, sir. Can I come in?")
            $hero("Yes, come in!")
        "\"Yes, come in...\"":
            pass


    
    $music("Daphne Theme")
    $daphne.chibi.State("door", speed="go").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")

    $daphne.State(pos="door").Visibility("body+")("~55 00 1 smi// Добрый день, профессор Дамблдор.") 

    $screens.Show("ctc").Pause().Hide("ctc")


    $daphne_pre_menu_text=None # текст, который будет говорить джин в конце
#    label daphne_pre_finish_menu:
    if event._finishCount==0: # Первый раз
        $hero (m, "#(Well, \"Miss Blue Blood\"... Our first meeting and conversations with Severus and Hermione gave me a few ideas.)") 
        $daphne("~55 00 1 ope// Parents sent me an owl, what are you going to do with me.// So I took a position at Hogwarts.") 
        $hero (m, "#(Yes, dear, you I will take very different positions.)") 
        $daphne("~55 00 1 pur// Frankly, I'm not thrilled with this idea...// ...// Sir?...") 
        $hero ("Frankly, I, too, miss.") 
        $daphne("~64 w0 1 ope// What?!... You are also not happy?") 
        $hero ("Hmm. Of course, I could help you, especially because I immediately set you apart from the crowd. You have taste and style.") 
        $daphne("~55 w0 smi 1// True, sir?") 
        $hero ("Yes, miss. Of course, I could hide from you the fact that you were not proud. But I think you are better than that.")
        $daphne("~55 w0 1 smi// Oh, how right you are, sir!// You... you have penetrated to the very depth!")
        $hero ("#(not Yet penetrated, dear, but it's not far off.)")
        $daphne("~46 w0 1 def// I Admit, I initially thought that you are unworthy to teach me - the heiress of the ancient family.") 
        $hero ("Hmm...")
        $daphne("~55 w0 1 smi// Sir, now I understand that it seems that was wrong.") 
        $hero ("#(You don't even know the girl how!)")
        $daphne("~46 00 1 pou// Professor Dumbledore! Here you will immediately notice that I have a special girl!//~37 00 pou 1// this is mugridge, they...") 
        $hero ("#(Great Sands, not that! Need to translate her thoughts in a more appropriate direction.)// Urgh! Miss, it's about style...// it's a Pity that the rules of Hogwarts prescribed uniform clothing.") 
        $daphne("~64 00 1 neu// Yes sir, that's right. But I do have taste, like hereditary, pureblood witch. Such taste, that's just wow!//"
            "~64 00 1 def// if I had the chance, I could have shown them what a real stylish witch!") 
        $hero ("But you have the opportunity, miss.") 
        $daphne("~46 w0 1 smi// There?") 
        $hero ("You're a cheerleader, as far as I know.// Cheerleader uniform at Hogwarts implies some personality and you can show it.// I'm ready to play the role of a grateful audience.")
        $daphne("~64 w0 1 ehh// That is, sir, you want me to...") 
        $hero ("Yes, they came here in the cheerleader uniform. Bravo, miss Greengrass! I knew you caught on fast, but didn't think so.")
        $daphne("~64 w0 1 dis// Spa Xibe, sir. But don't you find that a bit strange, if I came to class in this form. She's, um... a few free-style.") 
        $hero ("Miss Greengrass, you're not weird that you like mad in this form in front of the entire Hogwarts. What is so if you come in her Cabinet to your Director?")
        $daphne("~64 00 1 ope// But I'm not sure...") 
        $hero ("excited by... KGM!.. the objections are not accepted. Waiting for you next time in uniform.")

        $daphne("~55 00 1 def// But you never finished talking, sir, about why not happy and I could.") 
        $hero (m, "next time, miss. We are waiting for you in two days.// And while I have a little present for you.") 
        $daphne("~55 00 1 def// .........") 
        $event.Finalize()

    elif event._finishCount==1: # Second time
        $hero (m, "Wonderful, miss Greengrass. You look simply stunning.// When you look at any men will rise... um. The mood..") 
        $daphne("~55 00 1 neu// You confuse me, Professor. And I'm hardly happy about the fact that men have something there rises.//~26 00 pou 1// I knew that if I come to you in this form, then everything will begin!") 
        $hero ("Hmm. I'm sorry that I expressed delight about your appearance, miss.// You're probably right and I shouldn't distinguish you and make you compliments.") 
        $daphne("~55 n0 1 ehh// No sir, that's not what I meant. Just...// ~55 s0 1 dis// do I care if some Mudbloods something there...") 
        $hero ("\"Up\"? You wanted to say, miss?") 
        $daphne("~55 n2 2 ehh// Um... Well, yeah...") 
        $hero ("But if it occurs at the thoroughbred is quite another thing, miss.") 
        $daphne("~37 n0 2 neu// Sir, our conversation goes in a strange direction!// If you do not stop, I will leave immediately.") 
        $hero ("you don't stop that, miss?") 
        $daphne("~46 01 2 pou// 't Pay me so much attention.") 
        $hero ("nevertheless, you come in uniform.") 
        $daphne("~46 01 2 ope// But not about you I said!") 
        $hero ("#(why still, the witch!)// Of course, miss, please forgive me.// I promise to continue to pay attention to exactly what any Mudblood.") 
        $daphne("~73 00 2 ope// no, sir, you got it all wrong!") 
        $hero(".......?// Well, miss, it seems that today is not a good day to practice. Perhaps a great gift to lift your spirits.") 
        $event.Finalize()

    elif event._finishCount==2: # the Third time
#        $daphne.ItemsCustomize(delete={"hair"})
#        $daphne.ItemsCustomize(update={"hair"})
        $hero (m, "When you are in this form, miss Greengrass, I see you have a great body. ")
        $daphne("~55 00 1 pri// Sir, you are again!...") 
        $hero ("I was thinking, why don't you speak to miss Hogwarts?") 
        $daphne("~64 w0 ehh 1// Um... This is... this is very sudden, sir. You really think I could?..") 
        $hero ("I Certainly would. And what, if not win the contest will lift you to the top?")
        $daphne("~64 w0 1 smo// Oh!..") 
        $hero("you Have an excellent chance. Especially if you will strive the Director of Hogwarts.") 
        $daphne("~55 00 1 neu// Sir! I don't need it, I – blooded sorceress in Merlin knows what generation.// And I have to get everything just so, without any sort of protection!") 
        $hero ("Well, girl, no need to be resent.// Of course, you deserve to be Queen, and I without a moment's hesitation would have given you first place right now.//"
            "But you do realize how much around will be base-born, half-breeds and Frank Sagrada.// And they will all be jealous of you. And WE can't let you lose.")
        $daphne("~64 00 1 neu// We?") 
        $hero ("We are the wizards who are in certain positions. The loss will harm all of US. You do realize that?") 
        $daphne("~46 neu 01 1// Hmm, I never thought about it...") 
        $hero ("you should be, miss... If you are ready to teach a lesson to all nedovrsenom...") 
        $daphne("~26 n0 1 smo// Oh, sir, it is my greatest desire! Show them their place. To show who's really who. All of these girls...//"
            "~26 n0 1 wo// I have so many years at Hogwarts and what? They still couldn't see who you are dealing with!") 
        $hero  ("Well, miss Greengrass, I like your fighting spirit. And I want to support him a little gift.") 
        $daphne("~55 00 1 def")
        $event.Finalize()

    elif event._finishCount==3: # Chetvertyy and last time
        $hero (m, "Well, miss, I told you for the contest.//"
            "Right now the lists are hung on Hogwarts. And the owl with a note about this event and the list of participants already flies in the Daily prophet.") 
        $daphne("~55 w0 1 ang// Oh, sir, everything is so fast... I'm actually not sure... I'm still...//~55 01 1 dis// This needs to be undone!") 
        $hero ("And what will it look like?//"
            "Yesterday, you are ready today and go back on their word. Turns out Daphne Greengrass folded before Mudbloods?//"
            "However, if this is really what you want, I'll cancel it.") 
        $daphne("~55 01 pou 1// N-no, sir, this is wrong. But I don't know what to do...// ~64 00 1 ehh// You... you really do that for me?") 
        $hero ("of Course, miss Greengrass, if you will do what I say, you have nothing to worry about.// You'll even get the pleasure.")
        $daphne("~64 00 1 dis/ Pleasure, sir?//"
            "~64 s0 1 dis// don't know what can be fun when some half-breeds judging you as breeding bitches... er... cow.") 
        $hero ("Believe me, miss, with some training you would like to be bitches... and cows... we have to stand on the podium, Yes.") 
        $daphne("~26 w0 1 dis// TRAINING, SIR?!!!")
        $hero(g4, "Who said \"dog training\"?")
        $daphne("You just said!")
        $hero(m, "Oh, no, of course not, miss. I wanted to say \"training\",.//"
            "And who can come to mind to train such a pureblood witch like you?")
        $daphne("~46 00 1 pou// That's it! If someone tried, he would have immediately realized that Greengrassi not trainable!")
        $hero("no, No, miss, we will have regular classes. Well, almost normal, given your amazingness, of course.//" 
            "And I'm sure in the end you get as much pleasure as never received. #(Hehe)") 
        $daphne("~55 00 1 smi// Oh, you think when I take the position that we were talking about, so I'll like it?") 
        $hero (g9, "I assure you, miss.") 
        $daphne("~55 00 1 smo// Then, sir, I'm ready to start. To get him to take.") 
        $hero (m,"Excellent, miss Greengrass, and still rest today. I'll call you so we can start our play.// And I think you deserve a gift.") 

        $screens.Show(d3, "blktone", "notes")
        $ renpy.play('sounds/win2.mp3') 
        ">Now you can call Daphne Greengrass in the Cabinet."
        $screens.HideD3("blktone")

        $event.Finalize()

    label daphne_pre_menu(sayText=daphne_pre_menu_text):
    $item=None
    menu:
        "- To give her a parting gift-":
            python:
                choose = RunMenu()
                for o in hero.Items():
                    if not o.Name in {"scroll", "ball_dress"}:
                        choose.AddItem("- "+o._caption+" -", "daphne_giving", o.Name)

                choose.Show("daphne_pre_finish_menu")

        "- Never mind -":
            $daphne("Then I'll probably go.")



    label daphne_pre_finish_menu:
    $music()
    if item==None:
        $daphne("~55 01 1 pri// #Promised a gift and where is he? Miser...") #Почему-то не срабатывает рот? проверить
        $daphne.liking-=5
    $screens.HideD3("bld1")
    $daphne.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    if sayText!=None:
        $say(sayText)

#    $hero("...................................")
    call music_block
    return




