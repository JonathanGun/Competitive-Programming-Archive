from queue import LifoQueue

op = ['+', '-', '*', '/']

s = input().strip().split()
numbers = []

for operand in s:
    if operand not in op:
        numbers.append(operand)
    else:
        a = numbers.pop()
        b = numbers.pop()
        numbers.append(f"({b}{operand}{a})")

print(numbers[0])
