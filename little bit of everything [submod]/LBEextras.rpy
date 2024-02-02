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