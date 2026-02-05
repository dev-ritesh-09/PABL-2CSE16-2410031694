# 1. Sort the elements
# 2. result = a[-1] - a[0]
# 3. Lower tower -> +k and Taller tower -> -k
# 4. Should not negatgive
# 5. Compute possible min differnce 

# Input : k = 2, arr[] = {3, 9, 12, 16, 20}
# Output : 
# Explanation : The array can be modified as
# {3, 3, 6, 8}. The difference between the
# largest and the smallest is 8-3 = 5.

def minimum_height(arr, k):

    arr.sort()

    n = len(arr)
    result = arr[n-1] - arr[0]

    for i in range(1, n):
        if arr[i] >= k:
            min_height = min(arr[0] + k, arr[i] - k)
            max_height = max(arr[i-1] + k, arr[n-1] - k)
            result = min(result, max_height - min_height)

    return result

# Example usage
arr = [3, 9, 12, 16, 20]
k = 3
print("Minimum possible difference is:", minimum_height(arr, k))