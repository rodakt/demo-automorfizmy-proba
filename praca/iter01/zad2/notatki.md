# iter01/zad2 — ograniczenie dolne: brak automorfizmów stopnia 1–5 nad Q

Skrypt: `skrypty/dolne.sage` (uruchomienie: `cd skrypty; timeout 200 sage dolne.sage`, ok. 10 s).
Wyjście: `tmp/wynik_dolne.txt`. Wszystkie rachunki niezależnie od planisty, dokładnie nad Q.

## Dane
p = A(-1,-1), B(1,-1), C(1,1), D(-1,1), E(2,2);  q = (1,1), (-1,1), (-1,-1), (2,2), (1,-1).

## Narzędzie: twierdzenie Junga–van der Kulka (powołanie, bez numeru twierdzenia)
Grupa automorfizmów k[x,y] (k dowolne ciało, tu Q) jest produktem amalgamowanym grupy afinicznej Af
i grupy trójkątnej Bf = {(αx+β, γy+f(x))} nad ich przecięciem. Konsekwencja (np. Friedland–Milnor 1989,
„Dynamical properties of plane polynomial automorphisms”, §2; van den Essen, „Polynomial Automorphisms
and the Jacobian Conjecture”, rozdz. 5): każdy F nieafiniczny ma postać zredukowaną
F = a0∘T1∘a1∘…∘Tk∘ak, Ti ∈ Bf\Af, wewnętrzne ai ∈ Af\Bf, i wtedy deg F = ∏ deg Ti.
Pochłaniając części afiniczne Ti do sąsiadów, można przyjąć Ti = (x, y+fi(x)) (zmiana y; zamiana
x↔y jest afiniczna, więc to bez straty ogólności). Numerów twierdzeń nie podaję, bo nie mam źródła pod ręką.
Wniosek: deg F ∈ {1, 2, 3, 5} ⇒ F afiniczne albo F = a∘T∘b z jednym T (stopnie pierwsze);
deg F = 4 ⇒ F = a∘T∘b (deg T = 4) albo F = a∘T∘b∘T'∘c, deg T = deg T' = 2.

## Krok 1 (UDOWODNIONE, sprawdzone w skrypcie): stopień 1
A, C, E leżą na prostej y = x (det = 0), a ich obrazy (1,1), (-1,-1), (1,-1) nie są współliniowe (det = 4).
Odwzorowanie afiniczne zachowuje współliniowość ⇒ brak automorfizmu stopnia 1.
(Też: obrazy A, C, D = (1,1),(-1,-1),(2,2) współliniowe, a A, C, D nie.)

## Krok 2 — Lemat L1 (UDOWODNIONE + OBLICZENIOWE)
Jeśli F = a∘T∘b, T = (x, y+f(x)), to x∘T = x, więc l2∘F = l1 dla l2 := x∘a⁻¹, l1 := x∘b — oba
niestałe funkcjonały afiniczne. Zatem l1(p_i) = l2(q_i) dla i=1..5. (To samo dla F afinicznego.)
Układ liniowy na (a1,b1,c1,a2,b2,c2), l_j = a_j x + b_j y + c_j: jądro macierzy 5×6 jest
rozpięte przez (0,0,1,0,0,1), tj. tylko l1 = l2 = stała. (OBLICZENIOWE: `dolne.sage`, część (2).)
Wniosek (UDOWODNIONE przy JvdK): brak automorfizmu stopnia 2, 3, 5 i brak postaci a∘T∘b z deg T = 4.

## Krok 3 — stopień 4 jako a∘T∘b∘T'∘c, deg T = deg T' = 2
Wyprowadzenie (UDOWODNIONE). Niech l1 := x∘c, m := y∘c (c afiniczne ⇒ 1, l1, m bazą funkcji afinicznych),
r_i := T'(c(p_i)) = (l1(p_i), m(p_i) + f(l1(p_i))), deg f ≤ 2. Niech l2 := x∘a⁻¹.
Ponieważ x∘T = x, mamy l2(q_i) = x(T(b(r_i))) = x(b(r_i)) = α r_i,1 + β r_i,2 + γ, czyli
  (I) l2(q_i) = μ(p_i) + β f(l1(p_i)),  μ afiniczne.
