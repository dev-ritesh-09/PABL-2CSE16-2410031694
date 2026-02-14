# Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

# Examples:
# Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
# Output: true

# Explanation: b[] is a subset of a[]
# Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
# Output: true

# Explanation: b[] is a subset of a[]
# Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
# Output: false

# Explanation: b[] is not a subset of a[]

# Link: https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1

def isSubset(a, b):
    # Sort both arrays
    a.sort()
    b.sort()

    # Initialize pointers for both arrays
    i = 0
    j = 0

    # Traverse both arrays
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] == b[j]:
            i += 1
            j += 1
        else:
            return False

    # If we have traversed all elements of b, then it is a subset of a
    return j == len(b)

# Example usage:
a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]
result = isSubset(a, b)
print(result)