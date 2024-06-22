:- use_module(library(clpfd)).

plecak(Wartosci, Wielkosci, Pojemnosc, Zmienne) :-
	length(Wartosci, N),
	length(Wielkosci, N),
	length(Zmienne, N),
	Zmienne ins 0..1,

	scalar_product(Wielkosci, Zmienne, #=, W),
		scalar_product(Wartosci, Zmienne, #=, V),
	W #=< Pojemnosc,
	once(labeling([max(V)], Zmienne)).
