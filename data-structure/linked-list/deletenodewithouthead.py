

class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextnode=None



def deleteNodeWithoutHead(position):
    if position==None or position.nextnode==None:
        return False
    position.data = position.nextnode.data
    position.nextnode=position.nextnode.nextnode

    return position.data


a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
head=a
a.nextnode=b
b.nextnode=c
c.nextnode=d
print(deleteNodeWithoutHead(head.nextnode.nextnode.nextnode)) #3rd element
while a:
 print(a.data)
 a=a.nextnode