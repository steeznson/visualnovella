# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define priest_speech = Character("The Priest")
define superego_speech = Character("The Deontologist")
define id_speech = Character("The Consequentialist")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "anime_james_elf.png" to the images
    # directory.
    

    show blindpriest at center:
        zoom 0.6
    with Dissolve(.25)

    # These display lines of dialogue.

    priest_speech """
        'I can't see shit' is a curious phrase. It denotes blindness,
        but only through the tacit addition of 'even,' that is,
        'I can't {b}even{/b} see shit.'
    """

    show consequentialist:
        xalign 0.85
        yalign 0.70
        zoom 0.25
    with Dissolve(.25)

    id_speech '...'

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at center:
        zoom 0.6
    with Dissolve(.25)

    priest_speech """
        The thinking is that if even shit, that most conspicuous,
        and unwelcome of stimuli, eludes your sight,
        then there can't be much of anything else to see either.
    """

    priest_speech """
        I think of it another way; that most of what you {i}can{/i},
        see {b}is{/b} shit, and so if you can't see that, you can't see
        nothing. Which is to say, anything, if you get my meaning.
    """

    show consequentialist:
        xalign 0.85
        yalign 0.70
        zoom 0.25
    with Dissolve(.25)

    id_speech "woah dude"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at center:
        zoom 0.6
    with Dissolve(.25)

    priest_speech """
        But hold on, isn't shit generally something you'd avoid looking at,
        even if you could see? So then, the whole thing falls apart.
    """

    show consequentialist:
        xalign 0.85
        yalign 0.70
        zoom 0.25
    with Dissolve(.25)

    id_speech "huh?"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at center:
        zoom 0.6
    with Dissolve(.25)

    priest_speech """
        As in, you might be able to see perfectly well,
        but are understandably avoiding the sight of shit,
        perhaps due to a genteel over-sensitivity of the nerves.
    """

    show consequentialist:
        xalign 0.85
        yalign 0.70
        zoom 0.25
    with Dissolve(.25)

    id_speech "hmm"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at center:
        zoom 0.6
    with Dissolve(.25)


    priest_speech """
        And to digress, if shit were something you were intent
        on avoiding, you might be at a distinct disadvantage
        if you couldn't see it.
    """

    show consequentialist:
        xalign 0.85
        yalign 0.70
        zoom 0.25
    with Dissolve(.25)

    id_speech "yeah"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at center:
        zoom 0.6
    with Dissolve(.25)

    priest_speech """
        In which case, you'd hope you could at the very least smell it."
    """

    show consequentialist:
        xalign 0.85
        yalign 0.70
        zoom 0.25
    with Dissolve(.25)

    id_speech "Ok"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at center:
        zoom 0.6
    with Dissolve(.25)

    priest_speech """
        'I can't see anything,' is what's meant.
        It says much about the sentiments of those who say,
        'I can't see shit,' instead, particularly how they feel
        about anything; apparently, it's interchangeable with fecal matter.
    """

    show consequentialist:
        xalign 0.85
        yalign 0.70
        zoom 0.25
    with Dissolve(.25)

    id_speech "Sure"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at center:
        zoom 0.6
    with Dissolve(.25)

    priest_speech """
        The world must be a very desolate place for them;
        for them, literally nothing is distinguishable from shit.
        How miserable indeed.
    """

    show consequentialist:
        xalign 0.85
        yalign 0.70
        zoom 0.25
    with Dissolve(.25)

    id_speech "Very"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at center:
        zoom 0.6
    with Dissolve(.25)

    priest_speech """
        No, if you wanted to be truly cut and dry about the thing,
        you'd say, 'I can see neither shit, nor anything that is not
        shit.' Although that does have less of a ring to it, I suppose.
    """

    show consequentialist:
        xalign 0.85
        yalign 0.70
        zoom 0.25
    with Dissolve(.25)

    id_speech "..."

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at center:
        zoom 0.6
    with Dissolve(.25)

    priest_speech """
        Right, final try. Let's just say, if shit were here,
        I couldn't see it. But I could sure as hell smell it,
        buster, you betcha.
    """

    priest_speech "There, that strikes the right tone, doesn't it?"

    show consequentialist:
        xalign 0.85
        yalign 0.70
        zoom 0.25
    with Dissolve(.25)

    id_speech "Sure"

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at center:
        zoom 0.6
    with Dissolve(.25)

    priest_speech """
        Anyway, that's where I'm at currently, as far as shit
        and sight are concerned. Blind as a fucking bat, me.
        Want to hear all that again?
    """

    show consequentialist:
        xalign 0.85
        yalign 0.70
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

        # hide consequentialist
        # with Dissolve(.25)

        show blindpriest at center:
            zoom 0.6
        with Dissolve(.25)

        priest_speech """
            We'll continue our game here, but for now we're done.
        """

        show deontologist:
            xalign 0.10
            yalign 0.60
            zoom 0.25
        with Dissolve(.25)

        superego_speech """
            You'll regret not heeding my warning.
        """


        # ... the game continues here.

    # This ends the game.

    return
