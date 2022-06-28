class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def insertatposition(value, givennode):
    newnode = Node(value)
    newnode.nextnode=givennode.nextnode
    givennode.nextnode = newnode

a = Node(1)
b = Node(2)
c = Node(3)
head = a
a.nextnode = b
b.nextnode = c
insertatposition(4, head.nextnode)
temp=head
while temp:
    print(temp.value)
    temp = temp.nextnode

