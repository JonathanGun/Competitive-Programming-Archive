def ok(i):
    stri = str(i)
    se = sum(1 for d in stri if d in "02468")
    so = sum(1 for d in stri if d in "13579")
    return se == so


def aupto(nn):
    alst, an = [None], 0
    for n in range(1, nn + 1):
        while len(alst) < nn + 1:
            if ok(an):
                alst.append(an)
            an += 1
    return alst[1:]  # use alst[n] for a(n)


print(aupto(1000))
