def nextDuplicates(a):
    key = len(a)
    nomatch=True
    for i in range(len(a)):
        match = 0
        for j in range(len(a)):
            if a[i]==a[j]:
                match+=1
            if match==2 and j<key:
                key = j
                nomatch=False
    if not nomatch:
        return key 
    else:
        return -1  


a = [2, 4, 3, 5, 1]
a = [2, 3, 3, 1, 5, 2]
a = [1]
a = [2, 2]
a = [2, 1]
a = [2, 1, 3]
print nextDuplicates(a)
