# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.xDepth = -1
        self.yDepth = -2
        self.xParent = None
        self.yParent = None

        def dfs(root, parent, x, y, depth):
            if root is None: return
            if root.val == x:
                self.xParent = parent
                self.xDepth = depth
            elif root.val == y:
                self.yParent = parent
                self.yDepth = depth
            else:
                dfs(root.left, root, x, y, depth+1)
                dfs(root.right, root, x, y, depth+1)

        dfs(root, None, x, y, 0)
        return self.xDepth == self.yDepth and self.xParent != self.yParent
