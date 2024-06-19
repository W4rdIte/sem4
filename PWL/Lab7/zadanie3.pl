filozofowie :-
	mutex_create(F0),
	mutex_create(F4),
	thread_create(start(0, F4, F0), ID0, []),
	mutex_create(F1),
	thread_create(start(1, F1, F0), ID1, []),
	mutex_create(F2),
	thread_create(start(2, F2, F1), ID2, []),
	mutex_create(F3),
	thread_create(start(3, F3, F2), ID3, []),
	thread_create(start(4, F4, F3), ID4, []),

	thread_join(ID0, _),
	thread_join(ID1, _),
	thread_join(ID2, _),
	thread_join(ID3, _),
	thread_join(ID4, _).

identifier(0, Kto) :- format('[~w]   ', [Kto]), !.

identifier(N, Kto) :-
	write(' '),
	N_new is N - 1,
	identifier(N_new, Kto).

identifier(Kto) :-
	Number is Kto,
	identifier(Number, Kto).

napisz(Task, Kto) :-
	with_mutex(print, (identifier(Kto),
		write(Task), nl)).

mysli(Kto, ML, MR) :-
	napisz('mysli', Kto),
	sleep(2),
	podnies_prawy_widelec(Kto, ML, MR).

podnies_prawy_widelec(Kto, ML, MR) :-
	napisz('chce prawy widelec', Kto),
	mutex_lock(MR),
	napisz('podnosi prawy widelec', Kto),
	podnies_lewy_widelec(Kto, ML, MR).

podnies_lewy_widelec(Kto, ML, MR) :-
	napisz('chce lewy widelec', Kto),
	mutex_lock(ML),
	napisz('podnosi lewy widelec', Kto),
	jedz(Kto, ML, MR).

jedz(Kto, ML, MR) :-
	napisz('je', Kto),
	sleep(2),
	odloz_prawy_widelec(Kto, ML, MR).

odloz_prawy_widelec(Kto, ML, MR) :-
	napisz('odklada prawy widelec', Kto),
	mutex_unlock(MR),
	odloz_lewy_widelec(Kto, ML, MR).

odloz_lewy_widelec(Kto, ML, MR) :-
	napisz('odklada lewy widelec', Kto),
	mutex_unlock(ML),
	mysli(Kto, ML, MR).

start(Kto, Lewy_widelec, Prawy_widelec) :-
	mysli(Kto, Lewy_widelec, Prawy_widelec).

% filozofowie.
