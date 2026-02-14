# Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target. Return true if such a triplet exists, otherwise, return false.

# Examples:
# Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
# Output: true

# Explanation: The triplet {1, 4, 8} sums up to 13.
# Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10
# Output: true

# Explanation: The triplets {1, 3, 6} and {1, 2, 7} both sum to 10.
# Input: arr[] = [40, 20, 10, 3, 6, 7], target = 24
# Output: false

# Explanation: No triplet in the array sums to 24.
# Link: https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1

def find3Numbers(arr, target):
    # Sort the array
    arr.sort()

    # Traverse the array
    for i in range(len(arr) - 2):
        # Initialize two pointers
        left = i + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return False

# Example usage:
arr = [1, 4, 45, 6, 10, 8]
target = 13
result = find3Numbers(arr, target)
print(result)