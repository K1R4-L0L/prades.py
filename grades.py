names = ["Maya", "JP","Erica","Vincent"]
grades = [100,99,98,80]
#acessing names using a for loop in a list 
#names is a variable only used in a list 
print(f"{names[0]}'s grade is {grades[0]}")

for i in range(len(names)):
    print(f" { names[i]}grade is{ grades[i]}")
