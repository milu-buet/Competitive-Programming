# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            True
            
        stack = [(root,root)]
        
        while stack:
            
            n1, n2 = stack.pop()
            
            if n1 is None and n2 is None:
                continue
            elif n1 is None or n2 is None or n1.val != n2.val:
                return False
            
            stack.append((n1.left, n2.right))
            stack.append((n1.right, n2.left))
            
        return True
            