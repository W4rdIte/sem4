% Bezpośrednie leżenie na
% ta reguła meówi, że blok Black1 jest nad blokiem block2, jeśli
% Block1 leży bezpośrednio n Block2, co jest bezpośrednio określone
% przez fakty on
above(Block1, Block2) :- on(Block1, Block2).

% Tranzytywne leżenie na (przez inny blok)
% Ta reguła definiuje above w sposób tranzytywny. Oznacza to, że jeśli blok Block1
% leży na bloku BlockX, a następnie blok BlockX lezy nad blokiem Block2, to
% Block1 również jest nad Block2. To rekurencyjne wywołanie pozwala na przechodzenie
% przez stos bloków, gdzie blok może leżeć nad innym blokiem
% nie tylko bezpośrendio, ale też pośrednio, przez serię innych bloków.
above(Block1, Block2) :- on(Block1, BlockX), above(BlockX, Block2).

on(a, b).
on(b, c).
on(c, d).

% swipl
% above(a, d) = true
% above(d, b) = false
