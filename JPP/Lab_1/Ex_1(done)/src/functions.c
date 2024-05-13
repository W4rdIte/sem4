#include "functions.h"

unsigned long long factorial_loop(int n)
{
    unsigned long long result = 1;
    for (int i = 1; i <= n; ++i)
    {
        result *= i;
    }
    return result;
}

unsigned long long factorial_rec(int n)
{
    if (n == 0)
        return 1;
    else
        return n * factorial_rec(n - 1);
}

int gcd_loop(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int gcd_rec(int a, int b)
{
    if (b == 0)
        return a;
    else
        return gcd_rec(b, a % b);
}

DiofantResult diofant_loop(int a, int b, int c)
{
    DiofantResult result;
    int x = 0, y = 0;
    while (1)
    {
        if (a * x + b * y == c)
        {
            result.x = x;
            result.y = y;
            return result;
        }
        if (a * x + b * y > c)
            break;
        x++;
        y = (c - a * x) / b;
    }
    result.x = -1;
    result.y = -1;
    return result;
}

DiofantResult diofant_rec(int a, int b, int c)
{
    DiofantResult result;
    /* if (a == 0 && b == 0)
    {
        result.x = -1;
        result.y = -1;
        return result;
    }*/
    if (c % gcd_rec(a, b) != 0)
    {
        result.x = -1;
        result.y = -1;
        return result;
    }
    if (b == 0)
    {
        result.x = c / a;
        result.y = 0;
        return result;
    }
    DiofantResult temp = diofant_rec(b, a % b, c);
    result.x = temp.y;
    result.y = temp.x - (a / b) * temp.y;
    return result;
}