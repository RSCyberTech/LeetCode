# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while True:
            if head != None:
                if head.val == val:
                    if head.next != None:
                        head=head.next
                    else:
                        head=None
                        break
                else:
                    break
            else:
                break

        original = head

        while True:
            if head != None:
                if head.next != None:
                    if head.next.val==val:
                        if head.next.next:
                            head.next=head.next.next
                        else:
                            head.next=None
                    else:
                        head=head.next
                else:
                    break
            else:
                break

        return original
