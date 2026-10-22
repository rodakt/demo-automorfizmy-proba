# Niezalezny audyt (iter02/zad1): L1 i warunki (I),(II) dla stopnia 4 = 2*2
P=[(-1,-1),(1,-1),(1,1),(-1,1),(2,2)]; Qp=[(1,1),(-1,1),(-1,-1),(2,2),(1,-1)]
M=matrix(QQ,[[p[0],p[1],1,-q[0],-q[1],-1] for p,q in zip(P,Qp)])
print("L1 rank:",M.rank(),"jadro:",M.right_kernel().basis())
R.<a1,b1,a2,b2>=QQ[]
L1=[a1*p[0]+b1*p[1] for p in P]; L2=[a2*q[0]+b2*q[1] for q in Qp]
D1=matrix(R,[[1,P[i][0],P[i][1],L1[i]^2,L2[i]] for i in range(5)]).det()
D2=matrix(R,[[1,Qp[i][0],Qp[i][1],L2[i]^2,L1[i]] for i in range(5)]).det()
print("D1=",factor(D1)); print("D2=",factor(D2))
# wspolne zera w P1xP1: rugownik wzgledem (a2:b2) -- D1 liniowe w (a2,b2): D1=u*a2+v*b2
u=D1.coefficient({a2:1,b2:0}); v=D1.coefficient({a2:0,b2:1})
print("u=",factor(u)," v=",factor(v), " gcd(u,v)=",gcd(u,v))
# podstawienie (a2,b2)=(v,-u) do D2 (dla u,v nie obu zero)
r=D2.subs({a2:v,b2:-u}); print("forma w (a1:b1):",factor(r))
S.<T>=QQ[]
print("pierwiastki wymierne (a1:b1=T:1):",S(r.subs({a1:T,b1:1})).roots(QQ),"; b1=0:",r.subs({a1:1,b1:0}))
# przypadek u=v=0 (D1 tozsamosciowo 0 w (a2,b2)) dla wymiernego (a1:b1)
print("u=v=0 rozw. wymierne:", S(gcd(u.subs({a1:T,b1:1}),v.subs({a1:T,b1:1}))), u.subs({a1:1,b1:0}),v.subs({a1:1,b1:0}))
# rzad kolumn 1,x,y (P) i 1,x,y (Q)
print("rank [1,x,y] P,Q:",matrix(QQ,[[1,p[0],p[1]] for p in P]).rank(),matrix(QQ,[[1,q[0],q[1]] for q in Qp]).rank())
