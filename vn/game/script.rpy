﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Yung Steezy")
define f = Character("El Goblino")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "blind_guy.png" to the images
    # directory.

    show blind_guy at left:
        zoom 0.5

    # These display lines of dialogue.

    e "\"I can't see shit\" is a curious phrase. It denotes blindness, but only through the tacit addition of \"even,\" that is, \"I can't {b}even{/b} see shit.\""

    hide blind_guy

    show goblin_oni at right:
        zoom 0.5

    f '...'

    hide goblin_oni

    show blind_guy at left:
        zoom 0.5

    e "The thinking is that if even shit, that most conspicuous and unwelcome of stimuli, eludes your sight, then there can't be much of anything else to see either."

    e "I think of it another way; that most of what you {i}can{/i} see {b}is{/b} shit, and so if you can't see that, you can't see nothing. Which is to say, anything, if you get my meaning."

    hide blind_guy

    show goblin_oni at right:
        zoom 0.5

    f "woah dude"

    hide goblin_oni

    show blind_guy at left:
        zoom 0.5

    e "But hold on, isn't shit generally something you'd avoid looking at, even if you could see? So then, the whole thing falls apart." 

    hide blind_guy

    show goblin_oni at right:
        zoom 0.5

    f "huh?"

    hide goblin_oni

    show blind_guy at left:
        zoom 0.5

    e "As in, you might be able to see perfectly well, but are understandably avoiding the sight of shit, perhaps due to a genteel over-sensitivity of the nerves. "

    hide blind_guy

    show goblin_oni at right:
        zoom 0.5

    f "hmm"

    hide goblin_oni

    show blind_guy at left:
        zoom 0.5

    e "And to digress, if shit were something you were intent on avoiding, you might be at a distinct disadvantage if you couldn't see it."

    hide blind_guy

    show goblin_oni at right:
        zoom 0.5

    f "yeah"

    hide goblin_oni

    show blind_guy at left:
        zoom 0.5

    e "In which case, you'd hope you could at the very least smell it."

    hide blind_guy

    show goblin_oni at right:
        zoom 0.5

    f "Ok"

    hide goblin_oni

    show blind_guy at left:
        zoom 0.5

    e "\"I can't see anything,\" is what's meant. It says much about the sentiments of those who say, \"I can't see shit,\" instead, particularly how they feel about anything; apparently, it's interchangeable with fecal matter."

    hide blind_guy

    show goblin_oni at right:
        zoom 0.5

    f "Sure"

    hide goblin_oni

    show blind_guy at left:
        zoom 0.5

    e "The world must be a very desolate place for them; for them, literally nothing is distinguishable from shit. How miserable indeed."

    hide blind_guy

    show goblin_oni at right:
        zoom 0.5

    f "Very"

    hide goblin_oni

    show blind_guy at left:
        zoom 0.5

    e "No, if you wanted to be truly cut and dry about the thing, you'd say, \"I can see neither shit, nor anything that is not shit.\" Although that does have less of a ring to it, I suppose."

    hide blind_guy

    show goblin_oni at right:
        zoom 0.5

    f "..."

    hide goblin_oni

    show blind_guy at left:
        zoom 0.5

    e "Right, final try. Let's just say, if shit were here, I couldn't see it. But I could sure as hell smell it, buster, you betcha."

    e "There, that strikes the right tone, doesn't it?"

    hide blind_guy

    show goblin_oni at right:
        zoom 0.5

    f "Sure"

    hide goblin_oni

    show blind_guy at left:
        zoom 0.5

    e "Anyway, that's where I'm at currently, as far as shit and sight are concerned. Blind as a fucking bat, me."

    # show goblin_oni at right:
    #     zoom 0.5

    # f "We've got a long way to go, baby!"

    # This ends the game.

    # e "No time to waste, let's bone! I call topsies."

    return
