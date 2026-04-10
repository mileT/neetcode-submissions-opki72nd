class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = len(s)
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range(n):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        for key in s_dict.keys():
            if s_dict[key] != t_dict[key]:
                return False

        return True