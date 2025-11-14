# Group by Multiple Keys
# Problem:
# Group this list of dicts by both department and role:
records = [
    {"name": "Alice", "department": "IT", "role": "Developer"},
    {"name": "Bob", "department": "HR", "role": "Recruiter"},
    {"name": "Eve", "department": "IT", "role": "Developer"},
    {"name": "John", "department": "IT", "role": "Manager"},
     {"name": "CJ", "department": "HR", "role": "Recruiter"}
]
# Expected Output:
# {
#   ("IT", "Developer"): ["Alice", "Eve"],
#   ("HR", "Recruiter"): ["Bob"],
#   ("IT", "Manager"): ["John"]
# }

val_dict={}
res_dict={}
for elem in records:
    roles=[]
    for k,v in elem.items():
        if k in ('department','role'):
            roles.append(v)
            res_dict[elem['name']]=roles 
# print(res_dict)
value_set_list=[]
for k,v in res_dict.items():
    if v not in value_set_list:
        value_set_list.append(v)
        val_dict[tuple(v)]=[k]
    else:
        val_dict.get(tuple(v)).append(k)
print(val_dict,end='\n')  