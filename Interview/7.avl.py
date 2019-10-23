

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

	def getBalance(self):
		lh, rh = 0, 0
		if self.left:
			lh = self.left.height
		if self.right:
			rh = self.right.height
		return lh - rh



class AVL(object):
	"""docstring for AVL"""
	def __init__(self):
		self.root = None

	def insert(self, val):
		self.root =  self._insert(self.root, val)

	def _insert(self, root, val):
		if root is None:
			return Node(val)
		elif val < root.val:
			root.left = self._insert(root.left,val) 
		else:
			root.right = self._insert(root.right,val)

		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
		balance = root.getBalance()

		if balance > 1 and root.left and val < root.left.val: #left left
			return self.rightRotate(root)

		elif balance > 1 and root.left and val > root.left.val: #left right
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		elif balance < -1 and root.right and val > root.right.val: #right right
			return self.leftRotate(root)

		elif balance < -1 and root.right and val < root.right.val: #right left
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	def delete(self, val):
		self.root = self._delete(self.root, val)

	def _delete(self, root, val):
		if root is None:
			return None
		elif val < root.val:
			return self._delete(root.left, val)
		elif val > root.val:
			return self._delete(root.right, val)

		if root.left is None:
			return root.right
		elif root.right is None:
			return root.left

		root.val = self.getminval(root.right)
		root.right = self._delete(root.right, root.val)

		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
		balance = root.getBalance()

		if balance > 1 and root.left and val < root.left.val: #left left
			return self.rightRotate(root)

		elif balance > 1 and root.left and val > root.left.val: #left right
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		elif balance < -1 and root.right and val > root.right.val: #right right
			return self.leftRotate(root)

		elif balance < -1 and root.right and val < root.right.val: #right left
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root



	def rightRotate(self, root):
		if root is None:
			return None

		z = root
		y = z.left
		T = y.right

		z.left = T
		y.right = z

		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

		return y

	def leftRotate(self, root):
		if root is None:
			return None

		z = root
		y = z.right
		T = y.left

		z.right = T
		y.left = z

		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

		return y


	def getHeight(self, root):
		if root is None:
			return 0
		return root.height

	def getminval(self, root):
		if root is None:
			return None
		node = root
		while node.left:
			node = node.left
		return node.val 
	

	def preOrder(self):
		self._preOrder(self.root)

	def _preOrder(self, root): 

	    if not root: 
	        return

	    print("{0} ".format(root.val), end="") 
	    self._preOrder(root.left) 
	    self._preOrder(root.right) 



# Driver program to test above function 
myTree = AVL() 

myTree.insert(10) 
myTree.insert(20) 
myTree.insert(30) 
myTree.insert(40) 
myTree.insert(50) 
myTree.insert(25) 
myTree.delete(30)
  
"""The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50"""
  
# Preorder Traversal 
print("Preorder traversal of the", 
      "constructed AVL tree is") 
myTree.preOrder() 
print() 