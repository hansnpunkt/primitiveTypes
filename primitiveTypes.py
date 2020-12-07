from random import choice

def getRandomByte(n):
    # returns a random binary word as string of size n
    rand_bytes = ''.join(choice('01') for _ in range(n))
    return rand_bytes



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(getRandomByte(10))
