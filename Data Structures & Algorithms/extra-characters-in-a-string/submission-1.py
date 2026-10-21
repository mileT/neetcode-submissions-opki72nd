class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)

        root = TrieNode()
        for word in dictionary:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.is_word = True

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]

            cur = root
            for j in range(i, n):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.is_word:
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]
        