case = int(input())
H,W = map(int, input().split())

#matrix = [[0 for i in range(int(W))] for j in range(int(H))]
matrix = []
visit = [[0 for i in range(int(W))] for j in range(int(H))]
for i in range(int(H)):
    input_str = list(input())
    matrix.append(input_str)
cnt = 0
for i in range(H):
    for j in range(W):
        if matrix[i][j] == '#':
            visit[i][j] = 1

# 전부다 1인가 체크
def allone() -> bool:
    for i in range(H):
        for j in range(W):
            if visit[i][j] != 1:
                return False
    return True

# 방향 하나씩 들어가본다
def check(i,j) :
    if matrix[i][j] == '.' and matrix[i+1][j] == '.' and matrix[i+1][j+1] == '.':
        visit[i][j], visit[i + 1][j], visit[i + 1][j + 1] = 1,1,1
        return
    if matrix[i][j] == '.' and matrix[i][j+1] == '.' and matrix[i+1][j+1] == '.':
        visit[i][j], visit[i][j + 1], visit[i + 1][j + 1] = 1,1,1
        return
    if matrix[i][j] == '.' and matrix[i+1][j] == '.' and matrix[i][j+1] == '.':
        visit[i][j], visit[i + 1][j], visit[i][j + 1] = 1,1,1
        return
    if matrix[i+1][j] == '.' and matrix[i][j+1] == '.' and matrix[i+1][j+1] == '.':
        visit[i + 1][j], visit[i][j + 1], visit[i + 1][j + 1] = 1,1,1
        return
    return


for i in range(int(H)):
    for j in range(int(W)):
        if i+1 < H and j+1 < W :
            check(i,j)
            if allone() == True:
                cnt += 1

print(cnt)
print(matrix)
print(visit)


