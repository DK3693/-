import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomatoes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

queue = deque()
for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                queue.append((i, j, 0))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
days = 0
while queue:
    y, x, day = queue.popleft()
    days = day

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0 <= ny < N and 0 <= nx < M:
            if tomatoes[ny][nx] == 0:
                tomatoes[ny][nx] = 1
                queue.append((ny, nx, day + 1))
  
if any(0 in row for row in tomatoes): #모든 토마토가 익었는지 확인
    print(-1)
else:
    print(days)