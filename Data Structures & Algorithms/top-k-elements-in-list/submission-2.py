class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = defaultdict(int)
        for num in nums:
            freqCount[num] += 1
        # use max heap 
        maxHeap = [(-freq, num) for num, freq in freqCount.items()]
        heapq.heapify(maxHeap)
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(maxHeap)[1])

        return result
