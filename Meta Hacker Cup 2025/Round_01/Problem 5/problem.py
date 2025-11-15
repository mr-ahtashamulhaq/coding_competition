from collections import defaultdict

def perform_complex_calculation(input_data_structure):
    size_of_input = len(input_data_structure)
    final_numeric_result = 0
    
    frequency_map_container = defaultdict(int)
    index_aggregation_map = defaultdict(int)
    
    frequency_map_container[0] = 1
    index_aggregation_map[0] = -1
    
    running_xor_accumulator = 0
    for loop_iterator_variable in range(size_of_input):
        running_xor_accumulator ^= input_data_structure[loop_iterator_variable]

        occurrence_count = frequency_map_container[running_xor_accumulator]
        summed_index_value = index_aggregation_map[running_xor_accumulator]

        arithmetic_series_sum = (loop_iterator_variable + 1) * (loop_iterator_variable + 2) // 2
        deductible_length_sum = occurrence_count * loop_iterator_variable - summed_index_value
        non_zero_xor_sum_cost_part = arithmetic_series_sum - deductible_length_sum

        zero_xor_sum_cost_part = (occurrence_count * loop_iterator_variable - summed_index_value - occurrence_count) - (occurrence_count * (occurrence_count - 1) // 2)

        current_iteration_cost_value = non_zero_xor_sum_cost_part + zero_xor_sum_cost_part
        final_numeric_result += current_iteration_cost_value

        frequency_map_container[running_xor_accumulator] += 1
        index_aggregation_map[running_xor_accumulator] += loop_iterator_variable

    return final_numeric_result

def execute_primary_workflow():
    with open('input.txt', 'r') as input_file_handle, open('output.txt', 'w') as output_file_handle:
        number_of_scenarios = int(input_file_handle.readline())
        for case_counter in range(1, number_of_scenarios + 1):
            array_length_from_file = int(input_file_handle.readline())
            numeric_list_from_file = list(map(int, input_file_handle.readline().split()))
            value_to_write = perform_complex_calculation(numeric_list_from_file)
            output_file_handle.write(f"Case #{case_counter}: {value_to_write}\n")


if __name__ == "__main__":
    execute_primary_workflow()

