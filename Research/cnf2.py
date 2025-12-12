
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

		self.pr = {}
		self.A = A
		self.lastF = None
	def Pi(self, cnf, li):
		ans = 0
		for cl in cnf:
			if li in cl:
				ans += s**(-len(cl))
		return ans

	def Qi(self, cnf, li):
		return self.Pi(cnf, li) - (s-1)*self.Pi(cnf, -li)


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

	def Pt(self, cnf):
		ans = 0
		for cl in cnf:
			ans += s**(-len(cl))
		return ans		

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
				if A[i]!=-A[j] and A[i] not in self.played and A[j] not in self.played and A[i] not in self.pr and A[j] not in self.pr :
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

	def use_delay_pair2(self, cnf, n, li, lj):
		cnf_new = []
		for cl in cnf:
			cl_new = list(cl)

			# a
			if li in cl_new and lj in cl_new:
				pass
			# b
			elif li in cl_new and -lj in cl_new:
				cl_new.remove(li)
				cl_new.remove(-lj)

				one = cl_new + [li]
				two = cl_new + [-li, -lj]

				cnf_new.append(one)
				cnf_new.append(two)

			# c
			elif li in cl_new and lj not in cl_new and -lj not in cl_new:
				cl_new.remove(li)

				one = cl_new + [li]
				two = cl_new + [-li, -lj]

				cnf_new.append(one)
				cnf_new.append(two)
			# d
			elif -li in cl_new and lj in cl_new:
				cl_new.remove(-li)
				cl_new.remove(lj)

				one = cl_new + [lj]
				two = cl_new + [-li, -lj]

				cnf_new.append(one)
				cnf_new.append(two)

			# e
			elif -li in cl_new and -lj in cl_new:
				pass
			# f
			elif -li in cl_new and lj not in cl_new and -lj not in cl_new:
				cl_new.remove(-li)

				one = cl_new + [lj]
				two = cl_new + [-li, -lj]

				cnf_new.append(one)
				cnf_new.append(two)
			# g
			elif li not in cl_new and -li not in cl_new and lj in cl_new:
				cl_new.remove(lj)

				one = cl_new + [lj]
				two = cl_new + [-li, -lj]

				cnf_new.append(one)
				cnf_new.append(two)
			# h
			elif li not in cl_new and -li not in cl_new and -lj in cl_new:
				cl_new.remove(-lj)

				one = cl_new + [li]
				two = cl_new + [-li, -lj]

				cnf_new.append(one)
				cnf_new.append(two)
			else:
				cnf_new.append(cl_new)
		self.pr[li] = lj
		self.pr[lj] = li
		self.pr[-li] = -lj
		self.pr[-lj] = -li
		return cnf_new

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

	# def find_avanced_early(self, cnf, n, li):
	# 	A = self.A 
	# 	for lj in A:
	# 		if lj != li and lj != -li:
	# 			a,b,c,d,e,f,g,h = self.get_vars(cnf, li, lj)
	# 			if a+b+c+d+g < (s**2-1)*e + (s-1)*(f+h):
	# 				#print("problem found")
	# 				#print(li, lj, cnf)
	# 				return -lj
	# 	return None


	# def search_problem(self, cnf, lii, li):
	# 	A = self.A 
	# 	for lj in A:
	# 		if lj != li and lj != -li:
	# 			a,b,c,d,e,f,g,h = self.get_vars(cnf, li, lj)
	# 			if a+b+c+d+g < (s**2-1)*e + (s-1)*(f+h):
	# 				print("problem found")
	# 				print(lii, li, lj, cnf)
	# 				return True
	# 	return False

	# def search_problem(self, cnf, lii, li):
	# 	A = self.A 
	# 	for lj in A:
	# 		if lj != li and lj != -li:
	# 			a,b,c,d,e,f,g,h = self.get_vars(cnf, li, lj)
	# 			if a+b+c+d+g < (s**2-1)*e + (s-1)*(f+h):
	# 				print("problem found")
	# 				print(lii, li, lj, cnf)
	# 				return True
	# 	return False
	

	def Tplay(self, cnf, n):
	
		cnf = self.resolve_delay_pairs(cnf, n)
		if len(cnf) == 0 or len(cnf[0]) == 0:
			return cnf
		li  = self.getMaxQi(cnf, n)
	
		print("resolved by simple early:", li)
		cnf = self.move(cnf, li)
		return cnf

	def get_problem(self, cnf, li, msg=None):
		A = self.A 
		for lj in A:
			if lj not in self.pr and lj != li and lj != -li :
				a,b,c,d,e,f,g,h = self.get_vars(cnf, li, lj)
				if a+b+c+d+g < (s**2-1)*e + (s-1)*(f+h):
					if msg:
						print("problem found")
						print(li, lj, cnf)
					return lj
		return None	

	def Tplay2(self, cnf, n):

		if self.lastF is not None and self.lastF in self.pr:
			li = self.pr[self.lastF]
			cnf = self.move(cnf, li)
			print("resolved by future delay:", li, self.lastF)

			self.pr.pop(li)
			self.pr.pop(-li)
			self.pr.pop(self.lastF)
			self.pr.pop(-self.lastF)
			
			self.lastF = None
			return cnf
	
		while not(len(cnf) == 0 or len(cnf[0]) == 0):

			cnf = self.resolve_delay_pairs(cnf, n)
			
			li  = self.getMaxQi2(cnf, n)
			lj = self.get_problem(cnf, li)
		
			if lj is None:
				print("resolved by simple early:", li)
				cnf = self.move(cnf, li)
				return cnf
			else:
				cnf = self.use_delay_pair2(cnf, n, li, lj)
				print("resolved by early delay:", li, lj)
				#print("Potential=",self.Pt(cnf))
		return cnf

	def Tplay3(self, cnf, n):
	
		if not(len(cnf) == 0 or len(cnf[0]) == 0):

			cnf = self.resolve_delay_pairs(cnf, n)
			
			li  = self.getMaxQi2(cnf, n)
			lj = self.get_problem(cnf, li)
		
			if lj is None:
				print("resolved by simple early:", li)
				cnf = self.move(cnf, li)
			else:
				print("resolved by advanced early:", li, -lj)
				print("T played:", -lj)
				lk = self.get_problem(cnf, -lj, True)
				if lk:
					return [[]]
				cnf = self.move(cnf, -lj)
		return cnf

	def Tplay4(self, cnf, n):
	
		while not(len(cnf) == 0 or len(cnf[0]) == 0):

			cnf = self.resolve_delay_pairs(cnf, n)
			
			li  = self.getMaxQi2(cnf, n)
			lj = self.get_problem(cnf, li)
		
			if lj is None:
				print("resolved by simple early:", li)
				cnf = self.move(cnf, li)
				return cnf
			else:
				cnf = self.use_delay_pair2(cnf, n, li, lj)
				print("resolved by early delay:", li, lj)
				print(cnf)
				print("Potential=",self.Pt(cnf))
		return cnf

	def Tplay5(self, cnf, n):
		if self.lastF is not None and self.lastF in self.pr:
			li = self.pr[self.lastF]
			cnf = self.move(cnf, li)
			print("resolved by future delay:", li, self.lastF)

			self.pr.pop(li)
			self.pr.pop(-li)
			self.pr.pop(self.lastF)
			self.pr.pop(-self.lastF)
			
			self.lastF = None
			return cnf
	
		while not(len(cnf) == 0 or len(cnf[0]) == 0):

			cnf = self.resolve_delay_pairs(cnf, n)
			
			li  = self.getMaxQi2(cnf, n)
			lj = self.get_problem(cnf, li)
		
			if lj is None:
				print("resolved by simple early:", li)
				cnf = self.move(cnf, li)
				return cnf
			else:
				lk = self.get_problem(cnf, -lj)
				if lk is None:
					print("resolved by advanced early:", -lj)
					cnf = self.move(cnf, -lj)
					#print("Potential=",self.Pt(cnf))
					return cnf
				else:
					cnf = self.use_delay_pair2(cnf, n, li, lj)
					print("resolved by advanced delay pair:", li, lj)
					print("Potential=",self.Pt(cnf))
					#print(cnf)
					#print("Potential=",self.Pt(cnf))
		return cnf

	def Tplay6(self, cnf, n):
	
		if not(len(cnf) == 0 or len(cnf[0]) == 0):

			cnf = self.resolve_delay_pairs(cnf, n)
			
			li  = self.getMaxQi2(cnf, n)
			lj = self.get_problem(cnf, li)
		
			if lj is None:
				print("resolved by simple early:", li)
				cnf = self.move(cnf, li)
				return cnf
			else:
				lk1 = self.get_problem(cnf, -lj)
				lk2 = self.get_problem(cnf, -li)
				if lk1 is None:
					print("resolved by advanced early:", -lj)
					cnf = self.move(cnf, -lj)
					#print("Potential=",self.Pt(cnf))
					return cnf
				elif lk2 is None:
					print("resolved by advanced early:", -li)
					cnf = self.move(cnf, -li)
					#print("Potential=",self.Pt(cnf))
					return cnf
				else:
					#print("Error")
					#return [[]]
					print("resolved by ultra early:", -li)
					cnf = self.move(cnf, -li)
					#print("Potential=",self.Pt(cnf))
					return cnf

		return cnf
	def Tplay7(self, cnf, n):
		
			if not(len(cnf) == 0 or len(cnf[0]) == 0):

				cnf = self.resolve_delay_pairs(cnf, n)
				
				li  = self.getMaxQi2(cnf, n)
				lj = self.get_problem(cnf, li)
			
				if lj is None:
					print("resolved by simple early:", li)
					cnf = self.move(cnf, li)
					return cnf
				else:
					li, lj = None, None
					for lp in self.A:
						if lp not in self.played and lp not in self.pr:
							li = lp
							lj = self.get_problem(cnf, li)
							if lj is None:
								break

							li = -lp
							lj = self.get_problem(cnf, li)
							if lj is  None:
								break

					if lj is None:
						print("resolved by smart early:", li)
						cnf = self.move(cnf, li)
						return cnf
					else:
						li  = self.getMaxQi2(cnf, n)
						print("resolved by hopeless early:", li, ">" ,lj)
						cnf = self.move(cnf, li)
						return cnf




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


	def move_(self, cnf, x):
		cnf_new = []
		for cl in cnf:
			new_cl = list(cl)
			if x not in cl:
				if -x in cl:
					new_cl.remove(-x)
				cnf_new.append(new_cl)
		return cnf_new


	def move(self, cnf, x):
		cnf_new = self.move_(cnf, x)
		self.played.add(x)
		self.played.add(-x)
		return cnf_new

	def getMaxQi(self, cnf, n):
		A = self.A
		px = -1
		li = None
		for i in range(len(A)):
			if A[i] not in self.played:
				v = self.Qi(cnf, A[i])
				if  v > px:
					px = v
					li = A[i]
		return li

	def getMaxQi2(self, cnf, n):
		A = self.A

		px = -1
		li = None
		for i in A:
			if i not in self.played and i not in self.pr:
				v = self.Qi(cnf, i)
				if  v > px:
					px = v
					li = i
		return li

	def Fplayauto(self, cnf, n):

		li = None
		prev = self.Pt(cnf)
		for lf in self.A:
			if lf not in self.played and lf not in self.pr: 
				now = self.Pt(self.move_(cnf, lf))
				if prev < now:
					li = lf 
					break
		
		if li is None:
			li = self.getMaxQi(cnf, n)
		else:
			print("Tricky F's move")
			li = -li

		#li = self.getMaxQi(cnf, n)
		print("F played",-li)
		cnf = self.move(cnf, -li)
		self.lastF = -li
		return cnf



	def getcnf(self, k, elim, pot=s):
		#k=6
		cl = int(pot**k)
		clim = cl

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

	def check_two_delay(self, A, cnf, n):
		for i in range(len(A)):
			for j in range(i+1, len(A)):
				if A[i]!=-A[j]:
					li = A[i]
					lj = A[j]
					a,b,c,d,e,f,g,h = self.get_vars(cnf, li, lj)
					c1 = a+b+c+e+h >= s*d + (1/s)*(f+g)
					c2 = a+d+e+f+g >= s*b + (1/s)*(c+h)
					if  c1 and  c2:
						#print("found")
						return False
		return True

	def find_cnf(self):
		n,k =10,6
		A = list(range(-n, n+1))
		A.remove(0)
		A.sort()

		for i in range(10000):
			cnf,im = self.getcnf(k,n)
			if self.check_two_delay(A, cnf, n):
				print(cnf)
				return
			print(i)

