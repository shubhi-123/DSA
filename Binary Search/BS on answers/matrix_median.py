from bisect import bisect_right

class Solution:
    def median(self, mat):
        r = len(mat)
        c = len(mat[0])

        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)

        req = (r * c) // 2

        while low <= high:
            mid = (low + high) // 2

            count = 0
            for row in mat:
                count += bisect_right(row, mid)

            if count <= req:
                low = mid + 1
            else:
                high = mid - 1

        return low