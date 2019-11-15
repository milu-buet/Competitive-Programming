RED = True
BLACK = False


class Node(object):
	"""docstring for Node"""
	def __init__(self, val, color=RED):
		self.val = val
		self.left = None
		self.right = None
		self.parent = None
		self.color = color




class RB(object):
	"""docstring for RB"""
	def __init__(self):
		self.root = None


	def insert(self, val):

		root = self.root

		if root is None:
			self.root =  Node(val, BLACK) # case 1
			return self.root
		
		node = root
		pnode = None

		while node:
			pnode = node
			if val < node.val:
				node = node.left
			elif val > node.val:
				node = node.right
			else:
				return


		node = Node(val)
		node.parent = pnode

		if node.val < pnode.val:
			pnode.left = node
		else:
			pnode.right = node

		self.fix(node)

	def delete(self, val):
		pass


	def fix(self, node):

		while node.parent and node.parent.color == RED:
			parent = node.parent
			grandpa = parent.parent
			
			if parent == grandpa.left:  # working on the left side
				uncle = grandpa.right
				
				if uncle and uncle.color == RED: # uncle is red
					
					grandpa.color = RED
					parent.color = BLACK
					uncle.color = BLACK

					node = grandpa

				else:   # uncle is black
					if node == parent.right:
						node,parent = parent, node
						self.lr(node)
					parent.color = BLACK
					grandpa.color = RED
					self.rr(grandpa)

			else:
				uncle = grandpa.left
				
				if uncle and uncle.color == RED: # uncle is red
					
					grandpa.color = RED
					parent.color = BLACK
					uncle.color = BLACK

					node = grandpa

				else:   # uncle is black
					if node == parent.left:
						node,parent = parent, node
						self.rr(node)
					parent.color = BLACK
					grandpa.color = RED
					self.lr(grandpa)

		self.root.color = BLACK


	def rr(self, node):
		parent = node.parent
		left = (parent and node == parent.left)

		z = node
		y = node.left
		T = y.right

		y.right = z
		z.parent = y

		z.left = T
		if T:
			T.parent = z

		if parent:
			if left:
				parent.left = y
			else:
				parent.right = y
		
		y.parent = parent

		if parent is None:
			self.root = y


	def lr(self, node):
		parent = node.parent
		left = (parent and node == parent.left)

		z = node
		y = node.right
		T = y.left

		y.left = z
		z.parent = y

		z.right = T 

		if T:
			T.parent = z

		if parent:
			if left:
				parent.left = y
			else:
				parent.right = y
		
		y.parent = parent
		if parent is None:
			self.root = y

	def InOrder(self):
		self._InOrder(self.root)

	def _InOrder(self, root): 

	    if not root: 
	        return

	    
	    self._InOrder(root.left) 
	    print("{0} ".format(root.val), end="") 
	    self._InOrder(root.right) 


myTree = RB() 

myTree.insert(10) 
myTree.insert(20) 
myTree.insert(30) 
myTree.insert(40) 
myTree.insert(50) 
myTree.insert(25) 
#myTree.delete(30)


"""The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50"""
  
# Preorder Traversal 
print("Preorder traversal of the", 
      "constructed RB tree is") 
myTree.InOrder() 
print() 


















		