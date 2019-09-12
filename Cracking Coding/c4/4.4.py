
class Node(object):
	"""docstring for Node"""
	def __init__(self, x):
		self.x = x
		self.left = None
		self.right = None

class LNode(object):
	"""docstring for Node"""
	def __init__(self, x):
		self.x = x
		self.next = None





def DFS(root,i,H):

	if root is None:
		return None

	if i in H:
		H[i].append(root.x)
	else:
		H[i] = [root.x]


	DFS(root.left,i+1,H)
	DFS(root.right,i+1,H)



def DFSL(root,i,H,T):

	if root is None:
		return None

	if i in H:
		T[i].next = LNode(root.x)
		T[i] = T[i].next
	else:
		H[i] = LNode(root.x)
		T[i] = H[i]


	DFSL(root.left,i+1,H,T)
	DFSL(root.right,i+1,H,T)



H = {}
T = {}
root = Node(1)
l = Node(2)
r = Node(3)
root.left = l
root.right = r

#DFS(root, 0, H)
DFSL(root, 0, H, T)

print(H[1].next.x)