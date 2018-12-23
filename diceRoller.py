def diceroller(selection):
    version = '3'

    # print(selection)

    import random

    def reset():
        global sides, rolls, modifier, yn, rollSuccess, msg
        sides = 0  # Sides on the given die
        rolls = 0  # Total number of rolls
        modifier = '0'  # Modifiers to be Added after the fact
        rollSuccess = 0
        msg = ''

    reset()

    # print('Dice Roller Version ' + version)

    def check():
        try:
            request()
        except:
            basic()

    def basic():
        global msg
        if '+' in selection:
            op = '+'
            a, b = selection.split('+')
            total = int(a) + int(b)
        elif '-' in selection:
            op = '-'
            a, b = selection.split('-')
            total = int(a) - int(b)
        elif '*' in selection:
            op = '*'
            a, b = selection.split('*')
            total = int(a) * int(b)
        elif '/' in selection:
            op = '/'
            a, b = selection.split('/')
            total = int(a) / int(b)
        else:
            msg = 'Error\nUnknown Operator'
            return msg
        msg = 'Calculating:' + '\n' + str(a) + op + str(b) + '=' + str(total)

    def request():
        global sides, rolls, modifier
        rolls, a = selection.split('d')
        try:
            sides, modifier = a.split('+')
        except:
            try:
                sides, modifier = a.split('-')
                modifier = '-' + str(modifier)
            except:
                sides = a

        sides = int(sides)
        rolls = int(rolls)
        modifier = int(modifier)
        rollBones()

    def rollBones():
        global rolls, sides, modifier, msg
        roll = 0  # Outcome of a roll
        total = 0  # Total of all rolls combined, without modifier
        modifier = int(modifier)
        if modifier == 0:  # Cleans up equation when using modifiers
            modsy = ''
        elif modifier > 0:
            modsy = '+' + str(modifier)
        elif modifier < 0:
            modsy = '-' + str(-1 * modifier)

        # print('Rolling ' + str(rolls) + 'd' + str(sides) + str(modsy))
        trolls = rolls

        r = []

        while rolls > 0:
            roll = random.randint(1, sides)
            if roll == sides or roll == 1:
                r.append('**' + str(roll) + '**')
            else:
                r.append(roll)
            total = total + roll
            rolls = rolls - 1

        # print(r)

        r = str(r)

        # print('Total Rolled: ' + str(total))

        if modifier != 0:
            mofi = ''
            if modifier > 0:
                mofi = str(total) + (' + ') + str(modifier)
            elif modifier < 0:
                mofi = str(total) + (' - ') + str(-1 * modifier)
            # print('Modified Total: ' + str(total + modifier))
            msg = 'Rolling ' + str(trolls) + 'd' + str(sides) + str(modsy) + '\n' + r + '\n' + 'Total Rolled: ' + str(total) + '\n' + mofi + '\n' + 'Modified Total: ' + str(total + modifier)
        else:
            msg = 'Rolling ' + str(trolls) + 'd' + str(sides) + str(modsy) + '\n' + r + '\n' + 'Total Rolled: ' + str(total)

    check()
    return msg
