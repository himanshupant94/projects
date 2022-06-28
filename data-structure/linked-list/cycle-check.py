



class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextnode=None


def cycle_check(Node):
    temp=Node
    count=0
    while Node!=None and Node.nextnode!=None:
        if temp==Node.nextnode:
            print(Node.nextnode.data)
            return True
        else:
            count+=1
            print(count)
            Node=Node.nextnode
    return False


a=Node(1)
b=Node(2)
c=Node(3)

a.nextnode=b
b.nextnode=c
c.nextnode=None

print(cycle_check(a))





