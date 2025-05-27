from collections import deque

N, K = map(int, input().split())

visited = [False] * 100001
queue = deque()
queue.append((N, 0))

while queue:
    current, time = queue.popleft()
    if current == K:
        print(time)
        break
    
    for next_index in (current-1, current+1, current*2):
        if 0 <= next_index <= 100000 and not visited[next_index]:
            visited[next_index] = True
            queue.append((next_index, time+1))
        