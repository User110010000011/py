"""this is a merge deep funvtion"""
# You have two nested dictionaries:
# 👉 Merge them recursively so that values from b overwrite or extend a.
# Expected Output:
# {
#   "user": {"name": "John", "age": 30, "email": "john@example.com"},
#   "status": "active",
#   "role": "admin"}
def merge_deep(a,b,key:list):
    """this is a method for """
    if len(key)<=0:
        return a

    i=0
    if key[i] in a and key[i] in b:
                #    a[key[i]]=b[key[i]]
        if isinstance(b[key[i]],dict):
            for k,v in b[key[i]].items():
                        #   print(k,a[key[i]])
                if k in a[key[i]] and k in b[key[i]]:
                    a[key[i]][k]=b[key[i]][k]
                else:
                    a[key[i]].update({k:v})
    else:
        a.update({key[i]:b[key[i]]})
        b.pop(key[i])
        key.pop(key.index(key[i]))
        return merge_deep(a,b,key)  
alist = {"user": {"name": "John", "age": 25},"status":"active"}
blist = {"user": {"age": 49, "email": "john@example.com"}, "role": "admin"}
# for k,v in b.items():
#      if k in a :
#           for key,val in v.items():
#              if key in a[k] and key in b[k]:
#                a[k][key]=b[k][key]
#              else:
#                  a[k].update({key:b[k][key]})
#      else:
#          a.update({k:b[k]})
print(merge_deep(alist,blist,list(blist.keys())))
