# Invert Multi-Value Dictionary
# Problem:
# Given:
courses = {
    "Python": ["Alice", "Bob"],
    "Java": ["Bob", "Charlie"],
    "C++": ["Alice"]
}
result_dict={}
visited=set()
for k,v in courses.items():
    arr=[]
    for key in v:
        arr.append(key)
        result_dict[k]=arr
print(result_dict)
