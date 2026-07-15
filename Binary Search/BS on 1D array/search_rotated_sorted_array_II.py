class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True 

            #if first, last, mid element are equal you won't be able to identify the sorted part
            #shrinking the range of nums to avoid the edge case 
            if (nums[low]==nums[mid]) and (nums[high]==nums[mid]):
                low=low+1
                high=high-1
                continue
 
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False
        