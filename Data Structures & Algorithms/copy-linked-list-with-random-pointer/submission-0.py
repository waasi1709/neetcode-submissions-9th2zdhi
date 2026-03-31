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
        Mapz = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            Mapz[cur] = copy 
            cur = cur.next

        cur = head
        while cur:
            copy = Mapz[cur]
            copy.next = Mapz[cur.next]
            copy.random = Mapz[cur.random]
            cur = cur.next

        return Mapz[head]



        

        