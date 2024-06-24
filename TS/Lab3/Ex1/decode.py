from bit_framing import decode


def main() -> None:
    with open("data/encoded.txt", "r") as encoded_file:
        encoded_bits = encoded_file.read()

    with open("data/decoded.txt", "w") as decoded_file:
        decoded_bits, frame_len, successful_frames = decode(encoded_bits)
        decoded_file.write(decoded_bits)

    print(f"{successful_frames}/{frame_len}")


if __name__ == "__main__":
    main()
