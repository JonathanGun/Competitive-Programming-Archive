from queue import PriorityQueue as pq

n, m, k = map(int, input().split())
p = list(map(int, input().split()))

top_consuming_milks = pq()
for i in range(n):
    m -= p[i]
    top_consuming_milks.put(-p[i])
    if m < 0:
        if k == 0:
            print(i)
            break
        x = -top_consuming_milks.get()
        # print("restoring milk from", x)
        m += x
        k -= 1
else:
    print(n)
