# User.py

import random
from GF import GF

class User:
    
    secret = -1

    def __init__(self, dh_setup):
        self.dh_setup = dh_setup
        self.secret = random.randint(1, GF.PRIME_NUMBER)
        self.key = None

    def get_public_key(self):
        return self.dh_setup.power(self.dh_setup.get_generator(), self.secret)

    def set_key(self, a):
        if self.secret == -1:
            raise ValueError("Secret not initialized")
        self.key = self.dh_setup.power(a, self.secret)

    def encrypt(self, m):
        if self.key is None:
            raise ValueError("Key not set")
        return m * self.key

    def decrypt(self, c):
        if self.key is None:
            raise ValueError("Key not set")
        return c / self.key
