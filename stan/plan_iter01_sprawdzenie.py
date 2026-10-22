from sympy import *
P=[(-1,-1),(1,-1),(1,1),(-1,1),(2,2)];Q=[(1,1),(-1,1),(-1,-1),(2,2),(1,-1)]
a1,b1,a2,b2=symbols('a1 b1 a2 b2')
L1=[a1*x+b1*y for x,y in P]; L2=[a2*x+b2*y for x,y in Q]
c1=Matrix([[1,P[i][0],P[i][1],L1[i]**2,L2[i]] for i in range(5)]).det()
c2=Matrix([[1,Q[i][0],Q[i][1],L2[i]**2,L1[i]] for i in range(5)]).det()
print(factor(c1));print(factor(c2))
for s in [{b1:1,b2:1},{b1:0,a1:1,b2:1},{b2:0,a2:1,b1:1},{b1:0,a1:1,b2:0,a2:1}]:
  e1,e2=c1.subs(s),c2.subs(s); v=list(e1.free_symbols|e2.free_symbols)
  print(s, solve([e1,e2],v,dict=True) if v else (e1,e2))
