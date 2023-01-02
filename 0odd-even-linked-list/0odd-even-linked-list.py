# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index=0
        odd=[]
        even=[]
        while True:
            if head != None:
                if index%2==0:
                    odd.append(head)
                else:
                    even.append(head)
                if head.next != None:
                    head=head.next
                    index+=1
                else:
                    break
            else:
                break
        if len(odd):
            for r in range(len(odd)-1):
                odd[r].next=odd[r+1]
        if len(even):
            odd[-1].next=even[0]
            for r in range(len(even)-1):
                even[r].next=even[r+1]
            even[-1].next=None
        else:
            if len(odd):
                odd[-1].next=None
        if len(odd):
            return odd[0]