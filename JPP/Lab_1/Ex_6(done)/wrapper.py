import ctypes


class DiofantResult(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]


# Wczytanie biblioteki C
lib = ctypes.CDLL("./functions.so")

# Definicja sygnatury funkcji factorial_loop
lib.factorial_loop.argtypes = [ctypes.c_int]
lib.factorial_loop.restype = ctypes.c_ulonglong

# Definicja sygnatury funkcji factorial_rec
lib.factorial_rec.argtypes = [ctypes.c_int]
lib.factorial_rec.restype = ctypes.c_ulonglong

# Definicja sygnatury funkcji gcd_loop
lib.gcd_loop.argtypes = [ctypes.c_int, ctypes.c_int]
lib.gcd_loop.restype = ctypes.c_int

lib.gcd_rec.argtypes = [ctypes.c_int, ctypes.c_int]
lib.gcd_rec.restype = ctypes.c_int

lib.diofant_loop.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.diofant_loop.restype = DiofantResult

lib.diofant_rec.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.diofant_rec.restype = DiofantResult


class DiofantResult(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]


if __name__ == "__main__":
    n = 5
    print(f"5! (loop) = {lib.factorial_loop(n)}")
    print(f"5! (rec) = {lib.factorial_rec(n)}")

    a = 35
    b = 10
    print(f"gcd({a}, {b}) (loop) = {lib.gcd_loop(a, b)}")
    print(f"gcd({a}, {b}) (rec) = {lib.gcd_rec(a, b)}")

    c = 55
    result = lib.diofant_loop(a, b, c)
    print(f"x (loop) = {result.x}, y (loop) = {result.y}")
    result = lib.diofant_rec(a, b, c)
    print(f"x (rec) = {result.x}, y (rec) = {result.y}")
