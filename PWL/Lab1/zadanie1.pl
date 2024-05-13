% Definicje zestawów relacji rodzinnych
% X jest matką, jeśli X jest kobietą i jest rodzicem jakiegoś dziecka
jest_matka(X) :- kobieta(X), rodzic(X, _).
jest_ojcem(X) :- mezczyzna(X), rodzic(X, _).
jest_synem(X) :- mezczyzna(X), rodzic(X, _).
siostra(X, Y) :- kobieta(X), rodzic(Z, X), rodzic(Z, Y), X \= Y.
dziadek(X, Y) :- mezczyzna(X), rodzic(X, Z), rodzic(Z, Y).
rodzenstwo(X, Y) :- rodzic(Z, X), rodzic(Z, Y), X \= Y.

mezczyzna(adam).
kobieta(ewa).
rodzic(adam, jan).
rodzic(ewa, jan).