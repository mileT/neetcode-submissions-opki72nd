class Solution:
    def isValid(self, s: str) -> bool:
        pair_map = {"(": ")", "[" : "]", "{" : "}"}
        open_set = set(["(", "[", "{"])
        stack = []
        for char in s:
            if char in open_set:
                stack.append(char)
            elif stack and char == pair_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []
        