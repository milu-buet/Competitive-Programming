

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
		pass



n1 = Node(10)
n2 = Node(5)
n3 = Node(15)
n4 = Node(1)

n1.left = n2
n1.right = n3
n2.left = n4

Postorder().dfs_Ita(n1)


		