import math
from hash_fn import fvn_1a

def _calculate_optimal_m_k(n, p):
    # https://en.wikipedia.org/wiki/Bloom_filter
    m = - (n * math.log(p)) / (math.log(2) ** 2)
    k = (m / n) * math.log(2)
    return int(math.ceil(m)), int(math.ceil(k))


class BloomFilter:
    """
    filter: a bit array with all bits to zero.
    capacity(n): Number of items expected to be stored
    fp(p): Probability of false positive
    itemSize(m): Number of bits per element
    numOfHashFns(k): Number of hash functions
    """
    filter = []
    capacity = None
    fp = 0.01
    itemSize = None
    numOfHashFns = 1

    def __init__(self, n, fp):
        self.capacity = n
        self.fp = fp
        self.itemSize, self.numOfHashFns = _calculate_optimal_m_k(n, fp)
        self.filter = [0] * self.itemSize

    def insert(self, item):
        #Insert items by applying the hash functions and setting the corresponding bits to 1
        for hash_value in self._computeHashes(item):
            self.filter[hash_value] = 1

    def query(self, item):
        for hash_value in self._computeHashes(item):
            if self.filter[hash_value] == 0: 
                return False

        return True

    def _computeHashes(self, data):
        hash_values = []

        for i in range(0, self.numOfHashFns):
            # Use different seeds for different hash functions
            seed = str(i + 1)
            data = "%s%s" % (seed, data)
            hash = fvn_1a(data.encode('utf-8'))
            hash_values.append(hash % self.itemSize)

        return hash_values
