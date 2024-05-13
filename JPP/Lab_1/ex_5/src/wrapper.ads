with Interfaces.C; use Interfaces.C;

package Wrapper is

   type Diofant_Result is record
      x : int;
      y : int;
   end record;

   function Factorial_Loop (N : int) return unsigned_long_long;
   pragma Import (C, Factorial_Loop, "factorial_loop");
   function Factorial_Rec (N : int) return unsigned_long_long;
   pragma Import (C, Factorial_Rec, "factorial_rec");

   function GCD_Loop (A, B : int) return int;
   pragma Import (C, GCD_Loop, "gcd_loop");
   function GCD_Rec (A, B : int) return int;
   pragma Import (C, GCD_Rec, "gcd_rec");

   function Diophantine_Loop (A, B, C : int) return Diofant_Result;
   pragma Import (C, Diophantine_Loop, "diofant_loop");
   function Diophantine_Rec (A, B, C : int) return Diofant_Result;
   pragma Import (C, Diophantine_Rec, "diofant_rec");

end Wrapper;
