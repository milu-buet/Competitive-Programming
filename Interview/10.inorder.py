

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None



class Inorder(object):
	"""docstring for Inorder"""
	def __init__(self):
		pass


	def dfs(self, root):
		if root is None:
			return
		self.dfs(root.left)
		print(root.val)
		self.dfs(root.right)

	def dfs_Ita(self, root):
		
		node = root
		stack = []
		while stack or node:
			while node:
				stack.append(node)
				node = node.left
			node = stack.pop()
			print(node.val)
			node = node.right

	def dfs_ita_noSpace(self, root):
		node = root
		while node:
			if node.left is None:
				print(node.val)
				node = node.right
			else:
				pred = node.left
				while pred.right and pred.right!=node:
					pred = pred.right

				if pred.right is None:
					#first time
					pred.right = node
					node = node.left
				else:
					#second time
					print(node.val)
					node = node.right
					pred.right = None




class Iterator_stack(object):
	"""docstring for Iterator"""
	def __init__(self, root):
		self.node = root
		self.stack = []
		self.peekval = None

	def hasnext(self):
		return self.stack or self.node

	def next(self):
		if self.peekval is not None:
			ret  = self.peekval
			self.peekval = None
			return ret

		while self.node:
			self.stack.append(self.node)
			self.node = self.node.left
		self.node = self.stack.pop()
		ret = self.node.val
		self.node = self.node.right
		return ret

	def peek(self):
		if self.peekval is None:
			self.peekval = self.next()
		return self.peekval



class Iterator_noStack(object):
	"""docstring for Iterator_noStack"""
	def __init__(self, root):
		self.node = root
		self.peekval = None


	def hasnext(self):
		return self.node is not None


	def next(self):

		if self.peekval is not None:
			ret = self.peekval
			self.peekval = None
			return ret

		ret = None
		while ret is None and self.node is not None:
			if self.node.left is None:
					#print(node.val)
					ret = self.node.val
					self.node = self.node.right
			else:
				pred = self.node.left
				while pred.right and pred.right!=self.node:
					pred = pred.right

				if pred.right is None:
					#first time
					pred.right = self.node
					self.node = self.node.left
				else:
					#second time
					#print(node.val)
					ret = self.node.val
					self.node = self.node.right
					pred.right = None
		return ret


	def peek(self):
		if self.peekval is None:
			self.peekval = self.next()
		return self.peekval




		



n1 = Node(10)
n2 = Node(5)
n3 = Node(15)

n1.left = n2
n1.right = n3

#Inorder().dfs_Ita(n1)
#Inorder().dfs_ita_noSpace(n1)

#it = Iterator_stack(n1)
it = Iterator_noStack(n1)
while it.hasnext():
	print(it.peek())
	print(it.next())