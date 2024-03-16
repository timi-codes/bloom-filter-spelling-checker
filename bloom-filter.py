

import math


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
        self.itemSize, self.numOfHashFns = self._calculate_optimal_m_k(n, fp)
        self.filter = [0] * self.itemSize


    def insert(self, item):
        return ""

    def _computeHashes(self, ):
        hashValues = []

        for hashFn in len(self.numOfHashFns):
            

    def _calculate_optimal_m_k(self, n, p):
        m = - (n * math.log(p)) / (math.log(2) ** 2)
        k = (m / n) * math.log(2)
        return int(math.ceil(m)), int(math.ceil(k))
