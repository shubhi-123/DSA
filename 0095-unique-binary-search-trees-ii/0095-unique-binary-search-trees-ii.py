# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp={}
        def solve(start, end):
            if start>end:
                return [None]
            if (start, end) in dp:
                return dp[(start, end)]
            ans=[]
            for i in range(start, end+1):
                small_trees=solve(start, i-1)
                large_trees=solve(i+1, end)
                for small in small_trees:
                    for large in large_trees:
                        root=TreeNode(i)
                        root.left=small
                        root.right=large
                        ans.append(root)
            dp[(start, end)]=ans
            return ans
        return solve(1,n)
