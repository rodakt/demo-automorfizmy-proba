# Kontrola pozytywna: losowe G stopnia 4 (a∘T∘b∘T'∘c) i 2 (a∘T∘b); procedura z audyt.py musi znalezc oczekiwane zera.
import sys, random
sys.path.insert(0,'skrypty')
from audyt import *
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 1)
R=lambda: Rational(random.randint(-5,5),random.randint(1,3))
def afin():
    while True:
        A=Matrix(2,2,lambda i,j:R())
        if A.det()!=0: return A,Matrix([R(),R()])
def ap(Ab,v): A,b=Ab; w=A*Matrix(v)+b; return (expand(w[0]),expand(w[1]))
def tri(v,f): return (v[0], expand(v[1]+f.subs(x,v[0])))
def kw(): return R()*x**2+R()*x+(1 if True else 0)  # wspolczynnik przy x^2 moze byc 0 -> poprawiamy nizej
def kwad():
    while True:
        k=R()
        if k!=0: return k*x**2+R()*x+R()
def nietroj():
    while True:
        A,b=afin()
        if A[0,1]!=0 and A[1,0]!=0: return A,b
def pkt(G,n=5):
    while True:
        P=[(R(),R()) for _ in range(n)]
        Q=[tuple(g.subs({x:p[0],y:p[1]},simultaneous=True) for g in G) for p in P]
        if len(set(P))==n and len(set(Q))==n: return P,Q
out=open('tmp/kontrola_%s.log'%(sys.argv[1] if len(sys.argv)>1 else 1),'w')
def log(s): print(s); out.write(str(s)+'\n'); out.flush()
ok=True
# stopien 4
a,b,c=afin(),nietroj(),afin(); f,g=kwad(),kwad()
v=ap(c,(x,y)); v=tri(v,g); v=ap(b,v); v=tri(v,f); G=ap(a,v)
log(f'G4 = {G}, deg={max(Poly(G[0],x,y).total_degree(),Poly(G[1],x,y).total_degree())}')
Ainv=a[0].inv()
ocz1=(c[0][0,0],c[0][0,1]); ocz2=(Ainv[0,0],Ainv[0,1])
log(f'oczekiwane (a1:b1)={ocz1}, (a2:b2)={ocz2}')
P,Q=pkt(G)
log(f'P={P}\nQ={Q}')
log('L1 jadro (powinno byc tylko stale dla generycznego deg4): '+str([list(w) for w in L1(P,Q)]))
c1,c2=formy(P,Q)
v1=c1.subs({a1:ocz1[0],b1:ocz1[1],a2:ocz2[0],b2:ocz2[1]}); v2=c2.subs({a1:ocz1[0],b1:ocz1[1],a2:ocz2[0],b2:ocz2[1]})
log(f'c1,c2 w oczekiwanym punkcie: {v1}, {v2}'); ok&= (v1==0 and v2==0)
w=zera(c1,c2,log); log('WYMIERNE ZERA: '+str(w))
def rowne(z):
    nazwa,s=z
    if not isinstance(s,dict): return False
    pt={a1:ocz1[0],b1:ocz1[1],a2:ocz2[0],b2:ocz2[1]}
    # porownanie w P1xP1
    m={'b1=b2=1':{b1:1,b2:1},'b1=0,a1=1,b2=1':{b1:0,a1:1,b2:1},'b1=1,b2=0,a2=1':{b1:1,b2:0,a2:1},'b1=b2=0,a1=a2=1':{b1:0,b2:0,a1:1,a2:1}}[nazwa]
    full={**m,**s}
    return simplify(full[a1]*pt[b1]-full[b1]*pt[a1])==0 and simplify(full[a2]*pt[b2]-full[b2]*pt[a2])==0
zn=any(rowne(z) for z in w); log(f'ZNALEZIONO OCZEKIWANE ZERO deg4: {zn}'); ok&=zn
# stopien 2
a,b=afin(),afin(); f=kwad()
v=ap(b,(x,y)); v=tri(v,f); G=ap(a,v)
P,Q=pkt(G); ker=L1(P,Q)
nst=[list(w) for w in ker if any(w[i]!=0 for i in (0,1,3,4))]
log(f'deg2: jadro L1 = {[list(w) for w in ker]}; niestale: {bool(nst)}'); ok&=bool(nst)
log('KONTROLA OK' if ok else 'KONTROLA NIEUDANA')
