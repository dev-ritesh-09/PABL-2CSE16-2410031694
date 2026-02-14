# Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in orted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

# Examples:
# Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
# Output: a[] = [2, 2, 3, 4], b[] = [7, 10]

# Explanation: After merging the two non-decreasing arrays, we get, [2, 2, 3, 4, 7, 10]
# Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
# Output: a[] = [1, 2, 3, 5, 8, 9], b[] = [10, 13, 15, 20]

# Explanation: After merging two sorted arrays we get [1, 2, 3, 5, 8, 9, 10, 13, 15, 20].
# Input: a[] = [0, 1], b[] = [2, 3]
# Output: a[] = [0, 1], b[] = [2, 3]

# Explanation: After merging two sorted arrays we get [0, 1, 2, 3].

# Constraints:
# 1 ≤ n, m ≤ 105
# 0 ≤ a[i], b[i] ≤ 107

# Link: https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1

from typing import List
class Solution:
    def merge(self, a: List[int], b: List[int]) -> None:
        n = len(a)
        m = len(b)

        for i in range(n):
            if a[i] > b[0]:
                a[i], b[0] = b[0], a[i]
                first = b[0]

                k = 1
                while k < m and b[k] < first:
                    b[k - 1] = b[k]
                    k += 1
                b[k - 1] = first

# Example usage:

solution = Solution()
a = [2, 4, 7, 10]
b = [2, 3]
solution.merge(a, b)

print("Merged a:", a)
print("Merged b:", b)   