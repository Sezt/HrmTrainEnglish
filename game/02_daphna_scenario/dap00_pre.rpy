################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label daphne_pre_01: #Снейп обещает, что пришлет шлюху

    $snape.State(pos2=gMakePos( 340, 420 )).Visibility("head", transition=None)
    $hero("Look, Severus. You promised to send me a couple Slytherin sluts.")
    $snape("~29// Umm...")
    $hero("What do you mean «Umm»?... I know you have some sluts!// You recently bragged about being able to do whatever you want with these whores.")
    $snape("~03// You see, my friend, it is not that simple.//~04// These girls... they're convinced that... well, that the Headmaster is not aware of our small deals.")
    $hero("And?")
    $snape("~03// And if it becomes known that the Headmaster is no stranger to the pursuit of slu...\nof beauty, it might destroy their worldview...")
    $hero("Listen, buddy. I don't care about ideological whores, I'm interested in very different things.") 
    $snape("~06// Yes, but if they find out about your interests, they may not want to do this anymore.//~16// #(I Hope he will believe this bullshit)//"
        "~29// #Actually I'm not going to send him my whores.//"
        " #Genie, having so much cosmic power and all!//~26// #Who knows how that would affect them.")
    $hero("You think I'll believe this bullshit?")
    $snape("~05//What the fuck?//~04// My friend! I care about you! They really might stop offering their services!")
    $hero("Offering to who, buddy?// To you?// I think you just like to be the only rooster in the henhouse.//"
        "I don't sleep at night, working so hard to train the girl,...// and you hump like a rabbit and don't want to help me with a little entertainment.")
    $snape("~01// What's wrong with that?!// ~02//I heard you have a very good track record with miss Granger.")
    $hero("Do you want to switch? I'm ready to let you educate that girl for just a couple of whores.") 
    $snape("~29// Em...")
    $hero("I warn you, Severus, if you continue to hide girls from me,...// the Headmaster may stop hiding in his tower and come out on a quest!")
    $snape("~01// But you can't!..")
    $hero("Keep up the cockblocking and you will see if I can or not...")
    $snape("~06//......")
    $hero("......")
    $snape("~02//............")
    $hero("............")
    $snape("~23// Okay, okay...// You have me convinced. I'll send you a slut.")
    $hero("Two whores, Severus.")
    $snape("~28// I'm sure the one I have in mind will be better then two common whores.")
    $hero("Look, if this is some kind of freak...")
    $snape("~01// What do you take me for!// A pure blood descendant of Merlin, who was on the cover of \"Witch\"...//"
        "~02// #(she is qiute something in a lot of ways)// ~01// ...cheerleader for Slitheryn, as well!//"
        "~23// A petite girl - yum!")
    $hero("Alright, ...nice...// So what's the catch?")
    $snape("~05// The catch?")
    $hero("You're agreed too quickly. So I ask: what's the catch? ")
    $snape("~23// No catch, my friend!// ~02//You will see for yourself. Give it a few days. Just a couple of days!")
    $snape.Visibility()
    "> You decide to trust Snape and wait two days."
    "> The rest of the evening you listen to the cries of Severus\n about the plight of the teachers and\n fantasize about the promised whore."

    $wtevent.Finalize("day_start")
#    jump day_start


label daphne_pre_02: #LV.1 (Whoring = 0 - 2)
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    $daphne.Visibility()
    menu:
        "\"Who?\"":
            $daphne(who, "Sir, Professor Snape sent me...")
            $hero("#(Excellent! The slut has arrived!)// #(Hopefully, she is great. However, after so many days of abstinence I'm not that picky.)// Yes, come in!")
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



    $daphne.State(pos="door").Visibility("body+")("~55 00 1 smi// Good afternoon, Professor Dumbledore.") 
