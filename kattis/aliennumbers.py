# decode to base 10
def decode_number(num_str: str, digits: str) -> int:
    base = len(digits)
    value_map = {ch: i for i, ch in enumerate(digits)}

    value = 0
    for ch in num_str:
        value = value * base + value_map[ch]

    return value

# encode from base 10
def encode_number(value: int, digits: str) -> str:
    base = len(digits)

    if value == 0:
        return digits[0]

    result = []
    while value > 0:
        value, rem = divmod(value, base)
        result.append(digits[rem])

    return "".join(reversed(result))

n = int(input())
for i in range(n):
    num, source, target = input().split()
    ans = encode_number(decode_number(num, source), target)
    print(f"Case #{i + 1}: {ans}")
