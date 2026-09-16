init python:

    lbe_accessories = [
        ("lbe_acs_computer_open", "computer_open", MASPoseMap(default="0", use_reg_for_l=True), True),
        ("lbe_acs_computer_closed", "computer_closed", MASPoseMap(default="0", use_reg_for_l=True), True),
    ]

    for info in lbe_accessories:
        name = info[0]
        acs = MASAccessory(*info)
        vars()[name] = acs
        store.mas_sprites.init_acs(acs)

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lbe_old_computer",
            category=["Misc"],
            prompt="Old Computer",
            random=True,
            rules={mas_bookmarks_derand.BLACKLIST},
            aff_range=(mas_aff.HAPPY, None)
        )
    )

default persistent._mas_computer_seen = False

label lbe_old_computer:
    call mas_transition_to_emptydesk
    m "Hmm…."
    m "Hmmmm…."
    python:
        monika_chr.wear_acs(lbe_acs_computer_open)
    with Dissolve(1.0)
    call mas_transition_from_emptydesk("monika 1eua")
    m 3wub "Oh, [player]!"
    m 2eub "I was trying to find something very special."
    m 4hub "And… {w=0.5} Here it is!"
    m 1eub "Surprisingly, it’s still in pretty good shape."
    m 3tub "You know what this means, [player]? I can finally stop using your computer~"
    m 2rkb "Well, not completely, but you know what I mean."
    m 3dub "I wonder how much I can do on this? Hm…"
    m 2eub "Alright, give me a second to put this away."
    call mas_transition_to_emptydesk
    python:
        monika_chr.remove_acs(lbe_acs_computer_open)
    with Dissolve(1.0)
    pause 3
    call mas_transition_from_emptydesk("monika 1eua")

    $ persistent._mas_computer_seen = True
    return "derandom"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_work_with_me",
            prompt="Do you want to work on something with me, [m_name]?",
            category=['be right back'],
            pool=False,
            random=False,
            conditional="renpy.seen_label('lbe_old_computer')",
            action=EV_ACT_POOL
        ),
        markSeen=True
    )

label monika_work_with_me:
    $ ev = mas_getEV("monika_work_with_me")
    if ev.shown_count == 0:
        jump monika_work_with_me_first_1
    else:
        $ persistent._mas_idle_data["monika_work_with_me"] = True
        jump monika_work_with_me_2
    return


label monika_work_with_me_first_1:
    m 1wub "Oh? You want to work on something together, [player]?"
    m 3hub "What a nice idea. It’ll be good for both of us too, and we can still spend time together!"
    jump work_get_computer_first

label monika_work_with_me_2:
    m 1hub "Time to work again, [player]?"
    jump work_get_computer

label work_get_computer_first:
    m 3dub "Let me get my computer out..."
    call mas_transition_to_emptydesk
    pause 3
    python:
        monika_chr.wear_acs(lbe_acs_computer_open)
    with Dissolve(1.0)
    call mas_transition_from_emptydesk("monika 1eua")
    m 2hub "There we go."
    jump work_gotcomp_brb


label work_get_computer:
    m 2rtt "Alright, now wheres my computer..."
    call mas_transition_to_emptydesk
    pause 3
    python:
        monika_chr.wear_acs(lbe_acs_computer_open)
    with Dissolve(1.0)
    call mas_transition_from_emptydesk("monika 1eua")
    m 3hub "Got it!"
    jump work_gotcomp_brb

label work_gotcomp_brb:
    m 2tub "Now, let's get to work, shall we?"
    
    $ persistent._mas_idle_data["monika_work_with_me"] = True
    return "idle"

label monika_work_with_me_callback:
    m 1hub "It was fun working with you, [player]."
    m 3eub "Let me just fix up all this..."
    call mas_transition_to_emptydesk
    with Dissolve(1.0)
    python:
        monika_chr.remove_acs(lbe_acs_computer_open)
    pause 3
    call mas_transition_from_emptydesk("monika 1eua")
    m 1hub "Alright! Let's continue on with our day!"
    return
