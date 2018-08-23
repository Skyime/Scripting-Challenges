import re
import operator
from textwrap import dedent
from sys import exit

scorers = 'abcde'
scores = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}


#  function to convert upper and lower case forms of a letter into a positive or negative point, and give the sum
def score_convert(letter, to_score):
    score = []
    total = 0
    letters = '[' + letter + letter.upper() + ']'
    [score.append(-1) for x in re.findall(letters, to_score) if x.isupper()]
    [score.append(1) for y in re.findall(letters, to_score) if y.islower()]
    for each in score:
        total += each
    return total


#  function to see if user would like to keep tally again or not, and restart if so.
def again():
    print("\nWould you like to score again? Yes or no?")
    choice = input('>>  ').lower()
    if 'yes' in choice:
        tally_program()
    elif 'no' in choice:
        print("Quitting!")
        exit(0)
    else:
        print("Sorry, I don't know what '", choice, "' means...")
        again()


#  function to acquire user input score tally, and print out the resulting scores in order, winner first
def tally_program():
    print("Enter your tally below:")
    tally = input(">>  ")
    print("\nCalculating scores...\n")
    for char in scorers:
        scores[char] = score_convert(char, tally)
    result = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    for z in result:
        print(z)
    again()


print(dedent("""
    Welcome to Tally-Scorer!

    You may have up to 5 players, each assigned to a letter from 'a b c d e'
    Whenever someone's score increases by a point, type their letter in lowercase.
    When their score decreases by a point, type their letter in uppercase.
    Don't press enter until you're finished scoring!

    """))
tally_program()
