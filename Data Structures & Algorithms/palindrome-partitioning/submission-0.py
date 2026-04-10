class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(start, cur, s):
            if start == len(s):
                result.append(cur.copy())
                return

            for i in range(start, len(s)):
                if is_palindrome(s, start, i):
                    cur.append(s[start: i + 1])
                    dfs(i + 1, cur, s)
                    cur.pop()

        def is_palindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start = start + 1
                end -= 1
            return True

        dfs(0, [], s)
        return result
        