#    $hermi.Visibility("body+")(".....")

    $screens.Show("ctc").Pause().Hide("ctc")

    $hero (m, "#(Oh, what a specimen! I love leggy blondes!...)",g9,"#(...and also brunettes and redheads. I am sure she could help me cum!)",m," #(The tits might be too small. Maybe I could use a grow spell?..)", 
        g4, "#(No, Ginny, control your fantasies. Remember what happened when you tried to enlarge the tits of the Princess....hmm)", 
        m, "Hello, miss uh...// #(Great Sands, he didn't mention her name?).") 
    $daphne("~55 00 1 def// Professor Snape said that you wanted to see me.") 
    $hero ("Oh yeah, girl! Off course, I wanted to see you.// But, did he say, why he sent you?") 
    $daphne("~55 00 1 smi", "No, sir. He didn't say.") 
    $hero ("#(I think we need to start with a little chat. Just to warm up.)") 

    menu: 
        "Talk about education": 
            $hero ("well, miss, I wanted to talk to you about your studies.") 
            $daphne("My education is not what worries me, sir.// ~37 n0 1 def// I am much more interested in why Hogwarts enrolls mudbloods.//" 
                "Are you a pureblood wizard, sir?") 
            $hero (g4, "Who? Me?.. Ah, Yes. Sort of.") 
            $daphne("~37 00 1 pur", "Hmm. You seem confused.// The Greengrass linage is without historical equal and you should not know that.") 
            $hero (m,"#(What is she talking about... greengrass?)// #Rhymes with ass... probably not important.)") 
            $daphne("~37 00 1 pri", "But be that as it may, sir. Mom said you were supposed to make sure that mudbloods didn't have it too easy.", 
                "And instead, every new year, //~46 neu 01 1// pureblood girls are forced to work with them.") 
            $hero ("Pureblood girls?") 
            $daphne("~26 00 1 neu", "Yes, sir! Why does this Mudblood girl have the best grades?//"
                "Why are mudbloods even allowed to learn together with the true wizards?//" 
                "~55 00 1 pri// I can tolerate being around Malfoys or Parkinsons.//" 
                "Their family is so-so, second grade linage. But these commoners, and that girl!!!") 
        "Talk about your house": 
            $hero ("well, miss, I wanted to talk about your house.") 
            $daphne("~37 00 1 def", "The situation in my house, sir? It is disgusting!// Damned mudbloods invade Hogwarts.") 
            $hero ("#(What's going on?..)") 
            $daphne("~55 n0 1 ope", "And you pretend not to notice. Your father on the other hand...// Mother told me that he was a true pureblood wizard and not afraid to kill three Muggles. They even put him in Azkaban.") 
            $hero  ("Really? #(It seems the Headmaster is related to a murderer!)") 
            $daphne("~55 00 1 dis", "Don't pretend you don't remember, sir!// Forgetting that would not improve my opinion of you!", 
                "~55 00 1 pou// Greengrass always stood for purity of blood and when I see a wizard who betrays our ideals...")  

    $hero ("#(Uhh, great energy! Interesting if she Fucks just as vigorously?)// Wait, miss, this is all very exciting, but can we finish the foreplay and get down?") 
    $daphne("~64 00 1 smi// get Down to what, sir?") 
    $hero ("Well you know... fucky-fucky, titty-licky?") 
    $daphne("~64 w0 1 pur", "\"Fucky-fucky\", sir?") 
    $hero ("I don't know what you girls call it.// What you do with Professor Snape and why he sent you here.") 
    $daphne("~64 w0 1 pou// I don't understand, sir.") 
    $hero ("By the great Sands of the desert!// #(Her brain moves a bit slow. Hope her hips move faster.)//" 
        "I mean, do what you usually do slu...girl") 
    $daphne("~55 00 1 dis// What are you insinuating?!") 
    $hero ("What? I am not just going to say it!...") 
    $daphne("~37 s0 1 dis", "If you dare to hint at me doing something untoward with teachers, thats disgusting!") 
    $hero ("#(Uhmm, Snape, is this a joke?)") 
    $daphne("~37 s0 1 ope", "I will send an owl to my parents and report on the dirty things you are of asking me.", 
        "And they will inform the Ministry, I am sure.") 
    $hero (g4, "#(I can't believe it!... Bloody Snape!!!)// Um, wait, miss, you misunderstand!") 
    $daphne("~55 s0 1 dis// I don't think so! You won't stay in that chair for long!")

    $music()
    $screens.HideD3("bld1")
    $daphne.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    $hero("...................................")

    return wtevent.Finalize()

