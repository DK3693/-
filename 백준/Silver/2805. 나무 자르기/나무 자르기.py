N, M = map(int, input().split())  
tree = list(map(int, input().split()))

top = max(tree)
bottom = 0
height = 0

while bottom <= top:
    num = (top + bottom) // 2
    total = sum(x - num for x in tree if x > num)      
    if total >= M:
        height = num
        bottom = num + 1
    elif total < M:
        top = num - 1
print(height)
        
