// GF.cpp

#include "GF.h"

GF::GF() : value(0) {}

GF::GF(long value) : value((value % PRIME_NUMBER + PRIME_NUMBER) % PRIME_NUMBER) {}

long GF::characteristic() {
    return PRIME_NUMBER;
}

long GF::getValue() {
    return value;
}

bool GF::operator ==(const GF& other) {
    return value == other.value;
}

bool GF::operator !=(const GF& other) {
    return !(*this == other);
}

bool GF::operator <=(const GF& other) {
    return value <= other.value;
}

bool GF::operator >=(const GF& other) {
    return value >= other.value;
}

bool GF::operator <(const GF& other) {
    return value < other.value;
}

bool GF::operator >(const GF& other) {
    return value > other.value;
}

void GF::operator +=(const GF& other) {
    value = (value + other.value) % PRIME_NUMBER;
}

void GF::operator -=(const GF& other) {
    value = (value - other.value + PRIME_NUMBER) % PRIME_NUMBER;
}

void GF::operator *=(const GF& other) {
    value = (value * other.value) % PRIME_NUMBER;
}

void GF::operator /=(const GF& other) {
    if (other.value == 0)
        throw std::invalid_argument("Division by zero");
    *this *= other.inverse();
}

GF GF::inverse() const {
    if (value == 0)
        throw std::invalid_argument("Inverse of zero does not exist");

    long long int base = value;
    long long int exponent = PRIME_NUMBER - 2;
    long long int result = 1;
    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result = (result * base) % PRIME_NUMBER;
        }
        base = (base * base) % PRIME_NUMBER;
        exponent /= 2;
    }
    return GF(static_cast<int>(result));
}


GF operator +(const GF& l, const GF& r) {
    GF result = l;
    result += r;
    return result;
}

GF operator -(const GF& l, const GF& r) {
    GF result = l;
    result -= r;
    return result;
}

GF operator *(const GF& l, const GF& r) {
    GF result = l;
    result *= r;
    return result;
}

GF operator /(const GF& l, const GF& r) {
    GF result = l;
    result /= r;
    return result;
}

std::ostream& operator <<(std::ostream& os, const GF& gf) {
    os << gf.value;
    return os;
}

std::istream& operator >>(std::istream& is, GF& gf) {
    long temp;
    is >> temp;
    gf = GF(temp);
    return is;
}
