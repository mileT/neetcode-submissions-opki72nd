class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)

        cache = {}
        def dfs(i):
            if i == len(s):
                return [""]
            if i in cache:
                return cache[i]

            result = []
            cur = trie.root
            for j in range(i, len(s)):
                char = s[j]
                if char not in cur.children:
                    break
                cur = cur.children[char]
                if cur.isWord:
                    for suffix in dfs(j + 1):
                        if suffix:
                            result.append(s[i: j + 1] + " " + suffix)
                        else:
                            result.append(s[i: j + 1])

            cache[i] = result
            return result
        return dfs(0)
        