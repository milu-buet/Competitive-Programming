# import the library pulp as p 
import pulp as p 
import math
  
# Create a LP Minimization problem 
Lp_prob = p.LpProblem('Problem', p.LpMaximize)  
#Lp_prob = p.LpProblem('Problem', p.LpMinimize)
  
# Create problem Variables  
a = p.LpVariable(name="a", lowBound=0, upBound=1)
b = p.LpVariable(name="b", lowBound=0, upBound=1)
c = p.LpVariable(name="c", lowBound=0, upBound=1)
d = p.LpVariable(name="d", lowBound=0, upBound=1)
e = p.LpVariable(name="e", lowBound=0, upBound=1)
f = p.LpVariable(name="f", lowBound=0, upBound=1)
g = p.LpVariable(name="g", lowBound=0, upBound=1)
h = p.LpVariable(name="h", lowBound=0, upBound=1)


r5 = math.sqrt(5)
s = 1.618033989
#s = 1.51
#s = 1.55
#s = 1.9
s1 = s-1
s2 = s*s - 1
vv = 0.00001
v = 0.013155617   #9 = 8-cnf
#v = 0.021286236  #8 = 7-cnf
#v = 0.034441853  #7 = 6-cnf
#v = 0.05572809   #6 = 5-cnf
#v = 0.07294901702
#v = 0.090169943
v = vv
#v = p.LpVariable(name="v", lowBound=vv, upBound=1)
#m = p.LpVariable(name="m", lowBound=0.1, upBound=1)

Lp_prob +=    (a+d+g-(b+e+h)) #v#m#s2*e + s1*(f+h) - (a+b+c+d+g) #== s1**5
# Lp_prob += a == m#.236067
# Lp_prob += f == m#.236067
# Lp_prob += h == m#.236067
#Lp_prob += e == .1**m 

# Constraints: 
Lp_prob += a+b+c+d+e+f+g+h <= 1-v
Lp_prob += a+b+c >= d+e+f 
Lp_prob += a+b+c - s1*(d+e+f) >= b+e+h - s1*(a+d+g) 
#Lp_prob += a+b+c - s1*(d+e+f) >= a+d+g - s1*(b+e+h) + v


# i=1, j=1
Lp_prob += a+b+c+d+g <= s2*e + s1*(f+h) - v
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


