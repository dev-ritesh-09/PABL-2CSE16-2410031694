# Given an array arr[]. The task is to find the largest element and return it.

# Examples:

# Input: arr[] = [1, 8, 7, 56, 90]
# Output: 90

# Explanation: The largest element of the given array is 90.

# Link: https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-element-in-array


class Solution:
    def largest_element(self, arr):
        if not arr:
            return None  # Handle empty array case

        largest = arr[0]  # Assume the first element is the largest

        for num in arr:
            if num > largest:
                largest = num  # Update largest if current number is greater

        return largest

obj = Solution()   

arr = [1, 8, 7, 56, 90]

result = obj.largest_element(arr)
print("Largest element in the array:", result)