import sys

data = sys.stdin.buffer.read().split()
if not data:
    sys.exit()

vals = list(map(int, data))
cases = []

if len(vals) >= 2:
    n0 = vals[0]
    m0 = vals[1]
    if 2 + 3 * n0 == len(vals):
        cases.append((n0, m0, 2))
    else:
        t = n0
        ptr = 1
        for _ in range(t):
            n = vals[ptr]
            m = vals[ptr + 1]
            ptr += 2
            cases.append((n, m, ptr))
            ptr += 3 * n

out_lines = []

for n, m, start in cases:
    x = [0] * n
    y = [0] * n
    typ = [0] * n
    p = start
    for i in range(n):
        x[i] = vals[p]
        y[i] = vals[p + 1]
        typ[i] = vals[p + 2]
        p += 3

    rows = {}
    for i in range(n):
        rows.setdefault(y[i], []).append(i)

    row_seg = [0] * n
    R = 0
    for yy, idxs in rows.items():
        idxs.sort(key=lambda i: x[i])
        prev = None
        seg_id = None
        for i in idxs:
            if typ[i] != prev:
                seg_id = R
                R += 1
                prev = typ[i]
            row_seg[i] = seg_id

    cols = {}
    for i in range(n):
        cols.setdefault(x[i], []).append(i)

    col_seg = [0] * n
    C = 0
    for xx, idxs in cols.items():
        idxs.sort(key=lambda i: y[i])
        prev = None
        seg_id = None
        for i in idxs:
            if typ[i] != prev:
                seg_id = C
                C += 1
                prev = typ[i]
            col_seg[i] = seg_id

    total = R + C
    adj = [[] for _ in range(total)]
    U = [0] * n
    V = [0] * n
    deg = [0] * total

    for i in range(n):
        u = row_seg[i]
        v = R + col_seg[i]
        U[i] = u
        V[i] = v
        adj[u].append((v, i))
        adj[v].append((u, i))
        deg[u] += 1
        deg[v] += 1

    b = [0] * total
    for u in range(R):
        b[u] = deg[u] & 1

    need = b[:]
    yassign = [0] * n
    visited = [False] * total
    parent = [-1] * total
    parent_edge = [-1] * total

    ok = True

    for s in range(total):
        if deg[s] == 0 or visited[s]:
            continue
        stack = [s]
        visited[s] = True
        order = []
        while stack:
            v = stack.pop()
            order.append(v)
            for nei, e in adj[v]:
                if not visited[nei]:
                    visited[nei] = True
                    parent[nei] = v
                    parent_edge[nei] = e
                    stack.append(nei)

        for v in reversed(order):
            e = parent_edge[v]
            if e != -1:
                yassign[e] = need[v]
                need[parent[v]] ^= yassign[e]

        if need[s] != 0:
            ok = False
            break

    if not ok:
        out_lines.append("NO")
        continue

    assigned = [[] for _ in range(total)]
    for i in range(n):
        if yassign[i] == 0:
            assigned[U[i]].append(i)
        else:
            assigned[V[i]].append(i)

    pairs = []
    for node in range(total):
        lst = assigned[node]
        if len(lst) & 1:
            ok = False
            break
        for k in range(0, len(lst), 2):
            pairs.append((lst[k], lst[k + 1]))

    if not ok or len(pairs) * 2 != n:
        out_lines.append("NO")
        continue

    out_lines.append("YES")
    for a, b2 in pairs:
        out_lines.append(f"{a + 1} {b2 + 1}")

sys.stdout.write("\n".join(out_lines))
