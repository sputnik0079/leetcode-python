Linked List Cycle II 
=====================

> Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

> Follow up:

> Can you solve it without using extra space?

Solution
---------

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                fast = head
                while slow is not fast:
                    slow, fast = slow.next, fast.next
                return fast

        return None
```
