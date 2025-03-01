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

MAX_C = 1_000_000_000

t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    nums = list(map(int, input().split()))
    costL = [nums[i] + i + 1 for i in range(n)]
    costR = [nums[i] + (n - i) for i in range(n)]
    # for i in range(n):
    #     nums[i] += i + 1
    print(c, nums, costL, costR)

    mnL = MAX_C
    mnI = -1
    for i in range(n):
        if costL[i] < mnL:
            mnL = costL[i]
            mnI = i
    if mnI != -1:
        costL[mnI] = MAX_C + 1
        costR[mnI] = MAX_C + 1

    # 1st step
    ans = 0
    if c >= mnL:
        ans = 1
        c -= mnL
    for i in range(n):
        costL[i] = min(costL[i], costR[i])
    costL = sorted(costL)

    print(c, ans, costL)
    for i in range(n):
        c -= costL[i]
        if c < 0:
            break
        ans += 1
    print(ans)
