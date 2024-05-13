#include <stdio.h>
#include "wrapper.h"

int main()
{

    int n = 5;
    printf("Factorial of %u is %lld\n", n, wrapped_factorial(n));

    int a = 35, b = 10;
    printf("GCD of %u and %u is %u\n", a, b, wrapped_gcd(a, b));

    int c = 55;
    EquationSolution result = wrapped_diophantine(a, b, c);
    printf("Solution to the equation %dx + %dy = %d is x = %d, y = %d\n", a, b, c, result.x, result.y);

    return 0;
}