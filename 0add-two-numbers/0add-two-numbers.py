# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        li1=[]
        li2=[]
        while True:
            try:
                li1.append(l1.val)
                l1=l1.next
            except:
                break
        while True:
            try:
                li2.append(l2.val)
                l2=l2.next
            except:
                break
        print(li1)
        print(li2)
        totalList=[]
        for l in li1:
            totalList.append(l)
        for r in range(len(li2)):
            if r >= len(totalList):
                totalList.append(li2[r])
            else:
                totalList[r]+=li2[r]
        print(totalList)
        
        for r in range(len(totalList)):
            if totalList[r] > 9:
                try:
                    if r==len(totalList)-1 and totalList[-1]>9:
                        totalList.append(0)
                    totalList[r+1]+=int((totalList[r]-totalList[r]%10)/10)
                except:
                    break
                totalList[r]=totalList[r]%10
        print(totalList)
        totalList[-1]=ListNode(totalList[-1])
        for r in range(len(totalList)-2,-1,-1):
            totalList[r]=ListNode(totalList[r],totalList[r+1])
        return totalList[0]