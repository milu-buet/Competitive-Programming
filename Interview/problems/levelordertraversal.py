# Definition for a binary tree node.
class Node: 
    # Constructor to create a new node 
    def __init__(self, key): 
        self.val = key  
        self.left = None
        self.right = None
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans = []
        q = [root]
        level = 0
        while q:
            nq = []
            anslevel = []
            while q:
                node = q.pop(0)
                #print(node.val)
                anslevel.append(node.val)
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)

            ans.append(anslevel)
            q = nq
            level+=1   
        return ans


def insert( node, data): 
  
    # 1) If tree is empty then return a new singly node 
    if node is None: 
        return Node(data) 
    else: 
         
        # 2) Otherwise, recur down the tree 
        if data <= node.val: 
            temp = insert(node.left, data) 
            node.left = temp  
            temp.parent = node 
        else: 
            temp = insert(node.right, data) 
            node.right = temp  
            temp.parent = node 
          
        # return  the unchanged node pointer 
        return node 

root  = None
  
# Creating the tree given in the above diagram  
root = insert(root, 20) 
root = insert(root, 8)
root = insert(root, 22)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 10) 
root = insert(root, 14)


print(Solution().levelOrder(root))

