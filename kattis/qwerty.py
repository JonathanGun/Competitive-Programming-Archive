QWERTY = "qwertyuiopasdfghjklzxcvbnm"
n = int(input())
text = input().strip()
res = ""
for char in text:
    if char.islower():
        i = ord(char) - ord('a')
        res += QWERTY[i]
    else:
        res += char
print(res)
