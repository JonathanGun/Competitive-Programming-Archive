hill = input()
h, m = map(int, input().split(":"))
is_weekend = input() in ["sat", "sun"]
is_bad = input() == "1"
is_snow = input() == "1"
is_holiday = input() == "1"
total_mins = h * 60 + m
if is_weekend:
    total_mins *= 2
if is_bad:
    total_mins *= 2
if is_snow:
    total_mins *= 3
if is_holiday:
    total_mins *= 3

res_h, res_m = divmod(total_mins, 60)
print(f"{res_h}:{res_m:02d}")
