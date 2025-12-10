import sys

t = int(sys.stdin.readline())
for _ in range(t):
    x, y, z = map(int, sys.stdin.readline().split())
    n = x + y + z
    
    if max(x, y, z) > (n + 1) // 2:
        print("NO")
        continue
    
    def can_place(c, res, cnt):
        if cnt[c] == 0:
            return False
        if len(res) > 0 and res[-1] == c:
            return False
        if len(res) >= 2:
            if res[-2] == 'M' and res[-1] == 'I' and c == 'T':
                return False
            if res[-2] == 'T' and res[-1] == 'I' and c == 'M':
                return False
        return True
    
    orders = [['M','I','T'], ['M','T','I'], ['I','M','T'], ['I','T','M'], ['T','M','I'], ['T','I','M']]
    found = False
    
    for order in orders:
        res = []
        cnt = {'M': x, 'I': y, 'T': z}
        ok = True
        
        for i in range(n):
            placed = False
            for c in order:
                if can_place(c, res, cnt):
                    res.append(c)
                    cnt[c] -= 1
                    placed = True
                    break
            
            if not placed:
                ok = False
                break
        
        if ok and len(res) == n:
            print("YES")
            print(''.join(res))
            found = True
            break
    
    if not found:
        res = []
        cnt = {'M': x, 'I': y, 'T': z}
        ok = True
        
        for i in range(n):
            candidates = []
            for c in ['M', 'I', 'T']:
                if can_place(c, res, cnt):
                    candidates.append((cnt[c], c))
            
            if not candidates:
                ok = False
                break
            
            candidates.sort(reverse=True)
            best = candidates[0][1]
            res.append(best)
            cnt[best] -= 1
        
        if ok and len(res) == n:
            print("YES")
            print(''.join(res))
        else:
            print("NO")
