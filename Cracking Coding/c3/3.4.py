class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.arr = []

	def isEmpty(self):
		return len(self.arr) == 0

	def push(self, x):
		self.arr.append(x)
		

	def pop(self):
		if not self.isEmpty():
			return self.arr.pop(-1)

	def peek(self):
		if not self.isEmpty():
			return self.arr[-1]




def ToH(s1,s2,s3, i):
	if i == 1:
		s3.push(s1.pop())
		return
	else:
		ToH(s1,s3,s2,i-1)
		ToH(s1,s2,s3,1)
		ToH(s2,s1,s3,i-1)




s1 = Stack()
s1.push(4)
s1.push(3)
s1.push(2)
s1.push(1)
s2 = Stack()
s3 = Stack()

ToH(s1,s2,s3, 4)
print(s1.arr, s2.arr, s3.arr)