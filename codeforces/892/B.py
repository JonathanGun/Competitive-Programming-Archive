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

def find_small_2(arr):
    mnI = 0
    small = arr[0]
    for i in range(len(arr)):
        if arr[i] <= small:
            small = arr[i]
            mnI = i
    mnI2 = 0 if mnI != 0 else 1
    small_2 = arr[0] if mnI != 0 else arr[1]
    for i in range(len(arr)):
        if arr[i] < small_2 and mnI != i:
            small_2 = arr[i]
            mnI2 = i
    return small, small_2

t = int(input())
for _ in range(t):
    n = int(input())
    # sum(2nd smallest) - min(2nd smallest) + min(1 smallest)
    arrs = [None for i in range(n)]
    for i in range(n):
        _ = int(input())
        arrs[i] = list(map(int, input().split()))
    small_arr = []
    small_2_arr = []
    for i in range(n):
        small, small_2 = find_small_2(arrs[i])
        small_arr.append(small)
        small_2_arr.append(small_2)
    print(sum(small_2_arr) - min(small_2_arr) + min(small_arr))
