## Bloom Filter Spelling Checker
### Coding Challenge #53:
[The challenge](https://codingchallenges.substack.com/p/coding-challenge-53-bloom-filter) is to build a lightweight spelling checker by leveraging bloom filter without having to filter through a dictionary file (dict.txt), thus minimizing disk and memory usage.


### Bloom Filter
```bloom_filter/__init__.py``` contain the bloom filter class implementation which includes `calculate_optimal_m_k(n, fp)` function that takes the number of items to be stored in the filter and the false positives as arguments. This function is used to calculate the most efficient number of bits per item and number of hash functions needed to achieve the false positive. The bloom filter class also include the `compute_hashes(self, data)` function which uses a non-cryptographic hash function [Fowler–Noll–Vo hash algorithm](https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function) to generate the hash values to represent items in our bloom filter data structure.

### Build Bloom Filter from Dictionary
```bloom_filter/__main__.py``` contains `build_bloom_filter_from_file` helper for loading words in the dictionary into the bloom filter. The filter called `words.bf` is then generated and saved in the root directory.

    Usage: ```spellcheck < -build > <dictionary_file> [-fp <false_positive_rate>]```

    ```shell
        ./spellcheck -build dict.txt -fp 0.01
    ```

*Output*: 
```
    Bloom filter built and saved to words.bf
```

### Check Spelling
The `words.bf` is loaded and the Bloom Filter Class is reconstructed and we can use our `query()` function to check if a word exist in the bloom filter

- Usage ```spellcheck < -check > <words>```
    ```bash
        ./spellcheck -check This erro can be an isue with my real mothers tongu
    ```

*Output*: 
```
These words are spelt wrong:
 This
 erro
 isue
 mothers
 tongu
```


### References
[Coding Challenge #53 - Bloom Filter Spell Checker](https://codingchallenges.substack.com/p/coding-challenge-53-bloom-filter)

[Bloom Filters Explained](https://systemdesign.one/bloom-filters-explained/)

[FNV Hash](http://www.isthe.com/chongo/tech/comp/fnv/index.html)

[Bloom Filter Calculator](https://hur.st/bloomfilter/?n=235976&p=0.00000001&m=&k=)