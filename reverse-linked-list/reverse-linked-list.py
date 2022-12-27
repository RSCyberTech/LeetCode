# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        elif head.next == None:
            return head
        else:
            newOrder=[]
            pointer=head
            while True:
                try:
                    if pointer != None:
                        newOrder.insert(0,pointer)
                    pointer=pointer.next
                except:
                    break
            for r in range(len(newOrder)-1):
                newOrder[r].next=newOrder[r+1]
            newOrder[-1].next=None
            return newOrder[0]