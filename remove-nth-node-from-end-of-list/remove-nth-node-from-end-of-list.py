# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head != None:
            var=head
            size=0
            nodes=[]
            while True:
                if var != None:
                    size+=1
                    nodes.append(var)
                if var.next != None:
                    var=var.next
                else:
                    break
            print(size,len(nodes))
            if n == size:
                if head.next:
                    head=head.next
                else:
                    head=None
            elif n == size-1:
                if head.next:
                    if head.next.next:
                        head.next=head.next.next
                    else:
                        head.next=None
            else:
                print(len(nodes))
                try:
                    nodes[-n-1].next=nodes[-n].next
                except:
                    nodes[-n-1].next=None
            return head