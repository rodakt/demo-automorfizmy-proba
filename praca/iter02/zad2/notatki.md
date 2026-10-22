# iter02/zad2 — niezależny audyt (sympy) dolnego ograniczenia + kontrola pozytywna

Narzędzie: wyłącznie `$PYTHON` + sympy, rachunki dokładne nad Q. Skrypty napisane przed lekturą
iter01 (porównanie na końcu). Logi w `tmp/`.

## (1) L1 — `skrypty/audyt.py` (log: `tmp/audyt.log`)
Układ l1(p_i) = l2(q_i), l_j = u_j x + v_j y + w_j, macierz 5×6 nad Q. Jądro = span{(0,0,1,0,0,1)},
tj. tylko l1 = l2 = stała. **OBLICZENIOWE.** Wraz z JvdK (iter01) wyklucza stopnie 2, 3, 5 i postać
a∘T∘b z deg T = 4.

## (2) Stopień 4 = 2·2 — formy c1, c2 (`skrypty/audyt.py`)
c1 = det[1, x(p_i), y(p_i), l1(p_i)², l2(q_i)], c2 = det[1, x(q_i), y(q_i), l2(q_i)², l1(p_i)],
l1 = a1x+b1y, l2 = a2x+b2y:
- c1 = −4(3a1²a2 + 9a1²b2 + 30a1b1a2 + 26a1b1b2 + 3a2b1² + 9b1²b2)  (bistopień (2,1))
- c2 =  4(9a1a2² + 26a1a2b2 + 9a1b2² + 3a2²b1 + 30a2b1b2 + 3b1b2²)  (bistopień (1,2))

Wspólne zera w P¹×P¹ (cztery mapy):
- b1=b2=1: gcd(c1,c2)=stała (brak składowej wymiaru 1). Res_{a1} = 768·(15a2²+38a2−1)·(3a2³+39a2²+29a2+9),
  Res_{a2} = 768·(a1²−38a1−15)·(9a1³+29a1²+39a1+3). Oba czynniki nieprzywiedlne nad Q (sympy
  `is_irreducible`), brak pierwiastków wymiernych. `skrypty/ciala.py`: podrezultant stopnia 1 w a1
  ma współczynnik wiodący odwracalny modulo każdy czynnik ⇒ nad każdym pierwiastkiem a2 dokładnie jeden
  wspólny a1: a1 = −15·a2 dla czynnika kwadratowego (sprawdzone ręcznie z wyniku), a1 =
  −(3a2²+30a2+3)/(9a2²+26a2+9) dla sześciennego. Razem 5 punktów (zbiór 0-wymiarowy):
  2 nad Q(√94) (wyróżnik 1504 = 2⁵·47 = 16·94), 3 nad ciałem sześciennym (wyróżnik
  −2⁹·3·13·31, ciało nie-Galoisa).
- b1=0 (a1=1), b2=1: c1 ∝ a2+3, c2 ∝ 9a2²+26a2+9, gcd = 1 — brak zer.
- b1=1, b2=0 (a2=1): c1 ∝ a1²+10a1+1, c2 ∝ 3a1+1, gcd = 1 — brak zer.
- b1=b2=0: c1 = −12 ≠ 0.
Wniosek **OBLICZENIOWE**: (I)∧(II) nie mają zer wymiernych w P¹×P¹ ⇒ (przy wyprowadzeniu z iter01)
brak automorfizmu nad Q postaci a∘T∘b∘T'∘c z deg T = deg T' = 2 realizującego bijekcję.

## (3) Kontrola pozytywna — `skrypty/kontrola.py SEED` (logi `tmp/kontrola_SEED.log`)
Losowe wymierne G = a∘T∘b∘T'∘c (T,T' = (x, y+f(x)), f kwadratowe, b o obu pozadiagonalnych ≠ 0),
deg G = 4; 5 losowych wymiernych p_i, q_i = G(p_i). Dla seedów 1,2,3: c1, c2 zerują się w
oczekiwanym punkcie (l1 = część liniowa x∘c, l2 = x∘a⁻¹), a ta sama procedura `zera()` znajduje
to wymierne zero (np. seed 1: (3/5:1)×(1/2:1)). Kontrola stopnia 2 (G = a∘T∘b): jądro L1 zawiera
rozwiązanie niestałe dla wszystkich 3 seedów. **Wszystkie kontrole przeszły** — metoda nie daje
fałszywych negatywów w testowanych przypadkach.

## Porównanie z iter01 (`praca/iter01/zad2/notatki.md`, Sage)
Zgodne co do joty: to samo jądro L1, identyczne c1, c2, te same ideały (⟨15s²+38s−1, t+15s⟩ i
składowa sześcienna), te same sprzeczności w mapach b1=0, b2=0, b1=b2=0. Status: **potwierdzone**.

## Zakres / czego nie zrobiono
- Audyt dotyczy tylko rachunków; poprawność redukcji przez JvdK (stopnie 2,3,5 ⇒ a∘T∘b; 4 ⇒ jeden
  czynnik st. 4 lub 2·2) przyjęta z iter01, nie sprawdzana tu ponownie.
- Nie sprawdzano, czy nad Q(√94) lub ciałem sześciennym istnieje faktyczny automorfizm stopnia 4.
