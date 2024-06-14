class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return num.bit_length() - 1 + num.bit_count()



class Solution:
    def numberOfSteps(self, n: int) -> int:
        step=0
        while n!=0:
            if n%2==0:
                n/=2
                step+=1
            else:
                n-=1
                step+=1
        return step