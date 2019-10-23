
#python dict sort by val: 
sorted(freq, key=freq.__getitem__)

#Plain bfs
def bfs(root):
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
                #nlist.append(node.val)  # pre
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






    def twobst(root1, root2):

        st1 = [root1]
        vs1 = set()

        st2 = [root2]
        vs2 = set()

        while st1 or st2:
            if st1 and st1[-1] not in vs1:
                n1 = st1.pop()
                if n1.right: st1.append(n1.right)
                st1.append(n1)
                if n1.left: st1.append(n1.left)

                vs1.add(n1)

            elif st2 and st[-1] not in vs2:
                n2 = st2.pop()
                if n2.right: st2.append(n2.right)
                st2.append(n2)
                if n2.left: st2.append(n2.left)

                vss.add(n2)
            else:

                if st1 and st2 and st1[-1].val <= st2[-1],val:
                    print(st1.pop())
                elif st1 and st2 and st1[-1].val > st2[-1],val:
                    print(st2.pop())
                elif st1:
                    print(st1.pop())
                elif st2:
                    print(st2.pop())


