class RawRace:
    races = ["Dwarf", "Elf", "Halfling", "Human", "Gnome", "Half-Elf", "Half-Orc",
             "Tiefling", "Aasimar", "Forbolg", "Goliath", "Kenku", "Lizardfolk",
             "Tabaxi", "Triton", "Goblin", "Variant Human"]
    race_add_stat = ["Half-Elf", "Variant Human"]

    race_stats_dict = {
        "Dwarf": {"str": 0, "dex": 0, "con": 2, "int": 0, "wis": 0, "cha": 0},
        "Elf": {"str": 0, "dex": 2, "con": 0, "int": 0, "wis": 0, "cha": 0},
        "Halfling": {"str": 0, "dex": 2, "con": 0, "int": 0, "wis": 0, "cha": 0},
        "Human": {"str": 1, "dex": 1, "con": 1, "int": 1, "wis": 1, "cha": 1},
        "Gnome": {"str": 0, "dex": 0, "con": 0, "int": 2, "wis": 0, "cha": 0},
        "Half-Elf": {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 2},
        "Half-Orc": {"str": 2, "dex": 0, "con": 1, "int": 0, "wis": 0, "cha": 0},
        "Tiefling": {"str": 0, "dex": 0, "con": 0, "int": 1, "wis": 0, "cha": 2},
        "Aasimar": {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 2},
        "Forbolg": {"str": 1, "dex": 0, "con": 0, "int": 0, "wis": 2, "cha": 0},
        "Goliath": {"str": 2, "dex": 0, "con": 1, "int": 0, "wis": 0, "cha": 0},
        "Kenku": {"str": 0, "dex": 2, "con": 0, "int": 0, "wis": 1, "cha": 0},
        "Lizardfolk": {"str": 0, "dex": 0, "con": 2, "int": 0, "wis": 1, "cha": 0},
        "Tabaxi": {"str": 0, "dex": 2, "con": 0, "int": 0, "wis": 0, "cha": 1},
        "Triton": {"str": 1, "dex": 0, "con": 1, "int": 0, "wis": 0, "cha": 1},
        "Goblin": {"str": 0, "dex": 2, "con": 1, "int": 0, "wis": 0, "cha": 0},
        "Variant Human": {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 0}
    }


class SubRawRace:
    dnd_sub_raw_race_list = ["Dwarf", "Elf", "Halfling", "Gnome", "Aasimar"]

    sub_raw_race_dict = {
        "Dwarf": ["Hill Dwarf", "Mountain Dwarf"],
        "Elf": ["Eladrin", "High Elf", "Wood Elf", "Drow"],
        "Halfling": ["Lightfoot Halfling", "Stout Halfling"],
        "Gnome": ["Deep Gnome", "Rock Gnome"],
        "Aasimar": ["Protector Aasimar", "Scourge Aasimar", "Fallen Aasimar"]}

    sub_raw_race_stat_dict = {
        "Hill Dwarf": {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 1, "cha": 0},
        "Mountain Dwarf": {"str": 2, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 0},
        "Eladrin": {"str": 0, "dex": 0, "con": 0, "int": 1, "wis": 0, "cha": 0},
        "High Elf": {"str": 0, "dex": 0, "con": 0, "int": 1, "wis": 0, "cha": 0},
        "Wood Elf": {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 1, "cha": 0},
        "Drow": {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 1},
        "Lightfoot Halfling": {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 1},
        "Stout Halfling": {"str": 0, "dex": 0, "con": 1, "int": 0, "wis": 0, "cha": 0},
    }


class RawClass:
    dnd_classes = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
                   "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]


class RawSubClass:
    raw_sub_class_dict = {
        "Artificer": ["Alchemist", "Armorer", "Artillerist", "Battle Smith"],
        "Barbarian": ["Path of the Beserker", "Path of the Totem Warrior", "Path of the Ancestral Guardian",
                      "Path of the Storm Herald", "Path of the Zealot", "Path of the Beast",
                      "Path of Wild Magic"],
        "Bard": ["College of Lore", "College of Valor", "College of Fochlucan", "College of New Olamn",
                 "College of the Herald", "College of Glamour", "College of Swords", "College of Whispers",
                 "College of Creation", "College of Eloquence"],
        "Cleric": ["Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Tempest Domain",
                   "Trickery Domain", "War Domain", "Arcana Domain", "Forge Domain", "Grave Domain", "Order Domain",
                   "Peace Domain", "Twilight Domain"],
        "Druid": ["Circle of the Land", "Circle of the Moon", "Circle of Dreams", "Circle of the Shepherd",
                  "Circle of Spores", "Circle of Stars", "Circle of Wildfire"],
        "Fighter": ["Champion", "Battle Master", "Eldritch Knight", "Arcane Archer", "Cavalier", "Samurai",
                    "Psi Warrior", "Rune Knight"],
        "Monk": ["Way of the Open Hand", "Way of the Shadow", "Way of the Four Elements", "Way of the Long Death",
                 "Way of the Sun Soul", "Way of the Drunken Master", "Way of the Kensei", "Way of the Sun Soul",
                 "Way of Mercy", "Way of the Astral Self"],
        "Paladin": ["Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance", "Oath of the Crown",
                    "Oath of Conquest", "Oath of Redemption", "Oath of Glory", "Oath of the Watchers"],
        "Ranger": ["Hunter", "Beast Master", "Gloom Stalker", "Horizon Walker", "Monster Slayer", "Fey Wanderer",
                   "Swarmkeeper"],
        "Rogue": ["Thief", "Assassin", "Arcane Trickster", "Mastermind", "Swashbuckler", "Inquisitive", "Scout",
                  "Phantom", "Soulknife"],
        "Sorcerer": ["Draconic Bloodline", "Wild Magic", "Storm Sorcery", "Divine Soul", "Shadow Magic",
                     "Aberrant Mind", "Clockwork Soul"],
        "Warlock": ["The Fiend", "The Great Old One", "The Undying", "The Celestial", "The Hexblade", "The Fathomless",
                    "The Genie"],
        "Wizard": ["School of Abjuration", "School of Conjuration", "School of Divination", "School of Enchantment",
                   "School of Evocation", "School of Necromancy", "School of Transmutation", "Bladesinging",
                   "War Magic", "Order of Scribes"]
    }


class RawSubClassStats:
    raw_sub_class_stats_dict = {
        "Artificer": {"int": 0, "con": 0, "dex": 0, "wis": 0, "cha": 0, "str": 0},
        "Barbarian": {"str": 0, "con": 0, "dex": 0, "wis": 0, "int": 0, "cha": 0},
        "Bard": {"cha": 0, "dex": 0, "con": 0, "wis": 0, "int": 0, "str": 0},
        "Cleric": {"wis": 0, "con": 0, "str": 0, "int": 0, "dex": 0, "cha": 0},
        "Druid": {"wis": 0, "con": 0, "str": 0, "int": 0, "dex": 0, "cha": 0},
        "Fighter": {"str": 0, "con": 0, "dex": 0, "wis": 0, "int": 0, "cha": 0},
        "Fighter_Long": {"dex": 0, "con": 0, "str": 0, "wis": 0, "int": 0, "cha": 0},
        "Monk": {"dex": 0, "wis": 0, "con": 0, "str": 0, "int": 0, "cha": 0},
        "Paladin": {"str": 0, "cha": 0, "con": 0, "dex": 0, "wis": 0, "int": 0},
        "Ranger": {"dex": 0, "wis": 0, "con": 0, "str": 0, "int": 0, "cha": 0},
        "Rogue": {"dex": 0, "int": 0, "cha": 0, "con": 0, "wis": 0, "str": 0},
        "Sorcerer": {"cha": 0, "con": 0, "int": 0, "dex": 0, "wis": 0, "str": 0},
        "Warlock": {"cha": 0, "con": 0, "int": 0, "dex": 0, "wis": 0, "str": 0},
        "Wizard": {"int": 0, "con": 0, "cha": 0, "dex": 0, "wis": 0, "str": 0}
    }


