import regex
import requests


#  function to check if word contains ie or ei at all, then see if it follows the rule format & add to fail list if not
def rule_check(word_list):
    fail_list = []
    for word in word_list:
        if regex.search(r'(ei)|(ie)', word):
            if regex.search(r'c(ei)', word):
                continue
            elif regex.search(r'c(ie)|(ei)', word):
                fail_list.append(word)
    return fail_list


#  function to download enable1.txt
def get_text():
    r = requests.get('https://norvig.com/ngrams/enable1.txt', stream=True)
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            open('enable1.txt', 'wb').write(r.content)


#  function to ask user if they need to download enable1.txt or not
def download():
    print("\nDo you need to download 'enable1.txt'? Yes or no")
    choice = input(">> ").lower()
    if 'yes' in choice:
        get_text()
        print("'enable1.txt' should now be available locally\n")
    elif 'no' in choice:
        print("Assuming you already have 'enable1.txt' then...\n")
    else:
        print("Sorry, I'm not sure what '", choice, "' means...")
        download()


#  run download() then read enable1 text file, add each line into a list with no \n, then close the file
download()
enable_1 = [w.replace('\n', '') for w in open('enable1.txt', 'r').readlines()]
open('digital number challenges.txt', 'r').close()

#  short test lists
pass_words = ['fiery', 'hierarchy', 'hieroglyphic', 'ceiling', 'inconceivable',
              'receipt', 'daily', 'programmer', 'one', 'two', 'three']
exceptions = ['sleigh', 'stein', 'fahrenheit', 'deifies', 'either',
              'nuclei', 'reimburse', 'ancient', 'juicier', 'societies']

#  using rule_check function on test lists & enable_1 to get lists of failures & their sizes
check_1 = rule_check(pass_words)
check_2 = rule_check(exceptions)
check_3 = rule_check(enable_1)
print("Failures: ", check_1, "\nSize: ", len(check_1))
print("Failures: ", check_2, "\nSize: ", len(check_2))
print("Failures: ", check_3, "\nSize: ", len(check_3))
