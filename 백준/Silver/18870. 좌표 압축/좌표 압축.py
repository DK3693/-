import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
nums_uniqued = list(set(nums))              # 중복값 제거
nums_sorted = sorted(nums_uniqued)          # 정렬


nums_dic = {}
for i in range(len(nums_sorted)):
    nums_dic[nums_sorted[i]] = i            # 정렬된 상태로 딕셔너리에 저장

for num in nums:
    print(nums_dic[num], end=" ")           # 키값을 찾아 출력

