import random

dnd_dice = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']


def roll_dice():
    dice = input("What would you like to roll? d4, d6, d8, d10, d12, d20, or a d100? ")
    while dice not in dnd_dice:
        print("Please enter one of the following dice: d4, d6, d8, d10, d12, d20, d100")
        dice = input("Please enter dnd dice: ")
    print("Rolling...")
    die = int(dice[1:])
    roll = random.randint(1, die)
    print(roll)

    proceed = input("Would you like to roll another set? ").lower()

    if proceed == "yes":
        user_input()
    else:
        print("Good Luck")


def roll_many_dice():
    while True:
        try:
            dice_number = int(input("How many dice would you like to roll: "))
            break
        except ValueError:
            print("Please enter a valid number")
    dice = input("What would you like to roll? d4, d6, d8, d10, d12, d20, or a d100? ")
    while dice not in dnd_dice:
        print("Please enter one of the following dice: d4, d6, d8, d10, d12, d20, d100")
        dice = input("Please enter dnd dice: ")
    die = int(dice[1:])
    sum_roll = 0
    for i in range(int(dice_number)):
        roll = random.randint(1, die)
        sum_roll = sum_roll + roll
    print("Overall Total: ", sum_roll)

    proceed = input("Would you like to roll another set? ").lower()

    if proceed == "yes":
        user_input()
    else:
        print("Good Luck")


def user_input():
    while True:
        user_results = input("Are you looking to roll "'"many"'" dice, or "'"single"'" dice? ").lower()
        if user_results == "single":
            roll_dice()
        elif user_results == "many":
            roll_many_dice()
        break


user_navigation = input("Do you just want to "'"Roll"'" a dice or go with a "'"Character"'" roll? ").lower()

if user_navigation == "roll":
    user_input()
elif user_navigation == "character":
    print("In production")
