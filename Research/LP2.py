import pulp as p 
import math

r = 1.61803398875 
#r = 1.51
r1 = r-1
r2 = r**2-1
r3 = r**3-1
r4 = r**4-1
mn = 0.00001
#mn  = 0.05572809 
#mn = 0.090169943
  
# Create a LP Minimization problem 
Lp_prob = p.LpProblem('Problem', p.LpMaximize)  
#Lp_prob = p.LpProblem('Problem', p.LpMinimize)


vtypes = ['i1','i0','j1','j0','k1','k0','l1','l0']
all_sum = ''
var_list = []
for i in ['i1', 'i0', 'ix']:
	for j in ['j1', 'j0', 'jx']:
		for k in ['k1', 'k0', 'kx']:
			for l in ['l1', 'l0', 'lx']:
				v = i+j+k+l
				code = v + '= p.LpVariable(name="' + v + '", lowBound=0, upBound=1)'
				exec(code)
				#print(code)

				all_sum += '+'+v 
				var_list.append(v)
#print(var_list)
#var_list.pop()
#print(all_sum[1:])

#Lp_prob += i1j1k1l1

#################################################
# i1=1, j0=1, k0=1, l0=1 is bad
left =  ''
right = ''
for avar in var_list:
	if 'i1' in avar or 'j0' in avar or 'k0' in avar or 'l0' in avar:
		left += '+' + avar 
left = left[1:]
#print(left)

right = 'r4*i0j1k1l1' 
right += '+ r3*(i0j1k1lx + i0j1kxl1 + i0jxk1l1 + ixj1k1l1)'
right += '+ r2*(i0j1kxlx + i0jxk1lx + i0jxkxl1 + ixj1k1lx + ixj1kxl1 + ixjxk1l1)'
right += '+ r1*(i0jxkxlx + ixj1kxlx + ixjxk1lx + ixjxkxl1)' 

#print(right)

code = "Lp_prob += "  + '+ (' +left + ') - (' + right + ')'
exec(code)
############################################################

##########################################################

#constraints
########################################## Total sum <= 1
code = "Lp_prob += " + all_sum[1:] + '<= 1-mn'
exec(code)


############################### potential comparison Pr(pi)>=all
def Pr(s): #s='i1'
	os = s[0] + str(int(s[1])^1)
	pos = ''
	neg = ''
	for avar in var_list:
		if s in avar:
			pos += '+' + avar

		if os in avar:
			neg += '+' + avar

	return pos[1:] + '-r1*(' + neg[1:] + ')'

#print(Pr('1i'))
i1 = Pr('i1')
for s in vtypes[1:]:
	code = i1 + '>=' + Pr(s)
	code = "Lp_prob += " + code
	#print(code)
	exec(code)
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

#print(delay('i1','j1'))
for i in range(len(vtypes)):
	for j in range(i+1,len(vtypes)):
		s1 = vtypes[i]
		s2 = vtypes[j]
		if s1[0]!=s2[0]:
			code = delay(s1, s2)
			code = "Lp_prob += " + code
			exec(code)
##################################################

##################################################
# li=1, lj=1 is a bad move
a,b,c,d,e,f,g,h = get_vars('i1', 'j1')
code = "Lp_prob += " + a[1:]+b+c+d+g + '<=' + 'r2*('+e[1:]+')' + '+' + 'r1*('+f[1:]+h+')-mn'
exec(code)
#######################################################

#j=1, k=1 is good
a,b,c,d,e,f,g,h = get_vars('k1', 'j1')
code = "Lp_prob += " + a[1:]+b+c+d+g + '>=' + 'r2*('+e[1:]+')' + '+' + 'r1*('+f[1:]+h+')'
exec(code)

#######################################################
#j=0, k=0 is bad
code = "Lp_prob += " + b[1:]+d+e+f+h + '<=' + 'r2*('+a[1:]+')' + '+' + 'r1*('+c[1:]+g+')-mn'
exec(code)
##########################################################

# # i1=1, j0=1, k0=1, l0=1 is bad
# left =  ''
# right = ''
# for avar in var_list:
# 	if 'i1' in avar or 'j0' in avar or 'k0' in avar or 'l0' in avar:
# 		left += '+' + avar 
# left = left[1:]
# #print(left)

# right = 'r4*i0j1k1l1' 
# right += '+ r3*(i0j1k1lx + i0j1kxl1 + i0jxk1l1 + ixj1k1l1)'
# right += '+ r2*(i0j1kxlx + i0jxk1lx + i0jxkxl1 + ixj1k1lx + ixj1kxl1 + ixjxk1l1)'
# right += '+ r1*(i0jxkxlx + ixj1kxlx + ixjxk1lx + ixjxkxl1)' 

# #print(right)

# code = "Lp_prob += " + left + '+' + right 
# exec(code)
# ############################################################




# Display the problem 
print(Lp_prob) 
  
status = Lp_prob.solve()   # Solver 
print(p.LpStatus[status])   # The solution status 