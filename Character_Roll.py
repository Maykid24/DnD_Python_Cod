import DnD_Attributes
import random
import DnD_Weapons_Armor

dnd_user_choice = ["ability check", "saving throw", "initiative", "attack", "spell attack"]
ability_dict = {"acrobatics": DnD_Attributes.CharSkills.acrobatics,
                "animal handling": DnD_Attributes.CharSkills.animal_handling,
                "arcana": DnD_Attributes.CharSkills.arcana, "athletics": DnD_Attributes.CharSkills.athletics,
                "deception": DnD_Attributes.CharSkills.deception, "history": DnD_Attributes.CharSkills.history,
                "insight": DnD_Attributes.CharSkills.insight, "intimidation": DnD_Attributes.CharSkills.intimidation,
                "investigation": DnD_Attributes.CharSkills.investigation,
                "medicine": DnD_Attributes.CharSkills.medicine,
                "nature": DnD_Attributes.CharSkills.nature, "perception": DnD_Attributes.CharSkills.perception,
                "performance": DnD_Attributes.CharSkills.performance,
                "persuasion": DnD_Attributes.CharSkills.persuasion,
                "religion": DnD_Attributes.CharSkills.religion,
                "sleight of hand": DnD_Attributes.CharSkills.sleight_of_hand,
                "survival": DnD_Attributes.CharSkills.survival}
saving_dict = {"strength saving": DnD_Attributes.CharSaving.str_saving,
               "dexterity saving": DnD_Attributes.CharSaving.dex_saving,
               "constitution saving": DnD_Attributes.CharSaving.con_saving,
               "intelligence saving": DnD_Attributes.CharSaving.int_saving,
               "wisdom saving": DnD_Attributes.CharSaving.wis_saving,
               "charisma saving": DnD_Attributes.CharSaving.cha_saving}
attack_mod = {"strength": DnD_Attributes.CharModifier.str_modifier,
              "dexterity": DnD_Attributes.CharModifier.dex_modifier,
              "constitution": DnD_Attributes.CharModifier.con_modifier,
              "intelligence": DnD_Attributes.CharModifier.int_modifier,
              "wisdom": DnD_Attributes.CharModifier.wis_modifier,
              "charisma": DnD_Attributes.CharModifier.cha_modifier}
modifiers_raw = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
dnd_modifiers_raw = ', '.join(modifiers_raw)
simple_weapon_list = ["Club", "Dagger", "Great Club", "Hand Axe", "Javelin", "Light Hammer", "Mace", "Quarterstaff",
                      "Sickle", "Spear"]
dnd_simple_weapon_list = ', '.join(simple_weapon_list)
simple_range_weapon_list = ["Crossbow, Light", "Dart", "Shortbow", "Sling"]
dnd_simple_range_weapon_list = ', '.join(simple_range_weapon_list)
simple_martial_weapon_list = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword",
                              "Maul", "Morning Star", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident",
                              "War Pick", "Warhammer", "Whip"]
dnd_simple_martial_weapon_list = ', '.join(simple_martial_weapon_list)
simple_range_martial_weapon_list = ["Blowgun", "Crossbow, Hand", "Crossbow, Heavy", "Longbow"]
dnd_simple_range_martial_weapon_list = ', '.join(simple_range_martial_weapon_list)


def user_choice():
    user_input = input("What are you looking to do: Ability Check / Saving Throw / Initiative / Attack / Spell "
                       "Attack: ").lower()
    while user_input not in dnd_user_choice:
        user_input = input("Sorry, that is not a valid choice, please pick one of the following: Ability Check / "
                           "Saving Throw / Initiative / Attack / Spell Attack ").lower()
    if user_input in dnd_user_choice:
        if user_input == "Ability Check".lower():
            ability_check()
        elif user_input == "Saving Throw".lower():
            saving_throw()
        elif user_input == "Initiative".lower():
            initiative()
        elif user_input == "Attack".lower():
            attack()
        elif user_input == "Spell Attack".lower():
            spell_attack()


