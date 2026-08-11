class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = - 2**31

        sign = -1 if x < 0 else 1
        x = abs(x)

        def helper(num: int, rev: int) -> int:
            if num == 0:
                return rev
            digit = num % 10
            if rev > (MAX_INT - digit) // 10:
                return None
            return helper(num // 10, rev * 10 + digit)

        result = helper(x, 0)
        if result is None:
            return 0

        result *= sign
        if result > MAX_INT or result < MIN_INT:
            return 0

        return result
        