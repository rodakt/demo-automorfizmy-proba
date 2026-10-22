# iter02/zad1 — audyt dowodu „brak automorfizmów Q² stopnia ≤ 5 realizujących bijekcję”

Skrypt niezależny: `skrypty/audyt.sage` (`timeout 120 sage skrypty/audyt.sage`, kilka sekund),
wyjście: `tmp/audyt_wyjscie.txt` (skopiowane niżej). Metoda sprawdzania stopnia 4 inna niż w iter01
(rugownik po (a2:b2) zamiast map afinicznych P¹×P¹), wynik zgodny.

## (1) Wyniki audytu punktów a–e

**(a) Jung–van der Kulk.** Twierdzenie (Jung 1942 dla char 0, van der Kulk 1953 dla dowolnego ciała):
Aut(k[x,y]) = Af *_{Af∩Bf} Bf dla każdego ciała k, w szczególności k = Q. Wniosek o stopniu
(np. Friedland–Milnor 1989, §2; van den Essen, *Polynomial Automorphisms…*, rozdz. 5): dla słowa
zredukowanego F = a0 T1 a1 … Tk ak (Ti ∈ Bf\Af, wewnętrzne ai ∈ Af\Bf) zachodzi
deg F = ∏ deg Ti, gdzie deg to właśnie stopień całkowity max(deg F1, deg F2) — ten sam co w CLAUDE.md.
F afiniczne (k = 0, stopień 1) jest pokryte osobno (krok 1) i dodatkowo przez L1. Brak usterki;
jedyna słabość: powołanie bez numeru twierdzenia (nie mam źródła pod ręką — luka bibliograficzna,
nie matematyczna). Uwaga: nie potrzebujemy ani jednoznaczności słowa, ani warunku ai ∉ Bf poza samym
wzorem na stopień.

**(b) Normalizacja i rozkłady.** Ti = (αx+β, γy+f(x)), deg f ≥ 2, = A∘(x, y+f(x)/γ) z A = (αx+β, γy)
afinicznym — część afiniczną pochłania sąsiad (po pochłonięciu ai mogą przestać być ∉ Bf, ale to
nieistotne: dalsze rozumowanie używa tylko postaci F = a∘T∘b lub a∘T∘b∘T'∘c z dowolnymi afinicznymi
a,b,c i znanych stopni Ti). deg Ti ≥ 2, więc iloczyn = 2,3,5 (pierwsze) ⇒ k = 1; iloczyn 4 ⇒ (4) lub (2,2).
Poprawne. Zamiana x↔y nie jest tu nawet potrzebna, bo Bf zawiera już tylko zmianę y.

**(c) Lemat L1.** x∘T = x dla T = (x, y+f(x)), więc dla F = a∘T∘b: x∘a⁻¹∘F = x∘T∘b = x∘b.
l1 = x∘b, l2 = x∘a⁻¹ niestałe (a,b odwracalne). Układ l1(p_i) = l2(q_i): macierz 5×6 rzędu 5,
jądro = ⟨(0,0,1,0,0,1)⟩, tj. tylko stałe — sprzeczność. Potwierdzone niezależnie (OBLICZENIOWE).
Ręcznie: z A,B,C,D (kwadrat) i E wynika a1=b1=a2=b2=0 — zgodne.

