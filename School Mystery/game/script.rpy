# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define p = Character("Player")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg player room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show phone

    # These display lines of dialogue.

    p "Who's texting me at 3AM."

    p "WHAT! Sophia has been captured by the Saturday night killer!"

    p "How could she do something like be out at a Sunday night! She knows that the killer attacks on Sunday's nights! I have to find her before Saturday or she's dead!"

    # This ends the game.

    return
