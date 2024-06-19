% Author: Patrycja Paradowska
% 16 czerwca 2020r., Lista 9. Prolog, Zadanie 1.

% Napisz predykat schedule(Horizon, Starts, MakeSpan), ktory dla danego horyzontu 
% (koniec dostępnego zakresu czasu), oddaje liste chwil rozpoczecia zadan Starts,
% tz. wykonujac zadania w tych chwilach nie przekroczy sie zadanych limitów zasobow oraz
% termin zakonczenia najpozniej konczacego sie zadania MakeSpan jest jak najwczesniejszy.

:- use_module(library(clpfd)).

% Predykat ten definiuje liste zadan. Kazde zadanie opisane jest lista
% trojelementowa: 1. element to czas trwania zadania, 2. to liczba jednostek pierwszego zasobu
% potrzebnego do jego wykonania a 3. to liczba jednostek drugiego zasobu potrzebnego do jego wykonania

lista_zadan([ 
   %D R1 R2
   [2, 1, 3],
   [3, 2, 1],
   [4, 2, 2],
   [3, 3, 2],
   [3, 1, 1],
   [3, 4, 2],
   [5, 2, 1]]).

% Predykat resources(Res1, Res2) definiuje liczbe dostepnych w kazdej chwili jednostek pierwszego i drugiego zasobu
%         R1 R2
resources(5, 5).

mt([], _, [], [], [], _).
mt([[D, X1, X2] | L1], H, [task(S, D, E, X1, _) | L2],
	[task(S, D, E, X2, _) | L3], [S | L4], MS) :-
    S in 0..H,
    E #= S + D, MS #>= E,
    mt(L1, H, L2, L3, L4, MS).

schedule(H, Ss, MS) :-
    lista_zadan(L),
    resources(X1, X2),
    MS in 0..H,
    mt(L, H, Y1, Y2, Ss, MS),
    cumulative(Y1, [limit(X1)]),
    cumulative(Y2, [limit(X2)]),
    once(labeling([min(MS), ff], [MS | Ss])).