class RawBackgrounds:
    raw_background_dict = {
        "Acolyte": [
            "Skill Proficiencies: Insight, Religion",
            "Tool Proficiencies: None",
            "Languages: Two of your choice",
            "Equipment: A holy symbol (a gift to you when you entered the priesthood), a prayer book or prayer wheel, "
            "5 sticks of incense, vestments, a set of common clothes, and a pouch containing 15gp"
        ],
        "Anthropologist": [
            "Skill Proficiencies: Insight, Religion",
            "Tool Proficiencies: None",
            "Languages: Two of your choice",
            "Equipment: A leather-bound diary, a bottle of ink, an ink pen, a set of traveler's clothes, "
            "one trinket of special significance, and a pouch containing 10gp"
        ],
        "Archaeologist": [
            "Skill Proficiencies: History, Survival",
            "Tool Proficiencies: Cartographer's tools or navigator's tools",
            "Languages: One of your choice",
            "Equipment: A wooden case containing a map to a ruin or dungeon, a bullseye lantern, a miner's pick, a set "
            "of traveler's clothes, a shovel, a two-person tent, a trinket recovered from a dig site, and a pouch "
            "containing 25gp"
        ],
        "Athlete": [
            "Skill Proficiencies: Acrobatics, Athletics",
            "Languages: One of your choice",
            "Tool Proficiencies: Vehicles (Land)",
            "Equipment: A bronze discus or leather ball, a lucky charm or past trophy, a set of traveler's clothes, "
            "and a pouch containing 10 gp"
        ],
        "Charlatan": [
            "Skill Proficiencies: Deception, Sleight of Hand",
            "Tool Proficiencies: Disguise kit, forgery kit",
            "Languages: None",
            "Equipment: A set of fine clothes, a disguise kit, tools of the con of your choice (ten stoppered bottles "
            "filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an "
            "imaginary duke), and a pouch containing 15gp"
        ],
        "City Watch": [
            "Skill Proficiencies: Athletics, Insight",
            "Tool Proficiencies: None",
            "Languages: Two of your choice",
            "Equipment: A uniform in the style of your unit and indicative of your rank, a horn with which to summon "
            "help, a set of manacles, and a pouch containing 10gp"
        ],
        "Clan Crafter": [
            "Skill Proficiencies: History, Insight",
            "Tool Proficiencies: One type of artisan's tools",
            "Languages: Dwarvish or one other of your choice if you already speak Dwarvish",
            "Equipment: A set of artisan's tools with which you are proficient, a maker's mark chisel used to "
            "mark your handiwork with the symbol of the clan of crafters you learned your skill from, a set of "
            "traveler's clothes, and a pouch containing 5gp and a gem worth 10gp"
        ],
        "Cloistered Scholar": [
            "Skill Proficiencies: History, plus your choice of one from among Arcana, Nature, and Religion",
            "Tool Proficiencies: None",
            "Languages: Two of your choice",
            "Equipment: The scholar's robes of your cloister, a writing kit (small pouch with a quill, a bottle of "
            "ink, folded parchment, and a small penknife), a borrowed book on the subject of your current study, and a "
            "pouch containing 10gp"
        ],
        "Courtier": [
            "Skill Proficiencies: Insight, Persuasion",
            "Tool Proficiencies: None",
            "Languages: Two of your choice",
            "Equipment: A set of fine clothes and a pouch containing 5gp"
        ],
        "Criminal": [
            "Skill Proficiencies: Deception, Stealth",
            "Tool Proficiencies: One type of gaming set, thieves' tools",
            "Languages: None",
            "Equipment: A crowbar, a set of dark common clothes including a hood, and a pouch containing 15gp"
        ],
        "Entertainer": [
            "Skill Proficiencies: Acrobatics, Performance",
            "Tool Proficiencies: Disguise kit, one type of musical instrument",
            "Languages: None",
            "Equipment: A musical instrument (one of your choice), the favor of an admirer (love letter, lock of "
            "hair, or trinket), a costume, and a pouch containing 15gp"
        ],
        "Faceless": [
            "Skill Proficiencies: Deception, Intimidation",
            "Tool Proficiencies: Disguise kit",
            "Languages: One of your choice",
            "Equipment: A disguise kit, a costume, and a pouch containing 10gp"
        ],
        "Faction Agent": [
            "Skill Proficiencies: Insight and one Intelligence, Wisdom, or Charisma skill of your choice, as "
            "appropriate to your faction",
            "Tool Proficiencies: None",
            "Languages: Two of your choice",
            "Equipment: The badge or emblem of your faction, a copy of a seminal faction text (or a code-book for a "
            "covert faction), a set of common clothes, and a pouch containing 15gp"
        ],
        "Far Traveler": [
            "Skill Proficiencies: Insight, Perception",
            "Tool Proficiencies: Any one musical instrument or gaming set of your choice, likely something native "
            "to your homeland",
            "Languages: Any one of your choice",
            "Equipment: One set of traveler's clothes, any one musical instrument or gaming set you are proficient "
            "with, poorly wrought maps from your homeland that depict where you are in Faerûn, a small piece of "
            "jewelry worth 10gp in the style of your homeland's craftsmanship, and a pouch containing 5gp"
        ],
        "Feylost": [
            "Skill Proficiencies: Deception, Survival",
            "Tool Proficiencies: One type of musical instrument",
            "Languages: One of your choice of Elvish, Gnomish, Goblin, or Sylvan.",
            "Equipment: A musical instrument (one of your choice), a set of traveler's clothes, three trinkets "
            "(each determind by rolling on the Feywild Trinkets table), and a pouch containing 8gp"
        ],
        "Fisher": [
            "Skill Proficiencies: History, Survival",
            "Languages: One of your choice",
            "Equipment: Fishing tackle, a net, a favorite fishing lure or oiled leather wading boots, a set of "
            "traveler's clothes, and a belt pouch containing 10 gp"
        ],
        "Folk Hero": [
            "Skill Proficiencies: Animal Handling, Survival",
            "Tool Proficiencies: One type of artisan's tools, vehicles (land)",
            "Languages: None",
            "Equipment: A set of artisan's tools (one of your choice), a shovel, an iron pot, a set of common "
            "clothes, and a pouch containing 10gp"
        ],
        "Gladiator": [
            "Skill Proficiencies: Acrobatics, Performance",
            "Tool Proficiencies: Disguise kit, one type of musical instrument",
            "Languages: None",
            "Equipment: A musical instrument (one of your choice), the favor of an admirer "
            "(love letter, lock of hair, or trinket), a costume, and a pouch containing 15gp"
        ],
        "Guild Artisan": [
            "Skill Proficiencies: Insight, Persuasion",
            "Tool Proficiencies: One type of artisan's tools",
            "Languages: One of your choice",
            "Equipment: A set of artisan's tools (one of your choice), a letter of introduction from your guild, "
            "a set of traveler's clothes, and a pouch containing 15gp"
        ],
        "Guild Merchant": [
            "Skill Proficiencies: Insight, Persuasion",
            "Tool Proficiencies: One type of artisan's tools",
            "Languages: One of your choice",
            "Equipment: A set of artisan's tools (one of your choice), a letter of introduction from your "
            "guild, a set of traveler's clothes, and a pouch containing 15gp"
        ],
        "Haunted One": [
            "Skill Proficiencies: Choose two of Arcana, Investigation, Religion, or Survival",
            "Tool Proficiencies: None",
            "Languages: Choose one exotic language (Abyssal, Celestial, Deep Speech, Draconic, Infernal, "
            "Primordial, Sylvan, or Undercommon)",
            "Equipment: A monster hunter’s pack, and one trinket of special significance (choose one or roll on "
            "the Gothic Trinkets table). Also gain a set of set of common clothes and 1sp."
        ],
        "Hermit": [
            "Skill Proficiencies: Medicine, Religion",
            "Tool Proficiencies: Herbalism kit",
            "Languages: One of your choice",
            "Equipment: A scroll case stuffed full of notes from your studies or prayers, a winter blanket, "
            "a set of common clothes, an herbalism kit, and 5gp"
        ],
        "House Agent": [
            "Skill Proficiencies: Investigation, Persuasion",
            "Tool Proficiencies: Two proficiencies from the House Tool Proficiencies table",
            "Languages: None",
            "Equipment: A set of fine clothes, the signet ring of your house, identification papers, and a "
            "purse containing 20gp"
        ],
        "Inheritor": [
            "Skill Proficiencies: Survival, plus one from among Arcana, History, and Religion",
            "Tool Proficiencies: Your choice of a gaming set or a musical instrument",
            "Languages: Any one of your choice",
            "Equipment: Your inheritance, a set of traveler's clothes, the tool you choose for this background’s "
            "tool proficiency, and a pouch containing 15gp"
        ],
        "Investigator": [
            "Skill Proficiencies: Investigation, Insight",
            "Tool Proficiencies: None",
            "Languages: Two of your choice",
            "Equipment: A uniform in the style of your unit and indicative of your rank, a horn with which to summon "
            "help, a set of manacles, and a pouch containing 10gp"
        ],
        "Knight": [
            "Skill Proficiencies: History, Persuasion",
            "Tool Proficiencies: One type of gaming set",
            "Languages: One of your choice",
            "Equipment: A set of fine clothes, a signet ring, a scroll of pedigree, and a purse containing 25gp"
        ],
        "Knight of the Order": [
            "Skill Proficiencies: Persuasion, plus one from among Arcana, History, Nature, and Religion, "
            "as appropriate for your order",
            "Tool Proficiencies: One type of gaming set or musical instrument",
            "Languages: One of your choice",
            "Equipment: A set of traveler's clothes, a signet, banner, or seal representing your place or rank in "
            "the order, and a pouch containing 10gp"
        ],
        "Marine": [
            "Skill Proficiencies: Athletics, Survival",
            "Tool Proficiencies: Vehicles (land & water)",
            "Languages: None",
            "Equipment: A dagger that belonged to a fallen comrade, a folded rag emblazoned with the symbol of "
            "your ship or company, a set of traveler's clothes, and a pouch containing 10gp"
        ],
        "Mercenary Veteran": [
            "Skill Proficiencies: Athletics, Persuasion"
            "Tool Proficiencies: One type of gaming set, vehicles (land)"
            "Languages: None"
            "Equipment: A uniform of your company (traveler's clothes in quality), an insignia of your rank, a gaming "
            "set of your choice, and a pouch containing the remainder of your last wages (10gp)"
        ],
        "Noble": [
            "Skill Proficiencies: History, Persuasion",
            "Tool Proficiencies: One type of gaming set",
            "Languages: One of your choice",
            "Equipment: A set of fine clothes, a signet ring, a scroll of pedigree, and a purse containing 25gp"
        ],
        "Outlander": [
            "Skill Proficiencies: Athletics, Survival",
            "Tool Proficiencies: One type of musical instrument",
            "Languages: One of your choice",
            "Equipment: A staff, a hunting trap, a trophy from an animal you killed, a set of traveler's clothes, "
            "and a pouch containing 10gp"
        ],
        "Pirate": [
            "Skills Proficiencies: Intimidation, Deception",
            "Tool Proficiencies: with navigators tool’s, and also with the water vehicles you will get proficiency",
            "Languages: Thieves cant language you knew and also one other language of your choice.",
            "Equipment: a flask, grappling hook and also a rapier. These equipments you have."
        ],
        "Sage": [
            "Skill Proficiencies: Arcana, History",
            "Tool Proficiencies: None",
            "Languages: Two of your choice",
            "Equipment: A bottle of ink, a quill, a small knife, a letter from a dead colleague posing a question "
            "you have not yet been able to answer, a set of common clothes, and a pouch containing 10gp"
        ],
        "Sailor": [
            "Skill Proficiencies: Athletics, Perception",
            "Tool Proficiencies: Navigator's tools, vehicles (water)",
            "Languages: None",
            "Equipment: A belaying pin (club), 50 feet of silk rope, a lucky charm such as a rabbit foot or a "
            "small stone with a hole in the center (or you may roll for a random trinket on the Trinkets table "
            "in chapter 5), a set of common clothes, and a pouch containing 10gp"
        ],
        "Shipwright": [
            "Skill Proficiencies: History, Perception",
            "Tool Proficiencies: Carpenter's tools, Vehicles (water)",
            "Equipment: A set of well-loved carpenter's tools, a blank book, 1 ounce of ink, an ink pen, "
            "a set of traveler's clothes, and a leather pouch with 10 gp"
        ],
        "Smuggler": [
            "Skill Proficiencies Athletics, Deception",
            "Tool Proficiencies Vehicles (water)",
            "Equipment A fancy leather vest or a pair of leather boots, a set of common clothes, "
            "and a leather pouch with 15 gp"
        ],
        "Soldier": [
            "Skill Proficiencies: Athletics, Intimidation",
            "Tool Proficiencies: One type of gaming set, vehicles (land)",
            "Languages: None",
            "Equipment: An insignia of rank, a trophy taken from a fallen enemy (a dagger, broken blade, "
            "or piece of a banner), a set of bone dice or a deck of cards, a set of common clothes, and "
            "a pouch containing 10gp"
        ],
        "Spy": [
            "Skill Proficiencies: Deception, Stealth",
            "Tool Proficiencies: One type of gaming set, thieves' tools",
            "Languages: None",
            "Equipment: A crowbar, a set of dark common clothes including a hood, and a pouch containing 15gp",
        ],
        "Urban Bounty Hunter": [
            "Skill Proficiencies: Choose two from among Deception, Insight, Persuasion, and Stealth",
            "Tool Proficiencies: Choose two from among one type of gaming set, one musical instrument, "
            "and thieves' tools",
            "Languages: None",
            "Equipment: A set of clothes appropriate to your duties and a pouch containing 20gp"
        ],
        "Urchin": [
            "Skill Proficiencies: Sleight of Hand, Stealth",
            "Tool Proficiencies: Disguise kit, thieves' tools",
            "Languages: None",
            "Equipment: A small knife, a map of the city you grew up in, a pet mouse, "
            "a token to remember your parents by, a set of common clothes, and a pouch containing 10gp"
        ],
        "Uthgardt Bounty Hunter": [
            "Skill Proficiencies: Athletics, Survival",
            "Tool Proficiencies: One type of musical instrument or artisan's tools",
            "Languages: One of your choice",
            "Equipment: A hunting trap, a totemic token or set of tattoos marking your loyalty to Uthgar and "
            "your tribal totem, a set of traveler's clothes, and a pouch containing 10gp"
        ],
        "Waterdhavian Noble": [
            "Skill Proficiencies: History, Persuasion",
            "Tool Proficiencies: One type of gaming set or one musical instrument",
            "Languages: One of your choice",
            "Equipment: A set of fine clothes, a signet ring or brooch, a scroll of pedigree, "
            "a skin of fine zzar or wine, and a purse containing 20gp"
        ],
        "Witchlight Hand": [
            "Skill Proficiencies: Performance, Sleight of Hand",
            "Tool Proficiencies: Disguise kit or one type of musical instrument",
            "Languages: One of your choice",
            "Equipment: A disguise kit or a musical instrument of your choice, a deck of cards, a carnival "
            "uniform or costume, one trinket (determind by rolling on the Feywild Trinkets table), and a "
            "pouch containing 8gp"
        ],
        "Black Fist Double Agent": [
            "Skill Proficiencies: Deception, Insight",
            "Tool Proficiencies: Disguise Kit, and one type of artisan’s tools or gaming set",
            "Equipment: Disguise Kit, common clothes, a Tears of Virulence emblem, a writ of free agency signed "
            "by the Lord Regent, a set of artisan’s tools or gaming set you are proficient with, and a pouch "
            "with 15gp (payment for services rendered)."
        ],
        "Dragon Casualty": [
            "Skill Proficiencies: Intimidation, Survival",
            "Tool Proficiencies: Special (see origin below)",
            "Languages: Draconic",
            "Equipment: A dagger, tattered rags, a loaf of moldy bread, a small cast-off scale belonging to "
            "Vorgansharax – the Maimed Virulence, and a pouch with 5gp of various coins (salvaged during "
            "your escape from Phlan)."
        ],
        "Iron Route Bandit": [
            "Skill Proficiencies: Stealth, Animal Handling",
            "Tool Proficiencies: One type of gaming set, vehicles (land)",
            "Equipment: A set of dark common clothes, pack saddle, burglar’s pack and a pouch containing 5gp."
        ],
        "Phlan Insurgent": [
            "Skill Proficiencies: Stealth, Survival",
            "Tool Proficiencies: One type of artisan's tools, vehicles (land)",
            "Equipment: A bag of 20 caltrops, a small trinket that connects you to the life you once had before "
            "the occupation of Phlan, a healer's kit, a set of dark common clothes that includes a cloak and hood, "
            "and a pouch containing 5gp"
        ],
        "Stojanow Prisoner": [
            "Skill Proficiencies: Deception, Perception",
            "Tool Proficiencies: One type of gaming set, thieves' tools",
            "Equipment: A small knife, a set of common clothes, a trinket from the life "
            "you stayed behind to defend, and a pouch with 10gp"
        ],
        "Ticklebelly Nomad": [
            "Skill Proficiencies: Nature, Animal Handling",
            "Tool Proficiencies: Herbalism kit",
            "Languages: Giant",
            "Equipment: Herbalism kit, a small article of jewelry that is distinct to your tribe, a hunting trap, "
            "a set of common clothes, and a pouch containing 5gp"
        ],
        "Caravan Specialist": [
            "Skill Proficiencies: Animal Handling, Survival",
            "Tool Proficiencies: Land Vehicles",
            "Languages: One of your choice",
            "Equipment: A whip, a tent, a regional map, a set of traveler's clothes, and a pouch containing 10gp"
        ],
        "Earthspur Miner": [
            "Skill Proficiencies: Athletics, Survival",
            "Languages: Dwarven and Undercommon",
            "Equipment: A shovel or a miner's pick, a block and tackle, a climber's kit, "
            "a set of common clothes, and a pouch containing 5gp"
        ],
        "Harborfolk": [
            "Skill Proficiencies: Athletics, Sleight of Hand",
            "Tool Proficiencies: One type of gaming set, vehicles (water)",
            "Equipment: Fishing tackle, a dice set, playing card set, or Three Dragon Ante set, "
            "a set of common clothes, a rowboat, and a pouch containing 5gp"
        ],
        "Mulmaster Aristocrat": [
            "Skill Proficiencies: Deception, Performance",
            "Tool Proficiencies: One type of artistic artisan's tools and one musical instrument",
            "Equipment: One set of artisan's tools or musical instrument, a set of fine clothes, "
            "and a purse containing 10gp"
        ],
        "Phlan Refugee": [
            "Skill Proficiencies: Insight, Athletics",
            "Tool Proficiencies: One type of artisan's tools",
            "Languages: One of your choosing",
            "Equipment: A set of artisan’s tools (one of your choice), a token of the life you once knew, "
            "a set of traveler’s clothes, and a pouch containing 15gp"
        ],
        "Cormanther Refugee": [
            "Skill Proficiencies: Nature, Survival",
            "Language Proficiencies: Elven",
            "Tool Proficiencies: One type of artisan's tools",
            "Equipment: A two-person tent, artisan's tools, a holy symbol, a set of traveler's clothes, "
            "and a pouch containing 5gp"
        ],
        "Gate Urchin": [
            "Skill Proficiencies: Deception, Sleight of Hand",
            "Tool Proficiencies: Thieves' tools, one type of musical instrument",
            "Equipment: A battered alms box, a musical instrument, a cast-off military jacket, cap, or scarf, "
            "a set of common clothes, and a pouch containing 10gp"
        ],
        "Hillsfar Merchant": [
            "Skill Proficiencies: Insight, Persuasion",
            "Tool Proficiencies: Vehicles (land) and vehicles (water)",
            "Equipment: A set of fine clothes, a signet ring, a letter of introduction from your "
            "family's trading house, and a purse containing 25gp"
        ],
        "Hillsfar Smuggler": [
            "Skill Proficiencies: Perception, Stealth",
            "Language Proficiencies: One racial language",
            "Tool Proficiencies: Forgery kit",
            "Equipment: A forgery kit, a set of common clothes, and a pouch containing 5gp"
        ],
        "Secret Identity": [
            "Skill Proficiencies: Deception, Stealth",
            "Tool Proficiencies: Disguise kit, forgery kit",
            "Equipment: A disguise kit, a forgery kit, a set of common clothes, a belt pouch, 5gp."
        ],
        "Shade Fanatic": [
            "Skill Proficiencies: Deception, Intimidation",
            "Tool Proficiencies: Forgery kit",
            "Languages: Netherese",
            "Equipment: A forgery kit, a transparent cylinder of shadow that has no opening, a signet ring, "
            "a set of fine clothes, and 15gp."
        ],
        "Trade Sheriff": [
            "Skill Proficiencies: Investigation, Persuasion",
            "Tool Proficiencies: Thieves' kit",
            "Languages: Elven",
            "Equipment: A thieves' kit, a gray cloak, Sheriff's insignia (badge), a set of fine clothes, and 17gp."
        ],
        "Celebrity Adventurer's Scion": [
            "Skill Proficiencies: Perception, Performance",
            "Tool Proficiencies: Disguise kit",
            "Languages: Two of your choice",
            "Equipment: A disguise kit, a set of fine clothes, and a belt pouch containing 30 gp."
        ],
        "Failed Merchant": [
            "Skill Proficiencies: Investigation, Persuasion",
            "Tool Proficiencies: One type of artisan's tools",
            "Languages: Any one of your choice",
            "Equipment: One set of artisan's tools, merchant's scale, a set of fine clothes, "
            "and a belt pouch containing 10 gp."
        ],
        "Gambler": [
            "Skill Proficiencies: Deception, Insight",
            "Tool Proficiencies: One gaming set",
            "Languages: Any one of your choice",
            "Equipment: One gaming set, a lucky charm, a set of fine clothes, and a belt pouch containing 15 gp."
        ],
        "Plantiff": [
            "Skill Proficiencies: Medicine, Persuasion"
            "Tool Proficiencies: One type of artisan's tools"
            "Languages: Any one of your choice"
            "Equipment: One set of artisan's tools, a set of fine clothes, and 20 gp."
        ],
        "Rival Intern": [
            "Skill Proficiencies: History, Investigation"
            "Tool Proficiencies: One type of artisan's tools"
            "Languages: Any one of your choice"
            "Equipment: One set of artisan's tools, a ledger from your previous employer containing a small "
            "piece of useful information, a set of fine clothes, and a belt pouch containing 10 gp."
        ],
        "Initiate": [
            "Skill Proficiencies: Athletics, Intimidation",
            "Tool Proficiencies: One type of gaming set, vehicles (land)",
            "Equipment: A simple puzzle box, a scroll containing the basic teachings of the five gods, a gaming set, "
            "a set of common clothes, and a pouch containing 15gp. If you have completed any trials before the "
            "start of the campaign, you also have any cartouches you have earned."
        ],
        "Vizier": [
            "Skill Proficiencies: History, Religion",
            "Tool Proficiencies: One type of artisan's tools, one type of musical instrument",
            "Equipment: A set of artisan’s tools or a musical instrument (one of your choice), a scroll of your "
            "god’s teachings, a vizier’s cartouche, a set of fine clothes, and a pouch containing 25gp"
        ],
        "Inquisitor": [
            "Skill Proficiencies: Investigation, Religion",
            "Tool Proficiencies: Thieves' tools, one set of artisan's tools of your choice",
            "Equipment: A holy symbol, a set of traveler's clothes, and a pouch containing 15gp"
        ],
        "Azorius Functionary": [
            "Skill Proficiencies: Insight, Intimidation",
            "Languages: Two of your choice",
            "Equipment: An Azorius insignia, a scroll containing the text of a law important to you, a bottle "
            "of blue ink, an ink pen, a set of fine clothes, and a pouch containing 10gp (Azorius-minted 1-zino coins)"
        ],
        "Boros Legionnaire": [
            "Skill Proficiencies: Athletics, Intimidation",
            "Tool Proficiencies: One type of gaming set",
            "Languages: Choose one of Celestial, Draconic, Goblin, or Minotaur",
            "Equipment: A Boros insignia, a feather from an angel's wing, a tattered piece of a Boros banner "
            "(a souvenir from a famous battle), a set of common clothes, and a pouch containing 2gp "
            "(Boros-minted 1-zino coins)"
        ],
        "Dimir Operative": [
            "Skill Proficiencies: Deception, Stealth",
            "Tool Proficiencies: Disguise kit",
            "Languages: One of your choice",
            "Equipment: A Dimir insignia, three small knives, a set of dark-colored common clothes, and the starting "
            "equipment of the background described in this chapter for your secondary guild"
        ],
        "Golgari Agent": [
            "Skill Proficiencies: Nature, Survival",
            "Tool Proficiencies: Poisoner's Kit",
            "Languages: Choose one of Elvish, Giant, or Kraul",
            "Equipment: A Golgari insignia, a poisoner's kit, a pet beetle or spider, a set of common clothes, "
            "and a pouch containing 10gp worth of mixed coins."
        ],
        "Gruul Anarch": [
            "Skill Proficiencies: Animal Handling, Athletics",
            "Tool Proficiencies: Herbalism Kit",
            "Languages: Choose one of Draconic, Giant, Goblin, or Sylvan",
            "Equipment: A Gruul insignia, a hunting trap, an herbalism kit, the skull of a boar, a beast-hide cloak, "
            "a set of traveler's clothes, and a pouch containing 10gp (Azorius 1-zino coins)"
        ],
        "Izzet Engineer": [
            "Skill Proficiencies: Arcana, Investigation",
            "Tool Proficiencies: One type of artisan's tools",
            "Languages: Choose one of Draconic, Goblin, or Vedalken",
            "Equipment: An Izzet insignia, one set of artisan's tools, the charred and twisted remains of a "
            "failed experiment, a hammer, a block and tackle, a set of common clothes, and a pouch containing 5gp "
            "(Azorius 1-zino coins)"
        ],
        "Orzhov Representative": [
            "Skill Proficiencies: Intimidation, Religion",
            "Languages: Two of your choice",
            "Equipment: An Orzhov insignia, a foot-long chain made of ten gold coins, vestments, "
            "a set of fine clothes, and a pouch containing 1pp (an Orzhov-minted 10-zino coin)"
        ],
        "Rakdos Cultist": [
            "Skill Proficiencies: Acrobatics, Performance",
            "Tool Proficiencies: One type of musical instrument",
            "Languages: Choose one of either Abyssal or Giant",
            "Equipment: A Rakdos insignia, a musical instrument (one of your choice), a costume, a hooded lantern "
            "made of wrought iron, a 10-foot length of chain with sharply spiked links, a tinderbox, 10 torches, "
            "a set of common clothes, a pouch containing 10gp (a mix of Azorius and Boros 1-zino coins), "
            "and a bottle of sweet, red juice"
        ],
        "Selesnya Initiate": [
            "Skill Proficiencies: Nature, Persuasion",
            "Tool Proficiencies: One type of artisan's tools or one musical instrument",
            "Languages: Choose one of Elvish, Loxodon, or Sylvan",
            "Equipment: A Selesnya insignia, a healer's kit, robes, a set of common clothes, "
            "and a pouch containing 5gp (Azorius 1-zino coins)"
        ],
        "Simic Scientist": [
            "Skill Proficiencies: Arcana, Medicine",
            "Languages: Two of your choice",
            "Equipment: A Simic insignia, a set of commoner's clothes, a book of research notes, an ink pen, "
            "a bottle of squid ink, a flask of oil (made from blubber), a vial of acid (derived from digestive "
            "juices), a vial of fish scales, a vial of seaweed, a vial of jellyfish stingers, a glass bottle of "
            "unidentified slime, and a pouch containing 10gp (Azorius 1-zino coins)"
        ],
        "Grinner": [
            "Skill Proficiencies: Deception, Performance",
            "Tool Proficiencies: One type of musical instrument, thieves' tools",
            "Languages: None",
            "Equipment: A set of fine clothes, a disguise kit, a musical instrument of your choice, a gold-plated "
            "ring depicting a smiling face, and a pouch containing 15gp."
        ],
        "Volstrucker Agent": [
            "Skill Proficiencies: Deception, Stealth",
            "Tool Proficiencies: Poisoner's Kit",
            "Languages: One of your choice",
            "Equipment: A set of common clothes, a black cloak with a hood, a poisoner's kit, "
            "and a pouch containing 10gp"
        ]
    }

    raw_background_list = [
        "Acolyte", "Anthropologist", "Archaeologist", "Athlete", "Charlatan", "City Watch", "Clan Crafter",
        "Cloistered Scholar", "Courtier", "Criminal", "Entertainer", "Faceless", "Faction Agent", "Far Traveler",
        "Feylost", "Fisher", "Folk Hero", "Gladiator", "Guild Artisan", "Guild Merchant", "Haunted One", "Hermit",
        "House Agent", "Inheritor", "Investigator", "Knight", "Knight of the Order", "Marine", "Mercenary Veteran",
        "Noble", "Outlander", "Pirate", "Sage", "Sailor", "Shipwright", "Smuggler", "Soldier", "Spy",
        "Urban Bounty Hunter", "Urchin", "Uthgardt Bounty Hunter", "Waterdhavian Noble", "Witchlight Hand",
        "Black Fist Double Agent", "Dragon Casualty", "Iron Route Bandit", "Phlan Insurgent", "Stojanow Prisoner",
        "Ticklebelly Nomad", "Caravan Specialist", "Earthspur Miner", "Harborfolk", "Mulmaster Aristocrat",
        "Phlan Refugee", "Cormanther Refugee", "Gate Urchin", "Hillsfar Merchant", "Hillsfar Smuggler",
        "Secret Identity", "Shade Fanatic", "Trade Sheriff", "Celebrity Adventurer's Scion", "Failed Merchant",
        "Gambler", "Plantiff", "Rival Intern", "Initiate", "Vizier", "Inquisitor",
        "Azorius Functionary", "Boros Legionnaire", "Dimir Operative", "Golgari Agent", "Gruul Anarch",
        "Izzet Engineer", "Orzhov Representative", "Rakdos Cultist", "Selesnya Initiate", "Simic Scientist",
        "Grinner", "Volstrucker Agent"
    ]


