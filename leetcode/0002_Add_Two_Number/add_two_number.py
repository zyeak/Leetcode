# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        # dummy head
        head = curr = ListNode(None)
        while l1 or l2:
            val = carry
            
            if l1:
                val += l1.val
                l1 = l1.next
            
            if l2:
                val += l2.val
                l2 = l2.next
            
            if val >= 10:
                carry = 1
                curr.next = ListNode(val%10)
            else:
                carry = 0
                curr.next = ListNode(val)
            
        if carry != 0:
            curr.next = ListNode(carry)
            
        return head.next

# Solution 2:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
                
            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
                
            # update ptrs
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
                
        return dummy.next