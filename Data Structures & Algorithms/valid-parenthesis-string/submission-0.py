class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]
        return self.isValid(0, 0, s, memo)

    def isValid(self, index: int, openCount: int, s: str, memo: List[List[int]]) -> bool:
        if index == len(s):
            return openCount == 0

        if memo[index][openCount] != -1:
            return memo[index][openCount]

        if s[index] == '(':
            return self.isValid(index + 1, openCount + 1, s, memo)
        elif s[index] == ')':
            return openCount > 0 and self.isValid(index + 1, openCount - 1, s, memo)
        else:
            result = (self.isValid(index + 1, openCount, s, memo) or 
                self.isValid(index + 1, openCount + 1, s, memo) or 
                (openCount > 0 and self.isValid(index + 1, openCount - 1, s, memo)))
            memo[index][openCount] = result
            return memo[index][openCount]
        