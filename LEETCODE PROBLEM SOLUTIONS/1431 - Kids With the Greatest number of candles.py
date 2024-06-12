class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high,l=max(candies),[]
        flag=True
        for i in range(len(candies)):
            candies[i]+=extraCandies
            if candies[i]>=high:
                flag=True
            else:
                flag = False
            l.append(flag)
        return l
