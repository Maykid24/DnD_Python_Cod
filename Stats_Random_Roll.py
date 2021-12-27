import random

"""New Character stats rolls:
    Automatically roll 4d6 dice rolls 6 times and drop the lowest dice roll each time
    this is specifically for new character creation without the need rolling actual dice"""


def ability_stat_roll():
    stat_rolls_stored = []
    for i in range(6):
        stat_rolls = []
        for j in range(4):
            num = random.randint(1, 6)
            stat_rolls.append(num)
        del stat_rolls[stat_rolls.index(min(stat_rolls))]
        stat_rolls_stored.append(sum(stat_rolls))
        stat_rolls_stored.sort(reverse=True)
    print(stat_rolls_stored)

    null_stat_dict = {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 0}

    for i, stat in zip(null_stat_dict, stat_rolls_stored):
        null_stat_dict[i] += stat
    print(null_stat_dict)


ability_stat_roll()

# Do I want to add in race attributes as well?
# Would be a combination of stat increase along with ranking system of all 6 stat criteria
# Would need subclasses and classes of each individual race
# Could even go one step further and get Feats that have stat increase as well
# This however would be difficult if the user is able to choose which stat to increase
# Would require additional input from the user

