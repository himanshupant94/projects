class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def insertatlast(value, head):
    newnode = Node(value)
    last = head
    while last.nextnode:
        last = last.nextnode
        #print(last.value)
    last.nextnode=newnode
    return head


a = Node(1)
b = Node(2)
c = Node(3)
head = a
a.nextnode = b
b.nextnode = c
head = insertatlast(4, head)
while head:
    print(head.value)
    head = head.nextnode

