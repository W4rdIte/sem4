// User.java

import java.util.Random;

public class User<T extends GF> {

    private DHSetup<T> dhSetup;
    
    private T key;
    
    private long secret = -1;

    public User(DHSetup<T> dhSetup) {
        this.dhSetup = dhSetup;
        Random random = new Random();
        secret = random.nextInt(GF.characteristic()) + 1;
    }

    public T getPublicKey() {
        return dhSetup.power(dhSetup.getGenerator(), secret);
    }

    public void setKey(T a) {
        if (secret == -1) {
            throw new IllegalStateException("Secret not initialized");
        }
        this.key = dhSetup.power(a, secret);
    }

    public T encrypt(T m) {
        if (key == null) {
            throw new IllegalStateException("Key not set");
        }
        return (T) T.multiply(m, key);
    }

    public T decrypt(T c) {
        if (key == null) {
            throw new IllegalStateException("Key not set");
        }
        return (T) T.divide(c, key);
    }
}
