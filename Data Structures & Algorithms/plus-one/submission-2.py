class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one = 1
        i = 0
        digits.reverse()

        while i < len(digits):
            if one == 1:
                if digits[i] < 9:
                    digits[i] += 1
                    one = 0
                else:
                    digits[i] = 0
                    one = 1
            i += 1
        
        if one == 1:
            digits.append(1)

        digits.reverse()
        return digits