# import DnD_Weapons_Armor
import random
import collections

# import Character_Roll

# while True:
#     try:
#         data=int(input("Enter a Number: "))
#         print ("You entered: ", data)
#         break;
#     except ValueError:
#         print ("Invalid input")

# while True:
#     try:
#         number_of_dice = int(input("Enter how many dice you need rolled: "))
#         print("You entered: ", number_of_dice)
#         break;
#     except ValueError:
#         print("Not an actual number")
# dnd_dice = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']

# def roll_many_dice_test():
#     while True:
#         try:
#             dice_number = int(input("How many dice would you like to roll: "))
#             break
#         except ValueError:
#             print("Please enter a valid number")
#     dice = input("What would you like to roll? d4, d6, d8, d10, d12, d100, or a d20? ")
#     while dice not in dnd_dice:
#         print("Please enter one of the following dice: d4, d6, d8, d10, d12, d20, d100")
#         dice = input("Please enter dnd dice: ")
#     die = int(dice[1:])
#     sum_roll = 0
#     for i in range(int(dice_number)):
#         roll = random.randint(1, die)
#         sum_roll = sum_roll + roll
#     print("Overall Total: ", sum_roll)
#
#
# roll_many_dice_test()

# results = ['many'.lower(), 'single'.lower()]
#
#
# def user_input():
#     user_results = input("Are you looking to roll "'"many"'" dice, or "'"single"'" dice? ")
#     while user_results != results:
#         user_results = input("Would you want to roll "'"Many"'" or "'"Single"'" dice? ")
#         if user_results.lower() == "many":
#             print("Many dice Activated, prepare for avalanche!!")
#         elif user_results.lower() == "single":
#             print("Single Dice Activated")
#         break;
#
#
# user_input()

# list = ["hello", "honey", "cat", "dog"]
#
# user_input = input("Test: ").lower()
# while user_input not in list:
#     user_input = input("Sorry not in the list, try again: ").lower()
# if user_input in list:
#     if user_input == list:
#         print(user_input)

# print(user_input)


# import random
#
# ability_dict = {"acrobatics": 2, "animal handling": 2, "arcana": 8}
#
# import DnD_Attributes
# ability_stats = ["acrobatics", "animal handling", "arcana", "athletics", "deception", "history", "insight",
#                  "intimidation", "investigation", "medicine", "nature", "perception", "performance", "persuasion",
#                  "religion", "sleight of hand", "survival"]
#
#
# def ability_check():
#     while True:
#         user_ability = input("""What Ability Check would you want to look at:
#                             Acrobatics, Animal Handling, Arcana, Athletics, Deception, History, Insight,
#                             Intimidation, Investigation, Medicine, Nature, Perception, Performance,
#                             Persuasion, Religion, Sleight of Hand, Survival? """).lower()
#         if user_ability in ability_dict.keys():
#             roll = random.randint(1, 20)
#             check = roll + ability_dict[user_ability.lower()]
#             print(f"Your {user_ability} check rolled: ", check)
#             break
#
#
# ability_check()

#
# print(DnD_Weapons_Armor.SimpleWeapons.simple_weapon_damage)
#
# dice = input("Enter dice: ")
# split_dice = dice.split('d')
# dice_num = split_dice[0]
# dice_damage = split_dice[1]
#
# sum_roll = 0
# for i in range(int(dice_num)):
#     roll = random.randint(1, int(dice_damage))
#     sum_roll = sum_roll + roll
# print("Overall Total: ", sum_roll)

# weapon_list = ["Club", "Bow", "Great Axe", "Hammer"]
# dnd_weapons_str = ', '.join(weapon_list)
#
#
# weapon_check = input(f"Please choose one of the following: {dnd_weapons_str}: ")
#
# print("You've chosen: ", weapon_check)

