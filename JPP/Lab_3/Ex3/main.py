# Main.py

from DHSetup import DHSetup
from User import User
from GF import GF

if __name__ == "__main__":
    dh_setup = DHSetup()

    alice = User(dh_setup)
    bob = User(dh_setup)

    print("prime:", dh_setup.prime)
    print("generator:", dh_setup.get_generator())

    print("Alice's public key:", alice.get_public_key())
    print("Bob's public key:", bob.get_public_key())

    alice.set_key(bob.get_public_key())
    bob.set_key(alice.get_public_key())

    message = GF(12345)

    encrypted = alice.encrypt(message)
    print("Encrypted message:", encrypted)

    decrypted = bob.decrypt(encrypted)
    print("Decrypted message:", decrypted)
