N, K = map(int, input().split())
burgers = list(input())
count = 0

for i in range(N):
    if burgers[i] == 'P':
        left = max(0, i - K)
        right = min(N, i + K + 1)
        for j in range(left, right):
            if burgers[j] == 'H':
                burgers[j] = 'A'
                count += 1
                break
print(count)