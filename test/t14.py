

def fib(n):

	if n in mem:
		return mem[n]

	mem[n] = fib(n-1) + fib(n-2)

	return mem[n]

def fibi(n):
	mem = {1:1,2:1,}
	for i in range(3,n+1):
		mem[i] = mem[i-1] + mem[i-2]

	return mem[n]


def fibii(n):

	t1 = 1
	t2 = 1

	for i in range(3,n+1):
		temp = t2
		t2 = t1 + t2
		t1 = temp

	return t2






print(fibii(5000))