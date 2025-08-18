import sys
input = sys.stdin.readline

N, K = map(int, input().split())
row = input().strip()

H = [i for i, ch in enumerate(row) if ch == 'H']
P = [i for i, ch in enumerate(row) if ch == 'P']

i = j = ans = 0
while i < len(P) and j < len(H):
    if H[j] < P[i] - K:      # 이 햄버거는 너무 왼쪽 -> 다음 햄버거
        j += 1
    elif H[j] > P[i] + K:    # 이 사람에겐 너무 오른쪽 -> 다음 사람
        i += 1
    else:                    # |H[j] - P[i]| <= K → 매칭
        ans += 1
        i += 1
        j += 1

print(ans)