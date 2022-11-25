# To-do:
    # Change hour format into dd:hh
    #


define e = Character("Hypervisor")

label start:

    play music "lovelynight.ogg"

    scene bg room

    show trinity happy

    "Congratulations!"
    "u quit your job!"

    menu:
        "OK!":
            jump prologue

label prologue:

label query:

    menu:

        e "Would you like to view the tutorial?"

        "Yes.":
            jump tutorial
        "No.":
            jump varia


label tutorial:

    "You are a for-hire paramedic."

    "As time passes and actions are taken, you AgE accordingly."

    "As you take actions on behalf of your client, your max CoST (or in RPG parlance, constitution) expands proportionally."

    "You can overclock actions (🃏 RPM) to earn tips, 19 & 37 percent proportionally."



    "Choosing to ReST each hour recovers 1/8 of your max CoST."

    "Taking actions which exceed your CoST will cause you to take convalescent leave.  After losing time, you must ReST in order to act again."

    "Finishing @ AgE 60 or lower gives the not-so-great ending.  131 and above gives the best one ;)"

    "you take taxi orders from your Windows CE, affectionately dubbed `Dreamcast.`."

    "You have one week, or 168 hours."

    "After a 20 hour shift, you are automatically tired & sleep for 6 hours."

    "On the 7th day, you decided to work overtime.  As such, you don't sleep or recover any CoST if you reach intermezzo with less than 24 hours remaining.  Be careful! "

label varia:
    $ savings = 0
    $ hp = 0
    $ salary = 0
    $ death_counter = 0
    # Cost is related to time_counter, but resets at the start of a work event.
    $ cost = 0
    $ time = 0
    $ day = 1
    $ stress = 0

    "Seven chapters, seven endings.  Will you read the whole story?"

# How a typical day looks like...

label preroutine:

    $ cost = 0
    $ hp = 0

label routine:

    scene bg void
    with dissolve

    $ fare = 0
    $ time_counter = 0

    $ level = savings/60

    $ hp_max = 100*pow(10,(1+(level/100)))

    $ hp_counter = hp_max - hp

    # ! Error - object of type int has no len()
    $ ride_length = renpy.random.randint(30, 300)

    $ time_left = 168 - time

    $ rest = 20 - cost


    menu:
# TBD 6/30,What time countdown.
        "Your age is [level].  [time_left] hours remain; [rest] ReST before intermission.  [hp_counter] / [hp_max] CoST left.  You get a ride going [ride_length] km.  Will you accept?"

        "No, I'm going to ReST.":
            jump rest
        "Accept the ride.":
            jump accept



label rest:

    $ hp -= hp_max/8
    $ time += 1
    $ cost += 1

    play sound "mga.ogg"

    if hp < 0:
        $ hp = 0

    if time >= 168:
        jump ending
    else:
        if cost > 20:
            jump intermission
        else:
            jump routine

label accept:

    $ ride_time = 0

    $ neg_hp = hp_max - hp

    if 1 <= ride_length <= 100:
        $ ride_time += 1
    else:
        if 101 <= ride_length <= 200:
            $ ride_time += 2
        else:
            if 201 <= ride_length <= 300:
                $ ride_time += 3
            else:
                jump metabolism

label metabolism:

    menu:

        e "Choose your MeTA. Age [level], remaining CoST is [neg_hp]; distance [ride_length] km."

        "Low = 888 rpm.  Engine idle, no tip.":
            $ stress = 888/60
            $ bonus = 0
            jump resolve
        "Medium = 2221 rpm.  Small talk, 19 tip.":
            $ stress = 1337/60
            $ bonus = 1.19
            jump resolve
        "High = 3499 rpm,  Governor limit, 37 tip.":
            $ stress = 1409/60
            $ bonus = 1.37
            jump resolve

