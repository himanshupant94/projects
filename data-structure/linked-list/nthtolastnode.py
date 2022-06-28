class node(object):
    def __init__(self,data):
        self.data=data
        self.nextnode=None

def nthtolastnode(head,n):
    left_ptr=head
    right_ptr=head

    for i in range(n-1):
        if right_ptr.nextnode==None:
            raise LookupError("n is greater than linked list")
        right_ptr=right_ptr.nextnode

    while right_ptr.nextnode:
        left_ptr=left_ptr.nextnode
        right_ptr=right_ptr.nextnode
    return left_ptr

a=node(1)
b=node(2)
c=node(3)
d=node(4)
a.nextnode=b
b.nextnode=c
c.nextnode=d
print(nthtolastnode(a,4).data)

