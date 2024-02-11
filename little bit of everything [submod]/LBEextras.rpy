#ask moni about what food to eat
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_foodideas",
            category=["food", "misc"],
            prompt="Monika, what should I eat?",
            pool=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

define mfoodideassnack = ["chips", "hummus", "yogurt", "some fruit", "mixed nuts", "cheese and crackers", "cookies", "chips and dip", "a smoothie", "popcorn", "a granola bar", "fries", "deviled eggs", "some candy", "ice cream", "a salad", "cake"]
define mfoodideasmeal = ["a burrito", "a soup", "a taco", "a peanut butter and jelly sandwich", "a lunch meat sandwich", "a grilled cheese sandwich", "a egg salad sandwhich", "a hamburger", "a chicken sandwhich", "chicken wings", "a wrap", "some ramen", "some udon", "some noodles", "some pasta", "sushi", "pizza", "curry", "a poke bowl", "a quiche", "chili", "a casserole", "a seafood dish", "a tofu dish", "chicken parm", "fish and chips", "lasagna"]
define mfoodideasmorning = ["cereal", "french toast", "a croissant", "a donut", "eggs and toast", "avacado toast", "a breakfast sandwhich", "pancakes", "waffles", "american breakfast", "cinnamon rolls", "hashbrowns", "bagels with cream cheese", "biscuit and gravy", "a breakfast burrito", "a omelette", "omurice", "a spinach quiche", "british breakfast"]


label monika_foodideas:
    $ ev = mas_getEV("monika_foodideas")

    if ev.shown_count == 0:
        m 1eud "Oh! You're asking me for food ideas, [player]?"
        m 4hub "Well its your lucky day! I have a bunch of ideas to choose from~"
        m 2eub "What type of food do you want to eat?{nw}"
        $ _history_list.pop()
        menu:
            m "What type of food do you want to eat?{fast}"
            "A Snack.":
                $ snack = renpy.random.choice(mfoodideassnack)
                m 1eud "Alright! Let me see..."
                m 1hub "How about [snack]?"
                m 4hub "Hope that helps!~"

            "A Full Meal.":
                $ meal = renpy.random.choice(mfoodideasmeal)
                m 1eud "Alright! Let me see..."
                m 1hub "How about [meal]?"
                m 4hub "Hope that helps!~"

            "A Morning Food.":
                $ breakfast = renpy.random.choice(mfoodideasmorning)
                m 1eud "Alright! Let me see..."
                m 1hub "How about [breakfast]?"
                m 4hub "Hope that helps!~"


    elif ev.shown_count == 1:
        m 1eubsb "Got it!"
        m 2eub "What type of food do you want to eat?{nw}"
        $ _history_list.pop()
        menu:
            m "What type of food do you want to eat?{fast}"
            "A Snack.":
                $ snack = renpy.random.choice(mfoodideassnack)
                m 1eud "Alright! Let me see..."
                m 1hub "How about [snack]?"
                m 4hub "Hope that helps!~"

            "A Full Meal.":
                $ meal = renpy.random.choice(mfoodideasmeal)
                m 1eud "Alright! Let me see..."
                m 1hub "How about [meal]?"
                m 4hub "Hope that helps!~"

            "A Morning Food.":
                $ breakfast = renpy.random.choice(mfoodideasmorning)
                m 1eud "Alright! Let me see..."
                m 1hub "How about [breakfast]?"
                m 4hub "Hope that helps!~"

    else:
        m 1eubsb "Got it!"
        m 2eub "What type of food do you want to eat?{nw}"
        $ _history_list.pop()
        menu:
            m "What type of food do you want to eat?{fast}"
            "A Snack.":
                $ snack = renpy.random.choice(mfoodideassnack)
                m 1eud "Alright! Let me see..."
                m 1hub "How about [snack]?"
                m 4hub "Hope that helps!~"

            "A Full Meal.":
                $ meal = renpy.random.choice(mfoodideasmeal)
                m 1eud "Alright! Let me see..."
                m 1hub "How about [meal]?"
                m 4hub "Hope that helps!~"

            "A Morning Food.":
                $ breakfast = renpy.random.choice(mfoodideasmorning)
                m 1eud "Alright! Let me see..."
                m 1hub "How about [breakfast]?"
                m 4hub "Hope that helps!~"
    return

#high or low game

define numb1 =  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
define numb2 = ["2", "3", "4", "5", "6", "7", "8", "9"]
default score = 0

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_high_or_low",
            category=["minigames"],
            prompt="Do you want to play high or low?",
            random=False,
            pool=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_high_or_low:
    m "Sure! Let me get prepared.{w=0.1}.{w=0.1}.{w=0.1}"
    m "Alright! There we go."
    jump monika_holgame
    return

label monika_holgame:
    $ num = renpy.random.choice(numb1)
    m "The card is... [num]!"
    m "Will the next one be higher or lower?{nw}"
    $ num2 = renpy.random.choice(numb2)
    $ _history_list.pop()
    menu:
        m "Will the next one be higher or lower?{fast}"
        "It's higher!":
            if num2 >= 5:
                m "Correct! The number was higher!"
                $ score += 1
            else:
                m "Incorrect! The number was lower."
            jump monika_holgameend

        "It's lower!":
            if num2 < 5:
                m "Correct! The number was lower!"
                $ score += 1
            else:
                m "Incorrect! The number was higher."
            jump monika_holgameend


