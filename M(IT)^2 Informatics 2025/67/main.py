import sys
import math

def ask(i, j):
    sys.stdout.write(f"? {i} {j}\n")
    sys.stdout.flush()
    line = sys.stdin.readline()
    if not line:
        sys.exit()
    x = int(line.strip())
    if x == -1:
        sys.exit()
    return x

def answer(arr):
    sys.stdout.write("! " + " ".join(map(str, arr)) + "\n")
    sys.stdout.flush()

def solve(n):
    a = [0] * (n + 1)
    r = n % 3

    if r == 0:
        for s in range(1, n + 1, 3):
            i, j, k = s, s + 1, s + 2
            p1 = ask(i, j)
            p2 = ask(i, k)
            ai = math.gcd(p1, p2)
            a[i] = ai
            a[j] = p1 // ai
            a[k] = p2 // ai

    elif r == 1:
        m = n // 3
        tcnt = m - 1
        end_triples = 3 * tcnt
        s = 1
        for _ in range(tcnt):
            i, j, k = s, s + 1, s + 2
            p1 = ask(i, j)
            p2 = ask(i, k)
            ai = math.gcd(p1, p2)
            a[i] = ai
            a[j] = p1 // ai
            a[k] = p2 // ai
            s += 3

        idx = list(range(end_triples + 1, n + 1))
        x1, x2, x3, x4 = idx[0], idx[1], idx[2], idx[3]
        p12 = ask(x1, x2)
        p13 = ask(x1, x3)
        p24 = ask(x2, x4)
        ax1 = math.gcd(p12, p13)
        a[x1] = ax1
        a[x2] = p12 // ax1
        a[x3] = p13 // ax1
        a[x4] = p24 // a[x2]

    else:
        m = n // 3
        end_triples = 3 * m
        s = 1
        for _ in range(m):
            i, j, k = s, s + 1, s + 2
            p1 = ask(i, j)
            p2 = ask(i, k)
            ai = math.gcd(p1, p2)
            a[i] = ai
            a[j] = p1 // ai
            a[k] = p2 // ai
            s += 3

        x = end_triples + 1
        y = end_triples + 2
        pivot = 1
        ppx = ask(pivot, x)
        ppy = ask(pivot, y)
        a[x] = ppx // a[pivot]
        a[y] = ppy // a[pivot]

    return a[1:]

def main():
    line = sys.stdin.readline()
    if not line:
        return
    t = int(line.strip())
    for _ in range(t):
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
        arr = solve(n)
        answer(arr)

if __name__ == "__main__":
    main()
