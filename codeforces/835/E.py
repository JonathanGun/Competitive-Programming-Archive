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


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    if n == 1:
        print(0)
        continue
    # for n in nums, sum (number of zero) behind
    # always beneficial turn first 0 to 1
    # or last 1 to 0
    # flipping 0 -> 1: adds no of 0 behind = cnt0 - 1, minus no of 1 in front
    # flipping 1 -> 0: adds no of 1 infront = cnt1 - 1, minus no of 0 behind
    ans = 0
    cnt0 = 0
    cnt1 = 0
    first0 = -1
    last1 = n
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            cnt0 += 1
            first0 = i
        else:
            cnt1 += 1
            ans += cnt0
            if last1 == n:
                last1 = i
    front1 = 0
    behind0 = 0
    for i in range(n):
        if i < first0:
            if nums[i] == 1:
                front1 += 1
        if i > last1:
            if nums[i] == 0:
                behind0 += 1
    # print(ans, cnt0, cnt1, first0, last1, front1, behind0)
    tmp = ans
    if last1 != n:
        # print("flip last 1 to 0:", ans, cnt1 - 1, behind0)
        tmp = max(tmp, ans + cnt1 - 1 - behind0)
    if first0 != -1:
        # print("flip first 0 to 1:", ans, cnt0 - 1, front1)
        tmp = max(tmp, ans + cnt0 - 1 - front1)
    print(max(ans, tmp))
