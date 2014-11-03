Add Two Numbers 
================

> You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

> Input: `(2 -> 4 -> 3)` + `(5 -> 6 -> 4)`

> Output: `7 -> 0 -> 8`

Solutions
------------

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        
        dummy = ListNode(-1)
        curr, carry = dummy, 0
        while l1 or l2:
            res = carry
            res += l1.val if l1 else 0
            res += l2.val if l2 else 0
            carry, res = res/10, res%10
            curr.next = ListNode(res)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
            
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next
```
