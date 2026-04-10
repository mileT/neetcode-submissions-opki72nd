class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # good = set()

        # for triplet in triplets:
        #     if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
        #         continue
        #     for i, v in enumerate(triplet):
        #         if v == target[i]:
        #             good.add(i)

        # return len(good) == 3

        x = y = z = False

        for t in triplets:
            x |= (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])
            y |= (t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2])
            z |= (t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2])

            if x and y and z:
                return True

        return False

        