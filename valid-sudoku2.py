
grid = [[".",".",".",".",".",".","5",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 ["9","3",".",".","2",".","4",".","."], 
 [".",".","7",".",".",".","3",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".","3","4",".",".",".","."], 
 [".",".",".",".",".","3",".",".","."], 
 [".",".",".",".",".","5","2",".","."]]

grid2 = [["2","3","9","7","4","5","1","6","8"], 
 ["4","1","6","2","8","3","7","9","5"], 
 ["5","7","8","6","9","1","3","2","4"], 
 ["9","4","2","3","5","7","6","8","1"], 
 ["1","5","3","8","6","9","2","4","7"], 
 ["8","6","7","4","1","2","9","5","3"], 
 ["7","2","4","9","3","8","5","1","6"], 
 ["6","9","1","5","7","4","8","3","2"], 
 ["3","8","5","1","2","6","4","7","9"]]

import collections
def sudoku2(grid):
    thisrow=""
    thiscol=""
    for i in grid:
        for n in range(9): 
            if i[n] != ".": 
                thisrow = "%s%s" % (thisrow,i[n])
        thisrow = str(thisrow)

        freq = collections.Counter(thisrow)
        for k in freq:
            if freq[k] > 1:
                return False
                break
        thisrow=""
    
    
    for m in range(9):
        for j in grid:
            if j[m] != ".": 
                thiscol = "%s%s" % (thiscol,j[m])
        thiscol = str(thiscol)

        freq = collections.Counter(thiscol)
        for k in freq:
            if freq[k] > 1:
                return False
                break
        thiscol=""

    def block(a,b,x,y):
        section=""
        for i in grid[a:b]:    
            for n in range(x,y):
                if i[n] != ".":
                    section = "%s%s" % (section,i[n])
        freq = collections.Counter(section)
        for k in freq:
            if freq[k] > 1:
                return False
                break
        return True

    fail = 0
    if block(0,3,0,3) == False:
        fail = 1
    if block(0,3,3,6) == False:
        fail = 1
    if block(0,3,6,9) == False:
        fail = 1
    if block(3,6,0,3) == False:
        fail = 1
    if block(3,6,3,6) == False:
        fail = 1
    if block(3,6,6,9) == False:
        fail = 1
    if block(6,9,0,3) == False:
        fail = 1
    if block(6,9,3,6) == False:
        fail = 1
    if block(6,9,6,9) == False:
        fail = 1
    
    if fail == 1:
        return False
    else:
        return True


print sudoku2(grid) 