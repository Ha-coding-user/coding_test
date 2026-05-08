from copy import deepcopy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = -1

# Please write your code here.
def calculate(grid):
    count = 0

    for row in grid:
        count += sum(row)

    return count

def destroyed(idx, grid, bomb_list):
    global answer

    if idx == len(bomb_list):
        answer = max(answer, calculate(grid))
        # print(grid)
        return

    bomb_type = {1: [(2, 0), (1, 0), (-1, 0), (-2, 0)],
                2: [(1, 0), (-1, 0), (0, 1), (0, -1)],
                3: [(1, 1), (1, -1), (-1, 1), (-1, -1)]}

    for bt in bomb_type.keys():
        dir = bomb_type[bt]
        bomb_row, bomb_col = bomb_list[idx]

        change_list = []
        for d_row, d_col in dir:
            n_row, n_col = bomb_row + d_row, bomb_col + d_col
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid) and grid[n_row][n_col] == 0:
                grid[n_row][n_col] = 1
                change_list.append((n_row, n_col))
        destroyed(idx+1, grid, bomb_list)
        
        for c_row, c_col in change_list:
            grid[c_row][c_col] = 0

bomb = []
for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            bomb.append((row, col))

destroyed(0, grid, bomb)
print(answer)