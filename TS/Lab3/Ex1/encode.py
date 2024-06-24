from bit_framing import encode


def main() -> None:
    with open("data/input.txt", "r") as input_file:
        input_bits = input_file.read()

    with open("data/encoded.txt", "w") as encoded_file:
        encoded_bits = encode(input_bits)
        encoded_file.write(encoded_bits)

    print("Encoding complete")


if __name__ == "__main__":
    main()
