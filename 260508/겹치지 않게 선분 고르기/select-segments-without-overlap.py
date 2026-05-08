answer = 0

def dfs(idx, visited, x1, x2, count):
    global answer

    if max(visited) > 1:
        return

    if idx == len(x1):
        answer = max(answer, count)
        return

    # 현재 선 선택
    cur_a, cur_b = min(x1[idx], x2[idx]), max(x1[idx], x2[idx])
    for node in range(cur_a, cur_b+1):
        visited[node] += 1
    dfs(idx+1, visited, x1, x2, count+1)
    for node in range(cur_a, cur_b+1):
        visited[node] -= 1


    # 현재 선 선택 x
    dfs(idx+1, visited, x1, x2, count)


n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.
max_node = max(max(x1), max(x2))
visited = [0] * (max_node+1)

dfs(0, visited, x1, x2, 0)

print(answer)