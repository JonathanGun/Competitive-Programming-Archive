n = int(input())
cur = {
    "fishing": "alice",
    "golf": "bob",
    "hockey": "charlie",
}
for _ in range(n):
    tmp = input().split()
    name, game = tmp[0], tmp[-1]
    if cur[game] != name:
        print(f"{name} borrows {game} from {cur[game]}")
        cur[game] = name
    else:
        print(f"{name} already has {game}")
