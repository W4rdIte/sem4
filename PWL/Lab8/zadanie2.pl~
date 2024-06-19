:- use_module(library(clpfd)).

% jeśli n-ty element listy Zmienne ma wartość 1,
% to bierzemy przedmiot, jeśli 0 - nie bierzemy
plecak(Wartosci, Wielkosci, Pojemnosc, Zmienne) :-
	length(Wartosci, N),
	length(Wielkosci, N),
	length(Zmienne, N),
	Zmienne ins 0..1,
	% W - łączna wielkość wybranych przedmiotów
	scalar_product(Wielkosci, Zmienne, #=, W),
	% V - łączna wartość wybranych przedmiotów
	scalar_product(Wartosci, Zmienne, #=, V),
	W #=< Pojemnosc,
	once(labeling([max(V)], Zmienne)).