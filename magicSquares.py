''''

-create an nxn grid based on user input
-check if the grid fits the criteria of a magic square 

'''

import random
import io

n = input("How big should the grid be?\n ")

# random nxn grid
grid = list(xrange(1, n**2 + 1))
random.shuffle(grid)

'''
# magic square for testing
n = 3
grid = [8, 1, 6, 3, 5, 7, 4, 9, 2]
'''

# print grid for testing
print grid

# the magical sum
magic = (n * (n**2 + 1)) / 2
#print magic

# function that checks if the total is magic
def check(total) :
    if total != magic :
        return False
    else :
        return True

# returns the row that is asked for through y
def getRow(y) :
    row = []
    x = (y - 1) * n
    while x != n * y :
        row.append(grid[x])
        x = 1 + x
    return row
#print getRow(1)

# returns the column that is asked for through y
def getColumn(y) :
    column = []
    column.append(grid[y-1])
    x = (y - 1) + n
    while x < y + n * (n - 1) :
         column.append(grid[x])
         x = x + n
    return column

# returns both major diagnals of the grids
def getDiagnals() :
    diagnal1 = []
    diagnal2 = []
    x = 0
    while x < n**2 :
        diagnal1.append(grid[x])
        x = x + n + 1
    x = n - 1
    while len(diagnal2) < n :
        diagnal2.append(grid[x])
        x = x + n - 1
    return diagnal1, diagnal2
#print getDiagnals()

# check if the gird is a magic square
def checkMagic() :
    for i in range(1, n+1) :
        total1 = 0
        total2 = 0
        row = getRow(i)
        column = getColumn(i)
        for i in range (0, n) :
            total1 = total1 + row[i]
            total2 = total2 + row[i]
#        print row
#        print total1
#        print column
#        print total2
        if check(total1) == False :
            return "The grid is not a magic square!"
        elif check(total2) == False :
            return "The grid is not a magic square!"
    diagnal1, diagnal2 = getDiagnals()
    total = 0
    for i in range(0, n) :
        total = total + diagnal1[i]
#    print diagnal1
#    print total
    if check(total) == False :
        return "The grid is not a magic square!"
    total = 0
    for i in range(0, n) :
        total = total + diagnal2[i]
#    print diagnal2
#    print total
    if check(total) == False :
        return "The gird is not a magic square!"

    return "It's a magic Square!"

print checkMagic()
