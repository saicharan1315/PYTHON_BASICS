class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s_u_m = 0
        for i in range(len(nums)):
            if(bin(i).count('1')==k):
                s_u_m = s_u_m + nums[i]
        return s_u_m