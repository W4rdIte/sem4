import zlib


def bit_stuffing(data):
    count = 0
    stuffed = ""
    for bit in data:
        if bit == "1":
            count += 1
        else:
            count = 0
        stuffed += bit
        if count == 5:
            stuffed += "0"
            count = 0
    return stuffed


def compute_crc(data):

    crc_value = zlib.crc32(data.encode("utf-8")) & 0xFFFFFFFF
    return format(crc_value, "032b")


def frame_data(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read().strip()

    stuffed_data = bit_stuffing(data)
    crc = compute_crc(data)
    frame = stuffed_data + crc

    with open(output_file, "w") as f:
        f.write(frame)


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "encoded.txt"
    frame_data(input_file, output_file)
