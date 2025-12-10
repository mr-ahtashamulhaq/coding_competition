import sys
MOD = 998244353

def dist_sq(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return dx * dx + dy * dy

n = int(sys.stdin.readline())
points = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

o_d = [dist_sq(0, 0, x, y) for x, y in points]

canP = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        d_ij = dist_sq(points[i][0], points[i][1], points[j][0], points[j][1])
        maxOD = max(o_d[i], o_d[j])
        if d_ij > maxOD:
            canP[i][j] = True
            canP[j][i] = True


dp = [0] * (1 << n)
dp[0] = 1

for mask in range(1, 1 << n):
    check = True
    bits = []
    for i in range(n):
        if mask & (1 << i):
            bits.append(i)
    
    for i in range(len(bits)):
        for j in range(i + 1, len(bits)):
            if not canP[bits[i]][bits[j]]:
                check = False
                break
        if not check:
            break
    
    if check:
        dp[mask] = 1
    else:
        dp[mask] = 0

ans = 0
for mask in range(1, 1 << n):
    ans = (ans + dp[mask]) % MOD

print(ans)
