#ifndef EX_7
#define EX_7

#include <Python.h>

typedef struct {
    int x;
    int y;
    int gcd;
} EquationSolution;

long long wrapped_factorial(unsigned n);

unsigned wrapped_gcd(unsigned a, unsigned b);

EquationSolution wrapped_diophantine(int a, int b, int c);

#endif 