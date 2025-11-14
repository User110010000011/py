employees = [
    {"id": 101, "name": "Alice"},
    {"id": 102, "name": "Bob"},
    {"id": 101, "name": "Alice"},
    {"id": 103, "name": "Eve"}
]

set_check=set()
res_list=[]
for elem in employees:
    if elem['id'] not in set_check:
        set_check.add(elem['id'])
    else:
        res_list.append(elem)
# print(list(set(employees)))
print(res_list)