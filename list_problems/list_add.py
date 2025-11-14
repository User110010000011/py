""" 
"""
# arr2=sorted(arr,key=lambda x:sum(x))
# print(arr2)
def mid_index(arr2,start,last):
    """it is used to find the middle element"""
    if last<=start:
        return last
    else:
        start+=1
        last-=1
        return mid_index(arr2,start,last)
def  maximum(arr3):
    """used to find maximum of list of list's sum."""
    max_sum=float('-inf') # float('-inf')=+infinity ,float('-inf')=-infinity
    for i in arr3:
        if sum(i)>max_sum:
            max_sum=sum(i)
        else:
            pass
    return max_sum
def min_list(arr1,res1):
    """it return the sorted in descending order."""
    if len(arr1)<=0:
        return  res1
    else:
        pos=0
        val=None
        max1=maximum(arr1)
        for i in arr:
            if sum(i)==max1:
                val=i
                pos=arr1.index(i)
            else:
                pass
        res.append(val)
        arr.pop(pos)
        return min_list(arr1,res)

arr = [[5, 2],[1, 9, 3],[10, 0, -1],[1,9,4],[4],[1]]
res=min_list(arr,[])
mid=mid_index(res,0,len(res)-1)
print(res)
print("mid element:",res[mid])
# print(arr.index([1,9,3]))
