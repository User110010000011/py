data = [10, '5', '20', 3, '100']
arr=[int(i) for i in data]
print(f"before sort:{arr}")
# print(sorted(arr))
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
res=[]
for i in range(len(arr)):
    if arr[i] in data:
        res.append(arr[i])
    else:
       res.append(str(arr[i]))

print(f"after sort:{res}")
