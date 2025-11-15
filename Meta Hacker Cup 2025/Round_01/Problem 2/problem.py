import collections

def check(h, n, heights):

    if n == 0:
        return True
        
    q = collections.deque()
    visited = [False] * n
    visited_count = 0

    for i in range(n):
        if heights[i] <= h:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                visited_count += 1
    

    while q:
        u_idx = q.popleft()


        v_idx = u_idx - 1
        if v_idx >= 0 and not visited[v_idx]:
            if abs(heights[u_idx] - heights[v_idx]) <= h:
                visited[v_idx] = True
                q.append(v_idx)
                visited_count += 1

        v_idx = u_idx + 1
        if v_idx < n and not visited[v_idx]:
            if abs(heights[u_idx] - heights[v_idx]) <= h:
                visited[v_idx] = True
                q.append(v_idx)
                visited_count += 1

    return visited_count == n

def solve_metal_platforms_ch2():
    try:
        with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
            num_test_cases = int(infile.readline())

            for case_num in range(1, num_test_cases + 1):
                n = int(infile.readline())
                heights = list(map(int, infile.readline().split()))

                low = 0
                high = 10**9 + 7 
                ans = high

                while low <= high:
                    mid = low + (high - low) // 2
                    if check(mid, n, heights):
                        ans = mid
                        high = mid - 1
                    else:
                      
                        low = mid + 1
                
                outfile.write(f"Case #{case_num}: {ans}\n")
        
        print("Successfully processed all test cases for Chapter 2. Results are in 'output.txt'.")

    except FileNotFoundError:
        print("Error: 'input.txt' not found. Please ensure the file exists in the same directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the solver for Chapter 2
if __name__ == "__main__":
    solve_metal_platforms_ch2()
