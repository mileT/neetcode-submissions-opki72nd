class Solution:
    def longestPalindrome(self, s: str) -> str:
        result_index, result_length = 0, 0
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_length:
                    result_index = l
                    result_length = r - l + 1
                l -= 1
                r += 1
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_length:
                    result_index = l
                    result_length = r - l + 1
                l -= 1
                r += 1
        
        return s[result_index : result_index + result_length]
            