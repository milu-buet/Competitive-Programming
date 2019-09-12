


class Node(object):
	"""docstring for Node"""
	def __init__(self, x):
		self.x = x
		self.left = None
		self.right = None



def checkBalance(root):

	if root:
		mxL,mnL = checkBalance(root.left)
		mxR,mnR = checkBalance(root.right)

		return max(mxL,mxR)+1, min(mnL, mnR)+1

	else:
		return 0,0



root = Node(2)
L = Node(4)
L.left = Node(5)
root.left = L


print(checkBalance(root))