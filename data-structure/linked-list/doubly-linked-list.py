class DoublyLinkedList(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        self.prevnode=None


a=DoublyLinkedList(1)
b=DoublyLinkedList(2)
c=DoublyLinkedList(3)
a.nextnode=b
b.prevnode=a
b.nextnode=c
c.prevnode=b

print(b.prevnode.value)
print(b.value)
print(b.nextnode.value)


