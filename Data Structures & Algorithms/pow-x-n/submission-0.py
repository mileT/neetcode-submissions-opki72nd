class Solution:
    def myPow(self, x: float, n: int) -> float:

        def powHelper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
                
            if n % 2 == 0:
                half = powHelper(x, n // 2)
                return half * half
            else:
                half = powHelper(x, n // 2)
                return half * half * x

        if x == 0:
            return 0
        if n == 0:
            return 1
        if n > 0:
            return powHelper(x, n)
        else:
            return 1 / powHelper(x, -n)

        
        