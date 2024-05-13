srodkowy(L, X) :-
    length(L, Len),
    Len mod 2 =:= 1, % Check if length of list L is odd
    MiddleIndex is (Len + 1) // 2, % Calculate the middle index
    nth1(MiddleIndex, L, X). % X is the middle element if list length is odd
