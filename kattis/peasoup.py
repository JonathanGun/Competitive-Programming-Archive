ans = ""
n = int(input())
for _ in range(n):
    k = int(input())
    resto = input()
    has_pea_soup = False
    has_pancakes = False
    for _ in range(k):
        menu = input()
        if menu == "pea soup":
            has_pea_soup = True
        if menu == "pancakes":
            has_pancakes = True
    if has_pea_soup and has_pancakes and not ans:
        ans = resto
        break
if ans:
    print(ans)
else:
    print("Anywhere is fine I guess")
