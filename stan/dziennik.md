# Dziennik eksperymentu

Start: 22.10.2026 09:38

## Etap 0

Znana konstrukcja (dwa odwzorowania trójkątne z interpolacji) zapisana w praca/iter00/baza/.


## Iteracja 01 — plan

Wiemy tylko tyle, że konstrukcja bazowa daje zweryfikowany stopień 16. Krótki rachunek planisty (HIPOTEZA do sprawdzenia; skrypt `stan/plan_iter01_sprawdzenie.py`) oparty na twierdzeniu Junga–van der Kulka sugeruje, że: stopnie 1, 2, 3, 5 są niemożliwe (żaden pojedynczy czynnik trójkątny nie przenosi pęku prostych równoległych na pęk równoległy dla tej bijekcji), a stopień 4 (dwa czynniki kwadratowe) wymaga wymiernego punktu wspólnego dwóch krzywych w P1×P1, których wszystkie 5 punktów przecięcia jest niewymiernych (m.in. para nad Q(√94)). Stopień 6 (czynniki 3 i 2) prowadzi do warunku liniowego, więc powinien być osiągalny. Planujemy trzy niezależne zadania: (1) konstrukcja i weryfikacja rozwiązania stopnia 6, (2) staranny, niezależnie sprawdzony dowód, że stopień < 6 nad Q jest niemożliwy, (3) walidacja redukcji przez jawną konstrukcję automorfizmu stopnia 4 nad Q(√94). Jeśli wszystkie trzy się potwierdzą, problem będzie rozstrzygnięty: najniższy stopień 6 z dowodem dolnego ograniczenia.

## Iteracja 02 — plan

Po iteracji 01 mamy zweryfikowane rozwiązanie stopnia 6 (złożenie czynników trójkątnych stopni 3 i 2) oraz dowód z zad2, że nad Q stopień ≤ 5 jest niemożliwy (Jung–van der Kulk, lemat o poziomicach, warunki wyznacznikowe c1=c2=0 bez zer wymiernych). Zad3 pokazało, że redukcja jest ostra: nad Q(√94) i nad ciałem sześciennym istnieje automorfizm stopnia 4, więc przeszkoda nad Q jest czysto arytmetyczna. Problem wygląda na rozstrzygnięty (najniższy stopień 6), ale dowód dolnego ograniczenia w całości sprawdził tylko jeden wykonawca. Dlatego przed ogłoszeniem końca zlecamy dwa niezależne audyty: teoretyczny (krytyczne sprawdzenie kroków a–e i czysty dowód do raportu) oraz obliczeniowy (odtworzenie rachunków w sympy zamiast Sage, z kontrolą pozytywną na sztucznym przykładzie z wymiernym automorfizmem stopnia 4). Nie szukamy już niższego stopnia nad Q; jeśli audyt wykryje błąd, wyznaczy on kierunek iteracji 03, a jeśli nie — iteracja 03 może zakończyć eksperyment.

## Iteracja 03 — plan

Obie iteracje audytu potwierdziły wynik: mamy ZWERYFIKOWANE rozwiązanie stopnia 6 (iter01/zad1) oraz dowód, że nad Q stopień ≤ 5 jest niemożliwy (iter01/zad2). Dowód przeszedł niezależny audyt teoretyczny (iter02/zad1, inną metodą eliminacji) i obliczeniowy w sympy z kontrolą pozytywną (iter02/zad2). Kroki rachunkowe dowodu mają etykietę OBLICZENIOWE, rozumowanie redukcyjne (Jung–van der Kulk) — UDOWODNIONE; jedyna znana luka jest bibliograficzna (brak numeru twierdzenia w cytowaniu). Przeszkoda dla stopnia 4 jest czysto arytmetyczna: nad Q(√94) i nad ciałem sześciennym stopień 4 jest osiągalny (iter01/zad3). Uznajemy pytanie za rozstrzygnięte — minimalny stopień nad Q wynosi 6 — i kończymy eksperyment (`koniec: true`), zostawiając pozostały czas na redakcję raportu.

## Raport — wersja końcowa

Napisano sekcje metoda, przebieg, wnioski (z listą pytań otwartych), streszczenie i literaturę; raport podaje zweryfikowany stopień 6 oraz dowód (przy cytowanym tw. Junga–van der Kulka, z krokami obliczeniowymi), że nad Q stopień ≤5 jest niemożliwy. Kompilacja bez błędów.
