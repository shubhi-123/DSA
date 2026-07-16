class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        arr.sort()
        low=0
        ans=0
        high=arr[-1]-arr[0]
        def canplace(dist):
            cnt=1
            last=arr[0]
            for i in range(len(arr)):
                if arr[i]-last >=dist:
                    cnt=cnt+1
                    last=arr[i]
                if cnt>=k:
                    return True
            return False
        while (low<=high):
            mid=(low+high)//2
            if canplace(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans