class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = [""]
        digits_str_map = {
            "2": "abc", 
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }

        for d in digits:
            temp = []
            for comb in result:
                for char in digits_str_map[d]:
                    temp.append(comb + char)
            result = temp

        return result