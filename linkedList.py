class Linkedlist:
    def __init__(self, name, count=1, parent=None, nodeLink=None):
        self.name = name
        self.count = count
        self.nodeLink = nodeLink
        self.parent = parent
        self.children = {}
    
    def addCount(self, count):
        self.count += count