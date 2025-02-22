from random import randint
import random
from sort import binary_sort_search_member
from Mutation_5 import binary_sort_search_member_fail

def generate_pairwise_test_cases(num_elements=100, highest=1000, lowest=1):
    original_values = [randint(lowest, highest) for _ in range(num_elements)]
    mutated_values = []
    test_cases = []
    
    for i in range(num_elements):
        new_value = randint(lowest, highest)
        while new_value == original_values[i]:
            new_value = randint(lowest, highest)
        mutated_values.append(new_value)
    
    test_cases.append(original_values)
    
    for i in range(num_elements):
        new_test_case = original_values[:i] + [mutated_values[i]] + original_values[i+1:]
        test_cases.append(new_test_case)
    
    for i in range(num_elements):
        for j in range(i + 1, num_elements):
            new_test_case = (
                original_values[:i] + [mutated_values[i]] +
                original_values[i+1:j] + [mutated_values[j]] +
                original_values[j+1:]
            )
            test_cases.append(new_test_case)
    
    return test_cases

def test_mutation():
    test_case_index = 1
    while True:
        test_cases = generate_pairwise_test_cases()
        search_key = 0
        
        for test_case in test_cases:
            test_case_copy = test_case[:]
            
            if search_key == 0:
                random_index = random.randint(0, 7)
                search_key = test_case[random_index]
                print("The key is", search_key)
            
            correct_result = binary_sort_search_member(search_key, test_case)
            mutated_result = binary_sort_search_member_fail(search_key, test_case_copy)
            
            if correct_result == mutated_result:
                test_case_index += 1
            else:
                print(f"Mismatch found: Expected {correct_result}, but got {mutated_result}")
                print(f"Mutation detected on test case {test_case_index}")
                return

test_mutation()
