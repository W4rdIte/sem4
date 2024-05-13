#ifndef WRAP_H
#define WRAP_H

extern int Factorial_C(int N);
extern int GCD_C(int A, int B);
extern void Solve_Diophantine_C(int A, int B, int C, int* X, int* Y, int* GCD);

struct EquationSolution {
    int x;
    int y;
    int gcd;
};

int My_Factorial(int n);
int My_GCD(int a, int b);
struct EquationSolution solveDiophantine(int a, int b, int c);

#endif // WRAP_H