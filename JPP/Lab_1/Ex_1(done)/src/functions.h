#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <stdio.h>

typedef struct
{
    int x;
    int y;
} DiofantResult;

unsigned long long factorial_loop(int n);
unsigned long long factorial_rec(int n);
int gcd_loop(int a, int b);
int gcd_rec(int a, int b);
DiofantResult diofant_loop(int a, int b, int c);
DiofantResult diofant_rec(int a, int b, int c);

#endif /* FUNCTIONS_H */
