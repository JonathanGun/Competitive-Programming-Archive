from difflib import ndiff

for x in ndiff(['asd'], ['asf']):
    print(x)
