class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        freqCount = defaultdict(int)
        # bucket =[[] * (len(nums) + 1)]
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            freqCount[num] += 1

        for num, freq in freqCount.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
