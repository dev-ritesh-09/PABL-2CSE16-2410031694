# Input : arr [] = [100, 17, 36, 25, 19, 7, 3, 2, 1]
# K = 4
# Output : 7

# Solve using heap

# Importing necessary libraries
import heapq

def kth_smallest(arr, k):

    # Print the original array
    print("Original Array:", arr)

    # Check if k is within the valid range
    if k > len(arr):
        return None
    
    # Create a min-heap from the array
    heapq.heapify(arr)
    print("Min Heap:", arr)
    
    # Pop the smallest element from the heap k-1 times
    for _ in range(k - 1):
        heapq.heappop(arr)
        print(f"Heap after popping {_ + 1} time(s):", arr)

    return heapq.heappop(arr)

# Example usage
arr = [100, 17, 36, 25, 19, 7, 3, 2, 1]
k = 4
result = kth_smallest(arr, k)
print(f"The {k}-th smallest element is: {result}")  