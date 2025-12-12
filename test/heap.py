

class MyHeap(object):   #minHeap
	"""docstring for MyHeap"""
	def __init__(self,arr):
		self.arr = arr

	def getLeft(self, i):
		if 2*i + 1 < len(self.arr):
			return 2*i + 1

		return None

	def getRight(self,i):
		if 2*i + 2 < len(self.arr):
			return 2*i + 2

		return None

	def getMin(self,i):

		pmin = i
		l = self.getLeft(i)
		r = self.getRight(i)

		if l and self.arr[pmin] > self.arr[l]:
			pmin = l


		if r and self.arr[pmin] > self.arr[r]:
			pmin = r


		return pmin


	def getParent(self,i):

		if i%2 == 1:
			return int(i/2)

		return int(i/2) - 1

	def Drepair(self):
		i = 0
		pmin = self.getMin(i)

		while pmin != i:
			self.arr[i],self.arr[pmin] = self.arr[pmin], self.arr[i]
			i = pmin
			pmin = self.getMin(i)

	def getMinP(self,i):

		if i==0:
			return False

		parent = self.getParent(i)

		if self.arr[i] < self.arr[parent]:
			return True

		return False


	def Urepair(self):
		i = len(self.arr) -1

		while self.getMinP(i):
			pmin = self.getParent(i)
			self.arr[i],self.arr[pmin] = self.arr[pmin], self.arr[i]
			i=pmin


	
	def pop(self):

		elem = self.arr[0]
		self.arr[0],self.arr[-1] = self.arr[-1], self.arr[0]
		#print(self.arr)
		del self.arr[-1]
		self.Drepair()
		

		return elem


	def push(self, val):
		self.arr.append(val)
		self.Urepair()




