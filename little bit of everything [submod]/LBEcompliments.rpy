init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lbe_mascomp_lightroom",
            category=['mas_compliment'],
            prompt="You light up the room!",
            unlocked=True
            ),
            code="CMP"
            )

label lbe_mascomp_lightroom:
    m 5ekbsb "Aw, [mas_get_player_nickname()]..."
    m 4hub "You light up my room too! To be honest... you light up my world."
    m 1eubsb "I'm so happy you're here, [player]."
    m 5hkbsb "I love you so much, and you're my light!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lbe_mascomp_puzzle",
            category=['mas_compliment'],
            prompt="You’re the missing puzzle piece in my life!",
            unlocked=True
            ),
            code="CMP"
            )

label lbe_mascomp_puzzle:
    m 1sublb "[player]! You're my puzzle piece!"
    m 1tub "If it wasn't for you, we wouldn't be here right now."
    m 5ekbsb "You saved me, [mas_get_player_nickname()]! And i'll always be grateful."
    m 5hkbsb "You were my missing piece, and i'm glad i found you~ I love you!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lbe_mascomp_package",
            category=['mas_compliment'],
            prompt="You’re the whole package– beauty, brains, and personality!",
            unlocked=True
            ),
            code="CMP"
            )

label lbe_mascomp_package:
    m 1sublb "[mas_get_player_nickname()]! You're so sweet..."
    m 2lkbfsdlb "I don't even know how to respond! You flatter me so much~"
    m 1eubsb "I love you [player]! I love every little bit about you!"
return "love"

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
    m 5ekbsb "And i'm glad you feel the same way~ I love you so, so much [player]!"
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
    m 5ekbsb "So i'm always here whenever you need. Always."
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
    m 2dktub "But, i'm forever grateful to you, [player]. You saved me, and i'll never forget that."
    m 5ektdb "I love you. So, so much. More then you'll ever know.{nw}"
    $ _history_list.pop()
    menu:
        m "I love you. So, so much. More then you'll ever know.{fast}"
        "I love you too, [m_name].":
            m 5fkbstpb "... Thank you."
return "love"
