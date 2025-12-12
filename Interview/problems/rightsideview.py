# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
        
        ans = []
        node = root
        
        rlevel = 0
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()
            
            if level > rlevel:
                ans.append(node.val)
                rlevel = level
            
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
                
        return ans
        