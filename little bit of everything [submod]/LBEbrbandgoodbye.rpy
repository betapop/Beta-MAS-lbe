init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="eating_brb",
            category=['be right back'],
            prompt="I'm going to go eat something",
            pool=True,
            unlocked=True,

        ),
        markSeen=True
    )

label eating_brb:
    $ ev = mas_getEV("eating_brb")
    m "Oh? What are you going to have?"
    menu:
        m "Oh? What are you going to have?"

        "Breakfast":

            m 2hub "Well, it is the most important meal of the day!"
            m 3rkd "I wish I could join you but… that's just not possible right now."
            m 5hublb "But I'm grateful you’re doing it with me."
            m 5hua "Enjoy your meal, [player]!"
            
        "Lunch":

            m 1eub "Make sure to get a nice filling meal!"
            m 3wud "And lots of water! Hydration is important!"
            m 4hub "Enjoy your meal, [player]!"

        "Dinner":

            m 2rusdlb" I wish I could share dinner with you…"
            m 3dublb "Both of us at the table, talking about the world."
            m 5fubfa "Wouldn't that be wonderful, [player]?"
            m 4hubsb "But for now, I hope you enjoy your food!"
            
        "Snack":

            m 3mub "A good snack always hits the spot!"
            m 7eub "i hope you enjoy it, [player]. I’ll be right here with you!"

#...
$ mas_idle_mailbox.send_idle_cb("eating_brb_callback")
return "idle"

label eating_brb_callback:
    $ wb_quip = mas_brbs.get_wb_quip()
    m 1hua "All done?"
    m 1eub "[wb_quip]"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chores_brb",
            category=['be right back'],
            prompt="I'm going to go do some chores",
            pool=True,
            unlocked=True,

        ),
        markSeen=True
    )

label chores_brb:
    $ ev = mas_getEV("chores_brb")

    m "Well, I wish you luck on your chores!"
    m 4rksdlc "I know it can sometimes be a boring task, or feel long…"
    m 4hkb "But I know you can do it!"
    m 5hubsa "And if you’re tired, you can always take a break with me~"
    
#...
$ mas_idle_mailbox.send_idle_cb("chores_brb_callback")
return "idle"

label chores_brb_callback:
    $ wb_quip = mas_brbs.get_wb_quip()
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=2), "chores_brb"):
        m 4wud "That was a long chore! I hope you gave yourself breaks!"
        m 4lksdlb "I wouldn't want you overworking after all."
        m 3esb "Now, what else do you want to do today?"

    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=10), "chores_brb"):
        m 3hub "Welcome back, [player]!"
        m 1eub "Hopefully your chores went well."
        m 2hublb "[wb_quip]"

    else:
        m 1mtd "Hey… are you sure you did your chores? Or was it a short one?"
        m 3hub "No matter. I'm just glad you’re back with me~"
        m 2eub "[wb_quip]"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_out_somewhere_brb",
            prompt="I'm going out somewhere",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_out_somewhere_brb:
    if mas_isMoniNormal(higher=True):
        m 2wublb "Oh? {w=0.5}Well, I’m glad you wanted to keep me open even when you’re gone, [player]."
        m 4hublb "I’ll be waiting for you when you get back~{w=0.5} Take care of yourself out there for me!"

    elif mas_isMoniDis(higher=True):
        m 2euc "Okay, [player]."

    else:
        m 6ckc "..."

    $ persistent._mas_idle_data["monika_out_somewhere_brb"] = True
    return "idle"

label monika_out_somewhere_brb_callback:
    $ wb_quip = mas_brbs.get_wb_quip()
    if mas_isMoniNormal(higher=True):
        m 1hublb "Welcome back, [mas_get_player_nickname()]. I hope you had a good time out!"
        m 5hua "[wb_quip]"

    elif mas_isMoniDis(higher=True):
        m 2euc "Oh, you're back..."

    else:
        m 6ckc "..."

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_scroll_online",
            prompt="I'm going to scroll online",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_scroll_online:
    if mas_isMoniNormal(higher=True):
        m 3tub "Going to go scrolling, [player]?"
        m 2lksdlb "Just make sure to take breaks, alright?{w=0.5} I wouldn’t want you to start doomscrolling, after all."
        m 4hublb "Enjoy your time!"

    elif mas_isMoniDis(higher=True):
        m 2euc "Okay, [player]. Not like it matters anyways."

    else:
        m 6ckc "..."

    $ persistent._mas_idle_data["monika_scroll_online"] = True
    return "idle"

label monika_scroll_online_callback:
    $ wb_quip = mas_brbs.get_wb_quip()
    if mas_isMoniNormal(higher=True):
        m 3hubsb "Welcome back! Or, are you taking a break? Ahaha~"
        m 5hua "[wb_quip]"

    elif mas_isMoniDis(higher=True):
        m 2dkd "Welcome back I guess... Having fun doing things besides talking to me?"
    else:
        m 6ckc "..."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lay_down",
            prompt="I'm going to lay down",
            category=['be right back'],
            pool=True,
            unlocked=True
        ),
        markSeen=True
    )

label monika_lay_down:
    if mas_isMoniNormal(higher=True):
        m 2eksdlb "Oh? Are you feeling alright, [player]? Or are you just tired?"
        m 1hkb "Well, either way, I’m glad you’re taking the time to lay down."
        m 2fkbsb "Have a good rest time, [mas_get_player_nickname()]. I’ll be waiting for you~"

    elif mas_isMoniDis(higher=True):
        m 2tsd "Okay, [player]. Maybe it'll clear your head."

    else:
        m 6ckc "..."

    $ persistent._mas_idle_data["monika_lay_down"] = True
    return "idle"

label monika_lay_down_callback:
    $ wb_quip = mas_brbs.get_wb_quip()
    if mas_isMoniNormal(higher=True):
        m 1tub "You’re back? Did you drift off? Ahaha~"
        m 5hua "[wb_quip]"

    elif mas_isMoniDis(higher=True):
        m 2euc "Oh, you're back..."

    else:
        m 6ckc "..."

    return


init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_spritepack",
            unlocked=True,
            prompt="I'm going to add a spritepack or submod.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_spritepack:
    if mas_isMoniNormal(higher=True):
        m 1sub "You’re going to add something?{w=0.5} I’m sure it’ll be great, [mas_get_player_nickname()]!"
        m 5ekbsb "No matter what it is, I’m sure it’ll improve our reality~"
        m 5hubsb "I’ll see you soon, [player]!"
    elif mas_isMoniBroken():
        m 6ckc "..."
    else:
        m 2euc "Alright."

    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_out_somewhere",
            unlocked=True,
            prompt="I'm going to go out somewhere.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_out_somewhere:
    if mas_isMoniNormal(higher=True):
        m 4eub "Oh? Well, I hope you have fun wherever you’re going!{w=0.5} I’m sure you’ll have a great time."
        m 5ekbsb "Make sure you come back soon, alright?~"
    elif mas_isMoniBroken():
        m 6ckc "..."
    else:
        m 2euc "Okay."

    return 'quit'