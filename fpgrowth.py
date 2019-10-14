from linkedList import Linkedlist

def findFreqItems(tree, D1, min_sup, emptySet, freqItemList):
    orderedTuple = sorted(D1.items(), key=lambda kv: kv[0], reverse=True)
    orderedList = list()
    for tup in orderedTuple:
        orderedList.append(tup[0])
    for item in orderedList: # for every frequent item
        temSet = set(emptySet)
        temSet.add(item)
        freqItemList.append(temSet)
        linkedList = D1[item][1]
        cPB = dict()
        while linkedList != None:
            path_to_node = list()
            temLinkedList = Linkedlist(linkedList.name, linkedList.count, linkedList.parent, linkedList.nodeLink)
            while temLinkedList.parent != None:
                path_to_node.append(temLinkedList.name)
                temLinkedList = temLinkedList.parent
            if len(path_to_node) > 1:
                cPB[frozenset(path_to_node[1:])] = linkedList.count
            linkedList = linkedList.nodeLink
        tree, D_new = buildTree(cPB, min_sup)     
        if tree != None or D_new != None:
            findFreqItems(tree, D_new, min_sup, temSet, freqItemList)

def buildTree(dataDict, min_sup):
    D1 = dict()
    for trans in dataDict:
        for item in trans:
            if item not in D1:
                D1[item] = dataDict[trans]
            else:
                D1[item] += dataDict[trans]
    for item in list(D1):
        if D1[item] < min_sup:
            del(D1[item])           
    if len(D1) > 0:    
        for item in D1:
            D1[item] = [D1[item], None]
        startTree = Linkedlist('null')
        L1 = set(D1) #create set for frequent items
        for trans, count in dataDict.items():
            temDict = dict()
            for item in trans:
                if item in L1: #filter based on min_sup
                    temDict[item] = D1[item][0]
            if len(temDict) > 0:
                #sort the frequent item by descending order
                orderedTuple = sorted(temDict.items(), key=lambda kv: kv[0], reverse=True)
                orderedList = list()
                for tup in orderedTuple:
                    orderedList.append(tup[0])
                updateTree(orderedList, startTree, D1, count)
        return startTree, D1
    else:
        return None, None

def updateTree(Dk, tree, D1, count):
    if Dk[0] not in tree.children: #create a new branch
        tree.children[Dk[0]] = Linkedlist(Dk[0], count, tree)
        if D1[Dk[0]][1] == None:
            D1[Dk[0]][1] = tree.children[Dk[0]]
        else:
            addPointer(D1[Dk[0]][1], tree.children[Dk[0]])       
    else:   
        tree.children[Dk[0]].addCount(count)
        
    if len(Dk) > 1:
        updateTree(Dk[1::], tree.children[Dk[0]], D1, count)

def addPointer(currentNode, targetNode):
    while True:
        if currentNode.nodeLink == None:
            break
        else:
            currentNode = currentNode.nodeLink
    currentNode.nodeLink = targetNode

