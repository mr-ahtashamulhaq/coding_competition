def process_single_scenario(s):
    length = len(s)
    
    a_indices = [i for i, item in enumerate(s) if item == 'A']
    b_indices = [i for i, item in enumerate(s) if item == 'B']
    
    left = 0
    right = length - 1
    
    a_ptr = 0
    b_ptr = len(b_indices) - 1
    
    last_eater = None
    
 
    while True:

        a_moved = False
       
        while a_ptr < len(a_indices):
            pos = a_indices[a_ptr]
            if pos < left:
                
                a_ptr += 1
                continue
            if pos > right:
               break
            
            
            left = pos + 1
            a_ptr += 1
            last_eater = "Alice"
            a_moved = True
            break

  
        b_moved = False
    
        while b_ptr >= 0:
            pos = b_indices[b_ptr]
            if pos > right:
                
                b_ptr -= 1
                continue
            if pos < left:
                break

            right = pos - 1
            b_ptr -= 1
            last_eater = "Bob"
            b_moved = True
            break
            
        if not a_moved and not b_moved:
            break
            
    return last_eater

def run_solver():
        with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:
            t = int(f_in.readline())
            for case_num in range(1, t + 1):
                _ = f_in.readline().strip()
                line = f_in.readline().strip()
                
                result = process_single_scenario(line)
                f_out.write(f"Case #{case_num}: {result}\n")

if __name__ == "__main__":
    run_solver()