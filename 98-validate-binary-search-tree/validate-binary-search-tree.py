class Solution(object):
    def isValidBST(self,root):
        def check(node,left,right):
            if not node:
                return True

            if node.val<=left or node.val>=right:
                return False

            return check(node.left,left,node.val) and check(node.right,node.val,right)

        return check(root,float("-inf"),float("inf"))