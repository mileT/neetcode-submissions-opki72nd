class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)

        def dfs(i, path):
            if i == len(s):
                result.append(" ".join(path))
                return

            node = trie.root
            word = []
            for j in range(i, len(s)):
                char = s[j]
                if char not in node.children:
                    break

                word.append(char)
                node = node.children[char]

                if node.isWord:
                    path.append("".join(word))
                    dfs(j + 1, path)
                    path.pop()

        result = []
        dfs(0, [])
        return result
        