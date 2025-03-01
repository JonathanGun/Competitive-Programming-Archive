x = float(input())
low_limit = [
    ("Logn", 0),
    ("Andvari", 0.3),
    ("Kul", 1.6),
    ("Gola", 3.4),
    ("Stinningsgola", 5.5),
    ("Kaldi", 8.0),
    ("Stinningskaldi", 10.8),
    ("Allhvass vindur", 13.9),
    ("Hvassvidri", 17.2),
    ("Stormur", 20.8),
    ("Rok", 24.5),
    ("Ofsavedur", 28.5),
    ("Farvidri", 32.7),
]

for k, v in low_limit[::-1]:
    if x >= v:
        print(k)
        break
