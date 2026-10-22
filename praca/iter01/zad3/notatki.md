# iter01/zad3 — walidacja redukcji: automorfizm stopnia 4 nad Q(√94)

Skrypt: `skrypty/konstrukcja.sage` (uruchom: `sage skrypty/konstrukcja.sage`, ok. kilku sekund).
Pełne wyjście (wzory F, G, Phi1, Phi2): `skrypty/konstrukcja_wyjscie.txt`.
Nie tworzono plików `rozwiazanie*.json` (współczynniki niewymierne — weryfikator ich nie przyjmie, zgodnie z zadaniem).

## Konstrukcja (UDOWODNIONE — proste rozumowanie)
Niech l1 = a1 x + y (na płaszczyźnie p), l2 = a2 x + y (na płaszczyźnie q).
- (I) l2(q_i) = mu(p_i) + f2·l1(p_i)², mu afiniczne: układ liniowy 5×4 w (m0,m1,m2,f2).
- (II) l1(p_i) = nu(q_i) + g2·l2(q_i)², analogicznie.
Wtedy Phi1 = (l1, mu + f2 l1²) i Phi2 = (nu + g2 l2², l2) są automorfizmami stopnia 2
(jeśli mu niezależne od l1, nu od l2), Phi1(p_i) = Phi2(q_i) = (l1(p_i), l2(q_i)),
więc F = Phi2⁻¹ ∘ Phi1 spełnia F(p_i)=q_i, deg F ≤ 4. Redukcja jest więc wystarczająca.

## Obliczenia (OBLICZENIOWE, Sage, dokładnie)
1. Warunki wyznacznikowe (mapa b1=b2=1) — zgodne co do joty z planistą:
   e1 = -4(3a1²a2+9a1²+30a1a2+26a1+3a2+9), e2 = 4(9a1a2²+26a1a2+3a2²+9a1+30a2+3).
   Ideał zerowymiarowy, składowe pierwsze:
   ⟨15a2²+38a2−1, a1+15a2⟩ (para nad Q(√94); a1² − 38a1 − 15 = 0, a1 = 19 ± 2√94)
   i ⟨3a2³+39a2²+29a2+9, 9a1+3a2²+39a2+29⟩ (trójka, 9a1³+29a1²+39a1+3 nieprzywiedlny).
   Brak punktów wymiernych w tej mapie. Map b1=0 / b2=0 tu NIE sprawdzałem (planista twierdzi: brak zer).
2. Dla a1 = 19+2√94, a2 = −a1/15: oba układy liniowe (I),(II) rozwiązywalne jednoznacznie
   (jądro wymiaru 0), f2 = 29/60 − √94/20 ≠ 0, g2 = 13/4 + √94/4 ≠ 0, niedegeneracje spełnione
   (wyznaczniki (−268−29√94)/15 i (644+67√94)/15).
3. F = Phi2⁻¹∘Phi1, G = Phi1⁻¹∘Phi2 policzone jawnie w K = Q(√94):
   deg F1 = deg F2 = 4, deg G1 = deg G2 = 4; F(p_i) = q_i dla wszystkich 5 punktów;
   G∘F = id i F∘G = id (równość wielomianów); jakobian F = (335 − 24√94)/241 (stała ≠ 0).

## Wniosek
Konstrukcja działa — brak sygnału błędu w redukcji. Przeszkoda dla stopnia 4 nad Q (w klasie
złożeń dwóch trójkątnych stopnia 2) jest arytmetyczna: rozwiązania istnieją, ale nad Q(√94).
UWAGA: to nie dowodzi ograniczenia dolnego nad Q — pełność analizy (mapy b1=0, b2=0, przypadek
jednego czynnika stopnia 4, stopień 4 = 2·2 tylko w tej postaci wg Junga–van der Kulka) wymaga
osobnego sprawdzenia; tu tylko mapa b1=b2=1.

## Czego nie zrobiono / dalej
- Punkt 4 (trójka sześcienna) — patrz niżej, jeśli zdążono.
- Punkt 4 ZROBIONY (dokładnie, nie numerycznie): `skrypty/konstrukcja_szescienna.sage`, wyjście
  `skrypty/konstrukcja_szescienna_wyjscie.txt`. Ciało K = Q(a2), 3a2³+39a2²+29a2+9 = 0,
  a1 = −(3a2²+39a2+29)/9. Układy (I),(II) jednoznaczne, niedegeneracje spełnione, F stopnia 4,
  G stopnia 4, F(p_i)=q_i, G∘F=F∘G=id, jakobian = 1. (OBLICZENIOWE)
  Zatem wszystkie 5 zespolonych punktów mapy b1=b2=1 dają automorfizmy stopnia 4 — żaden wymierny.
