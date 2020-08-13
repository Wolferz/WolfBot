import random


def separator(msg):  # Separates the input roll into separate variables
    advantage = ['adv', 'advantage']
    disadvantage = ['dis', 'dadv', 'disadv', 'disavantage']
    count = ''
    die = ''
    diemod = ''
    adv = 0
    if any(a in msg for a in advantage):
        adv = 1
    elif any(d in msg for d in disadvantage):
        adv = -1
    if 'd' in msg:  # Is it a roll?
        try:  # Is it a 1d20 or a d20 style (There is a good chance this does absolutely nothing)
            count, diemod = msg.split('d')
        except ValueError:
            count = 1
            diemod = msg
        finally:
            try:
                die, mod = diemod.split('+')  # Addition Modifier
                operator = '+'
            except ValueError:
                try:
                    die, mod = diemod.split('-')  # Subtraction Modifier
                    operator = '-'
                except ValueError:
                    try:
                        die, mod = diemod.split('*')  # Multiplier Modifier
                        operator = '*'
                    except ValueError:
                        try:
                            die, mod = diemod.split('/')  # Division Modifier
                            operator = '/'
                        except ValueError:  # No Modifier
                            operator = ''
                            mod = ''
                            if not any(symbol in msg for symbol in ['+', '-', '*', '/']):
                                die = diemod

    else:  # The same thing as the if above, but sets count to 0 for strait math
        count = '0'
        try:
            die, mod = msg.split('+')
            operator = '+'
        except ValueError:
            try:
                die, mod = msg.split('-')
                operator = '-'
            except ValueError:
                try:
                    die, mod = msg.split('*')
                    operator = '*'
                except ValueError:
                    try:
                        die, mod = msg.split('/')
                        operator = '/'
                    except ValueError:
                        return 'Unknown Operator'

    if count is '':
        count = 1
    return count, die, mod, operator, adv


def organizer(count, die, mod, operator, roll, total, tmod):  # Formats the roll into a Discord readable string
    operation = ''  # Empty variable to avoid Undefined Error
    str(count)  # Converts all the relevant Integers to Strings
    str(die)
    str(mod)
    str(roll)
    str(total)
    str(tmod)
    selection = 'Rolling: {}d{}{}{}'.format(count, die, operator, mod)  # First Line of Response
    rolling = '\n{}\nTotal: {}'.format(roll, total)  # Second and Third Line of Response
    if operator is not '':  # Checks for an operator
        operation = '\n{}{}{}= **{}**'.format(total, operator, mod, tmod)  # Fourth line of Response
    return '{}{}{}'.format(selection, rolling, operation)  # Return the message in a readable format


def roller(selection):  # Returns the Roll or Error as a single string
    count, die, mod, operator, adv = separator(msg=selection)  # When not rolling 'die' acts as another mod
    count = int(count)  # Done separate to avoid an error on next line
    if 'd' in selection and count > 0:  # Rolling Dice
        total = 0  # Total of all rolls combined
        tmod = 0  # Total with Modifier
        rolls = []  # Empty list for append statement
        counter = count  # Done this way to be able to avoid count being 0 in the return message
        die = int(die)  # Sides on the die, converted to an integer
        if mod is not '':  # Avoid an error when converting '' to an integer
            mod = int(mod)
        while counter > 0:  # Makes sure all dice get rolled
            counter -= 1  # Subtracts from counter as to not go over intended count
            roll = random.randint(1, die)  # Actually rolling the die, using the sides of the die as the maximum
            rolls.append(roll)  # Adding the rolled number to the list
            total += roll  # Adds the rolled number to the total
        if operator is not '':  # Checks for an operator
            if operator is '/' and int(mod) == 0:  # Checks to see if it is a Divide by Zero problem
                return 'Error\nDivide by Zero'  # Returns an Error message
            else:  # There is an operator and it is not a Divide by Zero Problem
                operators = {  # Dictionary used to avoid an if then chain, by setting the operators to the key and
                    '+': int(total) + int(mod),  # calculating in the dictionary itself
                    '-': int(total) - int(mod),
                    '*': int(total) * int(mod),
                    '/': int(total) / int(mod)
                }
                tmod = operators.get(operator)  # Calls the dictionary above
        else:
            tmod = ''
        if adv != 0:
            if 'd' in selection and count >0:
                adv_total = 0
                adv_rolls = []
                adv_counter = count
                while counter > 0:
                    adv_counter -= 1
                    adv_roll = random.randint(1, die)
                    adv_rolls.append(adv_roll)
                    adv_total += adv_roll  # TODO Finish advantage Rolling

        return organizer(count=count, die=die, mod=mod, operator=operator, roll=rolls, total=total, tmod=tmod)
    elif mod is not '':  # Only Math (If you look at lines 90-100 the notes would be the same
        if operator is '/' and int(mod) == 0:
            return 'Error:\nDivide by Zero'
        else:
            operators = {  # Since die is substituted for the first mod, it is used instead of total
                '+': int(die) + int(mod),
                '-': int(die) - int(mod),
                '*': int(die) * int(mod),
                '/': int(die) / int(mod)
            }
            result = operators.get(operator)

            return 'Calculating:\n{} {} {} = {}'.format(str(die), operator, str(mod), str(result))  # Returns Result
    else:
        return 'An Unknown Error has Occurred'  # Catch all error message
