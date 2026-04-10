# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kthNode = self.getKthNode(groupPrev, k)
            if not kthNode:
                break
            groupNext = kthNode.next

            prev, cur = kthNode.next, groupPrev.next
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp

        return dummy.next

    def getKthNode(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
        