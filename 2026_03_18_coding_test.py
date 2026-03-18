TC = int(input())


# ---------------- 틀린 코드 --------------

for _ in range(1, TC+ 1):
    s, p = tuple(map(int,input().split()))
# n+m =s, n = -m+s, (-m+s)m = p, -m+s = p/m
    n ,m = 0, 0
    while True:
        m += 1
        if (-m+s) == p/m:
            n = -m + s
            if n > 0:
                print("Yes")
                break
        elif (m > max(s,p)):
            print("No")
            break


# --------------- 정답 코드 -------------------
# n+m = s, n*m = p
for _ in range(TC):
    s, p = map(int,input().split())

    found =False
    for m in range(1,s):
        # s와 m 이 정해져 있기 때문에 이렇게 적어도 됨
        n = s - m
        if n > 0  and n*m == p:
            found = True
            break

    if found:
        print("Yes")
    else:
        print("No")