from collections import defaultdict

m, n = map(int, input().split())
clauses = defaultdict(int)
for _ in range(m):
    a, b, c = map(int, input().split())
    clauses[frozenset([a, b, c])] += 1
if len(clauses) < 8:
    print("unsatisfactory")
else:
    print("satisfactory")
