
import heapq
def getAns(N, K, M):
	D = [0]*(N-1)
	for i in range(0,N-1):
		D[i] = M[i] - M[i+1] 

	heapq.heapify(D)
	mx = -heapq.heappop(D)
	heapq.heappush(D, -mx//2)

	return -heapq.heappop(D)

def getAnsBig(N, K, M):
	D = [0]*(N-1)
	for i in range(0,N-1):
		D[i] = M[i+1] - M[i]   

	lo = 1
	hi = max(D)
	while lo < hi:
		mid = lo + (hi-lo)//2
		if check(D, mid, K):
			hi = mid
		else:
			lo = mid + 1
	return hi


def check(D, size, K):
	c = 0
	for x in D:
		c += x//size
		if x%size==0: c-=1
		if c>K:
			return False
	return True

	
def main():
	T  =  int(input())
	for i in range(T):
		N, K = [int(x) for x in input().split(' ')]
		M =  [int(x) for x in input().split(' ')]
		ans = getAnsBig(N, K, M)
		out = "Case #%s: %s"%(i+1, ans)
		print(out)


if __name__ == "__main__":
    main()