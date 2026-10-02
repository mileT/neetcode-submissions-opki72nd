class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        trie = Trie()
        for word in strs:
            if not word:
                return ""
            trie.insert(word)

        prefix = []
        cur = trie.root
        while len(cur.children) == 1 and not cur.is_end:
            char, node = next(iter(cur.children.items()))
            prefix.append(char)
            cur = node

        return "".join(prefix)

        
        