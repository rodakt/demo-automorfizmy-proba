# iter01/zad1 — konstrukcja stopnia 6 (trójkątne stopni 3 i 2)

## Wynik: ZWERYFIKOWANE (lokalnie) — rozwiązanie stopnia 6
Plik `rozwiazanie_st6.json`, skrypt `skrypty/st6.py` (sympy, dokładnie nad Q).

Konstrukcja F = H⁻¹ ∘ P, gdzie
- P(p) = (l1(p), mu(p) + f(l1(p))), l1 = x − 3y, mu = −1/2 − 25/24·x + 1/8·y, f(t) = t²/8 + t³/96 (stopień 3);
- H(q) = (nu(q) + g(l2(q)), l2(q)), l2 = y, nu = 8/3 − x + 3y, g(t) = −8/3·t² (stopień 2).
Punkty pośrednie s_i = (l1(p_i), l2(q_i)) = P(p_i) = H(q_i).
Wybór l2 = y, l1 = x − 3y wg planu (c2 = 0 liniowe w (a1,b1): 36a1 + 12b1 = 0).
Niedegeneracja: det[[1,−3],[−25/24,1/8]] = 1/8 − 75/24 ≠ 0; det[[−1,3],[0,1]] = −1 ≠ 0.
Układy (I) (5 równań, 5 niewiadomych) i (II) (5 równań, 4 niewiadome) mają jednoznaczne rozwiązania wymierne.

Słowo (pierwszy działa pierwszy): afiniczne (l1, mu) → trójkątne y += x²/8 + x³/96 → trójkątne x += 8/3·y² (= odwrotność x −= g) → afiniczne (X,Y) ↦ (−X + 3Y + 8/3, Y) (= odwrotność q ↦ (nu, l2)).

Wynik weryfikatora:
```
"ok": true, "stopien": 6, "bledy": [], "stopnie_czynnikow": [3, 2], "liczba_wyrazow": 38
```

## Czego nie sprawdzano
- Ograniczenia dolnego (stopnie 4, 5) nie badałem — argumenty planisty (L1, wyznacznik c1,c2) mają status HIPOTEZA do niezależnej weryfikacji.
- Nie szukano stopnia 4 nad Q innymi drogami.
