import sys

sys.setrecursionlimit(1_000_000)
rd = sys.stdin.readline

n, m = map(int, rd().split())

g1 = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, rd().split())
    g1[a].append(b)
    g1[b].append(a)

g2 = [[] for _ in range(m + 1)]
for _ in range(m - 1):
    a, b = map(int, rd().split())
    a -= n
    b -= n
    g2[a].append(b)
    g2[b].append(a)


def ask(a, b, c, d):
    print("?", a, b, c, d)
    sys.stdout.flush()
    x = int(rd())
    if x == -1:
        sys.exit()
    return x


def cen(g, st, rm):
    pa = {st: 0}
    stc = [st]
    ord = []
    while stc:
        u = stc.pop()
        ord.append(u)
        for v in g[u]:
            if rm[v] or v == pa[u]:
                continue
            pa[v] = u
            stc.append(v)

    sz = {}
    for u in ord[::-1]:
        s = 1
        for v in g[u]:
            if not rm[v] and pa.get(v) == u:
                s += sz[v]
        sz[u] = s

    tot = sz[st]
    c = ord[0]
    best = tot + 1
    for u in ord:
        mx = tot - sz[u]
        for v in g[u]:
            if not rm[v] and pa.get(v) == u:
                if sz[v] > mx:
                    mx = sz[v]
        if mx < best:
            best = mx
            c = u
    return c


def sol(g, st, off, an, rm):
    def go(x):
        c = cen(g, x, rm)
        nb = [v for v in g[c] if not rm[v]]

        if not nb:
            return c

        if len(nb) == 1:
            if ask(nb[0] + off, an, c + off, c + off) == 0:
                rm[c] = True
                return go(nb[0])
            return c

        if len(nb) == 2:
            x = ask(nb[0] + off, an, nb[1] + off, c + off)
            if x == 0:
                rm[c] = True
                return go(nb[0])
            if x > 1:
                rm[c] = True
                return go(nb[1])
            return c

        if len(nb) == 3:
            x = ask(nb[0] + off, an, nb[1] + off, c + off)
            if x == 0:
                rm[c] = True
                return go(nb[0])
            if x > 1:
                rm[c] = True
                return go(nb[1])
            y = ask(nb[2] + off, an, nb[0] + off, c + off)
            if y == 0:
                rm[c] = True
                return go(nb[2])
            return c

        x = ask(nb[0] + off, an, nb[1] + off, c + off)
        if x == 0:
            rm[c] = True
            return go(nb[0])
        if x > 1:
            rm[c] = True
            return go(nb[1])

        y = ask(nb[2] + off, an, nb[3] + off, c + off)
        if y == 0:
            rm[c] = True
            return go(nb[2])
        if y > 1:
            rm[c] = True
            return go(nb[3])
        return c

    return go(st)


r1 = [False] * (n + 1)
u = sol(g1, 1, 0, n + 1, r1)

r2 = [False] * (m + 1)
v = sol(g2, 1, n, u, r2) + n

print("!", u, v)
sys.stdout.flush()