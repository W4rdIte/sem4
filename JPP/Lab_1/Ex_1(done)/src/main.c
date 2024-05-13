#include <stdio.h>
#include "functions.h"

int main()
{
    //! Factorial test
    int n = 5;
    printf("5! (loop) = %llu\n", factorial_loop(n));
    printf("5! (rec) = %llu\n", factorial_rec(n));

    //! GCD test
    int a = 35;
    int b = 10;
    printf("gcd(%d, %d) (loop) = %d\n", a, b, gcd_loop(a, b));
    printf("gcd(%d, %d) (rec) = %d\n", a, b, gcd_rec(a, b));

    //! Diofant test
    int c = 55;
    DiofantResult result;
    result = diofant_loop(a, b, c);
    printf("x (loop) = %d, y (loop) = %d\n", result.x, result.y);
    result = diofant_rec(a, b, c);
    printf("x (rec) = %d, y (rec) = %d\n", result.x, result.y);

    return 0;
}
