def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def gcd_loop(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def diophantine_loop(a, b, c):
    if a == 0 and b == 0:
        return None

    def gcd_loop(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd = gcd_loop(a, b)

    if c % gcd != 0:
        return None

    x, y = 0, 0
    while True:
        if (c - a * x) % b == 0:
            y = (c - a * x) // b
            break
        x += 1

    return (x, y)


def diophantine_recursive(a, b, c):
    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            d, x, y = extended_gcd(b, a % b)
            return (d, y, x - (a // b) * y)

    gcd, x, y = extended_gcd(a, b)
    if c % gcd != 0:
        return None
    else:
        x *= c // gcd
        y *= c // gcd
        return (x, y)
