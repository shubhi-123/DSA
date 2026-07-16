class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        def possible(day):
            cnt = 0
            bouquet = 0
            for bloom in bloomDay:
                if bloom <= day:
                    cnt += 1
                else:
                    bouquet += cnt // k
                    cnt = 0
            bouquet += cnt // k
            return bouquet >= m
        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low