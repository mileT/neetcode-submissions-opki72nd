class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freqDict = defaultdict(int)
        buckets = [[] for _ in range(n + 1)]
        result = []

        # loop nums to calculate freq
        for num in nums:
            freqDict[num] += 1

        for num, freq in freqDict.items():
            buckets[freq].append(num)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        