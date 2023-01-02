# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lista=[]
        while True:
            try:
                if list1 != None or list2 != None:
                    if list1 != None and list2 != None:
                        if list1.val <= list2.val:
                            lista.append(list1)
                            list1=list1.next
                        elif list2.val <= list1.val:
                            lista.append(list2)
                            list2=list2.next
                    elif list1 != None:
                        lista.append(list1)
                        list1=list1.next
                    elif list2 != None:
                        lista.append(list2)
                        list2=list2.next
                        
                else:
                    break
            except:
                break
        for r in range(len(lista)-1):
            lista[r].next=lista[r+1]
        if len(lista) > 0:
            return lista[0]