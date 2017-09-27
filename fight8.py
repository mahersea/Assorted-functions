crypt = ["SEND", "MORE", "MONEY"]

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]

crypt = ["TEN", "TWO", "ONE"]

solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]

crypt = ["A", "A", "A"]
solution = [["A","0"]]

def isCryptSolution(crypt, solution):
    testseq = []
    total = ""
    test = 2
    for i in crypt:
        for n in range(len(i)):
            for j in solution:
                if i[n] == j[0]:
                    total += j[1]
        testseq.append(total)
        total = ""
    if int(testseq[0]) + int(testseq[1]) == int(testseq[2]):
        test = 0
    if len(testseq[0]) > 1 and testseq[0][0] == "0":
        test = 1
    if len(testseq[1]) > 1 and testseq[1][0] == "0":
        test = 1
    if len(testseq[2]) > 1 and testseq[2][0] == "0":
        test = 1

    if test == 0:
        return True
    elif test == 1:
        return False
    else:
        return False

print isCryptSolution(crypt, solution)