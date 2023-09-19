a = str(input("Name of student:\n"))
b = [int(b) for b in input("Enter the grade with space:\n").split()]
class Student: 
    def __init__(self,a,b):
        self.b = b
        self.a= a
    def calculate(self):
        aver = sum(self.b)
        aver = aver / len(self.b)
        return aver
Callas = Student(a,b)
aves = Callas.calculate()
print(f'Average Grade: {aves}')