**(d) Warunki (I), (II) dla 2·2.** Sprawdzone krok po kroku:
- F = a∘T∘b∘T'∘c, r_i = T'(c(p_i)) = (l1(p_i), m(p_i)+f'(l1(p_i))), l1 = x∘c, m = y∘c;
  l2 = x∘a⁻¹: l2(q_i) = x∘T∘b(r_i) = x∘b(r_i) = α l1(p_i) + β m(p_i) + β f'(l1(p_i)) + γ
  ∈ span(1, x, y, l1²)(p_i) (deg f' ≤ 2). Poprawne; β = 0 nie szkodzi (warunek dalej konieczny).
- F⁻¹ = c⁻¹∘T'⁻¹∘b⁻¹∘T⁻¹∘a⁻¹, T⁻¹ = (x, y−f(x)) tej samej postaci i stopnia. Najbardziej prawy
  czynnik afiniczny to a⁻¹ ⇒ rola „l1” = x∘a⁻¹ = l2 (na płaszczyźnie q); najbardziej lewy to c⁻¹ ⇒
  rola „l2” = x∘(c⁻¹)⁻¹ = x∘c = l1. Zatem (II): l1(p_i) ∈ span(1,x,y,l2²)(q_i). Role zamienione dobrze.
- Stałe: (l+κ)² ∈ l² + span(1,l) ⊂ l² + span(1,x,y); stała w l2 — kolumna jedynek. Skalowanie —
  wyznacznik jednorodny. Więc (a1:b1), (a2:b2) ∈ P¹(Q). Poprawne.
- Degeneracja: jeśli kolumny 1,x,y,l1² (na p) są zależne, warunek (I) jest pusty (D1 ≡ 0 jako forma
  w (a2,b2)). Tu D1 = u·a2 + v·b2, u = −12(a1²+10a1b1+b1²), v = −4(9a1²+26a1b1+9b1²), gcd(u,v) = 1 ⇒
  u = v = 0 nie ma niezerowych rozwiązań nawet nad C (rugownik ≠ 0) — degeneracja nie występuje.
  Analogicznie wystarczy: dla (a1:b1) z (u,v) ≠ 0 jedynym (a2:b2) z D1 = 0 jest (v : −u); podstawienie
  do D2 daje formę 768(a1²−38a1b1−15b1²)(9a1³+29a1²b1+39a1b1²+3b1³), bez zer w P¹(Q)
  (b1=0 daje 6912 ≠ 0; brak pierwiastków wymiernych). [1,x,y] mają rząd 3 na p i na q.
  Wniosek iter01 (brak wymiernych (l1,l2)) potwierdzony niezależną metodą. Stopnie czynników
  (a1²−38a1−15: Q(√94), sześcienny nieprzywiedlny) zgodne z iter01/zad2 i zad3.

**(e) Jeden czynnik stopnia 4.** F = a∘T∘b z deg T = 4 — L1 nie używa stopnia T, więc pokryte.

**Werdykt: nie znalazłem błędu matematycznego.** Luki drobne: (i) brak dokładnego numeru twierdzenia
o multiplikatywności stopnia w źródle; (ii) w iter01/zad2 nie zaznaczono jawnie, że pochłonięcie
części afinicznych może zepsuć „zredukowanie” słowa — nieistotne dla dowodu (patrz b).

## (2) Czysty dowód (do raportu)

**Twierdzenie.** Każdy automorfizm wielomianowy F płaszczyzny Q² (współczynniki wymierne) z F(p_i)=q_i,
i=1..5, ma deg F ≥ 6. (UDOWODNIONE przy twierdzeniu Junga–van der Kulka + rachunki OBLICZENIOWE.)
Ponieważ istnieje zweryfikowane rozwiązanie stopnia 6 (iter01/zad1/rozwiazanie_st6.json), 6 jest
wtedy minimalnym stopniem (stan/zweryfikowane.json: przyjęte, stopień 6 — ZWERYFIKOWANE).

*Krok 0 (cytowane twierdzenie).* Jung–van der Kulk nad Q: F nieafiniczne ma postać
a0∘T1∘a1∘…∘Tk∘ak, ai afiniczne, Ti = (x, y+fi(x)), deg fi ≥ 2, i deg F = ∏ deg fi.
Stąd deg F ∈ {2,3,5} ⇒ k=1; deg F = 4 ⇒ k=1 (deg f1=4) lub k=2 (deg f1 = deg f2 = 2).

*Krok 1 (UDOWODNIONE).* Stopień 1: A,C,E leżą na y=x, a ich obrazy (1,1),(−1,−1),(1,−1) nie są
współliniowe; afiniczne odwzorowanie zachowuje współliniowość.

*Krok 2 (Lemat L1; UDOWODNIONE + OBLICZENIOWE, `skrypty/audyt.sage`, `iter01/zad2/skrypty/dolne.sage`).*
Jeśli F = a∘T∘b, T = (x, y+f(x)), to l2∘F = l1 dla niestałych afinicznych l1 = x∘b, l2 = x∘a⁻¹,
więc l1(p_i) = l2(q_i). Układ liniowy 5×6 ma rząd 5 i jądro złożone tylko z par stałych — sprzeczność.
Wyklucza stopnie 2, 3, 5 i stopień 4 z jednym czynnikiem.

*Krok 3 (UDOWODNIONE + OBLICZENIOWE).* F = a∘T∘b∘T'∘c, deg T = deg T' = 2. Z l1 = x∘c, l2 = x∘a⁻¹
(niestałe, wymierne, bez straty ogólności bez wyrazu wolnego, określone z dokładnością do skalara):
(I) wektor (l2(q_i)) ∈ span{(1),(x(p_i)),(y(p_i)),(l1(p_i)²)} ⊂ Q⁵, czyli D1 := det[1,x,y,l1²,l2] = 0;
(II) to samo dla F⁻¹ = c⁻¹∘T'⁻¹∘b⁻¹∘T⁻¹∘a⁻¹: D2 := det[1,x(q),y(q),l2(q)²,l1(p)] = 0.
D1 = u a2 + v b2 z gcd(u,v) = 1, więc (a2:b2) = (v:−u), a wtedy D2 = 768(a1²−38a1b1−15b1²)·
(9a1³+29a1²b1+39a1b1²+3b1³), co nie ma zer w P¹(Q). Sprzeczność.

*Krok 4.* Kroki 1–3 wyczerpują deg F ≤ 5. ∎

## Wyjście skryptu
```
L1 rank: 5 jadro: [
(0, 0, 1, 0, 0, 1)
]
D1= (-4) * (3*a1^2*a2 + 30*a1*b1*a2 + 3*b1^2*a2 + 9*a1^2*b2 + 26*a1*b1*b2 + 9*b1^2*b2)
D2= (4) * (9*a1*a2^2 + 3*b1*a2^2 + 26*a1*a2*b2 + 30*b1*a2*b2 + 9*a1*b2^2 + 3*b1*b2^2)
u= (-12) * (a1^2 + 10*a1*b1 + b1^2)  v= (-4) * (9*a1^2 + 26*a1*b1 + 9*b1^2)  gcd(u,v)= 1
forma w (a1:b1): (768) * (a1^2 - 38*a1*b1 - 15*b1^2) * (9*a1^3 + 29*a1^2*b1 + 39*a1*b1^2 + 3*b1^3)
pierwiastki wymierne (a1:b1=T:1): [] ; b1=0: 6912
u=v=0 rozw. wymierne: 1 -12 -36
rank [1,x,y] P,Q: 3 3
```
