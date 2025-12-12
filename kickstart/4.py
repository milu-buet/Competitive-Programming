class Node(object):
	def __init__(self, val):
		self.val = val
		self.children = {}
		self.end = 0
		self.c = 0

class Trie(object):
	"""docstring for Trie"""
	def __init__(self):
		self.root = Node(None)

	def add(self, s):
		node = self.root
		#node.c += 0
		for i in range(len(s)):
			if s[i] not in node.children:
				node.children[s[i]] = Node(s[i])
			node = node.children[s[i]]
			node.c+=1
		node.end += 1

	def show(self, K):
		ans = 0
		stack = [self.root]
		while stack:
			node = stack.pop()
			ans += (node.c//K)
			for n in node.children:
				stack.append(node.children[n])
		return ans

def getAns(N, K, M):
	trie = Trie()
	for s in M:
		trie.add(s)

	return trie.show(K)


	
def main():
	T  =  int(input())
	for i in range(T):
		N, K = [int(x) for x in input().split(' ')]
		S =  []
		#print(N, K)
		for j in range(N):
			S.append(input())
			#print(S[-1])

		ans = getAns(N, K, S)
		out = "Case #%s: %s"%(i+1, ans)
		print(out)


if __name__ == "__main__":
    main()