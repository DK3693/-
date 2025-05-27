N, M = map(int, input().split())
list = [i + 1 for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    list[i - 1 : j] = list[i - 1 : j][::-1]
print(" ".join(map(str, list)))