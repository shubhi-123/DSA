class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #this is optimal where t(n)=o(log n)
        left, right = 0, len(nums)-1
        while left < right:
            mid = int((left + right)/2)
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid%2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            else:
                right = mid
        return nums[left]

        #this is my logic that has t(n)=o(n)
        # n=len(nums)
        # def check(mid):
        #     target=nums[mid]
        #     left_same = (mid - 1 >= 0 and nums[mid - 1] == target)
        #     right_same = (mid + 1 < n and nums[mid + 1] == target)
        #     if not left_same and not right_same:
        #         return nums[mid]
        #     return None
        # def solve(low, high):
        #     if low>high:
        #         return None
        #     mid=low+(high-low)//2
        #     res=check(mid)
        #     if res is not None:
        #         return res
        #     left_res=solve(low,mid-1)
        #     if left_res is not None:
        #         return left_res
        #     right_res=solve(mid+1, high)
        #     if right_res is not None:
        #         return right_res
        #     return None
        # return solve(0,n-1)       

        