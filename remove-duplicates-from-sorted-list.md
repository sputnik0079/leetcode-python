Remove Duplicates from Sorted List
------------------------------------

> Given a sorted linked list, delete all duplicates such that each element appear only once.

> For example,

> Given `1->1->2`, return `1->2`.

> Given `1->1->2->3->3`, return `1->2->3`.

Solution
----------

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return None
        
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
```
