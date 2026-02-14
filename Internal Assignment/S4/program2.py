# Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.

# Examples:
# Input: n = 5
# Output: [1, 2, 0]

# Explanation: 5! = 1*2*3*4*5 = 120

# Input: n = 10
# Output: [3, 6, 2, 8, 8, 0, 0]

# Explanation: 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800
# Input: n = 1
# Output: [1]

# Explanation: 1! = 1
# Link: https://www.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1

class Solution:
    def factorial(self, n):
        result = [1]  # Start with 0! = 1
        
        for i in range(2, n + 1):
            carry = 0
            for j in range(len(result)):
                temp = result[j] * i + carry
                result[j] = temp % 10 
                carry = temp // 10 
            
            while carry > 0:
                result.append(carry % 10)
                carry //= 10
        
        return result[::-1]
    
# Example usage:
solution = Solution()
n = 10
print(solution.factorial(n))    