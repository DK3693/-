import sys
sys.setrecursionlimit(10000)

def check(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return
    if cabbage[y][x] == 1:
        cabbage[y][x] = 0
        check(x+1 ,y)
        check(x, y+1)
        check(x-1, y)
        check(x, y-1)

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    count = 0
    cabbage = [[0 for _ in range(M)] for _ in range(N)]
    
    for _ in range(K):    
        X, Y = map(int, sys.stdin.readline().split())
        cabbage[Y][X] = 1
        
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1:
                check(j, i)
                count += 1
     
    print(count)

