class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r = len(board)
        c = len(board[0])
        n = len(word)
        if n == 0:
            return False
        
        for i in range(r):
            for j in range(c):
                if word[0] == board[i][j] and self.dfs(board, word, 0, i, j):
                    return True
        return False


    def dfs(self, board, word, wi, i, j):
        
        #print(wi, i, j)
        
        if wi == len(word)-1:
            return True
        
        temp = board[i][j]
        board[i][j] = '#'
        
        tr = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for a,b in tr:
            a = a+i
            b = b+j
            if a>=0 and b>=0 and a<len(board) and b<len(board[0]) and word[wi+1] == board[a][b] and self.dfs(board, word, wi+1, a, b):
                board[i][j] = temp
                return True
        board[i][j] = temp
        return False
        

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
words = ["ABCCED", "SEE", "ABCB"]

for word in words:
    print(Solution().exist(board,word))



###########
class Node():
    def __init__(self, val):
        self.val = val
        self.nbs = {}
        self.end = None


class Trie():
    def __init__(self):
        self.root = Node(None)
        
        
    def add(self, s, j):
        i=0
        node = self.root
        while i<len(s):
            if s[i] not in node.nbs:
                node.nbs[s[i]] = Node(s[i])
            node = node.nbs[s[i]]
            i+=1
        node.end = j
        
    def show(self):
        
        node = self.root
        stack = [node]
        while stack:
            node = stack.pop()
            print(node.val, node.end)
            
            for nb in node.nbs:
                stack.append(node.nbs[nb])
                
                

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        trie = Trie()
        for i,word in enumerate(words):
            trie.add(word, i)
        
        #trie.show()
        root = trie.root
        
        ans = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.nbs:
                    self.dfs(words, board, root.nbs[board[i][j]], i, j, ans)

 
        return ans
    
    
    def dfs(self, words, board, root, i, j, ans):
        
        if root.end is not None:
            ans.append(words[root.end])
            root.end = None
            
    
        tr = [(-1,0), (1,0), (0,-1), (0,1)]
        for a,b in tr:
            a = a+i
            b = b+j
            
            if a>=0 and b>=0 and a<len(board) and b<len(board[0]) and board[a][b] in root.nbs:
                temp = board[i][j]
                board[i][j] = '#'
                self.dfs(words, board, root.nbs[board[a][b]], a, b, ans)
                board[i][j] = temp

        
       
        
            
        
        
        
        
        
