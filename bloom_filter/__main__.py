import sys
from bloom_filter.bloom_filter_obj import BloomFilter


def build_bloom_filter_from_file(file_path, size, false_positive_rate):
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file]
    bloom_filter = BloomFilter(
        size=size, false_positive_rate=false_positive_rate)
    for word in words:
        bloom_filter.insert(word)
    return bloom_filter

def check_spelling():
    print("")


if __name__ == "__main__":

    if sys.argv[1] == "-build":
        dictionary_file = sys.argv[2]
        output_file = sys.argv["OUTPUT_FILE"]
        size = 1000000 #read size from dictionary file
        false_positive_rate = sys.argv["FALSE_POSITIVE_RATE"]

        bloom_filter = build_bloom_filter_from_file(dictionary_file, size, false_positive_rate)
        with open(output_file, 'w') as f: f.write(str(bloom_filter))


