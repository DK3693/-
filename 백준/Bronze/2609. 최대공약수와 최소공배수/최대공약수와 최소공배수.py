import sys

a, b = map(int, sys.stdin.readline().split())

max1 = 1

for i in range(1, a+1):
    if (a % i == 0) and (b % i == 0) and max1 < i:
        max1 = i

max2 = (a * b) // max1

print(max1)
print(max2)
