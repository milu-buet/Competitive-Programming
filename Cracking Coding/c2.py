
class Node(object):
	"""docstring for Node"""
	def __init__(self, x):
		self.x = x
		self.next = None

#Input: A -> B -> C -> D -> E -> C


C = Node('C')
D = Node('D')
E = Node('E')

C.next = D
D.next = E
E.next = C

B = Node('B')
B.next = C

A = Node('A')
A.next = B

head = A




		