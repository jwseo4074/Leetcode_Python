# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:

cnt = 0
grid1 = [
    ["1","1","1","1","0"],\
    ["1","1","0","1","0"],\
    ["1","1","0","0","0"],\
    ["0","0","0","0","0"]
]
grid2 = [
    ["1","1","1","1","0"],\
    ["1","0","0","0","0"],\
    ["0","0","0","1","0"],\
    ["1","1","1","1","1"]
]
grid3 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
grid = [
    ["1","0","1","1","1"],
    ["1","0","1","0","1"],
    ["1","1","1","0","1"]
]
visit = [["0" for col in range(len(grid[0]))] for row in range(len(grid))]
max_row = len(grid)
max_col = len(grid[0])

def dfs(row, col):
    if 0 <= row < max_row and 0 <= col < max_col :
        if visit[row][col] == "0":
        # 방문 안한곳이면
            print("방문 = ", row, col)
            visit[row][col] = "1"
            print(visit)
            # 방문 체크
            if grid[row][col] == "1":
                # grid 가 1이여야 함 => 그럼 계속 진행
                dfs(row,col+1)
                # 오른쪽
                dfs(row+1, col)
                # 아래쪽
                dfs(row, col-1)
                # 왼쪽
                dfs(row-1, col)
                # 위쪽
        else:
        # 방문을 했던곳 -> 바로 리턴
            return
    else:
        # row 랑 col 이 범위를 넘어서면 바로 return
        return
    return

#print(visit)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if visit[i][j] == "0" and grid[i][j] == "1":
        # 방문을 안한곳이고 grid 가 1이여야 함
            dfs(i,j)
            #print(visit)
            cnt += 1

print(cnt)