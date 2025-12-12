# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        
        stack = [(root,0)]
        ans = 0
        while stack:
            node, val = stack.pop()
            
            val = val*10 + node.val
            
            if node.right:
                stack.append((node.right,val))
                
            if node.left:
                stack.append((node.left,val))
                
            if node.right is None and node.left is None:
                ans+=val
                
        return ans
                
            
            
        