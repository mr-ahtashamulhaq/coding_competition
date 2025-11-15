def solve_scaling_coolness():
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        num_test_cases = int(infile.readline())

        for case_num in range(1, num_test_cases + 1):
            n, a, b = map(int, infile.readline().split())
            
            coolness_after_n_days = 1
            for i in range(a, 0, -1):
                if b % i == 0:
                    coolness_after_n_days = i
                    break
            
            coolness_last_n_days = b // coolness_after_n_days

            multipliers = [coolness_after_n_days] + [1] * (n - 1)
            multipliers += [coolness_last_n_days] + [1] * (n - 1)
            
            result_str = ' '.join(map(str, multipliers))
            outfile.write(f"Case #{case_num}: {result_str}\n")

if __name__ == "__main__":
    solve_scaling_coolness()