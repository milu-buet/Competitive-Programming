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



n=0
for t in [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999]:
    ans = 0
    k=0
    n+=1
    p,q=0,0
    i=t
    while i > k and i > t-t//10**(n//2):
        if len(str(i*i)) < 2*n:
            break
        for j in range(i, t-t//10**(n//2), -1):
            a = i*j
            v = str(a)
            if v == v[::-1] and ans < a:
                k=j
                ans = a
                p,q = i,j
                #print(i,a,a%1337)
                break
        i-=1
        if n%2==0:
            break
        #break
    print(n,p,q,ans,ans%1337)
                