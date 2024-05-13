// User.cpp

#ifndef USER_CPP
#define USER_CPP

#include <stdexcept>
#include "DHSetup.cpp"
#include "GF.h"

template <typename T>
class User {
private:
    DHSetup<T> dh_setup;
    long secret = -1;
    GF key;

public:
    User(DHSetup<T> dh_setup);

    GF get_public_key();

    void set_key(GF a);

    GF encrypt(GF m);

    GF decrypt(GF c);
};

template <typename T>
User<T>::User(DHSetup<T> dh_setup) : dh_setup(dh_setup) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(1, key.characteristic() - 1);

    secret = dis(gen);
}

template <typename T>
GF User<T>::get_public_key() {
    return dh_setup.power(dh_setup.get_generator(), secret);
}

template <typename T>
void User<T>::set_key(GF a) {
    if (secret == -1) throw std::invalid_argument("Secret not initialized");
    key = dh_setup.power(a, secret);
}

template <typename T>
GF User<T>::encrypt(GF m) {
    if (key.getValue() == -1) throw std::invalid_argument("Key not set");
    return m * key;
}

template <typename T>
GF User<T>::decrypt(GF c) {
    if (key.getValue() == -1) throw std::invalid_argument("Key not set");
    return c / key;
}

#endif //USER_CPP