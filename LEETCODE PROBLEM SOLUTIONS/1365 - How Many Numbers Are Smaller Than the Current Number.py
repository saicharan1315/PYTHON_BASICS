class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    cnt += 1
            ans.append(cnt)
        return ans