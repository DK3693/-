N, M = map(int, input().split())
lists = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for num in range(i - 1, j):
        lists[num] = k
print(' '.join(map(str, lists)))