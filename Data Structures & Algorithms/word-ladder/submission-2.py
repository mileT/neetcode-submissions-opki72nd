class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                adj[pattern].append(word)
        
        visit = set([beginWord])
        queue = deque([beginWord])
        result = 1
        
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)
            result += 1
        return 0
        