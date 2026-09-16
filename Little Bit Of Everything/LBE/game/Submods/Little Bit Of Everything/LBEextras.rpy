#ask moni about what food to eat

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lbe_foodideas",
            category=["food", "misc"],
            prompt="[m_name], what should I eat?",
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
        jump food_randomizer

    elif ev.shown_count == 1:
        m 1eubsb "Got it!"
        jump food_randomizer

    else:
        m 1eubsb "Got it!"
        jump food_randomizer
    return

label food_randomizer:
        $ _history_list.pop()
        menu:
            m "What type of food do you want to eat?{fast}"
            "A Snack.":
                $ snack = renpy.random.choice(mfoodideassnack)
                m 1eud "Alright! Let me see..."
                m 1hub "How about [snack]?"
                jump food_randomizer_loop

            "A Full Meal.":
                $ meal = renpy.random.choice(mfoodideasmeal)
                m 1eud "Alright! Let me see..."
                m 1hub "How about [meal]?"
                jump food_randomizer_loop

            "A Morning Food.":
                $ breakfast = renpy.random.choice(mfoodideasmorning)
                m 1eud "Alright! Let me see..."
                m 1hub "How about [breakfast]?"
                jump food_randomizer_loop

label food_randomizer_loop:
    m "Do you want a different choice?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want a different choice?{fast}"
        "Yes.":
            m "Alright!"
            jump food_randomizer
        "I'm good.":
            m "Alright, hope that helps!~"
            return

#high or low game (im goated, it works too ez)

define numb1 =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
define numb2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
default hlscore = 0

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
    m 1tub "The number is... [num]!"
    m 4hub "Will the next one be higher or lower?{nw}"
    $ num2 = renpy.random.choice(numb2)
    $ _history_list.pop()
    menu:
        m "Will the next one be higher or lower?{fast}"
        "It's higher!":
            if num2 > num:
                m 4eub "Correct! The number, [num2], was higher!"
                $ hlscore += 1
            elif num2 == num:
                m 4eub "The numbers were equal!"
            else:
                m 2lkbfsdlb "Incorrect! The number, [num2], was lower."
            jump monika_lbe_holgameend

        "It's lower!":
            if num2 < num:
                m 4eub "Correct! The number, [num2], was lower!"
                $ hlscore += 1
            elif num2 == num:
                m 4eub "The numbers were equal!"
            else:
                m 2lkbfsdlb "Incorrect! The number, [num2], was higher."
            jump monika_lbe_holgameend


label monika_lbe_holgameend:
    m 1eubsb "You have [hlscore] correct so far!"
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

# pop

define lbe_cumb_lyric = "Hey I just met you, and this is crazy..."
define lbe_cumb_ans = ["but heres my number", "but here's my number", "but heres my number, so call me, maybe"]

define lbe_happy_lyric = "Because i'm happy..."
define lbe_happy_ans = ["Clap along if you feel", "clap along if you feel like a room without a roof"]

define lbe_sou_lyric = "Come, come on now, follow my lead (mmmm)..."
define lbe_sou_ans = ["i'm in love with the shape of you", "im in love with the shape of you"]

define lbe_iwitw_lyric = "But I want it that way! Tell me why..."
define lbe_iwitw_ans = ["ain't nothing but a heartache", "aint nothing but a heartache"]

define lbe_barbie_lyric = "I'm a Barbie girl, in the Barbie world..."
define lbe_barbie_ans = ["life in plastic, it's fantastic", "life in plastic it's fantastic", "life in plastic, its fantastic", "life in plastic its fantastic"]

# hip-hop

define lbe_alr_lyric = "My knees gettin' weak, and my gun might blow..."
define lbe_alr_ans = ["but we gon' be alright", "but we gon be alright", "we gon be alright", "we gonna be alright", "but we gonna be alright"]

define lbe_hotbli_lyric = "You used to call me on my cell phone..."
define lbe_hotbli_ans = ["late-night when you need my love", "late night when you need my love"]

define lbe_cua_lyric = "Can I get a kiss?"
define lbe_cua_ans = ["and can you make it last forever?", "and can you make it last forever"]

define lbe_mock_lyric = "Now hush little baby, don't you cry..."
define lbe_mock_ans = ["everything's gonna be alright", "everythings gonna be alright"]

