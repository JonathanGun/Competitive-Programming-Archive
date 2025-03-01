n, a, b = map(int, input().split())

fizz = 0
buzz = 0
fizzbuzz = 0
for x in range(1, n + 1):
    if x % a == 0 and x % b == 0:
        fizzbuzz += 1
    elif x % a == 0:
        fizz += 1
    elif x % b == 0:
        buzz += 1
    # print(x, fizz, buzz, fizzbuzz)
print(fizz, buzz, fizzbuzz)
