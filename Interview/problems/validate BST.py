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
        stack = [(root, mx, mn)]
        
        while stack:
            node, mx, mn = stack.pop()
            if node.val >= mx or node.val <= mn:
                return False
            if node.right:
                stack.append((node.right, mx, node.val))
            if node.left:
                stack.append((node.left, node.val, mn))
        return True
                