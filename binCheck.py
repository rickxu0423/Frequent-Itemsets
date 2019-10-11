from binClass import Bin_check
from binApply import Bin_apply

try:
    #fhand = open("adult.test")
    fhand = open("adult.data")
except:
    print('File cannot be open:', "adult.data")
    quit()

attrDict = dict()
giantList = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]    #initialize giantList

for line in fhand:  #read the data file
    attrs = line.replace(",", "").replace(".", "").split()
    attrs.pop(2)    #get rid of "fnlwgt"
    attrs.pop(3)    #get rid of "euducation-num"
    for i in range(len(attrs)):
        giantList[i].append(attrs[i])

for i in [0, 8, 9, 10]:
    giantList[i] = [ int(x) for x in giantList[i] ] #string to int prepared for binning
ageBin = Bin_check().equalWidthBin(11, 10, giantList[0], []) #bin the age
capitalGainBin = Bin_check().stratifiedBin([0, 0, 1, 99998, 99999, 99999], giantList[8], []) #bin the capital-gain
capitalLossBin = Bin_check().stratifiedBin([0, 0, 1, 99999], giantList[9], []) #bin the capital-loss
workHourBin = Bin_check().stratifiedBin([0, 0, 1, 34, 35, 40, 41, 104], giantList[10], [])    #bin the hours-per-week
for i in [0, 8, 9, 10]:
    if i == 0: model = ageBin
    elif i == 8: model = capitalGainBin
    elif i == 9 : model = capitalLossBin
    else: model = workHourBin
    giantList[i] = Bin_apply(giantList[i], model).generalApply(i)

nameList = ["age", "workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "label"]
for i in range(len(giantList)):
    for attr in giantList[i]:
        if attr not in attrDict:
            attrDict[attr] = 1
        else:
            attrDict[attr] += 1
print(attrDict)