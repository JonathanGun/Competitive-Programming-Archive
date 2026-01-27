s = input()
m, d, y = s.split('/')
danish_month_mapping = {
    1: "januar",
    2: "februar",
    3: "marts",
    4: "april",
    5: "maj",
    6: "juni",
    7: "juli",
    8: "august",
    9: "september",
    10: "oktober",
    11: "november",
    12: "december"
}
print(f"{int(d)}. {danish_month_mapping[int(m)]} {y}")
