class BinaryIndexTree(object):
    def __init__(self, nums, t):
        n = len(nums)
        self.nums = [0 for _ in range(n+1)]
        self.N = [0 for _ in range(n+1)]
        s = 1
        for i, v in enumerate(nums):
            p = 1
            if t: p = i+1
            self.set(i+1, s*int(v)*p)
            s *= -1

    def _lowbit(self, a):
        return a & -a

    def set(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        while i < len(self.N):
            self.N[i] += diff
            i += self._lowbit(i)

    def get(self, i):
        ret = 0
        while i > 0:
            ret += self.N[i]
            i -= self._lowbit(i)

        return ret


class NumArray(object):
    def __init__(self, nums, t):
        self.bit = BinaryIndexTree(nums, t)

    def update(self, i, val):
        self.bit.set(i+1, val)

    def sumRange(self, i, j):
        return self.bit.get(j+1)-self.bit.get(i)
 	

def update(posTree, megaPosTree, i, val):
	posTree.update(i, val*(-1)**(i&1))
	megaPosTree.update(i, (i+1)*val*(-1)**(i&1))

def query(posTree, megaPosTree, i, j):
	val = megaPosTree.sumRange(i,j) - i*posTree.sumRange(i,j)
	return val*(-1)**(i&1)

def main():
	T  =  int(input())
	for i in range(T):
		N, Q = [int(x) for x in input().split()]
		A =  input().split()
		posTree, megaPosTree = NumArray(A, False), NumArray(A, True)
		ans = 0
		for j in range(Q):
			x,y,z = input().split()
			y = int(y)
			z = int(z)
			if x == 'Q':
				val = query(posTree, megaPosTree, y-1, z-1)
				ans += val
			else:
				update(posTree, megaPosTree, y-1, z)

		out = "Case #%s: %s"%(i+1, ans)
		print(out)

if __name__ == "__main__":
    main()