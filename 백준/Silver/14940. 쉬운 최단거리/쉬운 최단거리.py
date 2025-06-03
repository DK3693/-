import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
mapp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

queue = deque()

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 2:
            mapp[i][j] = 0
            visited[i][j] = True
            queue.append((i, j))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
while queue:
    y, x = queue.popleft()
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ny][nx] and mapp[ny][nx] != 0:
                mapp[ny][nx] = mapp[y][x] + 1
                visited[ny][nx] = True
                queue.append((ny, nx))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and mapp[i][j] == 1:
            mapp[i][j] = -1
        
for i in range(n):
        print(*mapp[i])
