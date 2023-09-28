def recursive_search(arr, target, index=0):
    """If the index is out of bounds, return -1 to indicate not found."""
    if index >= len(arr):
        return -1

    """If the current element is equal to the target, return its index."""
    if arr[index] == target:
        return index

    """Recursive case: Call the function with the next index."""
    return recursive_search(arr, target, index + 1)


my_list = [2, 4, 6, 8, 10, 12]
target_value = 8

result = recursive_search(my_list, target_value)
if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the list.")
