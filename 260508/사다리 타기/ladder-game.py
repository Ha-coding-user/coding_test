n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
answer = float('inf')

max_height = 0
info = dict()
for a, b in edges:
    max_height = max(max_height, b)
    if b not in info.keys():
        info[b] = [(a, a+1)]
        continue
    info[b].append((a, a+1))

# Please write your code here.
def calc_results(info, n, m):
    results = []

    for s_node in range(1, n+1):
        cur_node = s_node

        for height in range(1, m+1):
            if height not in info.keys():
                continue

            cand = info[height]

            for a, b in cand:
                if cur_node == a:
                    cur_node = b
                elif cur_node == b:
                    cur_node = a

        results.append(cur_node)

    return results

def find_comb(idx, edges, origin_results, n, m, count=0, new_edges=[]):
    global answer

    if idx == len(edges):
        new_info = dict()
        for a, b in new_edges:
            if b not in new_info.keys():
                new_info[b] = [(a, a+1)]
                continue
            new_info[b].append((a, a+1))

        if calc_results(new_info, n, m) == origin_results:
            # print(calc_results(new_info, n, m))
            answer = min(answer, count)

        return

    # 현재 선 추가
    new_edges.append(edges[idx])
    find_comb(idx+1, edges, origin_results, n, m, count+1, new_edges)
    new_edges.pop()

    # 현재 선 추가 안함
    find_comb(idx+1, edges, origin_results, n, m, count, new_edges)

origin_results = calc_results(info, n, max_height)
find_comb(0, edges, origin_results, n, max_height, 0, [])

print(answer)
