class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        currA, currB = headA, headB
        
        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
        
        return currA  # either currA or currB, both will be the intersection node or None
