import sys
import math
import bisect

def solve_case(a):
    vals = sorted(set(a))
    k = len(vals)
    maxv = vals[-1]

    pre = []
    cur = 1
    for v in vals:
        cur = cur // math.gcd(cur, v) * v
        if cur > maxv:
            cur = maxv + 1
        pre.append(cur)

    suf = [0] * (k + 1)
    g = 0
    for i in range(k - 1, -1, -1):
        g = vals[i] if g == 0 else math.gcd(g, vals[i])
        suf[i] = g

    for i in range(k):
        X = pre[i]
        if X == maxv + 1:
            break

        j = bisect.bisect_left(vals, X) - 1
        if j >= 0:
            Lsmall = pre[j]
            if Lsmall == maxv + 1 or X % Lsmall != 0:
                continue

        idx_gt = bisect.bisect_right(vals, X)
        if idx_gt < k and suf[idx_gt] % X != 0:
            continue

        return X

    return -1

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx + n]))
        idx += n
        out.append(str(solve_case(arr)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
