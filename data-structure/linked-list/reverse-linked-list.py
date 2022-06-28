

class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextnode=None



def reverseList(head):
    currentNode=head
    prevNode=None
    nextnode=None

    while currentNode:
        nextnode=currentNode.nextnode
        currentNode.nextnode=prevNode
        prevNode=currentNode
        currentNode=nextnode

    return prevNode

a=Node(1)
b=Node(2)
c=Node(3)
a.nextnode=b
b.nextnode=c

print(reverseList(a).data)
print(c.nextnode.data)

