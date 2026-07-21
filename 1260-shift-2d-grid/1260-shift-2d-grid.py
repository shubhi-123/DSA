class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        ans = [[0] * cols for _ in range(rows)]
        total = rows * cols
        k %= total
        for i in range(rows):
            for j in range(cols):
                idx = i * cols + j
                new_idx = (idx + k) % total
                r = new_idx // cols
                c = new_idx % cols
                ans[r][c] = grid[i][j]
        return ans