label resolve:

    $ time += ride_time

    $ cost += ride_time

    $ stress_counter = 0

    $ stress_counter += (ride_length/33)*stress*(level/3)

    $ hp += stress_counter

    $ fare = ((ride_time*88)+(1*bonus*ride_length))/2

    $ ride_time = 0

    $ savings += fare

    play sound "mga.ogg"

    "You bleed [stress_counter] CoST."

    if time >= 168:
        jump ending
    else:
        if cost > 20:
            jump intermission
        else:
            if hp > hp_max:
                $ death_counter += 1
                jump fail_safe
            else:
                jump routine

label intermission:

    scene bg galaxy
    with fade

    $ level = savings / 60

    play sound "mgaget.ogg"

    $ cost = 0

    menu:
        "Congratulations!  You are now level [level].":
            jump int

label int:
    "You rest for 4 dream cycles. (🃏 6)"

    if 0 < time < 24:
        $ day += 1
        jump chapter_1
    else:
        if 24 < time < 48:
            $ day += 1
            jump chapter_2
        else:
            if 48 < time < 72:
                $ day += 1
                jump chapter_3
            else:
                if 72 < time < 96:
                    $ day += 1
                    jump chapter_4
                else:
                    if 96 <  time < 120:
                        $ day += 1
                        jump chapter_5
                    else:
                        if 120 < time < 144:
                            $ day += 1
                            jump chapter_6
                        else:
                            if time > 168:
                                jump chapter_7
                            else:
                                jump routine

# Chapters.
label chapter_warp:

    $ time += 9

    jump intermission


label chapter_1:
    "Day 1, Friday."
    "Rough Seas."
    "Did you have to pay for your own seabag?"

    "Paid your own way.  Had to take orders to do it."

    "What was it we were fighting for, again?"

    jump preroutine

label chapter_2:
    "Day 2, Saturday."
    "Innovation."

    "fdr's new deal"
    "speeding down the f d r"
    "in a cybertruck."

    "(for groceries oof)"

    "Gas prices are horrible!  Plus combustion engines spit out toxic fumes all day long."
    "Isn't there a better way?"
    "A day at the park.  clean air & solutions."
    "life after capitalism..."

    jump preroutine

label chapter_3:
    "Day 3, Sunday."
    "Cycles."

    "A war with questionable beginnings and no end."

    "I didn't know how special this place was until I grew up and started driving around."

    "No less than three languages understood on a given day."

    "The tourists left when the pandemic hit."

    "But planes keep taking off & landing here every day."

    "One day, I will get on a plane and never return."

    jump preroutine

label chapter_4:
    "Day 4, Monday."
    "🃏 Axiom Discard."
    "Burn through bridges!"

    "Saturdays spent away from home."

    "Thinking of music that I'd look forward to waking up to..."


    "Parents were always working."

    "I didn't learn about the true nature of economics from anyone but myself, since everyone was so busy working."

    "So the same fate befell me."

    "I didn't want this for my child..."

    jump preroutine

label chapter_5:
    "Day 5, Tuesday."

    "🃏 Creativity."
    "Failing at a new dish.  Falling off a skateboard you made.  Trying new things."

    "Two doves gaze, softly"
    "Cooling down around my mind"
    "As the world spins round"

    "I love to cook."

    "It reminds me of my connection to Earth."

    "Making something new."

    jump preroutine

label chapter_6:
    "Wednesday, New Year's Eve."
    "Day 6."
    "🃏 Healing."

    "Exhausted from working in the sun's brilliance."

    "Music, arts, eating heartily."

    "It's so much more of a life to live than I expected."

    "The funny thing is,"

    "it was once someone else's dream."

    "And now it's mine."

    jump preroutine

label chapter_7:
    "New Year's Day."

    "electric skateboard"
    "down the hills of prospect park"
    "a dove, nondescript."

    "I used to like Tuesdays because the city was quiet compared to all the other days."
    "After the pandemic, it got too quiet."
    "So I decided that it was time to leave."


# After ride finishes, check if clock_counter >= resting time.


