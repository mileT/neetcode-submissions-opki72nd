class PrefixTreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = PrefixTreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                cur.children[i] = PrefixTreeNode()
            cur = cur.children[i]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        def dfs(index, node):
            # base case, reach end of word
            if index == len(word):
                return node.end
            
            # for each char of word, there are 2 types, "." or real char
            if word[index] != ".":
                i = ord(word[index]) - ord("a")
                if node.children[i] == None:
                    return False
                node = node.children[i]
                return dfs(index + 1, node)
            else:
                for j in range(len(node.children)):
                    if node.children[j] and dfs(index + 1, node.children[j]):
                        return True
                return False
        return dfs(0, cur)


