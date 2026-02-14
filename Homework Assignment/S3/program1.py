# You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

# For example:
# If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
# If arr[i] = 0, you cannot jump forward from that position.

# Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

# Note: Return -1 if you can't reach the end of the array.

# Examples:
# Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# Output: 3
# Explanation: Jump to index 1 (value 3), then to index 4 (value 9), then to the last index.

# Input: arr = [1, 4, 3, 2, 6, 7]
# Output: 2
# Explanation: Jump to index 1, then jump to the last element.

# Input: arr = [0, 10, 20]
# Output: -1
# Explanation: Cannot move from the first element.

# Constraints:
# 2 ≤ arr.size() ≤ 10^5
# 0 ≤ arr[i] ≤ 10^5

def minJumps(arr):

    n = len(arr)
    
    # If first element is 0, can't move forward
    if arr[0] == 0:
        return -1
    
    # If array has only one element, already at the end
    if n == 1:
        return 0
    
    jumps = 0
    current_max = 0  # Farthest index reachable with current jumps
    next_max = 0     # Farthest index reachable with one more jump
    
    for i in range(n - 1):
        next_max = max(next_max, i + arr[i])
        
        # If we've reached the farthest index with current jumps
        if i == current_max:
            jumps += 1
            current_max = next_max
            
            # If we can reach or pass the last index
            if current_max >= n - 1:
                return jumps
    
    return -1

# Example usage:
arr1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(arr1))