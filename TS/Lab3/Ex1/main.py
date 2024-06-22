from bit_framing import encode, decode


def main() -> None:

    with open("data/input.txt", "r") as input_file:
        input_bits = input_file.read()
        # print(f"Input bits:\n{input_bits}\n")

    with open("data/encoded.txt", "w") as encoded_file:
        encoded_bits = encode(input_bits)
        # print(f"Encoded bits:\n{encoded_bits}\n")
        encoded_file.write(encoded_bits)

    with open("data/decoded.txt", "w") as decoded_file:
        decoded_bits, frame_len, successful_frames = decode(encoded_bits)
        # print(f"Decoded bits:\n{decoded_bits}\n")
        decoded_file.write(decoded_bits)

    print(f"{successful_frames}/{frame_len}")
    if input_bits == decoded_bits:
        print("The bits were successfully decoded!")


if __name__ == "__main__":
    main()
