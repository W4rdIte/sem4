package body functions is
   function Factorial (N : Positive) return Positive is
      Result : Positive := 1;
   begin
      for I in 1 .. N loop
         Result := Result * I;
      end loop;
      return Result;
   end Factorial;

   function GCD (A, B : Natural) return Positive is
      Local_A : Natural := A;
      Local_B : Natural := B;
      Temp : Natural;
   begin
      while Local_B /= 0 loop
         Temp := Local_B;
         Local_B := Local_A mod Local_B;
         Local_A := Temp;
      end loop;
      return Local_A;
   end GCD;

   function Solve_Diophantine (A, B : Integer; C : Natural) return Equation_Solution is
      X, Y, Last_X, Last_Y, Temp, Quotient : Integer;
      Local_A : Integer := A;
      Local_B : Integer := B;
   begin
      X := 0;
      Y := 1;
      Last_X := 1;
      Last_Y := 0;
      while Local_B /= 0 loop
         Quotient := Integer(Local_A / Local_B);
         Temp := Local_A;
         Local_A := Local_B;
         Local_B := Temp mod Local_B;
         Temp := X;
         X := Last_X - Quotient * X;
         Last_X := Temp;
         Temp := Y;
         Y := Last_Y - Quotient * Y;
         Last_Y := Temp;
      end loop;
      if C mod GCD(A, B) /= 0 then
         return (0, 0, GCD(A, B));
      else
         Last_X := Last_X * Integer(C / GCD(Local_A, Local_B));
         Last_Y := Last_Y * Integer(C / GCD(Local_A, Local_B));
         return (Last_X, Last_Y, GCD(Local_A, Local_B));
      end if;
   end Solve_Diophantine;
end functions;