"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head and head!=None:
            toReturn=head
            visited=[]
            visited.append({insertVal:Node(insertVal)})
            while True:
                try:
                    if {head.val:head} not in visited:
                        visited.append({head.val:head})
                        head=head.next
                        print(head.val)
                    else:
                        break
                except:
                    break
            print([list(x.keys())[0] for x in visited])
            print( list(visited[0].values())[0].val )
            visited=sorted(visited,key=lambda x:list(x.keys())[0])
            for v in visited:
                print(v)
            for r in range(len(visited)-1):
                print(r)
                list(visited[r].values())[0].next=list(visited[r+1].values())[0]
            list(visited[-1].values())[0].next=list(visited[0].values())[0]
            return toReturn
        elif insertVal!=None:
            newNode=Node(insertVal)
            newNode.next=newNode
            return newNode