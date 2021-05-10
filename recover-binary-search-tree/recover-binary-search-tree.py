# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        cur, prev, drops = root, TreeNode(float('-inf')), []
        while cur:
            if cur.left:
                temp = cur.left
                while temp.right and temp.right != cur:
                    temp = temp.right
                if not temp.right:
                    temp.right, cur = cur, cur.left
                    continue
                temp.right = None
            if cur.val < prev.val: drops.append((prev, cur))
            prev, cur = cur, cur.right
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val