def exp1():
	a = 0
	b=1
	for i in range(b):
		n = 7
		w, pot = 9, s
		obj=TTgame(n)
		cnf,im = obj.getcnf(w, n, pot)
		#cnf = [[-9, -8, 2, 3, 6], [-9, -6, -4, 2, 3], [-9, -5, -3, -2, 7], [-9, -2, 1, 5, 6], [-8, -6, 2, 3, 5], [-7, -6, -4, -3, -2], [-7, -6, -4, -3, 9], [-7, -3, 2, 5, 8], [-7, -1, 3, 4, 9], [-6, -2, 1, 4, 8], [-3, -1, 2, 6, 8]]
		#cnf = [[-8, 2, 3, 6], [-6, -4, 2, 3], [-5, -3, -2], [-2, 1, 5, 6], [-8, -6, 2, 3, 5], [-6, -2, 1, 4, 8], [-3, -1, 2, 6, 8]]
		#cnf = [[1,2],[-1]]
		#cnf = [[1,2], [-1,-3], [-1,3,4]]
		#cnf = [[-6, -5, -1, 4], [-6, -3, 1, 5], [-5, -4, -3, -2], [-5, -4, 2, 3], [-3, -1, 4, 5], [1, 2, 3, 5]]
		#cnf = [[-14, -13, -12, -10, -6, -5, -3, 4], [-14, -13, -12, -9, -7, -4, -2, 6], [-14, -13, -12, -4, -2, 3, 5, 10], [-14, -13, -11, -2, 1, 3, 4, 5], [-14, -12, -10, -9, -7, 2, 4, 13], [-14, -12, -9, -8, -2, -1, 3, 13], [-14, -11, -8, -4, 1, 5, 6, 13], [-14, -11, -7, -4, 5, 8, 9, 13], [-14, -10, -9, 3, 4, 6, 8, 12], [-14, -9, -7, -6, -5, -3, 10, 12], [-14, -7, -3, -2, -1, 8, 10, 11], [-13, -12, -10, -5, 4, 9, 11, 14], [-13, -12, -9, -6, -1, 7, 10, 14], [-13, -12, -6, -3, 1, 4, 5, 10], [-13, -11, -10, -7, -2, 1, 4, 6], [-13, -10, -9, -6, -5, -3, 2, 11], [-13, -10, -9, -5, 1, 3, 6, 8], [-13, -10, -8, -6, -2, 4, 11, 12], [-13, -10, -7, 4, 5, 6, 8, 14], [-13, -10, -3, 1, 2, 4, 6, 11], [-13, -9, -7, -6, -4, 1, 2, 12], [-13, -9, -5, -2, 1, 7, 10, 11], [-13, -4, 1, 3, 8, 9, 12, 14], [-12, -11, -8, -2, 3, 4, 7, 10], [-12, -8, -7, -6, -2, 5, 11, 13], [-12, -6, -3, -2, 4, 8, 10, 14], [-12, -5, -3, 2, 4, 8, 11, 14], [-12, 2, 3, 5, 9, 10, 13, 14], [-11, -10, -8, -5, -2, -1, 4, 6], [-11, -9, -8, -5, -3, 2, 7, 14], [-11, -8, -6, -3, 5, 7, 9, 13], [-11, -8, 1, 2, 7, 9, 13, 14], [-11, -7, -6, -2, -1, 4, 12, 14], [-11, -6, -4, -3, -1, 2, 12, 13], [-11, -6, -4, -3, 1, 2, 8, 10], [-11, -6, -3, -2, -1, 4, 9, 13], [-11, -2, 1, 4, 6, 7, 8, 14], [-10, -9, -8, -4, 1, 2, 11, 12], [-10, -9, -4, 2, 3, 7, 11, 13], [-10, -9, 4, 5, 7, 11, 13, 14], [-9, -8, -7, -5, -2, 4, 10, 13], [-9, 1, 2, 3, 4, 10, 13, 14], [-8, -7, -2, 1, 5, 6, 9, 11], [-8, -6, -4, 2, 3, 7, 9, 14], [-8, -2, 3, 4, 7, 10, 12, 13], [-6, -5, -4, -2, 3, 7, 12, 13]]
		#cnf = [[-13, -12, -2, 3, 5, 10], [-12, -9, -8, -2, -1, 3, 13], [-13, -10, -9, -5, -3, 2, 11], [-13, -9, 1, 2, 12], [-13, -9, -5, -2, 1, 10, 11], [-13, 1, 3, 8, 9, 12], [-12, -8, -2, 5, 11, 13], [-12, 2, 3, 5, 9, 10, 13], [-11, -8, -3, 5, 9, 13], [-11, -3, -1, 2, 12, 13], [-11, -3, 1, 2, 8, 10], [-10, -9, -8, 1, 2, 11, 12], [-10, -9, 2, 3, 11, 13], [-5, -2, 3, 12, 13]]

		#cnf = [[-7, -4, -2, 3, 5, 10], [-9, -7, -8, -2, -1, 3, 4], [-10, -9, -5, -4, -3, 2, 11], [-9, -4, 1, 2, 7], [-9, -5, -4, -2, 1, 10, 11], [-4, 1, 3, 8, 9, 7], [-8, -7, -2, 5, 11, 4], [-7, 2, 3, 5, 9, 10, 4], [-11, -8, -3, 5, 9, 4], [-11, -3, -1, 2, 7, 4], [-11, -3, 1, 2, 8, 10], [-10, -9, -8, 1, 2, 11, 7], [-10, -9, 2, 3, 11, 4], [-5, -2, 3, 7, 4]]		
		#cnf = [[-5, -3, 4], [-5, -1, 3], [-4, -2, -1], [-2, 4, 5], [3, 4, 5]]
		#print(obj.Pt(cnf))
		#cnf = [[1,3],[2,4],[-1,-2],[-3,-4]]
		cnf = [[-1,2], [-2,3], [-3,4], [-4,5], [-5, 1]]
		cnf = [[-1, 3, 4, -5, -6, -7], [-1, 3, 4, 7], [-1, -4, -5, 7], [1, 2, -4, -5], [1, 2, 5, 6], [1, 3, 4, 5, -6, -7], [-2, -3, 5, 6], [-2, -3, -6, -7]]
		
		# cnf = [[3, 4, -5, -6, -7], [3, 4, 7], [-4, -5, 7], [-3, 5, 6], [-3, -6, -7]] # 1, 2
		# cnf = [[-1, 4, -5, -6, -7], [-1, 4, 7], [-1, -4, -5, 7], [1, -4, -5], [1, 5, 6], [1, 4, 5, -6, -7]] # -2, -3 ***
		# cnf = [[-1, -5, 7], [1, 2, -5], [1, 2, 5, 6], [-2, 5, 6], [-2, -6, -7]] # 3, 4 ***
		# cnf = [[-1, 3, 7], [1, 2, 6], [1, 3, -6, -7], [-2, -3, 6], [-2, -3, -6, -7]] # -4, -5
		# cnf = [[-1, 3, 4, -7], [-1, 3, 4, 7], [-1, -4, 7], [1, 2, -4], [-2, -3, -7]] # 5, 6
		# cnf = [[-1, 3, 4], [-1, -4, -5], [1, 2, -4, -5], [1, 2, 5], [-2, -3, 5]] #-6, -7  ***
		# cnf = [[2, -4, -5], [2, 5, 6], [3, 4, 5, -6], [-2, -3, 5, 6], [-2, -3, -6]] #7, -1
		
		cnfs = []
		for cl in cnf:
			ncl = list(cl)
			cnfs.append(ncl)
		print(cnf)
		print("Potential=",obj.Pt(cnf))
		cnf = obj.Tplay7(cnf, n)
		#print("Potential=",obj.Pt(cnf))
		while cnf and len(cnf[0]) > 0:
			print(cnf)
			#cnf = obj.Fplay(cnf, n)
			cnf = obj.Fplayauto(cnf, n)
			print(cnf)
			print("Potential=",obj.Pt(cnf))
			cnf = obj.Tplay7(cnf, n)
			#print("Potential=",obj.Pt(cnf))
		#print(cnf)
		if len(cnf)==0:
			print("************T wins****************",a)
			a+=1
		else:
			print(cnfs)
			print(cnf)
			print("************F wins****************",a)
			#break
	if a==b:
		print('success!!!')

