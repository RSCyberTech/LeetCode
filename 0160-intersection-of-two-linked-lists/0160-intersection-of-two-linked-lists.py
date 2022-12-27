# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return
                
        visited=set()
        
        a=True
        b=True
        
        while a==True or b==True:
            if a==True:
                try:
                    if headA not in visited:
                        visited.add(headA)
                    else:
                        return headA
                    headA=headA.next
                except:
                    a=False
            if b==True:
                try:
                    if headB not in visited:
                        visited.add(headB)
                    else:
                        return headB
                    headB=headB.next
                except:
                    b=False