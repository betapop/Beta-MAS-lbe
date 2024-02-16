screen game_scr():
    
    #### This part will let us interact with the screen.
    # Put it under the "timer_on" trigger to be able to show it
    # to the player without any interaction.
    if timer_on:
        #### Every 0.5 sec the game will change its state.
        timer 0.5 action Return("smth") repeat True
        
        key "a" action Return("a")
        key "A" action Return("a")
        key "d" action Return("d")
        key "D" action Return("d")
    #
    ####
    
    #### The background of the game screen.
    # If you have predefined image, like "image game bg = 'game_bg.png'",
    # you'll be able to add it simple like:
    add "game bg" anchor (0.0, 0.0) pos (start_pos-125, 227)
    # Note: it is up to you to set the proper position for the bg
    # to let player know how far his car is from start and finish lines.
    #
    # But for now - some pseudographic bg
    # text "   ================================== \n\n====================================" color "#c0c0c0" anchor (0.0, 0.0) pos (start_pos-125, 200)
    # text "#\n#" color "#c0c0c0" anchor (1.0, 0.0) pos (start_pos, 270)
    # text "#\n#" color "#c0c0c0" anchor (0.0, 0.0) pos (finish_pos, 270)
    #
    ####
    
    #### Some of the opponents.
    # Use this part if you've set the "opponents" list.
    # If not - then just comment or delete this part.
    #
    for i, each_opponent in enumerate(opponents):
        ####
        # If you've set the opponent's car appearence as an image
        # then show it as:
        add each_opponent["car"] anchor (1.0, 0.0) pos (each_opponent["opp_car_pos"], 200-(len(opponents)-i)*5)
        #
        # But for pseudographic it will be
        # text (each_opponent["car"]) color (each_opponent["car_color"]) anchor (1.0, 0.0) pos (each_opponent["opp_car_pos"], 200-(len(opponents)-i)*5)
        #
        ####
    #
    ####
    
    #### Player's car.
    # If you have predefined image, like "image car = 'my_car.png'",
    # you'll be able to add it like:
    add "car" anchor (1.0, 0.0) pos (car_pos, 200)
    #
    # But for pseudographic car it will be
    # text "[car]" anchor (1.0, 0.0) pos (car_pos, 200)
    #
    ####

# The game starts here.
label race_game:
    show monika 2subla at t22
    #### Some variables that describes the game state.
    $ car = "___/-----\_____\n=@====@="
    $ start_pos = 200
    $ finish_pos = 600
    $ car_pos = (start_pos + finish_pos)/2
    $ last_pressed = ""
    $ timer_on = False
    
    #### The list of the opponents
    # (each one described by the dictionary).
    # If you have predefined image, like "image red car = 'red_car.png'",
    # you'll be able to set opponent's car appearence like:
    # "car":"red car"
    #
    image game bg = 'submods/little bit of everything [submod]/lbe_assets/road.png'
    image car = 'submods/little bit of everything [submod]/lbe_assets/moni_car.png'
    image yurii car = 'submods/little bit of everything [submod]/lbe_assets/yuri_car.png'
    image natsukii car = 'submods/little bit of everything [submod]/lbe_assets/nat_car.png'
    $ opponents = [
        {"car_name":"Yuri", "car":"yurii car", "car_color":"#c00", "opp_car_pos":(start_pos + finish_pos)/2, "opp_car_move":(-5, 0, 5, 5, 5, 5, 5, 10, 10)},
        {"car_name":"Natsuki", "car":"natsukii car", "car_color":"#0c0", "opp_car_pos":(start_pos + finish_pos)/2, "opp_car_move":(-5, 0, 5, 5, 5, 5, 5, 10, 10)}
        ]
    #
    ####
    
    #### Let's show the game screen.
    #
    show screen game_scr
    
    "Let's begin! Push 'a' and 'd' buttons."
    
    #### And for now the player is able to interact with the game.
    #
    $ timer_on = True
    
    #### The game loop that has all its logic.
    #
    label race_game_loop:
        #### The result of interaction with the game.
        #
        $ res = ui.interact()
        
        #### The game change its state by the timer.
        #
        if res == "smth":
            $ car_pos -= 5
            if car_pos <= start_pos:
                #### Don't forget to turn off the ability to interact
                # with the game before jump to the result of the game.
                #
                $ timer_on = False
                jump race_lose
            
            #### Let's change the opponents positions
            # (if you've set the "opponents" list, ofcourse).
            # If not - then just comment or delete this part.
            #
            python:
                for i in range(len(opponents)):
                    opponents[i]["opp_car_pos"] += renpy.random.choice(opponents[i]["opp_car_move"])
                    if opponents[i]["opp_car_pos"] >= finish_pos:
                        winner = opponents[i]["car_name"]
                        timer_on = False
                        renpy.jump("race_over")
            #
            ####
                        
            jump race_game_loop

        #### Let's check if player has pressed the right button.
        #
        elif res == "a" and last_pressed != "a":
            $ last_pressed = "a"
            $ car_pos += 10
        elif res == "d" and last_pressed != "d":
            $ last_pressed = "d"
            $ car_pos += 10
        if car_pos >= finish_pos:
            $ timer_on = False
            jump race_win
        
        jump race_game_loop

#### The results of the game.
#
label race_over:
    $ renpy.pause(0.5, hard=True)
    m 4tub "[winner] finished first! Sorry [player]~"
    hide screen game_scr
    jump play_again
    
label race_lose:
    $ renpy.pause(0.5, hard=True)
    m 1tub "Too slow!~"
    hide screen game_scr
    jump play_again
    
label race_win:
    $ renpy.pause(0.5, hard=True)
    m 1sublb "You finished first! Good job, [player]!"
    hide screen game_scr
    jump play_again

label play_again:
    m 4eub "Do you want to play again?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to play again?{fast}"
        "Yes!":
            m 4hub "Alright, lets go!"
            jump race_game

        "No, i'm beat.":
            m 1hub "Okay! Thanks for playing!"
            return