class RawFeat:
    raw_feats = {
        "Aberrant Dragonmark": [
            "Prerequisite: No other dragonmark",
            "You have manifested an aberrant dragonmark. Determine its appearance and the flaw associated with it. "
            "You gain the following benefits:",
            "Increase your Constitution score by 1, to a maximum of 20.",
            "You learn a cantrip of your choice from the sorcerer spell list. In addition, choose a 1st-level spell "
            "from the sorcerer spell list. You learn that spell and can cast it through your mark. Once you cast it, "
            "you must finish a short or long rest before you can cast it again through the mark. Constitution is your "
            "spellcasting ability for these spells.",
            "When you cast the 1st-level spell through your mark, you can expend one of your Hit Dice and roll it. "
            "If you roll an even number, you gain a number of temporary hit points equal to the number rolled. If "
            "you roll an odd number, one random creature within 30 feet of you (not including you) takes force damage "
            "equal to the number rolled. If no other creatures are in range, you take the damage."
        ],
        "Actor": [
            "Skilled at mimicry and dramatics, you gain the following benefits:",
            "Increase your Charisma score by 1, to a maximum of 20.",
            "You have an advantage on Charisma (Deception) and Charisma (Performance) checks when trying to pass "
            "yourself off as a different person.",
            "You can mimic the speech of another person or the sounds made by other creatures. You must have heard "
            "the person speaking, or heard the creature make the sound, for at least 1 minute. A successful Wisdom "
            "(Insight) check contested by your Charisma (Deception) check allows a listener to determine that the "
            "effect is faked."
        ],
        "Alert": [
            "Always on the lookout for danger, you gain the following benefits:",
            "You can’t be surprised while you are conscious."
            "You gain a +5 bonus to initiative.",
            "Other creatures don’t gain advantage on attack rolls against you as a result of being hidden from you."
        ],
        "Artificer Initiate": [
            "You’ve learned some of an artificer’s inventiveness:",
            "You learn one cantrip of your choice from the Artificer spell list, and you learn one 1st-level spell "
            "of your choice from that list. Intelligence is your spellcasting ability for these spells.",
            "You can cast this feat's 1st-level spell without a spell slot, and you must finish a long rest before "
            "you can cast it in this way again. You can also cast the spell using any spell slots you have.",
            "You gain proficiency with one type of artisan's tools of your choice, and you can use that type of tool "
            "as a spellcasting focus for any spell you cast that uses Intelligence as its spellcasting ability."
        ],
        "Athlete": [
            "You have undergone extensive physical training to gain the following benefits:",
            "Increase your Strength or Dexterity score by 1, to a maximum of 20.",
            "When you are prone, standing up uses only 5 feet of your movement.",
            "Climbing doesn’t cost you extra movement.",
            "You can make a running long jump or a running high jump after moving only 5 feet on foot, rather than "
            "10 feet."
        ],
        "Charger": [
            "When you use your action to Dash, you can use a bonus action to make one melee weapon attack or to "
            "shove a creature. If you move at least 10 feet in a straight line immediately before taking this bonus "
            "action, you either gain a +5 bonus to the attack’s damage roll (if you chose to make a melee attack "
            "and hit) or push the target up to 10 feet away from you (if you chose to shove and you succeed)."
        ],
        "Chef": [
            "Time and effort spent mastering the culinary arts has paid off. You gain the following benefits:",
            "Increase your Constitution or Wisdom score by 1, to a maximum of 20.",
            "You gain proficiency with cook’s utensils if you don’t already have it.",
            "As part of a short rest, you can cook special food, provided you have ingredients and cook's utensils on "
            "hand. You can prepare enough of this food for a number of creatures equal to 4 + your proficiency bonus. "
            "At the end of the short rest, any creature who eats the food and spends one or more Hit Dice to regain "
            "hit points regains an extra 1d8 hit points.",
            "With one hour of work or when you finish a long rest, you can cook a number of treats equal to your "
            "proficiency bonus. These special treats last 8 hours after being made. A creature can use a bonus action "
            "to eat one of those treats to gain temporary hit points equal to your proficiency bonus. "
        ],
        "Crossbow Expert": [
            "Thanks to extensive practice with the crossbow, you gain the following benefits:",
            "You ignore the loading quality of crossbows with which you are proficient.",
            "Being within 5 feet of a hostile creature doesn’t impose disadvantage on your ranged attack rolls.",
            "When you use the Attack action and attack with a one handed weapon, you can use a bonus action to "
            "attack with a hand crossbow you are holding."
        ],
        "Crusher": [
            "You are practiced in the art of crushing your enemies, granting you the following benefits:",
            "Increase your Strength or Constitution by 1, to a maximum of 20.",
            "Once per turn, when you hit a creature with an attack that deals bludgeoning damage, you can move it "
            "5 feet to an unoccupied space, provided the target is no more than one size larger than you.",
            "When you score a critical hit that deals bludgeoning damage to a creature, attack rolls against "
            "that creature are made with advantage until the start of your next turn."
        ],
        "Defensive Duelist": [
            "Prerequisite: Dexterity 13 or higher",
            "When you are wielding a finesse weapon with which you are proficient and another creature hits you "
            "with a melee attack, you can use your reaction to add your proficiency bonus to your AC for that attack, "
            "potentially causing the attack to miss you."
        ],
        "Dual Wielder": [
            "You master fighting with two weapons, gaining the following benefits:",
            "You gain a +1 bonus to AC while you are wielding a separate melee weapon in each hand.",
            "You can use two-weapon fighting even when the one handed melee weapons you are wielding aren’t light.",
            "You can draw or stow two one-handed weapons when you would normally be able to draw or stow only one."
        ],
        "Dungeon Delver": [
            "Alert to the hidden traps and secret doors found in many dungeons, you gain the following benefits:",
            "You have advantage on Wisdom (Perception) and Intelligence (Investigation) checks made to detect the "
            "presence of secret doors.",
            "You have advantage on saving throws made to avoid or resist traps.",
            "You have resistance to the damage dealt by traps.",
            "You can search for traps while traveling at a normal pace, instead of only at a slow pace"
        ],
        "Durable": [
            "Hardy and resilient, you gain the following benefits:",
            "Increase your Constitution score by 1, to a maximum of 20.",
            "When you roll a Hit Die to regain hit points, the minimum number of hit points you regain from the roll "
            "equals twice your Constitution modifier (minimum of 2). "
        ],
        "Eldritch Adept": [
            "Prerequisite: Spellcasting or Pact Magic feature",
            "Studying occult lore, you have unlocked eldritch power within yourself: you learn one Eldritch "
            "Invocation option of your choice from the warlock class. If the invocation has a prerequisite, "
            "you can choose that invocation only if you’re a warlock and only if you meet the prerequisite.",
            "Whenever you gain a level, you can replace the invocation with another one from the warlock class."
        ],
        "Elemental Adept": [
            "Prerequisite: The ability to cast at least one spell",
            "When you gain this feat, choose one of the following damage types: acid, cold, fire, lightning, "
            "or thunder.",
            "Spells you cast ignore resistance to damage of the chosen type. In addition, when you roll damage for a "
            "spell you cast that deals damage of that type, you can treat any 1 on a damage die as a 2. "
            "You can select this feat multiple times. Each time you do so, you must choose a different damage type."
        ],
        "Fey Touched": [
            "Your exposure to the Feywild's magic has changed you, granting you the following benefits:",
            "Increase your Intelligence, Wisdom, or Charisma score by 1, to a maximum of 20.",
            "You learn the Misty Step spell and one 1st-level spell of your choice. The 1st-level spell must be from "
            "the Divination or Enchantment school of magic. You can cast each of these spells without expending a "
            "spell slot. Once you cast either of these spells in this way, you can’t cast that spell in this way "
            "again until you finish a long rest. You can also cast these spells using spell slots you have of the "
            "appropriate level. The spells’ spellcasting ability is the ability increased by this feat. "
        ],
        "Fighting Initiate": [
            "Prerequisite: Proficiency with a martial weapon",
            "Your martial training has helped you develop a particular style of fighting. As a result, you learn one "
            "Fighting Style option of your choice from the fighter class. If you already have a style, the one you "
            "choose must be different.",
            "Whenever you reach a level that grants the Ability Score Improvement feature, you can replace this "
            "feat's fighting style with another one from the fighter class that you don't have. "
        ],
        "Gift of the Chromatic Dragon": [
            "You’ve manifested some of the power of chromatic dragons, granting you the following benefits:",
            "Chromatic Infusion. As a bonus action, you can touch a simple or martial weapon and infuse it with one "
            "of the following damage types: acid, cold, fire, lightning, or poison. For the next minute, the weapon "
            "deals an extra 1d4 damage of the chosen type when it hits. After you use this bonus action, you can’t do "
            "so again until you finish a long rest.",
            "Reactive Resistance. When you take acid, cold, fire, lightning, or poison damage, you can use your "
            "reaction to give yourself resistance to that instance of damage. You can use this reaction a number of "
            "times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest. "
        ],
        "Gift of the Gem Dragon": [
            "You’ve manifested some of the power of gem dragons, granting you the following benefits:",
            "Ability Score Increase. Increase your Intelligence, Wisdom, or Charisma score by 1, to a maximum of 20.",
            "Telekinetic Reprisal. When you take damage from a creature that is within 10 feet of you, you can use "
            "your reaction to emanate telekinetic energy. The creature that dealt damage to you must make a Strength "
            "saving throw (DC equals 8 + your proficiency bonus + the ability modifier of the score increased by this "
            "feat). On a failed save, the creature takes 2d8 force damage and is pushed up to 10 feet away from you. "
            "On a successful save, the creature takes half as much damage and isn’t pushed. You can use this reaction "
            "a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a "
            "long rest. "
        ],
        "Gift of the Metallic Dragon": [
            "You’ve manifested some of the power of metallic dragons, granting you the following benefits:",
            "Draconic Healing. You learn the Cure Wounds spell. You can cast this spell without expending a spell "
            "slot. Once you cast this spell in this way, you can’t do so again until you finish a long rest. You can "
            "also cast this spell using spell slots you have. The spell’s spellcasting ability is Intelligence, "
            "Wisdom, or Charisma when you cast it with this feat (choose when you gain the feat).",
            "Protective Wings. You can manifest protective wings that can shield you or others. When you or another "
            "creature you can see within 5 feet of you is hit by an attack roll, you can use your reaction to "
            "manifest spectral wings from your back for a moment. You grant a bonus to the target’s AC equal to your "
            "proficiency bonus against that attack roll, potentially causing it to miss. You can use this reaction a "
            "number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long "
            "rest. "
        ],
        "Grappler": [
            "Prerequisite: Strength 13 or higher",
            "You've developed the skills necessary to hold your own in close-quarters grappling. You gain the "
            "following benefits:",
            "You have advantage on attack rolls against a creature you are grappling.",
            "You can use your action to try to pin a creature grappled by you. To do so, make another grapple check. "
            "If you succeed, you and the creature are both restrained until the grapple ends. "
        ],
        "Great Weapon Master": [
            "You’ve learned to put the weight of a weapon to your advantage, letting its momentum empower your "
            "strikes. You gain the following benefits:",
            "On your turn, when you score a critical hit with a melee weapon or reduce a creature to 0 hit points "
            "with one, you can make one melee weapon attack as a bonus action.",
            "Before you make a melee attack with a heavy weapon that you are proficient with, you can choose to take "
            "a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack’s damage. "
        ],
        "Gunner": [
            "You have a quick hand and keen eye when employing firearms, granting you the following benefits:",
            "Increase your Dexterity score by 1, to a maximum of 20.",
            "You gain proficiency with firearms (see “Firearms” in the Dungeon Master’s Guide).",
            "You ignore the loading property of firearms.",
            "Being within 5 feet of a hostile creature doesn’t impose disadvantage on your ranged attack rolls."
        ],
        "Healer": [
            "You are an able physician, allowing you to mend wounds quickly and get your allies back in the fight. "
            "You gain the following benefits:",
            "When you use a healer's kit to stabilize a dying creature, that creature also regains 1 hit point.",
            "As an action. you can spend one use of a healer's kit to tend to a creature and restore 1d6 + 4 hit "
            "points to it, plus additional hit points equal to the creature's maximum number of Hit Dice. The "
            "creature can't regain hit points from this feat again until it finishes a short or long rest. "
        ],
        "Heavily Armored": [
            "Prerequisite: Proficiency with medium armor",
            "You have trained to master the use of heavy armor, gaining the following benefits:",
            "Increase your Strength score by 1, to a maximum of 20.",
            "You gain proficiency with heavy armor."
        ],
        "Heavy Armor Master": [
            "Prerequisite: Proficiency with heavy armor",
            "You can use your armor to deflect strikes that would kill others. You gain the following benefits:",
            "Increase your Strength score by 1, to a maximum of 20."
            "While you are wearing heavy armor, bludgeoning, piercing, and slashing damage that you take from "
            "nonmagical weapons is reduced by 3. "
        ],
        "Inspiring Leader": [
            "Prerequisite: Charisma 13 or higher",
            "You can spend 10 minutes inspiring your companions, shoring up their resolve to fight. When you do so, "
            "choose up to six friendly creatures (which can include yourself) within 30 feet of you who can see or "
            "hear you and who can understand you. Each creature can gain temporary hit points equal to your level + "
            "your Charisma modifier. A creature can't gain temporary hit points from this feat again until it has "
            "finished a short or long rest. "
        ],
        "Keen Mind": [
            "You have a mind that can track time, direction, and detail with uncanny precision. You gain the "
            "following benefits.",
            "Increase your Intelligence score by 1, to a maximum of 20.",
            "You always know which way is north.",
            "You always know the number of hours left before the next sunrise or sunset.",
            "You can accurately recall anything you have seen or heard within the past month."
        ],
        "Lightly Armored": [
            "You have trained to master the use of light armor, gaining the following benefits.",
            "Increase your Strength or Dexterity score by 1, to a maximum of 20.",
            "You gain proficiency with light armor.",
        ],
        "Linguist": [
            "You have studied languages and codes, gaining the following benefits:",
            "Increase your Intelligence score by 1, to a maximum of 20.",
            "You learn three languages of your choice.",
            "You can ably create written ciphers. Others can't decipher a code you create unless you teach them, "
            "they succeed on an Intelligence check (DC equal to your Intelligence score + your proficiency bonus), "
            "or they use magic to decipher it. "
        ],
        "Lucky": [
            "You have inexplicable luck that seems to kick in at just the right moment.",
            "You have 3 luck points. Whenever you make an attack roll, an ability check, or a saving throw, "
            "you can spend one luck point to roll an additional d20. You can choose to spend one of your luck points "
            "after you roll the die, but before the outcome is determined. You choose which of the d20s is used for "
            "the attack roll, ability check, or saving throw.",
            "You can also spend one luck point when an attack roll is made against you. Roll a d20 and then choose "
            "whether the attack uses the attacker's roll or yours.",
            "If more than one creature spends a luck point to influence the outcome of a roll, the points cancel each "
            "other out; no additional dice are rolled.",
            "You regain your expended luck points when you finish a long rest."
        ],
        "Mage Slayer": [
            "You have practiced techniques in melee combat against spellcasters, gaining the following benefits.",
            "When a creature within 5 feet of you casts a spell, you can use your reaction to make a melee weapon "
            "attack against that creature.",
            "When you damage a creature that is concentrating on a spell, that creature has disadvantage on the "
            "saving throw it makes to maintain its concentration.",
            "You have advantage on saving throws against spells cast by creatures within 5 feet of you."
        ],
        "Magic Initiate": [
            "Choose a class: bard, cleric, druid, sorcerer, warlock, or wizard. You learn two cantrips of your choice "
            "from that class's spell list. In addition, choose one 1st-level spell to learn from that same list. "
            "Using this feat, you can cast the spell once at its lowest level, and you must finish a long rest before "
            "you can cast it in this way again.",
            "Your spellcasting ability for these spells depends on the class you chose: Charisma for bard, sorcerer, "
            "or warlock; Wisdom for cleric or druid; or Intelligence for wizard. "
        ],
        "Martial Adept": [
            "You have martial training that allows you to perform special combat maneuvers. You gain the following "
            "benefits.",
            "You learn two maneuvers of your choice from among those available to the Battle Master archetype in the "
            "fighter class. If a maneuver you use requires your target to make a saving throw to resist the "
            "maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity "
            "modifier (your choice).",
            "You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from "
            "another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. "
            "You regain your expended superiority dice when you finish a short or long rest. "
        ],
        "Medium Armor Master": [
            "Prerequisite: Proficiency with medium armor",
            "You have practiced moving in medium armor to gain the following benefits:",
            "Wearing medium armor doesn't impose disadvantage on your Dexterity (Stealth) checks.",
            "When you wear medium armor, you can add 3, rather than 2, to your AC if you have a Dexterity of 16 or "
            "higher. "
        ],
        "Metamagic Adept": [
            "Prerequisite: Spellcasting or Pact Magic feature",
            "You've learned how to exert your will on your spells to alter how they function:",
            "You learn two Metamagic options of your choice from the sorcerer class. You can use only one Metamagic "
            "option on a spell when you cast it, unless the option says otherwise. Whenever you reach a level that "
            "grants the Ability Score Improvement feature, you can replace one of these Metamagic options with "
            "another one from the sorcerer class. "
            "You gain 2 sorcery points to spend on Metamagic (these points are added to any sorcery points you have "
            "from another source but can be used only on Metamagic). You regain all spent sorcery points when you "
            "finish a long rest. "
        ],
        "Mobile": [
            "You are exceptionally speedy and agile. You gain the following benefits:",
            "Your speed increases by 10 feet.",
            "When you use the Dash action, difficult terrain doesn't cost you extra movement on that turn.",
            "When you make a melee attack against a creature, you don't provoke opportunity attacks from that "
            "creature for the rest of the turn, whether you hit or not. "
        ],
        "Moderately Armored": [
            "Prerequisite: Proficiency with light armor",
            "You have trained to master the use of medium armor and shields, gaining the following benefits:",
            "Increase your Strength or Dexterity score by 1, to a maximum of 20.",
            "You gain proficiency with medium armor and shields."
        ],
        "Mounted Combatant": [
            "You are a dangerous foe to face while mounted. While you are mounted and aren't incapacitated, "
            "you gain the following benefits:",
            "You have advantage on melee attack rolls against any unmounted creature that is smaller than your mount.",
            "You can force an attack targeted at your mount to target you instead.",
            "If your mount is subjected to an effect that allows it to make Dexterity saving throw to take only half "
            "damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fails. "
        ],
        "Observant": [
            "Quick to notice details of your environment, you gain the following benefits:",
            "Increase your Intelligence or Wisdom score by 1, to a maximum of 20.",
            "If you can see a creature's mouth while it is speaking a language you understand, you can interpret what "
            "it's saying by reading its lips.",
            "You have a +5 bonus to your passive Wisdom (Perception) and passive Intelligence (Investigation) scores."
        ],
        "Piercer": [
            "You have achieved a penetrating precision in combat, granting you the following benefits:",
            "Increase your Strength or Dexterity by 1, to a maximum of 20.",
            "Once per turn, when you hit a creature with an attack that deals piercing damage, you can re-roll one of "
            "the attack’s damage dice, and you must use the new roll.",
            "When you score a critical hit that deals piercing damage to a creature, you can roll one additional "
            "damage die when determining the extra piercing damage the target takes. "
        ],
        "Poisoner": [
            "You can prepare and deliver deadly poisons, gaining the following benefits:",
            "When you make a damage roll, you ignore resistance to poison damage.",
            "You can coat a weapon in poison as a bonus action, instead of an action.",
            "You gain proficiency with the poisoner's kit if you don't already have it. With one hour of work using a "
            "poisoner's kit and expending 50 gp worth of materials, you can create a number of doses of potent poison "
            "equal to your proficiency bonus. Once applied to a weapon or piece of ammunition, the poison retains its "
            "potency for 1 minute or until you hit with the weapon or ammunition. When a creature takes damage from "
            "the coated weapon or ammunition, that creature must succeed on a DC 14 Constitution saving throw or take "
            "2d8 poison damage and become poisoned until the end of your next turn. "
        ],
        "Polearm Master": [
            "You gain the following benefits:",
            "When you take the Attack action and attack with only a glaive, halberd, quarterstaff, or spear, "
            "you can use a bonus action to make a melee attack with the opposite end of the weapon. This attack uses "
            "the same ability modifier as the primary attack. The weapon's damage die for this attack is a d4, "
            "and it deals bludgeoning damage.",
            "While you are wielding a glaive, halberd, pike, quarterstaff, or spear, other creatures provoke an "
            "opportunity attack from you when they enter the reach you have with that weapon. "
        ],
        "Resilient": [
            "Choose one ability score. You gain the following benefits:",
            "Increase the chosen ability score by 1, to a maximum of 20.",
            "You gain proficiency in saving throws using the chosen ability."
        ],
        "Ritual Caster": [
            "Prerequisite: Intelligence or Wisdom of 13 or higher",
            "You have learned a number of spells that you can cast as rituals. These spells are written in a ritual "
            "book, which you must have in hand while casting one of them.",
            "When you choose this feat, you acquire a ritual book holding two 1st-level spells of your choice. Choose "
            "one of the following classes: bard, cleric, druid, sorcerer, warlock, or wizard. You must choose your "
            "spells from that class's spell list, and the spells you choose must have the ritual tag. The class you "
            "choose also must have the ritual tag. The class you choose also determines your spellcasting ability for "
            "these spells: Charisma for bard, sorcerer, or warlock; Wisdom for cleric or druid; or Intelligence for "
            "wizard.",
            "If you come across a spell in written form, such as a magical spell scroll or a wizard's spellbook, "
            "you might be able to add it to your ritual book. The spell must be on the spell list for the class you "
            "chose, the spell's level can be no higher than half your level (rounded up), and it must have the ritual "
            "tag. The process of copying the spell into your ritual book takes 2 hours per level of the spell, "
            "and costs 50 gp per level. The cost represents the material components you expend as you experiment with "
            "the spell to master it, as well as the fine inks you need to record it. "
        ],
        "Savage Attacker": [
            "Once per turn when you roll damage for a melee weapon attack, you can reroll the weapon's damage dice "
            "and use either total. "
        ],
        "Sentinel": [
            "You have mastered techniques to take advantage of every drop in any enemy's guard, gaining the following "
            "benefits.",
            "When you hit a creature with an opportunity attack, the creature's speed becomes 0 for the rest of the "
            "turn.",
            "Creatures provoke opportunity attacks from you even if they take the Disengage action before leaving "
            "your reach.",
            "When a creature within 5 feet of you makes an attack against a target other than you (and that target "
            "doesn't have this feat), you can use your reaction to make a melee weapon attack against the attacking "
            "creature. "
        ],
        "Shadow Touched": [
            "Your exposure to the Shadowfell's magic has changed you, granting you the following benefits:"
            "Increase your Intelligence, Wisdom, or Charisma score by 1, to a maximum of 20."
            "You learn the Invisibility spell and one 1st-level spell of your choice. The 1st-level spell must be "
            "from the Illusion or Necromancy school of magic. You can cast each of these spells without expending a "
            "spell slot. Once you cast either of these spells in this way, you can't cast that spell in this way "
            "again until you finish a long rest. You can also cast these spells using spell slots you have of the "
            "appropriate level. The spells' spellcasting ability is the ability increased by this feat. "
        ],
        "Sharpshooter": [
            "You have mastered ranged weapons and can make shots that others find impossible. You gain the following "
            "benefits: "
            "Attacking at long range doesn't impose disadvantage on your ranged weapon attack rolls."
            "Your ranged weapon attacks ignore half and three-quarters cover."
            "Before you make an attack with a ranged weapon that you are proficient with, you can choose to take a -5 "
            "penalty to the attack roll. If that attack hits, you add +10 to the attack's damage. "
        ],
        "Shield Master": [
            "You use shields not just for protection but also for offense. You gain the following benefits while you "
            "are wielding a shield:",
            "If you take the Attack action on your turn, you can use a bonus action to try to shove a creature within "
            "5 feet of you with your shield.",
            "If you aren't incapacitated, you can add your shield's AC bonus to any Dexterity saving throw you make "
            "against a spell or other harmful effect that targets only you.",
            "If you are subjected to an effect that allows you to make a Dexterity saving throw to take only half "
            "damage, you can use your reaction to take no damage if you succeed on the saving throw, interposing your "
            "shield between yourself and the source of the effect. "
        ],
        "Skill Expert": [
            "You have honed your proficiency with particular skills, granting you the following benefits:",
            "Increase one ability score of your choice by 1, to a maximum of 20.",
            "You gain proficiency in one skill of your choice.",
            "Choose one skill in which you have proficiency. You gain expertise with that skill, which means your "
            "proficiency bonus is doubled for any ability check you make with it. The skill you choose must be one "
            "that isn't already benefiting from a feature, such as Expertise, that doubles your proficiency bonus. "
        ],
        "Skilled": [
            "You gain proficiency in any combination of three skills or tools of your choice."
        ],
        "Skulker": [
            "Prerequisite: Dexterity 13 or higher",
            "You are an expert at slinking through shadows. You gain the following benefits:",
            "You can try to hide when you are lightly obscured from the creature from which you are hiding.",
            "When you are hidden from a creature and miss it with a ranged weapon attack, making the attack doesn't "
            "reveal your position.",
            "Dim light doesn't impose disadvantage on your Wisdom (Perception) checks relying on sight."
        ],
        "Slasher": [
            "You’ve learned where to cut to have the greatest results, granting you the following benefits:",
            "Increase your Strength or Dexterity by 1, to a maximum of 20.",
            "Once per turn when you hit a creature with an attack that deals slashing damage, you can reduce the "
            "speed of the target by 10 feet until the start of your next turn.",
            "When you score a critical hit that deals slashing damage to a creature, you grievously wound it. Until "
            "the start of your next turn, the target has disadvantage on all attack rolls. "
        ],
        "Spell Sniper": [
            "Prerequisite: The ability to cast at least one spell",
            "You have learned techniques to enhance your attacks with certain kinds of spells, gaining the following "
            "benefits:",
            "When you cast a spell that requires you to make an attack roll, the spell's range is doubled.",
            "Your ranged spell attacks ignore half cover and three-quarters cover.",
            "You learn one cantrip that requires an attack roll. Choose the cantrip from the bard, cleric, druid, "
            "sorcerer, warlock, or wizard spell list. Your spellcasting ability for this cantrip depends on the spell "
            "list you chose from: Charisma for bard, sorcerer, and warlock; Wisdom for cleric or druid; or "
            "Intelligence for wizard. "
        ],
        "Tavern Brawler": [
            "Accustomed to the rough-and-tumble fighting using whatever weapons happen to be at hand, you gain the "
            "following benefits:",
            "Increase your Strength or Consititution score by 1, to a maximum of 20.",
            "You are proficient with improvised weapons.",
            "Your unarmed strike uses a d4 for damage.",
            "When you hit a creature with an unarmed strike or an improvised weapon on your turn, you can use a bonus "
            "action to attempt to grapple the target. "
        ],
        "Telekinetic": [
            "You learn to move things with your mind, granting you the following benefits:",
            "Increase your Intelligence, Wisdom, or Charisma score by 1, to a maximum of 20.",
            "You learn the Mage Hand cantrip. You can cast it without verbal or somatic components, and you can make "
            "the spectral hand invisible. If you already know this spell, its range increases by 30 feet when you "
            "cast it. Its spellcasting ability is the ability increased by this feat.",
            "As a bonus action, you can try to telekinetically shove one creature you can see within 30 feet of you. "
            "When you do so, the target must succeed on a Strength saving throw (DC 8 + your proficiency bonus + the "
            "ability modifier of the score increased by this feat) or be moved 5 feet toward or away from you. A "
            "creature can willingly fail this save. "
        ],
        "Telepathic": [
            "You awaken the ability to mentally connect with others, granting you the following benefits:",
            "Increase your Intelligence, Wisdom, or Charisma score by 1, to a maximum of 20.",
            "You can speak telepathically to any creature you can see within 60 feet of you. Your telepathic "
            "utterances are in a language you know, and the creature understands you only if it knows that language. "
            "Your communication doesn't give the creature the ability to respond to you telepathically.",
            "You can cast the Detect Thoughts spell, requiring no spell slot or components, and you must finish a "
            "long rest before you can cast it this way again. Your spellcasting ability for the spell is the ability "
            "increased by this feat. If you have spell slots of 2nd level or higher, you can cast this spell with "
            "them. "
        ],
        "Tough": [
            "Your hit point maximum increases by an amount equal to twice your level when you gain this feat. "
            "Whenever you gain a level thereafter, your hit point maximum increases by an additional 2 hit points "
        ],
        "War Caster": [
            "Prerequisite: The ability to cast at least one spell",
            "You have practiced casting spells in the midst of combat, learning techniques that grant you the "
            "following benefits:",
            "You have advantage on Constitution saving throws that you make to maintain your concentration on a spell "
            "when you take damage.",
            "You can perform the somatic components of spells even when you have weapons or a shield in one or both "
            "hands.",
            "When a hostile creature's movement provokes an opportunity attack from you, you can use your reaction to "
            "cast a spell at the creature, rather than making an opportunity attack. The spell must have a casting "
            "time of 1 action and must target only that creature. "
        ],
        "Weapon Master": [
            "You have practiced extensively with a variety of weapons, gaining the following benefits:",
            "Increase your Strength or Dexterity score by 1, to a maximum of 20.",
            "You gain proficiency with four weapons of your choice. Each one must be a simple or a martial weapon."
        ]
    }

    raw_feats_list = [
        "Aberrant Dragonmark", "Actor", "Alert", "Artificer Initiate", "Athlete", "Charger", "Chef",
        "Crossbow Expert", "Crusher", "Defensive Duelist", "Dual Wielder", "Dungeon Delver", "Durable",
        "Eldritch Adept", "Elemental Adept", "Fey Touched", "Fighting Initiate",
        "Gift of the Chromatic Dragon", "Gift of the Gem Dragon", "Gift of the Metallic Dragon",
        "Grappler", "Great Weapon Master", "Gunner", "Healer", "Heavily Armored", "Heavy Armor Master",
        "Inspiring Leader", "Keen Mind", "Lightly Armored", "Linguist", "Lucky", "Mage Slayer",
        "Magic Initiate", "Martial Adept", "Medium Armor Master", "Metamagic Adept", "Mobile",
        "Moderately Armored", "Mounted Combatant", "Observant", "Piercer", "Poisoner", "Polearm Master",
        "Resilient", "Ritual Caster", "Savage Attacker", "Sentinel", "Shadow Touched", "Sharpshooter",
        "Shield Master", "Skill Expert", "Skilled", "Skulker", "Slasher", "Spell Sniper",
        "Tavern Brawler", "Telekinetic", "Telepathic", "Tough", "War Caster", "Weapon Master"
    ]


