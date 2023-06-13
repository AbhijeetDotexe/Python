def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Example usage
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
element = 11

# Linear search
linear_result = linear_search(my_list, element)
print(f"Linear Search: {element} {'is' if linear_result else 'is not'} in the list.")

# Binary search
binary_result = binary_search(sorted(my_list), element)
print(f"Binary Search: {element} {'is' if binary_result else 'is not'} in the list.")
