'''
3
0 2 3

f(M,T) = ?
f(i,j) = f(i-1,j) , S[i-1] + f(i-1, j-S[i-1])

'''


def getAns(M, T, S):
	
	Table = [[0 for i in range(M+1)] for j in range(2)]
	top = 0
	bottom = 1
	for i in range(1,T+1):
		for j in range(1, M+1):
			Table[bottom][j] = Table[top][j]
			if j>= S[i-1]:
				Table[bottom][j] = max(Table[bottom][j], S[i-1] + Table[top][j-S[i-1]])
		top ^= 1
		bottom ^= 1

	return Table[top][-1]


def main():
	while True:
		try:
			M,T  =  [int(x) for x in input().split()]
		except:
			break
		
		S = [int(x) for x in input().split()]

		ans = getAns(M,T,S)
		out = "%s"%(ans,)
		#print(out)
		print(ans)



if __name__ == "__main__":
    main()