class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[: i] + '*' + word[i + 1 :]
                adj[pattern].append(word)

        visit = set([beginWord])
        q = collections.deque([beginWord])
        result = 1

        while q:
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                for k in range(len(word)):
                    pattern = word[: k] + '*' + word[k + 1 :]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            result += 1
            
        return 0
        