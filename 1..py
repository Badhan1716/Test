t = int(input())
for i in range(t):
    n = int(input( ))
    a = 0
    b = 0
    for j in range(n):
        x, y = map(int, input().split())
        a = max(a, x)
        b = max(b, y)

    print((a + b) * 2)
