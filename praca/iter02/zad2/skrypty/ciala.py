# Ktore pierwiastki rugownika sa rzeczywiscie wspolnymi zerami (mapa b1=b2=1)? Arytmetyka w Q(alfa).
from sympy import *
a1,a2=symbols('a1 a2')
c1=3*a1**2*a2 + 9*a1**2 + 30*a1*a2 + 26*a1 + 3*a2 + 9
c2=9*a1*a2**2 + 26*a1*a2 + 9*a1 + 3*a2**2 + 30*a2 + 3
for m in [15*a2**2 + 38*a2 - 1, 3*a2**3 + 39*a2**2 + 29*a2 + 9]:
    print('czynnik',m,'nieprzywiedlny nad Q:',Poly(m,a2).is_irreducible,'wymierne pierwiastki:',roots(m,filter='Q'), 'dyskryminanta:',factorint(discriminant(m,a2)))
    # gcd c1,c2 w a1 nad Q[a2]/(m)
    r1=rem(Poly(resultant(c1,c2,a1),a2),Poly(m,a2))
    # wspolny pierwiastek: podrezultant stopnia 1 w a1 modulo m
    from sympy import subresultants
    S=subresultants(Poly(c1,a1),Poly(c2,a1))
    for s in S:
        sr=Poly(s.as_expr(),a1)
        if sr.degree()==1:
            A,B=sr.all_coeffs()
            A=rem(Poly(A,a2),Poly(m,a2)).as_expr(); B=rem(Poly(B,a2),Poly(m,a2)).as_expr()
            print('  podrezultant stopnia 1 mod m: a1 =', -B, '/', A, ' (A mod m =0?)', A==0)
