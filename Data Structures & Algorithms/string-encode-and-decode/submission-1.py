class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, result = [], ""
        for s in strs:
            sizes.append(len(s))
        for size in sizes:
            result += str(size)
            result += ','
        result += "#"
        for s in strs:
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        result = []
        sizes, i = [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for size in sizes:
            result.append(s[i : i + size])
            i += size
        return result
