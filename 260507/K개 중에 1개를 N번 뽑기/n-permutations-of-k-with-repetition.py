K, N = map(int, input().split())

# Please write your code here.
def comb(K, N, answer=[]):
    if len(answer) == N:
        print(*answer)
        return

    for i in range(1, K+1):
        answer.append(i)
        comb(K, N, answer)
        answer.pop()

comb(K, N, [])
