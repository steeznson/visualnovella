# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Yung Steezy")
define f = Character("The Deontologist")
define g = Character("The Consequentialist")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "anime_james_elf.png" to the images
    # directory.

    show blindpriest at left:
        zoom 0.6
    with Dissolve(.25)
    
 

    # These display lines of dialogue.

    e """
        'I can't see shit' is a curious phrase. It denotes blindness,
        but only through the tacit addition of 'even,' that is,
        'I can't {b}even{/b} see shit.'
    """

    hide blindpriest
    with Dissolve(.25)

    show consequentialist at right:
        zoom 0.25
    with Dissolve(.25)

    f '...'

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at left:
        zoom 0.6
    with Dissolve(.25)

    e """
        The thinking is that if even shit, that most conspicuous,
        and unwelcome of stimuli, eludes your sight,
        then there can't be much of anything else to see either.
    """

    e """
        I think of it another way; that most of what you {i}can{/i},
        see {b}is{/b} shit, and so if you can't see that, you can't see
        nothing. Which is to say, anything, if you get my meaning.
    """

    hide blindpriest
    with Dissolve(.25)

    show consequentialist at right:
        zoom 0.25
    with Dissolve(.25)

    f "woah dude"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at left:
        zoom 0.6
    with Dissolve(.25)

    e """
        But hold on, isn't shit generally something you'd avoid looking at,
        even if you could see? So then, the whole thing falls apart.
    """

    hide blindpriest
    with Dissolve(.25)

    show consequentialist at right:
        zoom 0.25
    with Dissolve(.25)

    f "huh?"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at left:
        zoom 0.6
    with Dissolve(.25)

    e """
        As in, you might be able to see perfectly well,
        but are understandably avoiding the sight of shit,
        perhaps due to a genteel over-sensitivity of the nerves.
    """

    hide blindpriest
    with Dissolve(.25)

    show consequentialist at right:
        zoom 0.25
    with Dissolve(.25)

    f "hmm"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at left:
        zoom 0.6
    with Dissolve(.25)


    e """
        And to digress, if shit were something you were intent
        on avoiding, you might be at a distinct disadvantage
        if you couldn't see it.
    """

    hide blindpriest
    with Dissolve(.25)

    show consequentialist at right:
        zoom 0.25
    with Dissolve(.25)

    f "yeah"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at left:
        zoom 0.6
    with Dissolve(.25)

    e "In which case, you'd hope you could at the very least smell it."

    hide blindpriest
    with Dissolve(.25)

    show consequentialist at right:
        zoom 0.25
    with Dissolve(.25)

    f "Ok"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at left:
        zoom 0.6
    with Dissolve(.25)

    e """
        'I can't see anything,' is what's meant.
        It says much about the sentiments of those who say,
        'I can't see shit,' instead, particularly how they feel
        about anything; apparently, it's interchangeable with fecal matter.
    """

    hide blindpriest
    with Dissolve(.25)

    show consequentialist at right:
        zoom 0.25
    with Dissolve(.25)

    f "Sure"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at left:
        zoom 0.6
    with Dissolve(.25)

    e """
        The world must be a very desolate place for them;
        for them, literally nothing is distinguishable from shit.
        How miserable indeed.
    """

    hide blindpriest
    with Dissolve(.25)

    show consequentialist at right:
        zoom 0.25
    with Dissolve(.25)

    f "Very"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at left:
        zoom 0.6
    with Dissolve(.25)

    e """
        No, if you wanted to be truly cut and dry about the thing,
        you'd say, 'I can see neither shit, nor anything that is not
        shit.' Although that does have less of a ring to it, I suppose.
    """

    hide blindpriest
    with Dissolve(.25)

    show consequentialist at right:
        zoom 0.25
    with Dissolve(.25)

    f "..."

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at left:
        zoom 0.6
    with Dissolve(.25)

    e """
        Right, final try. Let's just say, if shit were here,
        I couldn't see it. But I could sure as hell smell it,
        buster, you betcha.
    """

    e "There, that strikes the right tone, doesn't it?"

    hide blindpriest
    with Dissolve(.25)

    show consequentialist at right:
        zoom 0.25
    with Dissolve(.25)

    f "Sure"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at left:
        zoom 0.6
    with Dissolve(.25)

    e """
        Anyway, that's where I'm at currently, as far as shit
        and sight are concerned. Blind as a fucking bat, me.
        Want to hear all that again?
    """

    hide blindpriest
    with Dissolve(.25)

    show consequentialist at right:
        zoom 0.25
    with Dissolve(.25)

    menu:

        "Yes, I do.":
            hide consequentialist
            with Dissolve(.25)
            jump start

        "No, I don't.":
            jump next_scene


    label next_scene:

        hide consequentialist
        with Dissolve(.25)

        show blindpriest at left:
            zoom 0.6
        with Dissolve(.25)

        e """
            We'll continue our game here, but for now we're done.
        """


        # ... the game continues here.
 

    # This ends the game.

    return
