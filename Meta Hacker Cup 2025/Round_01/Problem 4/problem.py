MOD_VAL = 10**9 + 7
EXP_LIMIT = 65

fact_lookup = [1] * (EXP_LIMIT + 1)
inv_fact_lookup = [1] * (EXP_LIMIT + 1)

for i in range(1, EXP_LIMIT + 1):
    fact_lookup[i] = (fact_lookup[i-1] * i) % MOD_VAL

inv_fact_lookup[EXP_LIMIT] = pow(fact_lookup[EXP_LIMIT], MOD_VAL - 2, MOD_VAL)
for i in range(EXP_LIMIT - 1, -1, -1):
    inv_fact_lookup[i] = (inv_fact_lookup[i+1] * (i+1)) % MOD_VAL


def find_prime_components(n_in):

    prime_map = {}
    divisor_candidate = 2
    while divisor_candidate * divisor_candidate <= n_in:
        while n_in % divisor_candidate == 0:
            prime_map[divisor_candidate] = prime_map.get(divisor_candidate, 0) + 1
            n_in //= divisor_candidate
        divisor_candidate += 1
    if n_in > 1:
        prime_map[n_in] = prime_map.get(n_in, 0) + 1
    return prime_map

def count_sequences(target_prod, day_count):

    if target_prod == 1:
        return 1
    
    prime_map = find_prime_components(target_prod)
    way_sum = 1
    
    for prime, exponent in prime_map.items():
        num_val = 1
        day_term = day_count % MOD_VAL
        for i in range(exponent):
            num_val = (num_val * (day_term + i)) % MOD_VAL
        
        ways_for_term = (num_val * inv_fact_lookup[exponent]) % MOD_VAL
        way_sum = (way_sum * ways_for_term) % MOD_VAL
        
    return way_sum

divisor_collection = []
def generate_all_divisors(p_factors_as_list, idx, curr_div):

    if idx == len(p_factors_as_list):
        divisor_collection.append(curr_div)
        return

    prime, exponent = p_factors_as_list[idx]
    p_power = 1
    for i in range(exponent + 1):
        generate_all_divisors(p_factors_as_list, idx + 1, curr_div * p_power)
        p_power *= prime

def execute_solution():
        with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
            case_count = int(input_file.readline())

            for c_idx in range(1, case_count + 1):
                param_n, param_a, param_b = map(int, input_file.readline().split())
                
                global divisor_collection
                divisor_collection = []
                b_prime_map = find_prime_components(param_b)
                b_prime_list = list(b_prime_map.items())
                generate_all_divisors(b_prime_list, 0, 1)
                
                total_sequences = 0
                for div_val in divisor_collection:
                    if div_val <= param_a:
                        seq_count1 = count_sequences(div_val, param_n)
                        seq_count2 = count_sequences(param_b // div_val, param_n)
                        total_sequences = (total_sequences + seq_count1 * seq_count2) % MOD_VAL
                
                output_file.write(f"Case #{c_idx}: {total_sequences}\n")
                
if __name__ == "__main__":
    execute_solution()