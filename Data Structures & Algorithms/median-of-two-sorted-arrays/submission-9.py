class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = (total + 1)// 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) 
        while l <= r:
            i = l + (r - l) // 2 # partion index for A
            j = half - i  # partion index for B

            Aleft = A[i - 1] if i > 0 else float("-infinity")
            Aright = A[i] if i  < len(A) else float("infinity")
            Bleft = B[j - 1] if j > 0 else float("-infinity")
            Bright = B[j] if j < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return max(Aleft, Bleft)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

        