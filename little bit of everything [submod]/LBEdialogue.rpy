init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_ddlcmerch",
            category=["ddlc"],
            prompt="DDLC Merch",
            random=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )

label monika_ddlcmerch:
    m 1eud "Hey, [player]?"
    m 3eud "You know how DDLC is a very popular game, right?"
    m 3hubsb "That means there's quite a lot of merchandise around it…{w=0.5} including some of me!"
    m 4eub "And including some pretty out there collabs, such as one with a watch company!"
    m 2lkblsdlb "There's a bunch of figurines, shirts, plushies, pins…{w=0.5} just everything of the sort!"
    m 7hub "If you have the time, you should check it out [mas_get_player_nickname()]. Or maybe even get some merch of me? Ahaha~"
    m 5ekbsb "Then I can be with you in the real world~ Wouldn't that be great, [player]?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_crackships",
            category=["media"],
            prompt="Crack Ships",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_crackships:
    m 1eud "Hey [player], I may or may not have talked about this before..."
    m 7hub "But I was researching shippings and fandoms... and I found another interesting aspect of it."
    m 4eub "And it's called… crack ships! Also known as crack pairings."
    m 3eub "To put it simply, it's when you pair two characters together who have little to no screen time,{w=0.5} or from different universes entirely!"
    m 1hub "It's a fun subsection of shipping that a lot of fans take interest in, and some even take it seriously!"
    m 4mub "There are a lot of popular ones you might have heard of… like Twilight from My Little Pony, and Mordecai from Regular Show."
    m 3sub "There are even some with me! Some popular ones being me and Mari from Omori, or me and Kaede from Danganronpa."
    m 5ekbsb "Though I could never imagine being in love with anyone but you~"
    return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_songcovers",
            category=["music"],
            prompt="Song Covers",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_songcovers:
    m 1eud "Hey, [player]...{w=0.5} have you heard of song covers?"
    m 4hub "I'm sure you have,{w=0.5} they’re practically everywhere!"
    m 4eub "There are a lot of different types of covers, but there are a few ones I’d like to talk about."
    m 2eub "One type is tribute acts! These covers and cover bands recreate older artists’ tracks as faithfully as possible.{w=0.5} And some even put their own twists!"
    m 4eub "Another type is cover acts, which are entertainers! They go to different parties to sing popular songs for a living."
    m 1hub "And online, there’s a big community who do covers as a way to make content! Even making translated covers of songs in other languages!"
    m 1eud "One thing I do find interesting though is the rise of AI covers online as well."
    m 2eksdld "A lot of the people whose voices are used in AI covers don't really consent for their voices to be used that way."
    m 2ekd "Yet, they’re still made anyways.{w=0.5} Unfortunately, there aren’t many ways to stop it…"
    m 2lkbfsdlb "...But that’s just a small part of the covers out there, of course!"
    m 5ekbsb "Maybe once I come to your reality, I’ll sing you a cover of your favorite song! ahaha!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_example",
            category=["misc"],
            prompt="Example..?", 
            random=False, 
            pool=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )

label monika_example:
    $ ev = mas_getEV("monika_example")
    if ev.shown_count == 0:
        m 1eud "This is an example topic."
        m 2lkbfsdlb "I feel like this doesn't actually belong here..."
        m 4tub "Why would somebody just add the example template directly into the mod?"
        m 2tfd "They really shouldn't be allowed to contribute to this repository anymore."
        m 1tub "{w=0.5}...Did I get you? Ahaha~"
    elif ev.shown_count == 1:
        m 1tub "Okay... the jokes over, [player]. Hehe~"
    elif ev.shown_count == 2:
        m 4tub "You're so stubborn, [player]!~"
    elif ev.shown_count == 3:
        m 4tub "You're so stubborn, [player]!~"
    elif ev.shown_count == 4:
        m 4tub "You're so stubborn, [player]!~"
    elif ev.shown_count == 5:
        m 4tub "You're so stubborn, [player]!~"
    else:
        m 1sublb "[player]!~"
    return