# simple_weapon_list = ["Club", "Dagger", "Great Club", "Hand Axe", "Javelin", "Light Hammer", "Mace", "Quarterstaff",
#                       "Sickle", "Spear"]
# modifiers_raw = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
# dnd_simple_weapon_list = ', '.join(simple_weapon_list)
# dnd_modifiers_raw = ', '.join(modifiers_raw)


# def attack():
#     while True:
#         attack_weapon_input = input("""Please choose from the following groups of weapons:
#                                         Simple Weapons, Simple Ranged Weapons, Simple Martial Weapons,
#                                         Simple Martial Ranged Weapons: """).lower()
#         if attack_weapon_input == "simple weapons":
#             while True:
#                 attack_weapon = input(f"""Please choose from the following weapons:
#                                             {dnd_simple_weapon_list} or Back: """).lower()
#                 if attack_weapon == "back":
#                     attack()
#                 else:
#                     attack_mod = input(f"""Which modifier would you like to attribute to this attack:
#                                         {dnd_modifiers_raw}: """).lower()
#                 break
#             print(attack_weapon, " ", attack_mod)
#
#             break
#         if attack_weapon_input == "simple ranged weapons":
#             print("simple ranged weapons!")
#             break
# attack()

# if attack_weapon in DnD_Weapons_Armor.SimpleWeapons.simple_weapon_damage
# for i in DnD_Weapons_Armor.SimpleWeapons.simple_weapon_damage:
#     if i.__contains__(attack_weapon):
#         print(i)

# for key, value in DnD_Weapons_Armor.SimpleWeapons.simple_weapon_damage.items():
#     print(value)

# print(attack_weapon_dice)

# attack_weapon = input("Enter something: ").lower()
#
# attack_weapon_damage = DnD_Weapons_Armor.SimpleWeapons.simple_weapon_damage.get(attack_weapon)
#
# print(attack_weapon_damage)

# list1 = []
#
# for i in range(0, 7):
#     number = int(input())
#     list1.append(number)
#
# print(list1)

# dwarf_stats_dict = {"str": 0, "dex": 0, "con": 2, "int": 0, "wis": 0, "cha": 0}
# test_dict = {"str": 15, "dex": 14, "con": 13, "int": 10, "wis": 11, "cha": 8}
#
# a_counter = collections.Counter(test_dict)
# b_counter = collections.Counter(dwarf_stats_dict)
#
# add_dict = a_counter + b_counter
# dict_1 = dict(add_dict)
#
# print(dict_1)

# stat_rolls_stored = [15, 14, 13, 12, 10, 8]
# null_stat_dict = {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 0}
# null_stat_dict_2 = {"int": 3, "wis": 5, "cha": 6, "str": 10, "dex": 15, "con": 12}

# for i, stat in zip(null_stat_dict, null_stat_dict_2):
#     null_stat_dict[i] += stat
# print(null_stat_dict)

# stat_dict = collections.Counter(null_stat_dict)
# stat_dict_2 = collections.Counter(null_stat_dict_2)
# total = stat_dict + stat_dict_2

# print(total)

# test_race = ["Gnome"]
# race = ["Human Variant", "Half-Elf"]
#
# test_dict = {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 0}
# print(test_dict)
#
# race_check = random.choice(list(test_race))
# print(race_check)
#
#
# def stat_increase():
#     if race_check in race:
#         stat_increases = input("Which stat would you like to increase? str / dex / con / int / wis / cha: ").lower()
#         test_dict[stat_increases] += 1
#         stat_increase_2 = input("Which second stat would you like to increase? (Please choose a different stat then "
#                                 "the First) str / dex / con / int / wis / cha: ").lower()
#         if stat_increase_2 == stat_increases:
#             print("Please choose a different stat than the first")
#             stat_increase_2 = input("Which second stat would you like to increase? (Please choose a different stat "
#                                     "then the first) str / dex / con / int / wis / cha: ").lower()
#             test_dict[stat_increase_2] += 1
#         else:
#             test_dict[stat_increase_2] += 1
#
#
# stat_increase()
#
# print(test_dict)
