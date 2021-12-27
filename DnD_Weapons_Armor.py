simple_weapons_name = ["club", "dagger", "great club", "hand axe", "javelin", "light hammer", "mace", "quarterstaff"
                       , "sickle", "spear"]
simple_ranged_weapon_name = ["crossbow, light", "dart", "shortbow", "sling"]
simple_martial_weapon_name = ["battleaxe", "flail", "glaive", "greataxe", "greatsword", "halberd", "lance", "longsword",
                              "maul", "morning start", "pike", "rapier", "scimitar", "shortsword", "trident",
                              "war pick", "warhammer", "whip"]
simple_martial_ranged_weapon_name = ["blowgun", "crossbow, hand", "crossbow, heavy", "longbow"]


class SimpleWeapons:
    simple_weapon_damage = {"club": '1d4', "dagger": '1d4', "great club": '1d8', "hand axe": '1d6', "javelin": '1d6',
                            "light hammer": '1d4', "mace": '1d6', "quarterstaff": '1d6', "sickle": '1d4',
                            "spear": '1d6'}
    simple_weapon_cost = {"club": '1 Sp', "dagger": '2 Gp', "great club": '2 Sp', "hand axe": '5 Gp', "javelin": '5 Sp',
                          "light hammer": '2 Gp', "mace": '5 Gp', "quarterstaff": '2 Sp', "sickle": '1 Gp',
                          "spear": '1 Gp'}
    simple_weapons_properties = {"club": 'Light', "dagger": 'Finesse, Light, Thrown (20/60)', "great club": 'Two-Handed'
        , "hand axe": 'Light, Thrown (20/60)', "javelin": 'Thrown (30/120)',
                                 "light hammer": 'Light, Thrown (20/60)', "mace": '-', "quarterstaff": 'Versatile (1d8)'
        , "sickle": 'Light', "spear": 'Thrown (20/60), Versatile (1d8)'}


class SimpleRangedWeapons:
    simple_ranged_weapon_damage = {"crossbow, light": '1d8', "dart": '1d4', "shortbow": '1d6', "sling": '1d4'}
    simple_ranged_weapon_cost = {"crossbow, light": '25 Gp', "dart": '5 Cp', "shortbow": '25 Gp', "sling": '1 Sp'}
    simple_ranged_weapon_properties = {"crossbow, light": 'Ammunition, Range (80/320), Loading, Two-Handed',
                                       "dart": 'Finesse, Thrown (20/60)',
                                       "shortbow": 'Ammunition, Range (80/320), Two-Handed',
                                       "sling": 'Ammunition, Range (30/120)'}


class SimpleMartialWeapons:
    simple_martial_weapons_damage = {"battleaxe": '1d8', "flail": '1d8', "glaive": '1d10', "greataxe": '1d12',
                                     "greatsword": '2d6', "halberd": '1d10', "lance": '1d12', "longsword": '1d8',
                                     "maul": '2d6', "morning star": '1d8', "pike": '1d10', "rapier": '1d8',
                                     "scimitar": '1d6',
                                     "shortsword": '1d6', "trident": '1d6', "war pick": '1d8', "warhammer": '1d8',
                                     "whip": '1d4'}
    simple_martial_weapons_cost = {"battleaxe": '10 Gp', "flail": '10 Gp', "glaive": '20 Gp', "greataxe": '50 Gp',
                                   "greatsword": '50 Gp', "halberd": '20 Gp', "lance": '10 Gp', "longsword": '15 Gp',
                                   "maul": '10 Gp', "morning star": '15 Gp', "pike": '5 Gp', "rapier": '25 Gp',
                                   "scimitar": '25 Gp', "shortsword": '10 Gp', "trident": '5 Gp', "war pick": '5 Gp',
                                   "warhammer": '15 Gp', "whip": '2 Gp'}
    simple_martial_weapons_properties = {"battleaxe": 'Versatile (1d10)', "flail": '-',
                                         "glaive": 'Heavy, Reach, Two-Handed', "greataxe": 'Heavy, Two-Handed',
                                         "greatsword": 'Heavy, Two-Handed', "halberd": 'Heavy, Reach, Two-Handed',
                                         "lance": 'Reach, Special', "longsword": 'Versatile (1d10)',
                                         "maul": 'Heavy, Two-Handed', "morning star": '-',
                                         "pike": 'Heavy, Reach, Two-Handed', "rapier": 'Finesse',
                                         "scimitar": 'Finesse, Light', "shortsword": 'Finesse, Light',
                                         "trident": 'Thrown (20/60), Versatile (1d8)', "war pick": '-',
                                         "warhammer": 'Versatile (1d10)', "whip": 'Finesse, Reach'}


