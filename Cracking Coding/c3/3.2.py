



#3.2
class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.arr = []
		self.mins = []

	def push(self, x):
		
		if len(self.arr) < 1 or x < self.mins[-1]:
			self.mins.append(x)
		else:
			self.mins.append(self.mins[-1])

		self.arr.append(x)


	def pop(self):

		if len(self.arr) > 0:
			self.mins.pop(-1)
			return self.arr.pop(-1)

		return None


	def min():

		if len(self.mins) > 0:
			return self.mins[-1]

		return None




st = Stack()
st.push(3)
st.push(1)
st.push(2)
st.push(-5)
st.push(-5)
#st.pop()
print(st.arr, st.mins)

#
		