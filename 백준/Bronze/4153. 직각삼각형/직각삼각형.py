while True:
    x, y, z = map(int, input().split())
    if x == y == z == 0:
        break
    state = "wrong"

    if x ** 2 + y ** 2 == z ** 2:
        state = "right"
    elif x ** 2 + z ** 2 == y ** 2:
        state = "right"
    elif y ** 2 + z ** 2 == x ** 2:
        state = "right"
 
    print(state)
