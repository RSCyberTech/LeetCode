"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head!=None:
            visited=[]
            new=[]
            while True:
                try:
                    if head != None:
                        visited.append(head)
                    head=head.next
                except:
                    break
            for v in visited:
                new.append(Node(v.val))
                print(v.val)
            for r in range(len(new)-1):
                new[r].next=new[r+1]
            new[-1].next=None
            for r in new:
                print(r.next)
            for r in range(len(visited)):
                if visited[r].random == None:
                    new[r].random=None
                else:
                    new[r].random=new[visited.index(visited[r].random)]
            return new[0]
                