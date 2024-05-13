# GF.py

class GF:
    PRIME_NUMBER = 1234567891

    def __init__(self, value=0):
        self.value = (value % self.PRIME_NUMBER + self.PRIME_NUMBER) % self.PRIME_NUMBER

    @staticmethod
    def characteristic(self):
        return self.PRIME_NUMBER

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __add__(self, other):
        return GF((self.value + other.value) % self.PRIME_NUMBER)

    def __sub__(self, other):
        return GF((self.value - other.value + self.PRIME_NUMBER) % self.PRIME_NUMBER)

    def __mul__(self, other):
        return GF((self.value * other.value) % self.PRIME_NUMBER)

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Division by zero")
        return self * other.inverse()

    def __iadd__(self, other):
        self.value = (self.value + other.value) % self.PRIME_NUMBER
        return self

    def __isub__(self, other):
        self.value = (self.value - other.value + self.PRIME_NUMBER) % self.PRIME_NUMBER
        return self

    def __imul__(self, other):
        self.value = (self.value * other.value) % self.PRIME_NUMBER
        return self

    def __itruediv__(self, other):
        if other.value == 0:
            raise ValueError("Division by zero")
        self *= other.inverse()
        return self

    def inverse(self):
        if self.value == 0:
            raise ValueError("Inverse of zero does not exist")

        base = self.value
        exponent = self.PRIME_NUMBER - 2
        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % self.PRIME_NUMBER
            base = (base * base) % self.PRIME_NUMBER
            exponent //= 2
        return GF(result)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"GF({self.value})"

    @staticmethod
    def from_input(value):
        return GF(value)
