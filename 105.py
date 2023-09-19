class Library:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def boook(self):
        list_book = []
        for i in range (self.a):
            book = input("Name of book:\n")
            list_book.append(book)
        result = ", ".join(list_book)
        return result
b = input("Give a library name:\n")
a = int(input("How many book you neet to add:\n"))
Library = Library(a,b)
print(f"Books in {Library.b} Library: {Library.boook()}")