# Konstrukcja F = H^{-1} o P, P(p)=(l1, mu+f(l1)) deg f<=3, H(q)=(nu+g(l2), l2) deg g<=2
import json, sympy as sp
from sympy import Rational as R
Z=json.load(open('../../../zadanie.json'))
P=[tuple(map(R,p)) for p in Z['punkty_p']]; Q=[tuple(map(R,q)) for q in Z['punkty_q']]
l1=lambda p:p[0]-3*p[1]; l2=lambda q:q[1]
# (I): l2(q_i) = m0+m1 x+m2 y + f2 l1^2 + f3 l1^3   (mu ma skladowa liniowa; wolny wyraz/term l1 wchlania mu)
m0,m1,m2,f2,f3=sp.symbols('m0 m1 m2 f2 f3')
eqI=[m0+m1*p[0]+m2*p[1]+f2*l1(p)**2+f3*l1(p)**3-l2(q) for p,q in zip(P,Q)]
sI=sp.solve(eqI,[m0,m1,m2,f2,f3],dict=True); print('I',sI)
n0,n1,n2,g2=sp.symbols('n0 n1 n2 g2')
eqII=[n0+n1*q[0]+n2*q[1]+g2*l2(q)**2-l1(p) for p,q in zip(P,Q)]
sII=sp.solve(eqII,[n0,n1,n2,g2],dict=True); print('II',sII)
