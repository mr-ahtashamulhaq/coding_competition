def compute(sz, heights):
    if sz == 1:
        return 0
    
    max_diff = 0
    for idx in range(sz - 1):
        diff = abs(heights[idx] - heights[idx + 1])
        max_diff = max(max_diff, diff)
    
    return max_diff


def runner():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    
    line_idx = 0
    num_cases = int(data[line_idx].strip())
    line_idx += 1
    
    output_lines = []
    
    for case_id in range(1, num_cases + 1):
        sz = int(data[line_idx].strip())
        line_idx += 1
        heights = list(map(int, data[line_idx].strip().split()))
        line_idx += 1
        
        result = compute(sz, heights)
        output_lines.append(f"Case #{case_id}: {result}")
    
    with open('output.txt', 'w') as f:
        f.write('\n'.join(output_lines))
    
    print("Done!")


if __name__ == "__main__":
    runner()