from typing import Optional

class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution():
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = tmp = ListNode()
        addval = 0
        while l1 or l2:
            val = (l1.val if l1 else 0 ) +(l2.val if l2 else 0) + addval
            tmpval, addval = val%10, val // 10
            tmp.next = ListNode(tmpval)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tmp = tmp.next
        if addval > 0:
            tmp.next = ListNode(addval)
        return head.next



