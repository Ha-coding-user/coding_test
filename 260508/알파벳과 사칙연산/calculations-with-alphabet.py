expression = input()

# Please write your code here.
alphabet = expression[::2]
operator = expression[1::2]

alpha_dict = dict()
for a in alphabet:
    alpha_dict[a] = 0

answer = -2**31

def make_comb(alpha_dict, idx, alphabet, operator):
    global answer

    if idx == len(alpha_dict.keys()):
        result = alpha_dict[alphabet[0]]

        for a, o in zip(alphabet[1:], operator):
            if o == "+":
                result += alpha_dict[a]
            elif o == "-":
                result -= alpha_dict[a]
            elif o == "*":
                result *= alpha_dict[a]

        answer = max(answer, result)
        return

    for i in range(1, 5):
        cur_a = list(alpha_dict.keys())[idx]
        alpha_dict[cur_a] = i
        make_comb(alpha_dict, idx+1, alphabet, operator)

make_comb(alpha_dict, 0, alphabet, operator)

print(answer)