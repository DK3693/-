chess_have = list(map(int, input().split()))
chess_musthave = [1, 1, 2, 2, 2, 8]
chess_need = []
for i in range(len(chess_musthave)):
    chess_need.append(chess_musthave[i] - chess_have[i])
print(" ".join(map(str, chess_need)))