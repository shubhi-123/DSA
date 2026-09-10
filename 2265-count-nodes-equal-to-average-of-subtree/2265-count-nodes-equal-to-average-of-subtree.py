# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans=0
        def dfs(node):
            nonlocal ans
            if node is None:
                return 0,0
            leftsum, leftcnt=dfs(node.left)
            rightsum, rightcnt=dfs(node.right)
            totalsum=leftsum+rightsum+node.val
            totalcnt=leftcnt+rightcnt+1
            if totalsum//totalcnt==node.val:
                ans+=1
            return totalsum, totalcnt
        dfs(root)
        return ans


            