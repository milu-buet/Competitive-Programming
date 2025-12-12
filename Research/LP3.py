import pulp as p 
import math
import sys
sys.setrecursionlimit(20000)
  
# Create a LP Minimization problem 
#Lp_prob = p.LpProblem('Problem', p.LpMaximize)  
Lp_prob = p.LpProblem('Problem', p.LpMinimize)


r = 1.61803398875 
#r = 1.51
r = 1.6
r1 = r-1
r2 = r**2-1
mn = 0.0001
#mn  = 0.05572809 
#mn = 0.090169943
#mn = p.LpVariable(name="mn", lowBound=0, upBound=1)

depth = 7
width = 7

X = ['i','j','k','l','m','n','p','q','r','s','t']
ps = [0, 1/r, 1/r**2, 1/r**3, 1/r**4, 1/r**5, 1/r**6, 1/r**7, 1/r**8, 1/r**9, 1/r**10]
X = X[:depth]
all_sum = ''
var_list = []

codes = []
def btrack(i, v):
	global all_sum
	if i == len(X):
		code = v + '= p.LpVariable(name="' + v + '", lowBound=0, upBound=1)'
		codes.append(code)

		all_sum += '+'+v 
		var_list.append(v)

		wd = depth - v.count('x')
		if wd > 0:
			name = 't'+v+str(wd)
			code = name +' = p.LpVariable(name="'+name+'", lowBound=0, upBound=1, cat="Integer")'
			#exec(code)
			codes.append(code)
		return

	for ch in ['0','1','x']:
		nv = v+X[i]+ch
		btrack(i+1, nv)

btrack( 0, '')
for code in codes:
	exec(code)

		
#print(var_list)
#var_list.pop()
#print(all_sum[1:])

code = "Lp_prob += " + all_sum[1:]
#print(code)
exec(code)
#Lp_prob += mn

# var structure

for v in var_list:
	wd = depth - v.count('x')
	name = 't'+v+str(wd)
	
	# for i in range(1,depth+1):
	# 	name = 't'+v+str(i)
	# 	code += name+'*ps['+str(i)+'] +'
	# code = code[:-1]
	
	if wd > 0:
		code = 'Lp_prob += ' + v + " == "
		code += name+'*ps['+str(wd)+']'	

		#print(code)
		exec(code)

	if wd > width:
		code = 'Lp_prob += ' + name + " == 0"
		exec(code)


############################### potential comparison Pr(pi)>=all
# def Pr(s): #s='i1'
# 	os = s[0] + str(int(s[1])^1)
# 	pos = ''
# 	neg = ''
# 	for avar in var_list:
# 		if s in avar:
# 			pos += '+' + avar

# 		if os in avar:
# 			neg += '+' + avar

# 	return pos[1:] + '-r1*(' + neg[1:] + ')'

# #print(Pr('1i'))
# i1 = Pr('i1')
# for s in vtypes[1:]:
# 	code = i1 + '>=' + Pr(s)
# 	code = "Lp_prob += " + code
# 	#print(code)
	#exec(code)
###########################################

########################################### delay games constraint

def get_vars(s1, s2):
	os1 = s1[0] + str(int(s1[1])^1)
	xs1 = s1[0] + 'x'

	os2 = s2[0] + str(int(s2[1])^1)
	xs2 = s2[0] + 'x'

	a,b,c,d,e,f,g,h = '','','','','','','',''
	for s in var_list:
		if s1 in s and s2 in s:
			a += '+' + s 
		elif s1 in s and os2 in s:
			b += '+' + s 
		elif s1 in s and xs2 in s:
			c += '+' + s

		elif os1 in s and s2 in s:
			d += '+' + s 
		elif os1 in s and os2 in s:
			e += '+' + s 
		elif os1 in s and xs2 in s:
			f += '+' + s

		elif xs1 in s and s2 in s:
			g += '+' + s

		elif xs1 in s and os2 in s:
			h += '+' + s
	return a,b,c,d,e,f,g,h


def delay(s1, s2): # pi, pj
	a,b,c,d,e,f,g,h = get_vars(s1,s2)
	code = a[1:] + e + '<=' + 'r2*('+b[1:]+d+')+r1*('+c[1:]+f+g+h+')-mn'
	return code

for i in range(len(X)):
	for ti in [X[i]+'0', X[i]+'1']:
		for j in range(i+1,len(X)):
			for tj in [X[j]+'0', X[j]+'1']:
				code = delay(ti, tj)
				code = "Lp_prob += " + code
				exec(code)
##################################################
#type 2

#9
#edges = [('i1', 'j1'),('j0', 'k0'), ('k1', 'l1'), ('l0', 'm0'), ('m1', 'n1'), ('n0', 'p0'), ('p1', 'q0'), ('q1', 'r0'), ('r1', 'i0') ]

#7
edges = [('i1', 'j1'),('j0', 'k0'), ('k1', 'l1'), ('l0', 'm0'), ('m1', 'n1'), ('n0', 'p0'), ('p1', 'i0') ]

#5
#edges = [('i1', 'j1'),('j0', 'k0'), ('k1', 'l1'), ('l0', 'm0'), ('m1', 'i0') ]

#3
#edges = [('i1', 'j1'), ('j0', 'k0'), ('k1', 'i0') ]



#edges = [('i1', 'j1'), ('i0', 'j1'),('j0', 'k0'), ('k1', 'l1'), ('k1', 'l0'), ('j1', 'm1'), ('k1', 'm0') ]
#edges = [('i1', 'j1'), ('i0', 'j1'),('j0', 'k0'), ('k1', 'l1'), ('l0', 'm1'), ('l0', 'm0') ]

#edges = [('i1', 'j1'), ('j0', 'k0'), ('i0', 'k1') ]
#edges = [('i1', 'j1'), ('i0', 'j1'), ('j0', 'k0')]#, ('i1', 'k1') ]
#edges = [('i1', 'j1'), ('i0', 'j1'), ('i1', 'k1') ]

#constraints
########################################## Total sum <= 1
code = "Lp_prob += " + all_sum[1:] + '<= 2'
exec(code)

code = "Lp_prob += " + all_sum[1:] + '>= .5'
#exec(code)




for x,y in edges:
	a,b,c,d,e,f,g,h = get_vars(x, y)
	code = "Lp_prob += " + a[1:]+b+c+d+g + '<=' + 'r2*('+e[1:]+')' + '+' + 'r1*('+f[1:]+h+')-mn'
	exec(code)


# Display the problem 
print(Lp_prob) 
  
status = Lp_prob.solve()   # Solver 
print(p.LpStatus[status])   # The solution status 

for v in var_list:

	code = 'print(v,p.value('+ v +'))'
	exec(code)

	# wd = depth - v.count('x')
	# if wd > 0:
	# 	name = 't'+v+str(wd)
	# 	code = 'print(' + ',name)'
	# 	exec(code)

print(p.LpStatus[status])
