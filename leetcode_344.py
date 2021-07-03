input_str = list(input())
answer = []

for i in range(len(input_str)):
    if input_str[i] in X :
        answer.append(input_str[i])
answer_2 = answer[::-1]

for j in range(len(answer_2)):
    if j == 0:
        print("[", end="")
    if j != len(answer_2)-1:
        print("\""+ answer_2[j] + "\"", end="")
        print(",", end="")
    if j == len(answer_2)-1:
        print("\"" + answer_2[j] + "\"" + "]")


