
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
		

class MyQ(object):
	"""docstring for MyQ"""
	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def isEmpty(self):
		return self.s1.isEmpty() and self.s2.isEmpty()

	def push(self, x):
		self.s1.push(x)

	def pop(self):
		if not self.isEmpty():
			if self.s2.isEmpty():
				while not self.s1.isEmpty():
					self.s2.push(self.s1.pop())
			return self.s2.pop()


q = MyQ()
q.push(1)
q.push(2)
q.push(3)
q.push(4)

print(q.pop())

