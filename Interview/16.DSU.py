# T(n) : find = O(logn) for single call. But almost constant 

class DSU(object):
	"""docstring for DCU"""
	def __init__(self, n):
		self.A = list(range(n))
		self.rank = [1]*n

	def find(self, x):
		#print(x)
		if self.A[x] != x:
			self.A[x] = self.find(self.A[x])
		return self.A[x]

	def add(self, x, y):
		xroot = self.find(x)
		yroot = self.find(y)
		
		if self.rank[xroot] < self.rank[yroot]:
			self.A[xroot] = self.A[yroot]
		elif self.rank[xroot] > self.rank[yroot]:
			self.A[yroot] = self.A[xroot]
		else:
			self.A[yroot] = self.A[xroot]
			self.rank[xroot]+=1


	def isSameSet(self, x, y):
		return self.find(x) == self.find(y)



a = DSU(10)
a.add(1,8)
a.add(2,8)

print(a.A)










class DSU():
	def __init__(self, n):
		self.arr = list(range(n))
		self.rank = [0]*n

	def find(self, x):
		if x != self.arr[x]:
			self.arr[x] = self.find(arr[x])
		return arr[x]


	def add(self, x, y):
		xroot = self.find(x)
		yroot = self.find(y)

		if self.rank[xroot] > self.rank[yroot]:
			self.arr[yroot] = self.arr[xroot]
		elif self.rank[xroot] < self.rank[yroot]:
			self.arr[xroot] = self.arr[yroot]
		else:
			self.arr[yroot] = self.arr[xroot]
			self.rank[xroot] += 1

	def isSameSet(self, x, y):
		return self.find(x) == self.find(y)












































		