class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        self.items.pop()
    def size(self):
        print(len(self.items))
    def isEmpty(self):
        print(self.items==[])
    def peak(self):
        print(self.items[0])

q=Queue()
q.isEmpty()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.items)
q.peak()





