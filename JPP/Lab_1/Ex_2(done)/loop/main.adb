with Ada.Text_IO; use Ada.Text_IO;
with functions ; use functions;

procedure Main is
    A : Integer := 35;
    B : Integer := 10;
    C : Positive := 55;
    Result : Equation_Solution;
begin
    Put_Line("Testing zad2 package:");
    Put_Line("Factorial is " & Integer'Image(Factorial(5)));
    Put_Line("GCD is " & Integer'Image(GCD(A, B)));
    Result := Solve_Diophantine(A, B, C);
    Put_Line("Solution to the Diophantine equation of" & Integer'Image(A) &"x +" & Integer'Image(B) &"y ="& Integer'Image(C) &" are  x = " & Integer'Image(Result.X) & ", y = " & Integer'Image(Result.Y) );
end Main;