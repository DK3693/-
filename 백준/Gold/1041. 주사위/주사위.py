N = int(input())
A, B, C, D, E, F = map(int, input().split())

vertex_list = [A+B+C, A+B+D, B+F+C, B+F+D, F+E+C, F+E+D, E+A+C, E+A+D]
corner_list = [A+B, B+F, F+E, E+A, A+D, A+C, E+D, E+C, B+D, B+C, F+D, F+C]
face_list = [A, B, C, D, E, F]

vertex = min(vertex_list)
corner = min(corner_list)
face = min(face_list)

vertex_sum = vertex * 4
corner_sum = corner * (4 * ((N-1) + (N-2)))
face_sum =face * ((N-2) * ((N-1) * 4 + (N-2)))

total = vertex_sum + corner_sum + face_sum

if N == 1:
    total = sum(face_list) - max(face_list)
    print(total)
else:
    print(total)