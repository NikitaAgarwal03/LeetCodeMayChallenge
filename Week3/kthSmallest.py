# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        result=list()
        res = self.ascending(root, result)
        return res[k-1]
    
    def ascending(self,root,result):
        
        if root == None:
            return
        self.ascending(root.left,result)
        result.append(root.val)
        self.ascending(root.right,result)
        return result   

        
