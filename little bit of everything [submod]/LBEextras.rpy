#ask moni about what food to eat
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lbe_foodideas",
            category=["food", "misc"],
            prompt="Monika, what should I eat?",
            pool=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

define mfoodideassnack = ["chips", "hummus", "yogurt", "some fruit", "mixed nuts", "cheese and crackers", "cookies", "chips and dip", "a smoothie", "popcorn", "a granola bar", "fries", "deviled eggs", "some candy", "ice cream", "a salad", "cake"]
define mfoodideasmeal = ["a burrito", "a soup", "a taco", "a peanut butter and jelly sandwich", "a lunch meat sandwich", "a grilled cheese sandwich", "a egg salad sandwhich", "a hamburger", "a chicken sandwhich", "chicken wings", "a wrap", "some ramen", "some udon", "some noodles", "some pasta", "sushi", "pizza", "curry", "a poke bowl", "a quiche", "chili", "a casserole", "a seafood dish", "a tofu dish", "chicken parm", "fish and chips", "lasagna"]
define mfoodideasmorning = ["cereal", "french toast", "a croissant", "a donut", "eggs and toast", "avacado toast", "a breakfast sandwhich", "pancakes", "waffles", "american breakfast", "cinnamon rolls", "hashbrowns", "bagels with cream cheese", "biscuit and gravy", "a breakfast burrito", "a omelette", "omurice", "a spinach quiche", "british breakfast"]


label monika_lbe_foodideas:
    $ ev = mas_getEV("monika_lbe_foodideas")

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

#high or low game [it kinda works]

define numb1 =  ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
define numb2 = ["2", "3", "4", "5", "6", "7", "8", "9"]
default score = 0

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lbe_high_or_low",
            category=["minigames"],
            prompt="Do you want to play high or low?",
            random=False,
            pool=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_lbe_high_or_low:
    m 1eubsb "Sure! Let me get prepared.{w=0.1}.{w=0.1}.{w=0.1}"
    m 4eub "Alright! There we go."
    jump monika_lbe_holgame
    return

label monika_lbe_holgame:
    $ num = renpy.random.choice(numb1)
    m 1tub "The card is... [num]!"
    m 4hub "Will the next one be higher or lower?{nw}"
    $ num2 = renpy.random.choice(numb2)
    $ _history_list.pop()
    menu:
        m "Will the next one be higher or lower?{fast}"
        "It's higher!":
            if num2 >= 5:
                m 4eub "Correct! The number was higher!"
                $ score += 1
            else:
                m 2lkbfsdlb "Incorrect! The number was lower."
            jump monika_lbe_holgameend

        "It's lower!":
            if num2 < 5:
                m 4eub "Correct! The number was lower!"
                $ score += 1
            else:
                m 2lkbfsdlb "Incorrect! The number was higher."
            jump monika_lbe_holgameend


label monika_lbe_holgameend:
    m 1eubsb "You have [score] correct so far!"
    m 1eud "Do you want to keep on playing?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to keep on playing?{fast}"
        "Yes.":
            m 4eub "Alright then!"
            jump monika_lbe_holgame
        "No.":
            m 4hub "Okay. Thanks for playing with me!"
            return

#finish the lyric game
# i am not getting it to work for the life of me so im commenting it out for now

# define lyricspop = ["Hey I just met you, and this is crazy...", "Because i'm happy..."]

# init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="monika_lbe_finish_the_lyric",
#            category=["minigames"],
#            prompt="Do you want to play finish the lyrics?",
#            random=False,
#            pool=True,
#            aff_range=(mas_aff.NORMAL, None)
#        )
#    )



# label monika_lbe_finish_the_lyric:
#    m "Of course! Let me look at the songs I have here.{w=0.1}.{w=0.1}.{w=0.1}"
#    m "Alright! What type of music do you want to do?{nw}"
#    menu:
#        m "Alright! What type of music do you want to do?{fast}"
#        "Pop.":
#            jump monika_lbe_finish_the_lyric_pop
#        "Rap/Hip Hop.":
#            m "Sorry, I cant think of any songs..."
#            return
#        "Indie.":
#            m "Sorry, I cant think of any songs..."
#            return
#        "Jazz/Blues.":
#            m "Sorry, I cant think of any songs..."
#            return

# label monika_lbe_finish_the_lyric_pop:
#    $ lyricpop = renpy.random.choice(lyricspop)
#    m "Okay! Let me think of a song.{w=0.1}.{w=0.1}.{w=0.1}"
#    m "Here's your lyric: [lyricpop]"

#    $ lyric = renpy.input("What is the rest of the line/lyric?", length=1000)
#    $ inputlyric = lyric.strip()

