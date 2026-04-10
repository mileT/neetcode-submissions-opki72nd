class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = 0 - heapq.heappop(maxHeap)
            x = 0 - heapq.heappop(maxHeap)

            if x < y:
                heapq.heappush(maxHeap, x - y)

        return -maxHeap[0] if len(maxHeap) > 0 else 0
        