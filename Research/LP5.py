# import the library pulp as p 
import pulp as p 
import math
  
# Create a LP Minimization problem 
Lp_prob = p.LpProblem('Problem', p.LpMaximize)  
Lp_prob = p.LpProblem('Problem', p.LpMinimize)
  
# Create problem Variables  
a = p.LpVariable(name="a", lowBound=0, upBound=1)
b = p.LpVariable(name="b", lowBound=0, upBound=1)
c = p.LpVariable(name="c", lowBound=0, upBound=1)
d = p.LpVariable(name="d", lowBound=0, upBound=1)
e = p.LpVariable(name="e", lowBound=0, upBound=1)
f = p.LpVariable(name="f", lowBound=0, upBound=1)
g = p.LpVariable(name="g", lowBound=0, upBound=1)
h = p.LpVariable(name="h", lowBound=0, upBound=1)

pli = p.LpVariable(name="pli", lowBound=-1, upBound=1)
pnli = p.LpVariable(name="pnli", lowBound=-1, upBound=1)
plj = p.LpVariable(name="plj", lowBound=-1, upBound=1)
pnlj = p.LpVariable(name="pnlj", lowBound=-1, upBound=1)


depth = 2
for var in ['a','b','c','d','e','f','g','h']:
	for i in range(1,depth+1):
		name = 't'+var+str(i)
		code = name +' = p.LpVariable(name="'+name+'", lowBound=0, cat="Integer")'
		exec(code)

s = 1.618033989
#s = 1.51
#s = 1.55
#s = 1.9
s1 = s-1
s2 = s*s - 1

ps = [0, 1/s, 1/s**2, 1/s**3, 1/s**4, 1/s**5]
vv = 0.0001
v = vv


Lp_prob +=  a+b+c+d+e+f+g+h 


for var in ['a','b','c','d','e','f','g','h']:
	code = 'Lp_prob += ' + var + " == "
	for i in range(1,depth+1):
		name = 't'+var+str(i)
		code += name+'*ps['+str(i)+'] +'
	code = code[:-1]
	#print(code)
	exec(code)



# Constraints: 
Lp_prob += a+b+c+d+e+f+g+h <= 1-v
Lp_prob += pli == a+b+c - s1*(d+e+f)
Lp_prob += pnli == d+e+f - s1*(a+b+c)
Lp_prob += plj == a+d+g - s1*(b+e+h) 
Lp_prob += pnlj == b+e+h - s1*(a+d+g) 

#Lp_prob += pnlj >= plj + v
#Lp_prob += pnlj >= pnli + v
#Lp_prob += pnlj >= pli + v

#Lp_prob += pli + pnli >=  v


# Lp_prob += pli <= pnli - v
# Lp_prob += pli <= plj - v


# i=1, j=1
Lp_prob += a+b+c+d+g <= s2*e + s1*(f+h) - v



# i=0, j=1
Lp_prob += a+d+e+f+g >= s2*b + s1*(c+h)

# i=1, j=0
Lp_prob += a+b+c+e+h >= s2*d + s1*(f+g) 



# i=0, j=0
Lp_prob += b+d+e+f+h >= s2*a + s1*(c+g) 



Lp_prob += a+e <= s2*(b+d) + s1*(c+f+g+h) - v
Lp_prob += b+d <= s2*(a+e) + s1*(c+f+g+h) - v

  
# Display the problem 
print(Lp_prob) 
  
status = Lp_prob.solve()   # Solver 
print(p.LpStatus[status])   # The solution status 
  
# Printing the final solution 
a,b,c,d,e,f,g,h = p.value(a), p.value(b), p.value(c), p.value(d), p.value(e), p.value(f), p.value(g), p.value(h)
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
print("e=",e)
print("f=",f)
print("g=",g)
print("h=",h)

print()
print(a+b+c+d+e+f+g+h, 0<=a+b+c+d+e+f+g+h<1)

print(a+b+c,             d+e+f,                   a+b+c >= d+e+f)
print(a+b+c-s1*(d+e+f),  b+e+h-s1*(a+d+g),        a+b+c-s1*(d+e+f) >= b+e+h-s1*(a+d+g) )
print(a+b+c-s1*(d+e+f),  a+d+g-s1*(b+e+h),        a+b+c-s1*(d+e+f) >= a+d+g-s1*(b+e+h))

print(a+b+c+d+g,         s2*e+s1*(f+h),           a+b+c+d+g < s2*e + s1*(f+h))
print(a+e,               s2*(b+d)+s1*(c+f+g+h),   a+e < s2*(b+d) + s1*(c+f+g+h))


