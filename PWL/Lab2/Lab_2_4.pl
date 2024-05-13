nieparzysty(L,X,Reszta) :-
    nth0(I,L,X,Reszta),
    I mod 2 =:= 0.
% P1 - pomocnicza lista w ktorej sa elementy juz wstawione do ciagu ale
% tylko raz
% P2 - poprawna lista przed obroceniem
% X - wynik
pom([], Y, Y, P2, X) :-
    reverse(P2,X).
pom(P1, I, OgrGorne, P2, X) :-
    J is I+1,
    I < OgrGorne,
    pom([J | P1], J, OgrGorne, [J | P2], X).

pom(P1, I, OgrGorne, P2, X) :-
    nieparzysty(P1,N,Reszta),
    pom(Reszta, I, OgrGorne, [N | P2], X).

lista(N, X) :-
    pom([], 0, N, [], X).
