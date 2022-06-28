

class Queue2Stacks:
    def __init__(self):
        self.instack=[]
        self.outstack=[]
    def enque(self,item):
        self.instack.append(item)

    def deque(self):
        if self.outstack==[]:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

q=Queue2Stacks()
q.enque(3)
q.enque(5)
q.enque(6)
q.deque()
q.deque()
print(q.outstack)