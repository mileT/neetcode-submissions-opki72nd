class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordsSet = set(wordList)
        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i] + c + word[i + 1:]
                    if nextWord in wordsSet:
                        wordsSet.remove(nextWord)
                        queue.append((nextWord, length + 1))
        return 0 
        