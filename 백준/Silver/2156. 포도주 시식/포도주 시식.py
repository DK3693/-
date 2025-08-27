import sys
input = sys.stdin.readline

n = int(input())
w = [int(input()) for _ in range(n)]

if n == 1:
    print(w[0])
elif n == 2:
    print(w[0] + w[1])
else:
    d0, d1, d2 = 0, w[0], w[0] + w[1]   # dp[i-3], dp[i-2], dp[i-1]
    for i in range(2, n):
        d0, d1, d2 = d1, d2, max(d2, d1 + w[i], d0 + w[i-1] + w[i])
    print(d2)