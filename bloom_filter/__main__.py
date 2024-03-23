import sys
from bloom_filter.bloom_filter_obj import BloomFilter
import struct


def build_bloom_filter_from_file(file_path, false_positive_rate):
    words_count = None

    with open(file_path, 'r') as file:
        words = [line.strip() for line in file]
        words_count = len(words)
    bloom_filter = BloomFilter(n=words_count, fp=false_positive_rate)

    for word in words:
        bloom_filter.insert(word)
    return bloom_filter

def load_bloom_filter(file_path):
    with open(file_path, "rb") as file:
        header = file.read(8)  # Assuming header size is 8 bytes

        # Validate file type and version
        file_type, version, num_hash_fns, filter_length = struct.unpack('>4sHHI', header)
        if file_type != b'CCBF' or version != 1:
            raise ValueError("Invalid file type or version")

        filter_bytes = file.read(filter_length)
        return filter_bytes


def check_spelling():
    filter_bytes = load_bloom_filter("words.bf")


if __name__ == "__main__":
    
    if sys.argv[1] == "-build":

        dictionary_file = sys.argv[2]
        output_file = "words.bf"
        false_positive_rate = float(sys.argv[3])

        bf = build_bloom_filter_from_file(dictionary_file, false_positive_rate)

        header = struct.pack('>4sHHI', b'CCBF', 1, bf.numOfHashFns, len(bf.filter))
        
        filter_bytes = bytes(bf.filter)
        with open(output_file, 'wb') as file:
            file.write(header)
            file.write(filter_bytes)

    elif sys.argv[1] == "-check":
        words = sys.argv[2:]
        print(words)