define lbe_thrift_lyric = "I'm gonna pop some tags..."
define lbe_thrift_ans = ["only got twenty dollars in my pocket"]

# i got the finish the lyric working! theres probably a better way to do this
# but whatever we ball

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lbe_finish_the_lyric",
            category=["minigames"],
            prompt="Do you want to play finish the lyric?",
            random=False,
            pool=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label lbe_finish_the_lyric:
    m 3hub "Of course! Let me look at the songs I have here.{w=0.1}.{w=0.1}.{w=0.1}"
    m 1eub "Alright! What type of music do you want to do?{nw}"
    menu:
        m "Alright! What type of music do you want to do?{fast}"
        "Pop.":
            jump lbe_ftl_pop1
        "Rap/Hip Hop.":
            jump lbe_ftl_rap1
            return
        "Nevermind.":
            m 3hub "All good, [player]. Let me know whenever you want to play!"
            return

label lbe_ftl_pop1:
    $ lbe_lyric_list_pop = [lbe_happy_lyric, lbe_cumb_lyric, lbe_barbie_lyric, lbe_iwitw_lyric, lbe_sou_lyric]

    $ lbe_lyricpop = renpy.random.choice(lbe_lyric_list_pop)
    m 1dua "Okay! Let me think of a song.{w=0.1}.{w=0.1}.{w=0.1}"
    m 1fub "Here's your lyric: {i}[lbe_lyricpop]{/i}"

    jump lbe_ftl_pop2

label lbe_ftl_pop2:
    $ lbe_lyric = renpy.input("What is the rest of the line/lyric?", length=1000).lower()

    if lbe_lyricpop == lbe_cumb_lyric:
        if lbe_lyric in lbe_cumb_ans:
            m 3wub "You got it right! The song was Call Me Maybe by Carly Rae Jepsen!"
            jump lbe_ftl_end
        elif lbe_lyric == "":
            m 2tfb "Hey, you didn't type anything! Try again~"
            jump lbe_ftl_pop2
        else:
            m 3hkb "That's incorrect! The song was Call Me Maybe by Carly Rae Jepsen!"
            jump lbe_ftl_end
    elif lbe_lyricpop == lbe_happy_lyric:
        if lbe_lyric in lbe_happy_ans:
            m 3wub "You got it right! The song was Happy by Pharrell Williams!"
            jump lbe_ftl_end
        elif lbe_lyric == "":
            m 2tfb "Hey, you didn't type anything! Try again~"
            jump lbe_ftl_pop2
        else:
            m 3hkb "That's incorrect! The song was Happy by Pharrell Williams!"
            jump lbe_ftl_end
    elif lbe_lyricpop == lbe_sou_lyric:
        if lbe_lyric in lbe_sou_ans:
            m 3wub "You got it right! The song was Shape of You by Ed Sheeran!"
            jump lbe_ftl_end
        elif lbe_lyric == "":
            m 2tfb "Hey, you didn't type anything! Try again~"
            jump lbe_ftl_pop2
        else:
            m 3hkb "That's incorrect! The song was Shape of You by Ed Sheeran!"
            jump lbe_ftl_end
    elif lbe_lyricpop == lbe_iwitw_lyric:
        if lbe_lyric in lbe_iwitw_ans:
            m 3wub "You got it right! The song was I Want It That Way by Backstreet Boys!"
            jump lbe_ftl_end
        elif lbe_lyric == "":
            m 2tfb "Hey, you didn't type anything! Try again~"
            jump lbe_ftl_pop2
        else:
            m 3hkb "That's incorrect! The song was I Want It That Way by Backstreet Boys!"
            jump lbe_ftl_end
    elif lbe_lyricpop == lbe_barbie_lyric:
        if lbe_lyric in lbe_barbie_ans:
            m 3wub "You got it right! The song was Barbie Girl by Aqua!"
            jump lbe_ftl_end
        elif lbe_lyric == "":
            m 2tfb "Hey, you didn't type anything! Try again~"
            jump lbe_ftl_pop2
        else:
            m 3hkb "That's incorrect! The song was Barbie Girl by Aqua!"
            jump lbe_ftl_end
    else:
        m "For some reason, the game isn't working... Im sorry, [player]!"
        return

    jump lbe_ftl_end

