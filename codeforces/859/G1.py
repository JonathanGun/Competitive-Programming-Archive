t = int(input())
for _ in range(t):
    n = int(input())
    # find max(n), remove that (set to 0)
    # if no subsequence sum = max(n), print NO
    # need to count sum range, update when deleted (use BIT -> log(n))
    # there is n element, time = n*log(n)

    # sort(nums) -> iterate from max to min
    # for every n in nums -> two pointer find subsequence with runningSum = n, if exist continue, else print NO and abort
    nums = sorted(list(map(int, input().split())))
    if nums[0] != 1:
        print("NO")
        continue

    cnt = 1
    for n in nums[1:]:
        if cnt < n:
            print("NO")
            break
        cnt += n
    else:
        print("YES")