label daphne_pre_03: #Разборки со Снейпом после того, как шлюха оказалась не шлюхой

    $screens.Hide("snape_main")#.Pause(0.3)

    if not daytime:
        $hero(m, "Enjoying your drink, buddy? Sitting comfortable?// Then, tell me...")
    $hero(g1, "What was that?!.. Answer me, in the name of the fucking desert!")

    $snape.State("doorleft")("~01").Visibility("body" if daytime else "head")

    $snape("~05// What are You talking about, my friend?")
    $hero("Don't be stupid! I asked you for a whore, you fucker, and what did you send me?")
    $snape("~03// Well, technically she's a whore.")
    $hero(m, "What does that even mean...technically she's a whore?")
    $snape("~13// Well, she has everything you need for whores. All the right...parts. And so full of energy!")
    $hero("Yes, the energy was hard to miss.")
    $snape("~20// I would gladly sleep with her.")
    $hero("I would have enjoyed that as well...",g4," Wait, so you haven't fucked her?!")
    $snape("~02// What do you take me for, my friend? Why would I offer you a used product?// Pureblood...")
    $hero(g4, "Enough about bloody purebloods!")
    $snape("~23// Thoroughbred untouched young sorceress who is just waiting for someone with experience.")
    $hero(m,"And you decided I was best suited for that role.")
    $snape("~02// Well, you work pretty well with Hermione Granger. I was sure that Daphne Greengrass was not too much for you.")
    $hero("If you had at least warned me, I could maybe have come up with something.//"
        "But now this young bitch will squeal to her parents and an Ministerial inspection is the least we can expect.//"
        "I warn you, if I they remove me from this office, you will follow soon after #(if I can't find a way to slip away before)")
    $snape("~06// Overly dramatic, my friend. I talked with miss Greengrass, and she won't announce anything to her parents.// Trust me.")
    $hero("You haven't been that trustworthy so far, fucking sand...//"
        "I'm not asking how you did it. And yet, forgive my curiosity,...//"
        "...if you get along so great with this bitch,...// why haven't you fucked her yet?!")
    $snape("~29// My friend. It's one thing to convince an arrogant bitch that rumours around such a sensitive subject as her innocence, are not in her interest.//"
        "And quite another to get in her pants.// ~23// I want to give that honor to you.")
    $hero("I'm Not going to meet her again!")
    $snape("~29// I'm afraid you have no choice.")
    $hero("I see...// What aren't you telling me?")
    $snape("~10// I don't want to but more pressure on you, my friend.// So just let events take their course. It will pay off.//"
        "But I would already start thinking about how to score such a charming girl from an ancient and noble family.//"
        "~03// Now if you'll excuse me, I must go.")

    $screens.Hide("snape_02", "bld1", d3 )
    $snape.Visibility(transition=d3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $wtevent.Finalize("night_start" if daytime else "day_start")



label daphne_pre_05: #Разборки со Снейпом после письма от родителей Дафны, само письмо лежит в 15_mail:daphne_pre_04

    $screens.Hide("snape_main")#.Pause(0.3)

    if not daytime:
        $hero(m, "I did Not expect this from you, buddy...")
    $hero(m, "You set me up!")

    $snape.State("doorleft")("~01").Visibility("body" if daytime else "head")

    $snape("~05// Calm down, my friend, calm down. It was the only possible solution.")
    $hero("Oh, really?")
    $snape("~03// Of Course. Those Greengrass snobs...they are ready to take the girl out of Hogwarts.")
    $hero("Excellent! That solves all our problems.")
    $snape("~01// I think there is a very good chance that she will tell her parents a story about how you found your way to her room.// And they will be more then angry. Think about that.// But while she is here...")
    $hero("Correct, she's here and can now see me every day.// She was ready to explode! You think she will forget all about it?")
    $snape("~10// I think you've lost your touch, my friend.// It is not that she CAN see you, and more the fact that she is REQUIRED to come to you, when you tell her to.//~20// Training opportunity?//"
        "Until the holidays she's all yours, you have been given another chance.// And I believe that you will take full advantage of this chance.")
    $hero("You're a damn bastard Severus Snape!// I have to work my ass off to fuck two girls, and you are swimming in easy sluts.")
    $snape("~02// Yes, we each have a destiny, my friend.")
    $hero(g4, "Screw you!.. you are controlling all of this.")
    $snape("~09// I am just trying to fulfill your desires.// If you followed our original plan and just trained miss Granger, none of this would have happened.//"
        "~06// But you wanted more, my friend and I did everything in my power.")
    $hero(m,"It was in your power to send me an ordinary slut!")
    $snape("~05// The next day every student in Hogwarts would talk about the Headmaster abusing his position.//"
        "~06// When these sluts are not busy using their mouths for useful jobs, they gossip and this will spread faster than the hiccups spell.//"
        "~13// But if you convert miss Greengrass, you can wreak her like a slut, and outside your office she will be quiet, arrogant and noble.//"
        "~22// That girl is too obsessed with her blue blood and reputation to reveal anything.")
    $hero("\"If\" is the key word here, buddy. But if it fails? What help are to me then?")
    $snape("~23// Hm...my friend, I don't mind helping you. If you need anything...")
    $hero(m,"Yeah, I need something. Tell me everything you know about her!")
    $snape("~03// That would be boring. How about I send you an owl with a copy of my file on her.// I take things serious when researching sluts.//"
        "~04// But also, I think you need to read some advanced books about how to treat girls of her kind.// Again, there is also a special potion...")
    $hero("Potion?! I will need more info about that...")
    $snape("~06// All the info needs to be found in books, my friend.")

    if not daytime:
        $snape("Let's not ruin such a wonderful moment and just have a drink.")
        "> You are trying to learn more from Snape, but he just downs liquor in large amounts - looks like the students seriously got to him."
        "> In the end, he starts screaming that all he need is cigarettes and alcohol. You could barely pacify him and send him to bed."
    else:
        $snape("I have a Gryffindor potionclass in 5 minutes, so I need to leave, my friend.")



    $screens.Hide("snape_02", "bld1", d3 )
    $snape.Visibility(transition=d3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $wtevent.Finalize("night_start" if daytime else "day_start")


label daphne_pre_07: #Разговор с Гермионой о Дафне. В зависимости от ветки и развращенности реакция. 
# После того, как будет получена информация о выпивке Дафны ивент заканчивается. А так с интервалом в 3 дня при попытке поговорить возобновляется.
    
    $hermi.State("door").Visibility("body+")
    $music("music/Chipper Doodle v2.mp3") # fadein 1 fadeout 1 # HERMIONE'S THEME.
    $hero (m, "I would like to talk to you, miss, about some of the girls from your school.//")
    if not event.IsExec( 1, "start1"): # If not a day passed since the beginning of the very first start, i.e. this is the first start
        $hermi("~body_04.png// Who do you want to talk about?") 
        $hero ("Yes, well...not someone specific...") 
        $hermi("~body_06.png// I don't understand, sir. The school has a lot of girls.") 
        $hero ("Let's start with the first one that comes to mind. Who is the first...") 
        $hermi("~body_01.png// Alphabetically, sir? Alicia.") 
        $hero ("Great Sands! Not following the alphabet...the highest ranked girl...")
        $hermi("~body_84.png// Oh, sir! I understand. You want to talk about me, because I am the first in academic achievement. But you hesitated...// this... This is so touching...") 
        $hero("No, No! This is about Daphne Greengrass.") 
        $hermi("~body_185.png// I don't understand, sir. Why is she first?") 
    else:
        $hermi("~body_09.png// You want to talk about Daphne again?")

    $hero("Nevermind, just tell me about her.") 
    $hermi("~body_09.png// Hmm...// I hate to talk about her. She is a pureblood braggart.")
    $hero("Any more information?") 
    $hermi("~body_03.png// What kind, sir?")
    $hero("Well, maybe some... how should I put this... weaknesses?") 
    $hermi("~body_05.png// Sir! You think I would rat out another student! That is beneath me!")

    if hermi.whoring<12:
        $hermi("~body_04.png// I will leave immediately!")
        $hermi.liking-=30
    else:
        $hero("Miss Granger, hold on. Please remember that Daphne is Slytherin, and by providing this information you are helping Gryffindor.//"
            "Especially if she has any dark secrets, then you would have to tell me. And I guess she would have to be punished.") 
        $hermi("~body_29.png// Still, sir, it's...")
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            $music("Supergirl")
            $hermi("~body_206.png// All this seems very reminiscent of the methods of MI6, sir. You wouldn't happen to work as a spy?") 
            $hero ("Very funny!") 
            $hermi("~body_186.png// Go ahead and laugh, sir. I'll send an owl to Mr. and Mrs. Greengrass, with a letter stating that you ferret out obscene information about their daughter.") 
            $hero (g4, "Wait! Who said \"obscene\"? I haven't said anything like that!") 
            $hermi("~body_100.png// You did not say, sir. But I know what you are thinking!") 
            $hero (m, "In the name of the fucking sands! Well, I know what you are doing. You want more points?") 
            $hermi("~body_186.png// Ten points, sir...") 
            $hero  (g9, "Ha! Is that all? Why all the fuss.") 
            $hermi("~body_195.png// For each of her visits.") 
            $hero (g4, "What? For each?... but what if she... uh...") 
            $hermi("~body_83.png// If she won't visit, sir? Well, that is not my problem. And also ten persent of your income.") 
            $hero (g4, "By the Great Sands! Why do you need money, girl? You're here on a full scholarship!") 
            $hermi("~body_111.png// A girl can have some personal desires, right?") 
            $hero (m, "Miss Granger, lately you are behaving...") 
            $hermi("~body_206.png// Are you dissatisfied with something in our arrangement, sir?")
            $hero (m, "#That's almost blackmail!") 
            $hermi("~body_186.png// Sir?")

            menu: 
                "\".....Agreed!\"":
                    $hermi.SetValue("incomePercent",10)
                    $hermi.SetValue("pointsPerDaphneVisit",10)
                    $hero ("Hmm....pretty satisfied. Alright, miss Granger, now tell me.")
                    jump daphne_pre_06_OK

                "\"No thanks, miss, no deal!\"":
                    jump daphne_pre_06_Cancel

        else:
            $hermi("~body_29.png// Sir, you like her, huh?")
            $hero("Don't be ridiculous, I just want the information.") 
            $hermi("~body_69.png// I am amazed that you have taken notice of this... this bitch, sir.//"
                "She looks down her nose at and ignores everyone, because no one is pureblood enough.//"
                "~body_120.png// Strange that she became a cheerleader. Seems low to dance half-dressed in front of a crowd of half-breeds and Mudbloods.")
            $hero("Anything else?") 
            $hermi("~body_29.png// Still you like her...// ~body_50.png// You want to get to know her, sir?")
            $hero("What? What are you talking about?!") 
            $hermi("~body_30.png// I'm just saying what's on your mind!//"
                "It's disgusting, sir, that you want anything to do with this student. And where?! In this very office, where...//")
            $hero("#...where the Headmaster and pupil are boning.") 
            $hermi("~body_191.png// You said something, sir?")
            $hero("Nevermind. But you are here doing something with me, miss Granger. Is that disgusting as well?") 
            $hermi("~body_206.png// Yes, don't think I like it!// But it can be justified, it is for the benefit of proud Gryffindor!//"
                "~body_30.png// And then you just want to fuck her... her! HER!!!...") 
            if hermi.liking>0:
                $hero("Miss Granger, you know that I appreciate you above the other students.")
                $hermi("~body_29.png// I... I think so, sir. But after what's going on here, how can I trust you?") 
                $hero("What do you mean, miss?")
                $hermi("You know, sir. All these questions...and everything else.") 
                $hero("Miss Granger...")
                $hermi("~body_50.png// Alright, sir. I will tell you what you want to know. To help you understand what a trashy girl she is.//"
                    "~body_61.png// Of course, that won't slow you down...// But I have one condition!") 
                $hero("................?")
                $hermi("~body_47.png// That girl must not visit you more then once every other day!")
                menu: 
                    "\"Have it your way...\"":
                        label daphne_pre_06_OK:

                        $music("Daphne Privacy")
                        $daphne.SetValue("visitInterval",48)

                        $hermi("~body_50.png// Well alright...// You will soon learn that your sweetheart is real bitch.")
                        $hero ("Miss Granger! She's not my sweetheart.")
                        $hermi("~body_120.png// Well, your bitch then.")
                        $hero ("She's not...")
                        $hermi("Maybe not yet. Isn't that the goal?")
                        $hero ("Miss! You forget your place! Any more info...")
                        $hermi("~body_103.png// As you wish, sir. Now, this... person has no friends except a single cow.")
                        $hero ("A cow?")
                        $hermi("~body_186.png// Excuse me, sir, I am talking about Pansy Parkinson. And friends would be a stretch - not purebred enough for her.//"
                             "No boyfriend. In her spare time she roams the halls with a thoughtful expression.//"
                            "~body_61.png// She loves to talk about purity - everyone is already sick of it, even her fellow Slytherin students.//"
                            "~body_120.png// At the last fall ball she got drunk as fuck, excuse my language sir, but that is the most accurate description.//"
                            "Although she claimed she didn't swallow anything.//"
                            "~body_111.png// If she swallows anything else, that I don't know, sorry.")
                        $hero ("Miss Granger! Don't be obnoxious! Are you jealous?")
                        $hermi("~body_66.png// Jealous? Of who, sir? //~body_186.png// HER?// Nonsense... // ~body_193.png// I'm just telling you how things really are.")
                        $hermi("~body_83.png// Will you allow me to continue?..// She loves getting praise. Especially about her looks.// ~body_111.png// And this despite the fact that her boobs can only be seen with a magnifying glass...")
                        $hero ("Hermione Granger!")
                        $hermi("~body_50.png// Sir, no need to get worked up, it is true! I can watch them in the showers as you know!")
                        $hero ("Without a magnifying glass?")
                        $hermi("~body_195.png// I got very lucky, sir, she dropped her towel right in front of me.//"
                            "~body_100.png// Well...// She seemed pretty embarrassed about bending over to pick it up.//"
                            "~body_111.png// If she bends over in other situations, is unknown to me.")
                        $hero ("Miss!")
                        $hermi("~body_100.png// She is still afraid of her mom and is afraid that people will slander her linage.//"
                            "Not the common people - she is not interested in their opinion.// Her family does not read \"The Daily Prophet\" - That newspaper is not sufficiently aristocratic.//"
                            "Instead, they read the \"Pureblood Post\" that writes about the grand balls, status and compare the length of the genealogical trees.//"
                            "~body_50.png// I think that is it is I know, sir...//"
                            "~body_103.png// Ah! Her owl Puglia only eats live food and swallows it whole. Don't know if you found that interesting...")
                        $hero ("Hmm... Thank you, miss Granger.")
                        $hermi("~body_50.png// Hope you got what you wanted, sir. And now I have to go.")
                        $wtevent.Finalize()

                    "\"No!\"":
                        label daphne_pre_06_Cancel:
                        $hermi("~body_206.png// Alright. In that case, sir, my answer is no!// I have to go...")
                        $hermi.liking-=30
            else:
                $hermi("~body_191.png// I would never help you with this, sir!..// I have to go!")
                $hermi.liking-=30
    call music_block
    $hermi.Visibility()
    jump hermione_goout



label daphne_pre_finish: #LV.1 (Whoring = 0 - 2)
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock!*"
    $daphne.Visibility()
    if IsNextRun(): # Начиная со второго посещения, Дафна в форме чирлидера
        $daphne.ItemSetsCustomize({"body","cheer_start_clothes"},True)
        $daphne.ItemsCustomize(update={"combi:cheer_topbase", "skirt:cheer_long"}).chibi.State(appearance="b")

    menu:
        "\"Who is it?\"":
            $daphne("This is... This is Daphne Greengrass, sir. Can I come in?")
            $hero("Yes, come in!")
        "\"Yes, come in...\"":
            pass


    
    $music("Daphne Theme")
    $daphne.chibi.State("door", speed="go").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")

    $daphne.State(pos="door").Visibility("body+")("~55 00 1 smi// Good afternoon, Professor Dumbledore.") 

    $screens.Show("ctc").Pause().Hide("ctc")


    $daphne_pre_menu_text=None # текст, который будет говорить джин в конце
#    label daphne_pre_finish_menu:
    if wtevent._finishCount==0: # Первый раз
        $hero (m, "#(Well, \"Miss Blue Blood\"...our first meeting and my conversations with Severus and Hermione gave me a few ideas.)") 
        $daphne("~55 00 1 ope// My parents sent me an owl about what you had planned for me.// So I decided to stay at Hogwarts.") 
        $hero (m, "#(Yes, dear, I have a lot of plans for your future.)") 
        $daphne("~55 00 1 pur// Frankly, I'm not that thrilled with this idea...// ...// Sir?...") 
        $hero ("To be honest, me neither, miss.") 
        $daphne("~64 w0 1 ope// What?!... you are unhappy about this?") 
        $hero ("Hmm. Of course, I could help you, especially because you immediately stand out from the crowd. You have taste and style.") 
        $daphne("~55 w0 smi 1// True, sir?") 
        $hero ("Yes, miss. I could try to hide from you the fact that you are special. But I think you are better than that.")
        $daphne("~55 w0 1 smi// Oh, how right you are, sir!// You... you have penetrated to the core of the issue!")
        $hero ("#(Not penetrated yet, dear, but it's not that far off.)")
        $daphne("~46 w0 1 def// I Admit, I initially thought that you are unworthy to teach me - the heiress of an ancient family.") 
        $hero ("Hmm...")
        $daphne("~55 w0 1 smi// Sir, now I see that I might have been wrong.") 
        $hero ("#(You don't even know the half or it!)")
        $daphne("~46 00 1 pou// Professor Dumbledore! You immediately noticed that I am special!//~37 00 pou 1// Those mudbloods on the other hand...") 
        $hero ("#(Great Sands, not that again! Need to move her train of thought in a more appropriate direction.)// urgh! Miss, it's all about style...// It's a pity that the rules of Hogwarts prescribe uniform clothing.") 
        $daphne("~64 00 1 neu// Yes sir, that's right. I do have great taste, inherited from a long line of pureblood witches.//"
            "~64 00 1 def// If I had the chance, I could show everybody what a real stylish witch is all about!") 
        $hero ("You can have that opportunity, miss.") 
        $daphne("~46 w0 1 smi// How?") 
        $hero ("You're a cheerleader, as far as I know.// Cheerleader uniforms at Hogwarts imply a lot of personality and you can wear that.// I'm ready to play the role of a grateful audience.")
        $daphne("~64 w0 1 ehh// So, sir, you want me to...") 
        $hero ("Yes, you come here in your cheerleader uniform. Bravo, miss Greengrass! I knew you would catch on fast, but didn't think so fast.")
        $daphne("~64 w0 1 dis// Thank you, sir. But wouldn't it be a bit strange, if I came to class in that outfit. That's, um... a bit too carefree.") 
        $hero ("Miss Greengrass, you might be right that is a bit too bold for you to wear it in front of the entire school. But you could start with wearing it when you visit your Headmaster?")
        $daphne("~64 00 1 ope// I'm not sure...") 
        $hero ("I'm excited...Miss!.. your objections are overruled. Next time I expect you in that uniform.")

        $daphne("~55 00 1 def// But you never finished talking about why you are unsure about teaching me, sir.") 
        $hero (m, "Next time, miss. I will be waiting for your visit in two days.// Finally I have a little present for you.") 
        $daphne("~55 00 1 def// .........") 
        $wtevent.Finalize()

    elif wtevent._finishCount==1: # Второй раз
        $hero (m, "Wonderful, miss Greengrass. You look simply stunning.// I am sure any man's...mood will rise when they see you like this.") 
        $daphne("~55 00 1 neu// Please, Professor, I'm hardly happy about the fact that men get excited.//~26 00 pou 1// I knew that if I came to you in this uniform, it would become weird!") 
        $hero ("Hmm. I'm sorry that I expressed delight about your appearance, miss.// You're probably right and I shouldn't distinguish and compliment you.") 
        $daphne("~55 n0 1 ehh// No sir, that's not what I meant. Just...// ~55 s0 1 dis// I would care if some Mudbloods got...") 
        $hero ("\"Aroused\"? Is that what you wanted to say, miss?") 
        $daphne("~55 n2 2 ehh// Um... Well, yeah...") 
        $hero ("But if it was a pureblood it would be quite another thing, right?.") 
        $daphne("~37 n0 2 neu// Sir, our conversation moves in a weird direction!// Please stop this or I will leave immediately.") 
        $hero ("What should I stop with, miss?") 
        $daphne("~46 01 2 pou// Paying this much attention to my outfit.") 
        $hero ("Well, you arrived in that uniform.") 
        $daphne("~46 01 2 ope// But you told me to!") 
        $hero ("#(Feisty little witch!)// Of course, miss, please forgive me.// I promise to pay more attention to what that Mudblood girl is wearing.") 
        $daphne("~73 00 2 ope// No, sir, you got it all wrong!") 
        $hero(".......?// Well, miss, it seems that today is not a good day to start tutoring. Perhaps a gift would lift your mood.") 
        $event.Finalize()

    elif wtevent._finishCount==2: # Третий раз
#        $daphne.ItemsCustomize(delete={"hair"})
#        $daphne.ItemsCustomize(update={"hair"})
        $hero (m, "When you are wearing that uniform, miss Greengrass, it is easy to see that you have a great body. ")
        $daphne("~55 00 1 pri// Sir, you are starting with this again!...") 
        $hero ("I was thinking, why don't you enter the Miss Hogwarts competition?") 
        $daphne("~64 w0 ehh 1// Um... This is... this is very sudden, sir. You really think I could?..") 
        $hero ("I certainly think so. And if you win it will no doubt elevate your status to the top of Hogwarts.")
        $daphne("~64 w0 1 smo// Oh!..") 
        $hero("You have an excellent chance. Especially if you follow the instructions of the Headmaster.") 
        $daphne("~55 00 1 neu// Sir! I don't need your help, I am a pureblooded sorceress directly descended from Merlin.// I would get everything right, without any sort of insider help!") 
        $hero ("Easy, girl, no need to be worked up.// Of course, you deserve to win, and I would without a moment's hesitation give you first place right now.//"
            "But you do realize that many of the contestants will be mudbloods, half-breeds and other freaks.// And they will all be jealous of you. WE can't let you lose.")
        $daphne("~64 00 1 neu// We?") 
        $hero ("The wizards in high-ranked positions. Your loss would harm all of US. You do realize that?") 
        $daphne("~46 neu 01 1// Hmm, I never thought about that...") 
        $hero ("You should, miss...you could teach them all a lesson...") 
        $daphne("~26 n0 1 smo// Oh, sir, that is my greatest dream! Show them their place. To show them who's really the best. All of these girls...//"
            "~26 n0 1 wo// I have so many years at Hogwarts and what? They still can't see who they are dealing with!") 
        $hero  ("Well, miss Greengrass, I like your fighting spirit. And I want to support you with a little gift.") 
        $daphne("~55 00 1 def")
        $wtevent.Finalize()

    elif wtevent._finishCount==3: # Четверты и последний раз
        $hero (m, "Well, miss, I told you about the competition.//"
            "The competitor list has been hung up all around school. And the owl with a note about the event and the current list of participants has already been sent The Daily Prophet.") 
        $daphne("~55 w0 1 ang// Oh, sir, everything is moving so fast...actually I'm not sure... I'm still...//~55 01 1 dis// I need to pull out!") 
        $hero ("What will that look like?//"
            "Yesterday you where are ready and to go back on your word today. Turns out Daphne Greengrass is afraid of Mudbloods?//"
            "However, if that is really what you want, I'll cancel it.") 
        $daphne("~55 01 pou 1// N-no, sir, this is wrong. But I don't know what to do...// ~64 00 1 ehh// Would...would you really help me?") 
        $hero ("Of Course, miss Greengrass, if you do what I say, you have nothing to worry about.// It would be my pleasure to help you have fun.")
        $daphne("~64 00 1 dis/ Fun, sir?//"
            "~64 s0 1 dis// I am not sure whats so fun about being judged by half-breeds ranking you like a breeding bitch...er... cow.") 
        $hero ("Believe me, miss, with some disciplining you would be the best bitch...or cow...to stand on that podium.") 
        $daphne("~26 w0 1 dis// DISCIPLINING, SIR?!!!")
        $hero(g4, "Who said \"disciplining\"?")
        $daphne("You just said!")
        $hero(m, "Oh, no, of course not, miss. I wanted to say \"training\",.//"
            "And not anybody could train a pureblood witch such as you?")
        $daphne("~46 00 1 pou// That's right! If someone tried, they would immediately realize that you can't train a Greengrass!")
        $hero("No, you are right, miss, we will have normal classes. Well, almost normal, given your amazingness, of course.//" 
            "And I'm sure in the end you would had as much fun as you ever had. #(Hehe)") 
        $daphne("~55 00 1 smi// Oh, you think when I finally take your help, like we have been talking about, that I will like it?") 
        $hero (g9, "I assure you that you will, miss.") 
        $daphne("~55 00 1 smo// Then, sir, I'm ready to start. To improve my position.") 
        $hero (m,"Excellent, miss Greengrass, take the rest of they day of. I'll call you when I am ready to start.// And I think you deserve a gift.") 

        $screens.Show(d3, "blktone", "notes")
        $ renpy.play('sounds/win2.mp3') 
        ">Now you can call Daphne Greengrass to your office."
        $screens.HideD3("blktone")

        $wtevent.Finalize()

    label daphne_pre_menu(sayText=daphne_pre_menu_text):
    $item=None
    menu:
        "- Give her a parting gift -":
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
        $daphne("~55 01 1 pri// # He promised me a gift and where is it? Cheapskate...") #Почему-то не срабатывает рот? проверить
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




