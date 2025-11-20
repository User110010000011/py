
# Sort a list of employees , then by salary descending, and finally by name ascending.

# Sort a list of employees , then by salary descending, and finally by name ascending.4

def getpos(emp_val,res):
    """v"""
    for i,value in enumerate(res):
        if value['salary']==emp_val:
            return i

employees = [
    {"name": "Alice", "dept": "Sales", "salary": 70000},
    {"name": "Bob", "dept": "HR", "salary": 40000},
    {"name": "Charlie", "dept": "Sales", "salary": 80000},
    {"name": "David", "dept": "HR", "salary": 50000},
    {"name": "Charlie", "dept": "Sales", "salary": 60000},
    {"name": "Ben Tennyson", "dept": "Sales", "salary": 60000},
    {"name": "Azmuth", "dept": "Sales", "salary": 60000},
    {"name": "Barlie", "dept": "Sales", "salary": 80000},
    {"name": "Barlie", "dept": "Sales", "salary": 70000},
    {"name": "Arno", "dept": "Sales", "salary": 70000},
    {"name": "Shepherd", "dept": "commander", "salary": 1000000}
]
result = []
new_dict={}
visited=set()
pos=0
for idx,val in enumerate(employees):
    new_dict[idx]=val['salary']
new_dict=sorted(new_dict,key=lambda x:new_dict[x],reverse=True)
# print(new_dict)
for idx ,val in enumerate(employees):
    if employees[new_dict[idx]]['salary'] not in visited:
        result.append(employees[new_dict[idx]])
        visited.add(employees[new_dict[idx]]['salary'])
    else: 
        pos=getpos(employees[new_dict[idx]]['salary'],result)
        result.insert(pos,employees[new_dict[idx]])
        # print(pos)
        # new_arr=sorted(new_arr,key=lambda x:x['name'])
# print(new_arr,pos)
print(result)
