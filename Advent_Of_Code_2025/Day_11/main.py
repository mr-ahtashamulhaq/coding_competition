from functools import cache

D = open("input.txt").read()
E = {}

for line in D.splitlines():
    x, ys = line.split(':')
    ys = ys.split()
    E[x] = ys

@cache
def part1(x):
    if x=='out':
        return 1
    else:
        return sum(part1(y) for y in E[x])

@cache
def part2(x, seen_dac, seen_fft):
    if x=='out':
        return 1 if seen_dac and seen_fft else 0
    else:
        ans = 0
        for y in E[x]:
            new_seen_dac = seen_dac or y=='dac'
            new_seen_fft = seen_fft or y=='fft'
            ans += part2(y, new_seen_dac, new_seen_fft)
        return ans

print(f"Part 1 : {part1('you')}")
print(f"Part 2 : {part2('svr', False, False)}")