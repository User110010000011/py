def minimum(arr):
    min_val=float('inf')
    for i in arr:
          if sum(i)<min_val:
              min_val=sum(i)
          else:
              pass
    return min_val
def sort_lists(arr:list,res:list):
     val=0
     if len(arr)<=0:
          return res
     else:
          pos=0
          min=minimum(arr)
          for i in arr:
               if sum(i)==min:
                  val=i
                  pos=arr.index(i)
               else:
                    pass
          res.append(val)
          if sum(val)==sum(res[-1]) and len(res)>=1:
               val_len=len(val)
               prev_len=len(res[-1])
               if val_len<prev_len:
                  res.insert(res.index(res[-1]),val)
          arr.pop(pos)
          return sort_lists(arr,res)

lists = [[5, 2], [1, 2, 3], [3, 3], [10],[6], [1, 1, 1, 1],[2,2],[4]]
res=sort_lists(lists,[])
print(res)

