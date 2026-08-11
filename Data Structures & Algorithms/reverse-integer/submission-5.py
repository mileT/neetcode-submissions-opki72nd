class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0
        while x != 0:
            digit = x % 10
            if result > (MAX_INT - digit) // 10:
                return 0
            result = result * 10 + digit
            x //= 10

        result *= sign
        if result > MAX_INT or result < MIN_INT:
            return 0

        return result        