// main.cpp

#include <iostream>
#include "DHSetup.cpp"
#include "User.cpp"
#include "GF.h"

int main() {
    DHSetup<GF> dh_setup = DHSetup<GF>();

    User<GF> alice(dh_setup);
    User<GF> bob(dh_setup);
    GF message;

    std::cout << "prime: " << message.characteristic() << std::endl;
    std::cout << "generator: " << dh_setup.get_generator() << std::endl;

    std::cout << "Alice's public key: " << alice.get_public_key() << std::endl;
    std::cout << "Bob's public key: " << bob.get_public_key() << std::endl;

    alice.set_key(bob.get_public_key());
    bob.set_key(alice.get_public_key());

    message = GF(12345);

    GF encrypted = alice.encrypt(message);
    std::cout << "Encrypted message: " << encrypted << std::endl;

    GF decrypted = bob.decrypt(encrypted);
    std::cout << "Decrypted message: " << decrypted << std::endl;

    return 0;
}