#    if lyricpop == "Hey I just met you, and this is crazy...":
#        if inputlyric == "But heres my number" or inputlyric "But here's my number" or inputlyric "But heres my number, so call me, maybe":
#            m "You got it right! The song was Call Me Maybe by  Carly Rae Jepsen!"
#            jump monika_lbe_finish_the_lyric_end
#        elif inputlyric == "":
#            m "Hey, you didnt type anything! Try again~"
#            jump monika_lbe_finish_the_lyric_pop
#        else:
#            m "Thats incorrect! The song was Call Me Maybe by  Carly Rae Jepsen!"
#            jump monika_lbe_finish_the_lyric_end
#    else:
#        m "For some reason, the game isn't working... Im sorry, [player]!"

#    if lyricpop == "Because i'm happy...":
#        if inputlyric == "Clap along if you feel" or inputlyric "clap along if you feel" or inputlyric "Clap along if you feel like a room without a roof" or inputlyric "clap along if you feel like a room without a roof":
#            m "You got it right! The song was Happy by Pharrell Williams!"
#            jump monika_lbe_finish_the_lyric_end
#        elif inputlyric == "":
#            m "Hey, you didnt type anything! Try again~"
#            jump monika_lbe_finish_the_lyric_pop
#        else:
#            m "Thats incorrect! The song was Happy by Pharrell Williams!"
#            jump monika_lbe_finish_the_lyric_end
#    else:
#        m "For some reason, the game isn't working... Im sorry, [player]!"

# label monika_lbe_finish_the_lyric_end:
#    m "Do you want to keep on playing?{nw}"
#    $ _history_list.pop()
#    menu:
#        m "Do you want to keep on playing?{fast}"
#        "Yes.":
#            jump monika_lbe_finish_the_lyric
#        "No.":
#            m "Okay. Thanks for playing with me!"
#            return

# touch moni!

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lbe_canitouch",
            category=["monika", "misc"],
            prompt="Can I touch you?",
            pool=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )

label monika_lbe_canitouch:
    m 1eubsb "Sure, [player]!"
    m 4tub "Just don't be naughty, okay?~"
    jump touch_screen_lbe
    return

define mheadpat = ["Aww.. thanks~", "Your touch is so nice~", "Head pats, huh?~", "Mmmm...", "Your touch is so comforting, haha~", "That feels good~"]
define mlcheek = ["Touching my cheeks, hm?~", "My left cheek~", "Don't poke me~ haha!"]
define mrcheek = ["Touching my cheeks, hm?~", "My right cheek~", "Don't poke me~ haha!"]

label touch_screen_lbe:
    show monika staticpose at t11
# cursor buttons
    screen cursor_touch:
        imagebutton:
            xpos 520
            ypos 10
            idle "submods/little bit of everything [submod]/lbe_assets/blank.png"
            hover "submods/little bit of everything [submod]/lbe_assets/hand_pat.png"
            action Jump("touch_pat")
        imagebutton:
            xpos 485
            ypos 300
            idle "submods/little bit of everything [submod]/lbe_assets/blank.png"
            hover "submods/little bit of everything [submod]/lbe_assets/left_cheek.png"
            action Jump("touch_left_cheek")
        imagebutton:
            xpos 685
            ypos 300
            idle "submods/little bit of everything [submod]/lbe_assets/blank.png"
            hover "submods/little bit of everything [submod]/lbe_assets/right_cheek.png"
            action Jump("touch_right_cheek")
    call screen cursor_touch

image pathand = "submods/little bit of everything [submod]/lbe_assets/hand_pat.png"
image cursorpinch1 = ("submods/little bit of everything [submod]/lbe_assets/left_cheek.png")
image cursorpinch2 = ("submods/little bit of everything [submod]/lbe_assets/right_cheek.png")

transform pinch_left:
    xpos 495
    ypos 300

transform pinch_right:
    xpos 675
    ypos 300

label touch_pat:
    show pathand at top onlayer overlay
    with Dissolve(1.0)
    $ touchpatrandom = renpy.random.choice(mheadpat)
    m 5ekbsb "[touchpatrandom]"
    hide pathand
    return

label touch_left_cheek:
    $ lcrandom = renpy.random.choice(mlcheek)
    show cursorpinch1 at pinch_left onlayer overlay
    with Dissolve(1.0)
    m 5ekbsb "[lcrandom]"
    hide cursorpinch1
    return

label touch_right_cheek:
    $ rcrandom = renpy.random.choice(mrcheek)
    show cursorpinch2 at pinch_right onlayer overlay
    with Dissolve(1.0)
    mm 5ekbsb "[rcrandom]"
    hide cursorpinch2
    return

# make it so this unlocks by dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lbe_racinggame",
            category=["minigames"],
            prompt="Can we play a racing game, [m_name]?",
            pool=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )

label monika_lbe_racinggame:
    m 1eubsb "Sure, [player]! Get ready to race~"
    jump race_game
    return

# submod header

init -990 python in mas_submod_utils:
    Submod(
        author="Betapop",
        name="Little Bit of Everything",
        description="a submod that adds new topics, spritepacks, interactions and more! Find the Github {a=https://github.com/betapop/Beta-MAS-lbe}{i}{u}here!{/u}{/i}{/a}",
        version="1.0.0",
    )

