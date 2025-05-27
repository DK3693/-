list = []
for _ in range(10):
    A = int(input())
    B = A % 42
    if B not in list:
        list.append(B)
print(len(list))