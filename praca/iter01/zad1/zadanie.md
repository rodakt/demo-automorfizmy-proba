# Konstrukcja automorfizmu stopnia 6 (złożenie trójkątnych stopni 3 i 2)

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

TWOJE ZADANIE: zbuduj zweryfikowane rozwiązanie stopnia 6 (lub, w razie porażki, najniższego możliwego < 16, np. 8 = 4·2 lub 9 = 3·3).
Plan: przypadek k=3 (T' stopnia 3), l=2 (T stopnia 2) — wtedy jedynym warunkiem jest c2 = 0, który jest LINIOWY w (a1,b1). Np. l2 = y (a2=0,b2=1) daje c2 = 4(9a1+3b1) => l1 = x - 3y. Sprawdź warunki niedegeneracji (mu niezależne od l1, nu niezależne od l2, układ (I) z k=3 rozwiązywalny), wylicz mu, f, nu, g i złóż słowo czynników w formacie 'slowo' z CLAUDE.md (pierwszy czynnik działa pierwszy): p -> (l1(p), mu(p)+f(l1(p))) [afiniczne p->(l1,mu) potem trójkątne zmienia y], potem mapa środkowa, potem odwrotność q -> (nu(q)+g(l2(q)), l2(q)) [też jako afiniczne+trójkątne]. Uważaj na kierunek: odwrotność trójkątnego (x+g(y),y) to (x-g(y),y). Jeśli l2=y nie zadziała, próbuj innych wymiernych l2 albo zamienionej kolejności (k=2, l=3). Możesz też najpierw policzyć w sympy jawne F i G oraz sprawdzić F(p_i)=q_i i G∘F=id.
Rezultat: praca/iter01/zad1/rozwiazanie_st6.json sprawdzone przez `$PYTHON narzedzia/verify.py sprawdz --zadanie zadanie.json ...` (wklej wynik do notatek), skrypt w skrypty/, notatki.md, wynik.json (pola: stopien, plik, status). Nie przekraczaj 12 min; jeśli stopień 6 nie wychodzi w 8 min, zgłoś cokolwiek < 16 (np. k=l=3 daje 9 bez warunków).
