# Given three sorted arrays in non-decreasing order, print all common elements in non-decreasing order across these arrays. If there are no such elements return an empty array. In this case, the output will be -1.

# Note: can you handle the duplicates without using any additional Data Structure?

# Examples :
# Input: arr1 = [1, 5, 10, 20, 40, 80] , arr2 = [6, 7, 20, 80, 100] , arr3 = [3, 4, 15, 20,
# 30, 70, 80, 120]
# Output: [20, 80]

# Explanation: 20 and 80 are the only common elements in arr1, arr2 and arr3.
# Input: arr1 = [1, 2, 3, 4, 5] , arr2 = [6, 7] , arr3 = [8,9,10]
# Output: [-1]

# Explanation: There are no common elements in arr1, arr2 and arr3.
# Input: arr1 = [1, 1, 1, 2, 2, 2], arr2 = [1, 1, 2, 2, 2], arr3 = [1, 1, 1, 1, 2, 2, 2, 2]
# Output: [1, 2]

# Explanation: We do not need to consider duplicates

#Link: https://www.geeksforgeeks.org/problems/common-elements1132/1

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i = j = k = 0
        common = []
        
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                if not common or common[-1] != arr1[i]:  # Avoid duplicates
                    common.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
        return common if common else [-1]
    
# Example usage:

solution = Solution()
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(solution.commonElements(arr1, arr2, arr3))