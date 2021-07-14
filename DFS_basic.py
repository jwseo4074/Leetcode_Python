number = 7
c = [0 for i in range(7)]
a = [[0 for col in range(8)] for row in range(8)]

def dfs(x):
    if (c[x]):
        return
    c[x] = True
    print(x, " ")
    for i in len(a[x]):
        y = a[x][i]
        dfs(y)

if __name__=="__main__":
    a[1].append(2)
    a[2].append(1)

    a[1].append(3)
    a[3].append(1)

    a[2].append(3)
    a[3].append(2)

    a[2].append(5)
    a[5].append(2)

    a[3].append(6)
    a[6].append(3)

    a[3].append(7)
    a[7].append(3)

    a[4].append(5)
    a[5].append(4)

    a[6].append(7)
    a[7].append(6)

    dfs(1)