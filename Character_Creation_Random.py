"""Specifically made to randomize a Character from scratch by doing the following:
    - Will choose a Race at random - Done
    - Will choose a Class at Random - Done
        - Including Sub-Class options if applicable - Done
    - Will roll Stats for all 6 stats - Done
        - Will try to organize it with how the Class is setup - Done
        - Highest number associated with Primary Stat/Secondary Stat/etc. - Done
    - Might include random Name generator - In Progress
    - Might include random Background - Done
    - Might suggest Feats that would work well with the Race/Class that is picked - Done

    - Order of events:
        - Choose Race and Class / Sub-Class
        - Get the RAW dict for Class association
        - Run Random Stat generator
        - Input into RAW dict
        - Add additional modifiers from Race / Sub-Race
            - Add in additional clause statements for Half-Elf / Variant Human
        - Print out results
            - Race / Class / Sub-Class / Starting Stats
"""

import random
import Character_Creation_Data
import collections

race_check = ""
sub_race_check = ""
dnd_class_check = ""
dnd_sub_class_check = ""
null_stat_dict = {}


def raw_race():
    global race_check
    global sub_race_check

    race_check = random.choice(list(Character_Creation_Data.RawRace.races))
    print(f"Race:", race_check)

    if race_check in Character_Creation_Data.SubRawRace.sub_raw_race_dict.keys():
        sub_race_check = random.choice(list(Character_Creation_Data.SubRawRace.sub_raw_race_dict.get(race_check, 0)))
        print(f"Sub Race:", sub_race_check)


def raw_class():
    global dnd_class_check
    global dnd_sub_class_check

    dnd_class_check = random.choice(list(Character_Creation_Data.RawClass.dnd_classes))
    print(f"DnD Class:", dnd_class_check)

    if dnd_class_check in Character_Creation_Data.RawClass.dnd_classes:
        dnd_sub_class_check = random.choice(
            list(Character_Creation_Data.RawSubClass.raw_sub_class_dict.get(dnd_class_check,
                                                                            0)))
        print(f"DnD Sub Class:", dnd_sub_class_check)


def raw_stat_roll():
    global null_stat_dict

    stat_rolls_stored = []
    for i in range(6):
        stat_rolls = []
        for j in range(4):
            num = random.randint(1, 6)
            stat_rolls.append(num)
        del stat_rolls[stat_rolls.index(min(stat_rolls))]
        stat_rolls_stored.append(sum(stat_rolls))
        stat_rolls_stored.sort(reverse=True)
    # print(f"Stat Rolls Stored:", stat_rolls_stored)

    null_stat_dict = Character_Creation_Data.RawSubClassStats.raw_sub_class_stats_dict.get(dnd_class_check, 0)

    for i, stat in zip(null_stat_dict, stat_rolls_stored):
        null_stat_dict[i] += stat
    # print(f"Null Stat Dict:", null_stat_dict)


def added_stats():
    a_counter = collections.Counter(null_stat_dict)
    b_counter = collections.Counter(Character_Creation_Data.RawRace.race_stats_dict.get(race_check, 0))

    if Character_Creation_Data.SubRawRace.sub_raw_race_stat_dict.get(sub_race_check, 0) == 0:
        c_counter = 0
    else:
        c_counter = collections.Counter(Character_Creation_Data.SubRawRace.sub_raw_race_stat_dict.get(
                                                                                        sub_race_check, 0))

    if race_check in Character_Creation_Data.RawRace.race_add_stat:
        print("")
        stat_increases = input("Which stat would you like to increase? str / dex / con / int / wis / cha: ").lower()
        b_counter[stat_increases] += 1
        stat_increase_2 = input("Which second stat would you like to increase? (Please choose a different stat then "
                                "the First) str / dex / con / int / wis / cha: ").lower()
        if stat_increase_2 == stat_increases:
            print("Please choose a different stat than the first")
            stat_increase_2 = input("Which second stat would you like to increase? (Please choose a different stat "
                                    "then the first) str / dex / con / int / wis / cha: ").lower()
            b_counter[stat_increase_2] += 1
        else:
            b_counter[stat_increase_2] += 1

    if c_counter == 0:
        add_dict = a_counter + b_counter
        final_dict = dict(add_dict)
        print(f"Final Stats:", final_dict)
    else:
        add_dict = a_counter + b_counter + c_counter
        final_dict = dict(add_dict)
        print(f"Final Stats:", final_dict)


def background_random():
    background_check = random.choice(list(Character_Creation_Data.RawBackgrounds.raw_background_list))
    joined_string = "\n".join(Character_Creation_Data.RawBackgrounds.raw_background_dict.get(background_check, 0))
    print(f"Background:", background_check)
    print(f"Background Info -\n{joined_string}")


def feat_random():
    feat_check = random.choice(list(Character_Creation_Data.RawFeat.raw_feats_list))
    joined_string = "\n".join(Character_Creation_Data.RawFeat.raw_feats.get(feat_check, 0))
    print(f"Feat:", feat_check)
    print(f"Feat Info -\n{joined_string}")


def name_random():
    if race_check in Character_Creation_Data.RawName.male_raw_first_names.keys():
        first_name_random = random.choice(list(Character_Creation_Data.RawName.male_raw_first_names.get(race_check, 0)))
        print(f"Male First Name:", first_name_random)

    if race_check in Character_Creation_Data.RawName.female_raw_first_names.keys():
        female_first_name = random.choice(list(Character_Creation_Data.RawName.female_raw_first_names.get(race_check, 0)))
        print(f"Female First Name:", female_first_name)

    if race_check in Character_Creation_Data.RawName.raw_last_names.keys():
        last_name = random.choice(list(Character_Creation_Data.RawName.raw_last_names.get(race_check, 0)))
        print(f"Last Name:", last_name)


def final_results():
    raw_race()
    raw_class()
    raw_stat_roll()
    added_stats()
    print()
    background_random()
    print()
    feat_random()


raw_race()
name_random()
