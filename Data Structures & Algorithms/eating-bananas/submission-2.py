class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = left + (right - left) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / mid)

            if totalTime <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
        