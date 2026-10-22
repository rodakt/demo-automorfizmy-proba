# Dowod ograniczenia dolnego: brak automorfizmow Q^2 stopnia 1..5 realizujacych bijekcje z zadanie.json
import json
Z=json.load(open('../../../../zadanie.json'))
P=[(QQ(a),QQ(b)) for a,b in Z['punkty_p']]; Qp=[(QQ(a),QQ(b)) for a,b in Z['punkty_q']]
print("P=",P); print("Q=",Qp)
# (1) wspolliniowosc
def kol(u,v,w): return matrix(QQ,[[1,u[0],u[1]],[1,v[0],v[1]],[1,w[0],w[1]]]).det()
from itertools import combinations
for i,j,k in combinations(range(5),3):
    if kol(P[i],P[j],P[k])==0 or kol(Qp[i],Qp[j],Qp[k])==0:
        print("trojka",(i,j,k),"det P:",kol(P[i],P[j],P[k]),"det Q:",kol(Qp[i],Qp[j],Qp[k]))
# (2) Lemat L1: l1(p_i)=l2(q_i), l1=a1x+b1y+c1, l2=a2x+b2y+c2
M=matrix(QQ,[[p[0],p[1],1,-q[0],-q[1],-1] for p,q in zip(P,Qp)])
print("L1: jadro ukladu (a1,b1,c1,a2,b2,c2):",M.right_kernel().basis())
# (3) stopien 4
R.<a1,b1,a2,b2>=PolynomialRing(QQ,order='lex')
l1=lambda u: a1*u[0]+b1*u[1]; l2=lambda u: a2*u[0]+b2*u[1]
D1=matrix(R,[[1,p[0],p[1],l1(p)^2,l2(q)] for p,q in zip(P,Qp)]).det()
D2=matrix(R,[[1,q[0],q[1],l2(q)^2,l1(p)] for p,q in zip(P,Qp)]).det()
print("c1 =",factor(D1)); print("c2 =",factor(D2))
S.<t,s>=PolynomialRing(QQ)
mapy={'(t:1)x(s:1)':{a1:t,b1:1,a2:s,b2:1},'(t:1)x(1:0)':{a1:t,b1:1,a2:1,b2:0},
      '(1:0)x(s:1)':{a1:1,b1:0,a2:s,b2:1},'(1:0)x(1:0)':{a1:1,b1:0,a2:1,b2:0}}
for nm,sub in mapy.items():
    f1=S(D1.subs(sub)); f2=S(D2.subs(sub))
    I=S.ideal([f1,f2])
    print("== mapa",nm,": c1=",factor(f1) if f1!=0 else 0,"; c2=",factor(f2) if f2!=0 else 0)
    print("   dim =",I.dimension())
    if I.dimension()<=0:
        for Pr in I.minimal_associated_primes():
            print("   skladowa:",Pr.gens(), " stopien:",Pr.vector_space_dimension() if Pr.dimension()==0 else 'dim>0')
        print("   punkty wymierne:",I.variety(QQ) if I.dimension()==0 else ('brak' if I.dimension()<0 else '?'))
        if I.dimension()==0:
            G=I.elimination_ideal([s]).gens()[0]; print("   rugownik w t:",factor(G))
            H=I.elimination_ideal([t]).gens()[0]; print("   rugownik w s:",factor(H))