#exp1()

# def exp2():
# 	obj=TTgame(10)
# 	obj.find_cnf()

# exp2()




#[[-6, -5, -4, 1], [-6, -1, 3, 4], [-5, -1, 3, 4], [-4, 1, 3, 6], [-3, -2, 1, 5], [-3, -1, 2, 6], [-3, -1, 5, 6]]
#[[-6, -5, -1, 4], [-6, -3, 1, 5], [-5, -4, -3, -2], [-5, -4, 2, 3], [-3, -1, 4, 5], [1, 2, 3, 5]]


def exp2():
	n=14
	obj=TTgame(n)
	cnf = [[-13, -12, -2, 3, 5, 10], [-12, -9, -8, -2, -1, 3, 13], [-13, -10, -9, -5, -3, 2, 11], [-13, -9, 1, 2, 12], [-13, -9, -5, -2, 1, 10, 11], [-13, 1, 3, 8, 9, 12], [-12, -8, -2, 5, 11, 13], [-12, 2, 3, 5, 9, 10, 13], [-11, -8, -3, 5, 9, 13], [-11, -3, -1, 2, 12, 13], [-11, -3, 1, 2, 8, 10], [-10, -9, -8, 1, 2, 11, 12], [-10, -9, 2, 3, 11, 13], [-5, -2, 3, 12, 13]]

	#cnf = [[-7, -4, -2, 3, 5, 10], [-9, -7, -8, -2, -1, 3, 4], [-10, -9, -5, -4, -3, 2, 11], [-9, -4, 1, 2, 7], [-9, -5, -4, -2, 1, 10, 11], [-4, 1, 3, 8, 9, 7], [-8, -7, -2, 5, 11, 4], [-7, 2, 3, 5, 9, 10, 4], [-11, -8, -3, 5, 9, 4], [-11, -3, -1, 2, 7, 4], [-11, -3, 1, 2, 8, 10], [-10, -9, -8, 1, 2, 11, 7], [-10, -9, 2, 3, 11, 4], [-5, -2, 3, 7, 4]]		

	print(obj.Pt(cnf))
	print(obj.Qi(cnf, 1))
	print(obj.Qi(cnf, 4))
	
	a,b,c,d,e,f,g,h = obj.get_vars(cnf, 4, -1)
	print("a=",a)
	print("b=",b)
	print("c=",c)
	print("d=",d)
	print("e=",e)
	print("f=",f)
	print("g=",g)
	print("h=",h)


