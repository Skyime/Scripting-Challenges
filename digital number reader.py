#  conversion list
numbers = [
    ' _ | ||_|',
    '     |  |',
    ' _  _||_ ',
    ' _  _| _|',
    '   |_|  |',
    ' _ |_  _|',
    ' _ |_ |_|',
    ' _   |  |',
    ' _ |_||_|',
    ' _ |_| _|'
    ]

#  read challenge text file, add each line into a list with no \n, then close the file
chall_text = [w.replace('\n', '') for w in open('digital number challenges.txt', 'r').readlines()]
open('digital number challenges.txt', 'r').close()

#  take characters for single digit over its 3 lines, add them in their own order as a string similar to conversion list
lines_ordered = ''
for i_0 in range(0, 10, 3):
    for i_1 in range(0, 25, 3):
        for i_2 in range(0, 3):
            lines_ordered += chall_text[i_0:(i_0 + 3)][i_2][i_1:(i_1 + 3)]

#  check each digit's characters against the conversion list and output as an integer number
results = []
for i_3 in range(0, 316, 9):
    [results.append(numbers.index(each)) for each in numbers if lines_ordered[i_3:(i_3 + 9)] == each]
for ind in range(1, 29, 9):
        print("Challenge {}: ".format(int((ind / 9) + 1)), ''.join(map(str, (results[(ind - 1):(ind + 8)]))))
