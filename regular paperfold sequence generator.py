paper = [[1]]


#  function to apply a step in the paper-fold sequence, which takes the previous step, adds a 1 to the end, then adds
#  the previous step in reverse order, with 1s and 0s switched.
def fold():
    a = list(paper[-1])
    b = ''.join(str(each) for each in a) + '1' + ''.join([str(1 - each) for each in reversed(a)])
    c = [int(each) for each in b]
    return c


#  user input and while loop to go through each step in the paper-fold sequence as many times as desired.
print('How many paper-fold steps would you like to go through?')
folds_to_do = int(input('>> '))
print(paper)
i = 0
while i < folds_to_do:
    paper.append(list(fold()))
    print(paper)
    i += 1
