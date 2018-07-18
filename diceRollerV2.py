def diceroller(selection):
    version = '2'

    print(selection)

    import random, time

    a = bool(True)
    def reset():
        #print('ResetDebug')
        global sides, rolls, modifier, yn, rollSuccess, msg
        sides = 0 #Sides on the given die
        rolls = 0 #Total number of rolls
        modifier = '0' #Modifiers to be Added after the fact
        yn = 'y' #Answer to roll again question
        rollSuccess = 0
        msg = ''

    reset()

    print('Dice Roller Version ' + version)

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

    def rollBones():
        global rolls, sides, modifier, msg
        roll = 0 #Outcome of a roll
        total = 0 #Total of all rolls combined, without modifier
        modifier = int(modifier)
        if modifier == 0: #Cleans up equation when using modifiers
            modsy = ''
        elif modifier > 0:
            modsy = '+' + str(modifier)
        elif modifier < 0:
            modsy = '-' + str(-1 * modifier)

        print('Rolling ' + str(rolls) + 'd' + str(sides) + str(modsy))
        trolls = rolls

        r = []

        while rolls > 0:
            rollSuccess = 1
            roll = random.randint(1,sides)
            if roll == sides or roll == 1:
                r.append('**' + str(roll) + '**')
            else:
                r.append(roll)
            total = total + roll
            rolls = rolls - 1

        print(r)

        r = str(r)

        print('Total Rolled: ' + str(total))

        if modifier != 0:
            mofi = ''
            if modifier > 0:
                mofi = str(total) + (' + ') + str(modifier)
            elif modifier < 0:
                mofi = str(total) + (' - ') + str(-1 * modifier)
            print('Modified Total: ' + str(total + modifier))
            msg = 'Rolling ' + str(trolls) + 'd' + str(sides) + str(modsy) + '\n' + r + '\n' + 'Total Rolled: ' + str(total) + '\n' + mofi + '\n' + 'Modified Total: ' + str(total + modifier)
        else:
            msg = 'Rolling ' + str(trolls) + 'd' + str(sides) + str(modsy) + '\n' + r + '\n' + 'Total Rolled: ' + str(total)

    request()
    rollBones()
    return msg
