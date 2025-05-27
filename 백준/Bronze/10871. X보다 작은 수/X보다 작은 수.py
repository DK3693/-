N, X = map(int, input().split())
A = map(int, input().split())

for i in A:
    if X > i:
        print(i, end=" ")
    