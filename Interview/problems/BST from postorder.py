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
    def bstFromPostorder(self, postorder):
        
        if len(postorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        stack = [root]
        
        for i in range(len(postorder)-2, -1, -1):
            top = stack[-1]
            if postorder[i] > top.val:
                node = TreeNode(postorder[i])
                top.right = node
                stack.append(node)
            else:
                # pop while top is smaller than ith
                stack.pop()
                while stack and postorder[i] < stack[-1].val:
                    top = stack.pop()
                
                node = TreeNode(postorder[i])
                top.left = node
                stack.append(node)
                    
        return root







def inorder(root):
    if root is None:
        return 

    inorder(root.left)
    print(root.val)
    inorder(root.right)

#      11,10,8

a = [1,7,5,12,10,8]
root = Solution().bstFromPostorder(a)
inorder(root)



def bstp(arr):

    root = TreeNode(arr[-1])
    




