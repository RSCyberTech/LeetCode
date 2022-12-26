class MyLinkedList:
    
    def __init__(self):
        self.size=0
        self.head=None

    def get(self, index: int) -> int:
        node=self.head
        i=0
        if node != None:
            if index==0:
                return node.val
            while node.next:
                node=node.next
                i+=1
                if i==index:
                    return node.val
            return -1
        else:
            return -1
        
    def addAtHead(self, val: int) -> None:
        node=Node(val)
        if node != None:
            node.next=self.head
            self.head=node
        else:
            self.head=node        
        self.size+=1
        
    def addAtTail(self, val: int) -> None:
        node=Node(val)
        head=self.head
        if head:
            while head.next:
                head=head.next
                
            head.next=node
        else:
            self.addAtHead(val)
        self.size+=1
        
    def addAtIndex(self, index: int, val: int) -> None:
        node=Node(val)
        head=self.head
        if index==self.size:
            self.addAtTail(val)
        elif index>self.size:
            pass
        elif self.head == None:
            self.head=node
            self.size+=1
        elif index==0:
            self.addAtHead(val)
        elif index==1:
            node.next=self.head.next
            self.head.next=node
            self.size+=1
        else:
            i=0
            while head.next:
                head=head.next
                i+=1
                if i==index-1:
                    break
            node.next=head.next
            head.next=node
            self.size+=1
            
    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            if index==0:
                if self.size>1:
                    self.head=self.head.next
                else:
                    self.head=None
            elif index==1:
                if self.size>2:
                    self.head.next=self.head.next.next
                else:
                    self.head.next=None
            else:
                head=self.head
                i=0
                while head.next:
                    head=head.next
                    i+=1
                    if i==index-1:
                        if index==self.size-1:
                            head.next=None
                        else:
                            head.next=head.next.next
            self.size -=1
            
class Node:
    
    def __init__(self, value):
        self.val=value
        self.next=None
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
        