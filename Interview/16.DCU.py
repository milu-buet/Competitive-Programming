

class DCU(object):
	"""docstring for DCU"""
	def __init__(self, n):
		self.A = list(range(n))
		self.rank = [1]*n

	def find(self, x):
		if self.A[x] != x:
			x = self.find(self.A[x])
		return x

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
		self.find(x) == self.find(y)


a = DCU(10)
a.add(1,8)
a.add(2,8)

print(a.A)
		