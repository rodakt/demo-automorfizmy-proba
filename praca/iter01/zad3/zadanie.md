# Walidacja redukcji: automorfizm stopnia 4 nad Q(sqrt 94) i weryfikacja

KONTEKST (rachunek planisty, do niezależnego sprawdzenia, status: HIPOTEZA): 
Punkty: A=(-1,-1)->C, B=(1,-1)->D, C=(1,1)->A, D=(-1,1)->E=(2,2), E->B (dane w zadanie.json).
Twierdzenie Junga–van der Kulka (dowolne ciało, więc też Q): każdy automorfizm to słowo zredukowane a0 T1 a1 T2 ... Tk ak (ai afiniczne, Ti trójkątne stopnia >=2, wewnętrzne ai nie trójkątne), a deg = iloczyn deg Ti. Stąd stopnie pierwsze d (2,3,5,...) dają tylko postać a∘T∘b z jednym czynnikiem trójkątnym.
(L1) a∘T∘b z jednym T przeprowadza poziomice funkcjonału l1 = x∘b na poziomice l2 = x∘a^{-1}, więc musiałoby być l1(p_i) = l2(q_i) dla wszystkich i z niestałymi afinicznymi l1,l2. Planista rozwiązał ten układ liniowy ręcznie: ma tylko rozwiązania stałe. Wniosek: stopnie 1,2,3,5,7 i 'pojedynczy czynnik stopnia 4' niemożliwe.
(Redukcja dwuczynnikowa) F = a∘T∘b∘T'∘c. Niech l1 = x∘c (funkcjonał na płaszczyźnie p zachowywany przez T'c), l2 = x∘a^{-1} (na płaszczyźnie q). Po afinicznej zmianie środkowej płaszczyzny punkty pośrednie to s_i = (l1(p_i), l2(q_i)). Warunki istnienia z deg T' <= k, deg T <= l:
 (I)  l2(q_i) = mu(p_i) + f(l1(p_i)), mu afiniczne niezależne od l1, deg f <= k;
 (II) l1(p_i) = nu(q_i) + g(l2(q_i)), nu afiniczne niezależne od l2, deg g <= l.
Dla k=2 warunek (I) wymaga det[1, px_i, py_i, l1(p_i)^2, l2(q_i)]_{i=1..5} = 0; analogicznie (II) dla l=2. Dla k=3 warunek (I) jest generycznie spełniony automatycznie (5 wektorów 1,x,y,l1^2,l1^3 w Q^5).
Krótkie sprawdzenie planisty (sympy, plik stan/plan_iter01_sprawdzenie.py) dla l1=a1 x+b1 y, l2=a2 x+b2 y:
 c1 = -4(3a1^2a2 + 9a1^2b2 + 30a1a2b1 + 26a1b1b2 + 3a2b1^2 + 9b1^2b2),
 c2 =  4(9a1a2^2 + 26a1a2b2 + 9a1b2^2 + 3a2^2b1 + 30a2b1b2 + 3b1b2^2);
 wspólne zera w P1xP1: brak w mapach b1=0 lub b2=0; w mapie b1=b2=1 pięć punktów, wszystkie niewymierne (para z sqrt(94), trójka z nieprzywiedlnego sześciennego). Sugeruje to: stopień 4 niemożliwy nad Q, ale możliwy nad Q(sqrt 94).

TWOJE ZADANIE: sprawdzić, że redukcja do warunków (I),(II) jest nie tylko konieczna, ale i wystarczająca, przez jawną konstrukcję automorfizmu stopnia 4 o współczynnikach w Q(sqrt(94)) (to NIE będzie rozwiązanie w sensie weryfikatora — nie twórz plików rozwiazanie*.json; to kontrola poprawności teorii, ważna dla raportu: pokazuje, że przeszkoda dla stopnia 4 jest arytmetyczna).
Kroki: (1) Niezależnie (sympy lub Sage) wylicz wspólne zera c1=c2=0 przy b1=b2=1, znajdź parę punktów nad Q(sqrt 94). (2) Dla jednego z nich rozwiąż (I),(II) z k=l=2 (liniowo względem mu,f,nu,g), sprawdź niedegenerację, złóż F = złożenie czynników i jawnie policz F oraz odwrotność G dokładnie w Q(sqrt 94) (sympy z sqrt(94) symbolicznie, upraszczaj). (3) Sprawdź F(p_i)=q_i dla wszystkich 5 punktów, G∘F = id, deg F = 4. (4) Dodatkowo (jeśli zostanie czas): sprawdź, czy któryś z trzech punktów sześciennych też daje rozwiązanie (wystarczy numerycznie, opisz jako takie).
Rezultat: praca/iter01/zad3/notatki.md (etykiety: OBLICZENIOWE z dokładnym opisem), skrypt w skrypty/, wynik.json (pola: czy_konstrukcja_dziala, ciało, stopien, uwagi). Jeśli konstrukcja NIE działa, to sygnał błędu w redukcji — opisz dokładnie, gdzie się psuje.
