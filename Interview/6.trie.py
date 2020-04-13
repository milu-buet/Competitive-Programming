
# add: 
# T(n) = theta(n)
# S(n) = O(n), omega(1)

# search
# T(n) = theta(n)
# S(n) = theta(1)

class Node(object):
	def __init__(self, val):
		self.val = val
		self.neighbours = {}
		self.end = False

class Trie(object):
	"""docstring for Trie"""
	def __init__(self):
		self.root = Node(None)

	def add(self, s):
		node = self.root
		for i in range(len(s)):
			if s[i] not in node.neighbours:
				node.neighbours[s[i]] = Node(s[i])
			node = node.neighbours[s[i]]
		node.end = True

	def search(self, s):
		node = self.root
		for i in range(len(s)):
			if s[i] not in node.neighbours:
				return False
			node = node.neighbours[s[i]]
		return node.end

	def show(self):
		stack = [self.root]
		while stack:
			node = stack.pop()
			print(node.val, node.end)
			for n in list(node.neighbours.keys())[::-1]:
				stack.append(node.neighbours[n])

trie = Trie()
trie.add('abcd')
trie.add('abc')
trie.add('fabc')
trie.show()











		