exp2()


# problem found
# 13 -1 [[-13, -12, -2, 3, 5, 10], [-12, -9, -8, -2, -1, 3, 13], [-13, -10, -9, -5, -3, 2, 11], [-13, -9, 1, 2, 12], [-13, -9, -5, -2, 1, 10, 11], [-13, 1, 3, 8, 9, 12], [-12, -8, -2, 5, 11, 13], [-12, 2, 3, 5, 9, 10, 13], [-11, -8, -3, 5, 9, 13], [-11, -3, -1, 2, 12, 13], [-11, -3, 1, 2, 8, 10], [-10, -9, -8, 1, 2, 11, 12], [-10, -9, 2, 3, 11, 13], [-5, -2, 3, 12, 13]]

# [[-14, -13, -12, -10, -6, -5, -3, 4], [-14, -13, -12, -9, -7, -4, -2, 6], [-14, -13, -12, -4, -2, 3, 5, 10], [-14, -13, -11, -2, 1, 3, 4, 5], [-14, -12, -10, -9, -7, 2, 4, 13], [-14, -12, -9, -8, -2, -1, 3, 13], [-14, -11, -8, -4, 1, 5, 6, 13], [-14, -11, -7, -4, 5, 8, 9, 13], [-14, -10, -9, 3, 4, 6, 8, 12], [-14, -9, -7, -6, -5, -3, 10, 12], [-14, -7, -3, -2, -1, 8, 10, 11], [-13, -12, -10, -5, 4, 9, 11, 14], [-13, -12, -9, -6, -1, 7, 10, 14], [-13, -12, -6, -3, 1, 4, 5, 10], [-13, -11, -10, -7, -2, 1, 4, 6], [-13, -10, -9, -6, -5, -3, 2, 11], [-13, -10, -9, -5, 1, 3, 6, 8], [-13, -10, -8, -6, -2, 4, 11, 12], [-13, -10, -7, 4, 5, 6, 8, 14], [-13, -10, -3, 1, 2, 4, 6, 11], [-13, -9, -7, -6, -4, 1, 2, 12], [-13, -9, -5, -2, 1, 7, 10, 11], [-13, -4, 1, 3, 8, 9, 12, 14], [-12, -11, -8, -2, 3, 4, 7, 10], [-12, -8, -7, -6, -2, 5, 11, 13], [-12, -6, -3, -2, 4, 8, 10, 14], [-12, -5, -3, 2, 4, 8, 11, 14], [-12, 2, 3, 5, 9, 10, 13, 14], [-11, -10, -8, -5, -2, -1, 4, 6], [-11, -9, -8, -5, -3, 2, 7, 14], [-11, -8, -6, -3, 5, 7, 9, 13], [-11, -8, 1, 2, 7, 9, 13, 14], [-11, -7, -6, -2, -1, 4, 12, 14], [-11, -6, -4, -3, -1, 2, 12, 13], [-11, -6, -4, -3, 1, 2, 8, 10], [-11, -6, -3, -2, -1, 4, 9, 13], [-11, -2, 1, 4, 6, 7, 8, 14], [-10, -9, -8, -4, 1, 2, 11, 12], [-10, -9, -4, 2, 3, 7, 11, 13], [-10, -9, 4, 5, 7, 11, 13, 14], [-9, -8, -7, -5, -2, 4, 10, 13], [-9, 1, 2, 3, 4, 10, 13, 14], [-8, -7, -2, 1, 5, 6, 9, 11], [-8, -6, -4, 2, 3, 7, 9, 14], [-8, -2, 3, 4, 7, 10, 12, 13], [-6, -5, -4, -2, 3, 7, 12, 13]]