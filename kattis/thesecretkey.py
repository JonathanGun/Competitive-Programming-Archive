n = int(input())
nums = {int(input(), 2) for _ in range(n)}

# pigeonhole principle
for i in range(n + 1):
    if i not in nums:
        print(f"{i:0{n}b}")
        break
