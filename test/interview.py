
class Board(object):
	"""docstring for Board"""
	def __init__(self):
		self.board = []

		for i in range(3):
			row = ['-']*3
			self.board.append(row)


	def addToken(self, i, j, val):
		
		if i<0 or i>2 or j<0 or j>2:
			return False

		if self.board[i][j]=='X' or self.board[i][j]=='O':
			return False

		if val=='X' or val=='O':
			self.board[i][j] = val
			return True

		return False


	def print2(self):

		for row in self.board:
			print(row)

	def print(self):

		for row in self.board:
			for c in row[:-1]:
				print('%s|'%(c), end='')

			print(row[-1])

	def isFull(self):
		added=0
		for i in range(3):
			for j in range(3):
				if self.board[i][j]!='-':
					added+=1
				

		return added==9


	def findBlank(self):
		for i in range(3):
			for j in range(3):
				if self.board[i][j] == '-':
					return (i,j)




class AI(object):
	"""docstring for AI"""
	def __init__(self, board):
		self.borad = board

	
	def findMoveSimple(self):
		if self.board.isFull():
			raise Exception('No valid moves')

		i,j = self.board.findBlank()


	def makeMove(self, i, j):
		self.borad.addToken(i,j,'O')



		


b = Board()
b.print()


b.addToken(2,0,'X')
b.print()
print(b.isFull())

for i in range(3):
	for j in range(3):
		b.addToken(i,j,'X')

print(b.isFull())

		