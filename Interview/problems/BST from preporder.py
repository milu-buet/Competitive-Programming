# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 8,5,1,7,10,12
# [8, 5, 1]
# [8, 7]

class Solution:
    def bstFromPreorder(self, preorder):
        
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        
        stack = [root]
        
        for i in range(1,len(preorder)):
            #print(stack)
            
            #print([t.val for t in stack] )
            
            top = stack[-1]
            if preorder[i] < top.val:
                node = TreeNode(preorder[i])
                top.left = node
                stack.append(node)
            else:
                # pop while top is smaller than ith
                stack.pop()
                while stack and preorder[i] > stack[-1].val:
                    top = stack.pop()
                
                node = TreeNode(preorder[i])
                top.right = node
                stack.append(node)
                    
        return root


def preorder(root):
    if root is None:
        return 

    print(root.val)
    preorder(root.left)
    preorder(root.right)

#      11,10,8

a = [1,7,5,12,10,8]
root = bstpre(a)
preorder(root)

