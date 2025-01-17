# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        head2 = prev

        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        
        return True

            