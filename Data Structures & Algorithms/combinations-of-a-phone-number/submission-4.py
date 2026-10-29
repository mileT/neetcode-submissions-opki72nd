class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0:
            return []

        result = []
        digit_char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        n = len(digits)

        def dfs(i, cur):
            if i == n:
                result.append(cur[:])
                return
            for c in digit_char_map[digits[i]]:
                dfs(i + 1, cur + c)

        dfs(0, "")
        return result

        
        