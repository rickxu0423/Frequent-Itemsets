class Bin_check:
    
    def equalWidthBin(self, minNum, gap, data, binList):
        maxNum = minNum + gap -1
        binCounter = 0
        temList = list()
        temList.append(minNum)
        temList.append(maxNum)
        temList.append(binCounter)
        data.sort()

        for i in range(len(data)):
            if i == len(data) - 1  :
                binList.append(temList)  
            if data[i] < minNum:
                continue
            elif minNum <= data[i] <= maxNum:
                temList[2] += 1        
            else:
                binList.append(temList)
                self.equalWidthBin(minNum+gap, gap, data[i:], binList)
                break

        return binList

    def stratifiedBin(self, stratifiedList, data, binList):
        minNum = stratifiedList[0]
        maxNum = stratifiedList[1]
        binCounter = 0
        temList = list()
        temList.append(minNum)
        temList.append(maxNum)
        temList.append(binCounter)
        data.sort()
        for i in range(len(data)):
            if i >= len(data) - 1  :
                binList.append(temList)  
            if data[i] < minNum:
                continue
            elif minNum <= data[i] <= maxNum:
                temList[2] += 1        
            else:
                binList.append(temList)
                stratifiedList.pop(0)
                stratifiedList.pop(0)
                self.stratifiedBin(stratifiedList, data[i:], binList)
                break

        return binList