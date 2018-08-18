import string
import pandas as pd
import numpy as np
from itertools import cycle
from sys import exit

alpha_array = np.empty(shape=(26, 26), dtype=str)
alpha_list = list(string.ascii_lowercase)
n = 0
new_list = []

for each in range(0, 26):
    new_list = alpha_list[n:] + alpha_list[0:n]
    n += 1
    alpha_array[each] = new_list

alpha_df = pd.DataFrame(data=alpha_array, index=list(string.ascii_uppercase), columns=list(string.ascii_uppercase))


def quits():
    print("Quitting...")
    exit(0)


def cipher_interface():
    print("Do you want to decode, encode, or quit?")
    choice = input('>>  ')

    if choice == 'encode':

        en_result = ''
        encode_key = ''

        print("What is the codeword?")
        en_word = input('>>  ').upper()
        encode_cycle = cycle(en_word)

        print("What is the message to be encoded?")
        en_message = input('>>  ').upper()
        en_message_key = ''.join(e for e in en_message if e.isalnum())

        while len(encode_key) != len(en_message_key):
            encode_key += next(encode_cycle)

        for e, m in zip(encode_key, en_message_key):
            en_result += alpha_df.loc[e, m]

        print("\nYour encoded message is: \n\t", en_result, '\n')
        print("Would you like to do something else, yes or no?")
        choice_en = input('>>  ')

        if 'yes' in choice_en:
            cipher_interface()
        elif 'no' in choice_en:
            quits()
        else:
            print("I'll take that as a no...")
            quits()

    elif choice == 'decode':

        de_result = ''
        decode_key = ''

        print("What is the codeword?")
        de_word = input('>>  ').upper()
        decode_cycle = cycle(de_word)

        print("What is the message to be decoded?")
        de_message = input('>>  ')
        de_message_key = ''.join(e for e in de_message if e.isalnum())

        while len(decode_key) != len(de_message_key):
            decode_key += next(decode_cycle)

        for d, m in zip(decode_key, de_message_key):
            de_result += alpha_df[alpha_df[d] == m].index[0]

        print("\nYour decoded message is: \n\t", de_result.lower(), '\n')
        print("Would you like to do something else, yes or no?")
        choice_de = input('>>  ')

        if 'yes' in choice_de:
            cipher_interface()
        elif 'no' in choice_de:
            quits()
        else:
            print("I'll take that as a no...")
            quits()

    elif choice == 'quit':
        quits()

    else:
        print("Sorry, I don't understand '", input, "', please try again.")
        cipher_interface()


cipher_interface()
