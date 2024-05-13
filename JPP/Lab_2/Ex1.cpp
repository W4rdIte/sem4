#include <iostream>
#include <stdexcept>

class GF1234577
{
private:
    int value;
    static const int characteristic = 1234577;

public:
    GF1234577(int val = 0) : value(val % characteristic)
    {
        if (value < 0)
        {
            value += characteristic;
        }
    }

    int getCharacteristic() const
    {
        return characteristic;
    }

    GF1234577 operator+(const GF1234577 &other) const
    {
        return GF1234577((value + other.value) % characteristic);
    }

    GF1234577 &operator+=(const GF1234577 &other)
    {
        value = (value + other.value) % characteristic;
        return *this;
    }

    GF1234577 operator-(const GF1234577 &other) const
    {
        return GF1234577((value - other.value + characteristic) % characteristic);
    }

    GF1234577 &operator-=(const GF1234577 &other)
    {
        value = (value - other.value + characteristic) % characteristic;
        return *this;
    }

    GF1234577 operator*(const GF1234577 &other) const
    {
        return GF1234577((1LL * value * other.value) % characteristic);
    }

    GF1234577 &operator*=(const GF1234577 &other)
    {
        value = (1LL * value * other.value) % characteristic;
        return *this;
    }

    GF1234577 operator/(const GF1234577 &other) const
    {
        if (other.value == 0)
        {
            throw std::invalid_argument("Division by zero");
        }

        int inverse = 1;
        int base = other.value;
        int exponent = characteristic - 2;
        while (exponent > 0)
        {
            if (exponent % 2 == 1)
            {
                inverse = (1LL * inverse * base) % characteristic;
            }   
            base = (1LL * base * base) % characteristic;
            exponent /= 2;
        }
        return GF1234577((1LL * value * inverse) % characteristic);
    }

    GF1234577 &operator/=(const GF1234577 &other)
    {
        *this = *this / other;
        return *this;
    }

    bool operator==(const GF1234577 &other) const
    {
        return value == other.value;
    }

    bool operator!=(const GF1234577 &other) const
    {
        return !(*this == other);
    }

    bool operator<(const GF1234577 &other) const
    {
        return value < other.value;
    }

    bool operator<=(const GF1234577 &other) const
    {
        return value <= other.value;
    }

    bool operator>(const GF1234577 &other) const
    {
        return value > other.value;
    }

    bool operator>=(const GF1234577 &other) const
    {
        return value >= other.value;
    }

    friend std::ostream &operator<<(std::ostream &os, const GF1234577 &num)
    {
        os << num.value;
        return os;
    }

    friend std::istream &operator>>(std::istream &is, GF1234577 &num)
    {
        int val;
        is >> val;
        num = GF1234577(val);
        return is;
    }
};

int main()
{
    // Testowanie klasy GF1234577
    GF1234577 a = 123;
    GF1234577 b = 23;
    GF1234577 c;

    // Operacje arytmetyczne
    c = a + b;
    std::cout << "a + b = " << c << std::endl;
    c = a - b;
    std::cout << "a - b = " << c << std::endl;
    c = a * b;
    std::cout << "a * b = " << c << std::endl;
    c = a / b;
    std::cout << "a / b = " << c << std::endl;

    // Operatory porównania
    std::cout << "a == b : " << (a == b) << std::endl;
    std::cout << "a != b : " << (a != b) << std::endl;
    std::cout << "a < b : " << (a < b) << std::endl;
    std::cout << "a <= b : " << (a <= b) << std::endl;
    std::cout << "a > b : " << (a > b) << std::endl;
    std::cout << "a >= b : " << (a >= b) << std::endl;

    // Wczytywanie i wypisywanie
    std::cout << "Enter a value for c: ";
    std::cin >> c;
    std::cout << "c = " << c << std::endl;

    return 0;
}
