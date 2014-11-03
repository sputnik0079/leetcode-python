Pow(x, n) 
----------

> Implement `pow(x, n)`.

Solution
----------

```python
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        def p(x, n):
            value, result = x, 1
            while n:
                if n%2 != 0:
                    result *= value
                value *= value
                n /= 2
            return result
        return p(x, n) if n > 0 else 1/p(x, -n)
```
