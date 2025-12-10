import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

t = int(data[0])
idx = 1
out_lines = []
letters = ('R', 'G', 'B')

for _ in range(t):
    n = int(data[idx])
    idx += 1
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = int(data[idx])
        idx += 1

    vis = [False] * (n + 1)
    col = [''] * (n + 1)

    for i in range(1, n + 1):
        if not vis[i]:
            cur = i
            cycle = []
            while not vis[cur]:
                vis[cur] = True
                cycle.append(cur)
                cur = p[cur]

            k = len(cycle)
            if k % 2 == 0:
                for pos, node in enumerate(cycle):
                    col[node] = letters[pos & 1]
            else:
                last_pos = k - 1
                for pos, node in enumerate(cycle):
                    if pos == last_pos:
                        col[node] = letters[2]
                    else:
                        col[node] = letters[pos & 1]

    out_lines.append(''.join(col[1:]))

sys.stdout.write('\n'.join(out_lines))
