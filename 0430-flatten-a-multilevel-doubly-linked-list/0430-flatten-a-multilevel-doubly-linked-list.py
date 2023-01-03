"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        toReturn=head
        toKeep=[]
        if head != None:
            while True:
                try:
                    print(head.val)
                    if head.child and head.child != None:
                        if head.next and head.next != None:
                            toKeep.append(head.next)
                            head.next=head.child
                            head.child=None
                            head.next.prev=head
                        else:
                            head.next=head.child
                            head.child=None
                            head.next.prev=head
                        head=head.next
                    elif head.next and head.next != None:
                        head=head.next
                    elif len(toKeep) > 0:
                        head.next=toKeep[-1]
                        toKeep.pop(-1)
                        head.next.prev=head
                        head=head.next
                    else:
                        break
                except:
                    break
            return toReturn