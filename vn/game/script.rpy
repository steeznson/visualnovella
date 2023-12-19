# The script of the game goes in this file.

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
    # replace it by adding a file named "anime_james_elf.png" to the images
    # directory.

    show anime_james_elf at left:
        zoom 0.5

    # These display lines of dialogue.

    e "Here is our template."

    show goblin_oni at right:
        zoom 0.5

    f "We've got a long way to go, baby!"

    # This ends the game.

    e "No time to waste, let's bone! I call topsies."

    return
