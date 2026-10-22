# Konstrukcja F = Phi2^{-1} o Phi1, Phi1=(l1, mu+f(l1)), Phi2=(nu+g(l2), l2), oba stopnia 2.
P=[(-1,-1),(1,-1),(1,1),(-1,1),(2,2)]; Q=[(1,1),(-1,1),(-1,-1),(2,2),(1,-1)]
R.<a1,a2>=QQ[]
def detI(PP,QQ_,c1,c2):  # wiersze [1,x,y,l1(p)^2, l2(q)] , l1=c1 x+y, l2=c2 x+y
    return matrix([[1,p[0],p[1],(c1*p[0]+p[1])^2, c2*q[0]+q[1]] for p,q in zip(PP,QQ_)]).det()
e1=detI(P,Q,a1,a2); e2=detI(Q,P,a2,a1)
I=R.ideal([e1,e2]); print("e1=",e1.factor()); print("e2=",e2.factor())
print("dim",I.dimension())
for comp in I.minimal_associated_primes(): print("skladowa:",comp.gens())
pol=I.elimination_ideal(a2).gens()[0]; print("eliminacja a1:",pol.factor())

K.<s>=NumberField(polygen(QQ)^2-94)
A1=19+2*s; A2=-A1/15   # a1 z a1^2-38a1-15=0, a2=-a1/15
assert A1^2-38*A1-15==0 and 15*A2^2+38*A2-1==0
S.<X,Y>=K[]
def czynnik(PP,QQ_,c1,c2):
    # znajdz mu=m0+m1x+m2y, f=f2*l1^2 z c2*qx+qy = mu(p)+f2*(c1 px+py)^2
    M=matrix(K,[[1,p[0],p[1],(c1*p[0]+p[1])^2] for p in PP]); b=vector(K,[c2*q[0]+q[1] for q in QQ_])
    sol=M.solve_right(b); assert M*sol==b; print("  jadro wymiar",M.right_kernel().dimension())
    m0,m1,m2,f2=sol; l1=c1*X+Y; mu=m0+m1*X+m2*Y
    print("  niezaleznosc det",matrix(K,[[c1,1],[m1,m2]]).det(), " f2=",f2)
    assert matrix(K,[[c1,1],[m1,m2]]).det()!=0 and f2!=0
    return l1, mu+f2*l1^2
# Phi1(p)=(l1(p), l2 z q)
u1,v1=czynnik(P,Q,A1,A2)        # Phi1=(u1,v1): u1=l1, v1=mu+f(l1)
v2,u2=czynnik(Q,P,A2,A1)        # Phi2=(u2,v2): v2=l2, u2=nu+g(l2)
for p,q in zip(P,Q):
    s1=(u1(*p),v1(*p)); s2=(u2(*q),v2(*q)); assert s1==s2
print("Phi1(p_i)==Phi2(q_i) OK")
# Phi2=(u2,v2): v2=l2=A2*X+Y, u2 = nuL(X,Y) + c*l2^2. Odwrotnosc liniowa po odjeciu c*v^2.
nuL=S(sum(u2.monomial_coefficient(m)*m for m in u2.monomials() if m.degree()<=1))
gp=u2-nuL; c=gp.monomial_coefficient(Y^2); assert gp==c*(A2*X+Y)^2
Mlin=matrix(K,[[nuL.monomial_coefficient(X),nuL.monomial_coefficient(Y)],[A2,1]])
Mi=Mlin.inverse(); n0=nuL.constant_coefficient()
def Phi2inv(a,b):
    r=[a-n0-c*b^2, b]; return (Mi[0,0]*r[0]+Mi[0,1]*r[1], Mi[1,0]*r[0]+Mi[1,1]*r[1])
def Phi1(a,b): return (u1(a,b), v1(a,b))
def Phi2(a,b): return (u2(a,b), v2(a,b))
def Phi1inv(a,b):
    # u1=A1 X+Y=a, v1=mu+f2*a^2=b ; mu liniowe
    muL=v1-(v1.monomial_coefficient(X^2)/A1^2)*(A1*X+Y)^2
    M=matrix(K,[[A1,1],[muL.monomial_coefficient(X),muL.monomial_coefficient(Y)]]); Mi1=M.inverse()
    r=[a, b-muL.constant_coefficient()-(v1.monomial_coefficient(X^2)/A1^2)*a^2]
    return (Mi1[0,0]*r[0]+Mi1[0,1]*r[1], Mi1[1,0]*r[0]+Mi1[1,1]*r[1])
F=Phi2inv(*Phi1(X,Y)); G=Phi1inv(*Phi2(X,Y))
print("deg F:",[f.degree() for f in F]," deg G:",[g.degree() for g in G])
for p,q in zip(P,Q): assert (F[0](*p),F[1](*p))==(K(q[0]),K(q[1]))
print("F(p_i)=q_i dla wszystkich 5 OK")
GF=[g(*F) for g in G]; FG=[f(*G) for f in F]
print("G o F = id:",GF==[X,Y]," F o G = id:",FG==[X,Y])
print("Jakobian F:",matrix([[f.derivative(z) for z in (X,Y)] for f in F]).det())
print("F1 =",F[0]); print("F2 =",F[1])
print("G1 =",G[0]); print("G2 =",G[1])
print("Phi1 =",Phi1(X,Y)); print("Phi2 =",Phi2(X,Y))
