T = int(input())

for _ in range(T):
    N = int(input())
    nums = []
    for i in range(N):
        if i < 3:
            nums.append(1)
        elif i < 5:
            nums.append(2)
        else:
            num = nums[i-1] + nums[i-5]
            nums.append(num)

    print(nums[N-1])
