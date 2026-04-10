class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = defaultdict(int)
        for num in nums:
            freqCount[num] += 1

        minHeap = []
        for num, freq in freqCount.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [num for freq, num in minHeap]
        