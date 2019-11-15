

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Postorder(object):
	"""docstring for Postorder"""
	def __init__(self):
		pass

	def dfs(self, root):
		if root is None:
			return
		self.dfs(root.left)
		self.dfs(root.right)
		print(root.val)

	def dfs_Ita(self, root):

		node = root
		stack = []

		while stack or node:
			while node:
				if node.right:
					stack.append(node.right)
				stack.append(node)
				node = node.left

			node = stack.pop()

			if stack and node.right and node.right==stack[-1]:
				stack.pop()
				stack.append(node)
				node = node.right
			else:
				print(node.val)
				node = None

	def dfs_Ita_nospace(self, root):

		if root is None:
			return

		node = Node(None)
		node.left = root

		while node:
			if node.left is None:
				node = node.right
			else:
				pre = node.left
				while pre.right and pre.right!=node:
					pre = pre.right
				if pre.right is None:
					#first time
					pre.right = node
					node = node.left
				else:
					#second time
					first = node
					middle = node.left

					while middle!=node:
						last = middle.right
						middle.right = first
						first = middle
						middle = last

					first = node
					middle = pre

					while middle!=node:
						print(middle.val)
						last = middle.right
						middle.right = first
						first = middle
						middle = last

					pre.right = None
					node = node.right



class Iterator_stack(object):
	"""docstring for Iterator_stack"""
	def __init__(self, root):
		self.node = root
		self.stack = []
		self.peekval = None


	def hasnext(self):
		return self.stack or self.node

	def next(self):
		ret = None

		if self.peekval is not None:
			ret = self.peekval
			self.peekval = None

		while  ret is None:
			while self.node:
				if self.node.right:
					self.stack.append(self.node.right)
				self.stack.append(self.node)
				self.node = self.node.left

			self.node = self.stack.pop()

			if self.stack and self.node.right and self.node.right==self.stack[-1]:
				self.stack.pop()
				self.stack.append(self.node)
				self.node = self.node.right
			else:
				ret = self.node.val
				self.node = None

		return ret


	def peek(self):
		if self.peekval is None:
			self.peekval = self.next()
		return self.peekval



class Iterrator_nostack(object):
	"""docstring for Iterrator_"""
	def __init__(self, root):
		self.node = Node(-1)
		self.node.left = root
		self.normal = True
		self.peekval = None


	def hasnext(self):
		return self.node is not None

	def next(self):

		if self.peekval is not None:
			ret = self.peekval
			self.peekval = None
			return ret

		ret = None

		while ret is None:
			while self.normal and self.node:
				if self.node.left is None:
					self.node = self.node.right
				else:
					pre = self.node.left
					while pre.right and pre.right!=self.node:
						pre = pre.right
					if pre.right is None:
						#first time
						pre.right = self.node
						self.node = self.node.left
					else:
						#second time
						first = self.node
						middle = self.node.left

						while middle!=self.node:
							last = middle.right
							middle.right = first
							first = middle
							middle = last

						self.pre = pre
						self.first = self.node
						self.middle = pre
						self.normal = False


			if self.middle == self.node:

				self.pre.right = None
				self.node = self.node.right
				self.normal = True
				
			else:
				ret = self.middle.val
				last = self.middle.right
				self.middle.right = self.first
				self.first = self.middle
				self.middle = last

		return ret



	def peek(self):
		if self.peekval is None:
			self.peekval = self.next()
		return self.peekval
		
		




n1 = Node(10)
n2 = Node(5)
n3 = Node(15)
n4 = Node(1)

n1.left = n2
n1.right = n3
n2.left = n4

#Postorder().dfs_Ita(n1)
#Postorder().dfs_Ita_nospace(n1)

# it = Iterrator_nostack(n1)
# while it.hasnext():
# 	print(it.peek())
# 	print(it.next())


def dfsItaNospace(root):
	node = Node(-1)
	node.left = root

	while node:
		if node.left is None:
			node = node.right
		else:

			pre = node.left

			while pre.right and pre.right!=node:
				pre = pre.right

			if pre.right is None:
				pre.right = node
				node = node.left

			else:

				first = node
				mid = node.left

				while mid!=node:
					last = mid.right
					mid.right = first
					first = mid
					mid = last

				first = node
				mid = pre

				while mid!=node:
					print(mid.val)
					last = mid.right
					mid.right = first
					first = mid
					mid = last

				pre.right = None
				node = node.right


dfsItaNospace(n1)







		