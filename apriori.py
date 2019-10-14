from itertools import combinations

def apriori_gen(Lk, k):
    Ck = list()
    for l1 in Lk:
        for l2 in Lk:
            if len(l2 - l1) == 1:
                c = l1.union(l2)
                if has_infrequent_subset(c, Lk, k): 
                    continue
                elif c not in Ck:
                    Ck.append(c)
    return Ck

def createDict(Ck, database):
    cDict = {}
    for line in database:
        for c in Ck:            
                if c.issubset(line):
                    fc = frozenset(c)
                    if fc not in cDict:
                        cDict[fc] = 1
                    else:
                        cDict[fc] += 1
    return cDict

def createDict_improved(Ck, transDict):
    cDict = {}
    for trans in transDict:
        for c in Ck:            
                if c.issubset(trans):
                    fc = frozenset(c)
                    if fc not in cDict:
                        cDict[fc] = transDict[trans]
                    else:
                        cDict[fc] += transDict[trans]
    return cDict

def has_infrequent_subset(c, Lk, k):
    subSetList = list()
    for subtuple in combinations(c, k-1):
        subset = set(subtuple)
        subSetList.append(subset)
    for subset in subSetList:
        if subset not in Lk:
            return True
    return False