class SimpleMartialRangedWeapons:
    martial_ranged_weapons_damage = {"blowgun": '1d1', "crossbow, hand": '1d6', "crossbow, heavy": '1d10',
                                     "longbow": '1d8'}
    martial_ranged_weapons_cost = {"blowgun": '10 Gp', "crossbow, hand": '75 Gp', "crossbow, heavy": '50 Gp',
                                   "longbow": '50 Gp'}
    martial_ranged_weapons_properties = {"blowgun": 'Ammunition, Range (25/100), Loading',
                                         "crossbow, hand": 'Ammunition, Range (30/120), Light, Loading',
                                         "crossbow, heavy": 'Ammunition, Range (100/400), Heavy, Loading, Two-Handed',
                                         "longbow": 'Ammunition, Range (150/600), Heavy, Two-Handed'}


class LightArmor:
    light_armor_ac = {"padded": '11', "leather": '11',
                      "studded leather": '12'}
    light_armor_dex = {"padded": 'dexterity_modifier', "leather": 'dexterity_modifier',
                       "studded leather": 'dexterity_modifier'}
    light_armor_cost = {"padded": '5 Gp', "leather": '10 Gp', "studded leather": '45 Gp'}
    light_armor_stealth = {"padded": 'Disadvantage', "leather": '-', "studded leather": '-'}


class MediumArmor:
    medium_armor_ac = {"hide": '12', "chain shirt": '13', "scale mail": '14', "spiked armor": '14',
                       "breastplate": '14', "halfplate": '15'}
    medium_armor_dex = {"hide": 'dexterity_modifier (max 2)', "chain shirt": 'dexterity_modifier (max 2)',
                        "scale mail": 'dexterity_modifier (max 2)',
                        "spiked armor": 'dexterity_modifier (max 2)',
                        "breastplate": 'dexterity_modifier (max 2)',
                        "halfplate": 'dexterity_modifier (max 2)'}
    medium_armor_cost = {"hide": '10 Gp', "chain shirt": '50 Gp', "scale mail": '50 Gp', "spiked armor": '75 Gp',
                         "breastplate": '400 Gp', "halfplate": '750 Gp'}
    medium_armor_stealth = {"hide": '-', "chain shirt": '-', "scale mail": 'Disadvantage',
                            "spiked armor": 'Disadvantage', "breastplate": '-', "halfplate": 'Disadvantage'}


class HeavyArmor:
    heavy_armor_ac = {"ring mail": '14', "chain mail": '16', "splint": '17', "plate": '18'}
    heavy_armor_cost = {"ring mail": '30 Gp', "chain mail": '75 Gp', "splint": '200 Gp', "plate": '1500 Gp'}
    heavy_armor_stealth = {"ring mail": 'Disadvantage', "chain mail": 'Disadvantage', "splint": 'Disadvantage',
                           "plate": 'Disadvantage'}
    heavy_armor_strength = {"ring mail": '-', "chain mail": 'Str 13', "splint": 'Str 15', "plate": 'Str 15'}


class Shield:
    shield_ac = {"shield": '2'}
    shield_cost = {"shield": '10 Gp'}


class DonDoffTime:
    armor_don = {"light armor": '1 minute', "medium armor": '5 minutes', "heavy armor": '10 minutes',
                 "shield": '1 action'}
    armor_doff = {"light armor": '1 minute', "medium armor": '5 minutes', "heavy armor": '5 minutes',
                  "shield": '1 action'}
