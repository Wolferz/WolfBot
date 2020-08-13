def create_random_character():
    import random
    import os
    import shutil
    import openpyxl
    from math import floor

    folder_path = os.getcwd() + "/randomcharacter"
    base_file = folder_path + "/blanksheet.xlsx"

   # if not os.path.isdir(folder_path):
   #     print('Character Sheet Directory Not Found, Remaking It')
   #     try:
   #         os.mkdir(folder_path)
   #     except OSError as e:
   #         print('Error In Creating Character Sheet Directory. [{}]'.format(e))
   #         return
   #     else:
   #         print('Current Directory: ' + folder_path)
   # else:
   #     print('Current Directory: ' + folder_path)

    if not os.path.isfile(base_file):
        print('ERROR, blank sheet not found at: ' + base_file)
        return

    abilities = ["str", "dex", "con", "int", "wis", "cha"]

    races = {
        "dragonborn": ["str", "str", "cha"],
        "dwarf": ["con", "con"],
        "elf": ["dex", "dex"],
        "gnome": ["int", "int"],
        "half-elf": ["cha", "cha", "pic"],
        "halfling": ["dex", "dex"],
        "half-orc": ["str", "str", "con"],
        "human": ["str", "dex", "con", "int", "wis", "cha"],
        "tiefling": ["cha", "cha", "int"]
    }
    classes = {
        "barbarian": 12,
        "bard": 8,
        "cleric": 8,
        "druid": 8,
        "fighter": 10,
        "monk": 8,
        "paladin": 10,
        "ranger": 10,
        "rogue": 8,
        "sorcerer": 6,
        "warlock": 8,
        "wizard": 6
    }

    first = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
             'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
             'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
             'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam', 'She', 'Sheel',
             'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

    second = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
              'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
              'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
              'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
              'wain', 'wan', 'win', 'wise', 'ya']

    c_class = random.choice(list(classes))
    race = random.choice(list(races))
    name = random.choice(first) + random.choice(second)
    hp = classes[c_class]

    b_stats = {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 0}
    r_stats = {"str": races[race].count("str"), "dex": races[race].count("dex"), "con": races[race].count("con"),
               "int": races[race].count("int"), "wis": races[race].count("wis"), "cha": races[race].count("cha")}
    for stat in b_stats:
        i = 0
        rolls = []
        while i < 4:
            i += 1
            roll = 1
            while roll == 1:
                roll = random.randint(1, 6)
            else:
                rolls.append(roll)
        total = sum(rolls)
        if total + r_stats[stat] > 20:
            total = 20 - r_stats[stat]
        b_stats[stat] = total

    if "pic" in races[race]:
        races[race].append(random.choice(abilities))

    mods = {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 0}
    for stat in b_stats:
        score = b_stats[stat] + r_stats[stat]
        mods[stat] = floor((score / 2) - 5)

    c_scores = {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 0}
    for score in c_scores:
        c_scores[score] = b_stats[score] + r_stats[score]

    file_dir = os.getcwd() + "/randomcharacter/" + name + ".xlsx"

    try:
        shutil.copy(base_file, file_dir)
    except IOError:
        print("ERROR: random character folder is not writable")
        return

    wb = openpyxl.load_workbook(file_dir)
    sheet = wb.active
    sheet["A1"] = name
    sheet["B2"] = race.capitalize()
    sheet["D2"] = c_class.capitalize()
    sheet["F1"] = 1
    sheet["F2"] = hp
    sheet["A4"] = mods["str"]
    sheet["B4"] = mods["dex"]
    sheet["C4"] = mods["con"]
    sheet["D4"] = mods["int"]
    sheet["E4"] = mods["wis"]
    sheet["F4"] = mods["cha"]
    sheet["A6"] = str(b_stats["str"]) + " + " + str(r_stats["str"])
    sheet["B6"] = str(b_stats["dex"]) + " + " + str(r_stats["dex"])
    sheet["C6"] = str(b_stats["con"]) + " + " + str(r_stats["con"])
    sheet["D6"] = str(b_stats["int"]) + " + " + str(r_stats["int"])
    sheet["E6"] = str(b_stats["wis"]) + " + " + str(r_stats["wis"])
    sheet["F6"] = str(b_stats["cha"]) + " + " + str(r_stats["cha"])
    wb.save(file_dir)

    return name, file_dir, c_scores, race, c_class
