class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def insertatfirst(value, head):
    newnode = Node(value)
    newnode.nextnode = head
    head = newnode
    return head


a = Node(1)
b = Node(2)
c = Node(3)
head = a
a.nextnode = b
b.nextnode = c
head = insertatfirst(4, head)
temp=head
while temp:
    print(temp.value)
    temp = temp.nextnode
