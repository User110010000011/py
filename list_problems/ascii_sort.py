# # sort based on ascii order input:["apple", "bat", "ball", "ant"] output:['apple','ant',ball,bat]
# a="apple"
# # arr=["apple", "bat", "ball","cat", "ant"]
# sum(),min()
arr=["apple", "bat", "ball","cat", "ant","anc","ancple","baz","bad","anble","a"]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        start=0
        if ord(arr[i][start])>ord(arr[j][start]):
                arr[i],arr[j]=arr[j],arr[i]
        elif ord(arr[i][start])==ord(arr[j][start]):
                min_val=min(len(arr[i][start]),len(arr[j][start]))     
                while start<min_val:
                     if ord(arr[i][start])==ord(arr[i][start]):
                        start+=1
                     else:
                        break
                arr[i],arr[j]=arr[j],arr[i]

                                                  
print(arr)

# arr1=[1,"banyan",6]
# arr3=[2,"mangroves",9]
# print(arr1+arr3) #[1, 'banyan', 6, 2, 'mangroves', 9]


#other method
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]  # choose first element as pivot
#     left  = [x for x in arr[1:] if x <= pivot]
#     right = [x for x in arr[1:] if x > pivot]
#     return quicksort(left) + [pivot] + quicksort(right)

# arr = ["apple","bat","ball","cat","ant","anc","ancple","baz","bad","anble","a"]
# print(quicksort(arr))


# arr = ["apple","bat","ball","cat","ant","anc","ancple","baz","bad","anble","a"]

# res = []
# while arr:
#     m = min(arr)   # find lexicographically smallest
#     res.append(m)
#     arr.remove(m)
# print(res)
