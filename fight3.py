def nextDuplicates(a):
    import collections
    dups = collections.defaultdict(list)
    for index, item in enumerate(a):
        dups[item].append(index)
        if len(dups[item])==2:
            return item     
            break
    return -1


a = [2, 4, 3, 5, 1]
a = [2, 1, 8, 3, 9, 3, 4, 1, 5, 2]
"""
a = [1]
a = [2, 2]
a = [2, 1]
a = [2, 1, 3]
"""
print nextDuplicates(a)
