class GF1234577:
    characteristic = 1234577

    def __init__(self, val=0):
        self.value = val % self.characteristic
        if self.value < 0:
            self.value += self.characteristic

    def __add__(self, other):
        return GF1234577((self.value + other.value) % self.characteristic)

    def __sub__(self, other):
        return GF1234577(
            (self.value - other.value + self.characteristic) % self.characteristic
        )

    def __mul__(self, other):
        return GF1234577((self.value * other.value) % self.characteristic)

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Division by zero")

        inverse = 1
        base = other.value
        exponent = self.characteristic - 2
        while exponent > 0:
            if exponent % 2 == 1:
                inverse = (inverse * base) % self.characteristic
            base = (base * base) % self.characteristic
            exponent //= 2
        return GF1234577((self.value * inverse) % self.characteristic)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":

    a = GF1234577(123)
    b = GF1234577(23)

    c = a + b
    print("a + b =", c)
    c = a - b
    print("a - b =", c)
    c = a * b
    print("a * b =", c)
    c = a / b
    print("a / b =", c)

    print("a == b :", a == b)
    print("a != b :", a != b)
    print("a < b :", a < b)
    print("a <= b :", a <= b)
    print("a > b :", a > b)
    print("a >= b :", a >= b)

    c = GF1234577(int(input("Enter a value for c: ")))
    print("c =", c)
