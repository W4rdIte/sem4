import java.util.Scanner;

public class GF1234577 {
    private int value;
    private static final int characteristic = 1234577;

    public GF1234577(int val) {
        value = val % characteristic;
        if (value < 0) {
            value += characteristic;
        }
    }

    public int getCharacteristic() {
        return characteristic;
    }

    public GF1234577 add(GF1234577 other) {
        return new GF1234577((value + other.value) % characteristic);
    }

    public GF1234577 subtract(GF1234577 other) {
        return new GF1234577((value - other.value + characteristic) % characteristic);
    }

    public GF1234577 multiply(GF1234577 other) {
        return new GF1234577((int) ((1L * value * other.value) % characteristic));
    }

    public GF1234577 divide(GF1234577 other) {
        if (other.value == 0) {
            throw new IllegalArgumentException("Division by zero");
        }

        int inverse = 1;
        int base = other.value;
        int exponent = characteristic - 2;
        while (exponent > 0) {
            if (exponent % 2 == 1) {
                inverse = (int) ((1L * inverse * base) % characteristic);
            }
            base = (int) ((1L * base * base) % characteristic);
            exponent /= 2;
        }
        return new GF1234577((int) ((1L * value * inverse) % characteristic));
    }

    public boolean equals(GF1234577 other) {
        return value == other.value;
    }

    public boolean lessThan(GF1234577 other) {
        return value < other.value;
    }

    public String toString() {
        return Integer.toString(value);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        GF1234577 a = new GF1234577(123);
        GF1234577 b = new GF1234577(23);
        GF1234577 c;

        c = a.add(b);
        System.out.println("a + b = " + c);
        c = a.subtract(b);
        System.out.println("a - b = " + c);
        c = a.multiply(b);
        System.out.println("a * b = " + c);
        c = a.divide(b);
        System.out.println("a / b = " + c);

        // Operatory porównania
        System.out.println("a == b : " + a.equals(b));
        System.out.println("a != b : " + !a.equals(b));
        System.out.println("a < b : " + a.lessThan(b));
        System.out.println("a <= b : " + (a.lessThan(b) || a.equals(b)));
        System.out.println("a > b : " + (!a.lessThan(b) && !a.equals(b)));
        System.out.println("a >= b : " + (!a.lessThan(b)));

        // Wczytywanie i wypisywanie
        System.out.print("Enter a value for c: ");
        c = new GF1234577(scanner.nextInt());
        System.out.println("c = " + c);
        scanner.close();
    }
}
