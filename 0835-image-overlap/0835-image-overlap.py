from collections import Counter
class Solution:
    def largestOverlap(self, img1, img2):
        points1 = []
        points2 = []
        n = len(img1)
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    points1.append((i, j))
                if img2[i][j] == 1:
                    points2.append((i, j))
        count = Counter()
        for r1, c1 in points1:
            for r2, c2 in points2:
                count[(r2 - r1, c2 - c1)] += 1
        return max(count.values(), default=0)