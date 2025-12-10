import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

t = int(data[0])
idx = 1
out_lines = []

for _ in range(t):
    a = data[idx]
    b = data[idx + 1]
    idx += 2

    pa = a.count('P')
    pb = b.count('P')

    if pa == 0 or pb == 0:
        if a == b:
            out_lines.append("YES")
        else:
            out_lines.append("NO")
        continue

    if pa != pb:
        out_lines.append("NO")
        continue

    ta = len(a) - a.rfind('P') - 1
    tb = len(b) - b.rfind('P') - 1

    if ta == tb:
        out_lines.append("YES")
    else:
        out_lines.append("NO")

sys.stdout.write("\n".join(out_lines))
