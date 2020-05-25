# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        stack = [root]
        
        for i in range(1, len(preorder)):
            if preorder[i] < stack[-1].val:
                top = TreeNode(preorder[i])
                stack[-1].left = top
                stack.append(top)
            else:
                while stack and stack[-1].val < preorder[i]:
                    pop = stack.pop()
                top = TreeNode(preorder[i])
                pop.right = top
                stack.append(top)
                
        return root        
