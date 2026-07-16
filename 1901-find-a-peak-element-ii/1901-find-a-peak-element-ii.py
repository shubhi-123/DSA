class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1
        while low <= high:
            mid = (low + high) // 2
            # Find the row having maximum element in the middle column
            maxRow = 0
            for i in range(1, n):
                if mat[i][mid] > mat[maxRow][mid]:
                    maxRow = i

            left = -1
            if mid > 0:
                left = mat[maxRow][mid - 1]

            right = -1
            if mid < m - 1:
                right = mat[maxRow][mid + 1]

            # Peak found
            if mat[maxRow][mid] > left and mat[maxRow][mid] > right:
                return [maxRow, mid]

            # Move towards the larger neighbour
            elif left > mat[maxRow][mid]:
                high = mid - 1
            else:
                low = mid + 1