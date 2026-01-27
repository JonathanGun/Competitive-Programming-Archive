virus = input()
filename = input()
i = 0
for c in filename:
    if c == virus[i]:
        i += 1
    if i == len(virus):
        print("Ja")
        break
else:
    print("Nej")
