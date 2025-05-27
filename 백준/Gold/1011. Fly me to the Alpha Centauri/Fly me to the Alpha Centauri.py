T = int(input())
test_list = []
for _ in range(T):
    test_list.append(list(map(int, input().split())))

for i in range(T):
    x, y = test_list[i][0], test_list[i][1]
    distance = y - x
    max_num = int(distance ** 0.5)
    
    if distance == max_num ** 2:
        print(max_num * 2 - 1)
    elif distance <= max_num * (max_num + 1):
        print(max_num * 2)
    else:
        print(max_num * 2 + 1)