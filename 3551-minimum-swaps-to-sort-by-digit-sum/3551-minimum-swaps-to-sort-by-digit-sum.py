class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))
        pos = {v: i for i, v in enumerate(nums)}
        visited = [False] * len(nums)
        count = 0
        for i in range(len(nums)):
            if visited[i] or arr[i] == nums[i]:
                continue
            j = i
            cycle = 0
            while not visited[j]:
                visited[j] = True
                j = pos[arr[j]]
                cycle += 1
            count += cycle - 1
        return count