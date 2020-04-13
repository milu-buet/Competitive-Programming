# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
        
        mn = float('-inf')
        mx = float('inf')
        stack = [(root, mn, mx)]
        
        while stack:
            node, mn, mx = stack.pop()
            if node.val <= mn or node.val >= mx :
                return False
            if node.right:
                stack.append((node.right, node.val, mx))
            if node.left:
                stack.append((node.left, mn, node.val))
        return True
                