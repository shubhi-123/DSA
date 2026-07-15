class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bina(arr,x):
            low=0
            high=m-1
            while (low<=high):
                mid=(low+high)//2
                if arr[mid]==target:
                    return True
                elif arr[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            if target>=matrix[i][0] and target<=matrix[i][m-1]:
                if bina(matrix[i], target) is True:
                    return True
        return False