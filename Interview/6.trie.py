
# add: 
# T(n) = theta(n)
# S(n) = O(n), omega(1)

# search
# T(n) = theta(n)
# S(n) = theta(1)

class Node(object):
	def __init__(self, val):
		self.val = val
		self.chd = {}
		self.end = False

class Trie(object):
	"""docstring for Trie"""
	def __init__(self):
		self.root = Node(None)

	def add(self, s):
		node = self.root
		for i in range(len(s)):
			if s[i] not in node.chd:
				node.chd[s[i]] = Node(s[i])
			node = node.chd[s[i]]
		node.end = True

	def search(self, s):
		node = self.root
		for i in range(len(s)):
			if s[i] not in node.chd:
				return False
			node = node.chd[s[i]]
		return node.end

	def show(self):
		stack = [self.root]
		while stack:
			node = stack.pop()
			print(node.val, node.end)
			for n in list(node.chd.keys())[::-1]:
				stack.append(node.chd[n])

trie = Trie()
trie.add('abcd')
trie.add('abc')
trie.add('fabc')
trie.show()


