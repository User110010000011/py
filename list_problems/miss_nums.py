arr=[1,2,4,5,6,15,27]
sum=0
prev_num_arr=[]
# basic_diff=1
val=0
for i in range(1,len(arr)):
  res=arr[i]-arr[i-1]
  if res<=1:
    sum+=res
    #  print(f"sum:{sum}")
  elif res>1:
    count=1
    while count<res:
      prev_num_arr.append(arr[i]-count)
      count+=1
print(sorted(prev_num_arr))    


         