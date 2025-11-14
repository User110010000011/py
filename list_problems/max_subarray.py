# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray [-2] has the largest sum -2.

# Input: arr[] = [5, 4, 1, 7, 8]
# Output: 25
# Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.

arr =  [2, 3, -8, 7, -1, 2, 3]
maxending=arr[0]
res=arr[0]
for i in range(1,len(arr)):
    maxending=max(maxending+arr[i],arr[i])
    res=max(res,maxending)

print(res)
