################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label daphne_pre_01: #LV.1 (Whoring = 0 - 2)

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
    $snape("~23// НNo catch, my friend!// ~02//You will see for yourself. Give it a few days. Just a couple of days!")
    $snape.Visibility()
    "> You decide to trust Snape and wait two days."
    "> The rest of the evening you listen to the cries of Severus\n about the plight of the teacher and\n fantasize about the promised whore."

    $event.Finalize()
    jump day_start


label daphne_pre_02: #LV.1 (Whoring = 0 - 2)
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    $daphne.Visibility()
    menu:
        "\"Who is it?\"":
            $daphne(who, "Sir, I sent Professor Snape...")
            $hero("#(Excellent! Whore has arrived!)// #(Hopefully not too scary-looking. However, after so many days of abstinence I'm not very picky.)")
        "\"Yes, come on in...\"":
            pass

    skaz "Sorry to interrupt the most interesting place? "
    skaz "Us too. But this storyline so far finished only up to this point..."
    skaz "(however, you have access to the other storylines)."
    skaz "Leave your questions, thanks and wishes on our {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}ФОРУМЕ{/a}. \nSo you stimulate us and the continuation will appear faster. :)"
    $event.Finalize()
    return
#    jump day_start
