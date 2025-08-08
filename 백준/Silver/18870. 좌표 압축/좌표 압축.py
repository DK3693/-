import sys

_ = int(sys.stdin.readline())  # N은 사용 안 함
nums = list(map(int, sys.stdin.readline().split()))

nums_dic = {v: i for i, v in enumerate(sorted(set(nums)))}

print(*[nums_dic[n] for n in nums])