# And an ending based on points.  This happens after the engine works and is tested thoroughly.
# Endings:
label ending:

    scene bg night
    with dissolve

    if level >= 131:
        jump end_7
    else:
        if 120 <= level <= 130:
            jump end_6
        else:
            if 111 <= level <= 119:
                jump end_5
            else:
                if 101 <= level <= 110:
                    jump end_4
                else:
                    if 84 <= level <= 100:
                        jump end_3
                    else:
                        if 61 <= level <= 83:
                            jump end_2
                        else:
                            if level <= 60:
                                jump end_1

# Make sure that you include in ending dialogue the score threshold required.
# Ending dialogue.

label end_7:

    "Your star, blazing through"
    "From the point of no return"
    "til the end of time..."

    "My seabag, full of gifts from strangers from many different countries..."
    e "Thanks, everyone!"
# you are my fancy# https://music.youtube.com/watch?v=sClwRtvwZc0&feature=share

    jump end

label end_6:
    "I live off the land now."
    "Leaving the rat race behind..."
    "Walking through a meadow of grass, I notice plants growing that look out of place."
    "Swiss chard here, a fruit that looks like pomegranate..."

    jump end

label end_5:
    "Started a new business, a cloud kitchen selling healthy seafood potstickers in the newest gentrified blocks."
    "A wise man once said that food is medicine."
    "Meeting with everyone from all over the world, all in this one city."

    jump end

label end_4:
    "I work hard for the rest of my life.  Some days are tedious, but it's mostly nice."
    "Became a line cook in Montreal."
    e "Finding an ideal balance between work & downtime."
    "Slowly saving, looking forward to the day where my toil will be over.  And to cook lovely meals for my grandchildren!"

    jump end

label end_3:
    "What's the value of all your stuff in that seabag?, the customs officer asked."
    "It was all free, a gift from a relative."

    jump end

label end_2:
    "You broke even. So you decided it wasn't for you."
    "Then you decided to be an essential worker & ended up catching Covid."
    "Laying in bed, wondering if I'd make it.."

    "As water & the virus saturated my usually ashen skin, the one thing that kept coming to mind was that you are not your source of income."
    "All I wanted was to provide for my child."

    e "But will I make it to the next day?"

    jump end

label end_1:
    "You couldn't make the rent."
    "As a matter of fact, you owe the taxi company."
    "What does it mean to be healthy in the 21st century?"

    e "Does your government really care if you can't play the global game of capitalism?"

    "Without the help of family & friends, I would've been forced to choose between eating well and a roof over my head."

    "Without community, all of life's necessities might just be luxuries."

    "ReST well..."

    jump end

label fail_safe:

    if death_counter == 1:
        $ time += 12
        jump d25
    else:
        if death_counter == 2:
            $ time += 26
            jump d50
        else:
            if death_counter == 3:
                $ time += 42
                jump d75
            else:
                if death_counter == 4:
                    jump game_over







label d25:
    "Sometimes you need to remember to go offline & take the mask off."
    "While your body doesn't get less oxygen from being masked, recirculating CO2 pushes your body into a more acidic state."
    "Prevention is better than cure."
    "You rest for 12 hours to reverse the toll on your body."

    jump routine

label d50:
    "Take the mask off."
    "Sometimes you're forced to live this way."
    "To work up to the point of exhaustion."
    "Whom is there to impress with items of luxury now?"
    "You have been incapacitated for 26 hours."

    jump routine

label d75:
    "Take a break."
    "The recycled CO2 from over exertion while being masked for work pushes your body into metabolic acidosis."
    "You have been hospitalized."
    "Extreme stress can sometimes break the mind of a person."
    "42 hours lost."
    jump routine

label game_over:

    jump ending



label end:

# This ends the game.
return
# True ending WiP:  Make variables e1 ➡️7, d1>4.
# If all endings are met, then true ending is revealed.
# '"5000 km away..."
