



class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextnode=None


def cycle_check(Node):
    marker1=Node
    marker2=Node

    while marker2 != None and marker2.nextnode!=None:
        marker1=marker1.nextnode
        marker2=marker2.nextnode.nextnode

        if marker1==marker2:
            print(marker1.data)
            return True
    return False


a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=b

print(cycle_check(a))
