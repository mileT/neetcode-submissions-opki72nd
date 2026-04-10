class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        count = 0
        for i in range(len(s)):
            count += self.helper(s, i, i)
            count += self.helper(s, i, i + 1)

        return count

    def helper(self, s: str, l: int, r: int) -> int:
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
        