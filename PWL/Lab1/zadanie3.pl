% Sprawdzenie, czy liczba jest pierwsza

% fakt, że liczba 2 jest pierwsza
is_prime(2).

% reguła, która definiuje, że liczba N jest pierwsza, jeśli
% N jest większa od 2 i nie ma dzielnika (\+ oznacza negację)
% Zaczyna sprawdzanie od 2.
is_prime(N) :- N > 2, \+ has_divisor(N, 2).

% Sprawdzenie, czy N ma dzielnik w zakresie od L do sqrt(N)

% reguła sprawdza, czy liczba N jest podzielna przez L bez reszty,
% co oznacza, że L jest dzielnikiem N.
has_divisor(N, L) :- N mod L =:= 0.

% reguła rekurencyjna, która sprawdza dzielniki N poczynając od L i inkremetując L o 1
% w każdym kroku rekurencji, ale tylko do momentu, gdy kwadrat bieżącego dzielnika L
% jest mniejszy niż N. Robimy to, ponieważ żaden dzielnik liczby na
% nie może być większy niz sqrt(n) (poza N samym w sobie).
has_divisor(N, L) :- L * L < N, L2 is L + 1, has_divisor(N, L2).

% Generowanie liczb pierwszych w zakresie

% reguła, która generuje liczby N, między LO, a HI włącznie
% (używając predytkatu wbudowanego between), a następnie sprawdza,
% czy N jest liczbą pierwszą za pomocą is_prime(N).
% Dla każdej liczby N spełniającej te warunki, reguła ta zwróci true,
% umożliwiając iterację przez wszystkie liczby pierwsze w zadanym zakresie.
prime(LO, HI, N) :- between(LO, HI, N), is_prime(N).

% uruchomienie: prime(10, 20, X).
