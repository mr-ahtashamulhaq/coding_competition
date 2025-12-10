import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

t = int(data[0])
idx = 1
out_lines = []

for _ in range(t):
    n = int(data[idx]); idx += 1
    B = int(data[idx]); idx += 1
    a = list(map(int, data[idx:idx+n])); idx += n

    d = B - 1
    s = 0
    for x in a:
        s += x

    if d != 0 and s % d != 0:
        out_lines.append("NO")
        continue

    if d == 0:
        out_lines.append("NO")
        continue

    q = []
    rem = 0
    for x in a:
        rem = rem * B + x
        qd = rem // d
        rem = rem % d
        q.append(qd)

    i = 0
    while i < len(q) and q[i] == 0:
        i += 1
    q = q[i:]
    if not q:
        q = [0]

    g = 1
    Y = [g, 0] + q
    Z = [g] + q + [0]
    M = len(Y)

    out_lines.append("YES")
    out_lines.append(str(M))
    out_lines.append(" ".join(map(str, Y)))
    out_lines.append(" ".join(map(str, Z)))

sys.stdout.write("\n".join(out_lines))
