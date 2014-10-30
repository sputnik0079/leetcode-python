Anagrams
========

> Given an array of strings, return all groups of strings that are anagrams.

> Note: All inputs will be in lower-case.

Solution
---------

```python
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        if not strs:
            return None
        table = {}
        for str in strs:
            key = ('').join(sorted(str))
            if key in table:
                table[key].append(str)
            else:
                table[key] = [str]
        res = []
        for anagrams in table.values():
            if len(anagrams) > 1:
                res.extend(anagrams)
        return res
```
