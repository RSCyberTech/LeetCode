# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        size=0
        toCheck=head
        
        while True:
            size+=1
            if toCheck.next != None:
                toCheck = toCheck.next
            else:
                break
        
        toReturn=int(size//2+1)
                
        toCheck=head
        for r in range(toReturn-1):
            toCheck=toCheck.next
        
        return(toCheck)