

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		

class Preorder(object):
	"""docstring for Inorder"""
	def __init__(self):
		pass

	def dfs(self, root):
		if root is None:
			return 
		print(root.val)
		self.dfs(self.left)
		self.dfs(self.right)


	def dfs_Ita(self, root):  # with stack, T(n) = Theta(n), S(n)=O(H)

		stack = [root]
		while stack:
			node = stack.pop()
			print(node.val)

			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)

	def dfsItaNospace(self, root):  # without stack, T(n) = O(n*H), S(n)=O(1)
		node = root
		while node:
			if node.left is None:
				print(node.val)
				node = node.right
			else:
				pred = node.left
				while pred.right and pred.right != node:
					pred = pred.right

				if pred.right is None:
					# first time
					print(node.val)
					pred.right = node
					node = node.left
				else:
					#second time
					node = node.right
					pred.right = None







class Iterator_stack(object):
	"""docstring for Iterator"""
	def __init__(self, root):
		self.stack = [root]

	def hasnext(self):
		return len(self.stack)>0

	def next(self):
		node = self.stack.pop()

		if node.right:
			self.stack.append(node.right)
		if node.left:
			self.stack.append(node.left)
		return node.val

	def peek(self):
		return self.stack[-1].val



class Iterator_noStack(object):
	def __init__(self, root):
		self.node = root
		self.peekval = None

	def hasnext(self):
		return self.node is not None

	def next(self):

		ret = None
		if self.peekval is not None:
			ret = self.peekval
			self.peekval = None
		
		while ret is None and self.node is not None:
			if self.node.left is None:
				ret = self.node.val
				self.node = self.node.right
			else:
				pred = self.node.left
				while pred.right and pred.right != self.node:
					pred = pred.right

				if pred.right is None:
					# first time
					ret = self.node.val
					pred.right = self.node
					self.node = self.node.left
				else:
					#second time
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

#Preorder().dfsItaNospace(n1)

#it = Iterator_stack(n1)
it = Iterator_noStack(n1)
while it.hasnext():
	#print(it.peek())
	#print(it.peek())
	print(it.next())





		