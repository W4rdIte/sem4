# DHSetup.py

import random
from GF import GF

class DHSetup:
    prime = GF.PRIME_NUMBER

    def __init__(self):
        random.seed()
        generator_value = 0
        while True:
            generator_value = random.randint(1, self.prime)
            if self.__is_generator(generator_value):
                break
        self.generator = GF(generator_value)

    def __is_generator(self, candidate):
        temp = GF(candidate)
        for q in range(2, int(self.prime ** 0.5) + 1):
            if self.__is_prime(q) and (self.prime - 1) % q == 0:
                exp = (self.prime - 1) // q
                result = self.power(temp, exp)
                one = GF(1)
                if result == one:
                    return False
        return True

    @staticmethod
    def __is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def get_generator(self):
        return self.generator

    @staticmethod
    def power(a, b):
        result = GF(1)
        if b == 0:
            return result
        if b == 1:
            result = a
            return result
        if b % 2 == 0:
            temp = DHSetup.power(a, b // 2)
            return temp * temp
        if b % 2 == 1:
            temp = DHSetup.power(a, (b - 1) // 2)
            return temp * temp * a
