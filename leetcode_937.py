logs = ["dig1 8 1 5 1", "let1 art can" , "dig2 3 6", "let2 own kit dig", "let3 art zero"]

charlog = []
digitlog = []
answer = []
for i in range(len(logs)):
    X = list(logs[i].split())
    if X[1].isdigit():
        digitlog.append(logs[i])
    else :
        charlog.append(logs[i])

charlog.sort(key=lambda x: (x.split()[1:], x.split()[0]))
answer = charlog+digitlog
print(answer)
