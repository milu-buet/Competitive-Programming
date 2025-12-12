class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1
class PrettyPrint(object):
	"""docstring for PrettyPrint"""
	def __init__(self, root):
		self.root = root
	def getHeight(self, root):
		if root is None:
			return 0
		leftH = self.getHeight(root.left)
		rightH = self.getHeight(root.right)
		return 1 + max(leftH, rightH)
	def print(self):
		q = [self.root]
		level = 1
		height = self.getHeight(self.root)
		while q:
			i = height - level
			self.spaces(self.nodestartSpace(i))
			nq = []
			while q:
				node = q.pop(0)
				print(node.val, end="")
				v = self.nodeSpace(i)
				self.spaces(v)
				if node.left:
					nq.append(node.left)
				if node.right:
					nq.append(node.right)
			if i>0:
				print("")
				self.spaces(self.slashtartSpace(i))
				inner = self.slashinnerSpace(i)
				outer = self.slashouterSpace(i)
				for j in range(level):
					print('/',end='')
					self.spaces(inner)
					print("\\",end='')
					self.spaces(outer)
			print("")
			q = nq
			level += 1
	def spaces(self, n):
		print(" "*n, end="")
	def nodestartSpace(self, i):
		# f(l=h) = 0
		# f(l=h-1) = 2
		# f(l=h-2) = 6
		# f(l=h-3) = 14
		# 0, 2, 6, 14, 
		# 0, 0+2, 2+4, 6+8

		# f(0) = 0
		# f(i) = f(i-1) + 2^i
		# i = h-l
		if i==0:
			return 0
		return self.nodestartSpace(i-1) + 2**i
	def nodeSpace(self, i):
		# 3, 7, 15
		# 3, 3+4, 7+8

		# f(0) = 3
		# f(i) = f(i-1) + 2^(i+1)
		if i==0:
			return 3
		return self.nodeSpace(i-1) + 2**(i+1)
	def slashtartSpace(self, i):
		# 1, 3, 7

		# f(1) = 1
		# f(i) = f(i-1) + 2**(i-1) 
		if i==1:
			return 1
		return self.slashtartSpace(i-1) + 2**(i-1)
	def slashinnerSpace(self, i):
		# 1, 5, 13

		# f(1) = 1
		# f(i) = f(i-1) + 2**(i) 
		if i==1:
			return 1
		return self.slashtartSpace(i-1) + 2**(i)
	def slashouterSpace(self, i):
		# 5, 9, 13
		if i==1:
			return 5
		return self.slashouterSpace(i-1) + 4



# class Node(object):
# 	"""docstring for Node"""
# 	def __init__(self, val):
# 		self.val = val
# 		self.left = None
# 		self.right = None
# 		self.height = 1

class AVL(object):
	"""docstring for AVL"""
	def __init__(self):
		self.root = None

	def insert(self, val):
		self.root = self.insert_(self.root, val)

	def insert_(self, root, val):
		if root is None:
			return Node(val)
		elif root.val == val:
			return root
		elif val < root.val:
			root.left = self.insert_(root.left, val)
		elif val > root.val:
			root.right = self.insert_(root.right, val)

		return self.balance(root, val)
		

	def delete(self, val):
		self.root = self.delete_(self.root, val)

	def delete_(self, root, val):
		if root is None:
			return None
		elif val < root.val:
			root.left = self.delete_(root.left, val)
		elif val > root.val:
			root.right = self.delete_(root.right, val)
		elif val == root.val and root.left is None:
			return root.right
		elif val == root.val and root.right is None:
			return root.left 
		elif val == root.val:
			mval = self.getmin(root.right)
			root.val = mval
			root.right = self.delete_(root.right, mval)
		
		return self.balance(root, val)


	def balance(self, root, val):

		lefth = self.geth(root.left)
		righth = self.geth(root.right)
		root.height = 1 + max(lefth, righth)

		balance = lefth - righth

		if balance > 1 and val < root.left.val:
			root = self.rr(root)
		elif balance > 1 and val > root.left.val:
			root.left = self.lr(root.left)
			root = self.rr(root)
		elif balance < -1  and val > root.right.val:
			root = self.lr(root)
		elif balance < -1 and val < root.right.val:
			root.right = self.rr(root.right)
			root = self.lr(root)

		return root



	def geth(self, node):
		if node is None:
			return 0
		return node.height

	def rr(self, x):

		y = x.left 
		T1 = y.left
		T2 = y.right 
		T3 = x.right

		y.right = x
		x.left = T2

		x.height = 1 + max(self.geth(T2), self.geth(T3))
		y.height = 1 + max(self.geth(T1), self.geth(x))

		return y

	def lr(self, x):
		
		y = x.right 
		T1 = x.left 
		T2 = y.left 
		T3 = y.right 

		y.left = x
		x.right = T2

		x.height = 1 + max(self.geth(T1), self.geth(T2))
		y.height = 1 + max(self.geth(x), self.geth(T3))

		return y
	
	def getmin(self, root):
		if root is None:
			return None
		node = root
		while node.left:
			node = node.left
		return node.val 

	

"""The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50"""
  
# Preorder Traversal 
print("Preorder traversal of the", 
      "constructed AVL tree is") 
myTree = AVL() 
myTree.insert(10) 
myTree.insert(20) 
myTree.insert(30) 
myTree.insert(40) 
myTree.insert(50) 
myTree.insert(25) 
#myTree.delete(30)
PrettyPrint(myTree.root).print()


    def bl(self, root):
        
        if root is None:
            return None, 0
        
        root.left, lefth = self.balanceBST(root.left)
        root.right, righth = self.balanceBST(root.right)
        
        
        balance = lefth - righth
        val = root.val
        
        while not -1 <= balance <= 1 :
            if balance > 1:
                root = self.rr(root)
                balance -= 1
            elif balance < -1:
                root = self.lr(root)
                balance += 1

	return root


	def lr(self, x):
		y = x.right 
		T1 = x.left 
		T2 = y.left 
		T3 = y.right 

		y.left = x
		x.right = T2
        
	def rr(self, x):

		y = x.left 
		T1 = y.left
		T2 = y.right 
		T3 = x.right

		y.right = x
		x.left = T2