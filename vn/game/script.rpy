# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define priest_speech = Character("The Priest")
define superego_speech = Character("The Deontologist")
define id_speech = Character("The Consequentialist")


# The game starts here.

label start:

    play music "gnossienne-1.ogg"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cell

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

    priest_speech """
        'I can't see anything,' is what's meant.
        Those who say, 'I can't see shit' instead say a lot about how they feel about anything; 
        apparently, it's interchangeable with fecal matter. How miserable indeed.
    """

    show consequentialist:
        xalign 0.85        yalign 0.70
        zoom 0.25
    with Dissolve(.25)

    id_speech "Forget that, priest. You have more pressing concerns."

    hide consequentialist
    with Dissolve(.25)

    show blindpriest_happy at center:
        zoom 0.6

    hide blindpriest

    priest_speech """
        My old friend - here to badger me again, no doubt. He often has my best interests at heart, 
        however. Bless him 
    """
    # hide blindpriest_happy

    show blindpriest_happy at left:
        zoom 0.6
    with Dissolve(.25)

    show consequentialist:
        xalign 0.85
        yalign 0.70
        zoom 0.25
    with Dissolve(.25)

    priest_speech """
        Such as? 
    """
    hide blindpriest_happy
    
    show blindpriest at left:
        zoom 0.6
        
    id_speech "Better you figure that out for yourself - I don't want to shock you." 
    



    menu: 

        "why don't you try having a rummage around?" 

        "Tap the ground with your staff":
            jump tapground
            
        "Crouch down and feel the ground":
            jump crouchdown 

           
        
    label tapground:

        $ menu_flag = True 
 
        "I hardly need the sound to inform me the floor is hard, cold flagstone - as the pain 
        in my back attests, I've been sleeping on it the past few hours. The sound echoes 
        throughout the room - I think the walls are bare, and the space is narrow and enclosed."
      
        jump menu_end
            
    label crouchdown:
            
        $ menu_flag = False 

        "The floor is cool and clammy - it feels like roughly hewn flagstone, mottled with
        dirt and grime. I could think of more comfortable beds - judging by the pain in 
        my back, I've been sleeping here for the past few hours, at least."
  
        jump menu_end 

    label menu_end: 

    priest_speech """
        Oh my, it seems I've fallen on hard circumstances. 
    """
    id_speech """
        "I'll say - try a little harder priest, step forward.
    """ 

    hide consequentialist
    with Dissolve(.25)

    show blindpriest at center:
        zoom 0.6
    with Dissolve(.25)

    menu: 

        "There's nothing for it..." 

        "Walk forward.": 
            "I inch forward apprehensively, my staff raised in front."
            jump walk_forward

    label walk_forward: 
        if menu_flag:
            "From the sound I made earlier, I guessed I was in an open space, but no-"

        else:
            """Not for long, as I was stopped in my tracks by something tall, thin, metallic -
            and legion."""

    hide blindpriest

    show priest_behind_bars at center:
        zoom 0.6
    with Dissolve(.50) 

    id_speech """
        You figured it out yet? You're in the clink priest. This is another fine mess 
        you've gotten us into. 
    """
    label walk_forward_end: 

    hide priest_behind_bars
    with Dissolve(.50) 

    show blindpriest at left:
        zoom 0.6
    with Dissolve(.25) 

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

        hide blindpriest
        with Dissolve(.25)

        hide deontologist
        with Dissolve(.25)

        hide consequentialist
        with Dissolve(.25)

        show priest_behind_bars at center:
            zoom 0.75
        with Dissolve(.25)

        priest_speech """
            ...
        """
        
        hide priest_behind_bars
        
        scene bg bed
        with Dissolve(.5)
            
        show priest_falling:
            xalign 0.5
            yalign 0.1
            zoom 0.75
        with Dissolve(.5)

        pause(0.5)
        "I feel myself suddenly falling..."

        # priest_speech """
        #     ...
        # """


        # ... the game continues here.

    # This ends the game.

    return