Wektor (l2(q_i))_i leży więc w przestrzeni rozpiętej przez wektory 1, x(p_i), y(p_i), l1(p_i)² w Q⁵
(l1 jest kombinacją 1,x,y). Warunek konieczny: det[1, x_i, y_i, l1(p_i)², l2(q_i)] = 0.
Nie korzystam tu z nietrójkątności b ani z β≠0 — warunek jest konieczny zawsze, co tylko wzmacnia wniosek.
Symetrycznie dla F⁻¹ = c⁻¹∘T'⁻¹∘b⁻¹∘T⁻¹∘a⁻¹ (T⁻¹ też zmienia tylko y, ten sam stopień), rolę l1 gra
x∘a⁻¹ = l2 (na płaszczyźnie q), a rolę l2 gra x∘c = l1:
  (II) det[1, x(q_i), y(q_i), l2(q_i)², l1(p_i)] = 0.
Stałe w l1, l2 nie mają znaczenia: (l+c)² = l² + 2c·l + c² ∈ l² + span(1,x,y), a stała w l2 to
wielokrotność kolumny jedynek. Więc wystarczy l1 = a1x+b1y, l2 = a2x+b2y, (a_j:b_j) ∈ P¹ (l_j niestałe,
bo l1 = x∘c, l2 = x∘a⁻¹, a, c odwracalne).

OBLICZENIOWE (`dolne.sage`, część (3)), zgodne z planistą:
 c1 = -4(3a1²a2 + 9a1²b2 + 30a1b1a2 + 26a1b1b2 + 3b1²a2 + 9b1²b2)   [stopień (2,1)]
 c2 =  4(9a1a2² + 26a1a2b2 + 9a1b2² + 3b1a2² + 30b1a2b2 + 3b1b2²)   [stopień (1,2)]
Wspólne zera w P¹×P¹, cztery mapy pokrywające:
 - (t:1)×(s:1): ideał zerowymiarowy; minimalne ideały pierwsze nad Q:
   ⟨15s²+38s−1, t+15s⟩ (wyróżnik 1504 = 16·94 ⇒ punkty nad Q(√94)) oraz
   ⟨3s³+39s²+29s+9, 3s²+9t+39s+29⟩ (sześcienny nieprzywiedlny nad Q). Rugowniki:
   w t: (t²−38t−15)(9t³+29t²+39t+3), w s: (15s²+38s−1)(3s³+39s²+29s+9) — brak pierwiastków wymiernych;
   `I.variety(QQ)` = [].
 - (t:1)×(1:0): c1 ∝ t²+10t+1, c2 ∝ 3t+1 — sprzeczne (ideał = (1)).
 - (1:0)×(s:1): c1 ∝ s+3, c2 ∝ 9s²+26s+9 — sprzeczne (9·9−78+9=12≠0).
 - (1:0)×(1:0): c1 = −12 ≠ 0.
Przypadek zdegenerowany (dla pewnego (a1:b1) c1 ≡ 0 jako forma w (a2,b2)): wymagałby wspólnego zera
3a1²+30a1b1+3b1² i 9a1²+26a1b1+9b1²; wtedy zbiór zer miałby składową wymiaru 1, a w każdej mapie
ideał ma wymiar 0 lub jest jednostkowy — więc taki przypadek nie występuje (sprawdzone, nie tylko założone).
Wniosek: brak wymiernych (l1,l2) ⇒ brak automorfizmu postaci a∘T∘b∘T'∘c, deg T = deg T' = 2.

## Krok 4 — wniosek (UDOWODNIONE modulo JvdK + rachunki OBLICZENIOWE z kroków 2–3)
Żaden automorfizm Q² o współczynnikach wymiernych stopnia ≤ 5 nie realizuje tej bijekcji; każde
rozwiązanie wymierne ma stopień ≥ 6. (6 = 2·3 — pierwszy stopień nie wykluczony.)
Uwaga: nad Q(√94) warunki konieczne (I),(II) dla stopnia 4 mają rozwiązania — nie sprawdzałem, czy
wtedy istnieje faktyczny automorfizm stopnia 4 nad Q(√94) (warunki są tylko konieczne). HIPOTEZA.

## Ocena rozumowania planisty
Nie znalazłem błędu: wielomiany c1, c2, rozkład zer (para z √94, trójka z nieprzywiedlnego sześciennego)
i brak zer w mapach b1=0 / b2=0 potwierdzone niezależnie. Doprecyzowanie: warunek (I) nie wymaga
„nietrójkątności b”, a planista pisał „μ niezależne od l1” — do dowodu niepotrzebne.

## Luki / czego nie zrobiono
- Numer twierdzenia o multiplikatywności stopnia w źródle nie został sprawdzony (powołanie ogólne).
- Nie badano stopnia 6 (ograniczenie górne — inne zadania).
