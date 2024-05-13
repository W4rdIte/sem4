package functions is
   type Equation_Solution is record
      X : Integer;
      Y : Integer;
      GCD : Positive;
   end record;

   function Factorial (N : Positive) return Positive;
   pragma Export (C, Factorial, "Factorial_C");
   function GCD (A, B : Natural) return Positive;
   pragma Export (C, GCD, "GCD_C");
   procedure Solve_Diophantine (A, B : Integer; C : Natural; X, Y : out Integer; GCD : out Natural);
   pragma Export (C, Solve_Diophantine, "Solve_Diophantine_C");

end functions;