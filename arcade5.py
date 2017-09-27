def makeArrayConsecutive2(statues):
    statsort = sorted(statues)
    newstats = list()
    for i in range(0,len(statsort)-1):
        missing = statsort[i+1] - statsort[i]
        for n in range(1,missing):
            newstats.append(statsort[i] + n)
    return len(newstats)

statues = [6, 2, 3, 8]

print makeArrayConsecutive2(statues)