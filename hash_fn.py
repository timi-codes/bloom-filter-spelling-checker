# Fowler–Noll–Vo (FNV) hash function
# https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
# http://www.isthe.com/chongo/tech/comp/fnv/index.html

def fvn_1a(data):
    # FNV prime and offset basis
    FNV_PRIME = 0x01000193
    OFFSET_BASIS = 0x811c9dc5

    hash = OFFSET_BASIS
    for byte in data:
        hash ^= byte
        hash *= FNV_PRIME
        # Ensures hashValue does not exceed a 32-bit integer range
        hash &= 0xFFFFFFFF

    return hash


# hash = fvn_1a(b"Spell Checker")
# print("Hash value:", hex(hash))
