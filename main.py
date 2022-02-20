def linear_search(num_list,num_to_find):
    for i, elem in enumerate(num_list):
        if elem == num_to_find:
            return i
    return -1

def binary_search(num_list,num_to_find):
    right_index = 0
    left_index = len(num_list) - 1

    while right_index <= left_index:
        mid_index = (right_index + left_index) // 2
        mid_number = num_list[mid_index]

        if num_to_find == mid_number:
            return mid_index
        elif num_to_find > mid_number:
            right_index = mid_index + 1
        elif num_to_find < mid_number:
            left_index = mid_index - 1
    return -1

def binary_search_recursive(num_list,num_to_find,left_idx, right_idx):
    if num_to_find < right_idx or num_to_find > left_idx:
        return -1

    mid_idx = (left_idx + right_idx) // 2
    mid_num = num_list[mid_idx]

    if num_to_find == mid_num:
        return mid_idx
    elif num_to_find > mid_num:
        right_idx = mid_idx + 1
    elif num_to_find < mid_num:
        left_idx = mid_idx - 1

    #new_list = num_list[num_list[right_idx]:left_idx+1]

    return binary_search_recursive(num_list,num_to_find,left_idx,right_idx)

if __name__=='__main__':

    number_list=[i for i in range(10)]
    print(number_list)
    find = 10

    idx = linear_search(number_list, find)
    print(f'Linear Search: Integer value found at index: {idx}')

    idx = binary_search(number_list, find)
    print(f'Binary Search: Integer value found at index: {idx}')

    idx = binary_search_recursive(number_list, find, len(number_list) - 1, 0)
    print(f'Binary Search Recursive: Integer value found at index: {idx}')