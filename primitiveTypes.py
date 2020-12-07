# some tests with bitwise operators


def count_bits(x):
    # counting all non-zero entries of the bitwise representation
    num_bits = 0
    while x:
        num_bits+=x&1 # returns 1 if both the bits are 1, this tests if first byte is 1 (returns 1 if it is)
        x>>=1 # shift by 1 bit and do again
    return num_bits


if __name__ == '__main__':
    # for first 5 integers, print binary representation and count 1s
    for i in range(5):
        print(i, bin(i)[2:].zfill(4), count_bits(i))