class RawName:
    male_raw_first_names = {
        "Dwarf": [
            "Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk",
            "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim",
            "Rurik", "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"
        ],
        "Elf": [
            "Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan",
            "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren",
            "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"
        ],
        "Halfling": [
            "Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric",
            "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"
        ],
        "Human": [
            "Aseir", "Bardeid", "Haseid", "Khemed", "Mehmen", "Sudeiman", "Zasheir", "Darvin", "Dorn",
            "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal", "Stedd", "Bor", "Fodel", "Glar",
            "Grigor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor", "Ander", "Blath", "Bran", "Frath",
            "Geth", "Lander", "Luth", "Malcer", "Stor", "Taman", "Urth", "Aoth", "Bareris", "Ehput-Ki", "Kethoth",
            "Mumed", "Ramas", "So-Kehur", "Thazar-De", "Urhur", "Borivik", "Faurgar", "Jandar", "Kanithar", "Madislak",
            "Ralmevik", "Shaumar", "Vladislak", "An", "Chen", "Chi", "Fai", "Jiang", "Jun", "Lian", "Long", "Meng",
            "On", "Shan", "Shui", "Wen", "Anton", "Diero", "Marcon", "Pieron", "Rimardo", "Romero", "Salazar", "Umbero"
        ],
        "Gnome": [
            "Alston", "Alvyn", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin", "Frug", "Gerbo",
            "Gimble", "Glim", "Jebeddo", "Kellen", "Namfoodle", "Orryn", "Roondar", "Seebo", "Sindri", "Warryn",
            "Wrenn", "Zook"
        ],
        "Half-Elf": [
            # Utilize Human/Elf Naming conventions
            "Test"
        ],
        "Half-Orc": [
            "Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Mhurren", "Ront", "Shump", "Thokk"
        ],
        "Tiefling": [
            "Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Leucis", "Melech", "Mordai",
            "Morthos", "Pelaios", "Skamos", "Therai"
        ],
        "Aasimar": [
            "Test"
        ],
        "Forbolg": [
            "Test"
        ],
        "Goliath": [
            "Test"
        ],
        "Kenku": [
            "Test"
        ],
        "Lizardfolk": [
            "Test"
        ],
        "Tabaxi": [
            "Test"
        ],
        "Triton": [
            "Test"
        ],
        "Goblin": [
            "Test"
        ],
        "Variant Human": [
            # Human Names
            "Test"
        ]
    }

    female_raw_first_names = {
        "Dwarf": [
            "Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda",
            "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl",
            "Torbera", "Torgga", "Vistra"
        ],
        "Elf": [
            "Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Drusilia",
            "Enna", "Felosial", "Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara",
            "Quelenna", "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirastra", "Thia", "Vadania",
            "Valanthe", "Xanaphia"
        ],
        "Halfling": [
            "Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Merla", "Nedda",
            "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani", "Verna"
        ],
        "Human": [
            "Atala", "Ceidil", "Hama", "Jasmal", "Meilil", "Seipora", "Yasheira", "Zasheida", "Anton", "Diero",
            "Marcon", "Pieron", "Rimardo", "Romero", "Salazar", "Umbero", "Alethra", "Kara", "Katernin", "Mara",
            "Natali", "Olma", "Tana", "Zora", "Amafrey", "Betha", "Cefrey", "Kethra", "Mara", "Olga", "Silifrey",
            "Westra", "Arizima", "Chathi", "Nephis", "Nulara", "Murithi", "Sefris", "Thola", "Umara", "Zolis",
            "Fyevarra", "Hulmarra", "Immith", "Imzel", "Navarra", "Shevarra", "Tammith", "Yuldra", "Bai", "Chao",
            "Jia", "Lei", "Mei", "Qiao", "Shui", "Tai", "Balama", "Dona", "Faila", "Jalana", "Luisa", "Marta",
            "Quara", "Selise", "Vonda"
        ],
        "Gnome": [
            "Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ella", "Ellyjobell", "Ellywick",
            "Lilli", "Loopmottin", "Lorilla", "Mardnab", "Nissa", "Nyx", "Oda", "Orla", "Roywyn", "Shamil", "Tana",
            "Waywocket", "Zanna"
        ],
        "Half-Elf": [
            # Utilize Human/Elf Naming conventions
            "Test Last"
        ],
        "Half-Orc": [
            "Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka", "Shautha", "Sutha", "Vola", "Volen",
            "Yevelda"
        ],
        "Tiefling": [
            "Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria", "Nemeia",
            "Orianna", "Phelaia", "Rieta"
        ],
        "Aasimar": [
            "Test Last"
        ],
        "Forbolg": [
            "Test Last"
        ],
        "Goliath": [
            "Test Last"
        ],
        "Kenku": [
            "Test Last"
        ],
        "Lizardfolk": [
            "Test Last"
        ],
        "Tabaxi": [
            "Test Last"
        ],
        "Triton": [
            "Test Last"
        ],
        "Goblin": [
            "Test Last"
        ],
        "Variant Human": [
            # Human Names
            "Test Last"
        ]
    }

    raw_last_names = {
        "Dwarf": [
            "Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek",
            "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"
        ],
        "Elf": [
            "Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Naïlo", "Siannodel",
            "Xiloscient"
        ],
        "Halfling": [
            "Brushgather", "Goodbarrel", "Greenbottle", "High-hill", "Hilltopple", "Leagallow", "Tealeaf", "Thorngage",
            "Tosscobble", "Underbough"
        ],
        "Human": [
            "Basha", "Dumein", "Jassan", "Khalid", "Mostana", "Pashar", "Rein", "Amblecrown", "Buckman", "Dundragon",
            "Evenwood", "Greycastle", "Tallstag", "Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk", "Nemetsk", "Shemov",
            "Starag", "Brightwood", "Helder", "Hornraven", "Lackman", "Stormwind", "Windrivver", "Ankhalab", "Anskuld",
            "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt", "Chergoba", "Dyernina", "Iltazyara", "Murnyethara",
            "Stayanoga", "Ulmokina", "Chien", "Huang", "Kao", "Kung", "Lao", "Ling", "Mei", "Pin", "Shin", "Sum",
            "Tan", "Wan", "Agosto", "Astorio", "Calabra", "Domine", "Falone", "Marivaldi", "Pisacar", "Ramondo"
        ],
        "Gnome": [
            "Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Timbers",
            "Turen"
        ],
        "Half-Elf": [
            # Utilize Human/Elf Naming conventions
            "Test Last Last"
        ],
        "Half-Orc": [
            # Doesn't have last name
            "Test Last Last"
        ],
        "Tiefling": [
            # Doesn't have last name
            "Test Last Last"
        ],
        "Aasimar": [
            "Test Last Last"
        ],
        "Forbolg": [
            "Test Last Last"
        ],
        "Goliath": [
            "Test Last Last"
        ],
        "Kenku": [
            "Test Last Last"
        ],
        "Lizardfolk": [
            "Test Last Last"
        ],
        "Tabaxi": [
            "Test Last Last"
        ],
        "Triton": [
            "Test Last Last"
        ],
        "Goblin": [
            "Test Last Last"
        ],
        "Variant Human": [
            # Human Names
            "Test Last Last"
        ]
    }

