package body functions is
   function Factorial (N : Positive) return Positive is
   begin
      if N = 1 then
         return 1;
      else
         return N * Factorial (N - 1);
      end if;
   end Factorial;

   function GCD (A, B : Natural) return Positive is
   begin
      if B = 0 then
         return A;
      else
         return GCD (B, A mod B);
      end if;
   end GCD;

   procedure Solve_Diophantine (A, B : Integer; C : Natural; X, Y : out Integer; GCD : out Natural) is
      function Extended_Euclidean (A, B : Integer) return Equation_Solution is
      begin
         if B = 0 then
            return (1, 0, Positive(Abs(A)));
         else
            declare
               Next : Equation_Solution := Extended_Euclidean (B, A mod B);
            begin
               return (Next.Y, Next.X - (A / B) * Next.Y, Next.GCD);
            end;
         end if;
      end Extended_Euclidean;
   begin
      declare
         Result : Equation_Solution := Extended_Euclidean (A, B);
      begin
         if C mod Result.GCD /= 0 then
            X := 0;
            Y := 0;
            GCD := Result.GCD;
         else
            X := Result.X * Integer(C / Result.GCD);
            Y := Result.Y * Integer(C / Result.GCD);
            GCD := Result.GCD;
         end if;
      end;
   end Solve_Diophantine;
end functions;