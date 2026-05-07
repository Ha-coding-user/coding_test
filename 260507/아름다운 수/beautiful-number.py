n = int(input())

count = 0

# Please write your code here.
def create_num(n, answer=""):
    global count

    if len(answer) >= n:
        if len(answer) == n:
            count += 1
            return
        else:
            return

    for i in range(1, 5):
        create_num(n, answer + str(i)*i)

create_num(n, "")
print(count)