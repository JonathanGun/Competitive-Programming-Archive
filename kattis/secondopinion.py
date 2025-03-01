s = int(input())
print(" : ".join(map(str, [s // 3600, (s % 3600) // 60, (s % 60)])))