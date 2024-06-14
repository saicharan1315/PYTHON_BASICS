class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n = x
        result = 0
        while n != 0:
            result += (n % 10)
            n = n // 10
        if x % result == 0:
            return result
        else:
            return -1
