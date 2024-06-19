consult('zadanie1.pl').

split(IN, OUT1, OUT2) :-
   split(IN, OUT1, OUT2, 0).

split(IN, OUT1, OUT2, Selection) :-
   freeze(IN,
      (IN = [H | T] ->
         (Selection = 0 ->
            OUT1 = [H | OUT1_new],
            split(T, OUT1_new, OUT2, 1);
            OUT2 = [H | OUT2_new],
            split(T, OUT1, OUT2_new, 0)
         );
         (OUT1 = [], OUT2 = [])
      )
   ), !.


merge_sort(IN, OUT) :-
   freeze(IN,
      (IN = [H | T] ->
         (freeze(T,
            (T = [] ->
                OUT = [H];
                split(IN, O1, O2),
                merge_sort(O1, OUT1),
                merge_sort(O2, OUT2),
                merge(OUT1, OUT2, OUT)
             )
          ));
          OUT = []
      )
   ), !.

% split([a, b, c, d], OUT1, OUT2).
% split([a, b, c, d | A], OUT1, OUT2).
% merge_sort([5, 1, 3, 2, 4], X).
% merge_sort(X, Y), X = [4, 1, 3, 2].
% merge_sort([5, 1, 3, 2, 4 | A], X).
