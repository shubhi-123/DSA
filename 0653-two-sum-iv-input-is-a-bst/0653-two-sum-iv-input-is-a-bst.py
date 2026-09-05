# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr=[]
        def traversal(node):
            if not node:
                return 
            traversal(node.left)
            arr.append(node.val)
            traversal(node.right)
        traversal(root)

        i=0
        j=len(arr)-1
        while i<j:
            summ=arr[i]+arr[j]
            if summ<k:
                i=i+1
            elif summ>k:
                j=j-1
            else:
                return True
        return False


        