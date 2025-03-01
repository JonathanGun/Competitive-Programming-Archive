#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase

# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

from typing import List
from itertools import permutations

"""
cost is p*i over all i, except the largest p*i
"""


def cost(arr: List[int]):
    ans = 0
    maxAI = 0
    for i, a in enumerate(arr):
        ans += a * (i + 1)
        if a * (i + 1) > maxAI:
            maxAI = a * (i + 1)
    return ans - maxAI

MAX_N = 250 + 5
flipI = 0
ans = [0 for i in range(MAX_N)]
for n in range(2, MAX_N):
    # print(n)
    ls = [(i + 1 if i < flipI else n - i + flipI) for i in range(n)]
    ls2 = [(i + 1 if i < flipI - 1 else n - i + flipI - 1) for i in range(n)]
    # print(ls)
    # print(ls2)
    costL = cost(ls)
    costL2 = cost(ls2)
    if costL > costL2:
        flipI += 1
    ans[n] = max(costL, costL2)
    # mx = 0
    # mxL = []
    # for l in permutations(ls):
    #     c = cost(l)
    #     if c > mx:
    #         mx = c
    #         mxL = l
    #     # print(l, c)
    # print(i, mxL, mx)


# def max_permutation_cost(N):
#     dp = [[0] * (N + 1) for _ in range(N + 1)]

#     for i in range(1, N + 1):
#         for j in range(i + 1):
#             dp[i][j] = dp[i - 1][j]  # Skip the current element

#             if j > 0:
#                 dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + i * j)

#     max_cost = 0
#     for j in range(N + 1):
#         max_cost = max(max_cost, dp[N][j] - j * N)

#     return max_cost


t = int(input())
for _ in range(t):
    N = int(input())
    print(ans[N])
