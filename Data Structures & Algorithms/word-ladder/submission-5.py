class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        result = 1
        wordList.append(beginWord)
        adjList = collections.defaultdict(list) # adjList is the graph, each node is the word
        queue = deque([beginWord])
        visited = set([beginWord]) # set for visited nodes in graph

        for word in wordList:
            for i in range(len(word)):
                pattern = word[0:i] + "*" + word[i + 1 :]
                adjList[pattern].append(word)
        
        while queue:
            for j in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result
                for k in range(len(word)):
                    pattern = word[:k] + "*" + word[k + 1:]
                    for nei in adjList[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            result += 1
        return 0

        