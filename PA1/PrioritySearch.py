# Md Lutfar Rahman
# mrahman9@memphis.edu
# Computational Geometry
# PA-1



#Implementation of the tree
class PrioritySearch(object):
	"""docstring for PrioritySearch"""
	def __init__(self, P):
		P.sort(key=lambda node: node.y)
		#print(P)
		self.root = self.createTree(P)

	def createTree(self, P):
		if len(P) == 0:
			return None

		root,root_i = self.getMinX(P)
		P = P[:root_i] + P[root_i+1:]

		#print(P)

		median = int((len(P)+1)/2)
		#print(median)

		if len(P)>0:
			ymid = P[median-1].y
			root.ymid = ymid
		else:
			root.ymid = root.y

		left_nodes = P[:median]
		#print(left_nodes)
		root.left = self.createTree(left_nodes)

		right_nodes = P[median:]
		#print(right_nodes)
		root.right = self.createTree(right_nodes)

		return root

	def showTree(self):
		self.showTree2(self.root)
		print()

	def showTree2(self, root):
		if root:
			print(root)
			self.showTree2(root.left)
			self.showTree2(root.right)

# get a point with minimum x-value
	def getMinX(self, P):
		minx_node = P[0]
		min_i = 0
		for i,node in enumerate(P):
			if minx_node.x > node.x:
				minx_node = node
				min_i = i

		return minx_node, min_i

	def REPORTINSUBTREE(self, v, qx, reported):
		if v and v.x <= qx:
			reported.append(v)
			self.REPORTINSUBTREE(v.left, qx, reported)
			self.REPORTINSUBTREE(v.right, qx, reported)

		return reported

	def QUERYPRIOSEARCHTREE(self, v, qx, qy1, qy2, splitted , reported ):

		if v is None:
			return reported
		
		if v and v.x <= qx and qy1 <= v.y and v.y <= qy2:
			reported.append(v)

		if splitted == -1:    #No split
			if qy2 <= v.ymid:
				self.QUERYPRIOSEARCHTREE(v.left, qx, qy1, qy2, -1, reported)

			elif qy1 > v.ymid:
				self.QUERYPRIOSEARCHTREE(v.right, qx, qy1, qy2, -1, reported)

			elif qy1 <= v.ymid:
				self.QUERYPRIOSEARCHTREE(v.left, qx, qy1, qy2, 1, reported)
				self.QUERYPRIOSEARCHTREE(v.right, qx, qy1, qy2, 2, reported)
		elif splitted == 1:  #left split
			if qy1 <= v.ymid:
				self.REPORTINSUBTREE(v.right, qx, reported)
				self.QUERYPRIOSEARCHTREE(v.left, qx, qy1, qy2, 1, reported)
			else:
				self.QUERYPRIOSEARCHTREE(v.right, qx, qy1, qy2, 1, reported)
		elif splitted == 2:  #right split
			if qy2 > v.ymid:
				self.REPORTINSUBTREE(v.left, qx, reported)
				self.QUERYPRIOSEARCHTREE(v.right, qx, qy1, qy2, 2, reported)
			else:
				self.QUERYPRIOSEARCHTREE(v.left, qx, qy1, qy2, 2, reported)

		return reported


	def search(self, qx, qy1, qy2):
		reported = []
		self.QUERYPRIOSEARCHTREE(self.root, qx, qy1, qy2, -1, reported)
		return reported


class Node(object):
	"""docstring for Node"""
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)
		self.left = None
		self.right = None
		self.ymid = None

	def __str__(self):
		return "(%s,%s)"%(self.x,self.y)

	def __repr__(self):
		return "(%s,%s)"%(self.x,self.y)		



		
def readDataFile():
	P = []
	file = open("data.txt", "r") 

	for line in file.readlines():
		x,y = line.split(' ')
		P.append(Node(x,y))

	return P



if __name__ == "__main__":

	P = readDataFile()
	obj = PrioritySearch(P)
	obj.showTree()

	while True:
		print('Enter qx qy1 qy2: ')
		ui = input()
		if ui == '0':
			break
		qx, qy1, qy2 = ui.split()
		ans = obj.search(int(qx),int(qy1),int(qy2))
		for p in ans:
			print(p)
		print(len(ans))

## input format for 'qx qy1 qy2' = '11 5 10'