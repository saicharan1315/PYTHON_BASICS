class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result=""
        for i in range(len(s)):
            b = indices.index(i)
            result += s[b]
        return result