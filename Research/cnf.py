

from collections import defaultdict
import random
import bisect

def getcnf(k, elim):
	#k=6
	cl = int(2**(k/2))
	clim = cl//2

	cnf = [ [] for i in range(cl)]

	#elim = 12
	elems = set(range(1,elim+1)) | set(range(-elim, 0))
	filled = set()
	ec = defaultdict(int)
	icompleted = cl
	for i in range(cl):
		for j in range(k):
			negates = set([-x for x in cnf[i]])
			targets = elems - filled - set(cnf[i]) - negates
			#print(targets)
			if len(targets) == 0:
				break

			x = random.choice(tuple(targets))
			ec[x] += 1
			
			if ec[x] >= clim:
				break
			elif ec[x] >= clim -1:
				filled.add(x)
			bisect.insort(cnf[i], x)

		if len(cnf[i]) == k:
			icompleted -= 1
		#print()
	cnf.sort()
	return cnf, icompleted


def show(cnf):
	print(cnf)
	ec = defaultdict(int)
	for cl in cnf:
		for x in cl:
			ec[x] += 1
	arr = []
	for key in ec:
		arr.append((ec[key], key))
	arr.sort(reverse=True)
	for vh, ky in arr:
		print((ky,vh), (-ky, ec[-ky]))


def move(cnf, x):
	for cl in cnf:
	 	if x in cl:
	 		cl.clear()
	 	elif -x in cl:
	 		cl.remove(-x)

	while [] in cnf:
	 	cnf.remove([])
 	

def play(cnf):
	x,y = [int(x) for x in input().split("=")]

	if y==0:
		x *= -1


	if x==0:
		return x
	move(cnf, x)
	return x


def C(clause):
	return 2**(-len(clause))


def getbest(cnf):
	xc = {}
	mx = [float('-inf'),0]
	mxx = None
	for cl in cnf:
		pt = C(cl)
		for x in cl:
			if x not in xc:
				xc[x] = [0.0, 0.0]

			if -x not in xc:
				xc[-x] = [0.0, 0.0]

			xc[x][0] += pt
			xc[x][1] += 1

			xc[-x][0] -= pt
			if mx < xc[x]:
				mx = xc[x]
				mxx = x 

			# if mx < xc[-x]:
			# 	mx = xc[-x]
			# 	mxx = -x 


	print(xc)
	return mxx


cnf, icompleted= getcnf(6, 8)

#k=4, T..T = 1,2,3,4,5 = 9
cnf = [[1, 2, 3, 4], [-1, -2, 3, 4], [1, 2, -3,-4], [-1,-2,-3,-4], [-1, 2, -3, -4], [-1, 2, 3, 4], [1, 2, -3, 4], [-1, -2, -3, 4], [-1, 2, -3, 4]]


# k = 6, F..T = 1,2,3,4,5,6 = 18
cnf1 = [[1, 2, 3, 4, 5, 6], [-1, -2, 3, 4, 5, 6], [1, 2, -3,-4, 5, 6], [-1,-2,-3,-4, 5, 6], [-1, 2, -3, -4, 5, 6], [-1, 2, 3, 4, 5, 6], [1, 2, -3, 4, 5, 6],
       [-1, -2, -3, 4, 5, 6], [-1, 2, -3, 4, 5, 6],
       [1, 2, 3, 4,-5, 6], [-1, -2, 3, 4,-5, 6], [1, 2, -3,-4,-5, 6], [-1,-2,-3,-4,-5, 6], [-1, 2, -3, -4,-5, 6], [-1, 2, 3, 4,-5, 6], [1, 2, -3, 4,-5, 6], 
       [-1, -2, -3, 4,-5, 6], [-1, 2, -3, 4,-5, 6]]



# k=6, T..F
cnf2 = [[1,2,3,4,5,6],[1,2,-3,-4,5,6],[-1,-2,3,4,5,6],[-1,-2,-3,-4,5,6],[1,2,3,4,-5,-6],[1,2,-3,-4,-5,-6],[-1,-2,3,4,-5,-6],[-1,-2,-3,-4,-5,-6] ]

cnf11 = [tuple(sorted(c)) for c in cnf1]
cnf22 = [tuple(sorted(c)) for c in cnf2]

ans = print(set(cnf11) & set(cnf22))
print(ans)


cnf = [[-6, -2, -1, 3], [-5, 2, 3, 4], [-4, -1, 2, 3], [-4, 1, 3, 6], [-3, 1, 4, 5], [1, 2, 4, 5], [1, 4, 5, 6]]
cnf = [[-6, -5, -1, 4], [-6, -3, 1, 5], [-5, -4, -3, -2], [-5, -4, 2, 3], [-3, -1, 4, 5], [1, 2, 3, 5]]

#print("icomp=",icompleted)
#print(cnf)
#show(cnf)

# r = 0
# x = getbest(cnf)
# move(cnf, x)
# print("\n***T played:", x)
# show(cnf)
# print("F's move:")
# while play(cnf) != 0:
# 	show(cnf)
# 	x = getbest(cnf)
# 	move(cnf, x)
# 	print("\n***T played:", x)
# 	show(cnf)
# 	print("F's move:")

def Pt(cnff):
	ans = 0
	for cl in cnff:
		ans += 1.618**(-len(cl))
	return ans

cnf = [[-1, 3, 4, -5, -6, -7], [-1, 3, 4, 7], [-1, -4, -5, 7], [1, 2, -4, -5], [1, 2, 5, 6], [1, 3, 4, 5, -6, -7], [-2, -3, 5, 6], [-2, -3, -6, -7]]

print(cnf)
print(Pt(cnf))
r = 0
print("T's move:")
while play(cnf) != 0:
	#show(cnf)
	print(cnf)
	print(Pt(cnf))
	print("")
	if r%2==0:
		print("F's move:")
	else:
		print("T's move:")

	r+=1



# helo kem aso?



