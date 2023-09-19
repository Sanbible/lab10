class Student:
    def __init__(self,name,mark):
        self.n=name
        self.m=mark
    
a = input("Enter student name:\n")
b = float(input("Enter student marks:\n"))
Student=Student(a,b)
print("Original Student Name:",Student.n)
print("Original Marks:",Student.m)
new_a = input("Enter new student name:\n")
new_b = float(input("Enter new student marks:\n"))
Student.n=new_a
Student.m=new_b
print("Modified Student Name:",Student.n)
print("Modified Marks:",Student.m)

