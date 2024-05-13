//DHSetup.cpp

#ifndef DHSETUP_CPP
#define DHSETUP_CPP

#include <random>
#include "GF.h"

template <typename T>
class DHSetup {
private:
    GF generator;

    bool is_prime(long number);

    bool is_generator(long candidate);

public:
    DHSetup();

    GF get_generator();

    GF power(GF a, int b);
};

template <typename T>
DHSetup<T>::DHSetup() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(1, generator.characteristic() - 1);

    long generator_value = dis(gen);
    do {
        generator_value = dis(gen);
    } while (!is_generator(generator_value));
    generator = GF(generator_value);
}

template <typename T>
bool DHSetup<T>::is_prime(long number) {
    if (number <= 1) return false;
    for (int i = 2; i * i <= number; i++) {
        if (number % i == 0) return false;
    }
    return true;
}

template <typename T>
bool DHSetup<T>::is_generator(long candidate) {
    GF temp = GF(candidate);
    for (long q = 2; q*q <= generator.characteristic() - 1; q++) {
        if (is_prime(q) && (generator.characteristic() - 1) % q == 0) {
            long exp = (generator.characteristic() - 1) / q;
            GF result = power(temp, exp);
            GF one(1);
            if (result == one) return false;
        }
    }
    return true;
}

template <typename T>
GF DHSetup<T>::get_generator() {
    return generator;
}

template <typename T>
GF DHSetup<T>::power(GF a, int b) {
    GF result(1);
    if (b == 0) return result;
    if (b == 1) return a;
    if (b % 2 == 0) {
        GF temp = power(a, b / 2);
        return temp * temp;
    }
    if (b % 2 == 1) {
        GF temp = power(a, (b - 1) / 2);
        return temp * temp * a;
    }
    return result;
}

#endif //DHSETUP_CPP