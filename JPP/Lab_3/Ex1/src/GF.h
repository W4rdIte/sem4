// GF.h

#ifndef GF_H
#define GF_H

#include <iostream>
#include <stdexcept>

const long PRIME_NUMBER = 1234567891;

class GF {
private:
    long value;

public:
    GF();
    GF(long value);

    long characteristic();

    long getValue();

    bool operator ==(const GF& other);

    bool operator !=(const GF& other);

    bool operator <=(const GF& other);

    bool operator >=(const GF& other);

    bool operator <(const GF& other);

    bool operator >(const GF& other);

    void operator +=(const GF& other);

    void operator -=(const GF& other);

    void operator *=(const GF& other);

    void operator /=(const GF& other);

    GF inverse() const;

    friend GF operator +(const GF& l, const GF& r);

    friend GF operator -(const GF& l, const GF& r);

    friend GF operator *(const GF& l, const GF& r);

    friend GF operator /(const GF& l, const GF& r);

    friend std::ostream& operator <<(std::ostream& os, const GF& gf);

    friend std::istream& operator >>(std::istream& is, GF& gf);
};

#endif // GF_H
