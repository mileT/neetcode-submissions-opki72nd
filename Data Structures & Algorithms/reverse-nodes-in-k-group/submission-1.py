# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth_node = self.getKthNode(group_prev, k)
            if not kth_node:
                break
            group_next = kth_node.next
        
            prev, cur = kth_node.next, group_prev.next
            while cur != group_next:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            next_group_prev = group_prev.next
            group_prev.next = kth_node
            group_prev = next_group_prev

        return dummy.next

    def getKthNode(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
        