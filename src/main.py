from huffman_encoder import huffman_encode
import os
import sys

main_script_dir = os.path.dirname(os.path.abspath(__file__))
TEXT_PATH = os.path.join(main_script_dir, "../text_encoded_files/")

input_file = f"{TEXT_PATH}{sys.argv[1]}"

if __name__ == "__main__":
    huffman_encode(input_file)
    #decompression_time = decode(compressed_file, output_file)
    #detailed_report("Huffman Encoding", input_file, compressed_file, compression_time, 
                    #decompression_time)
