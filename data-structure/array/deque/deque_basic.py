class Deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        print(self.items.pop())
    def removeRear(self):
        print(self.items.pop(0))


d=Deque()
d.addFront(3)
d.addRear(1)
d.removeFront()
d.removeRear()
print(d.items)


