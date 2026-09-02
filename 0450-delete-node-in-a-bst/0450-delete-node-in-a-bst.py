# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getsucc(current):
            current=current.right
            while current is not None and current.left is not None:
                current=current.left
            return current
        if root is None:
            return root
        if key<root.val:
            root.left=self.deleteNode(root.left, key)
        elif key>root.val:
            root.right=self.deleteNode(root.right, key)
        else:
            #if not left child, return right subtree
            if root.left is None:
                return root.right
            #if not right child, return left subtree
            if root.right is None:
                return root.left
            #succ is the smallest of the right subtree
            succ=getsucc(root)
            #copy succ to deleting node
            root.val=succ.val
            #set succ to Null
            root.right=self.deleteNode(root.right, succ.val)
        return root

