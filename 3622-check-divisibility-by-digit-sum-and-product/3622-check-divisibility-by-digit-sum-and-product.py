class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        summ = 0
        prod = 1
        while temp > 0:
            digit = temp % 10
            summ += digit
            prod *= digit
            temp //= 10
        return n % (summ + prod) == 0