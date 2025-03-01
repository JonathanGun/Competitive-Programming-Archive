n = int(input())
for _ in range(n):
    sent = input()
    print(sent[0].upper() + sent[1:].lower())