def ability_check():
    while True:
        user_ability = input("""Please choose one of the following: 
                               Acrobatics, Animal Handling, Arcana, Athletics, 
                               Deception, History, Insight, Intimidation, Investigation, Medicine, Nature, Perception, 
                               Performance, Persuasion, Religion, Sleight of Hand, Survival: """).lower()
        if user_ability in ability_dict.keys():
            roll = random.randint(1, 20)
            check = roll + ability_dict[user_ability.lower()]
            print(f"Your {user_ability} check rolled: ", check)
            main_menu = input("Would you like to go back to the main menu or exit? (Y/N): ").lower()
            if main_menu == "y":
                user_choice()
            else:
                print("Good Luck!")
            break


def saving_throw():
    while True:
        user_saving = input("""Please choose one of the following:
                               Strength Saving, Dexterity Saving, Constitution Saving, Intelligence Saving,
                               Wisdom Saving, Charisma Saving: """).lower()
        if user_saving in saving_dict.keys():
            roll = random.randint(1, 20)
            check = roll + saving_dict[user_saving.lower()]
            print(f"Your {user_saving} rolled: ", check)
            main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
            if main_menu == "y":
                user_choice()
            else:
                print("Good Luck!")
            break


def initiative():
    roll = random.randint(1, 20)
    check = roll + DnD_Attributes.CharModifier.dex_modifier
    print(f"Your initiative is: ", check)
    main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
    if main_menu == "y":
        user_choice()
    else:
        print("Good Luck!")