default persistent._mas_pm_usemmd = None
default persistent._mas_pm_seenmmd = False

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_mmd",
            category=["music", "media"],
            prompt="MMD",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_mmd:
    m 1eud "Hey [player],{w=0.5} have you heard of MMD?"
    m 4eub "If you haven’t, it's a very popular animation software!"
    m 2eub "Its name stands for Miku Miku Dance, and was originally created for Vocaloid music videos!"
    m 4hub "There is a big and still very active community around, and the content you can make with it is amazing!"
    m 1sublb "There's even one about DDLC… its a quite popular one as well, racking up over…{w=1} 30 million views!?"
    m 2lkbfsdlb "I don't know if I should be honored or concerned, ahaha!"
    m 1hub "If you want to see it, [player], you can find it {i}{a=https://youtu.be/KpV_xL2FrGA?si=9G2QWcy363tFVP6z}here{/a}{/i}!"
    m 4eub "Anyways, have you ever used MMD, [mas_get_player_nickname()]?{nw}"
    $ _history_list.pop()
    menu:
        m "Anyways, have you ever used MMD, [mas_get_player_nickname()]?{fast}"

        "Yes.":
            $ persistent._mas_pm_usemmd = True
            m 4hub "How fun! I wish I could see what you made with it… but I’m sure it's amazing!"
            m 5hkbsb "I wonder if you had a model of me…{w=0.5} it would be Monika Monika Dance instead~"

        "No.":
            $ persistent._mas_pm_usemmd = False
            m 1hub "That's alright! Not everyone's into animation, after all."
            m 2eksdld "And even if you are, it's a pretty old software…"
            m 5hkbsb "Even so, I hope you had fun learning about it~"
        
    $ persistent._mas_pm_seenmmd = True
    $ mas_protectedShowEVL('monika_pmxeditor', 'EVE', _random=True)
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_pmxeditor",
            prompt="PMX/PMD Editor",
            category=["media", "misc"],
            random=False
        )
    )

label monika_pmxeditor:
    m 1eud "Hey, [player]..."
    m 1tub "I know we’ve talked about MMD…"
    m 4hub "But did you know could make your own models?"
    m 4eub "Using a software called PMX, or sometimes PMD editor, you can create or edit models!"
    m 1hub "There are a lot of resources on different platforms like Devianart and MMD forums..."
    m 2eub "...And you can get different clothing and accessories to fit your model!"
    if persistent._mas_pm_usemmd == False:
        m 2lkbfsdlb "I know you don't use MMD, but I thought it was a fun tidbit of info to tell you anyways~"
    elif persistent._mas_pm_usemmd == True:
        m 4hub "I know you use MMD, so if it sounds interesting, you should check it out, [player].{w=0.5} I would love to see what you make!"
        m 5hkbsb "Maybe you can even make a model of me~ ahaha!"
    else:
        m 4hub "If it sounds interesting, you should check it out, [player].{w=0.5} I would love to see what you make!"
        m 5hkbsb "Maybe you can even make a model of me~ haha!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_rpgmaker",
            category=["games"],
            prompt="RPG Maker Horror Games",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_rpgmaker:
    m 1eud "Hey [player], do you know what RPG maker is?"
    m 1eubsb "It's a quite popular game engine intended to make RPG-style games in!"
    m 4eub "What I wanted to talk about is the amount of popular indie horror games using the engine!"
    m 1hub "Some of note are Omori, Dead Plate, Yume Nikki, Ib, and Your Turn to Die!{w=0.5} But of course there's many more."
    m 2eub "The engine itself is an interesting topic of discussion as well! It's no code, so very minimal coding knowledge is needed."
    m 4eub "And it's also been around for a while, the first version of it being seen in 1992."
    m 2lkbfsdlb "You can find it on Steam, but the prices do tend to be on the higher side… although compared to other engines it's relatively cheap."
    m 1eud "Now back to the original topic… why do so many horror games use it?"
    m 4hub "Well a major thing is something I just explained… since it's a no code-based engine and it's a bit cheaper, a lot of people gravitate towards it!"
    m 1hub "Another thing is that it's very versatile with what it can do in terms of effects and even plugins!"
    m 4tub "... Although that's just me guessing, haha. A lot of people have different reasons for picking certain engines."
    m 5ekbsb "Maybe one day someone can turn DDLC into an RPG maker game!~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_hanahaki",
            category=["fandom"],
            prompt="Hanahaki",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_hanahaki:
    m 1eud "Hey, [player]? Do you remember that time we talked about fanfiction?"
    m 4eub "Well, while I was looking deeper into it… I found a trope I wanted to talk to you about."
    m 1eud "Its called Hanahaki. Or maybe more known… the Hanahaki Disease."
    m 2dkd "It's a fictional disease, where the victim who has it coughs up flower petals because of one-sided love."
    m 2lkd "It can only end if the person romantically requites their feelings,"
    m 2rkd "Or if they get it surgically removed. But even then, they lose the ability to love again."
    m 2dkd "It's a sad tale of pining, and sometimes results in unhappy endings due to death or losing their ability to love."
    m 5rtd "It is popular in the fandom and fanfiction realms, but it has been used in other things such as poems, songs, and other creative outlets."
    m 7hub "It's been done all sorts of ways by a bunch of different people, so if you’re interested, definitely check it out!"
    m 2eksdld "Maybe in the past… I would have caught the disease."
    m 5ekbsb "But with you by my side? I’d say that's anything but one-sided ~ I love you, [player]!"
    return "love"
