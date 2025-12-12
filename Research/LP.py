# import the library pulp as p 
import pulp as p 
import math
  
# Create a LP Minimization problem 
Lp_prob = p.LpProblem('Problem', p.LpMaximize)  
#Lp_prob = p.LpProblem('Problem', p.LpMinimize)
  
# Create problem Variables  
a1 = p.LpVariable(name="a1", lowBound=0, upBound=1)
b1 = p.LpVariable(name="b1", lowBound=0, upBound=1)
c1 = p.LpVariable(name="c1", lowBound=0, upBound=1)
d1 = p.LpVariable(name="d1", lowBound=0, upBound=1)
e1 = p.LpVariable(name="e1", lowBound=0, upBound=1)
f1 = p.LpVariable(name="f1", lowBound=0, upBound=1)
g1 = p.LpVariable(name="g1", lowBound=0, upBound=1)
h1 = p.LpVariable(name="h1", lowBound=0, upBound=1)


a2 = p.LpVariable(name="a2", lowBound=0, upBound=1)
b2 = p.LpVariable(name="b2", lowBound=0, upBound=1)
c2 = p.LpVariable(name="c2", lowBound=0, upBound=1)
d2 = p.LpVariable(name="d2", lowBound=0, upBound=1)
e2 = p.LpVariable(name="e2", lowBound=0, upBound=1)
f2 = p.LpVariable(name="f2", lowBound=0, upBound=1)
g2 = p.LpVariable(name="g2", lowBound=0, upBound=1)
h2 = p.LpVariable(name="h2", lowBound=0, upBound=1)

a3 = p.LpVariable(name="a3", lowBound=0, upBound=1)
b3 = p.LpVariable(name="b3", lowBound=0, upBound=1)
c3 = p.LpVariable(name="c3", lowBound=0, upBound=1)
d3 = p.LpVariable(name="d3", lowBound=0, upBound=1)
e3 = p.LpVariable(name="e3", lowBound=0, upBound=1)
f3 = p.LpVariable(name="f3", lowBound=0, upBound=1)
g3 = p.LpVariable(name="g3", lowBound=0, upBound=1)
h3 = p.LpVariable(name="h3", lowBound=0, upBound=1)

r5 = math.sqrt(5)
s = 1.618033989
#s = 1.51
#s = 1.55
#s = 1.9
s1 = s-1
s2 = s*s - 1
vv = 0.000001
v = 0.013155617   #9 = 8-cnf
#v = 0.021286236  #8 = 7-cnf
#v = 0.034441853  #7 = 6-cnf
v = 0.05572809   #6 = 5-cnf
#v = 0.090169943
#v = vv
#v = p.LpVariable(name="v", lowBound=vv, upBound=1)
  
# Objective Function 
#Lp_prob +=   s2*(b1+d1) + s1*(c1+f1+g1+h1)-(a1+e1)

#Lp_prob +=    a1+b1+c1+e1+h1 - s2*d1 - s1*(f1+g1)

Lp_prob +=   v# s2*a2 + s1*(c2+g2) - (b2+d2+e2+f2+h2) #== s1**5



#Lp_prob += a+e #s1*(an+en) - (bn+s1*dn) - s1*(a+e) + (b+s1*d)
#Lp_prob +=  s2*e1 + s1*(f1+h1) - (a1+b1+c1+d1+g1)
#Lp_prob += a1+b1+c1-s1*(d1+e1+f1)- (b1+e1+h1-s1*(a1+d1+g1))
#Lp_prob += (b1+c1+h1 - (d1+f1+g1))

#Lp_prob += a1+b1+c1+d1+e1+f1+g1+h1+c2+f2


Lp_prob += a1 >= v 
Lp_prob += f1 >= v 


# Lp_prob += b1 == 0
# Lp_prob += d1 == 0

#Lp_prob += a1 >= r5

#Lp_prob += c1 == 0
#Lp_prob += e1 == 0
#Lp_prob += g1 == 0

#Lp_prob += a3 == 0
#Lp_prob += e3 == 0