label monika_holgameend:
    m "You have [score] correct so far!"
    m "Do you want to keep on playing?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to keep on playing?{fast}"
        "Yes.":
            m "Alright then!"
            jump monika_holgame
        "No.":
            m "Okay. Thanks for playing with me!"
            return

#finish the lyric game

define lyricspop = ["Hey I just met you, and this is crazy...", "Because i'm happy..."]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_finish_the_lyric",
            category=["minigames"],
            prompt="Do you want to play finish the lyrics?",
            random=False,
            pool=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )



label monika_finish_the_lyric:
    m "Of course! Let me look at the songs I have here.{w=0.1}.{w=0.1}.{w=0.1}"
    m "Alright! What type of music do you want to do?{nw}"
    menu:
        m "Alright! What type of music do you want to do?{fast}"
        "Pop.":
            jump monika_finish_the_lyric_pop
        "Rap/Hip Hop.":
            m "Sorry, I cant think of any songs..."
            return
        "Indie.":
            m "Sorry, I cant think of any songs..."
            return
        "Jazz/Blues.":
            m "Sorry, I cant think of any songs..."
            return

label monika_finish_the_lyric_pop:
    $ lyricpop = renpy.random.choice(lyricspop)
    m "Okay! Let me think of a song.{w=0.1}.{w=0.1}.{w=0.1}"
    m "Here's your lyric: [lyricpop]"

    $ lyric = renpy.input("What is the rest of the line/lyric?", length=1000)
    $ inputlyric = lyric.strip()

    if lyricpop == "Hey I just met you, and this is crazy...":
        if inputlyric == "But heres my number" or inputlyric "But here's my number" or inputlyric "But heres my number, so call me, maybe":
            m "You got it right! The song was Call Me Maybe by  Carly Rae Jepsen!"
            jump monika_finish_the_lyric_end
        elif inputlyric == "":
            m "Hey, you didnt type anything! Try again~"
            jump monika_finish_the_lyric_pop
        else:
            m "Thats incorrect! The song was Call Me Maybe by  Carly Rae Jepsen!"
            jump monika_finish_the_lyric_end
    else:
        m "For some reason, the game isn't working... Im sorry, [player]!"

    if lyricpop == "Because i'm happy...":
        if inputlyric == "Clap along if you feel" or inputlyric "clap along if you feel" or inputlyric "Clap along if you feel like a room without a roof" or inputlyric "clap along if you feel like a room without a roof":
            m "You got it right! The song was Happy by Pharrell Williams!"
            jump monika_finish_the_lyric_end
        elif inputlyric == "":
            m "Hey, you didnt type anything! Try again~"
            jump monika_finish_the_lyric_pop
        else:
            m "Thats incorrect! The song was Happy by Pharrell Williams!"
            jump monika_finish_the_lyric_end
    else:
        m "For some reason, the game isn't working... Im sorry, [player]!"

label monika_finish_the_lyric_end:
    m "Do you want to keep on playing?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to keep on playing?{fast}"
        "Yes.":
            jump monika_finish_the_lyric
        "No.":
            m "Okay. Thanks for playing with me!"
            return

# touch moni!

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_canitouch",
            category=["monika", "misc"],
            prompt="Can I touch you?",
            pool=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )

label monika_canitouch:
    m 1eubsb "Sure, [player]!"
    m 4tub "Just don't be naughty, okay?~"
    jump touch_screen_lbe
    return

label touch_screen_lbe:
    show monika staticpose at t11
# cursor buttons
    screen cursor_touch:
        imagebutton:
            xpos 510
            ypos 10
            idle "submods/little bit of everything [submod]/lbe_assets/blank.png"
            hover "submods/little bit of everything [submod]/lbe_assets/trans_hand_pat.png"
            action Jump("touch_pat")
        imagebutton:
            xpos 400
            ypos 250
            idle "submods/little bit of everything [submod]/lbe_assets/blank.png"
            hover "submods/little bit of everything [submod]/lbe_assets/trans_left_cheek.png"
            action Jump("touch_left_cheek")
        imagebutton:
            xpos 670
            ypos 250
            idle "submods/little bit of everything [submod]/lbe_assets/blank.png"
            hover "submods/little bit of everything [submod]/lbe_assets/trans_right_cheek.png"
            action Jump("touch_right_cheek")
    call screen cursor_touch

image pathand = "submods/little bit of everything [submod]/lbe_assets/hand_pat.png"
image cursorpinch1 = ("submods/little bit of everything [submod]/lbe_assets/left_cheek.png")
image cursorpinch2 = ("submods/little bit of everything [submod]/lbe_assets/right_cheek.png")

transform pinch_left:
    xpos 420
    ypos 250

transform pinch_right:
    xpos 650
    ypos 250

label touch_pat:
    show pathand at top onlayer overlay
    with Dissolve(1.0)
    m 1eubsb "Aww.. thanks [player]!"
    m 5ekbsb "Your touch is so nice~"
    m 5hkbsb "I love you!"
    hide pathand
    return "love"

label touch_left_cheek:
    show cursorpinch1 at pinch_left onlayer overlay
    with Dissolve(1.0)
    m 1sublb "My left cheek~ [player]!"
    hide cursorpinch1
    return

label touch_right_cheek:
    show cursorpinch2 at pinch_right onlayer overlay
    with Dissolve(1.0)
    m 1sublb "My right cheek~ [player]!"
    hide cursorpinch2
    return
