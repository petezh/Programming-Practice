# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        # if leaf and sums
        if not root.left and not root.right and root.val == sum:
            return True
        # decrement val
        sum -= root.val
        # recurse
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)