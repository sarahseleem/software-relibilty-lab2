def insertion_sort(array):
    index = 5.  # 5 instead of 1
    while index < len(array):
        current_position = index
        while (current_position > 0) and (array[current_position] < array[current_position - 1]):
            temp = array[current_position]
            array[current_position] = array[current_position - 1]
            array[current_position - 1] = temp
            current_position -= 1
        index += 1
    return array


def binary_search(key, array):
    left = 0
    right = len(array) - 1
    mid = (left + right) // 2

    while array[mid] != key and left <= right:
        if array[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    return array[mid] == key


def binary_sort_search_member(key, array):
    sorted_array = insertion_sort(array)
    print(sorted_array)
    return binary_search(key, sorted_array)
    
def test():
    print(insertion_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8])
    print(insertion_sort([1]) == [1])
    print(insertion_sort([]) == [])
    
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("\nTesting binary_search...")
    print(binary_search(5, sorted_array) == True)
    print(binary_search(10, sorted_array) == False)

    print("\nTesting binary_sort_search_member...")
    print(binary_sort_search_member(4, [5, 3, 8, 4, 2]) == True)
    print(binary_sort_search_member(10, [1, 2, 3, 4, 5]) == False)

test()
