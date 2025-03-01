while True:
    n = int(input())
    if n == -1:
        break
    adjs = []
    for _ in range(n):
        adjs.append(list(map(int, input().split())))
    weaks = [True for _ in range(n)]
    for i in range(n):
        # print(i, adjs[i])
        for j, adj in enumerate(adjs[i]):
            if adj == 1 and j > i:
                # print("adj to", j , adjs[j])
                for k, adj2 in enumerate(adjs[j]):
                    if adjs[j][k] == 1 and adjs[k][i] == 1 and k != i:
                        # print(i, j, k)
                        # print("adj to", k, "as well")
                        # print(i, j)
                        weaks[i] = False
                        weaks[j] = False
                        weaks[k] = False
                        break
    for i, weak in enumerate(weaks):
        if weak:
            print(i, end=" ")
    print()
