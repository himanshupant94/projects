class Node(object):
    def __init__(self,value=None):
        self.value=value
        self.nextnode=None


def mergeSortedList(list1,list2):
    dummy=Node()
    tail=dummy

    while list1 and list2:
        if list1.value<list2.value:
            tail.nextnode=list1
            list1=list1.nextnode
        else:
            tail.nextnode=list2
            list2=list2.nextnode
        tail=tail.nextnode

        if list1:
            tail.nextnode=list1
        else:
            tail.nextnode=list2


    return dummy

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
head=a
a.nextnode=b
b.nextnode=c
c.nextnode=d

e=Node(2)
f=Node(3)
g=Node(5)
e.nextnode=f
f.nextnode=g
#g.nextnode=d
dummy=mergeSortedList(a,e)

while dummy:
    print(dummy.value)
    dummy=dummy.nextnode










