# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=[]
        if head:
            while head.next:
                visited.append(id(head))
                head=head.next
                if id(head) in visited:
                    return True
        return False