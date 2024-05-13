from functions import (
    factorial_loop,
    factorial_recursive,
    gcd_loop,
    gcd_recursive,
    diophantine_loop,
    diophantine_recursive,
)


def test_factorial():
    n = 5
    print(f"Factorial of {n} (loop): {factorial_loop(n)}")
    print(f"Factorial of {n} (recursive): {factorial_recursive(n)}")


def test_gcd():
    a, b = 15, 12
    print(f"GCD of {a} and {b} (loop): {gcd_loop(a, b)}")
    print(f"GCD of {a} and {b} (recursive): {gcd_recursive(a, b)}")


def test_diophantine_equation():
    a, b, c = 35, 10, 55
    print(f"Solving {a}x + {b}y = {c} (loop): {diophantine_loop(a, b, c)}")
    print(f"Solving {a}x + {b}y = {c} (recursive): {diophantine_recursive(a, b, c)}")


if __name__ == "__main__":
    print("Testing factorial functions:")
    test_factorial()
    print("\nTesting GCD functions:")
    test_gcd()
    print("\nTesting Diophantine equation function:")
    test_diophantine_equation()
