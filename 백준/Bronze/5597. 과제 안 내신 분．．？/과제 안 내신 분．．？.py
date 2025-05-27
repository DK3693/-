n_list = []
for i in range(30):
    n_list.append(i + 1)
for _ in range(28):
    index = int(input())
    n_list.remove(index)
print(n_list[0])
print(n_list[1])