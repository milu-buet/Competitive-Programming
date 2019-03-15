
#python dict sort by val: 
sorted(freq, key=freq.__getitem__)

#Plain bfs
bfs(root):
	if root == None:
		return

	queue = [root]

	while root:
		queue.push(root.left)
		queue.push(root.right)

		root = queue.pop()
		print(root.val)


#dfs_itarative
    def Traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        nlist = []
        stack = []
        
        node = root
        while node or stack:
            while node:
                nlist.append(node.val)  # pre
                stack.append(node)
                node = node.left
                
            node = stack[-1]
            stack.pop()

            nlist.append(node.val)  # in
            
            node = node.right
            
            
        return nlist


    def post_order_Ita(self, root, nlist):  #post
        
        stack = []
        
        node = root, False
        while node[0] or stack:
            while node[0]:
                stack.append(node)
                node = node[0].left, False
                
            node = stack[-1]
            stack.pop()
            if node[1] == False:
                stack.append((node[0],True))
                node = node[0].right, False
            else:
                nlist.append(node[0].val)
                node = None, False
            
            
            
            
        return nlist


### construct tree from pre post
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        
        nodes = {}
        root = TreeNode(pre[0])
        nodes[pre[0]] = root
        
        for i in range(1,len(pre)):
            node = TreeNode(pre[i])
            nodes[pre[i]] = node
            p_i = post.index(pre[i])
            
            if post[p_i+1] in nodes:
                nodes[post[p_i+1]].right = node
            
            else:
                nodes[pre[i-1]].left = node
            
            
            
            
        return root