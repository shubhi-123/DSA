class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            value = ord(s[i]) - ord('a') + 1
            reverse_value = 26 - value + 1
            total += reverse_value * (i + 1)
        return total