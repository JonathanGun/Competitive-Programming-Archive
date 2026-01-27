w, h = map(int, input().split())
rectangle = w + h
diagonal = (w**2 + h**2) ** 0.5
print(rectangle - diagonal)
