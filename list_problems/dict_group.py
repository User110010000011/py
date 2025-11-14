age={'John': 45, 'Alice': 80, 'Bob': 60,'Kat':55}
res=lambda age:{k:v for k,v in age.items() if v>50}
print(res(age))