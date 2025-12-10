import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

t = int(data[0])
idx = 1
out_lines = []

for _ in range(t):
    n = int(data[idx])
    idx += 1
    mid = n // 2
    for r in range(n):
        row = ['.'] * n
        row[0] = '#'
        row[-1] = '#'
        if r <= mid:
            row[r] = '#'
            row[n - 1 - r] = '#'
        out_lines.append(''.join(row))

sys.stdout.write('\n'.join(out_lines))
