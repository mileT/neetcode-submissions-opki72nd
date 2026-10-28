class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        root = TrieNode()
        dp = [0] * (n + 1)
        # build the Trie with dictionary
        for word in dictionary:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.is_word = True
        
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            cur = root
            for j in range(i, n):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.is_word:
                    dp[i] = min(dp[i], dp[j + 1])
        
        return dp[0]

            
        