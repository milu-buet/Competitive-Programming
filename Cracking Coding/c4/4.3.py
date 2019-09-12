

class Node(object):
	"""docstring for Node"""
	def __init__(self, x):
		self.x = x
		self.left = None
		self.right = None




def createTree(arr, i, j):

	if i<=j:
		mid = (i+j)//2
		root = Node(arr[mid])
		root.left = createTree(arr, i, mid-1)
		root.right = createTree(arr, mid+1, j)

		return root
	else:
		return None


arr = [1,2,3,4,5,6,7,8,9]
arr = [1,2]
createTree(arr, 0, len(arr)-1)