# Constraints: 
Lp_prob += a1+b1+c1+d1+e1+f1+g1+h1+c2+f2 <= 1-v
Lp_prob += a1+b1+c1+d1+e1+f1+g1+h1+g3+h3 <= 1-v
#Lp_prob += a+b+c+d+e+f+g+h+cn+fn+gm+hm >= 0

Lp_prob += a1+b1+c1 >= d1+e1+f1 
Lp_prob += a1+b1+c1 - s1*(d1+e1+f1) >= b1+e1+h1 - s1*(a1+d1+g1) 
Lp_prob += a1+b1+c1 - s1*(d1+e1+f1) >= a1+d1+g1 - s1*(b1+e1+h1) 

# i=1, j=1
Lp_prob += a1+b1+c1+d1+g1 <= s2*e1 + s1*(f1+h1) - v
Lp_prob += a1+e1 <= s2*(b1+d1) + s1*(c1+f1+g1+h1) - v
Lp_prob += b1+d1 <= s2*(a1+e1) + s1*(c1+f1+g1+h1) - v
Lp_prob += a1+d1 <= s2*(b1+e1) + s1*(c1+f1+g1+h1) - v
Lp_prob += b1+e1 <= s2*(a1+d1) + s1*(c1+f1+g1+h1) - v
#Lp_prob += (a+d+e+g+f <= s2*b + s1*(c+h)- v) or (a+b+c+e+h <= s2*d + s1*(g+f)- v) or (b+d+e+f+h <= s2*a + s1*(c+g)- v)

# #############################################################################
# Lp_prob += a2+b2+c2+d2+e2+f2+g2+h2+c1+f1 <= 1-v
# Lp_prob += a2+b2+c2+d2+e2+f2+g2+h2+c3+f3 <= 1-v
# #Lp_prob += an+bn+cn+dn+en+fn+gn+hn+c+f+cm+fm >= 0

# Lp_prob += b1+e1+h1 == b2 + e2 + h2 
# Lp_prob += a1+d1+g1 == a2 + d2 + g2

# Lp_prob += a1+b1+c1 - s1*(d1+e1+f1) >= a2+b2+c2 - s1*(d2+e2+f2) 
# Lp_prob += a1+b1+c1 - s1*(d1+e1+f1) >= d2+e2+f2 - s1*(a2+b2+c2) 


# Lp_prob += a2+e2 <= s2*(b2+d2) + s1*(c2+f2+g2+h2) - v
# Lp_prob += b2+d2 <= s2*(a2+e2) + s1*(c2+f2+g2+h2) - v
# Lp_prob += a2+d2 <= s2*(b2+e2) + s1*(c2+f2+g2+h2) - v
# Lp_prob += b2+e2 <= s2*(a2+d2) + s1*(c2+f2+g2+h2) - v

# # j=1, k=1,  but i=1 is problem
# Lp_prob += a2+b2+c2+d2+g2 >= s2*e2 + s1*(f2+h2)

# # j=0, k=0
# Lp_prob += b2+d2+e2+f2+h2 <= s2*a2 + s1*(c2+g2) - v

# #Lp_prob += a+b+c - s1*(d+e+f) + s1*(a+e) - (b+s1*d) <=  an+bn+cn - s1*(dn+en+fn) + s1*(an+en) - (bn+s1*dn) - v 

# #########################################################################
# Lp_prob += a3+b3+c3+d3+e3+f3+g3+h3+g1+h1 <= 1-v
# Lp_prob += a3+b3+c3+d3+e3+f3+g3+h3+g2+h2 <= 1-v
# #Lp_prob += am+bm+cm+dm+em+fm+gm+hm + gn + hn + g + h >= 0
# Lp_prob += a1+b1+c1 == a3+b3+c3
# Lp_prob += d1+e1+f1 == d3+e3+f3
# Lp_prob += a2 + b2 + c2 == a3 + d3 + g3
# Lp_prob += d2 + e2 + f2 == b3 + e3 + h3

