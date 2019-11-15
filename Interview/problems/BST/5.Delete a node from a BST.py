


#  5
# / \
#3   7

# delete 5
#  3
# /
#7

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None
		self.height = 1

	def getbalance(self):
		lf = 0
		rf = 0
		if root.left:
			lf = root.left.height

		if root.right:
			rf = root.right.height 

		return lf - rf

		



class Solution(object):
	"""docstring for Solution"""

	def deleteNode(self, root, val):
		
		if root is None:
			return None
		elif val < root.val:
			root.left =  self.delete(root.left, val)
		elif val > root.val:
			root.right = self.delete(root.right, val)
		elif root.left is None:
			return root.right
		elif root.right is None:
			return root.left
		else:


			root.val  = self.getMinval(self, root.right)
			root.right = self.delete(root.right, root.val)
			root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))


			balance = root.balance()

			if balance > 1 and root.left and val < root.left.val:
				return self.rightrotate(root)

			elif balance > 1 and root.left and val > root.left.val:
				root.left = self.leftrorate(root.left)
				return self.rightrotate(root)

			elif balance < -1 and root.right and val > root.right.val:
				return self.leftrorate(root)

			elif balance < -1 and root.right and val < root.right.val:
				root.right = self.rightrotate(root.right)
				return self.leftrorate(root)

			return root


	def leftrorate(self, root):
		pass


	def rightrotate(self, root):
		pass


	def getMinval(self, root):

		while root.left:
			root = root.left 

		return root.val


	def getHeight(self, node):
		if node:
			return node.height

		return None







root = deleteNode(root, val)