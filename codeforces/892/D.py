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


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        furthest_portal = [0] * n
        events = []

        for i in range(n):
            l, r, a, b = map(int, input().split())
            furthest_portal[i] = b
            events.append((b, 2, i))
            events.append((l, 0, i))

        q = int(input())
        queries = list(map(int, input().split()))
        events.extend((x, 1, i) for i, x in enumerate(queries))

        events.sort(reverse=True)
        current_open_portal = -1
        n_open_portal = 0

        for value, type_, i in events:
            if type_ == 2:
                if n_open_portal > 0:
                    furthest_portal[i] = current_open_portal
                current_open_portal = furthest_portal[i]
                n_open_portal += 1
            elif type_ == 1:
                if n_open_portal > 0:
                    queries[i] = max(queries[i], current_open_portal)
            else:
                n_open_portal -= 1
                if n_open_portal == 0:
                    current_open_portal = -1

        print(*queries)


if __name__ == "__main__":
    main()
