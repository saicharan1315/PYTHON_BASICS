class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        n = len(encoded)
        for i in range(n):
            a = ans[-1] ^ encoded[i]
            ans.append(a)
        return ans
