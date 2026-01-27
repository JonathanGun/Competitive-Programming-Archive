TRUE_VALUE = "SATT"
FALSE_VALUE = "OSATT"

n = int(input())
tmp = {}
for _ in range(n):
    cmd, *args = input().split()
    if cmd == "INNTAK":
        name, value = args
        if value == TRUE_VALUE:
            value = True
        else:
            value = False
        tmp[name] = value
    elif cmd == "UTTAK":
        inp = args[0]
        if tmp[inp]:
            print(inp, TRUE_VALUE)
        else:
            print(inp, FALSE_VALUE)
    elif cmd == "OG":
        inp1, inp2, name = args
        if tmp[inp1] and tmp[inp2]:
            tmp[name] = True
        else:
            tmp[name] = False
    elif cmd == "EDA":
        inp1, inp2, name = args
        if tmp[inp1] == False and tmp[inp2] == False:
            tmp[name] = False
        else:
            tmp[name] = True
    elif cmd == "EKKI":
        inp, name = args
        if tmp[inp]:
            tmp[name] = False
        else:
            tmp[name] = True
