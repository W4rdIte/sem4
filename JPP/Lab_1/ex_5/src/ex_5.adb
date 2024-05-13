with Ada.Text_IO;  use Ada.Text_IO;
with Interfaces.C; use Interfaces.C;
with Wrapper;

procedure Ex_5 is
begin
  -- Testing factorial functions
  Put_Line ("Testing factorial functions...");
  declare
    N           : Integer                         := 5;
    Result_Loop : Interfaces.C.unsigned_long_long :=
     Wrapper.Factorial_Loop (Interfaces.C.int (N));
    Result_Rec  : Interfaces.C.unsigned_long_long :=
     Wrapper.Factorial_Rec (Interfaces.C.int (N));
  begin
    Put_Line
     ("Factorial of " & Integer'Image (N) & " using loop: " &
      Integer'Image (Integer (Result_Loop)));
    Put_Line
     ("Factorial of " & Integer'Image (N) & " using recursion: " &
      Integer'Image (Integer (Result_Loop)));
  end;

  -- Testing GCD functions
  Put_Line ("Testing GCD functions...");
  declare
    A           : Integer          := 15;
    B           : Integer          := 10;
    Result_Loop : Interfaces.C.int :=
     Wrapper.GCD_Loop (Interfaces.C.int (A), Interfaces.C.int (B));
    Result_Rec  : Interfaces.C.int :=
     Wrapper.GCD_Rec (Interfaces.C.int (A), Interfaces.C.int (B));
  begin
    Put_Line
     ("GCD of " & Natural'Image (Integer (A)) & " and " &
      Natural'Image (Integer (B)) & " using loop: " &
      Natural'Image (Integer (Result_Loop)));
    Put_Line
     ("GCD of " & Natural'Image (Integer (A)) & " and " &
      Natural'Image (Integer (B)) & " using recursion: " &
      Natural'Image (Integer (Result_Rec)));
  end;

  -- Testing Diophantine functions
  Put_Line ("Testing Diophantine functions...");
  declare
    A           : Integer                := 35;
    B           : Integer                := 10;
    C           : Integer                := 55;
    Result_Loop : Wrapper.Diofant_Result :=
     Wrapper.Diophantine_Loop
      (Interfaces.C.int (A), Interfaces.C.int (B), Interfaces.C.int (C));
    Result_Rec  : Wrapper.Diofant_Result :=
     Wrapper.Diophantine_Rec
      (Interfaces.C.int (A), Interfaces.C.int (B), Interfaces.C.int (C));
  begin
    Put_Line
     ("Diophantine equation " & Integer'Image (A) & "*x +" &
      Integer'Image (B) & "*y =" & Integer'Image (C) & " using loop:");
    Put_Line
     ("x = " & Integer'Image (Integer (Result_Loop.x)) & ", y = " &
      Integer'Image (Integer (Result_Loop.y)));
    Put_Line
     ("Diophantine equation " & Integer'Image (A) & "*x +" &
      Integer'Image (B) & "*y =" & Integer'Image (C) & " using recursion:");
    Put_Line
     ("x = " & Integer'Image (Integer (Result_Rec.x)) & ", y = " &
      Integer'Image (Integer (Result_Rec.y)));
  end;
end Ex_5;
