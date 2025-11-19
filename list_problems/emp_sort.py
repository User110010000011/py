from collections import deque
# Sort a list of employees , then by salary descending, and finally by name ascending.
employees = [
    {"name": "Alice", "dept": "Sales", "salary": 70000},
    {"name": "Bob", "dept": "HR", "salary": 40000},
    {"name": "Charlie", "dept": "Sales", "salary": 80000},
    {"name": "David", "dept": "HR", "salary": 50000},
    {"name": "Charlie", "dept": "Sales", "salary": 60000},
    {"name": "Ben10", "dept": "Sales", "salary": 60000},
    {"name": "Azmuth", "dept": "Sales", "salary": 60000}
]


result = []
new_dict={}
for idx,val in enumerate(employees):
    new_dict[idx]=val['salary']
new_dict=sorted(new_dict,key=lambda x:new_dict[x],reverse=True)
for idx ,val in enumerate(employees):
    result.append(employees[new_dict[idx]])
print(result)

#git revert check