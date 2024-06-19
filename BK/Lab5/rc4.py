class RC4:
    def __init__(self, key):
        self.key = key
        self.S = self.KSA()

    def KSA(self):
        key_length = len(self.key)
        S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + S[i] + self.key[i % key_length]) % 256
            S[i], S[j] = S[j], S[i]
        return S

    def PRGA(self):
        S = self.S[:]
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            K = S[(S[i] + S[j]) % 256]
            yield K

    def encrypt(self, plaintext):
        keystream = self.PRGA()
        if isinstance(plaintext, str):
            plaintext = plaintext.encode("ascii")
        return bytes([c ^ next(keystream) for c in plaintext])

    def decrypt(self, ciphertext):
        return self.encrypt(ciphertext)


def test_rc4():
    key1 = b"Key1"
    key2 = b"Key2"
    plaintexts = ["Test"]  # teksty jawne

    rc4_key1 = RC4(key1)
    rc4_key2 = RC4(key2)

    print("Testing RC4 with different keys...")
    for plaintext in plaintexts:
        ciphertext1 = rc4_key1.encrypt(plaintext)  # szyfrogram
        decrypted1 = rc4_key1.decrypt(ciphertext1)

        ciphertext2 = rc4_key2.encrypt(plaintext)
        decrypted2 = rc4_key2.decrypt(ciphertext2)

        print(f"Plaintext: {plaintext}")
        print(f"Ciphertext with Key1: {ciphertext1}")
        print(f"Decrypted with Key1: {decrypted1.decode('ascii')}")
        print(f"Ciphertext with Key2: {ciphertext2}")
        print(f"Decrypted with Key2: {decrypted2.decode('ascii')}")
        print()


if __name__ == "__main__":
    test_rc4()
