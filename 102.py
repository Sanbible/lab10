a = int(input("Give a width:\n"))
b = int(input("Give a height:\n"))

class Rectangle:
    def __init__(self,a,b):
        self.width = a
        self.height = b
    def calculate(self):
        ans = self.width*self.height
        return ans
    def Perimeter(self):
        ans2 = (self.width+self.height)*2
        return ans2

callas= Rectangle(a,b)
area = callas.calculate()
print(f'Area: {area}')
per = callas.Perimeter()
print(f"Perimeter: {per}")