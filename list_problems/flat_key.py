# Transform Flat Keys to Nested Dict
# Problem:
# Convert this:
flat = {
    "user.name": "John",
    "user.email": "john@example.com",
    "address.city": "Austin",
    "address.zip": "73301"}
# # 👉 Into:
# {
#   "user": {"name": "John", "email": "john@example.com"},
#   "address": {"city": "Austin", "zip": "73301"}
# }

res_dict={}
visited=set()
for k,v in flat.items(): 
    arr=[]     
    arr=k.split(".") 
    # print(arr)
    val_dict={}
    # print(arr[0],arr[1])
    if  arr[0] not in visited :
         # visited.add(arr[0])
        visited.add(arr[0])
        val_dict[arr[1]]=v
        res_dict[arr[0]]=val_dict        
    else:
        val_dict.update({arr[1]:v})
        res_dict[arr[0]].update(val_dict)
   

print(res_dict)
