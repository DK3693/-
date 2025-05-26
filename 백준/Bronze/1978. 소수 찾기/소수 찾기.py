N = int(input())
numbers = list(map(int, input().split()))
count = 0

for i in numbers:
    if i < 2:
        continue
    state = True
    for num in range(2, int(i ** 0.5) + 1): 
        if i % num == 0:
            state = False
            break
    if state:
        count += 1

print(count)

        
        