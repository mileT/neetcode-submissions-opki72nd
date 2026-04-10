class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for word in words:
            for c in word:
                indegree[c] = 0
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    indegree[w2[j]] += 1
                    break
                    
        q = deque([c for c in indegree if indegree[c] == 0])
        result = ""
        while q:
            c = q.popleft()
            result += c
            for neighbor in adj[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return result if len(result) == len(indegree) else ""