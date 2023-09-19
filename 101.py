x = float(input("Enter the base (x):\n"))
n = int(input("Enter the exponent (n):\n"))
def calculate_power(x,n):
    ans =  x**n
    return ans
print(f"{x}^{n} = {calculate_power(x,n)}")
