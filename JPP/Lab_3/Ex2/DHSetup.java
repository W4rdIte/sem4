// DHSetup.cpp

import java.util.Random;
import java.util.function.Function;

import java.util.ArrayList;
import java.util.List;

class DHSetup<T extends GF> {
    private final T generator;

    public DHSetup(Function<Long, T> constructor) {
        Random random = new Random();
        long generatorValue;
        do {
            generatorValue = random.nextInt(GF.characteristic())+1;
        } while (!isGenerator(generatorValue));
        this.generator = constructor.apply(generatorValue);
    }

    private boolean isGenerator(long candidate) {
        T temp = (T) new GF(candidate);
        for (long q = 2; q * q <= T.characteristic() - 1; q++) {
            if (isPrime(q) && (T.characteristic()-1) % q == 0 ) {
                long exp = (T.characteristic() - 1) / q;
                T result = power(temp, exp);
                T one = (T) new GF(1);
                if (result == one) {
                    return false;
                }
            }
        }
        return true;
    }

    private static boolean isPrime(long number) {
        if (number <= 1) {
            return false;
        }
        for (long i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public T getGenerator() {
        return generator;
    }

    public T power(T a, long b) {
        T result = a;
        if (b == 0) {
            return result;
        }
        if (b == 1) {
            result = a;
            return result;
        }
        if (b % 2 == 0) {
            T temp = (T) power(a, b / 2);
            return (T) T.multiply(temp, temp);
        }
        if (b % 2 == 1) {
            T temp = power(a, (b - 1) / 2);
            return (T) T.multiply(T.multiply(temp, temp), a);
        }
        return result;
    }
}
