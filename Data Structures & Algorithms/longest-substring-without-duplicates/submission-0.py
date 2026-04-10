class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left, right = 0, 0
        char_map = {}

        while (right < len(s)):
            if ( s[right] in char_map and char_map.get(s[right]) >= left):
                left = char_map.get(s[right]) + 1
            else:
                char_map[s[right]] = right
                max_len = max(max_len, right - left + 1)
                right += 1

        return max_len
        