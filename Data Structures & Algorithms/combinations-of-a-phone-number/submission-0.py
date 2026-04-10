class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0:
            return []

        result = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, cur):
            if i == len(digits):
                result.append(cur)
                return

            digit = digits[i]
            for c in digitToChar.get(digit):
                dfs(i + 1, cur + c)
        dfs(0, "")
        return result