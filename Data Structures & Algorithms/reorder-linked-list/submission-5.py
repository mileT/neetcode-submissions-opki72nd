# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        mid = self.findMid(head)
        secondHead = self.reverseList(mid)
        self.mergeLists(head, secondHead)

    def findMid(self, head):
        slow, fast = head, head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        if pre:
            pre.next = None
        return slow

    def reverseList(self, head: Optional[ListNode]):
        if not head or not head.next:
            return head

        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return newHead

    def mergeLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            next1 = list1.next
            next2 = list2.next

            tail.next = list1
            tail = tail.next
            tail.next = list2
            tail = tail.next

            list1 = next1
            list2 = next2

        if  list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next