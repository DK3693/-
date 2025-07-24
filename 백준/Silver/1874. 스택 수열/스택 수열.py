import sys

n = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
result = []
count = 1
possible = True

for num in nums:
    while count <= num:
        stack.append(count)
        result.append("+")
        count += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")

    else:
        possible = False
        break

if possible:
    for i in result:
        print(i)
else:
    print("NO")
