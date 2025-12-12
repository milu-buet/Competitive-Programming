

class TrieNode(object):
	"""docstring for TrieNode"""
	def __init__(self, val, parent):
		self.val = val
		self.children = {}
		self.parent = parent
		self.isWord = False


	def addChild(self, with_val):
		new_val = self.val + with_val

		if new_val in self.children:
			return self.children[new_val]

		new_node = TrieNode(new_val, self)
		self.children[new_val] = new_node
		return new_node
		

	def addWordinTree(self, root, word):
		for i in range(len(word)):
			root = root.addChild(word[i])
		root.isWord = True


	def show(self):
		print(self.val)
		for key in self.children:
			self.children[key].show()


def generateTree(words):

	root =  TrieNode('',None)
	for word in words:
		root.addWordinTree(root, word)


	return root



words = ["aaaac","abc"]
root = generateTree(words)
root.show()