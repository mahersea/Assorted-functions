# area of elements in a 2d grid

def shapeArea(n):
    total = 1
    for i in range(1,n+1):
        total = total + (4 * (i-1))
        print total
    return total

n = 1
n = 2
n = 3
n = 4
n = 5
n = 6

print shapeArea(n)