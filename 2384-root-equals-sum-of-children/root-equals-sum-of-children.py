# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        if root is None:
            return False
        s=root.left.val +root.right.val
        if root.val==s:
            return True
        else:
            return False
        