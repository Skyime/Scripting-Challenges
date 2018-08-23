from random import randint
from textwrap import dedent
import re
from sys import exit


#  function to calculate individual dice roll results
def dice_roll(num, size):
    rolls = []
    total = 0
    for each in range(0, int(num)):
        rolls.append(randint(1, int(size)))
    for each in rolls:
        total += each
    print("Rolls: ", rolls, "Total: ", total)
    return total


# function to add/subtract final dice roll results
def calculate(calc, num):
    total = num[0]
    if len(calc) == 1:
        if '+' in calc[0]:
            total += num[1]
        elif '-' in calc[0]:
            total -= num[1]
    elif len(calc) == 2:
        if '+' in calc[0] and '+' in calc[1]:
            total += (num[1] + num[2])
        elif '-' in calc[0] and '-' in calc[1]:
            total -= (num[1] + num[2])
        elif '+' in calc[0] and '-' in calc[1]:
            total += (num[1] - num[2])
        elif '-' in calc[0] and '+' in calc[1]:
            total += (num[2] - num[1])
    return total


#  function to restart script if input was bad somehow, and say why
def bad_roll(reason):
        print("Error : ", reason, "\nPlease use the given input format, replacing only N with a value from 1 to 999.")
        dice_interface()
        
        
#  function to check if user would like to roll again or not once finished
def roll_again():
    print("Would you like to roll again, yes or no?")
    choice = input(">> ").lower()
    if 'yes' in choice:
        dice_interface()
    elif 'no' in choice:
        print("Goodbye!")
        exit(0)
    else:
        print("Sorry, I don't know what '", choice, "' means...")
        roll_again()


#  function for user interface, input checks & to perform required operations based on input, then output result.
def dice_interface():
    print(dedent("""
        You can roll anything in the form of:
        
        NdN +/- NdN +/- NdN
        
        Replacing N as desired.
        You can add or subtract two or three simultaneous rolls,
        or just roll one e.g. 1d6
        
        What would you like to roll?
    """))
    calcs = []
    dice = input(">>> ")
    nums = []
    dice_num = []
    dice_size = []
    result = 0
    
    #  checking if input is good and assigning to relevant variables if so
    if re.match(r'[^ d\d+-]', dice):
        bad_roll('Input has bad characters...')
    elif re.match(r'\d', dice):
        if 'd' in dice:
            [dice_num.append(each) for each in re.findall(r'(\d+)d', dice)]
            [dice_size.append(each) for each in re.findall(r'(?<=d)\d+', dice)]
            if '+' and '-' in dice:
                [calcs.append(each) for each in re.findall(r'\+', dice)]
                [calcs.append(each) for each in re.findall(r'-', dice)]
            elif '+' in dice:
                [calcs.append(each) for each in re.findall(r'\+', dice)]
            elif '-' in dice:
                [calcs.append(each) for each in re.findall(r'-', dice)]
        else:
            bad_roll('You need the d...')
    else:
        bad_roll('Input has no numbers...')
        
    #  checking if too many dice/operations specified for script, or a variable has somehow got the wrong amount
    if len(dice_num) < 1 or len(dice_num) > 3:
        bad_roll('Too many or too few dice to roll...')
    elif len(dice_size) != len(dice_num):
        bad_roll('Number of types of dice to roll does not match number of multiples of dice to roll...')
    elif len(calcs) != (len(dice_num) - 1):
        bad_roll('Number of calculations do not match number of dice')

    #  rolling the dice
    print("Rolling...\n")
    if len(dice_num) == 1:
        print("First die:")
        nums.append(dice_roll(dice_num[0], dice_size[0]))
    elif len(dice_num) == 2:
        print("First die:")
        nums.append(dice_roll(dice_num[0], dice_size[0]))
        print("Second die:")
        nums.append(dice_roll(dice_num[1], dice_size[1]))
    else:
        print("First die:")
        nums.append(dice_roll(dice_num[0], dice_size[0]))
        print("Second die:")
        nums.append(dice_roll(dice_num[1], dice_size[1]))
        print("Third die:")
        nums.append(dice_roll(dice_num[2], dice_size[2]))
    
    #  adding or subtracting as asked
    if len(calcs) == 1 or len(calcs) == 2:
        result = calculate(calcs, nums)
    elif len(calcs) == 0:
        result = nums[0]
    
    #  giving a nice readable result
    if len(nums) == 1:
        print('\n', dice, " = ", result, '\n')
    elif len(nums) == 2:
        print('\n', dice, " = ", nums[0], calcs[0], nums[1], " = ", result, '\n')
    elif len(nums) == 3:
        print('\n', dice, " = ", nums[0], calcs[0], nums[1], calcs[1], nums[2], " = ", result, '\n')
        
    roll_again()


print("\nWelcome to Simple Dice Roller!\n==============================")
dice_interface()
