# Linear Search
def linear_search_last_occurrence(arr, target):
    count = 0
    for i in range(len(arr) - 1, -1, -1):
        count += 1
        if arr[i] == target:
            return [i, count]
    return "Not found"

# Binary Search
def binary_search_last_occurrence(arr, target):
    count = 0
    low = 0
    high = len(arr)
    last_occur = -1
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            last_occur = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last_occur, count

# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40, 10, 10]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")