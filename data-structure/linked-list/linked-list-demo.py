
class Node:
    def __init__(self,data):
        self.data=data
        self.next= None


class LinkedList:
    def __int__(self):
        self.head=None

if __name__=='__main__':
    llist=LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    llist.next=second
    second.next=third

    print(llist.head.data)
    print(llist.next.data)
    print(second.next.data)