label lbe_ftl_rap1:
    $ lbe_lyric_list_rap = [lbe_thrift_lyric, lbe_alr_lyric, lbe_hotbli_lyric, lbe_cua_lyric, lbe_mock_lyric]

    $ lbe_lyricrap = renpy.random.choice(lbe_lyric_list_rap)
    m 1dua "Okay! Let me think of a song.{w=0.1}.{w=0.1}.{w=0.1}"
    m 1fub "Here's your lyric: {i}[lbe_lyricrap]{/i}"

    jump lbe_ftl_rap2

label lbe_ftl_rap2:
    $ lbe_lyric = renpy.input("What is the rest of the line/lyric?", length=1000).lower()

    if lbe_lyricrap == lbe_alr_lyric:
        if lbe_lyric in lbe_alr_ans:
            m 3wub "You got it right! The song was Alright by Kendrick Lamar!"
            jump lbe_ftl_end
        elif lbe_lyric == "":
            m 2tfb "Hey, you didn't type anything! Try again~"
            jump lbe_ftl_rap2
        else:
            m 3hkb "That's incorrect! The song was Alright by Kendrick Lamar!"
            jump lbe_ftl_end
    elif lbe_lyricrap == lbe_hotbli_lyric:
        if lbe_lyric in lbe_hotbli_ans:
            m 3wub "You got it right! The song was Hotline Bling by Drake!"
            jump lbe_ftl_end
        elif lbe_lyric == "":
            m 2tfb "Hey, you didn't type anything! Try again~"
            jump lbe_ftl_rap2
        else:
            m 3hkb "That's incorrect! The song was Hotline Bling by Drake!"
            jump lbe_ftl_end
    elif lbe_lyricrap == lbe_cua_lyric:
        if lbe_lyric in lbe_cua_ans:
            m 3wub "You got it right! The song was See you again by Tyler, The Creator!"
            jump lbe_ftl_end
        elif lbe_lyric == "":
            m 2tfb "Hey, you didn't type anything! Try again~"
            jump lbe_ftl_rap2
        else:
            m 3hkb "That's incorrect! The song was See you again by Tyler, The Creator!"
            jump lbe_ftl_end
    elif lbe_lyricrap == lbe_mock_lyric:
        if lbe_lyric in lbe_mock_ans:
            m 3wub "You got it right! The song was Mockingbird by Eminem!"
            jump lbe_ftl_end
        elif lbe_lyric == "":
            m 2tfb "Hey, you didn't type anything! Try again~"
            jump lbe_ftl_rap2
        else:
            m 3hkb "That's incorrect! The song was Mockingbird by Eminem!"
            jump lbe_ftl_end
    elif lbe_lyricpop == lbe_thrift_lyric:
        if lbe_lyric in lbe_thrift_ans:
            m 3wub "You got it right! The song was Thrift Shop by Macklemore!"
            jump lbe_ftl_end
        elif lbe_lyric == "":
            m 2tfb "Hey, you didn't type anything! Try again~"
            jump lbe_ftl_rap2
        else:
            m 3hkb "That's incorrect! The song was Thrift Shop by Macklemore!"
            jump lbe_ftl_end
    else:
        m 2mksdlb "For some reason, the game isn't working... Im sorry, [player]!"
        return

    jump lbe_ftl_end


label lbe_ftl_end:
    m "Do you want to keep on playing?{nw}"
    $ _history_list.pop()
    menu:
        m 3eub "Do you want to keep on playing?{fast}"
        "Yes.":
            $ lbe_lyricpop = None
            $ lbe_lyricrap = None
            jump lbe_finish_the_lyric
        "No.":
            m 3hub "Okay. Thanks for playing with me!"
            return


# i did remove the touch feature, kinda pointless ngl

# racing game

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
    menu:
        "I'm ready!":
            jump lbe_race_game
        "I changed my mind.":
            m "No worries! We'll play another time."
    return

# submod header

init -990 python in mas_submod_utils:
    Submod(
        author="Betapop",
        name="Little Bit of Everything",
        description="A submod that adds new topics, spritepacks, interactions and more! Find the Github {a=https://github.com/betapop/Beta-MAS-lbe}{i}{u}here!{/u}{/i}{/a}",
        version="1.1.1",
    )

