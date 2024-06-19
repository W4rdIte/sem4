import random

# Banki i ich numery rozliczeniowe
BANK_IDENTIFIERS = {
    "NBP": "10100000",
    "PKO BP": "10200003",
    "ING": "10500002",
    "mBank": "11400000",
    "Pekao SA": "12400001",
}


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
        return self.encrypt(ciphertext)  # RC4 jest symetryczny


def generate_bank_account(bank_code):
    """Generuje losowy numer konta bankowego zgodny z formatem IBAN."""
    account_number = f"{bank_code}{''.join(random.choices('0123456789', k=16))}"
    return account_number


def generate_control_number(account_number):
    """Generuje sumę kontrolną dla numeru konta bankowego."""
    rearranged_number = account_number + "2521"  # "PL" jako liczby
    check_sum = 98 - (int(rearranged_number) % 97)
    return f"{check_sum:02d}"


def format_iban(control_number, bank_code, account_number):
    """Formatuje pełny numer IBAN."""
    return f"{control_number}{bank_code}{account_number}"


def xor_bytes(a, b):
    """XOR dla dwóch ciągów bajtów."""
    return bytes(x ^ y for x, y in zip(a, b))


def analyze_xor(ciphertexts):
    """Analizuje XORy kryptogramów w celu odgadnięcia tekstów jawnych."""
    n = len(ciphertexts)
    for i in range(n):
        for j in range(i + 1, n):
            xor_result = xor_bytes(ciphertexts[i], ciphertexts[j])
            print(f"XOR kryptogramów {i} i {j}: {xor_result}")


def main():
    key = b"SecretKey"
    rc4 = RC4(key)

    num_accounts = 5
    bank_names = list(BANK_IDENTIFIERS.keys())

    plaintext_accounts = []
    ciphertext_accounts = []

    # Generowanie numerów kont, ich IBANów i szyfrowanie
    for _ in range(num_accounts):
        bank_name = random.choice(bank_names)
        bank_code = BANK_IDENTIFIERS[bank_name]
        account_number = generate_bank_account(bank_code)
        control_number = generate_control_number(account_number)
        iban = format_iban(control_number, bank_code, account_number)
        ciphertext = rc4.encrypt(iban)

        plaintext_accounts.append(iban)
        ciphertext_accounts.append(ciphertext)
        print(f"Bank: {bank_name}, Numer konta: {iban}, Szyfrogram: {ciphertext}")

    # Analiza XORów kryptogramów
    analyze_xor(ciphertext_accounts)


if __name__ == "__main__":
    main()
