# Linear Search
def linear_search_unsorted(arr, target):
    steps = 0
    for num in arr:
        steps += 1
        if num == target:
            return [num, steps]
    return [target, "Not found"]


# Binary Search
def binary_search_unsorted(arr, target):
    steps = 0
    low = 0
    # sorted_arr = sorted(arr)
    high = len(arr) - 1
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return [target, "NOT FOUND"]

# Scenario 1 Test

unsorted_list = [42, 15, 7, 30, 22, 10, 18]
target_1 = 30
result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)
print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")