# Given an array arr, rotate the array by one position in clockwise direction.

# Examples:
# Input: arr[] = [1, 2, 3, 4, 5]
# Output: [5, 1, 2, 3, 4]

# Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.

# Link: https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1

"""
def rotate_array_clockwise(arr):
    if not arr:
        return arr
    
    # Store the last element
    last = arr[-1]
    
    # Shift all elements to the right by one position
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    
    # Place the last element at the first position
    arr[0] = last
    
    return arr

# Example
arr = [1, 2, 3, 4, 5]
rotated_arr = rotate_array_clockwise(arr)
print("Rotated Array:", rotated_arr)

"""

"""
def rotate_array_anticlockwise(arr):
    if not arr:
        return arr
    
    # Store the first element
    first = arr[0]
    
    # Shift all elements to the left by one position
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]
    
    # Place the first element at the last position
    arr[-1] = first
    
    return arr

# Example
arr = [1, 2, 3, 4, 5]
rotated_arr = rotate_array_anticlockwise(arr)
print("Rotated Array:", rotated_arr)    

"""

"""

# Rotate array in clockwise direction k times
def rotate_array_clockwise_k_times(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    
    k = k % n  # In case k is greater than n
    
    for _ in range(k):
        last = arr[-1]
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last
    return arr

# Example
arr = [1, 2, 3, 4, 5]
k = 2
rotated_arr = rotate_array_clockwise_k_times(arr, k)
print("Rotated Array by", k, "times:", rotated_arr)

"""

# Rotate array in anticlockwise direction k times
def rotate_array_anticlockwise_k_times(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    
    k = k % n  # In case k is greater than n
    
    for _ in range(k):
        first = arr[0]
        for i in range(n - 1):
            arr[i] = arr[i + 1]
        arr[-1] = first
    return arr  

# Example
arr = [1, 2, 3, 4, 5]
k = 2
rotated_arr = rotate_array_anticlockwise_k_times(arr, k)
print("Rotated Array by", k, "times:", rotated_arr)