

#    5
#   / \
#  3   10
# / \    \
#2   4     11

# 2 3 4 5 10 11
# if has right subtree,  left most node in the right subtree
#  find the recent parent for which it belongs to the left subtree



def inorderSucc(self, root, node):
	
	if node.right:
		node = node.right
		while node.left:
			node = node.left
		return node
	else:
		candidate = None
		cur = root
		while cur:
			if cur.val > node.val:
				candidate = cur
				cur = cure.left
			elif cur.val < node.val:
				cur = cur.right
			else:
				break

		return candidate



#    5
#   / \
#  3   10
# / \    \
#2   4     11

# 5 3 2 4 10 11
# if node has left subtree, then succ = root of the left subtree
# elif node has right subtree, then succ = root of the right subtree
# get the parent p where node belongs to the left subtree and p has a right subtree, then if p then p.right
# 

def preOrderSucc(self, root, node):

	if node.left:
		return node.left
	elif node.right:
		return node.right

	p = None
	cur = root

	while cur:
		if cur.val > node.val:
			if cur.right:
				p = cur.right
			cur = cur.left
		elif cur.val < node.val:
			cur = cur.right
		else:
			break

	return p


# left right node
#      7
#     / \
#    6   10
#   / \    \
#  2   5     11
# /   /
#1   4

#  1 2 4 5 6 11 10 7
# find node's succ
# if node.parent == NULL, then null
# node.parent.right = node. then parent
# node.parent.left = node: 
#			if parent.right: left most of the parent.right
#			else parent


class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.val = key  
        self.left = None
        self.right = None

def postOrderSucc(root, node):
	
	parent = None
	cur = root

	# get node's parent
	while cur:
		if cur.val > node.val:
			parent = cur
			cur = cur.left
		elif cur.val < node.val:
			parent = cur
			cur = cur.right
		else:
			break

	if parent is None:
		return None

	# if node is at the left of the parent
	elif parent.left == node and parent.right:
		cur = parent.right
		while cur:
			if cur.left:
				cur = cur.left
			elif cur.right:
				cur = cur.right
			else:
				break
		return cur
	else:
		return parent

def post_succ(root, node):

	if node is None:
		return None 
    
    # find the higest level parent where node is in left sub tree
	cur = root 
	candidate = None 
	while cur:
		if node.val < cur.val:
			candidate = cur.left 
			cur = cur.left 
		elif node.val > cur.val:
			cur = cur.right 
			candidate = cur.right 
		else:
			break

	if candidate:
		if candidate.right:
			cur = candidate.right 
			while cur:
				if cur.left:
					cur = cur.left 
				elif cur.right and node.val!=cur.left.val:
					cur = cur.right 
				else:
					return cur 
		else:
			return candidate

	return None 


def insert( node, data): 
  
    # 1) If tree is empty then return a new singly node 
    if node is None: 
        return Node(data) 
    else: 
         
        # 2) Otherwise, recur down the tree 
        if data <= node.val: 
            temp = insert(node.left, data) 
            node.left = temp  
            temp.parent = node 
        else: 
            temp = insert(node.right, data) 
            node.right = temp  
            temp.parent = node 
          
        # return  the unchanged node pointer 
        return node 

root  = None
  
# Creating the tree given in the above diagram  
root = insert(root, 20) 
root = insert(root, 8)
root = insert(root, 22)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 10) 
root = insert(root, 14)

node = root

while node.left:
	node = node.left

while node:
	print(node.val)
	node = postOrderSucc(root, node)

print("****************")

node = root

while node.left:
	node = node.left

c = 0
while node and c < 2:
	print(node.val)
	node = post_succ(root, node)
	c+=1





