import fpgrowth 
import apriori
from time import time
from replace import Replace

try:
    fhand = open("adult.data")
    #fhand = open("adult.data")
except:
    print('File cannot be open:', "adult.data")
    quit()

while True:
    print("1: Apriori")
    print("2: FP-Growth")
    model = input("Choose a model for analysis(1 or 2): ")
    if not model:
        continue
    elif model == "1" or model == "2":
        model = int(model)
        break
    else:
        print("Please either input 1 or 2!")

while True:
    min_sup = input("Enter minimum support(1-30000, recommend 8000): ")
    if not min_sup:
        continue
    elif 1 <= int(min_sup) <= 30000:
        min_sup = int(min_sup)
        break
    else:
        print("Please input a number between 1 and 30000!")

database = []
for line in fhand:  #read the data file
    attrs = line.replace(",", "").replace(".", "").split()
    attrs.pop(2)    #get rid of "fnlwgt"
    attrs.pop(3)    #get rid of "euducation-num"
    for i in [0, 8, 9, 10]: 
        attrs[i] = int(attrs[i])
        attrs[i] = Replace(attrs[i]).replace(i)
    attrSet = set(attrs)
    if '?' in attrSet:
        attrSet.remove('?')
    database.append(attrSet)

print("Calculating frequent itemsets")
t = time()

#Apriori
if model == 1:
    attrDict = dict()
    for line in database:
        for attr in line:
            if attr not in attrDict:
                attrDict[attr] = 1
            else:
                attrDict[attr] += 1

    L1 = list()
    temSet = set()
    for attr in attrDict:
        if attrDict[attr] >= min_sup:
            temSet.add(attr)
            L1.append(temSet)
            temSet = set()

    Lk = list(L1)
    L_all = list(L1)
    k = 2
    while len(Lk) > 0:
        Ck = apriori.apriori_gen(Lk, k)
        Lk = list()
        cDict = apriori.createDict(Ck, database)
        for c in Ck:
            key = frozenset(c)
            if key in cDict and cDict[key] >= min_sup:
                Lk.append(c)
        k += 1
        L_all += Lk

    for itemsets in L_all:
        print(itemsets)
    print(len(L_all))
    print("Calculated in %.1fs" % (time() - t))

#FP-growth
else:
    transDict = dict()
    for trans in database:
        temSet = frozenset(trans)
        if temSet not in transDict:
            transDict[temSet] = 1
        else:
            transDict[temSet] += 1
    tree, D1 = fpgrowth.buildTree(transDict, min_sup)
    freqItemList = []
    fpgrowth.findFreqItems(tree, D1, min_sup, [], freqItemList)
    for x in freqItemList:
        print(x)
    print(len(freqItemList))
    print("Calculated in %.1fs" % (time() - t))

