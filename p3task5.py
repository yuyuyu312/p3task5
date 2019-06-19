p = int(input())


for l in range(p):
    s1 = input()
    s2 = input()
    s1 = set(s1)
    s2 = set(s2)
    g = False
    for i in s1:
        for x in s2:
            if i == x:
                g = True
                break
    if g == True:
        print('YES')
    else:
        print('NO')
