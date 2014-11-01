3Sum 
-----

> Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

> Note:

> Elements in a triplet `(a,b,c)` must be in non-descending order. (ie, `a ≤ b ≤ c`)

> The solution set must not contain duplicate triplets.

  > For example, given array S = `{-1 0 1 2 -1 -4}`,

  > A solution set is:
  
  > `(-1, 0, 1)`
  > `(-1, -1, 2)`
  
Solution
---------

```python
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        result = []
        table = {}
        seen = set()
        for i, elem in enumerate(num):
            target = 0 - elem
            for n in num[i:]:
                if n in table:
                    res = sorted([elem, n, table[n]])
                    if tuple(res) not in seen():
                        seen.add(tuple(res))
                        result.append(res)
                else:
                    table[n] = target - n
        return result
```
