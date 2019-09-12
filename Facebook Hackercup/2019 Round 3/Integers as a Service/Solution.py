#
def solve(Q,V,R):
	#print(Q,V,R)
	
	return 1


f = open("large.txt")
f = open("small.txt")
out = open("out.txt",'w+')

T = int(f.readline())
for t in range(1,T+1):
	N = int(f.readline())   #

	Q = [0]*N
	V = [0]*N
	R = [0]*N
	for i in range(N):
		Q[i],V[i],R[i]  = f.readline().split(" ")
		V[i] = int(V[i])
		R[i] = int(R[i])


	ans = solve(Q,V,R)
	res = "Case #" + str(t) + ": " + str(ans)
	print(res)
	out.write(res+"\n")

out.close()
f.close()











