n = int(input())
tmp = {}
for _ in range(n):
    cmd, *args = input().split()
    if cmd == "INNTAK":
        name, value = args
        tmp[name] = value
    elif cmd == "UTTAK":
        inp = args[0]
        print(tmp[inp])
    elif cmd == "OG":
        inp1, inp2, name = args
    elif cmd == "EDA":
        inp1, inp2, name = args
    elif cmd == "EKKI":
        inp, name = args
