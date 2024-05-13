// GF.java

public class GF {
    private static final int PRIME_NUMBER = 1234567891;
    private long value;

    public GF() {
        this.value = 0;
    }

    public GF(long value) {
        this.value = (value % PRIME_NUMBER + PRIME_NUMBER) % PRIME_NUMBER;
    }

    public static int characteristic() {
        return PRIME_NUMBER;
    }

    public boolean equals(GF other) {
        return this.value == other.value;
    }

    public boolean notEquals(GF other) {
        return !this.equals(other);
    }

    public boolean lessThanOrEqual(GF other) {
        return this.value <= other.value;
    }

    public boolean greaterThanOrEqual(GF other) {
        return this.value >= other.value;
    }

    public boolean lessThan(GF other) {
        return this.value < other.value;
    }

    public boolean greaterThan(GF other) {
        return this.value > other.value;
    }

    public void add(GF other) {
        this.value = (this.value + other.value) % PRIME_NUMBER;
    }

    public void subtract(GF other) {
        this.value = (this.value - other.value + PRIME_NUMBER) % PRIME_NUMBER;
    }

    public void multiply(GF other) {
        this.value = (this.value * other.value) % PRIME_NUMBER;
    }

    public void divide(GF other) {
        if (other.value == 0)
            throw new IllegalArgumentException("Division by zero");
        this.multiply(other.inverse());
    }

    public GF inverse() {
        if (value == 0)
            throw new IllegalArgumentException("Inverse of zero does not exist");

        long base = value;
        long exponent = PRIME_NUMBER - 2;
        long result = 1;
        while (exponent > 0) {
            if (exponent % 2 == 1) {
                result = (result * base) % PRIME_NUMBER;
            }
            base = (base * base) % PRIME_NUMBER;
            exponent /= 2;
        }
        return new GF((long) result);
    }

    public static GF add(GF l, GF r) {
        GF result = new GF(l.value);
        result.add(r);
        return result;
    }

    public static GF subtract(GF l, GF r) {
        GF result = new GF(l.value);
        result.subtract(r);
        return result;
    }

    public static GF multiply(GF l, GF r) {
        GF result = new GF(l.value);
        result.multiply(r);
        return result;
    }

    public static GF divide(GF l, GF r) {
        GF result = new GF(l.value);
        result.divide(r);
        return result;
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }

    public static GF parseGF(String input) {
        long longValue = Long.parseLong(input);
        return new GF(longValue);
    }
}
