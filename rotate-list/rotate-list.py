# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head!=None:
            lista=[]
            while True:
                try:
                    if head not in lista and head!=None:
                        lista.append(head)
                    head=head.next
                except:
                    break
            if len(lista) <= k:
                k=k%len(lista)
            lista=list(lista[0-k:]+lista[:0-k])
            for r in range(len(lista)-1):
                lista[r].next=lista[r+1]
            lista[-1].next=None
            return lista[0]