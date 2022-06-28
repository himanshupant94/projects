class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def size(self):
        print(len(self.items))
    def isEmpty(self):
        print(self.items==[])
    def peak(self):
        print(self.items[-1])

s=stack()
s.isEmpty()
s.push(3)
s.push(2)
s.push("a")
s.pop()
s.size()
s.isEmpty()
s.peak()




