# You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

# Note : A subarray is a continuous part of an array.

# Examples:
# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11

# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

# Link: practice.geeksforgeeks.org/problems/kadanes-algorithm/0

def max_subarray_sum(arr):
    max_num = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_num = max(max_num, max_ending_here)

    return max_num

# Example
arr = [2, 3, -8, 7, -1, 2, 3]
result = max_subarray_sum(arr)
print("The maximum sum of a subarray is:", result)