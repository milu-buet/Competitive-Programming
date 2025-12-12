# Md Lutfar Rahman
# mrahman9@memphis.edu
# milu.buet@gmail.com
# University of Memphis


import math
from collections import defaultdict
import random
import bisect
s = 1.618033
#s = 1.9

class TTgame(object):
	"""docstring for TTgame"""
	def __init__(self,n):
		A = list(range(-n, n+1))
		A.remove(0)
		A.sort()

		self.played = set()
		self.A = A
	def Pi(self, cnf, li):
		ans = 0
		for cl in cnf:
			if li in cl:
				ans += s**(-len(cl))
		return ans

	def Pr(self, cnf, li):
		return self.Pi(cnf, li) - (s-1)*self.Pi(cnf, -li)


	# get potential of clauses where li,-li,lj,-lj occurs
	def Pf(self, cnf, li, lj):
		ans = 0
		for cl in cnf:
			if li in cl or -li in cl or lj in cl or -lj in cl:
				ans += s**(-len(cl))
		return ans

	def Pu(self, cnf, li, lj):
		ans = 0
		for cl in cnf:
			if li in cl and lj in cl:
				ans += s**(-len(cl))
		return ans

	def Pv(self, cnf, li, lj):
		ans = 0
		for cl in cnf:
			if li in cl and lj not in cl and -lj not in cl:
				ans += s**(-len(cl))
		return ans		

	# get total potential of cnf
	def Pt(self, cnf):
		ans = 0
		for cl in cnf:
			ans += s**(-len(cl))
		return ans		

	# for li,lj pair in cnf
	def get_vars(self, cnf, li, lj):
		a = self.Pu(cnf, li, lj)
		b = self.Pu(cnf, li, -lj)
		c = self.Pv(cnf, li, lj)

		d = self.Pu(cnf, -li, lj)
		e = self.Pu(cnf, -li, -lj)
		f = self.Pv(cnf, -li, lj)

		g = self.Pv(cnf, lj, li)
		h = self.Pv(cnf, -lj, li)

		return a,b,c,d,e,f,g,h


	def check_delay_pair(self, cnf, li, lj):

		a,b,c,d,e,f,g,h = self.get_vars(cnf, li, lj)
		area = a+e - (s**2-1)*(b+d) - (s-1)*(c+f+g+h)
		return area

	def search_delay_pair(self, cnf, n):

		A = self.A

		pair = None
		pval = 0

		for i in range(len(A)):
			for j in range(i+1, len(A)):
				if A[i]!=-A[j] and A[i] not in self.played and A[j] not in self.played :
					val = self.check_delay_pair(cnf, A[i], A[j])
					if val >= pval:
						pval = val 
						pair = A[i],A[j]	
		return pair

	def use_delay_pair(self, cnf, n, li, lj):
		cnf_new = []
		for cl in cnf:
			if not ((li in cl and lj in cl) or (-li in cl and -lj in cl)):
				cl_new = list(cl)
				if li in cl_new:
					cl_new.remove(li)
				if -li in cl_new:
					cl_new.remove(-li)
				if lj in cl_new:
					cl_new.remove(lj)
				if -lj in cl_new:
					cl_new.remove(-lj)

				if cl_new not in cnf_new:
					#print(cl)
					cnf_new.append(cl_new)
		self.played.add(li)
		self.played.add(-li)
		self.played.add(lj)
		self.played.add(-lj)
		return cnf_new


	# search delay pairs and reduce cnf
	def resolve_delay_pairs(self, cnf, n):
		while True:
			pair = self.search_delay_pair(cnf, n)
			if pair is None:
				break
			li, lj = pair 
			print("resolved by delay pair=",li,lj)
			#print(cnf)
			cnf = self.use_delay_pair(cnf, n, li, lj)
			#print(cnf)

			print("Potential=",self.Pt(cnf))
		return cnf

	# check if li=1 is a good move for T in the cnf
	def get_problem(self, cnf, li, msg=None):
		A = self.A 
		for lj in A:
			if lj != li and lj != -li:
				a,b,c,d,e,f,g,h = self.get_vars(cnf, li, lj)
				if a+b+c+d+g < (s**2-1)*e + (s-1)*(f+h):
					if msg:
						print("problem found")
						print(li, lj, cnf)
					return lj
		return None	

	# T's strategy
	def Tplay(self, cnf, n):
	
		if not(len(cnf) == 0 or len(cnf[0]) == 0):

			cnf = self.resolve_delay_pairs(cnf, n)
			
			li  = self.getMaxPr(cnf, n)
			lj = self.get_problem(cnf, li)
		
			if lj is None: # li=1 is valid move
				print("resolved by simple early:", li)
				cnf = self.move(cnf, li)
				return cnf
			else:
				lk1 = self.get_problem(cnf, -lj)
				lk2 = self.get_problem(cnf, -li)
				if lk1 is None: # lj=0 is a valid move
					print("resolved by advanced early1:", -lj)
					print(cnf)
					cnf = self.move(cnf, -lj)
					#print("Potential=",self.Pt(cnf))
					return cnf
				elif lk2 is None: # li=0 is a valid move
					print("resolved by advanced early2:", -li)
					print(cnf)
					cnf = self.move(cnf, -li)
					#print("Potential=",self.Pt(cnf))
					return cnf
				else:
					print("Error")
					return [[]]
		return cnf

	def Fplay(self, cnf, n):
		print("F move:")
		x,y = [int(x) for x in input().split("=")]
		if y==0:
			x *= -1
		if x==0:
			return None
		cnf = self.move(cnf, x)
		return cnf

	def move(self, cnf, x):
		cnf_new = []
		for cl in cnf:
			new_cl = list(cl)
			if x not in cl:
				if -x in cl:
					new_cl.remove(-x)
				cnf_new.append(new_cl)
		self.played.add(x)
		self.played.add(-x)
		return cnf_new

	def getMaxPr(self, cnf, n):
		A = self.A
		px = -1
		li = None
		for i in range(len(A)):
			if A[i] not in self.played:
				v = self.Pr(cnf, A[i])
				if  v > px:
					px = v
					li = A[i]
		return li

	def Fplayauto(self, cnf, n):
		li = self.getMaxPr(cnf, n)
		print("F played",li)
		cnf = self.move(cnf, -li)
		self.lastF = li
		return cnf


	# create a random uniform k-CNF with n variables
	def getcnf(self, k, n):

		cl = int(s**k)
		clim = cl
		cnf = [ [] for i in range(cl)]

		elems = set(range(1,n+1)) | set(range(-n, 0))
		filled = set()
		ec = defaultdict(int)
		icompleted = cl
		for i in range(cl):
			for j in range(k):
				negates = set([-x for x in cnf[i]])
				targets = elems - filled - set(cnf[i]) - negates
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
		cnf.sort()
		return cnf


# Main driver programe
def Main():
	# settings
	n = 15 # number of variables = |X|
	k = 9  # width of the cnf
	s = 1.618033 # target ratio
	TotalGameCount=100


	TWinCount = 0
	for i in range(TotalGameCount):
		obj=TTgame(n)
		cnf= obj.getcnf(k, n) # create a random k uniform CNF with n variables
		cnfs = [] # deep copy of cnf
		for cl in cnf:
			ncl = list(cl)
			cnfs.append(ncl)
		print("Potential=",obj.Pt(cnf))
		cnf = obj.Tplay(cnf, n)
		while cnf and len(cnf[0]) > 0:
			cnf = obj.Fplayauto(cnf, n)
			print("Potential=",obj.Pt(cnf))
			cnf = obj.Tplay(cnf, n)
		if len(cnf)==0:
			print("************T wins****************",TWinCount)
			TWinCount+=1
		else:
			print(cnfs)
			print(cnf)
			print("************F wins****************",TWinCount)
			#break
	if TWinCount==TotalGameCount:
		print('success!!! T wins all of them')

Main()
