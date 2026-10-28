class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0:
            return []

        result = ['']
        digits_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        for digit in digits:
            combination = []
            for letter in digits_map[digit]:
                for comb in result:
                    combination.append(comb + letter)
            result = combination

        return result

        