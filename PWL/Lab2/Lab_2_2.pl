jednokrotnie(X, L) :-
    count_occurrences(X, L, 1).

dwukrotnie(X, L) :-
    count_occurrences(X, L, 2).

count_occurrences(_, [], 0).
count_occurrences(X, [X|T], N) :-
    count_occurrences(X, T, N1),
    N is N1 + 1.
count_occurrences(X, [H|T], N) :-
    X \= H,
    count_occurrences(X, T, N).
