init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lbe_ddlcmerch",
            category=["ddlc"],
            prompt="DDLC Merch",
            random=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )

label monika_lbe_ddlcmerch:
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
            eventlabel="monika_lbe_crackships",
            category=["media"],
            prompt="Crack Ships",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_lbe_crackships:
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
            eventlabel="monika_lbe_songcovers",
            category=["music"],
            prompt="Song Covers",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_lbe_songcovers:
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
            eventlabel="monika_lbe_example",
            category=["misc"],
            prompt="Example..?", 
            random=False, 
            pool=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )

label monika_lbe_example:
    $ ev = mas_getEV("monika_lbe_example")
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
            eventlabel="monika_lbe_mmd",
            category=["music", "media"],
            prompt="MMD",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_lbe_mmd:
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
    $ mas_protectedShowEVL('monika_lbe_pmxeditor', 'EVE', _random=True)
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lbe_pmxeditor",
            prompt="PMX/PMD Editor",
            category=["media", "misc"],
            random=False
        )
    )

label monika_lbe_pmxeditor:
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
            eventlabel="monika_lbe_rpgmaker",
            category=["games"],
            prompt="RPG Maker Horror Games",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_lbe_rpgmaker:
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
            eventlabel="monika_lbe_hanahaki",
            category=["fandom"],
            prompt="Hanahaki",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_lbe_hanahaki:
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


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lbe_swimwear",
            category=["life"],
            prompt="History of Swimwear",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_lbe_swimwear:
    m 1eud "You know what’s interesting, [player]?"
    m 1rub "Swimwear. The idea and execution of it, in general."
    m 3hub "Did you know, up until the 18th century, it was normal and practice to swim nude?"
    m 3dub "Most of the bathing and swimming was done in a private setting, so there was no need to cover up."
    m 4eud "When more modest traditions started to roll in, they started making ladies wear long, oversized dresses to cover curves and privates."
    m 2rub "The men were still allowed to swim nude, but the popularity of swimsuits started to become more common."
    m 3dsb "There were a lot of different iterations of the swimwear, including bloomer swimsuits— Which were quite controversial for being too close to men's pants."
    m 1msb "Eventually, a swimmer named Annette Kellerman made a swimsuit that was closer to a traditional man's swimsuit, and what would eventually start the one-piece craze."
    m 1hub "And as it moved into the 30s and 40s, it started to look more like what a normal one-piece would look like in our times."
    m 1tfb "And suddenly... a man named Louis Réard would go on to make the first bikini, and it was seen as very shocking at first."
    m 3rsb "It was something different, and something more revealing. But it also had good functionality for swimming as well."
    m 2lub "So eventually, the world picked up on it. And since then, we never really looked back. More different and modern designs kept coming out, and people kept buying them."
    m 1dub "It's a cool section of fashion that I don't think many people know the story behind, although it's a pretty simple one."
    m 3hub "And if you didn't know, you do now! ehehe~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lbe_lawgames",
            category=["fandom"],
            prompt="Law Based Games",
            random=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )

label monika_lbe_lawgames:
    m 1eud "Hey, [player]? You know what I find interesting?"
    m 3rud "All of the games that are surprisingly, based on real law and court."
    m 4hub "There are a few ones I want to talk about."
    m 3dub "Those being Your Turn to Die, Ace Attorney, and Danganronpa."
    m 1rkb "Both Your Turn to Die and Danganronpa are based around the idea of a killing game."
    m 1msb "And both have trial segments, where you try to find out who the real killer is and vote them out."
    m 2rksdld "I guess, in a weird, twisted way, I kind of understand them."
    m 2dssdld "If you have to kill a person by voting, or kill a person to have a chance at escaping…"
    m 3mtd "… You’re just doing it for your own survival, right?"
    m 5dtd "And it’s kind of similar to me as well. Although I didn’t exactly ‘kill’ the girls… {w=0.5}I had to get rid of them to achieve my happy ending."
    m 2rfd "It’s… unfair, sometimes. What you have to do to survive."
    m 2hksdlb "…But, anyways! The other game is a bit happier."
    m 3esb "Ace Attorney revolves around a defense attorney named Phoenix Wright, who goes around defending people getting falsely accused."
    m 4tub "It’s a very interesting franchise, as you get to collect your own evidence and present it in court."
    m 5hub "Including all of the magical tropes and aspects of it! I would recommend you check it out if it sounds fun, [player]."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lbe_inflation",
            category=["Life"],
            prompt="Inflation",
            random=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )

label monika_lbe_inflation:
    m 1eud "Hmm… hey, [player]?"
    m 2rksdlb "Right now i’m looking at what seems to be the world’s inflation rates."
    m 2eksdlb "And… it doesn’t look like it’s doing too well."
    m 3dkd "In some countries it spiked bad.. like the United States or Argentina."
    m 4mkd "It seems like the global pandemic really disrupted the system."
    m 2ekd "And the worse thing is these things are still increasing right now."
    m 3dsd "Here’s a good comparison: In the US, potato chips used to be around 3-4$ dollars in 2015..."
    m 3tfp "And now they’re upwards of 7$. Just for one bag!"
    m 5rkd "Hopefully when I get to your world, we won’t have these problems."
    m 5ekd "And I just want you to know, [mas_get_player_nickname()]…"
    m 5dkd "If you’re facing hard times right now, money or otherwise…"
    m 5fkbsb "I love you so much, and i’m supporting you every step of the way."
    m 1ekbsb "If you need a friend, a girlfriend, or just any support in general… i’m here."
    m 1dkbld "I never want to see you suffering. Especially with that the world’s putting you up with."
    m 3fkbsb "Again, I love you! And i’ll always be here~ ehehe."
    return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lbe_content_farms",
            category=["misc"],
            prompt="Content Farms",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_lbe_content_farms:
    m 1eud "Have you ever heard of content farms, player?{nw}"
    $ _history_list.pop()
    menu:
        m "Have you ever heard of content farms, player?{fast}"
        "Yes.":
            m 3hub "Saves me the explanation then!"
        "No.":
            m 3hub "Don’t worry! I’ll explain it to you."
            m 4rud "It’s a term usually for a company that produces a lot of low quality media to get boosted by the algorithm."
            m 3rud "It started on article websites, who would pump out different stories not written by ‘specialists’. Which inherently makes them less quality."
            m 1lksdlb "But that’s a discussion for a different time."

    m 7eud "What I wanted to talk about are the content farms on Youtube."
    m 7tub "I’m sure you’ve encountered at least a few of them, even if you didn’t know."
    m 2eud "Like for example, the channels 5-Minute Crafts or Troom Troom."
    m 2rksdlb "And if you’ve been on the internet lately… you might have heard about The Amazing Digital Circus and Hazbin Hotel."
    m 2rksdlb "Right now, the animated content farms, that seem to be targeted more towards children, are booming with these these inappropriate videos of these fandom characters."
    m 1rsc "To the point where it’s becoming a real problem. If you searched either of those topics on Youtube, you’re sure to find a few content farmed videos."
    m 1rtd "If you know about it, it’s very similar to the Elsagate controversy back in 2017."
    m 1ltd "What Youtube is going to do about it? No one really knows yet, since no action has been made."
    m 1dsd "Hopefully they’ll fix it soon though…"
    m 1hub "I’m sure it’ll work itself out, [player]. And when it does, come celebrate with me!~"
    return
