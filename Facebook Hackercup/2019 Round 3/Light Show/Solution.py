#
def prefsum(pos_col):
	c1=0
	c2=0
	n = len(pos_col)
	C1=[0]*n
	C2=[0]*n

	for i in range(n):
		if pos_col[i][1]==1:
			c1+=1
		else:
			c2+=1

		C1[i] = c1
		C2[i] = c2

	return C1,C2

def getmxcon1(C1, C2, i, j):
	if i==0:
		mx = max(C1[j],C2[j])
	else:
		mx = max(C1[j] - C1[i-1], C2[j] - C2[i-1])
	return mx*(mx-1)//2

def solve(H, N, X, C):

	n = len(X)
	pos_col = sorted(zip(X,C))
	C1,C2 = prefsum(pos_col)
	
	#print(pos_col)

	dp = [0]*n

	for j in range(n):
		for i in range(j+1):
			#nmax = getmxcon1(pos_col,i,j)
			nmax = getmxcon1(C1,C2,i,j)
			if i>0:
				nmax += dp[i-1]
			
			dp[j] = max(dp[j], nmax) 



	return dp[-1]

			






















f = open("large.txt")
#f = open("small.txt")
out = open("out.txt",'w+')

T = int(f.readline())
for t in range(1,T+1):
	H,N = [int(x) for x in f.readline().split(" ")]   #

	X = [0]*N
	C = [0]*N
	for i in range(N):
		X[i],C[i]  = [int(x) for x in f.readline().split(" ")]


	ans = solve(H, N, X, C)
	res = "Case #" + str(t) + ": " + str(ans)
	print(res)
	out.write(res+"\n")

out.close()
f.close()











