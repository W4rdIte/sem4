from frame_bits import frame_data
from deframe_bits import deframe_data

if __name__ == "__main__":
    input = "input.txt"
    encoded = "encoded.txt"
    decoded = "decoded.txt"

    input_file = input
    output_file = encoded
    frame_data(input_file, output_file)

    input_file = encoded
    output_file = decoded
    deframe_data(input_file, output_file)
