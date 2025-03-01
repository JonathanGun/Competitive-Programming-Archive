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


def inLine(xS, yS, xT, yT, d):
    xDiff = xT - xS
    yDiff = yT - yS
    if d == "DR":
        if xDiff >= 0 and yDiff >= 0 and xDiff == yDiff:
            return True
    elif d == "DL":
        if xDiff >= 0 and yDiff <= 0 and xDiff == -yDiff:
            return True
    elif d == "UR":
        if xDiff >= 0 and yDiff <= 0 and -xDiff == yDiff:
            return True
    elif d == "UL":
        if xDiff <= 0 and yDiff <= 0 and xDiff == yDiff:
            return True


t = int(input())

for _ in range(t):
    r, c, y1, x1, y2, x2, d = input().split()
    startX, startY = x1, y1
    y1 = int(y1)
    y2 = int(y2)
    x1 = int(x1)
    x2 = int(x2)
    r = int(r)
    c = int(c)
    coords = set()
    bounces = set()
    last = -1
    print(x1, y1, d)
    
    while last != len(bounces) and len(bounces) < 10:
        last = len(bounces)
        if d == "DR":
            # R shorter than D
            if c - x1 <= r - y1:
                d = "DL"
                x1, y1 = r, y1 + (c - x1)
            else:
                d = "UR"
                x1, y1 = x1 + (r - y1), r
        elif d == "DL":
            # L shorter than D
            if x1 - 1 <= r - y1:
                d = "DR"
                x1, y1 = 1, y1 + (x1 - 1)
            else:
                d = "UL"
                x1, y1 = x1 + (r - y1), r
        elif d == "UR":
            # R shorter than U
            if c - x1 <= y1 - 1:
                d = "UL"
                x1, y1 = c, y1 - (c - x1)
            else:
                d = "DR"
                x1, y1 = x1 + (y1 - 1), 1
        elif d == "UL":
            # L shorter than U
            if x1 - 1 <= y1 - 1:
                d = "UR"
                x1, y1 = 1, y1 - (x1 - 1)
            else:
                d = "DL"
                x1, y1 = x1 - (y1 - 1), 1
        print(x1, y1, d)

        if inLine(x1, y1, x2, y2, d):
            print(len(coords))
            break
        bounces.add((x1, y1, d))
        if (x1, y1) != (startX, startY):
            coords.add((x1, y1))
    else:
        print(-1)
