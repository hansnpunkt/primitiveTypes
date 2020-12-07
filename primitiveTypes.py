# some tests with bitwise operators


def count_bits(x):
    # counting all non-zero entries of the bitwise representation
    num_bits = 0
    while x:
        num_bits+=x&1 # returns 1 if both the bits are 1, this tests if first byte is 1 (returns 1 if it is)
        x>>=1 # shift by 1 bit and do again
    return num_bits

def parity_bits(x):
    # calculate parity of a word
    result = 0
    while x:
        result^=x&1 # first checks if lowest set bit is 1, then xor with 0 or 1 (switches between 0 and 1, mod 2)
        x>>=1
    return result # time complexity O(n)

def improved_parity(x):
    result = 0
    while x:
        result ^= 1
        x &= (x - 1) # drop lowest set bit (basically drop bits k times, reduced time complexity is O(k)
    return result


if __name__ == '__main__':
    # for first 5 integers, print binary representation and count 1s, print parity too
    for i in range(5):
        print(i, bin(i)[2:].zfill(4), count_bits(i), parity_bits(i), improved_parity(i))
