# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        items=[]
        while True:
            try:
                items.append(head.val)
                head=head.next
            except:
                break
        if len(items) < 2:
            return True
        if len(items)%2 == 0:
            firstHalf=items[:int(len(items)/2)]
            secondHalfReversed=list(reversed(items[int(len(items)/2):]))
        else:
            firstHalf=items[:int(len(items)/2)]
            secondHalfReversed=list(reversed(items[int(len(items)/2)+1:]))
            print(len(items))
        print(firstHalf)
        print(secondHalfReversed)
        return firstHalf==secondHalfReversed