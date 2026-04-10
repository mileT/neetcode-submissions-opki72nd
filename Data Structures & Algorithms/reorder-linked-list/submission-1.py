# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # find the first node of second half in the linkedlist
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        second = self.reverseList(slow)

        first = head
        while first:
            first_next, second_next = first.next, second.next
            first.next = second
            if not first_next or not second_next:
                break

            second.next = first_next
            first = first_next
            second = second_next
        

    def reverseList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        prev, cur = None, head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        return prev
        