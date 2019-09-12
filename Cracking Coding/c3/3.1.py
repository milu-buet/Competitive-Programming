#3.1
#A1
class ThreeStack(object):
	"""docstring for ThreeStack"""
	def __init__(self):
		self.size = 10
		self.arr = [None]*3*self.size
		self.h = [None, None, None]


	def push(self, i, x):
		#print(self.h[i])
		
		if self.h[i] is not None:
			if self.h[i]+1 >= (i+1)*self.size:
				#print("shit")
				return
			self.h[i]+=1
		else:
			self.h[i] = i*self.size

		#print(self.h[i])
		self.arr[self.h[i]] = x

		#print("***")


	def pop(self, i):
		ret = None
		if self.h[i] is not None:
			ret = self.arr[self.h[i]]
			self.arr[self.h[i]] = None
			if self.h[i] == i*self.size:
				self.h[i] = None
			elif self.h[i] > i*self.size:
				self.h[i]-=1
		return ret


	def peek(self,i):
		if self.h[i] is not None:
			return self.arr[self.h[i]]

		return None


st = ThreeStack()
st.push(0,3)
st.push(0,4)
st.push(1,7)
st.push(1,5)
st.push(2,7)
st.push(2,6)

st.pop(1)
st.pop(1)
st.pop(1)

print(st.arr)

#A2

class Node(object):
	"""docstring for Node"""
	def __init__(self, prev, x):
		self.prev = prev
		self.x = x

	def __str__(self):
		return self.x


class TStack(object):
	"""docstring for TStack"""
	def __init__(self):
		self.size = 20
		self.arr = [None]*self.size
		self.h = [None, None, None]
		self.free = list(range(self.size))


	def push(self, i, x):
		if len(self.free) > 0:
			ai = self.free.pop(0)
			if self.h[i] is None:
				elem = Node(None, x)
			else:
				prev = self.arr[self.h[i]]
				elem = Node(prev, x)
			self.h[i] = ai
			self.arr[self.h[i]] = elem


	def pop(self, i):
		ret = None
		if self.h[i] is not None:
			self.free.append(self.h[i])
			ret = self.arr[self.h[i]].x
			temp = self.h[i]
			self.h[i] = self.arr[self.h[i]].prev
			self.arr[temp] = None
		return ret



st = TStack()
st.push(0,3)
# st.push(0,4)
st.push(1,7)
# st.push(1,5)
#st.push(2,7)
# st.push(2,6)

#st.pop(1)
#st.pop(1)
#st.pop(1)

print(st.arr)
		
