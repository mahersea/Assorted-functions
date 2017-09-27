

def nextDuplicates(a):
    alreadyAdded = False
    dupl_a = dict()
    sorted_ind_a = sorted(range(len(a)), key=lambda x: a[x]) # sort incoming list but save the indexes of sorted items
    index = len(a)
    nomatch = True
    for i in xrange(len(a) - 1): # loop over indexes of sorted items
        if a[sorted_ind_a[i]] == a[sorted_ind_a[i+1]]: # if two consecutive indexes point to the same value, add it to the duplicates
            if not alreadyAdded:
                dupl_a[a[sorted_ind_a[i]]] = [sorted_ind_a[i], sorted_ind_a[i+1]]
                if sorted_ind_a[i+1] < index:
                    index = a[sorted_ind_a[i]]
                    nomatch = False
                alreadyAdded = True
            else:
                dupl_a[a[sorted_ind_a[i]]].append( sorted_ind_a[i+1] )
        else:
            alreadyAdded = False
    if not nomatch:
        return index
    else:
        return -1


a = [2, 3, 3, 1, 5, 2]
a = [2, 4, 3, 5, 1]
a = [3, 6, 3, 3, 1, 2, 5, 2]

print nextDuplicates(a)
