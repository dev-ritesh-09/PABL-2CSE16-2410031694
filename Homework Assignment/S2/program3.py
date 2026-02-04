# You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

# For example:
# • If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
# • If arr[i] = 0, you cannot jump forward from that position.

# Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.
# Note: Return -1 if you can't reach the end of the array.

# Examples :
# Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# Output: 3

# Explanation: First jump from 1st element to 2nd element with value 3. From here
# we jump to 5th element with value 9, and from here we will jump to the last.

# Link: https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

def min_jumps(arr):
    n = len(arr)
    if n == 0 or arr[0] == 0:
        return -1

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

            if current_end >= n - 1:
                break

    return jumps if current_end >= n - 1 else -1

# Example usage:
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
result = min_jumps(arr)
print("Minimum number of jumps to reach the end is:", result)