# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]

# preorder+inorder
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        index = {}
        for i,val in enumerate(inorder):
            index[val] = i
        self.i = 0
        return self.construct(preorder, inorder, 0, len(preorder)-1, index)
        
    def construct(self, preorder, inorder, ni, nj, index):
        if ni>nj:
            return None
        root = TreeNode(preorder[self.i])
        ind = index[root.val]
        self.i+=1
        root.left = self.construct(preorder, inorder, ni, ind-1, index)
        root.right = self.construct(preorder, inorder, ind+1, nj, index)      
        return root


# postorder+inorder
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        index = {}
        for i, val in enumerate(inorder):
            index[val] = i
        self.i = len(postorder)-1
        return self.construct(inorder, postorder, 0, len(inorder)-1, index)
    
    def construct(self, inorder, postorder, pi, pj, index):
        if pi>pj:
            return None
        root = TreeNode(postorder[self.i])
        ind = index[root.val]
        self.i-=1
        root.right = self.construct(inorder, postorder, ind+1, pj, index)
        root.left = self.construct(inorder, postorder, pi, ind-1, index)
        return root


# preorder + postorder
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        index = {}
        for i,val in enumerate(post):
            index[val] = i
        return self.construct(pre, 0, len(pre)-1, post, 0, len(post)-1, index)
        
    def construct(self, pre, i, j, post, a, b, index):
        if i>j or a>b:
            return None
        root = TreeNode(pre[i])
        if i==j:
            return root
        ind = index[pre[i+1]]
        ln = ind - a + 1
        root.left = self.construct(pre, i+1, i+ln, post, a, ind, index)
        root.right = self.construct(pre, i+ln+1, j, post, ind+1, b-1, index)
        return root
        




