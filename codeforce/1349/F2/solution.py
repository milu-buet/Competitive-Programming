





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