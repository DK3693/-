from collections import deque

N, M= map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, input().strip())))
    
maze_visited = [[0] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    maze_visited[y][x] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < M) and (0 <= ny < N):
                if (maze[ny][nx] == 1) and (maze_visited[ny][nx]) == 0:
                    maze_visited[ny][nx] = 1
                    maze[ny][nx] = maze[y][x] + 1
                    queue.append((nx, ny))

bfs(0, 0)
print(maze[N-1][M-1])
    
