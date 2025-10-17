from collections import defaultdict, deque

def solve():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    ptr = 0
    m = int(lines[ptr].strip())
    ptr += 1
    
    results = []
    
    for tc in range(1, m + 1):
        sz = int(lines[ptr].strip())
        ptr += 1
        p = list(map(int, lines[ptr].strip().split()))
        ptr += 1
        q = list(map(int, lines[ptr].strip().split()))
        ptr += 1
        
        if any(q[k] < p[k] for k in range(sz)):
            results.append(f"Case #{tc}: -1")
            continue
        
        freq = defaultdict(int)
        for val in p:
            freq[val] += 1
        
        uniq = set(q)
        flag = False
        for val in uniq:
            if freq[val] == 0:
                flag = True
                break
        
        if flag:
            results.append(f"Case #{tc}: -1")
            continue
        
        grp = defaultdict(list)
        for k, val in enumerate(q):
            grp[val].append(k)
        
        pos = defaultdict(deque)
        for k, val in enumerate(p):
            pos[val].append(k)
        
        moves = []
        
        for val in sorted(grp.keys()):
            if not pos[val]:
                flag = True
                break
            src = pos[val][0]
            for k in grp[val]:
                if p[k] == val:
                    continue
                moves.append((src + 1, k + 1))
                p[k] = val
                pos[val].append(k)
        
        if flag:
            results.append(f"Case #{tc}: -1")
        else:
            output = [f"Case #{tc}: {len(moves)}"]
            for a, b in moves:
                output.append(f"{a} {b}")
            results.append('\n'.join(output))
    
    with open('output.txt', 'w') as f:
        f.write('\n'.join(results))

if __name__ == "__main__":
    solve()