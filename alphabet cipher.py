import string
import pandas as pd
import numpy as np
from itertools import cycle
from sys import exit

#  creating empty array, and a list containing every letter of the alphabet
alpha_array = np.empty(shape=(26, 26), dtype=str)
alpha_list = list(string.ascii_lowercase)
n = 0
new_list = []

#  forming the rotating alphabet sequences and adding them to the array
for each in range(0, 26):
    new_list = alpha_list[n:] + alpha_list[0:n]
    n += 1
    alpha_array[each] = new_list

#  turning the array into a dataframe with keys/column names which correspond to the codeword & message letters
alpha_df = pd.DataFrame(data=alpha_array, index=list(string.ascii_uppercase), columns=list(string.ascii_uppercase))


#  function to restart or quit based on user input
def more():
    print("Would you like to do something else, yes or no?")
        choice_m = input('>>  ').lower()

        if 'yes' in choice_m:
            cipher_interface()
        elif 'no' in choice_m:
            quits()
        else:
            print("Sorry, I don't understand '", choice_m, "', please try again.")
            more()

#  quitting function
def quits():
    print("Quitting...")
    exit(0)

#  main function to interact with user and encode/decode their messages
def cipher_interface():
    print("Do you want to decode, encode, or quit?")
    choice = input('>>  ')

    if choice == 'encode':

        en_result = ''
        encode_key = ''
        
        #  acquire codeword input and make into uppercase iterable cycle
        print("What is the codeword?")
        en_word = input('>>  ').upper()
        encode_cycle = cycle(en_word)

        #  acquire message input and make into uppercase string with no spaces
        print("What is the message to be encoded?")
        en_message = input('>>  ').upper()
        en_message_key = ''.join(e for e in en_message if e.isalnum())

        #  make the cipher key from the codeword, so that it matches the length of the message
        while len(encode_key) != len(en_message_key):
            encode_key += next(encode_cycle)

        #  acquire the resulting encoded letters from the dataframe & add to the result output
        for e, m in zip(encode_key, en_message_key):
            en_result += alpha_df.loc[e, m]

        print("\nYour encoded message is: \n\t", en_result, '\n')
        more()

    elif choice == 'decode':

        de_result = ''
        decode_key = ''

        #  acquire codeword input and make into uppercase iterable cycle
        print("What is the codeword?")
        de_word = input('>>  ').upper()
        decode_cycle = cycle(de_word)

        #  acquire message input and make into string with no spaces
        print("What is the message to be decoded?")
        de_message = input('>>  ')
        de_message_key = ''.join(e for e in de_message if e.isalnum())

        #  make the cipher key from the codeword, so that it matches the length of the message
        while len(decode_key) != len(de_message_key):
            decode_key += next(decode_cycle)

        #  acquire the resulting decoded letters from the dataframe & add to the result output
        for d, m in zip(decode_key, de_message_key):
            de_result += alpha_df[alpha_df[d] == m].index[0]

        print("\nYour decoded message is: \n\t", de_result.lower(), '\n')
        more()

    elif choice == 'quit':
        quits()

    else:
        print("Sorry, I don't understand '", choice, "', please try again.")
        cipher_interface()


cipher_interface()