def attack():
    global attack_mod_raw

    while True:
        attack_weapon_input = input("""Please choose from the following groups of weapons:
                                        Simple Weapons, Simple Ranged Weapons, Simple Martial Weapons,
                                        Simple Martial Ranged Weapons: """).lower()
        if attack_weapon_input == "simple weapons":
            while True:
                attack_weapon = input(f"""Please choose from the following weapons: 
                                            {dnd_simple_weapon_list} or Back: """).lower()
                if attack_weapon == "back":
                    attack()
                else:
                    attack_mod_raw = input(f"""Which modifier would you like to attribute to this attack:
                                        {dnd_modifiers_raw}: """).lower()
                prof_weapon = input("Are you proficient in this weapon? (Y/N): ").lower()
                if prof_weapon == "y":
                    roll = random.randint(1, 20)
                    check = roll + attack_mod.get(attack_mod_raw) + DnD_Attributes.CharMainStats.prof_bonus
                    print(f"Your attack is: ", check)
                    hit_or_not = input("Does this hit (Y/N): ").lower()
                    if hit_or_not == "y":
                        dice = DnD_Weapons_Armor.SimpleWeapons.simple_weapon_damage.get(attack_weapon)
                        split_dice = dice.split('d')
                        dice_num = split_dice[0]
                        dice_damage = split_dice[1]
                        sum_roll = 0
                        for i in range(int(dice_num)):
                            roll = random.randint(1, int(dice_damage))
                            sum_roll = sum_roll + roll
                        overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                        print("Overall Total: ", overall_sum_roll)
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw) + DnD_Attributes.CharMainStats.prof_bonus
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleWeapons.simple_weapon_damage.get(attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                                break
                    if hit_or_not == "n":
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw) + DnD_Attributes.CharMainStats.prof_bonus
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleWeapons.simple_weapon_damage.get(attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                                break
                if prof_weapon == "n":
                    roll = random.randint(1, 20)
                    check = roll + attack_mod.get(attack_mod_raw)
                    print(f"Your attack is: ", check)
                    hit_or_not = input("Does this hit (Y/N): ").lower()
                    if hit_or_not == "y":
                        dice = DnD_Weapons_Armor.SimpleWeapons.simple_weapon_damage.get(attack_weapon)
                        split_dice = dice.split('d')
                        dice_num = split_dice[0]
                        dice_damage = split_dice[1]
                        sum_roll = 0
                        for i in range(int(dice_num)):
                            roll = random.randint(1, int(dice_damage))
                            sum_roll = sum_roll + roll
                        overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                        print("Overall Total: ", overall_sum_roll)
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw)
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleWeapons.simple_weapon_damage.get(attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                            break
                    if hit_or_not == "n":
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw)
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleWeapons.simple_weapon_damage.get(attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                            break
                break
        if attack_weapon_input == "simple ranged weapons":
            while True:
                attack_weapon = input(f"""Please choose from the following weapons: 
                                            {dnd_simple_range_weapon_list} or Back: """).lower()
                if attack_weapon == "back":
                    attack()
                else:
                    attack_mod_raw = input(f"""Which modifier would you like to attribute to this attack:
                                        {dnd_modifiers_raw}: """).lower()
                prof_weapon = input("Are you proficient in this weapon? (Y/N): ").lower()
                if prof_weapon == "y":
                    roll = random.randint(1, 20)
                    check = roll + attack_mod.get(attack_mod_raw) + DnD_Attributes.CharMainStats.prof_bonus
                    print(f"Your attack is: ", check)
                    hit_or_not = input("Does this hit (Y/N): ").lower()
                    if hit_or_not == "y":
                        dice = DnD_Weapons_Armor.SimpleRangedWeapons.simple_ranged_weapon_damage.get(attack_weapon)
                        split_dice = dice.split('d')
                        dice_num = split_dice[0]
                        dice_damage = split_dice[1]
                        sum_roll = 0
                        for i in range(int(dice_num)):
                            roll = random.randint(1, int(dice_damage))
                            sum_roll = sum_roll + roll
                        overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                        print("Overall Total: ", overall_sum_roll)
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw) + DnD_Attributes.CharMainStats.prof_bonus
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleRangedWeapons.simple_ranged_weapon_damage.get(
                                        attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                                break
                    if hit_or_not == "n":
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw) + DnD_Attributes.CharMainStats.prof_bonus
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleRangedWeapons.simple_ranged_weapon_damage.get(
                                        attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                                break
                if prof_weapon == "n":
                    roll = random.randint(1, 20)
                    check = roll + attack_mod.get(attack_mod_raw)
                    print(f"Your attack is: ", check)
                    hit_or_not = input("Does this hit (Y/N): ").lower()
                    if hit_or_not == "y":
                        dice = DnD_Weapons_Armor.SimpleRangedWeapons.simple_ranged_weapon_damage.get(attack_weapon)
                        split_dice = dice.split('d')
                        dice_num = split_dice[0]
                        dice_damage = split_dice[1]
                        sum_roll = 0
                        for i in range(int(dice_num)):
                            roll = random.randint(1, int(dice_damage))
                            sum_roll = sum_roll + roll
                        overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                        print("Overall Total: ", overall_sum_roll)
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw)
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleRangedWeapons.simple_ranged_weapon_damage.get(
                                        attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                            break
                    if hit_or_not == "n":
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw)
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleRangedWeapons.simple_ranged_weapon_damage.get(
                                        attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                            break
                break
        if attack_weapon_input == "simple martial weapons":
            while True:
                attack_weapon = input(f"""Please choose from the following weapons: 
                                            {dnd_simple_martial_weapon_list} or Back: """).lower()
                if attack_weapon == "back":
                    attack()
                else:
                    attack_mod_raw = input(f"""Which modifier would you like to attribute to this attack:
                                        {dnd_modifiers_raw}: """).lower()
                prof_weapon = input("Are you proficient in this weapon? (Y/N): ").lower()
                if prof_weapon == "y":
                    roll = random.randint(1, 20)
                    check = roll + attack_mod.get(attack_mod_raw) + DnD_Attributes.CharMainStats.prof_bonus
                    print(f"Your attack is: ", check)
                    hit_or_not = input("Does this hit (Y/N): ").lower()
                    if hit_or_not == "y":
                        dice = DnD_Weapons_Armor.SimpleMartialWeapons.simple_martial_weapons_damage.get(attack_weapon)
                        split_dice = dice.split('d')
                        dice_num = split_dice[0]
                        dice_damage = split_dice[1]
                        sum_roll = 0
                        for i in range(int(dice_num)):
                            roll = random.randint(1, int(dice_damage))
                            sum_roll = sum_roll + roll
                        overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                        print("Overall Total: ", overall_sum_roll)
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw) + DnD_Attributes.CharMainStats.prof_bonus
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleMartialWeapons.simple_martial_weapons_damage.get(
                                        attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                                break
                    if hit_or_not == "n":
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw) + DnD_Attributes.CharMainStats.prof_bonus
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleMartialWeapons.simple_martial_weapons_damage.get(
                                        attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                                break
                if prof_weapon == "n":
                    roll = random.randint(1, 20)
                    check = roll + attack_mod.get(attack_mod_raw)
                    print(f"Your attack is: ", check)
                    hit_or_not = input("Does this hit (Y/N): ").lower()
                    if hit_or_not == "y":
                        dice = DnD_Weapons_Armor.SimpleMartialWeapons.simple_martial_weapons_damage.get(attack_weapon)
                        split_dice = dice.split('d')
                        dice_num = split_dice[0]
                        dice_damage = split_dice[1]
                        sum_roll = 0
                        for i in range(int(dice_num)):
                            roll = random.randint(1, int(dice_damage))
                            sum_roll = sum_roll + roll
                        overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                        print("Overall Total: ", overall_sum_roll)
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw)
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleMartialWeapons.simple_martial_weapons_damage.get(
                                        attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                            break
                    if hit_or_not == "n":
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw)
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleMartialWeapons.simple_martial_weapons_damage.get(
                                        attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                            break
                break
        if attack_weapon_input == "simple martial ranged weapons":
            while True:
                attack_weapon = input(f"""Please choose from the following weapons: 
                                            {dnd_simple_range_martial_weapon_list} or Back: """).lower()
                if attack_weapon == "back":
                    attack()
                else:
                    attack_mod_raw = input(f"""Which modifier would you like to attribute to this attack:
                                        {dnd_modifiers_raw}: """).lower()
                prof_weapon = input("Are you proficient in this weapon? (Y/N): ").lower()
                if prof_weapon == "y":
                    roll = random.randint(1, 20)
                    check = roll + attack_mod.get(attack_mod_raw) + DnD_Attributes.CharMainStats.prof_bonus
                    print(f"Your attack is: ", check)
                    hit_or_not = input("Does this hit (Y/N): ").lower()
                    if hit_or_not == "y":
                        dice = DnD_Weapons_Armor.SimpleMartialRangedWeapons.martial_ranged_weapons_damage.get(
                            attack_weapon)
                        split_dice = dice.split('d')
                        dice_num = split_dice[0]
                        dice_damage = split_dice[1]
                        sum_roll = 0
                        for i in range(int(dice_num)):
                            roll = random.randint(1, int(dice_damage))
                            sum_roll = sum_roll + roll
                        overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                        print("Overall Total: ", overall_sum_roll)
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw) + DnD_Attributes.CharMainStats.prof_bonus
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleMartialRangedWeapons.martial_ranged_weapons_damage. \
                                        get(attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                                break
                    if hit_or_not == "n":
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw) + DnD_Attributes.CharMainStats.prof_bonus
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleMartialRangedWeapons.martial_ranged_weapons_damage. \
                                        get(attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                                break
                if prof_weapon == "n":
                    roll = random.randint(1, 20)
                    check = roll + attack_mod.get(attack_mod_raw)
                    print(f"Your attack is: ", check)
                    hit_or_not = input("Does this hit (Y/N): ").lower()
                    if hit_or_not == "y":
                        dice = DnD_Weapons_Armor.SimpleMartialRangedWeapons.martial_ranged_weapons_damage.get(
                            attack_weapon)
                        split_dice = dice.split('d')
                        dice_num = split_dice[0]
                        dice_damage = split_dice[1]
                        sum_roll = 0
                        for i in range(int(dice_num)):
                            roll = random.randint(1, int(dice_damage))
                            sum_roll = sum_roll + roll
                        overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                        print("Overall Total: ", overall_sum_roll)
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw)
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleMartialRangedWeapons.martial_ranged_weapons_damage.\
                                        get(attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                            break
                    if hit_or_not == "n":
                        while True:
                            another_attack = input("Would you like to make another attack with the 'same' weapon, "
                                                   "'different' weapon, or 'quit'? ").lower()
                            if another_attack == "same":
                                roll = random.randint(1, 20)
                                check = roll + attack_mod.get(attack_mod_raw)
                                print(f"Your attack is: ", check)
                                hit_or_not = input("Does this hit (Y/N): ").lower()
                                if hit_or_not == "y":
                                    dice = DnD_Weapons_Armor.SimpleMartialRangedWeapons.martial_ranged_weapons_damage.\
                                        get(attack_weapon)
                                    split_dice = dice.split('d')
                                    dice_num = split_dice[0]
                                    dice_damage = split_dice[1]
                                    sum_roll = 0
                                    for i in range(int(dice_num)):
                                        roll = random.randint(1, int(dice_damage))
                                        sum_roll = sum_roll + roll
                                    overall_sum_roll = sum_roll + attack_mod.get(attack_mod_raw)
                                    print("Overall Total: ", overall_sum_roll)
                            elif another_attack == "different":
                                attack()
                            else:
                                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                                if go_back_main_menu == "y":
                                    user_choice()
                                elif go_back_main_menu == "n":
                                    print("Good Luck!")
                            break
                break
        break


def spell_attack():
    roll = random.randint(1, 20)
    check = roll + DnD_Attributes.CharMainStats.spell_attack
    print(f"Your Spell Attack is: ", check)
    hit_or_not = input("Does this hit (Y/N): ").lower()
    if hit_or_not == "y":
        dice = input("Enter dice: ")
        split_dice = dice.split('d')
        dice_num = split_dice[0]
        dice_damage = split_dice[1]
        sum_roll = 0
        for i in range(int(dice_num)):
            roll = random.randint(1, int(dice_damage))
            sum_roll = sum_roll + roll
        print("Overall Total: ", sum_roll)
        while True:
            another_attack = input("Would you like to roll another Spell Attack, or additional Dice or No? ").lower()
            if another_attack == "attack":
                roll = random.randint(1, 20)
                check = roll + DnD_Attributes.CharMainStats.spell_attack
                print(f"Your Spell Attack is: ", check)
                hit_or_not = input("Does this hit (Y/N): ").lower()
                if hit_or_not == "y":
                    dice = input("Enter dice: ")
                    split_dice = dice.split('d')
                    dice_num = split_dice[0]
                    dice_damage = split_dice[1]
                    sum_roll = 0
                    for i in range(int(dice_num)):
                        roll = random.randint(1, int(dice_damage))
                        sum_roll = sum_roll + roll
                    print("Overall Total: ", sum_roll)
            elif another_attack == "dice":
                dice = input("Enter dice: ")
                split_dice = dice.split('d')
                dice_num = split_dice[0]
                dice_damage = split_dice[1]
                sum_roll = 0
                for i in range(int(dice_num)):
                    roll = random.randint(1, int(dice_damage))
                    sum_roll = sum_roll + roll
                print("Overall Total: ", sum_roll)
            else:
                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                if go_back_main_menu == "y":
                    user_choice()
                elif go_back_main_menu == "n":
                    print("Good Luck!")
                break
    elif hit_or_not == "n":
        while True:
            another_attack = input("Would you like to roll another Spell Attack, or additional Dice or No? ").lower()
            if another_attack == "attack":
                roll = random.randint(1, 20)
                check = roll + DnD_Attributes.CharMainStats.spell_attack
                print(f"Your Spell Attack is: ", check)
                hit_or_not = input("Does this hit (Y/N): ").lower()
                if hit_or_not == "y":
                    dice = input("Enter dice: ")
                    split_dice = dice.split('d')
                    dice_num = split_dice[0]
                    dice_damage = split_dice[1]
                    sum_roll = 0
                    for i in range(int(dice_num)):
                        roll = random.randint(1, int(dice_damage))
                        sum_roll = sum_roll + roll
                    print("Overall Total: ", sum_roll)
            elif another_attack == "dice":
                dice = input("Enter dice: ")
                split_dice = dice.split('d')
                dice_num = split_dice[0]
                dice_damage = split_dice[1]
                sum_roll = 0
                for i in range(int(dice_num)):
                    roll = random.randint(1, int(dice_damage))
                    sum_roll = sum_roll + roll
                print("Overall Total: ", sum_roll)
            else:
                go_back_main_menu = input("Would you like to go to the main menu (Y/N)? ").lower()
                if go_back_main_menu == "y":
                    user_choice()
                elif go_back_main_menu == "n":
                    print("Good Luck!")
                break


user_choice()
