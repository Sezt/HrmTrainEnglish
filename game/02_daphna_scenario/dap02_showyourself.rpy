#########################
######### LEVEL 02 ##########
#########################
####REQUEST_02 Show Your Self####
#########################
label dap_request_02: #LV.2 (Whoring = 3 - 9)
    
    $music("Daphne Theme")

label dap_request_02_complete:
    if daphne.whoring < 3:
        $hero("������ ��� ��� ��� �� ������ � ����� ���������...// ����� �����....")
        call daphne_main_menu_requests
    pass
    if IsRunNumber(1):
        $hero("Alright, miss Greengrass. The time has come to work on your stage presence. Are you ready?")
        $daphne("~55 00 1 def// Yes, sir, what do you want me to do? Walk around?")
        $hero("No, miss, lie down.")
        $daphne("~46 w0 1 def// ...?!")
        $hero(g4, "Oh, I'm sorry, miss, I looked at you and suddenly started daydreaming...")
        $daphne("~37 s0 1 neu// About what?")
        $hero("What? About... about some faculty problems, Yeah...",
            m," And no, we want to start with something less complicated then \"walk or lie down\"...you should reduce the amount clothes you wear.")
        $daphne("~37 c0 1 dis// Clothes, sir? But... I'm already wearing, what my mom would consider, a whore outfit!")
        $hero("Miss Greengrass, the competition is not for your mom. You have to focus on the jury, who expect to see the contestants in suitable outfits.// Of course, you could go to the podium in your usual uniform.//"
         "But I don't think it would show of your style. A minimum of clothes would really show of your appearance to the members of the jury.")
        $daphne("~73 c0 1 pri// But, sir. That is terrible. I will be thought of as a price pony...!")
        $hero("#Hehe, I think \"bitch\" would be better.")
        $daphne("~73 00 1 pri// You said something, sir?")
        $hero("Oh, nevermind, miss. So where would you like to begin?")
        $daphne("~73 00 1 ehh// Well, I can change my top to be a bit more revealing. I hope that is enough?")
        $hero("Miss, it is your competition, your success or your failure. You decide what is enough.")
        $daphne("~73 01 1 pur// Hmm... Well, I hope it is.")

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $daphne.ItemsCustomize(delete={"sleeves"}).chibi.State(appearance="c")#.Refresh()
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("You have lovely hands, miss Greengrass, I've never seen them naked.")
        $daphne("~73 00 2 ang// Oh please, sir.")
        $hero ("The green straps of your bra clash a bit with the rest.")
        $daphne("~73 00 2 pou// But, sir, I figured that I would be almost...")
        $hero("naked in front of a man?")
        $daphne("~73 n2 3 def// Well, yeah...")
        $hero("It's all right, miss. You look very attractive. I think you deserved a small reward.")
        $daphne.whoring += 1
    elif IsRunNumber(2):
        $hero("Well, miss Greengrass. Let's continue to work on your stage presence.")
        $daphne("~55 00 2 def// Should I walk or something else?")
        $hero("Something else! You need to remove another item of clothing.")
        $daphne("~46 00 2 ehh// Well alright, I have long wanted to take off these stockings, I look like a bloody freak.")

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $daphne.ItemsCustomize(delete={"stockings"}).chibi.State(appearance="c")#.Refresh()
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("��� ��� ���������! ��� ������� ��������� ���, ����, ���� �� ������ ������� ��� ��������� ������.")
        $daphne("~46 w0 1 ehh// ���?!...")
        $hero(g4, "��... ��� � �������, ����.",m ,"������� ����� ���������, ��� � ������� ����� ��� ��������.")
        $daphne.whoring += 1
    elif IsRunNumber(3):
        $hero("Alright, miss Greengrass, we are getting close to a pleasant outfit for the compitition.")
        $daphne("~55 00 1 neu// Sir, I thought this was the final look!")
        $hero("Not at all, miss, we still have some work ahead of us. It's time to lose another item.")
        $daphne("~55 00 1 ehh// Like what?")
        $hero("You decide for yourself, miss.")
        $daphne("~26 01 2 ope// You don't think, sir, that I'll show you my underwear?! What would that look like?!")
        $hero("On stage you should only be in what you call underwear, miss.//"
            "By the way, I'm sure YOUR underwear is of the highest quality and matched with your inherent style and grace...//"
            "You shouldn't be ashamed to show that of even in the most elegant enviroment.")
        $daphne("~26 01 smi 2// Uhm...you are certainly right, sir.")
        $hero("#(Fucking Sands, having to watch my language and not blurt out \"On your knees, slut!\")")
        $daphne("~37 00 smi 2// I mean, you are certainly right about my gracefulness...//~73 00 smi 2// Sir?")
        $hero("Huh? Yeah, so I...I would gladly admire your underwear, miss. When you are ready, of course.")
        $daphne("~01 2 73 ehh// Oh... I don't know...is it really graceful, as a sorceress descended from Merlin I should know that!...")
        $hero("#(Not this again. My dick is the only part that is not tired of her...)")
        $daphne("~73 01 2 pur// I'm not ready, sir. But I need to remove something...//~55 01 2 pou// Then I will take this off. Turn around, sir!//~55 01 3 pou// Better yet, I'll turn around.")

        $screens.Show(Dissolve(1), "blkfade") #Completely black screen.
        $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"}).chibi.State(appearance="f")#.Refresh()
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") 
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("Urgh, you decided to show me your erect nipples? I appreciate that, they are excellent!")
        $daphne("~37 00 2 ope// What?! Sir!")
        $hero("Miss Greengrass, you could have taken off your shirt and I would not have been able to see such beautiful details.// But you decided to show me your excitement.")
        $daphne("~26 00 wo 3// What? No! How dare you!")
        $hero("Miss Greengrass, don't be angry, that you get excited when exposing yourself to the man is very good news.// This will not only help you during the competition.")
        $daphne("~26 00 3 ope// That is not because I took off my bra, just so you know!")
        $hero("Hmm. Are you excited about the thought that you will stand in front of an audience in your underwear?")
        $daphne("~26 00 3 dis// Sir, this is going to far!!! I will immediately complain to my parents!")
        $hero("You never told them that you are trying to become Miss Hogwarts.//"
            "They don't even read \"The Daily Prophet\", right?")
        $daphne("~55 s0 3 pou")
        $hero("I suppose you wanted to come home with a victory or keep it a secret if you failed.//"
            "Very unlikely you will be able to hide that from your mother, girl, when you get knocked out in the first round.//"
            "Your enemies or the faculty will take care of that.//")
        $daphne("~37 01 3 dis// ........................")
        $hero("#(������, � ��� �� ������� �������� �����... �� �����, ������� ������� ����� ��������� �� ���� �������, ��� ��� ��� ���������.)//"
            "����, �������, ��� ���������, ������ ���.// �� � ���� ����� ������� � ��� ��������� ������� ��� � ��� ����� ����������.")
        $daphne.whoring += 1
        $daphne.liking-=7
    elif IsRunNumber(4):
        $hero("�� ��� �, ���� ���������, �� ��������� ����������....")
        $daphne("~73 01 1 smi// ....������� ���������.")
        $hero("�� ����������� ������ ���....")
        $daphne("~37 n0 1 pou// ���....// ���-�� �� ���, ���?//~37 00 2 neu// ��� ���� ��� ������ �������....")
        $hero(g9, "#(��� �� ��� ��������)")
        $daphne("~73 00 2 pri// ���, ���?")
        $hero(m, "��.... � ������, ��� ������� ��� ����� ��������� ��������� ��������������� ���� ������ �����.")
        $daphne("~26 00 3 dis// {size=+5}�������?!{/size}")
        $daphne("{size=+5}���, ��� �� �������������!{/size}")
        $hero(".................// � ��� ��� ����� ��� ����������, ��� ��� ��� ��� � ������� �����.....// �� ����� ��������� �� �����.....// ������ ��� ������ ��� ������.....// ������ ���� �������� ���� ���������....")
        $daphne("~55 00 2 dis// ��!...")
        $daphne.liking-=15
        $wtevent.Finalize("daphne_goout")
        $hero(g4, "#(�� ������ �� ������� ��� �� �����, ������)")
    elif IsRunNumber(5):
        if daphne.whoring < 5:
            $daphne("���, � ���� ������ ���� ����...// ������� ��������� �����....")
            call daphne_goout
        pass
        $daphne("..............//~46 00 1 neu// ���, �������� ���� �� �� ��� ����....// ������ �...//~73 01 1 ang// .....� �� ���� ���������.")
        $hero(m, "������ �����....// � �� �������....// ������ ��� ����������, ��� �� ������ � �����....")
        $daphne("~37 n0 1 pou// ....� ���� ��� ������, ���....//~46 w0 1 dis// ��... � �� ���� ���������� � ������ �����, ����� �� ���� �������� ���� ������.")
        $hero("�� �� ������ ���� ���������, ����� ����� ���� ������ ���.")
        $hero("� �� ������ - ��� ������� � ���, ��� �� � ������ �����?// ��� �� �� ������ ��������� �����������....")
        $daphne("~26 00 3 dis// ���������?!....")
        $hero("�� ������������ � ������....// ��� � �������� �������...")
        $daphne("~37 00 2 neu// ��........// ��... � ���� �� ����....// ................")
        $hero("....�� �� ������ ������� ������� ���������.... ���� ���������?!")
        $daphne("~73 n0 1 pri// .................// .....�� ������ ���������.//~46 00 1 neu// �� �����.... ����� ��� ������ ����������.")
        $hero(g9, "#(��-��, ����� � �� ����������)")
        $daphne("~73 01 2 ehh// ....���?!")
        $hero(m, "��... � �����, ��� ��� ����, ��� �� ����������� � ����.// �� ����... ���� �� ������...")
        $daphne("~73 01 2 pur// ��, ��...// ......� ������.")
        $hero("������.....// ....��� ��� �� �� ������ �����?")
        $daphne("~37 02 3 dis// ��... ������� ��...�//~73 00 2 pri// ......������, ���������...")
        $hero(".......................// ������ ��� - ���� ���������...// ��� �� �� �� ������������ �����?")
        $daphne(".....�� ������������ ��, ���?//~73 c0 1 pri// #..........................//~37 00 2 ope// ����� � ����� �� ����� ������....//~37 00 2 neu// ����� ��� ������...")
        "> �� ���������, ��� ����� ������� �� �������� � ����, �� ��� ���-���� ������� ������."

        $screens.Show(Dissolve(1), "blkfade") #������ �����
        $daphne.ItemsCustomize(delete={"combi"}, update={"bra"}) #delete - ����� (������) ����. update - ����� ����.
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") 
        $screens.Show("ctc").Pause().Hide("ctc")

        $hero("������ ���� ���������....// ���������� ���� �� �����?")
        $daphne(".... ���, ���.//~73 01 3 ang// #(�� ����� ���� ��� ������� �� �� ����)")
        $hero("� �� �������...// ����� ��� ������ ����������...")
        $daphne("~55 00 1 neu// ............// ....����� � ����� ������, ���...")
        $hero(g9, "#(����������....)")
        $daphne("~37 s0 2 ope// �-�..... ���....")
        $hero(m, "� ��� ����� �����....// ��� �����������?")
        $daphne("~37 01 1 neu// � ������ �������....// ��....// ....��� �� ��� ����� ����� ����� ������ �� �����.... ����� �����.....// ................")
        $hero("....�� ������ �����, ����� �� ��� ����� ��������, ���� ���������?")
        $daphne("~73 01 3 ang// .....��, ���������.")
        $hero("#(� ����� ��� ����....)")
        $hero(g9, "#(��� ������ � ��� ����������...)")
        $hero(m, "��, �� ����� �����....// �� ������....// � ������....// ������ ����������....")
        $daphne("~37 00 2 neu")
        "> ���� ����� ����� �� ������ �����...."
        "> ��� ���� � ��������, �� ������� � ���� ����."

        $screens.Show(Dissolve(1), "blkfade") #������ �����
        $daphne.ItemsCustomize(delete={"skirt"}) #delete - ����� (������) ����. update - ����� ����.
        pause.5
        $screens.Hide(Dissolve(1), "blkfade") 
        $screens.Show("ctc").Pause().Hide("ctc")

        $daphne("~73 01 2 smi// ���.... ���....")
        menu:
            "\"���� ����� ���������� ���� ���������\"":
                $daphne("~55 00 1 neu// �������, ���...")
                $hero("��....// ��������... ���...�// ���-�� ��� ��� ����������....// �� ��....")
                stop music
                $screens.Show(Dissolve(1), "blkfade") #�� �������� ����� ������ ���� whitefade, �� ���� ����������, ����� � ��� ������. �� ������.
                pause 1.5
                "��� �������� ���� ������� ��������..."
                "�������, ���������..."
                $hero("..................")
                $hero("#(��....)")
                $hero(g9, "#(���������... ��� ������ ������ ��������)")
                $daphne("~55 02 2 ehh// #.....���?!")
                $hero(m, "......?!")
                $screens.Hide(Dissolve(1), "blkfade")
                $daphne("~37 00 2 neu// ...���, �� ���� �������?// ....� ���-�� ������� �� ���?!")
                $hero("��... � ���������...// ������� � ������� ������������....")
                play music "music/Bittersweet Symphony (Instrumental).mp3"
                $hero("#(�� ��, �����....)")
            "\"��, � ������ �������� ��������� ���� ���������\"":
                $daphne("~77 w0 2 wo// {size=+7}���!?{/size}// ��, ������....// ��� ��������� ��� �������...")
                $daphne("~55 01 2 dis//")

                $screens.Show(Dissolve(1), "blkfade")
                $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"})
                $daphne.ItemsCustomize(update={"skirt:cheer_long"})
                pause.5
                $screens.Hide(Dissolve(1), "blkfade") 
                $screens.Show("ctc").Pause().Hide("ctc")

                $wtevent.Finalize("daphne_goout")
                $hero(g4, "������� � ��������....")
                $daphne.liking -= 20
                $wtevent.Finalize ("night_start")

        $hero(m, "������� ���� ���������...// ������... ��� ��� ����� ������ �������� �������.")
        $daphne("....��?!//~73 01 1 smi// .....�������� �� �����, ���������.")
        $hero(m, "#(��....)// #(������ � � ����� ��������....)")
        $hero(g9, "#(....���-�� � ���� �������?!)")
        a6 "�� ��������..."
        a7 "��� ��������� ��-�� ���� �� ��� �������?"
        $hero(m, "#(.....�����)// #(������ ��� �� ����....)// #(� ��� ������....)")
        a6 "���� �� �� ���� ����������������, ������ ����� ������ ��."
        $daphne("~55 s0 1 pou// ��....// ....���������, �� ���� �������?")
        $hero("���..... ��������... � �� �� ����� ���������.// ....�� ���-�� �������?")
        $daphne("~73 02 3 ang// � ������, ��� ����� ��� ��� ������?")

        menu:
            "- ��������� � -":
                $hero("������ ��������� ���� ���������....")
                $daphne("~73 01 1 smi// ������, ���...")

                $screens.Show(Dissolve(1), "blkfade")
                $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"})
                $daphne.ItemsCustomize(update={"skirt:cheer_long"})
                pause.5
                $screens.Hide(Dissolve(1), "blkfade") 
                $screens.Show("ctc").Pause().Hide("ctc")

                $daphne.liking += 3
                $hero("�� ������� ���� ���������...// �� ������� ������ �����������, � ������������ ���������....")
            "- ��� ����� ������ -": #������� ������������, ����� ����������, � �� � ���������(����� ������ � ������ �����). ��� ����?
                $hero("��������� �� ��� �����....// � ���� �� ��� ���������� �� �����...")
                $daphne("~37 00 2 neu// ��... �� ���� ��� �����, ���...")
                pause 1.0
                felix "� �������� ���������, ������ �������� ����� ���� �������� ������ �� ����� �������..."
                felix "{size=-3}(��, ��� �������� �������� ������ �������� �����){/size}"
                felix "�������� ���� �������, ������������� � ��������� �� ����� {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}������{/a}."
                felix "��� �� ��������������� ���, � ����������� �������� �������. :)"
            
                $screens.Show(Dissolve(1), "blkfade")
                $daphne.ItemsCustomize(delete={"bra"}, update={"combi:cheer_topbase_withnipples"})
                $daphne.ItemsCustomize(update={"skirt:cheer_long"})
                pause.5
                $screens.Hide(Dissolve(1), "blkfade") 
                $screens.Show("ctc").Pause().Hide("ctc")
            
                $hero("�� ������� ���� ���������...// �� ������� ������ �����������, � ������������ ���������....")
        $daphne.whoring += 2
    elif IsRunNumber(6):
        pause 1.0
        felix "� �������� ���������, ������ �������� ����� ���� �������� ������ �� ����� �������..."
        felix "{size=-3}(��, ��� �������� �������� ������ �������� �����){/size}"
        felix "�������� ���� �������, ������������� � ��������� �� ����� {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}������{/a}."
        felix "��� �� ��������������� ���, � ����������� �������� �������. :)"
        call daphne_main_menu_requests

    return
