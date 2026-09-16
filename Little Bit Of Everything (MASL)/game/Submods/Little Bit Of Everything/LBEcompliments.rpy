
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lbe_mascomp_believelove",
            category=['mas_compliment'],
            prompt="You’re the reason why I believe in love.",
            unlocked=True
            ),
            code="CMP"
            )

label lbe_mascomp_believelove:
    m 5ekbsb "Aw~ you're my reason I believe in love too."
    m 5hkbsb "I know from the moment I met you that this was true love. That this was meant to be."
    m 5ekbsb "And I'm glad you feel the same way~ I love you so, so much [player]!"
return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lbe_mascomp_haven",
            category=['mas_compliment'],
            prompt="You are my safe haven in this crazy world.",
            unlocked=True
            ),
            code="CMP"
            )

label lbe_mascomp_haven:
    m 1hub "I'm glad I can be a safe place from your reality, [player]."
    m 2eksdld "I know the outside world can be hectic..."
    m 5ekbsb "So I'm always here whenever you need. Always."
    m 5hkbsb "I love you~"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lbe_mascomp_11scale",
            category=['mas_compliment'],
            prompt="On a scale from 1 to 10, you’re an 11.",
            unlocked=True
            ),
            code="CMP"
            )

label lbe_mascomp_11scale:
    m 1sublb "[player]~ Well how about this..."
    m 4hub "{i}You{/i} broke my scale because you're so beautiful!"
    m 1eubsb "I love you, [mas_get_player_nickname()]!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lbe_mascomp_gladmet",
            category=['mas_compliment'],
            prompt="I'm so glad we met.",
            unlocked=True
            ),
            code="CMP"
            )

label lbe_mascomp_gladmet:
    m 5fkb "The sentiment is the same, [player]. I'm very glad we met."
    m 4rkd "After all, if we didn't..."
    m 2dktpc "..."
    m 2hktub "..Sorry. The feels got to me, ahaha!"
    m 2dktub "But, I'm forever grateful to you, [player]. You saved me, and I'll never forget that."
    m 5ektdb "I love you. So, so much. More then you'll ever know.{nw}"
    $ _history_list.pop()
    menu:
        m "I love you. So, so much. More then you'll ever know.{fast}"
        "I love you too, [m_name].":
            m 5fkbstpb "... Thank you."
return "love"
