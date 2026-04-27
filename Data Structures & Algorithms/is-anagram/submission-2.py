class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_dict = defaultdict(int)
        if len(s) != len(t):
            return False
        n = len(s)
        for i in range(n):
            str_dict[s[i]] += 1
            str_dict[t[i]] -= 1

        for v in str_dict.values():
            if v != 0:
                return False

        return True
        