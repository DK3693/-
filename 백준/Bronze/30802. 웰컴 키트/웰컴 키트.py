N = int(input())
total = 0

clothes = list(map(int, input().split()))
T, P = map(int, input().split())

for i in clothes:
    if i % T == 0:
        total += int(i / T)
    else:
        total += int(i / T) + 1
        
pens = int(N/P)
pen = N % P

print(total)
print(pens, pen)
