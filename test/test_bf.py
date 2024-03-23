import unittest
from bloom_filter import BloomFilter
from types import SimpleNamespace

test_dict = {
    "capacity": 235976, # This is the total number of words in dict.txt
    "fp": 0.01,
    "bits_per_element": 2261844,
    "num_hash_fns": 7
}
test_params = SimpleNamespace(**test_dict)

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.bf = BloomFilter(test_params.capacity, test_params.fp)

    def test_init(self):
        self.assertEqual(self.bf.capacity, test_params.capacity, "Capacity wasn't properly set")
        self.assertEqual(self.bf.fp, test_params.fp,"False positive is wrongly set")
        self.assertIsNotNone(self.bf.bits_size, "False positive is wrongly set")
        self.assertGreater(self.bf.num_hash_fns, 1, "Hash functions is invalid")
        self.assertEqual(len(self.bf.filter), test_params.bits_per_element, "filter length is not equal to the expected size")

    def test_optimal_m_k(self):
        m, k = BloomFilter.calculate_optimal_m_k(test_params.capacity, test_params.fp)
        self.assertEqual(m, test_params.bits_per_element, "No of bits per element is not equal")
        self.assertEqual(k, test_params.num_hash_fns, "No of hash functions is not equal")


    def test_computeHashes(self):
        hashValues = self.bf.compute_hashes("RED")

        self.assertEqual(len(hashValues), test_params.num_hash_fns, "No of hash functions is not equal")

    def test_insert(self):
        item = "RED"
        self.bf.insert(item)

        for hash_value in self.bf.compute_hashes(item):
            self.assertEqual(self.bf.filter[hash_value], 1, f"Bit at index {hash_value} should be set to 1 after inserting the item")

    def test_query_postive(self):
        item = "RED"
        self.bf.insert(item)  

        result = self.bf.query(item)
        self.assertTrue(result, "Query should return True for an inserted item")

    def test_query_negative(self):
        item = "RED"

        result = self.bf.query(item)
        self.assertFalse(result, "Query should return False for an item not inserted")


    def test_false_positives(self):
        bf = BloomFilter(10, 0.1)

        known_items = ["apple", "banana", "cherry"]
        for item in known_items:
            bf.insert(item)

        non_inserted_items = ["grape", "kiwi", "orange", "date", "elderberry", "fig", "honeydew", "pear", "quince", "raspberry", "wig"]
        false_positives = 0
        for item in non_inserted_items:
            if bf.query(item):
                false_positives += 1

        false_positive_rate = false_positives / len(non_inserted_items)
        print(false_positive_rate)

        self.assertTrue(false_positive_rate <= 0.1, "False positive rate exceeds threshold")

if __name__ == '__main__':
    unittest.main()
