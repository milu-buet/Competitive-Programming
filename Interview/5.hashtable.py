

# What kind of keys will be there?
# hash function depends on key type

# How to resolve hash collision?
# 1. Separate Chaining: linked list
# 2. self balancing BST
# 3. double hash: hash of hashes.
# 4. Linear Probing: Using next avialble free location. h(k)+i, i++
# 5. quadratic probing: h(k)+c1.i+c2.i^2, i++


def h(s):
	sm = 0
	n = len(s)
	for i,c in enumerate(s):
		sm += ord(s[i]) * 31**(n-i-1)
	return sm




######  Linked List Implementation
class HashNode(object):
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.next = None

class HashTable(object):
	"""docstring for HashTable"""
	def __init__(self):
		
		self.size = 0
		self.cap = 10
		self.arr = [None]*self.cap

	def get(self, key):
		
		head = self.getBucketHead(key)
		while head and head.key!=key:
			head = head.next

		if head:
			return head.val

		return None

	def add(self, key, val):
		
		bucketId = self.getBucketId(key)
		head = cur = self.getBucketHead(key)

		while cur and cur.key!=key:
			cur = cur.next

		if cur:
			cur.val = val
			return

		newNode = HashNode(key, val)
		newNode.next = head
		self.arr[bucketId] = newNode
		self.size+=1

		if float(self.size)/self.cap >= .7:
			self.expand()


	def remove(self, key):
		head = self.getBucketHead(key)
		prev = None
		while head and head.key!=key:
			prev = head
			head = head.next

		if head:
			if prev:
				prev.next = head.next
			else:
				bucketId = self.getBucketId(key)
				self.arr[bucketId] = head.next
			return head.val
		return None


	def isEmpty(self):
		self.getsize() == 0

	def getBucketId(self, key):
		return h(key)%self.cap

	def getBucketHead(self, key):
		return self.arr[self.getBucketId(key)]


	def getSize(self):
		return self.size

	def expand(self):
		
		temp = self.arr

		self.cap*=2
		self.size=0
		self.arr = [None]*self.cap

		for head in temp:
			while head:
				self.add(head.key, head.val)
				head = head.next


d = HashTable()
d.add('abc',5)
print(d.get('abc'))
d.remove('abc')
print(d.get('abc'))



########## Linear Probing

def h(s):
	sm = 0
	n = len(s)
	for i,c in enumerate(s):
		sm += ord(s[i]) * 31**(n-i-1)
	return sm

class HashNode():
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.deleted = False

class HasHTable():

	def __init__(self):
		self.size = 0
		self.cap = 1
		self.arr = [None]*self.cap


# Find the appropiate place
# if node found, change it
# if deleted node found, use it
# if null node found use it
# if size/cap>.7 the resize it
	def set(self, key, val):
		bucketId = self.getBucketId(key)

		node = self.arr[bucketId]
		while node and not node.deleted and node.key!=key:
			bucketId+=1
			node = self.arr[bucketId]

		if node is None or node.deleted:
			newNode = HashNode(key,val)
			self.arr[bucketId] = newNode
			self.size+=1
		elif node.key == key:
			node.val = val

		if self.size/self.cap>.7:
			self.resize()

# if node is none, searching should stop
# if node is deleted, searching should continue
# if node is not equal, searching should continue
	def get(self, key):
		
		bucketId = self.getBucketId(key)

		node = self.arr[bucketId]
		while node and (node.deleted or node.key!=key):
			bucketId+=1
			node = self.arr[bucketId]

		if node and not node.deleted and node.key==key:
			return node.val

		return None
		
# locate it
# if node is None, stop
# if node is deleted continue
# if node.key != key, continue
# if node found, mark it deleted, return the val
# if not found return None
	def remove(self,key):
		bucketId = self.getBucketId(key)

		node = self.arr[bucketId]
		while node and (node.deleted or node.key!=key):
			bucketId+=1
			node = self.arr[bucketId]
		
		if node and not node.deleted and node.key==key:
			node.deleted = True
			self.size-=1
			return node.val

		return None


	def getSize(self):
		return self.size

	def isEmpty(self):
		return self.getsize()==0

	def resize(self):
		
		self.cap *= 2
		temp = self.arr

		self.arr = [None]*self.cap
		self.size = 0

		for node in temp:
			if node and not node.deleted:
				self.set(node.key, node.val)

	def getBucketId(self, key):
		return h(key)%self.cap



d = HashTable()
d.add('abc',5)
d.add('abcd',6)

print(d.get('abc'))
print(d.get('abcd'))
d.remove('abc')
print(d.get('abc'))
print(d.get('abcd'))






