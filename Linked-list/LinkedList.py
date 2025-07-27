class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        
class List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_front(self,val):
        node = Node(val)
        if self.head==None:
            self.head=self.tail=Node
        else:
            node.next = self.head
            self.head = node
            