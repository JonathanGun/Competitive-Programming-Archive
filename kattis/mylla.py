n = int(input())
s = input()
cur_a, cur_h = 0, 0
cnt_a, cnt_h = 0, 0
for c in s:
    if c == 'A':
        cur_a += 1
    else:
        cur_h += 1
    if cur_a == 3:
        cnt_a += 1
        cur_a, cur_h = 0, 0
    elif cur_h == 3:
        cnt_h += 1
        cur_a, cur_h = 0, 0
    if cnt_a == n:
        print('Hannes')
        break
    elif cnt_h == n:
        print('Arnar')
        break
