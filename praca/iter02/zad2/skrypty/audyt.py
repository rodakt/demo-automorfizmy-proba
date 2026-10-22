# Audyt sympy: warunki konieczne dla stopni 2,3,5 (L1) i 4=2*2 (c1,c2). Uruchom: $PYTHON skrypty/audyt.py [kontrola]
import sys, json, random
from sympy import *
x,y,a1,b1,a2,b2,t=symbols('x y a1 b1 a2 b2 t')
def wczytaj():
    d=json.load(open(sys.argv[2] if len(sys.argv)>2 else '../../../zadanie.json'))
    P=[(Rational(u),Rational(v)) for u,v in d['punkty_p']]; Q=[(Rational(u),Rational(v)) for u,v in d['punkty_q']]
    return P,Q
def L1(P,Q):
    # l1=u1 x+v1 y+w1, l2=u2 x+v2 y+w2, l1(p_i)=l2(q_i)
    M=Matrix([[p[0],p[1],1,-q[0],-q[1],-1] for p,q in zip(P,Q)])
    return M.nullspace()
def formy(P,Q):
    l1=lambda p:a1*p[0]+b1*p[1]; l2=lambda q:a2*q[0]+b2*q[1]
    c1=expand(Matrix([[1,p[0],p[1],l1(p)**2,l2(q)] for p,q in zip(P,Q)]).det())
    c2=expand(Matrix([[1,q[0],q[1],l2(q)**2,l1(p)] for p,q in zip(P,Q)]).det())
    return c1,c2
def zera(c1,c2,log):
    wyn={}
    # mapy: (a1:b1),(a2:b2); s=a1/b1 lub b1=0 (a1=1), analog. dla 2
    mapy={'b1=b2=1':{b1:1,b2:1},'b1=0,a1=1,b2=1':{b1:0,a1:1,b2:1},'b1=1,b2=0,a2=1':{b1:1,b2:0,a2:1},'b1=b2=0,a1=a2=1':{b1:0,b2:0,a1:1,a2:1}}
    wymierne=[]
    for nazwa,s in mapy.items():
        f1=expand(c1.subs(s)); f2=expand(c2.subs(s))
        log(f'--- mapa {nazwa}: c1={factor(f1)} ; c2={factor(f2)}')
        zm=[v for v in (a1,a2) if v not in s]
        if not zm:
            log(f'  punkt: c1={f1}, c2={f2}'); 
            if f1==0 and f2==0: wymierne.append((nazwa,{}))
            continue
        if len(zm)==1:
            g=gcd(Poly(f1,zm[0]),Poly(f2,zm[0])) if (f1!=0 and f2!=0) else Poly(f1+f2,zm[0])
            log(f'  gcd={g.as_expr()} -> {factor(g.as_expr())}')
            if f1==0 and f2==0: log('  CALA PROSTA ZER!'); wymierne.append((nazwa,'prosta'))
            for r in roots(g,filter='Q') if g.degree()>0 else []:
                wymierne.append((nazwa,{zm[0]:r}))
            continue
        g=gcd(f1,f2); log(f'  gcd(c1,c2)={factor(g)}')
        if g.as_poly(a1,a2).total_degree()>0: log('  SKLADOWA WYMIARU 1!'); wymierne.append((nazwa,'krzywa '+str(factor(g))))
        R=factor(resultant(f1,f2,a1)); log(f'  Res_a1 (w a2) = {R}')
        for r in (roots(Poly(resultant(f1,f2,a1),a2),filter='Q') if R!=0 else []):
            h=gcd(Poly(f1.subs(a2,r),a1),Poly(f2.subs(a2,r),a1))
            for s1 in roots(h,filter='Q'):
                wymierne.append((nazwa,{a1:s1,a2:r}))
            log(f'  a2={r}: gcd w a1 = {h.as_expr()}')
        R2=factor(resultant(f1,f2,a2)); log(f'  Res_a2 (w a1) = {R2}')
    return wymierne
if __name__=='__main__':
    out=open(sys.argv[1] if len(sys.argv)>1 else 'tmp/audyt.log','w')
    def log(s): print(s); out.write(s+'\n'); out.flush()
    P,Q=wczytaj()
    log('L1 jadro: '+str([list(v) for v in L1(P,Q)]))
    c1,c2=formy(P,Q); log(f'c1={factor(c1)}'); log(f'c2={factor(c2)}')
    w=zera(c1,c2,log); log('WYMIERNE ZERA: '+str(w))
