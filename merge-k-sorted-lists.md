Merge k Sorted Lists
=====================

> Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Naive Solution
---------------

*Note*: Could not pass any huge test cases, but still it's a simple solution.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if not lists:
            return None
        res = lists[0]
        for nodes in lists[1:]:
            res = self.mergeTwoLists(res, nodes)
        return res
    
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        
        return dummy.next
```

Solution
-----------

