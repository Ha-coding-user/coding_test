n, m, C = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def calc_weight(idx, item, C, new_item, answer_list=[]):
    if idx == len(item):
        if sum(new_item) <= C:
            answer_list.append(sum([i**2 for i in new_item]))
        return

    # 선택
    new_item.append(item[idx])
    calc_weight(idx+1, item, C, new_item, answer_list)
    new_item.pop()

    # 선택 안함
    calc_weight(idx+1, item, C, new_item, answer_list)

steal_grid = [[0] * n for _ in range(n)]
for row in range(n):
    for col in range(n-m+1):
        item = [weight[row][c] for c in range(col, col+m)]
        
        if sum(item) <= C:
            steal_grid[row][col] = sum([i**2 for i in item])
        else:
            answer_list = []
            calc_weight(0, item, C, [], answer_list)
            steal_grid[row][col] = max(answer_list)

m1_list = []
m1 = 0
for row in range(n):
    for col in range(n-m+1):
        if steal_grid[row][col] > m1:
            m1 = steal_grid[row][col]
            m1_list = [(row, col)]
        elif steal_grid[row][col] == m1:
            m1_list.append((row, col))

m2 = 0
for m1_row, m1_col in m1_list:
    used = [(m1_row, m1_c) for m1_c in range(m1_col, m1_col+m)]
    
    for row in range(n):
        for col in range(n-m+1):
            ok = False
            for c in range(col, col+m):
                if (row, c) in used:
                    ok = True
            
            if ok:
                continue
            
            m2 = max(m2, steal_grid[row][col])

print(m1 + m2)