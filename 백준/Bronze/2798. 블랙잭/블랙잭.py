import sys

N, M = map(int, input().split())
cards = list(map(int,sys. stdin.readline().split()))

best_sum = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            total = cards[i] + cards[j] + cards[k]
            if total <= M:
                best_sum = max(best_sum, total)

print(best_sum)