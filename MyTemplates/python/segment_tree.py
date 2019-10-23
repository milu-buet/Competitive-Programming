
class Node:

	def __init__(self, val, rstart, rend):
		self.val = val
		
		self.left = None
		self.right = None
		
		self.rstart= rstart
		self.rend=rend

class SegTree():

	def __init__(self, A):

		self.A = A
		self.root = self.create_tree(self.psum(A), 0, len(A)-1)
		#print(self.root)


	def get(self, i, j):
		return self.getVal(self.root, i, j)

	def getVal(self, root, i, j):
		if root.rstart==i and root.rend==j:
			return root.val

		#entirely left
		#print(root.left.rend)
		if j <= root.left.rend:
			return self.getVal(root.left, i, j)

		#entirely right
		elif i >= root.right.rstart:
			return self.getVal(root.right, i, j)

		#mixed
		else:
			leftval= self.getVal(root.left, i, root.left.rend)
			rightval = self.getVal(root.right, root.right.rstart, j)
			return leftval+rightval

	def set(self, i, val):
		self.setVal(self.root, i, val)
		self.A[i] = val

	def setVal(self, root, i, val):

		
		root.val = root.val - self.A[i] + val
		
		if root.rstart == i and root.rend == i:
			return

		elif i <= root.left.rend:
			self.setVal(root.left, i, val)

		elif i>= root.right.rstart:
			self.setVal(root.right, i, val)



		


	def create_tree(self, psum, i, j):
		#print(i,j)

		val = psum[j]
		if i>0:
			val-=psum[i-1]

		obj = Node(val, i, j)

		
		if i==j:
			return obj

		mid  = (i+j)//2

		obj.left = self.create_tree(psum, i, mid)
		obj.right = self.create_tree(psum, mid+1, j)

		return obj

	def psum(self, a):
		sm = 0
		ans = [0]*len(a)
		for i in range(len(a)):
			sm+=a[i]

			ans[i] = sm

		return ans

	# def show(self, root):
	# 	if root is None:
	# 		return

	# 	print(root.val, root.rstart, root.rend)












a = [1, 3, 5, 7, 9, 11]
obj = SegTree(a)
print(obj.get(0,5))
obj.set(0,2)
print(obj.get(0,5))




def bridge(self): 
   
        visited = [False] * (self.n) 
        find = [float("Inf")] * (self.n) 
        lp = [float("Inf")] * (self.n) 
        parent = [-1] * (self.n) 
  
        for i in range(self.n): 
         	if visited[i] == False: 
         		self.bridgeUtil(i, visited, parent, lp, find) 
