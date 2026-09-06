# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr=[]
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        prev=None
        for i in range(len(arr)):
            node=TreeNode(arr[i])
            if not prev:
                curr=node
            if prev:
                prev.right=node
            prev=node
        return curr

        

