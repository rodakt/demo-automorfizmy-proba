# Dziennik eksperymentu

Start: 22.10.2026 09:38

## Etap 0

Znana konstrukcja (dwa odwzorowania trójkątne z interpolacji) zapisana w praca/iter00/baza/.


## Iteracja 01 — plan

Wiemy tylko tyle, że konstrukcja bazowa daje zweryfikowany stopień 16. Krótki rachunek planisty (HIPOTEZA do sprawdzenia; skrypt `stan/plan_iter01_sprawdzenie.py`) oparty na twierdzeniu Junga–van der Kulka sugeruje, że: stopnie 1, 2, 3, 5 są niemożliwe (żaden pojedynczy czynnik trójkątny nie przenosi pęku prostych równoległych na pęk równoległy dla tej bijekcji), a stopień 4 (dwa czynniki kwadratowe) wymaga wymiernego punktu wspólnego dwóch krzywych w P1×P1, których wszystkie 5 punktów przecięcia jest niewymiernych (m.in. para nad Q(√94)). Stopień 6 (czynniki 3 i 2) prowadzi do warunku liniowego, więc powinien być osiągalny. Planujemy trzy niezależne zadania: (1) konstrukcja i weryfikacja rozwiązania stopnia 6, (2) staranny, niezależnie sprawdzony dowód, że stopień < 6 nad Q jest niemożliwy, (3) walidacja redukcji przez jawną konstrukcję automorfizmu stopnia 4 nad Q(√94). Jeśli wszystkie trzy się potwierdzą, problem będzie rozstrzygnięty: najniższy stopień 6 z dowodem dolnego ograniczenia.
