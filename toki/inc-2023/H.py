from queue import PriorityQueue as pq

n, m = map(int, input().split())

best_treasures = pq()

for _ in range(n):
    w, v = map(int, input().split())
    best_treasures.put((w, -v))

carts = list(map(int, input().split()))
carts.sort(reverse=True)

total_values = 0
for i, cart in enumerate(carts):
    while not best_treasures.empty():
        w, v = best_treasures.get()
        if w <= cart:
            print("cart", i, "can carry", cart, "worth", v, "treasure weight", w)
            total_values -= v
            break
    else:
        continue
print(total_values)
