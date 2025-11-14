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


result = deque()
for elem in employees:
    inserted = False
    for i in range(len(result)):
        if elem['salary'] >= result[i]['salary']:
            result.insert(i, elem)
            inserted = True
            break
        elif elem['salary']==result[i]['salary']:
            if ord(elem['name'][0])>ord(result[i]['name']):
                result.insert(i,elem)
                inserted=True
            else:
                result.append(elem)
                inserted=True
    if not inserted:
        result.append(elem)


print(result)