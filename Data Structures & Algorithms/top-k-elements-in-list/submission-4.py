class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = defaultdict(int)
        n = len(nums)

        for num in nums:
            freqDict[num] += 1

        buckets = [[] for _ in range(n + 1)]

        for num, freq in freqDict.items():
            buckets[freq].append(num)

        result = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result