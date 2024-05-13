#include "wrap.h"

int My_Factorial(int n)
{
    return Factorial_C(n);
}

int My_GCD(int a, int b)
{
    return GCD_C(a, b);
}

struct EquationSolution solveDiophantine(int a, int b, int c)
{
    int x = 0;
    int y = 0;
    unsigned int gcd = 0;
    Solve_Diophantine_C(a, b, c, &x, &y, &gcd);
    struct EquationSolution result = {x, y, gcd};
    return result;
}