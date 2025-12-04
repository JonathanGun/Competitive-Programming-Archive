import sys

data = sys.stdin.read()
data = data.replace("\n", ",").replace(" ", "")
bytes_list = [int(x) for x in data.split(",") if x.strip()]

n = len(bytes_list)


def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]


PRIMES = sieve(1700)


def check_length(length):
    h = sum(PRIMES[bytes_list[i]] for i in range(length))
    s = sum(bytes_list[:length])

    hash_to_first = {}
    key = (h, s)
    hash_to_first[key] = 0

    for i in range(1, n - length + 1):
        h = h - PRIMES[bytes_list[i - 1]] + PRIMES[bytes_list[i + length - 1]]
        s = s - bytes_list[i - 1] + bytes_list[i + length - 1]
        key = (h, s)

        if key in hash_to_first:
            first_i = hash_to_first[key]
            if i >= first_i + length:
                seq1 = bytes_list[first_i : first_i + length]
                seq2 = bytes_list[i : i + length]
                if seq1 != seq2 and sorted(seq1) == sorted(seq2):
                    return (first_i, i)
        else:
            hash_to_first[key] = i

    return None


for length in range(n // 2, 3, -1):
    pair = check_length(length)
    if pair:
        print(length, pair[0], pair[1])
        sys.exit()

print("no key")
