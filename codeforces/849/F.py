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


N = 200_005
arr = [0 for i in range(N)]
diff = [0 for i in range(N)]


def lowbit(x):
    return x & (-x)


def add(x, v, n):
    i = x
    while i <= n:
        diff[i] += v
        i += lowbit(i)


def ask(x):
    ans = 0
    i = x
    while i >= 1:
        ans += diff[i]
        i -= lowbit(i)
    return ans


def sumdigit(x):
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans


t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(n + 5):
        diff[i] = 0

    for i in range(q):
        args = list(map(int, input().split()))
        if args[0] == 1:
            l, r = args[1], args[2]
            add(l, 1, n)
            add(r + 1, -1, n)
        if args[0] == 2:
            j = args[1]
            cnt = min(ask(j), 3)
            ans = nums[j - 1]
            for i in range(cnt):
                ans = sumdigit(ans)
            print(ans)
