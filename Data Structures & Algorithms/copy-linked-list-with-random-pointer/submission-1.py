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
        hashmap = collections.defaultdict(lambda: Node(0))
        hashmap[None] = None
        cur = head

        while cur:
            clone = hashmap[cur]
            clone.val = cur.val
            clone.next = hashmap[cur.next]
            clone.random = hashmap[cur.random]
            cur = cur.next
        
        return hashmap.get(head)
        