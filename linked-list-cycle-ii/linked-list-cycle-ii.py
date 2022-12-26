# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited={}
        if head:
            index=0
            while True:
                if id(head) not in visited.keys():
                    visited[id(head)]=index
                # print(visited)
                try:
                    head=head.next
                    index+=1
                except:
                    break
                if id(head) in visited.keys():
                    return head
        # return -1