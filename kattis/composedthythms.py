n = int(input())
a = n // 3 if n % 3 == 0 else (n - 2) // 3
b = 0 if n % 3 == 0 else (1 if n % 3 == 2 else 2)

print(a + b)
for _ in range(a):
    print(3, end=" ")
for _ in range(b):
    print(2, end=" ")
print()
