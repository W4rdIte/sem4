package functions is
   type Equation_Solution is record
      X : Integer;
      Y : Integer;
      GCD : Positive;
   end record;

   function Factorial (N : Positive) return Positive;
   function GCD (A, B : Natural) return Positive;
   function Solve_Diophantine (A, B : Integer; C : Natural) return Equation_Solution;
end functions;