import Ability_Modifier_Calc

dnd_dice = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']


class CharAbilityRaw:
    str_ability = 9
    dex_ability = 14
    con_ability = 17
    int_ability = 20
    wis_ability = 11
    cha_ability = 11


class CharModifier:
    str_modifier = Ability_Modifier_Calc.ability_score(CharAbilityRaw.str_ability)
    dex_modifier = Ability_Modifier_Calc.ability_score(CharAbilityRaw.dex_ability)
    con_modifier = Ability_Modifier_Calc.ability_score(CharAbilityRaw.con_ability)
    int_modifier = Ability_Modifier_Calc.ability_score(CharAbilityRaw.int_ability)
    wis_modifier = Ability_Modifier_Calc.ability_score(CharAbilityRaw.wis_ability)
    cha_modifier = Ability_Modifier_Calc.ability_score(CharAbilityRaw.cha_ability)


class CharMainStats:
    hit_dice = 'd8'
    hit_points = 47
    character_level = 5
    prof_bonus = 3
    passive_perception = 10 + CharModifier.wis_modifier
    spell_attack = 9
    spell_dc = 17
    attack_modifier = CharModifier.int_modifier


class CharSaving:
    str_saving = CharModifier.str_modifier
    dex_saving = CharModifier.dex_modifier
    con_saving = CharModifier.con_modifier + CharMainStats.prof_bonus
    int_saving = CharModifier.int_modifier + CharMainStats.prof_bonus
    wis_saving = CharModifier.wis_modifier
    cha_saving = CharModifier.cha_modifier


class CharSkills:
    acrobatics = CharModifier.dex_modifier
    animal_handling = CharModifier.dex_modifier
    arcana = CharModifier.int_modifier + CharMainStats.prof_bonus
    athletics = CharModifier.str_modifier
    deception = CharModifier.cha_modifier
    history = CharModifier.int_modifier
    insight = CharModifier.wis_modifier + CharMainStats.prof_bonus
    intimidation = CharModifier.cha_modifier
    investigation = CharModifier.int_modifier + CharMainStats.prof_bonus
    medicine = CharModifier.wis_modifier
    nature = CharModifier.int_modifier
    perception = CharModifier.wis_modifier
    performance = CharModifier.cha_modifier
    persuasion = CharModifier.cha_modifier + CharMainStats.prof_bonus
    religion = CharModifier.int_modifier
    sleight_of_hand = CharModifier.dex_modifier
    survival = CharModifier.wis_modifier