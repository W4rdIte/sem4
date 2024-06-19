import zlib


def bit_unstuffing(data):
    count = 0
    unstuffed = ""
    i = 0
    while i < len(data):
        bit = data[i]
        if bit == "1":
            count += 1
        else:
            count = 0
        unstuffed += bit
        if count == 5:
            if i + 1 < len(data) and data[i + 1] == "0":
                i += 1
            count = 0
        i += 1
    return unstuffed


def verify_crc(data, crc):
    computed_crc = compute_crc(data)
    return computed_crc == crc


def compute_crc(data):
    crc_value = zlib.crc32(data.encode("utf-8")) & 0xFFFFFFFF
    return format(crc_value, "032b")


def deframe_data(input_file, output_file):
    with open(input_file, "r") as f:
        frame = f.read().strip()

    stuffed_data = frame[:-32]
    received_crc = frame[-32:]

    unstuffed_data = bit_unstuffing(stuffed_data)

    if verify_crc(unstuffed_data, received_crc):
        with open(output_file, "w") as f:
            f.write(unstuffed_data)
    else:
        print("CRC verification failed.")


if __name__ == "__main__":
    input_file = "encoded.txt"
    output_file = "decoded.txt"
    deframe_data(input_file, output_file)
