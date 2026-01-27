from heapq import heappush, heappop
from math import hypot


def solve(n, colonies):
    dist = [
        [
            hypot(colonies[i][0] - colonies[j][0], colonies[i][1] - colonies[j][1])
            for j in range(n)
        ]
        for i in range(n)
    ]

    visited = [False] * n
    pq = [(0, 0, -1)]
    adj = [[] for _ in range(n)]

    while pq:
        edge_w, u, p = heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        if p != -1:
            adj[u].append((p, edge_w))
            adj[p].append((u, edge_w))
        for v in range(n):
            if not visited[v]:
                heappush(pq, (dist[u][v], v, u))

    max_edge = [0.0] * n
    visited = [False] * n
    stack = [(0, 0.0)]
    while stack:
        u, m = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        max_edge[u] = m
        for v, w in adj[u]:
            if not visited[v]:
                stack.append((v, max(m, w)))

    total_pop = sum(c[2] for c in colonies)
    if total_pop == 0:
        return 0.0
    return sum(colonies[i][2] * max_edge[i] / 3 for i in range(n)) / total_pop


case = 0
while True:
    n = int(input())
    if n == 0:
        break
    case += 1
    colonies = [tuple(map(int, input().split())) for _ in range(n)]
    print(f"Colony Group: {case} Average {solve(n, colonies):.2f}")
    print()
