# Find max and min of an give array without using built-in functions.

class solution:
    def max_min(self, arr):
        if len(arr) == 0:
            return None, None  # Handle empty array case

        max_val = arr[0]
        min_val = arr[0]

        for num in arr:
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num

        return max_val, min_val
    
obj = solution()

arr = [1, 2, 3, 4, 5]

result = obj.max_min(arr)
print("Max and Min:", result)