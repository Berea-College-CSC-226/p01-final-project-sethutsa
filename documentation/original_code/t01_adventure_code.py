######################################################################
# Author: Utsa Seth and Sonam Tsering
# username: sethutsa and Sonam867
#
# Assignment: T01: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
######################################################################
# Acknowledgements:
#   Original Authors: Dr. Scott Heggen and Prof. Brian Schack
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
#
######################################################################
from functools import reduce
from operator import truediv
from time import sleep

delay = 2  # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False  # You start out not dead, which is good.

# Asks the user to input their name.
username = input("What do they call you, unworthy adversary? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome,", username, ", to the labyrinth.")
sleep(delay)
print("Before you lie two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print("\n")
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

direction = input("Which direction would you like to go? [North/South/East/West]")

if direction == "North":
    # Good choice!
    print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
    sleep(delay)
elif direction == "South":
    # Oh... Bad choice
    print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
    sleep(delay)
    print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
    print("Running seems like a good idea now. But... it's really, really dark.")
    print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
    print("He eats you. You are delicious.")
    dead = True
else:
    # Neutral choice
    print(
        "You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# TODO Add your part of the story here.

print("Suddenly, a light switches on. You see two doors, yellow and red.")
color = input("choose your door, type red/yellow: ")
sleep(delay)

if color == "red":
    print(
        "Good job! You chose well. You should find 2 keys in this room. One key leads to the treasure and the other key leads a deadly trap.")
    sleep(delay)
    key = input("which key do you want, 1 or 2: ")
    if key == "1":
        print(
            "A blinding light shines in your eye. You think you're dead, but when you finally adjust to the light, you see a treasure chest filled to the brim with gold and precious stones.")
    else:
        print(
            "A blinding light shines in your eye and you begin to feel very hot. You open your eyes and see a red leathery mass. It's a dragon, and you're its next meal.")
        dead = True

    sleep(delay)
    if dead:
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
        quit()

else:
    print("You encounter a unicorn, a mermaid, and a nymph. They are holding vials in their hand.")
    vial = input("Choose who's vial you want to drink. Type u/m/n: ")
    if vial == "m":
        print("You nervously sip the vial, but it tastes familiar. It's milk. You're safe!")
    elif vial == "u":
        print("You nervously sip the vial... You die.")
        dead = True
    else:
        print(
            "You try to be clever and 'accidentally' drop the vial, the nymph catches on. She pulls out her sword and knocks you out.")
        dead = True

        if dead:
            print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
            quit()

# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# The following is the end of the story. Don't change this section, unless you really want to.
print("Look at that! You made it to the end of the story without dying! ")
print("Congratulations... now go play again and find an interesting way to perish. ")
print("Try again by hitting the green play button.")