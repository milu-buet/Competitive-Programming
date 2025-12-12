
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


#Ascending
def sortStack(st):
	rt = Stack()

	while not st.isEmpty():
		temp = st.pop()

		while not rt.isEmpty() and rt.peek() < temp:
			st.push(rt.pop())

		rt.push(temp)

	while not rt.isEmpty():
		st.push(rt.pop())




st = Stack()
st.push(3)
st.push(1)
st.push(2)
st.push(-5)
st.push(-6)


sortStack(st)
print(st.arr)