# Lp_prob += a3+e3 <= s2*(b3+d3) + s1*(c3+f3+g3+h3) - v
# Lp_prob += b3+d3 <= s2*(a3+e3) + s1*(c3+f3+g3+h3) - v
# Lp_prob += a3+d3 <= s2*(b3+e3) + s1*(c3+f3+g3+h3) - v
# Lp_prob += b3+e3 <= s2*(a3+d3) + s1*(c3+f3+g3+h3) - v

# ###########################
#what if i=0 is the strategy? No
# Lp_prob += a3+b3+c3+d3+g3 >= s2*e3 + s1*(f3+h3)
# Lp_prob += b3+d3+e3+f3+h3 <= s2*a3 + s1*(c3+g3) - v


# # # what if k==1 is the strategy

# # #k=1, j=0
#Lp_prob += a2+b2+c2+e2+h2 <= s2*d2 + s1*(f2+g2) - v

# # #k=1, j=1
#Lp_prob += a2+b2+c2+d2+g2 <= s2*e2 + s1*(f2+h2) - v

# # #k=1, i=0
#Lp_prob += a3+d3+g3+e3+f3 <= s2*b3 + s1*(c3+h3) - v   



# # what if k==0 is the strategy
# # k=0, j=0
# Lp_prob += bn+dn+en+fn+hn <= s2*an + s1*(cn+gn) - v

# #Lp_prob += cm >= .1



  
# Display the problem 
print(Lp_prob) 
  
status = Lp_prob.solve()   # Solver 
print(p.LpStatus[status])   # The solution status 
  
# Printing the final solution 
#print(p.value(a), p.value(e), p.value(Lp_prob.objective))
a1,b1,c1,d1,e1,f1,g1,h1 = p.value(a1), p.value(b1), p.value(c1), p.value(d1), p.value(e1), p.value(f1), p.value(g1), p.value(h1)
print("a1=",a1)
print("b1=",b1)
print("c1=",c1)
print("d1=",d1)
print("e1=",e1)
print("f1=",f1)
print("g1=",g1)
print("h1=",h1)

print()

a2,b2,c2,d2,e2,f2,g2,h2 = p.value(a2), p.value(b2), p.value(c2), p.value(d2), p.value(e2), p.value(f2), p.value(g2), p.value(h2)
print("a2=",a2)
print("b2=",b2)
print("c2=",c2)
print("d2=",d2)
print("e2=",e2)
print("f2=",f2)
print("g2=",g2)
print("h2=",h2)

print()

a3,b3,c3,d3,e3,f3,g3,h3 = p.value(a3), p.value(b3), p.value(c3), p.value(d3), p.value(e3), p.value(f3), p.value(g3), p.value(h3)
print("a3=",a3)
print("b3=",b3)
print("c3=",c3)
print("d3=",d3)
print("e3=",e3)
print("f3=",f3)
print("g3=",g3)
print("h3=",h3)

print()

# a= .38
# b= 0
# c= 1.14
# d=0
# e= .76
# f= .76
# g=0
# h=0

# a= 0.09017029540389399
# b= 0
# c= 0.29179710331469666
# d= 0
# e= 0.18034051465958892
# f= 0.09017029540389399
# g= 0
# h= 0.09017029540389399


print(a1+b1+c1+d1+e1+f1+g1+h1, 0<=a1+b1+c1+d1+e1+f1+g1+h1<1)

print(a1+b1+c1,             d1+e1+f1,                   a1+b1+c1 >= d1+e1+f1)
print(a1+b1+c1-s1*(d1+e1+f1),  b1+e1+h1-s1*(a1+d1+g1),        a1+b1+c1-s1*(d1+e1+f1) >= b1+e1+h1-s1*(a1+d1+g1) )
print(a1+b1+c1-s1*(d1+e1+f1),  a1+d1+g1-s1*(b1+e1+h1),        a1+b1+c1-s1*(d1+e1+f1) >= a1+d1+g1-s1*(b1+e1+h1))

print(a1+b1+c1+d1+g1,         s2*e1+s1*(f1+h1),           a1+b1+c1+d1+g1 < s2*e1 + s1*(f1+h1))
print(a1+e1,               s2*(b1+d1)+s1*(c1+f1+g1+h1),   a1+e1 < s2*(b1+d1) + s1*(c1+f1+g1+h1))


