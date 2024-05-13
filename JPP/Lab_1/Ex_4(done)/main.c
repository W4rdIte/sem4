#include "wrap.h"
#include <stdio.h>
/*  
    gcc -c wrap.c main.c
    gnatmake functions.adb
    gcc -o run functions.o wrap.o main.o -lgnat
*/
int main() {
    int a=35, b=10, c=55, n=5;
    printf("Factorial of %d: %d\n", n, My_Factorial(n));
    printf("GCD of %d and %d: %d\n", a, b, My_GCD(a, b));
    struct EquationSolution solution = solveDiophantine(a, b, c);
    printf("Solution to the Diophantine equation %dx + %dy = %d: x = %d, y = %d\n", a, b, c, solution.x, solution.y);
    return 0;
}