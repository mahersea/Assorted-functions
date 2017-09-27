a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
def rotateImage(a):
    rotated90 = zip(*a[::-1])
    return rotated90
print rotateImage(a)
